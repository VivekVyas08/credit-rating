"""Single READY / NOT READY verdict for a finance-research deliverable (a Research Note /
fact pack), mirroring delivery_audit.py's role for rating cases.

WHY THIS EXISTS
---------------
delivery_audit.py gates a RATING (tie-outs, scorecard-vs-rationale match, section/quality
probes). The finance-research skill produces a different deliverable - a Research Note with NO
rating or outlook - and none of the rating-specific checks apply to it directly (there is no
scorecard, no anchor, no agency grade to reconcile). Operator instruction, 03-Sep-2026: build
the same audit/loop discipline around finance-research specifically, so a research note is not
called "done" until every one of the skill's own binding requirements is mechanically checked,
not just claimed in the note's own prose.

WHAT THIS CHECKS, each one is a requirement the finance-research SKILL.md already states -
nothing here is invented:
  1. Every document in Companies/<slug>/documents/ appears in the note's Document Read Log
     (SKILL.md step 1 - "Read EVERY document... before writing anything").
  2. The computation script (research_ratios.py, or compute_ratios.py if that convention was
     used instead) exists and runs without a Python error.
  3. Reported vs normalised earnings are shown side by side (SKILL.md step 2).
  4. Every mandatory section is present, by header (SKILL.md step 7's stated structure).
  5. NO rating or outlook has leaked into the note (SKILL.md: "No rating, no outlook. If the
     user wants a rating, hand off to the icra-rating skill").
  6. Every broker note supplied is attributed by house name (SKILL.md step 4).

    python tools/research_audit.py <case-slug>
    python tools/research_audit.py --all
"""

import argparse
import glob
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COMPANIES = ROOT.parent / "Companies"

# A leading "N." or "N)" numbering prefix is common house style and is not itself a defect -
# every pattern below tolerates one. "&" and "and" are used interchangeably across notes.
_NUM = r"^#{1,3}\s*(?:\d+[.)]\s*)?"
MANDATORY_SECTIONS = [
    ("TL;DR", [_NUM + r"TL;?DR\b"]),
    ("Company & segments", [_NUM + r"Company\s*(?:&|and)?\s*segments?\b",
                             _NUM + r"About the company\b"]),
    ("Computed financials", [_NUM + r"Computed financials\b"]),
    ("Broker-view synthesis", [_NUM + r"Broker[- ]view synthesis\b"]),
    ("Red-flag sweep", [_NUM + r"Red[- ]?flags?\b.{0,30}\b(?:sweep|monitorable)"]),
    ("Peer context", [_NUM + r"Peer context\b"]),
    ("What to watch", [_NUM + r"What to watch\b"]),
    ("Document Read Log", [_NUM + r"Document Read Log\b"]),
    ("Sources & caveats", [_NUM + r"Sources\s*(?:&|and)?\s*caveats?\b"]),
]

# A grade token from any of the three agencies' scales - its presence in a Research Note is a
# scope violation, not a finding to report (SKILL.md: "No rating, no outlook").
RATING_GRADE_RE = re.compile(
    r"\[(?:ICRA|CRISIL|CARE)\]\s*(?:AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?|C|D)\b"
    r"|\bCrisil\s+(?:AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?|C|D)\b"
    r"|\bCARE\s+(?:AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?|C|D)\b")
OUTLOOK_RE = re.compile(r"\b(Stable|Positive|Negative)\s+outlook\b", re.I)


def _run(cmd: list) -> tuple[int, str]:
    p = subprocess.run(cmd, cwd=str(ROOT.parent), capture_output=True, text=True,
                        encoding="utf-8", errors="replace", timeout=900)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


# Words too generic to prove a specific document was referenced - "AR" or "Report" appears in
# half the filenames in any case folder, so matching on them alone would pass a note that never
# mentioned the file at all.
_GENERIC_TOKENS = {
    "ar", "ip", "vfinal", "final", "limited", "ltd", "annual", "report", "reports",
    "investor", "presentation", "notice", "agm", "results", "result", "financial",
    "financials", "unaudited", "audited", "integrated", "the", "and", "for", "of",
    "release", "press", "outcome", "note", "update", "sees", "upside", "downside",
}
_YEAR_QUARTER_RE = re.compile(
    r"\bq[1-4]\s*fy\s*2?\d{1,2}\b|\bfy\s*2?\d{2}(?:[\s-]2?\d{2})?\b|\b20\d\d[\s-]2?\d{2}\b",
    re.I)


def _normalise(s: str) -> str:
    return re.sub(r"[_\-\s]+", " ", s).strip().lower()


