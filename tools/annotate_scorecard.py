"""Make a filled scorecard say, on its own face, that it is NOT the rating.

WHY THIS EXISTS
---------------
The workbook prints its anchor grade under the heading "Rating line (agency house style)" and
formats it exactly like an assigned rating - "[ICRA]B- (Stable) / [ICRA]A4". The only caveat
is a generic sentence at the bottom of the sheet. So a reader who opens the scorecard beside
the rationale sees B- in one and A- in the other and reasonably concludes something is broken.

Nothing IS broken. The anchor is deliberately computed on the financials ALONE, with support
notches entered as zero, so that any divergence from the analyst's view has to be argued rather
than absorbed into a notch. That is the design. But the design was legible only to someone who
had read the workpaper, which is the wrong place for it: a document that can be opened on its
own has to explain itself on its own.

Found 01-Sep-2026 when the operator asked why the Excel said B- and the rationale said A-.
That is the question every reader will ask, including a rating committee.

    python annotate_scorecard.py --all            # every case, rating read from its rationale
    python annotate_scorecard.py <slug>           # one case
    python annotate_scorecard.py <slug> --rating "[ICRA]A- (Stable)"   # explicit override

The annotation is written into empty cells and static labels only - no formula is touched - and
recalc_workbook.py is re-run afterwards so the cached values stay consistent.
"""

import argparse
import re
import sys
from pathlib import Path

from openpyxl.styles import Alignment, Font, PatternFill

ROOT = Path(__file__).resolve().parent.parent  # this script now lives in tools/,
# one level below the project root - moved here 01-Sep-2026 to declutter the root.
NAVY = "1B2A4A"
AMBER = "FFF4E5"
RED = "9B2226"


# The agency prefix must be consumed before the grade is matched. Without it the pattern
# finds the "A" inside "[ICRA]" and reports a phantom grade - which it did on the first run of
# the corpus comparison, inventing divergences on Alembic and Balkrishna that do not exist.
# SHORT-TERM grades are in the alternation too, and they have to be, because some issuers are
# rated on the short-term scale ALONE. ITC's ICRA and CareEdge rationales each rate a single
# Rs 500 crore commercial-paper programme - "[ICRA]A1+" and "CARE A1+" - and carry no
# long-term grade anywhere. Without A1..A4 the pattern found nothing in either file, both fell
# through to ITC's CRISIL report, and all three ITC scorecards were annotated "Crisil AAA".
# The short-term alternatives must precede the bare "A": otherwise "A1+" tries to match as
# "A", the trailing lookahead rejects the digit, and the whole match fails. Found 01-Sep-2026.
GRADE_RE = re.compile(
    r"(?:\[ICRA\]|Crisil\s+|CARE\s+)"
    r"(AAA|AA[+-]|AA|A1\+|A1|A2\+|A2|A3\+|A3|A4\+|A4"
    r"|A[+-]|A|BBB[+-]|BBB|BB[+-]|BB|B[+-]|B|C|D)(?![A-Za-z0-9+-])")
_ST = {"A1+", "A1", "A2+", "A2", "A3+", "A3", "A4+", "A4"}


# The rationale's LONG-TERM and SHORT-TERM grades are read SEPARATELY - the first of each. Taking
# just the first grade in the file compared whichever row the Summary-of-rating-action table
# happened to lead with, and ICRA's own ordering puts commercial paper FIRST. Ashok Leyland,
# 10-Oct-2026: the run printed "assigned A1+ vs rationale A1+ -> MATCHES" off the CP row, and the
# long-term [ICRA]AA+ (Stable) was never compared - so a long-term mismatch passed silently.
def split_grades(text):
    """(long-term grade, short-term grade): the first of each in `text`; either may be None."""
    lt = st = None
    for m in GRADE_RE.finditer(text or ""):
        if m.group(1) in _ST:
            st = st or m.group(1)
        else:
            lt = lt or m.group(1)
    return lt, st


def _quote(head, m):
    """The rating as written at match m: grade, Watch '&', and outlook in each agency's form -
    "[ICRA]AA+ (Stable)", "Crisil AA+/Stable", "CARE AA; Stable". Nothing else, so a combined
    cell "[ICRA]AA+ (Stable)/[ICRA]A1+" or a headline "... A1+ reaffirmed" quotes cleanly."""
    tail = re.match(r"&?(?:\s*\((?:Stable|Positive|Negative|Developing)\)"
                    r"|\s*[/;]\s*(?:Stable|Positive|Negative|Developing))?", head[m.end():])
    return m.group(0) + tail.group(0)



