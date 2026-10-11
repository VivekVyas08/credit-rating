"""QLoRA fine-tuning of IBM Granite 4.1 8B Instruct on credit-rating training data.

Prerequisites (run once):
    pip install torch transformers peft trl datasets accelerate bitsandbytes
    # Optional but 2-3x faster on GPU:
    pip install unsloth

Usage:
    python tools/finetune.py
    python tools/finetune.py --epochs 5 --lr 1e-4 --rank 32

Output:
    models/granite-4.1-8b-lora/   (LoRA adapter; ~300 MB)

After training run export_gguf.py to merge + quantize back to GGUF.

Hardware:
    - Minimum: 12 GB VRAM (NVIDIA) with 4-bit quantization (default)
    - Recommended: 16-24 GB VRAM
    - CPU-only: works but takes hours per epoch — use --max-steps 50 to test
"""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRAIN_FILE = ROOT / "finetune" / "train.jsonl"
OUT_DIR = ROOT / "models" / "granite-4.1-8b-lora"
BASE_MODEL = "ibm-granite/granite-4.1-8b-instruct"


def _check_deps():
    missing = []
    for pkg in ("torch", "transformers", "peft", "trl", "datasets", "accelerate"):
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    if missing:
        print("Missing packages:", ", ".join(missing))
        print("Install with:  pip install", " ".join(missing), "bitsandbytes")
        sys.exit(1)


def _load_dataset():
    from datasets import Dataset
    if not TRAIN_FILE.exists():
        print(f"Training data not found: {TRAIN_FILE}")
        print("Run first:  python tools/build_finetune_data.py")
        sys.exit(1)
    rows = [json.loads(ln) for ln in open(TRAIN_FILE, encoding="utf-8")]
    print(f"Loaded {len(rows)} training samples from {TRAIN_FILE}")
    return Dataset.from_list(rows)


def _make_text(sample, tokenizer):
    """Convert messages list to the model's chat-template string."""
    return tokenizer.apply_chat_template(
        sample["messages"],
        tokenize=False,
        add_generation_prompt=False,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--lr", type=float, default=2e-4)
    parser.add_argument("--rank", type=int, default=16, help="LoRA rank")
    parser.add_argument("--batch", type=int, default=1)
    parser.add_argument("--grad-accum", type=int, default=8)
    parser.add_argument("--max-steps", type=int, default=-1,
                        help="Limit steps (use 50 to test CPU mode)")
    parser.add_argument("--base-model", default=BASE_MODEL)
    parser.add_argument("--output", default=str(OUT_DIR))
    parser.add_argument("--no-4bit", action="store_true",
                        help="Disable 4-bit quantization (needs more VRAM)")
    parser.add_argument("--hf-token", default=None,
                        help="HuggingFace token (or set HF_TOKEN env var)")
    args = parser.parse_args()

    _check_deps()

    # HuggingFace auth — needed for gated models like IBM Granite
    hf_token = args.hf_token or os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
    if hf_token:
        try:
            from huggingface_hub import login as hf_login
            hf_login(token=hf_token, add_to_git_credential=False)
            print("HuggingFace login OK")
        except Exception as e:
            print(f"HuggingFace login failed: {e}")
    else:
        print("No HF token supplied — assuming already logged in via `huggingface-cli login`")

    import torch
    device = "cuda" if torch.cuda.is_available() else "cpu"
    use_4bit = (device == "cuda") and not args.no_4bit
    print(f"Device: {device}  |  4-bit quant: {use_4bit}")

    # Try unsloth first (faster on GPU), fall back to standard stack
    _use_unsloth = False
    if device == "cuda":
        try:
            import unsloth  # noqa: F401
            _use_unsloth = True
            print("Using unsloth for faster training")
        except ImportError:
            print("unsloth not installed — using standard transformers+peft")

    # ── Load base model ──────────────────────────────────────────────────────
    if _use_unsloth:
        from unsloth import FastLanguageModel
        model, tokenizer = FastLanguageModel.from_pretrained(
            model_name=args.base_model,
            max_seq_length=4096,
            dtype=None,
            load_in_4bit=use_4bit,
        )
        model = FastLanguageModel.get_peft_model(
            model,
            r=args.rank,
            target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                            "gate_proj", "up_proj", "down_proj"],
            lora_alpha=args.rank * 2,
            lora_dropout=0.05,
            bias="none",
            use_gradient_checkpointing="unsloth",
            random_state=42,
        )
    else:
        from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
        from peft import LoraConfig, get_peft_model

        tokenizer = AutoTokenizer.from_pretrained(args.base_model, trust_remote_code=True)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        bnb_config = None
        if use_4bit:
            bnb_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
            )

        model = AutoModelForCausalLM.from_pretrained(
            args.base_model,
            quantization_config=bnb_config,
            device_map="auto" if device == "cuda" else None,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            trust_remote_code=True,
        )

        lora_config = LoraConfig(
            r=args.rank,
            lora_alpha=args.rank * 2,
            target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM",
        )
        model = get_peft_model(model, lora_config)
        model.print_trainable_parameters()

    # ── Dataset ──────────────────────────────────────────────────────────────
    raw = _load_dataset()

    def _fmt(batch):
        return {"text": [_make_text({"messages": m}, tokenizer) for m in batch["messages"]]}

    dataset = raw.map(_fmt, batched=True, remove_columns=raw.column_names)

    # ── Trainer ──────────────────────────────────────────────────────────────
    from trl import SFTTrainer
    from transformers import TrainingArguments

    training_args = TrainingArguments(
        output_dir=args.output,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch,
        gradient_accumulation_steps=args.grad_accum,
        learning_rate=args.lr,
        fp16=(device == "cuda"),
        bf16=False,
        logging_steps=10,
        save_strategy="epoch",
        save_total_limit=2,
        warmup_ratio=0.05,
        lr_scheduler_type="cosine",
        max_steps=args.max_steps if args.max_steps > 0 else -1,
        report_to="none",
        optim="paged_adamw_8bit" if use_4bit else "adamw_torch",
        dataloader_num_workers=0,
    )

    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=dataset,
        dataset_text_field="text",
        max_seq_length=4096,
        args=training_args,
    )

    print("\nStarting training …")
    trainer.train()

    # ── Save ─────────────────────────────────────────────────────────────────
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    if _use_unsloth:
        model.save_pretrained(str(out))
        tokenizer.save_pretrained(str(out))
    else:
        trainer.save_model(str(out))
        tokenizer.save_pretrained(str(out))

    print(f"\nLoRA adapter saved to {out}")
    print("Next step: python tools/export_gguf.py")


if __name__ == "__main__":
    main()
