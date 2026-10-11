"""QLoRA fine-tuning of IBM Granite 4.1 8B on the credit-rating training pairs.

Teaches the offline model to answer the rate_engine prompt the way the delivered rationales do.
Each sample is (system + verified-ratio prompt) -> JSON rating view. The loss is computed on the
ANSWER only, so the model is not trained to reproduce the prompt.

Prerequisites (run once):
    pip install torch transformers peft accelerate
    pip install bitsandbytes          # NVIDIA GPU, for 4-bit QLoRA
    pip install unsloth               # optional, faster on an NVIDIA GPU

Usage:
    python tools/build_finetune_data.py            # writes finetune/train.jsonl
    python tools/finetune.py --max-steps 50        # short test run
    python tools/finetune.py                       # full run (3 epochs)
    python tools/finetune.py --base-model HuggingFaceTB/SmolLM2-135M-Instruct --max-steps 2   # 1-minute CPU smoke test

Output:
    models/granite-4.1-8b-lora/   (LoRA adapter, a few hundred MB)
Then run:  python tools/export_gguf.py   to merge the adapter and make a GGUF the tool can use.

Hardware: an NVIDIA GPU with 12+ GB VRAM (16-24 GB recommended) for the 8B model. CPU-only runs work
only for tiny models (the smoke test above); an 8B model on CPU is impractical.
The default base model, ibm-granite/granite-4.1-8b, is public (Apache-2.0); no token is needed.
"""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRAIN_FILE = ROOT / "finetune" / "train.jsonl"
OUT_DIR = ROOT / "models" / "granite-4.1-8b-lora"
BASE_MODEL = "ibm-granite/granite-4.1-8b"
LORA_TARGETS = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
MAX_LEN = 6144  # tokens; 4096 would drop 21% of the samples, 8192 keeps all (needs ~24 GB VRAM)


def _check_deps():
    missing = []
    for pkg in ("torch", "transformers", "peft", "accelerate"):
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    if missing:
        print("Missing packages:", ", ".join(missing))
        print("Install with:  pip install", " ".join(missing), "(plus bitsandbytes for 4-bit on a GPU)")
        sys.exit(1)


def _encode(sample, tokenizer):
    """Tokenise one chat sample; labels are -100 everywhere except the assistant answer."""
    msgs = sample["messages"]
    prompt = tokenizer.apply_chat_template(msgs[:-1], tokenize=False, add_generation_prompt=True)
    full = tokenizer.apply_chat_template(msgs, tokenize=False)
    if not full.startswith(prompt):
        return None
    p_ids = tokenizer(prompt, add_special_tokens=False)["input_ids"]
    f_ids = tokenizer(full, add_special_tokens=False)["input_ids"]
    if len(f_ids) > MAX_LEN or len(p_ids) >= len(f_ids):
        return None
    return {"input_ids": f_ids, "attention_mask": [1] * len(f_ids),
            "labels": [-100] * len(p_ids) + f_ids[len(p_ids):]}


class _Rows:
    def __init__(self, rows):
        self.rows = rows

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, i):
        return self.rows[i]


def _load_rows(tokenizer):
    if not TRAIN_FILE.exists():
        print(f"Training data not found: {TRAIN_FILE}\nRun first:  python tools/build_finetune_data.py")
        sys.exit(1)
    samples = [json.loads(ln) for ln in open(TRAIN_FILE, encoding="utf-8") if ln.strip()]
    rows = [r for r in (_encode(s, tokenizer) for s in samples) if r]
    print(f"Loaded {len(samples)} samples; {len(rows)} usable "
          f"({len(samples) - len(rows)} dropped: longer than {MAX_LEN} tokens or template mismatch)")
    if not rows:
        sys.exit("No usable training rows.")
    return _Rows(rows)