def _superseded(path) -> bool:
    """A kept-aside copy of a workbook that a rebuild replaced - not a deliverable.

    When a scorecard is rebuilt onto a newer template the old one is kept beside it as
    `*.pre_restructure.xlsx` (the convention the project root already uses for the master
    template). Those copies predate the three-stage layout by definition, so they have no
    Rating sheet - and picking them up made the tool report NOT VERIFIED for a case whose
    LIVE workbook verifies perfectly well. A superseded backup must not fail the gate.
    """
    n = path.name.lower()
    return ("pre_restructure" in n or "superseded" in n or n.endswith(".bak.xlsx")
            or n.startswith("~$"))

def rationale_for(slug: str, agency: str = None):
    """(grade, filename) from this case's own rationale headline, or (None, None).

    Reads the case folder first, then the project root - rationales now live in
    Companies/<slug>/ (organised 01-Sep-2026), with the root kept as a fallback for a report
    filed before its case folder existed. Matching is by the same case resolver the delivery
    gate uses, so a case registered under a short name still finds its report.
    """
    import check_sections as CS
    # A superseded report is not the rationale. The glob also matches "..._SUPERSEDED.md", and
    # Dhampur's 04-Sep copy (BBB+; Stable) sorted ahead of the live 13-Sep one (BBB+; Positive).
    cand = sorted(f for f in (ROOT / "Companies" / slug).glob("*Rating Rationale*.md")
                  if not _superseded(f))
    for f in sorted(ROOT.glob("*Rating Rationale*.md")):
        d = CS.resolve_case_dir(f)
        if d is not None and d.name == slug and not _superseded(f):
            cand.append(f)

    # A case can hold rationales from more than one agency - JSW Steel has both an ICRA and a
    # CRISIL report in the root. The scorecard is filled for ONE agency and must quote THAT
    # agency's rating line; "[ICRA]AA" on a CRISIL scorecard is wrong even when the grade
    # letter happens to match. Key on the prefix of the grade each file LEADS WITH, not on
    # whether the agency name appears anywhere - an ICRA report lists CRISIL in its
    # rating-history table, and a plain substring test is defeated by that.
    prefix = {"ICRA": "[ICRA]", "CRISIL": "Crisil", "CareEdge": "CARE"}.get(agency or "")
    if prefix:
        def _leads_with(f):
            m = GRADE_RE.search(f.read_text(encoding="utf-8", errors="replace")[:1200])
            return 0 if (m and m.group(0).lower().startswith(prefix.lower())) else 1
        matching = [f for f in cand if _leads_with(f) == 0]
        # STRICT. If no rationale leads with this agency's own prefix, return nothing rather
        # than falling back to another agency's report. Annotating an ICRA scorecard with a
        # CRISIL rating line is the very defect this module exists to prevent, and a silent
        # fallback through sort order is exactly how it happened on ITC. A skip is visible in
        # the run output; a wrong rating is not.
        if not matching:
            return None, None
        cand = matching

    for f in cand:
        # 1,200 chars, not 600: a CareEdge press release puts its rating table below a masthead
        # and a date line, so the first grade on IIFL sits at character 624. The first grade
        # in that table is the primary long-term facility, which is the one to quote.
        head = f.read_text(encoding="utf-8", errors="replace")[:1200]
        # Long-term first, then short-term, each quoted as written. A short-term-only mandate
        # (ITC's CP programmes, Solar) yields the ST quote alone, exactly as before.
        quotes = [_quote(head, m) for m in (
            next((m for m in GRADE_RE.finditer(head) if (m.group(1) in _ST) == st), None)
            for st in (False, True)) if m]
        if quotes:
            return " / ".join(quotes), f.name
    return None, None


# What each agency calls its operating-profit measure, and how that measure is DEFINED in that
# agency's own criteria. Stated on the workbook so a reader knows which convention produced the
# numbers - the three are not interchangeable and the difference is material.
CONVENTION = {
    "ICRA": ("OPBDIT",
             "OPBDIT = PBT + finance cost + depreciation and amortisation LESS other income "
             "in full. ICRA strips other income unconditionally. Total debt includes lease "
             "liabilities, off-balance-sheet items such as discounted receivables, and the "
             "debt component of hybrids. Tangible net worth excludes revaluation reserves."),
    "CRISIL": ("EBITDA",
               "PBDIT / EBITDA RETAINS recurring non-operating income rather than stripping "
               "it. Gearing uses adjusted total debt over adjusted networth, both adjusted "
               "for revaluation reserves, miscellaneous expenditure not written off, and "
               "off-balance-sheet items assessed for devolvement."),
    "CareEdge": ("PBILDT",
                 "PBILDT = total operating income less all operating expenses. Interest, "
                 "dividend and rental income are EXCLUDED from TOI even when recurring, and "
                 "indirect taxes are netted off gross sales. Total debt includes acceptances "
                 "and creditors on LC, and lease liabilities."),
}


