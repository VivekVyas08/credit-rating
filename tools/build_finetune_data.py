"""Build fine-tuning training data from the 33 delivered rating cases.

Each case that has BOTH a compute_ratios.py (ratio engine) AND a *Rationale*.md (ground truth)
becomes one training sample:
  - INPUT  : the exact prompt build_prompt() would send to the model
  - OUTPUT : a JSON object matching SCHEMA, parsed from the delivered rationale

Output: finetune/train.jsonl  (chat-template format for SFTTrainer)
        finetune/train_stats.txt (per-case summary and any parse warnings)

Run:
    python tools/build_finetune_data.py [--augment N]   # N=augmentation multiplier, default 3
"""
import argparse
import glob
import importlib.util
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from rate_engine import build_prompt, SYSTEM, SCHEMA  # noqa: E402

OUT_DIR = ROOT / "finetune"
OUT_DIR.mkdir(exist_ok=True)
COMPANIES = ROOT / "Companies"

# ──────────────────────────────────────────────────────────────────────────────
# Grade-parsing helpers (handles ICRA, CRISIL, CareEdge formats)
# ──────────────────────────────────────────────────────────────────────────────

# LT grade patterns: AA+, AA, AA-, A+, A, A-, BBB+, BBB, BBB-, BB+, BB, BB-, B+, B, B-, C+, C, C-
_LT_RE = re.compile(
    r"\b(AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?|C[+-]?|D)\b"
)
# ST grade patterns: A1+, A1, A2+, A2, A3+, A3, A4+, A4
_ST_RE = re.compile(
    r"\b(A1\+|A1|A2\+|A2|A3\+|A3|A4\+|A4)\b"
)
_OUTLOOK_RE = re.compile(
    r"\b(Stable|Positive|Negative|Not applicable|Watch)\b", re.I
)


def _parse_grades_from_table(text):
    """Extract (lt_grade, outlook, st_grade) from the rating action / summary table."""
    lt_grade = ""
    outlook = "Stable"
    st_grade = ""

    # Walk every table cell that contains a grade keyword
    for line in text.splitlines():
        if "|" not in line:
            continue
        cells = [c.strip() for c in line.split("|")]
        for cell in cells:
            # Skip header cells
            if re.search(r"instrument|amount|action|rating action|facility", cell, re.I):
                continue
            # CRISIL format: "Crisil AAA/Stable" or "Crisil A1+"
            crisil = re.search(r"Crisil\s+([A-Z0-9+]+)[/;, ]+([Ss]table|[Pp]ositive|[Nn]egative)", cell)
            if crisil:
                lt_grade = lt_grade or crisil.group(1)
                outlook = crisil.group(2).capitalize()
                continue
            crisil_st = re.search(r"Crisil\s+(A[1-4]\+?)\b", cell)
            if crisil_st and not lt_grade:
                st_grade = st_grade or crisil_st.group(1)
            # ICRA format: "[ICRA]AA+ (Stable)" or "[ICRA]A1+"
            icra = re.search(r"\[ICRA\]([A-Z0-9+\-]+)\s*\(([Ss]table|[Pp]ositive|[Nn]egative)\)", cell)
            if icra:
                lt_grade = lt_grade or icra.group(1)
                outlook = icra.group(2).capitalize()
                continue
            icra_st = re.search(r"\[ICRA\](A[1-4]\+?)(?:[;\s,|]|$)", cell)
            if icra_st:
                st_grade = st_grade or icra_st.group(1)
            # CareEdge format: "CARE AA-; Stable" or "CARE A1+"
            care = re.search(r"CARE\s+([A-Z0-9+\-]+)\s*[;,]\s*([Ss]table|[Pp]ositive|[Nn]egative)", cell)
            if care:
                lt_grade = lt_grade or care.group(1)
                outlook = care.group(2).capitalize()
                continue
            care_st = re.search(r"CARE\s+(A[1-4]\+?)(?:[;\s,|]|$)", cell)
            if care_st:
                st_grade = st_grade or care_st.group(1)

    # Fallback: scan entire text for first LT grade + outlook
    if not lt_grade:
        # Look for patterns in the header/title line
        header_match = re.search(
            r"(Crisil|CARE|ICRA)[^'\n]{0,10}['\"]?\s*"
            r"(AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?)[/;, ]*"
            r"([Ss]table|[Pp]ositive|[Nn]egative)?",
            text[:2000],
        )
        if header_match:
            lt_grade = header_match.group(2)
            if header_match.group(3):
                outlook = header_match.group(3).capitalize()

    # Outlook from "(Stable)" anywhere in first 3000 chars if not yet found
    if not outlook or outlook == "Stable":
        om = _OUTLOOK_RE.search(text[:3000])
        if om:
            outlook = om.group(1).capitalize()

    # Derive ST from LT if not found
    if not st_grade and lt_grade:
        _st_map = {
            "AAA": "A1+", "AA+": "A1+", "AA": "A1+", "AA-": "A1+",
            "A+": "A1+", "A": "A1", "A-": "A2+",
            "BBB+": "A2", "BBB": "A3+", "BBB-": "A3",
            "BB+": "A4+", "BB": "A4", "BB-": "A4",
            "B+": "A4", "B": "A4", "B-": "A4",
        }
        st_grade = _st_map.get(lt_grade, "A4")

    return lt_grade, outlook, st_grade


