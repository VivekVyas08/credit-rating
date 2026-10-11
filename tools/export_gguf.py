"""Merge LoRA adapter into base model and export to GGUF (Q4_K_M).

The resulting GGUF is a drop-in replacement for the current
models/granite-4.1-8b-Q4_K_M.gguf: rate_engine.py will auto-prefer it.

Steps:
  1. Merge the LoRA adapter (models/granite-4.1-8b-lora/) into the base model
  2. Save the merged weights to models/granite-4.1-8b-merged/
  3. Clone llama.cpp (if not already present) and build its converter
  4. Convert merged weights to GGUF  (F16 first, then quantize to Q4_K_M)
  5. Place final GGUF at models/granite-4.1-8b-finetuned.gguf (rate_engine.py prefers *finetuned*.gguf)

Usage:
    python tools/export_gguf.py
    python tools/export_gguf.py --lora models/granite-4.1-8b-lora --out models/my.gguf

Requirements:
    pip install transformers peft
    git, cmake, make (or Visual Studio on Windows for llama.cpp build)
    ~30 GB free disk space during conversion
"""
import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LORA_DIR = ROOT / "models" / "granite-4.1-8b-lora"
MERGED_DIR = ROOT / "models" / "granite-4.1-8b-merged"
LLAMACPP_DIR = ROOT / "models" / "llama.cpp"
OUT_GGUF = ROOT / "models" / "granite-4.1-8b-finetuned.gguf"
BASE_MODEL = "ibm-granite/granite-4.1-8b"


def _run(cmd, cwd=None, check=True):
    print("$", " ".join(str(c) for c in cmd))
    result = subprocess.run([str(c) for c in cmd], cwd=cwd, check=check)
    return result


def merge_lora(lora_dir, base_model, merged_dir):
    """Merge LoRA weights into the base model and save full weights."""
    print("\n-- Step 1/4: Merging LoRA adapter --")
    try:
        from peft import PeftModel
        from transformers import AutoModelForCausalLM, AutoTokenizer
        import torch
    except ImportError:
        print("Missing: pip install transformers peft torch")
        sys.exit(1)

    print(f"Loading base model {base_model} ...")
    model = AutoModelForCausalLM.from_pretrained(
        base_model,
        dtype=torch.float16,
        device_map="cpu",
        trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)

    print(f"Loading LoRA from {lora_dir} ...")
    model = PeftModel.from_pretrained(model, str(lora_dir))

    print("Merging weights ...")
    model = model.merge_and_unload()

    merged_dir = Path(merged_dir)
    merged_dir.mkdir(parents=True, exist_ok=True)
    print(f"Saving merged model to {merged_dir} ...")
    model.save_pretrained(str(merged_dir), safe_serialization=True)
    tokenizer.save_pretrained(str(merged_dir))
    print("Merge done.")


def clone_llamacpp():
    """Clone llama.cpp repo if not already present."""
    if LLAMACPP_DIR.exists():
        print(f"\nllama.cpp already at {LLAMACPP_DIR} - skipping clone")
        return
    print("\n-- Step 2/4: Cloning llama.cpp --")
    _run(["git", "clone", "--depth", "1",
          "https://github.com/ggerganov/llama.cpp.git",
          str(LLAMACPP_DIR)])


def build_llamacpp():
    """Build llama.cpp convert script dependencies."""
    print("\n-- Step 3/4: Installing llama.cpp Python deps --")
    req = LLAMACPP_DIR / "requirements.txt"
    if req.exists():
        _run([sys.executable, "-m", "pip", "install", "-r", str(req)])
    else:
        _run([sys.executable, "-m", "pip", "install", "gguf", "sentencepiece"])


def convert_to_gguf(merged_dir, out_gguf):
    """Convert HuggingFace weights -> F16 GGUF -> Q4_K_M GGUF."""
    print("\n-- Step 4/4: Converting to GGUF --")
    convert_script = LLAMACPP_DIR / "convert_hf_to_gguf.py"
    if not convert_script.exists():
        # Older llama.cpp used convert.py
        convert_script = LLAMACPP_DIR / "convert.py"
    if not convert_script.exists():
        print(f"ERROR: convert script not found in {LLAMACPP_DIR}")
        print("Try: pip install gguf  then  python llama.cpp/convert_hf_to_gguf.py ...")
        sys.exit(1)

    f16_gguf = Path(out_gguf).with_suffix(".f16.gguf")

    # Convert to F16 first
    _run([sys.executable, str(convert_script),
          str(merged_dir),
          "--outfile", str(f16_gguf),
          "--outtype", "f16"])

    # Quantize to Q4_K_M
    quantize_bin = LLAMACPP_DIR / "build" / "bin" / "llama-quantize"
    if not quantize_bin.exists():
        quantize_bin = LLAMACPP_DIR / "build" / "bin" / "quantize"  # older name
    if not quantize_bin.exists():
        print(f"\nllama-quantize binary not found at {quantize_bin}")
        print("Either build llama.cpp (cmake . && make) or use the Python gguf-convert:")
        print(f"  The F16 GGUF is at {f16_gguf}")
        print("  Rename it to use as-is (larger, ~15 GB), or build llama.cpp and quantize manually:")
        print(f"    ./llama-quantize {f16_gguf} {out_gguf} Q4_K_M")
        return False

    _run([str(quantize_bin), str(f16_gguf), str(out_gguf), "Q4_K_M"])

    # Clean up F16 intermediate
    if Path(f16_gguf).exists():
        print(f"Removing intermediate {f16_gguf}")
        os.remove(f16_gguf)

    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lora", default=str(LORA_DIR))
    parser.add_argument("--base-model", default=BASE_MODEL)
    parser.add_argument("--merged", default=str(MERGED_DIR))
    parser.add_argument("--out", default=str(OUT_GGUF))
    parser.add_argument("--skip-merge", action="store_true",
                        help="Skip merge step if merged/ already exists")
    args = parser.parse_args()

    lora_dir = Path(args.lora)
    if not lora_dir.exists():
        print(f"LoRA adapter not found: {lora_dir}")
        print("Run training first:  python tools/finetune.py")
        sys.exit(1)

    if not args.skip_merge:
        merge_lora(lora_dir, args.base_model, args.merged)
    else:
        print(f"Skipping merge (--skip-merge); using {args.merged}")

    clone_llamacpp()
    build_llamacpp()
    ok = convert_to_gguf(args.merged, args.out)
    if ok:
        print(f"\nOK Fine-tuned GGUF: {args.out}")
        print("rate_engine.py prefers any models/*finetuned*.gguf automatically; no other change is needed.")
    else:
        print("\nConversion to Q4_K_M incomplete - F16 GGUF is still usable.")


if __name__ == "__main__":
    main()
