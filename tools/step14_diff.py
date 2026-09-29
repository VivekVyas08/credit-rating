"""Step 14, made mechanical: diff our report against the agency's own action for this issuer.

    python tools/step14_diff.py <case-slug> [--tolerance 3.0]

WHY THIS EXISTS
---------------
Every other gate in this project verifies INTERNAL CONSISTENCY - do my numbers agree with the
printed totals in the document I chose, would a tie-out notice if an input moved, are the
required sections present, does the workbook agree with the report. All of them can score 100%
on a report built off the wrong statement, the wrong period or the wrong definition, because
such a report is perfectly self-consistent. That is verification. It is not validation.

Dhampur Bio Organics, 04-Sep-2026, is the case that proved the gap: 34/34 tie-outs, 100.0%
mutation coverage, every section present, scorecard matching - and the rated amount overstated
by Rs 72.40 crore, the basis wrong, liquidity overstated ~8x, and the sector's defining
operating metric absent. Not one gate could see any of it.

This tool is the missing half. Step 14 already REQUIRES opening the agency's own action; it
just never required comparing anything but the grade. Here every comparable number is compared,
and a divergence must be explained in the report or the gate fails.

WHAT IT DOES NOT DO
-------------------
It does not import a single figure into the report (R2 - the reference library teaches craft
and is never a data source). It reads the agency's numbers only to ask "why is mine different?"
That question is the whole point, and it is the one question no other check in this project
asks.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
LIBS = ["Report for Reference", "CRISIL/Report for Reference", "CareEdge/Report for Reference"]

STOP = {"limited", "ltd", "the", "and", "of", "india", "private", "company", "co"}

# Rows worth comparing, with the aliases each agency uses for them.
ROWS = [
    ("Total operating income", r"total operating income|total income|toi\b|operating income"),
    ("PBILDT / EBITDA",        r"pbildt|pbdit|opbdit|ebitda"),
    ("PAT",                    r"profit after tax|^pat\b|\bpat\b"),
    ("Overall gearing (x)",    r"overall gearing|gearing \(x|gearing \(times"),
    ("Interest coverage (x)",  r"interest coverage"),
    ("Tangible net worth",     r"tangible net worth|\btnw\b|net worth"),
    ("Total debt",             r"total debt"),
]


def tokens(name: str):
    return {w for w in re.findall(r"[a-z0-9]+", name.lower())
            if w not in STOP and len(w) > 2}


AGENCY_LIB = {"ICRA": "Report for Reference",
              "CRISIL": "CRISIL/Report for Reference",
              "CareEdge": "CareEdge/Report for Reference"}


def find_publications(slug: str, case_name: str, agency: str = ""):
    """Same-issuer agency publications, matched on filename (the library is ~2,100 files)."""
    want = tokens(case_name) or tokens(slug.replace("-", " "))
    if not want:
        return []
    # Step 14 compares OUR action with THE SAME AGENCY's action. Comparing an ICRA report
    # against a CareEdge one diverges by construction - the conventions differ on purpose
    # (ICRA OPBDIT strips other income; CareEdge PBILDT nets excise off TOI), which is the
    # entire basis of failure mode 32. Hindustan Aeronautics reproduced ICRA's figures exactly
    # and was still failed, on a CareEdge report that tabulates absolute PBILDT where ICRA
    # tabulates OPBDIT/OI as a percentage.
    libs = [AGENCY_LIB[agency]] if agency in AGENCY_LIB else LIBS
    out = []
    for lib in libs:
        d = ROOT / lib
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.md")):
            have = tokens(f.stem)
            if not have:
                continue
            # A ONE-TOKEN issuer identity must match EXACTLY, or it drags in every unrelated
            # company sharing that word. "Oil India" reduces to {oil} once stopwords go, and a
            # subset test then matched Gulf Oil Lubricants and Indian Oil Corporation - the
            # tool reported a 2,671,066% divergence in total debt against a company that is not
            # the issuer. This is failure mode 24 from the other direction, the same trap the
            # FM37 probe hit with {steel}. The partial-overlap fallback is gone for the same
            # reason: near-misses on a 2,100-file library are almost always a different issuer.
            if len(want) == 1:
                if have == want:
                    out.append(f)
            elif want <= have:
                out.append(f)
    return out


def nums(line: str):
    """Numeric cells in a markdown/plain table row, as floats."""
    vals = []
    for cell in re.split(r"\||\s{2,}", line):
        c = cell.strip().replace(",", "").replace("*", "")
        c = re.sub(r"^\(|\)$", "-", c) if c.startswith("(") else c
        m = re.fullmatch(r"-?\d+(?:\.\d+)?%?", c)
        if m:
            vals.append(float(c.rstrip("%")))
    return vals


def _financials_block(text: str) -> str:
    """Just the Brief Financials / Key Financial Indicators table.

    Scoping matters more than matching here. The first version of this tool searched the WHOLE
    document and reported PBILDT "theirs = -20.00" and interest coverage "theirs = 0.74" -
    numbers scraped off unrelated tables. A gate that cries wolf trains the reader to ignore
    it, which is worse than no gate.
    """
    m = re.search(r"^[^\n]*(brief financial|key financial indicator|financial performance)"
                  r"[^\n]*$", text, re.I | re.M)
    if not m:
        return ""
    # Start at the START of the matched line: in CareEdge's format the caption and the period
    # headers are the SAME row ("|Brief Financials(Rs crore)|March 31, 2024(A)|..."), so
    # slicing from m.end() threw the periods away and left nothing comparable.
    tail = text[m.start(): m.start() + 1700]
    stop = re.search(r"^\s*#{1,4}\s|\bannexure\b", tail[80:], re.I | re.M)
    return tail[: stop.start() + 80] if stop else tail


def _norm_period(cell: str):
    """'March 31, 2025(A)' -> 'FY2025'.  'H1FY26(UA)' -> None (not an annual column).

    Returning None for part-year columns is the point. Without it this tool compared our
    FULL-YEAR FY2026 against the agency's H1FY26 stub and reported PBILDT diverging 754% -
    which is a period error inside the very tool built to catch period errors.
    """
    c = cell.lower().replace("*", "").strip()
    if re.search(r"\b(h1|h2|q[1-4]|9m|6m|3m)\b|\b(h1|q[1-4]|9m)fy", c):
        return None
    m = re.search(r"march\s*31,?\s*(20\d\d)", c)
    if m:
        return "FY" + m.group(1)
    m = re.search(r"fy\s*(20\d\d)", c)
    if m:
        return "FY" + m.group(1)
    m = re.search(r"fy\s*(\d\d)\b", c)
    if m:
        return "FY20" + m.group(1)
    return None


def brief_rows(text: str):
    """{canonical row -> {period -> value}} from the financials table only, period-aligned."""
    block = _financials_block(text)
    if not block:
        return {}
    periods = []
    for line in block.splitlines():
        if line.count("|") >= 2 and re.search(r"20\d\d|fy\s*\d", line, re.I):
            # Do NOT drop empty cells: a table headed "| | FY2025 | FY2026 |" has an EMPTY
            # label cell, and filtering it shifts every period one column left. That made the
            # tool pair OUR FY2025 against THEIR FY2026 and report a 24% divergence between
            # two tables that are in fact identical. Positional alignment is the whole game.
            cells = line.split("|")[1:]
            if cells and not cells[-1].strip():
                cells = cells[:-1]
            cand = [_norm_period(c) for c in cells]
            if any(cand):
                periods = cand
                break
    if not periods:
        return {}
    found = {}
    for line in block.splitlines():
        if not re.search(r"\d", line) or line.count("|") < 2:
            continue
        low = line.lower()
        label = low.split("|")[1]
        # Labels arrive from PDF extraction with spaces eaten ("Total operatingincome",
        # "Overallgearing", "Profit after tax(PAT)"). Match on a squeezed label so a lost
        # space cannot hide the headline row.
        squeezed = re.sub(r"[^a-z0-9]", "", label)
        # An ABSOLUTE-value row must not be matched by a RATIO row of the same name. Without
        # this, "PBILDT margin (%)" answered to "PBILDT" and "gearing" answered to "net worth",
        # so the tool compared a percentage against a rupee-crore figure and called it a 26%
        # divergence. Same failure shape as the label-collision it exists to catch.
        _is_ratio_row = re.search(r"margin|%|\(x\)|\(times\)|ratio|gearing|coverage|days",
                                  label) is not None
        for canon, pat in ROWS:
            if _is_ratio_row and canon in ("Total operating income", "PBILDT / EBITDA", "PAT",
                                           "Tangible net worth", "Total debt"):
                continue
            if (not _is_ratio_row) and canon in ("Overall gearing (x)",
                                                 "Interest coverage (x)"):
                continue
            if canon in found:
                continue
            if not (re.search(pat, label)
                    or re.search(re.sub(r"[^a-z0-9|]", "", pat), squeezed)):
                continue
            v = nums(line)
            if not v:
                continue
            # align values to the header, right-padding when the label cell held no number
            # periods[0] is the LABEL column, so value cells start at index 1 on both sides.
            cells = [c.strip() for c in line.split("|")[1:]]
            if cells and not cells[-1]:
                cells = cells[:-1]
            vals = {}
            for idx, c in enumerate(cells):
                if idx == 0:
                    continue
                if idx >= len(periods) or not periods[idx]:
                    continue
                cn = nums("|" + c + "|")
                if cn:
                    vals[periods[idx]] = cn[0]
            if vals:
                found[canon] = vals
    return found


def rated_total(text: str):
    """Sum of the rated facility amounts in the RATING-ACTION table only.

    Bounded to the text before the first Annexure. Unbounded, it summed the action table AND
    Annexure-1, which describe the SAME facilities - reporting our Rs 1,134.45 crore programme
    as Rs 2,268.90 crore, exactly double. Rows whose label says 'total' are skipped so the
    printed total is not added to its own components.
    """
    head = re.split(r"\bannexure\b", text, maxsplit=1, flags=re.I)[0]
    # ICRA's summary table carries BOTH "Previous rated amount" and "Current rated amount".
    # Taking max() across the row mixes the two vintages and invents a programme size that
    # never existed - on HLE Glascoat it produced 437.55 against a real 517.50. Where both
    # columns are present, the CURRENT one is the answer.
    two_col = bool(re.search(r"previous rated", head, re.I)
                   and re.search(r"current rated", head, re.I))
    total = None
    for line in head.splitlines():
        if not re.search(r"(long|short)[- ]term|commercial paper|fund[- ]based"
                         r"|non-fund[- ]based|cash credit|term loan|bank ?guarantee"
                         r"|letter of credit|unallocated|derivative", line, re.I):
            continue
        if line.count("|") < 2:
            continue
        cells = [c.strip() for c in line.split("|")[1:]]
        label = cells[0] if cells else ""
        if re.search(r"\btotal\b", label, re.I):
            continue
        # A parenthesised amount is an INTERCHANGEABLE sub-limit carved out of another
        # facility, not additional exposure. Adding it double-counts the programme.
        if any(re.match(r"^\**\(", c) for c in cells[1:3]):
            continue
        # Take the LEADING number of each cell, not a whole-cell match: agencies write
        # "987.05 (reduced from 1,019.45)" in the amount column, and a strict fullmatch drops
        # the row entirely - silently losing the very figure this check exists to compare.
        v = []
        for c in cells[1:]:
            m = re.match(r"\**\s*(-?[\d,]+(?:\.\d+)?)", c.replace("`", ""))
            if m:
                try:
                    x = float(m.group(1).replace(",", ""))
                except ValueError:
                    continue
                if x > 1.0:
                    v.append(x)
        if not v:
            continue
        total = (total or 0.0) + (v[1] if (two_col and len(v) > 1) else v[0])
    return total


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--tolerance", type=float, default=3.0,
                    help="%% divergence on a financial row that must be explained (default 3)")
    a = ap.parse_args()

    case = ROOT / "Companies" / a.slug
    if not case.is_dir():
        sys.exit("no such case: %s" % a.slug)
    mine_f = [p for p in sorted(case.glob("*Rating Rationale*.md"))
              if "SUPERSEDED" not in p.name.upper()]
    if not mine_f:
        print("no rationale in %s - nothing to diff" % a.slug)
        return 0
    mine_p = mine_f[-1]
    mine = mine_p.read_text(encoding="utf-8", errors="replace")

    name = a.slug.replace("-", " ")
    agency = ""
    cj = case / "case.json"
    if cj.is_file():
        import json
        try:
            _m = json.loads(cj.read_text(encoding="utf-8"))
            name = _m.get("name", name)
            agency = str(_m.get("agency", "") or "")
        except Exception:                                                 # noqa: BLE001
            pass

    pubs = find_publications(a.slug, name, agency)
    print("=" * 92)
    print("STEP 14 DIFF  |  %s" % name)
    print("=" * 92)
    print("our report : %s" % mine_p.name)
    print("agency     : %s (comparing only against this agency's own actions)"
          % (agency or "not declared - searching all libraries"))
    if not pubs:
        print("\nNo same-issuer agency publication found in the reference libraries.")
        print("Step 14 falls back to peer benchmarking; nothing to diff mechanically.")
        return 0

    my_rows, my_rated = brief_rows(mine), rated_total(mine)
    unexplained = 0
    for pub in pubs:
        txt = pub.read_text(encoding="utf-8", errors="replace")
        print("\n--- vs %s ---" % pub.name)

        # basis
        mb = re.search(r"analytical approach:?\**\s*:?\**\s*(standalone|consolidated|combined)",
                       mine, re.I)
        tb = re.search(r"analytical approach:?\**\s*:?\**\s*(standalone|consolidated|combined)",
                       txt, re.I)
        if mb and tb:
            same = mb.group(1).lower() == tb.group(1).lower()
            print("  %-26s ours=%-12s theirs=%-12s %s"
                  % ("Analytical basis", mb.group(1).lower(), tb.group(1).lower(),
                     "ok" if same else "*** DIFFERS ***"))
            if not same:
                unexplained += 1

        # rated amount
        tr = rated_total(txt)
        if my_rated and tr:
            d = abs(my_rated - tr)
            flag = "ok" if d < 0.01 else "*** DIFFERS by %.2f ***" % d
            print("  %-26s ours=%-12.2f theirs=%-12.2f %s"
                  % ("Rated amount (total)", my_rated, tr, flag))
            if d >= 0.01:
                unexplained += 1

        # financial rows
        their_rows = brief_rows(txt)
        shared = sorted(set().union(*[set(v) for v in my_rows.values()]) &
                        set().union(*[set(v) for v in their_rows.values()])) \
            if my_rows and their_rows else []
        if not shared:
            print("  (no overlapping ANNUAL period between the two financials tables - "
                  "nothing comparable; their latest column may be a part-year)")
        for period in shared:
            for canon, _ in ROWS:
                mv = my_rows.get(canon, {}).get(period)
                tv = their_rows.get(canon, {}).get(period)
                if mv is None or tv is None or tv == 0:
                    continue
                pct = abs(mv - tv) / abs(tv) * 100
                flag = "ok" if pct <= a.tolerance else "*** %.1f%% ***" % pct
                print("  %-9s %-24s ours=%-11.2f theirs=%-11.2f %s"
                      % (period, canon, mv, tv, flag))
                if pct > a.tolerance:
                    unexplained += 1

    print("\n" + "-" * 92)
    if unexplained:
        # What counts as "explained" must match how an analyst actually writes it. The first
        # version demanded the literal phrase "divergence table" and rejected a report whose
        # Brief Financials carried a full, numbered divergence note headed "Divergence against
        # CareEdge's published figures, disclosed not forced" - i.e. exactly the behaviour the
        # gate exists to require. A gate that fails compliant work teaches people to ignore it.
        # TWO false negatives out of two real cases told me this list was too narrow. Both
        # reports DID explain their divergence and both were failed: Dhampur v2 carried a
        # numbered note headed "Divergence against CareEdge's published figures, disclosed not
        # forced"; Jindal Stainless states "This is the UNADJUSTED measure: CareEdge's adjusted
        # leverage also incorporates acceptances/LC creditors and guarantees to group entities,
        # neither of which is separately quantified". Failing compliant work is how a gate
        # teaches people to ignore it, so the detector now recognises a genuine
        # basis-or-convention discussion, not a magic phrase.
        explained = re.search(
            r"divergence table|divergence against|diverge[sd]? (from|by)"
            r"|differs? (from|by|slightly) (the )?(agency|prior|published|their|careedge|crisil|icra)"
            r"|basis differs|why this (differs|basis differs)|step 14"
            r"|disclosed,? not forced|not adjusted to close"
            r"|unadjusted measure|adjusted (gearing|leverage)"
            r"|on (this|our) convention|convention (is |)stated"
            r"|(their|the agency\S{0,2}) (denominator|definition|convention|basis)",
            mine, re.I)
        if explained:
            print("%d divergence(s) flagged; the report carries a Step 14 divergence "
                  "discussion. READ IT and confirm it covers each line above." % unexplained)
            return 0
        print("%d DIVERGENCE(S) UNEXPLAINED - the report has no Step 14 divergence table.\n"
              "Every line marked *** must be explained in the report, or corrected."
              % unexplained)
        return 1
    print("No material divergence against the agency's own action.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