# ──────────────────────────────────────────────────────────────────────────────
# Section extractors
# ──────────────────────────────────────────────────────────────────────────────

def _extract_section(text, header_re, stop_re=None):
    """Return the text between a section header and the next same-level header."""
    m = re.search(header_re, text, re.I | re.M)
    if not m:
        return ""
    start = m.end()
    if stop_re:
        e = re.search(stop_re, text[start:], re.I | re.M)
        return text[start:start + e.start()].strip() if e else text[start:].strip()
    # Default stop: next ## or ### header
    e = re.search(r"^#{2,3}\s+\S", text[start:], re.M)
    return text[start:start + e.start()].strip() if e else text[start:].strip()


def _extract_bold_bullets(section_text):
    """Extract the bold headline from each bullet/paragraph in a section.

    Handles:
      **Headline text** — some body text
      - **Headline text**: body text
      **Headline text**\n\nbody text
    """
    results = []
    seen = set()
    for m in re.finditer(r"\*\*(.+?)\*\*", section_text):
        h = m.group(1).strip()
        # Skip short markers, table markers, or agency prefixes
        if len(h) < 8:
            continue
        if re.match(r"(Total|Rating|Note|Source|Positive|Negative|Credit|Key|Environmental|Liquidity"
                    r"|Analytical|About|Status|Any other|Complexity|Annexure)", h, re.I):
            continue
        # De-duplicate (same headline can appear as section title + first bullet)
        key = h.lower()[:40]
        if key in seen:
            continue
        seen.add(key)
        results.append(h)
    return results


def _extract_reasoning(text):
    """Pull the ## Rationale / ## Rationale and key rating drivers section."""
    body = _extract_section(
        text,
        r"^#{1,2}\s+\*?\*?Rationale\b",
        r"^#{2,3}\s+(Key rating|Credit strength|Environmental|Liquidity|Rating sens|About|Analytical)",
    )
    if not body:
        # Try inline rationale (CRISIL format sometimes has inline)
        body = _extract_section(text, r"## \*\*Rationale", r"^## ")
    # Truncate to ~2000 chars — the model shouldn't memorise very long texts
    return body[:2000].strip()


def _extract_monitorable(text):
    """Pull the first negative sensitivity as the principal monitorable."""
    sens = _extract_section(text, r"^#{2,3}\s+Rating sensitivities")
    if not sens:
        return "See rating sensitivities section."

    # Format 1: inline paragraph after **Negative factors** –
    neg_inline = re.search(
        r"\*\*Negative factors?\*\*\s*[–—-]\s*(.+?)(?=\n\n|\Z)",
        sens, re.S | re.I
    )
    if neg_inline:
        raw = neg_inline.group(1).replace("\n", " ").strip()
        # Take first sentence (up to first full stop that ends a clause)
        first = re.split(r"\.\s+", raw)[0].strip()
        return (first + ".")[:250]

    # Format 2: bulleted negative factors
    neg_m = re.search(r"\*\*Negative factors?\*\*", sens, re.I)
    if neg_m:
        rest = sens[neg_m.end():]
        bullet = re.search(r"[-*]\s*\*\*(.+?)\*\*", rest)
        if bullet:
            return bullet.group(1).strip()
        # plain first sentence
        first_sent = re.search(r"[A-Z][^.]{10,}[.]", rest)
        if first_sent:
            return first_sent.group(0)[:250]

    return "See rating sensitivities section."


# ──────────────────────────────────────────────────────────────────────────────
# Per-case loading
# ──────────────────────────────────────────────────────────────────────────────

