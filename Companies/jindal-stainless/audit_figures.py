"""Step 17 drift check: every figure in the rationale, classified and verified.

CLAUDE.md Step 17 requires TWO checks, not one:
  * COMPUTED figures must match the ratio engine;
  * NON-COMPUTED figures (volumes, capacities, percentages read from narrative, instrument
    details) bypass the engine entirely and must be re-verified against their source document.
A single "all figures match" that silently covers only the computed set is failure mode 8.

This script does the first mechanically and lists the second for document verification.
"""

import re
import sys
from pathlib import Path

import compute_ratios as C

HERE = Path(__file__).resolve().parent
RATIONALE = HERE / "Jindal Stainless Limited_26 Aug 2026_CARE_Rating Rationale.md"
DOCS = HERE / "documents"


def engine_values():
    """Every number the engine can produce, as a set of rounded strings."""
    vals = {}
    R = C.compute()
    for y in C.YEARS:
        for k, v in R[y].items():
            if isinstance(v, (int, float)):
                vals.setdefault(round(v, 2), []).append("%s %s" % (y, k))
    for name, block in (("PL", C.PL), ("NCA", C.NON_CURRENT_ASSETS),
                        ("CA", C.CURRENT_ASSETS), ("EQ", C.EQUITY),
                        ("NCL", C.NON_CURRENT_LIABILITIES), ("CL", C.CURRENT_LIABILITIES)):
        for k, series in block.items():
            for i, v in enumerate(series):
                vals.setdefault(round(abs(v), 2), []).append("%s %s %s" % (name, C.YEARS[i], k))
    # derived aggregates that appear in the report
    for y in C.YEARS:
        for label, fn in (("total assets", C.total_assets), ("total equity", C.total_equity),
                          ("current assets", C.current_assets),
                          ("current liabilities", C.current_liabilities),
                          ("total debt", C.total_debt), ("net debt", C.net_debt),
                          ("TNW", C.tangible_net_worth), ("liquid", C.liquid_assets),
                          ("borrowings only", C.borrowings_only),
                          ("PBILDT base", C.pbildt_base)):
            vals.setdefault(round(fn(y), 2), []).append("%s %s" % (y, label))
    return vals


def doc_corpus():
    txt = []
    for f in DOCS.rglob("*.md"):
        txt.append(f.read_text(encoding="utf-8", errors="replace"))
    return "\n".join(txt)


NUM_RE = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{2,3})*(?:\.\d+)?|\d+\.\d+)(?![\w])")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    rat = RATIONALE.read_text(encoding="utf-8", errors="replace")
    # Ignore the correction paragraph: it deliberately quotes superseded figures.
    rat_body = re.sub(r"An earlier version of this analysis.*?stated judgement\.", "", rat,
                      flags=re.S)

    eng = engine_values()
    docs = doc_corpus()
    docs_nospace = re.sub(r"[ ,]", "", docs)

    seen, matched_engine, matched_doc, unmatched = set(), [], [], []
    for m in NUM_RE.finditer(rat_body):
        raw = m.group(1)
        if raw in seen:
            continue
        seen.add(raw)
        try:
            val = float(raw.replace(",", ""))
        except ValueError:
            continue
        if val < 1:
            continue
        ctx = rat_body[max(0, m.start() - 60):m.start() + 40].replace("\n", " ")
        key = round(val, 2)
        if key in eng:
            matched_engine.append((raw, eng[key][0]))
        elif raw in docs or re.sub(r"[ ,]", "", raw) in docs_nospace:
            matched_doc.append((raw, ctx))
        else:
            unmatched.append((raw, ctx))

    print("=" * 90)
    print("FIGURE AUDIT - %s" % RATIONALE.name)
    print("=" * 90)
    print("\n[1] MATCHED TO THE RATIO ENGINE: %d" % len(matched_engine))
    print("[2] NOT in the engine but PRESENT VERBATIM in the document set: %d"
          % len(matched_doc))
    print("[3] MATCHED NEITHER - each needs a source or is derived: %d\n" % len(unmatched))

    print("-" * 90)
    print("[3] REQUIRES EXPLICIT VERIFICATION")
    print("-" * 90)
    for raw, ctx in unmatched:
        print("  %-12s ...%s..." % (raw, ctx.strip()))

    print("\n" + "-" * 90)
    print("[2] IN DOCUMENTS BUT NOT COMPUTED - confirm each is used in the right context")
    print("-" * 90)
    for raw, ctx in matched_doc:
        print("  %-12s ...%s..." % (raw, ctx.strip()))


if __name__ == "__main__":
    main()