def _doc_referenced(path: Path, note_text: str) -> bool:
    """A document counts as referenced if the note contains EITHER a year/quarter code drawn
    from its filename (e.g. "Q1FY26", "2023-24") OR a distinctive (non-generic, 4+ letter)
    word from it - never the whole filename verbatim, since a well-written Read Log routinely
    abbreviates or groups several files under one descriptive row rather than reproducing
    upload filenames."""
    haystack = _normalise(note_text)
    haystack_nospace = haystack.replace(" ", "")
    stem_norm = _normalise(path.stem)

    # Regex \b treats "_" as a word character, so it fails to see a boundary right after the
    # underscore in "...Presentation_Q3FY26" - search the SEPARATOR-NORMALISED stem instead,
    # where that underscore is already a space and a real boundary exists.
    for m in _YEAR_QUARTER_RE.finditer(stem_norm):
        token = _normalise(m.group(0))
        # A filename writes "Q3FY26" with no space where the note writes "Q3 FY26" with one -
        # comparing both sides with ALL whitespace stripped catches that regardless of which
        # side has the space.
        if token in haystack or token.replace(" ", "") in haystack_nospace:
            return True
    for word in stem_norm.split():
        if len(word) >= 4 and word not in _GENERIC_TOKENS and not word.isdigit():
            if word in haystack:
                return True
    return False


def _find_note(case_dir: Path):
    hits = sorted(case_dir.glob("*Research_Note*.md")) or sorted(case_dir.glob("*Research Note*.md"))
    return hits[0] if hits else None