def _load_case(slug):
    """Return (mod, R, meta, n_tieouts) or raise."""
    case_dir = COMPANIES / slug
    spec = importlib.util.spec_from_file_location(
        f"cr_{slug}", case_dir / "compute_ratios.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    R = mod.compute()
    n_tieouts = len(getattr(mod, "TIEOUTS", []))
    meta = json.loads((case_dir / "case.json").read_text(encoding="utf-8"))

    # Some cases return R = {'standalone': {FY…: {…}}, 'consolidated': {FY…: {…}}}
    # Flatten to the period-keyed sub-dict that build_prompt expects (mod.YEARS keys at top level)
    years = getattr(mod, "YEARS", None)
    if years and isinstance(R, dict) and years[0] not in R:
        basis = meta.get("basis", "consolidated").lower()
        if basis in R:
            R = R[basis]
        elif "consolidated" in R:
            R = R["consolidated"]
        elif "standalone" in R:
            R = R["standalone"]
        else:
            # Some scripts return {metric: {year: val}} — transpose to {year: {metric: val}}
            # Others return {metric: [val0, val1, …]} parallel to mod.YEARS
            first_val = next(iter(R.values()), None)
            if isinstance(first_val, dict):
                transposed: dict = {}
                for metric, yr_dict in R.items():
                    for yr, val in yr_dict.items():
                        transposed.setdefault(yr, {})[metric] = val
                R = transposed
            elif isinstance(first_val, list) and years and len(first_val) == len(years):
                transposed = {}
                for metric, vals in R.items():
                    for yr, val in zip(years, vals):
                        transposed.setdefault(yr, {})[metric] = val
                R = transposed

    # Filter YEARS to only periods present in R (handles data gaps like a missing projected year)
    if years:
        present = [y for y in years if y in R]
        if present and len(present) < len(years):
            mod.YEARS = present

    return mod, R, meta, n_tieouts


def _parse_rationale(slug):
    """Return the structured expected output dict from the delivered rationale."""
    case_dir = COMPANIES / slug
    files = sorted(glob.glob(str(case_dir / "*Rationale*.md")))
    if not files:
        raise FileNotFoundError(f"No rationale for {slug}")
    text = open(files[0], encoding="utf-8", errors="replace").read()

    lt_grade, outlook, st_grade = _parse_grades_from_table(text)

    # Handles: "### Credit strengths", "## **Credit strengths**",
    # "### **Key Rating Drivers - Strengths**", "### Key Rating Drivers - Strengths"
    strengths_sec = _extract_section(
        text,
        r"^#{2,3}\s+\*{0,2}(Credit strengths?|Key Rating Drivers\s*[-–]\s*Strengths)\b",
        r"^#{2,3}\s+\*{0,2}(Credit challenges?|Key Rating Drivers\s*[-–]\s*Weak|Environmental|Liquidity|Rating)",
    )
    weaknesses_sec = _extract_section(
        text,
        r"^#{2,3}\s+\*{0,2}(Credit challenges?|Key Rating Drivers\s*[-–]\s*Weak)",
        r"^#{2,3}\s+\*{0,2}(Environmental|Liquidity|Rating|Analytical|About|Brief Financials)",
    )

    # For CareEdge / CRISIL-inline: drivers are standalone ### headings or **bold** paragraphs
    # embedded directly in the rationale section with no parent grouping header.
    # Collect all ### heading text between rationale and sensitivities as drivers.
    if not strengths_sec and not weaknesses_sec:
        rat_end = re.search(
            r"^#{2,3}\s+\*{0,2}(Rating sensitivities?|Analytical approach|About|Brief Financials)",
            text, re.M | re.I
        )
        rat_start = re.search(r"^#{1,3}\s+\*{0,2}(Rationale|Detailed Rationale)", text, re.M | re.I)
        if rat_start and rat_end:
            driver_block = text[rat_start.end():rat_end.start()]
            # Collect ### subheading lines as driver titles
            driver_titles = re.findall(r"^#{3}\s+\*{0,2}(.+?)\*{0,2}\s*$", driver_block, re.M)
            # Heuristic: bold-dash paragraphs (CRISIL inline style)
            driver_titles += re.findall(r"^\*\*(.{15,100}?)\*\*(?:\s+[–—-]|\s*\n)", driver_block, re.M)
            # Split roughly in half: first half = strengths, second half = weaknesses
            mid = max(1, len(driver_titles) // 2)
            strengths_sec = "\n".join(f"**{t}**" for t in driver_titles[:mid])
            weaknesses_sec = "\n".join(f"**{t}**" for t in driver_titles[mid:])

    strengths = _extract_bold_bullets(strengths_sec)
    weaknesses = _extract_bold_bullets(weaknesses_sec)
    reasoning = _extract_reasoning(text)
    monitorable = _extract_monitorable(text)

    return {
        "long_term_grade": lt_grade,
        "outlook": outlook if outlook in ("Stable", "Positive", "Negative", "Not applicable") else "Stable",
        "short_term_grade": st_grade,
        "key_strengths": strengths[:6],      # cap at 6
        "key_weaknesses": weaknesses[:6],
        "principal_monitorable": monitorable,
        "reasoning": reasoning,
        "confidence": "high",
        "data_limitations_considered": (
            "Training example: ground truth from delivered rationale. "
            "All verified ratio suite tie-outs passed before this case was delivered."
        ),
    }


# ──────────────────────────────────────────────────────────────────────────────
# Simple augmentations (shuffles + paraphrase-lite so we don't overfit 33 examples)
# ──────────────────────────────────────────────────────────────────────────────

def _augment(sample, seed):
    """Return a lightly varied copy of a sample dict for data augmentation."""
    import random
    rng = random.Random(seed)
    s = dict(sample)
    s["messages"] = list(sample["messages"])   # shallow copy

    # Shuffle strengths and weaknesses (model should still produce them in any order)
    assistant_obj = json.loads(s["messages"][-1]["content"])
    ks = list(assistant_obj["key_strengths"])
    kw = list(assistant_obj["key_weaknesses"])
    rng.shuffle(ks)
    rng.shuffle(kw)
    assistant_obj["key_strengths"] = ks
    assistant_obj["key_weaknesses"] = kw

    # Slightly vary confidence wording for one-in-three augmentations
    if seed % 3 == 1:
        assistant_obj["confidence"] = "high"
    elif seed % 3 == 2:
        assistant_obj["confidence"] = "medium"

    s["messages"][-1] = {"role": "assistant", "content": json.dumps(assistant_obj, ensure_ascii=False)}
    return s


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--augment", type=int, default=3,
                        help="Number of augmented copies per sample (default 3)")
    parser.add_argument("--slug", help="Process a single case (for debugging)")
    args = parser.parse_args()

    slugs = (
        [args.slug] if args.slug
        else sorted(s for s in os.listdir(COMPANIES) if (COMPANIES / s).is_dir())
    )

    samples = []
    stats = []

    for slug in slugs:
        case_dir = COMPANIES / slug
        if not (case_dir / "compute_ratios.py").exists():
            continue
        if not glob.glob(str(case_dir / "*Rationale*.md")):
            continue

        try:
            mod, R, meta, n_tieouts = _load_case(slug)
        except Exception as e:
            stats.append(f"SKIP {slug}: compute_ratios failed — {e}")
            print(f"  SKIP {slug} (engine error): {e}")
            continue

        try:
            prompt = build_prompt(slug, mod, R, meta, n_tieouts)
        except Exception as e:
            stats.append(f"SKIP {slug}: build_prompt failed — {e}")
            print(f"  SKIP {slug} (build_prompt): {e}")
            continue

        try:
            expected = _parse_rationale(slug)
        except Exception as e:
            stats.append(f"SKIP {slug}: rationale parse failed — {e}")
            print(f"  SKIP {slug} (rationale): {e}")
            continue

        # Validate
        warnings = []
        if not expected["long_term_grade"]:
            warnings.append("lt_grade missing")
        if len(expected["key_strengths"]) < 2:
            warnings.append(f"only {len(expected['key_strengths'])} strengths parsed")
        if len(expected["key_weaknesses"]) < 1:
            warnings.append(f"only {len(expected['key_weaknesses'])} weaknesses parsed")
        if len(expected["reasoning"]) < 100:
            warnings.append("reasoning very short")

        sample = {
            "messages": [
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": json.dumps(expected, ensure_ascii=False)},
            ]
        }
        samples.append(sample)

        # Augmented copies
        for i in range(1, args.augment + 1):
            samples.append(_augment(sample, seed=hash(slug) + i))

        line = (f"OK   {slug:<45} lt={expected['long_term_grade']!r:6} "
                f"str={len(expected['key_strengths'])} wk={len(expected['key_weaknesses'])} "
                f"rsn={len(expected['reasoning'])}ch")
        if warnings:
            line += "  WARN: " + "; ".join(warnings)
        stats.append(line)
        print(line)

    # Write JSONL
    train_path = OUT_DIR / "train.jsonl"
    with open(train_path, "w", encoding="utf-8") as f:
        for s in samples:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")

    stats_path = OUT_DIR / "train_stats.txt"
    stats_path.write_text("\n".join(stats) + f"\n\nTotal samples (incl. augmentation): {len(samples)}\n",
                          encoding="utf-8")

    print(f"\nWrote {len(samples)} samples to {train_path}")
    print(f"Stats -> {stats_path}")
    base = len(samples) // (args.augment + 1)
    print(f"  {base} base cases × {args.augment + 1} (1 original + {args.augment} augmented) = {len(samples)}")


if __name__ == "__main__":
    main()