def scope_to_agency(wf, agency: str) -> int:
    """Strip every other agency's information out of the workbook.

    A delivered scorecard is the artefact for ONE rating. Leaving the other two agencies'
    conventions in the reference sheets invites a reader to mix them, and the three operating
    profit definitions are NOT interchangeable - which is the single most consequential
    difference between the agencies (failure modes 32 and 33). Operator instruction,
    01-Sep-2026: an ICRA scorecard carries ICRA information only.

    The ACTIVE agency's row is left where it is, because the Ratios and Rating sheets look it
    up with MATCH against that range; only the inactive rows are cleared.
    """
    removed = 0
    if "Ref_Scales" in wf.sheetnames:
        ws = wf["Ref_Scales"]
        for r in range(5, 8):                       # H5 ICRA, H6 CRISIL, H7 CareEdge
            if str(ws.cell(row=r, column=8).value or "").strip() != agency:
                for col in (8, 9, 10):
                    if ws.cell(row=r, column=col).value is not None:
                        ws.cell(row=r, column=col).value = None
                        removed += 1
    if "README" in wf.sheetnames:
        rm = wf["README"]
        rm["B2"] = "Credit Rating Scorecard - %s" % agency
        for coord in ("B18", "B19"):
            v = rm[coord].value
            if isinstance(v, str):
                # Keep the disclosure that these are the TOOL'S calibration - removing it would
                # imply the bands are agency-published, which is a worse error than naming a
                # second agency. Only the cross-agency naming goes.
                for other in ("ICRA", "CRISIL", "Crisil", "CareEdge", "CARE"):
                    if other != agency:
                        v = v.replace(other + " / ", "").replace(" / " + other, "")
                        v = v.replace(other + ", ", "").replace(", " + other, "")
                        v = v.replace(other, agency)
                rm[coord] = v
                removed += 1
    # Two notes cite another agency's rule or methodology by name. On a single-agency artefact
    # that is exactly the mixing the operator instruction forbids: a CareEdge financial-
    # flexibility rule has no business justifying an assumption on an ICRA scorecard.
    RUBRIC = {
        "ICRA": "ICRA methodology 960 (industry / business / management)",
        "CRISIL": "CRISIL's three risk profiles - market position is the ability to sell "
                  "PROFITABLY and control price; risk appetite is explicit",
        "CareEdge": "CareEdge rating blocks A-D",
    }
    if "Ref_Qualitative" in wf.sheetnames:
        wf["Ref_Qualitative"]["B3"] = (
            "Anchors the Industry, Business and Management scores so two operators score "
            "alike. Lifted from %s. Pick the row whose description best fits; justify the "
            "pick in one line in the report." % RUBRIC.get(agency, "the applicable methodology"))
        removed += 1
    if "Projections" in wf.sheetnames:
        wf["Projections"]["B20"] = (
            "Interest on average of opening/closing debt. Depreciation held at FY0 level "
            "(conservative for flat capex). No equity raising assumed - an unraised issue is "
            "not a committed source of funds.")
        removed += 1

    # PROVENANCE lines. These say where the tool's own calibration came from, and they named a
    # reference corpus of published rationales. On a single-agency artefact the corpus's agency
    # must not be named - but the DISCLOSURE must survive, because deleting it would imply the
    # mapping and bands are the agency's own. So the name goes and the disclaimer sharpens.
    PROV = ("Derived from an empirical corpus of published rationales and back-tested "
            "18-Jul-2026 against 396 rated issuers. This is THIS PROJECT'S calibration and is "
            "NOT published by %s.")
    for sheet, coords in (("README", ("B20", "B21", "B29")), ("Ref_Scales", ("A23",))):
        if sheet in wf.sheetnames:
            ws = wf[sheet]
            for coord in coords:
                if isinstance(ws[coord].value, str):
                    ws[coord] = PROV % agency
                    removed += 1

    for sheet, coord in (("Ref_Bands", "A2"), ("Ref_Bands_Fin", "A2")):
        if sheet in wf.sheetnames:
            ws = wf[sheet]
            ws[coord] = ("This project's OWN calibration - illustrative benchmark ranges, "
                         "NOT published by %s. See Scorecard_Backtest_Report_18Jul2026.md."
                         % agency)
            removed += 1
    return removed