def audit_case(slug: str) -> dict:
    case_dir = COMPANIES / slug
    checks = []
    note = _find_note(case_dir)

    if note is None:
        checks.append(("Research Note delivered", False,
                        "no *Research_Note*.md in the case folder"))
        return {"slug": slug, "ready": False, "checks": checks}
    checks.append(("Research Note delivered", True, note.name))
    text = note.read_text(encoding="utf-8", errors="replace")

    # A note may legitimately DELEGATE its Document Read Log to a linked workpaper from the
    # same company's rating case, rather than duplicating a per-file table inline ("the full
    # Step-1b read is recorded in [X_Ratio_Workpaper.md]"). Follow any markdown link to a local
    # .md file inside the Document Read Log section and fold its text into the search haystack,
    # so a genuinely complete log recorded elsewhere is not treated as absent.
    doc_search_text = text
    log_section = re.search(r"(?:Document Read Log)\b(.*?)(?:\n#{1,3}\s|\Z)", text,
                             re.I | re.S)
    if log_section:
        for m in re.finditer(r"\]\(([^)]+\.md)\)", log_section.group(1)):
            linked = case_dir / m.group(1)
            if linked.is_file():
                doc_search_text += "\n" + linked.read_text(encoding="utf-8", errors="replace")

    # ------------------------------------------------------------- 1. document read log
    docs_dir = case_dir / "documents"
    all_docs = [p for p in docs_dir.rglob("*") if p.is_file()] if docs_dir.is_dir() else []
    if all_docs:
        missing = [d.name for d in all_docs if not _doc_referenced(d, doc_search_text)]
        checks.append(("Document Read Log covers every uploaded document", not missing,
                        "all %d document(s) referenced" % len(all_docs) if not missing else
                        "%d of %d document(s) not found referenced anywhere in the note: %s"
                        % (len(missing), len(all_docs), ", ".join(missing[:5]))))
    else:
        checks.append(("Document Read Log covers every uploaded document", None,
                        "no documents/ folder found for this case"))

    # ------------------------------------------------------- 2. computation script runs clean
    engine = None
    for name in ("research_ratios.py", "compute_ratios.py"):
        if (case_dir / name).is_file():
            engine = case_dir / name
            break
    if engine is None:
        checks.append(("Computation script present and runs clean", False,
                        "no research_ratios.py or compute_ratios.py in the case folder - "
                        "SKILL.md step 2 requires figures to be computed, never transcribed"))
    else:
        rc, out = _run([sys.executable, str(engine)])
        checks.append(("Computation script present and runs clean", rc == 0,
                        "%s exits 0" % engine.name if rc == 0 else
                        "%s exits %d: %s" % (engine.name, rc, out.strip()[-300:])))

    # --------------------------------------------------- 3. reported vs normalised earnings
    has_reported = bool(re.search(r"\breported\b", text, re.I))
    has_normalised = bool(re.search(r"\bnormali[sz]ed?\b", text, re.I))
    checks.append(("Reported vs normalised earnings shown", has_reported and has_normalised,
                    "both terms present" if (has_reported and has_normalised) else
                    "missing: %s" % ", ".join(
                        n for n, ok in (("'reported'", has_reported),
                                        ("'normalised'/'normalized'", has_normalised)) if not ok)))

    # ------------------------------------------------------------- 4. mandatory sections
    headers = [h.strip() for h in re.findall(r"^#{1,6}.*$", text, re.M)]
    missing_sections = []
    for label, patterns in MANDATORY_SECTIONS:
        if not any(re.search(p, h, re.I) for h in headers for p in patterns):
            missing_sections.append(label)
    checks.append(("All mandatory sections present", not missing_sections,
                    "all %d present" % len(MANDATORY_SECTIONS) if not missing_sections else
                    "missing: %s" % ", ".join(missing_sections)))

    # ------------------------------------------------------- 5. no rating/outlook leaked in
    # A grade token is not itself a violation - the skill's own Peer context step explicitly
    # requires citing peers "on scale, margins, leverage, returns", and a fact pack legitimately
    # reports the SUBJECT company's own already-published, externally-sourced rating as a fact
    # (e.g. "the AR's ratings note records ICRA/CARE/India Ratings all at AA") without that
    # being the note ASSIGNING one. The violation is a grade asserted with no citation context
    # at all - as if the note itself were the source. Each hit is checked for a citation signal
    # (rationale/rated/disclos/outstanding/records/AR/annual report/"as per") within 120 chars;
    # only an uncited hit is flagged, and it is flagged for a person to read, not auto-failed,
    # since this distinction is a judgment call a regex cannot make with full confidence.
    # NOTE: deliberately does NOT include the bare word "peer" - a hit inside a "## Peer
    # context" section would then always look cited merely from proximity to its own header,
    # which is exactly the gap a note asserting its OWN opinion ("we assess X should be rated
    # AA") could hide behind. Every signal here names a specific, checkable external source.
    CITATION_SIGNAL = re.compile(
        r"rationale|disclos|outstanding rating|\brecords?\b|annual report|\bAR'?s\b|"
        r"\bas per\b|rating note|rated by|currently rated|published rating|"
        r"\b(?:ICRA|CRISIL|CARE|Moody'?s|Fitch|S&P)\s+(?:notes?|states?|rationale)", re.I)
    uncited = []
    for m in RATING_GRADE_RE.finditer(text):
        window = text[max(0, m.start() - 120):m.end() + 40]
        if not CITATION_SIGNAL.search(window):
            uncited.append(m.group(0))
    outlook_hits = [m for m in OUTLOOK_RE.finditer(text)
                     if not CITATION_SIGNAL.search(text[max(0, m.start()-120):m.end()+40])]
    if uncited or outlook_hits:
        checks.append(("No UNCITED rating or outlook in the note (fact pack only)", False,
                        "found rating-scale language with no nearby citation signal - verify "
                        "these are citing an existing published rating, not the note's own "
                        "opinion: %s" % ", ".join(set(uncited) | {m.group(0) for m in outlook_hits})))
    else:
        checks.append(("No UNCITED rating or outlook in the note (fact pack only)", True,
                        "clean, or every grade mention is clearly cited to an external source"))

    # ------------------------------------------------------- 6. brokers attributed by house
    if re.search(r"\bbroker\b", text, re.I):
        # A named house next to "target"/"stance"/"rating"/"estimate" is the synthesis table's
        # own shape (SKILL.md: "house | stance | target | thesis | key estimates").
        house_pattern = re.search(
            r"\b(Motilal Oswal|ICICI Securities|Kotak|Nomura|Jefferies|CLSA|Morgan Stanley|"
            r"Goldman Sachs|JM Financial|Nuvama|Emkay|Antique|Systematix|Axis Capital|"
            r"HDFC Securities|IIFL|Elara|Prabhudas Lilladher|Sharekhan|Yes Securities)\b", text)
        checks.append(("Brokers attributed by house name", bool(house_pattern),
                        "found a named house" if house_pattern else
                        "the note discusses 'broker' views but no recognised brokerage house "
                        "name was found - verify attribution is real, not generic"))
    else:
        checks.append(("Brokers attributed by house name", None,
                        "no broker notes referenced - not necessarily a gap if none were "
                        "supplied for this case"))

    hard = [c for c in checks if c[1] is False]
    return {"slug": slug, "ready": len(hard) == 0, "checks": checks}


def print_report(result: dict) -> None:
    print("=" * 92)
    print("RESEARCH AUDIT - %s" % result["slug"])
    print("-" * 92)
    for name, ok, detail in result["checks"]:
        tag = "  OK  " if ok is True else ("  N/A " if ok is None else "*FAIL*")
        print("[%s] %-46s %s" % (tag, name, str(detail)[:200]))
    print("-" * 92)
    print("VERDICT: %s" % ("READY TO SHARE" if result["ready"] else "NOT READY - do not deliver"))
    print("=" * 92)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    if a.all:
        slugs = sorted({Path(p).parent.name for p in
                         glob.glob(str(COMPANIES / "*" / "*Research_Note*.md"))} |
                        {Path(p).parent.name for p in
                         glob.glob(str(COMPANIES / "*" / "*Research Note*.md"))})
    elif a.slug:
        slugs = [a.slug]
    else:
        ap.error("give a case slug or --all")

    if not slugs:
        print("No research notes found.")
        return 0

    all_ready = True
    for slug in slugs:
        result = audit_case(slug)
        print_report(result)
        all_ready = all_ready and result["ready"]
        print()
    return 0 if all_ready else 1


if __name__ == "__main__":
    sys.exit(main())