def main():
    global MAX_LEN
    ap = argparse.ArgumentParser()
    ap.add_argument("--epochs", type=int, default=3)
    ap.add_argument("--lr", type=float, default=2e-4)
    ap.add_argument("--rank", type=int, default=16, help="LoRA rank")
    ap.add_argument("--batch", type=int, default=1)
    ap.add_argument("--grad-accum", type=int, default=8)
    ap.add_argument("--max-steps", type=int, default=-1, help="stop after N steps (50 for a test run)")
    ap.add_argument("--max-len", type=int, default=MAX_LEN, help="drop samples longer than this many tokens")
    ap.add_argument("--base-model", default=BASE_MODEL)
    ap.add_argument("--output", default=str(OUT_DIR))
    ap.add_argument("--no-4bit", action="store_true", help="disable 4-bit quantisation (needs more VRAM)")
    ap.add_argument("--hf-token", default=None, help="only for a gated/private --base-model (or set HF_TOKEN)")
    args = ap.parse_args()

    MAX_LEN = args.max_len
    _check_deps()
    import torch

    token = args.hf_token or os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
    if token:
        from huggingface_hub import login
        login(token=token, add_to_git_credential=False)

    cuda = torch.cuda.is_available()
    use_4bit = cuda and not args.no_4bit
    bf16 = cuda and torch.cuda.is_bf16_supported()
    print(f"Device: {'cuda' if cuda else 'cpu'}  |  4-bit: {use_4bit}  |  precision: {'bf16' if bf16 else 'fp16' if cuda else 'fp32'}")

    use_unsloth = False
    if cuda:
        try:
            import unsloth  # noqa: F401
            use_unsloth = True
            print("Using unsloth")
        except ImportError:
            pass

    if use_unsloth:
        from unsloth import FastLanguageModel
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=args.base_model, max_seq_length=MAX_LEN, dtype=None, load_in_4bit=use_4bit)
        model = FastLanguageModel.get_peft_model(
            model, r=args.rank, target_modules=LORA_TARGETS, lora_alpha=args.rank * 2, lora_dropout=0.05,
            bias="none", use_gradient_checkpointing="unsloth", random_state=42)
    else:
        from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
        from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
        tokenizer = AutoTokenizer.from_pretrained(args.base_model)
        compute = torch.bfloat16 if bf16 else torch.float16
        bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=compute,
                                 bnb_4bit_use_double_quant=True) if use_4bit else None
        model = AutoModelForCausalLM.from_pretrained(
            args.base_model, quantization_config=bnb, device_map="auto" if cuda else None,
            dtype=compute if cuda else torch.float32)
        if use_4bit:
            model = prepare_model_for_kbit_training(model)
        model = get_peft_model(model, LoraConfig(
            r=args.rank, lora_alpha=args.rank * 2, target_modules=LORA_TARGETS, lora_dropout=0.05,
            bias="none", task_type="CAUSAL_LM"))
        model.print_trainable_parameters()

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    rows = _load_rows(tokenizer)

    from transformers import DataCollatorForSeq2Seq, Trainer, TrainingArguments
    targs = TrainingArguments(
        output_dir=args.output, num_train_epochs=args.epochs, per_device_train_batch_size=args.batch,
        gradient_accumulation_steps=args.grad_accum, learning_rate=args.lr, bf16=bf16, fp16=cuda and not bf16,
        logging_steps=5, save_strategy="no", warmup_steps=0.05, lr_scheduler_type="cosine",
        max_steps=args.max_steps, report_to="none", remove_unused_columns=False, dataloader_num_workers=0,
        optim="paged_adamw_8bit" if use_4bit else "adamw_torch")
    trainer = Trainer(model=model, args=targs, train_dataset=rows,
                      data_collator=DataCollatorForSeq2Seq(tokenizer, padding=True, label_pad_token_id=-100))
    print("\nStarting training ...")
    trainer.train()

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(str(out))
    tokenizer.save_pretrained(str(out))
    print(f"\nLoRA adapter saved to {out}\nNext step: python tools/export_gguf.py")


if __name__ == "__main__":
    main()