def annotate(book: Path, proposed: str, ref: str) -> str:
    from openpyxl import load_workbook

    wf = load_workbook(book)
    wv = load_workbook(book, data_only=True)
    if "Rating" not in wf.sheetnames:
        return "no Rating sheet - skipped"
    ws, vs = wf["Rating"], wv["Rating"]
    if "Inputs" not in wv.sheetnames:
        return "no Inputs sheet - skipped"
    agency = str(wv["Inputs"]["C5"].value or "").strip()
    stripped = scope_to_agency(wf, agency)

    # The sheet now explains itself: Stage 1 anchor -> Stage 2 overlay -> Stage 3 assigned
    # rating, with the divergence COMPUTED in C34. This function's job is therefore no longer
    # to narrate the divergence - it is to VERIFY that Stage 3 equals the rationale, and to say
    # so loudly when it does not. A mismatch is the defect the operator reported on 02-Sep-2026
    # ("the rating in the excel and the rating in the report are different").
    anchor_grade = vs["C16"].value
    assigned_line = vs["C36"].value
    assigned_grade = vs["C32"].value
    divergence = vs["C34"].value
    caps = vs["C14"].value

    # Long-term against C32 whenever the rationale carries one; short-term against C33 whenever
    # it carries one. Short-term-only mandates (ITC: a single CP programme rated [ICRA]A1+, no
    # long-term grade in the rationale at all) therefore compare the ST grade alone, as before.
    want_lt, want_st = split_grades(proposed)
    got_lt = str(assigned_grade).strip() if assigned_grade is not None else None
    got_st = str(vs["C33"].value or "").strip() or None
    pairs = [(w, g) for w, g in ((want_lt, got_lt), (want_st, got_st)) if w]
    agree = bool(pairs) and all(w == g for w, g in pairs)
    want_grade = "/".join(w for w, _ in pairs) or None
    got_grade = "/".join(str(g) for _, g in pairs) or None
    shown = " / ".join(str(v) for v, w in ((assigned_line, want_lt), (vs["C37"].value, want_st))
                       if w) or assigned_line

    rows = [
        ("RECONCILIATION - this workbook against the rationale", ""),
        ("Assigned rating on this sheet (Stage 3, cells C36 / C37)", shown),
        ("Rating stated in the rationale", proposed),
        ("Do they agree?", "YES" if agree else "NO - RESOLVE BEFORE DELIVERY"),
        ("", ""),
        ("Financial anchor (Stage 1, cell C16)", anchor_grade),
        ("Hard cap tested", caps),
        ("Divergence anchor -> assigned, in notches (computed, C34)", divergence),
        ("", ""),
        ("The anchor is a SCREEN computed from the audited financials alone. Every notch "
         "between it and the assigned", ""),
        ("rating is itemised and justified in Stage 2 on this sheet - not asserted in prose. "
         "The notch count above is", ""),
        ("COMPUTED by the workbook; it is never typed, because the first two hand-typed notch "
         "counts in this project", ""),
        ("were both wrong (Godrej Properties said 9 where the chain gives 3 after the sector "
         "correction; Vodafone Idea", ""),
        ("said 12 where it was 9).", ""),
        ("", ""),
        ("The divergence on this case is argued in %s." % ref, ""),
        ("The rating decision belongs to the Rating Committee (Step 17c), not to this "
         "workbook.", ""),
        ("", ""),
        ("CONVENTION USED - %s ONLY. This workbook carries no other agency's definitions."
         % agency.upper(), ""),
        ("Operating-profit measure: %s. %s" % CONVENTION.get(
            agency, ("as filled", "convention not recorded for this agency")), ""),
    ]
    start = 55
    for i, (label, val) in enumerate(rows):
        r = start + i
        c = ws.cell(row=r, column=2, value=label or None)
        if i == 0:
            c.font = Font(bold=True, size=12, color=NAVY)
            for col in range(2, 7):
                ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor=AMBER)
        elif i <= 7:
            c.font = Font(size=10)
            v = ws.cell(row=r, column=3, value=val)
            v.font = Font(bold=True, size=10,
                          color=(RED if (i == 3 and not agree) else NAVY))
        else:
            c.font = Font(italic=True, size=9, color="555555")
        c.alignment = Alignment(vertical="top")

    ws.column_dimensions["B"].width = max(ws.column_dimensions["B"].width or 10, 62)
    wf.save(book)
    verdict = "MATCHES" if agree else "*** MISMATCH ***"
    return "assigned %s vs rationale %s -> %s | anchor %s (%s notch bridge) | scoped to %s (%d cleared)" % (
        got_grade, want_grade, verdict, anchor_grade, divergence, agency, stripped)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?", help="case slug; omit with --all")
    ap.add_argument("--all", action="store_true", help="every case that has a scorecard")
    ap.add_argument("--rating", help='override, e.g. "[ICRA]A- (Stable)"')
    ap.add_argument("--ref", default="the workpaper", help="where the divergence is explained")
    a = ap.parse_args(argv)
    sys.path.insert(0, str(ROOT))

    if a.all:
        slugs = sorted(d.name for d in (ROOT / "Companies").iterdir()
                       if [f for f in d.glob("Rating_Scorecard*.xlsx")
                           if not _superseded(f)])
    elif a.slug:
        slugs = [a.slug]
    else:
        ap.error("give a slug or --all")

    import recalc_workbook

    books, skipped, unverified = [], 0, []
    for slug in slugs:
        found = sorted(f for f in (ROOT / "Companies" / slug).glob("Rating_Scorecard*.xlsx")
                       if not _superseded(f))
        if not found:
            print("no scorecard in Companies/%s" % slug)
            continue
        # The agency is resolved PER WORKBOOK, not once per case. A case folder can hold more
        # than one scorecard - ITC was rated by all three agencies out of a single folder -
        # and reading the agency from found[0] would then write, say, the CareEdge rating onto
        # the ICRA workbook. That is the exact cross-agency defect this script exists to
        # prevent, arriving through its own back door. Found 01-Sep-2026 when ITC's three
        # scorecards were built.
        for b in found:
            rating = a.rating
            ref = a.ref
            if not rating:
                ag = None
                try:
                    from openpyxl import load_workbook
                    ag = load_workbook(b, data_only=True)["Inputs"]["C5"].value
                except Exception:                                         # noqa: BLE001
                    pass
                rating, src = rationale_for(slug, ag)
                ref = "%s and the workpaper" % src if src else a.ref
            if not rating:
                # No rationale yet - annotating with an unknown rating would be worse than not
                # annotating, so say so and move on rather than writing a placeholder.
                print("%-28s SKIPPED - no rationale found to read the proposed rating from"
                      % b.name)
                skipped += 1
                continue
            # Recalculate BEFORE annotating. The annotation quotes the anchor grade, the composite
            # and the index by reading them out of the workbook, and a scorecard fresh from
            # fill_scorecard.py holds formulas with no cached value - so annotating first writes a
            # block full of None. Found 01-Sep-2026 by rebuilding a scorecard from the template and
            # reading the block it produced: only the proposed rating, which comes from the
            # rationale rather than the workbook, survived.
            recalc_workbook.recalc(b)
            msg = annotate(b, rating, ref)
            print("%-28s %s" % (slug, msg))
            books.append(b)
            # A workbook that yields neither MATCHES nor MISMATCH was NOT verified.
            # It used to print "skipped" and still exit 0, so Step 18 - whose whole
            # instruction is "read its verdict" - reported success having checked
            # nothing. Found 04-Sep-2026: SBI's scorecard predates the three-stage
            # rebuild, has no Rating sheet, and passed this way on every run.
            if "MATCHES" not in msg and "MISMATCH" not in msg:
                unverified.append("%s (%s)" % (slug, msg))
    if not books:
        return 1 if skipped else 0

    # The annotation is written with openpyxl, which strips cached formula values - the exact
    # defect recalc_workbook.py exists to undo. Re-run it, or the workbook goes blank again.
    # Every workbook is recalculated even if an earlier one reports blanks. Returning early
    # here left the rest of the batch with NO cached values at all - so they displayed blank
    # outside Excel, which is the exact defect this step exists to prevent (found 02-Sep-2026
    # when Godrej Properties, verified minutes earlier, read back empty).
    failed = []
    for b in books:
        written, _ = recalc_workbook.recalc(b)
        have, miss = recalc_workbook.verify(b)
        print("recalculated %-49s %d cells written, %d still blank" % (b.name, written, miss))
        if miss:
            failed.append(b.name)
    if failed:
        print("STILL BLANK after recalculation: %s" % ", ".join(failed))
        return 1
    if unverified:
        print("NOT VERIFIED - Stage 3 could not be compared with the rationale: %s"
              % ", ".join(unverified))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
