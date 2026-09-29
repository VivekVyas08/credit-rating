"""Build Rating_Methodology_Guide.xlsx - the step-by-step guide to how a rating is produced here.

WHY THIS IS GENERATED, NOT HAND-TYPED
-------------------------------------
Every weight, threshold and formula in this workbook is READ OUT OF the artefact that actually
uses it - Rating_Scorecard.xlsx's own formula chain, the three agencies' methodology files, and
the tie-out engine - rather than retyped from memory. Retyping is how a guide drifts away from
the thing it documents. Re-run this script after changing the scorecard and the guide follows.

    python build_methodology_guide.py

LAYOUT RULE: ONE TABLE PER SHEET. Two tables on one sheet share the same columns, so their
widths overwrite each other and whichever is written second crushes the first - which is exactly
what happened to the first version of this workbook and was found by the clipping check, not by
looking at it. Row heights are COMPUTED from the text and the column width, never guessed,
because Excel auto-fits a wrapped cell only while its height has never been set, and does not
auto-fit a merged cell at all.

Sources, all inside this project:
  * Rating_Scorecard.xlsx            - Ratios / Scorecard / Rating / Ref_* sheets (weights, bands)
  * CLAUDE.md                        - the 19-step SOP and the 39 named failure modes
  * Methodology/927~ Financial Ratio Analysis, Sep 2024        (ICRA definitions)
  * CRISIL/Methodology/criteria-for-manufacturing-trading-...  (CRISIL Section IV definitions)
  * CareEdge/CORPORATE_CONVENTIONS.md, BROKING_CONVENTIONS.md  (CareEdge definitions)
  * common_tieouts.py, tieout_mutation.py, check_sections.py, preflight.py (the gates)
"""

import os
import sys

# This script takes no arguments and does its work at module level, so ANY argument used
# to be ignored and the build ran anyway - `--help` silently OVERWROTE the guide at the
# project root. Found 04-Sep-2026 while smoke-testing every tool's entry point: asking a
# script what it does must never be the thing that changes state.
if len(sys.argv) > 1:
    print(__doc__.strip().splitlines()[0])
    print("\nUsage: python tools/build_methodology_guide.py       (takes no arguments)")
    print("Rebuilds Rating_Methodology_Guide.xlsx at the project root, overwriting it.")
    sys.exit(0 if any(a in ("-h", "--help") for a in sys.argv[1:]) else 2)

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

NAVY = "1B2A4A"
TEAL = "0E7C86"
BAND = "F4F6F9"
AMBER = "FFF4E5"
# this script now lives in tools/, one level below the project root - moved here 01-Sep-2026.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "Rating_Methodology_Guide.xlsx")

THIN = Side(style="thin", color="C7D0DE")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

LINE_PT = 12.6          # one wrapped line at Calibri 10, with slack
CHARS_PER_UNIT = 1.05   # a column-width unit holds about one character of Calibri 10
NL = chr(10)


# ----------------------------------------------------------------------------- sheet helpers
def _lines(text, width_units):
    """Wrapped-line count for `text` in a column `width_units` wide, honouring hard newlines."""
    if not isinstance(text, str) or not text:
        return 1
    cap = max(4, int(width_units * CHARS_PER_UNIT) - 1)
    return sum(max(1, -(-len(para) // cap)) for para in text.split(NL))


def fit(texts, widths, pad=6.0, floor=15.0):
    """Row height that fits the tallest cell in the row."""
    n = max(_lines(t, w) for t, w in zip(texts, widths))
    return round(max(floor, n * LINE_PT + pad), 1)


def sheet(wb, name, title, subtitle, widths):
    """One sheet, one table. `widths` are the table's column widths, starting at column B."""
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    for j, w in enumerate(widths):
        ws.column_dimensions[get_column_letter(2 + j)].width = w
    total = sum(widths)
    last = 1 + len(widths)

    ws.merge_cells(start_row=2, start_column=2, end_row=2, end_column=last)
    c = ws.cell(row=2, column=2, value=title)
    c.font = Font(bold=True, size=15, color=NAVY)
    c.alignment = Alignment(vertical="center")
    ws.row_dimensions[2].height = fit([title], [total], pad=10, floor=24)

    ws.merge_cells(start_row=3, start_column=2, end_row=3, end_column=last)
    c = ws.cell(row=3, column=2, value=subtitle)
    c.font = Font(italic=True, size=10, color="555555")
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[3].height = fit([subtitle], [total])

    ws.freeze_panes = "B6"
    ws._guide_widths = widths
    return ws, 5


def header(ws, row, cols):
    widths = ws._guide_widths
    for i, c in enumerate(cols):
        cell = ws.cell(row=row, column=2 + i, value=c)
        cell.font = Font(bold=True, size=10, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor=NAVY)
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        cell.border = BORDER
    ws.row_dimensions[row].height = fit(cols, widths, pad=8, floor=28)
    return row + 1


def rows(ws, row, data, band=True):
    """Data rows carry NO explicit height, so Excel auto-fits the wrapped text itself.

    The one exception is a full-width section label: it is merged, and Excel does not auto-fit
    a merged cell, so that height is computed.
    """
    widths = ws._guide_widths
    span = len(widths)
    for i, rec in enumerate(data):
        if rec is None:                                   # spacer
            row += 1
            continue
        if isinstance(rec, str):                          # full-width section label
            ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=1 + span)
            for j in range(span):
                cell = ws.cell(row=row, column=2 + j)
                cell.fill = PatternFill("solid", fgColor=AMBER)
                cell.border = BORDER
            cell = ws.cell(row=row, column=2, value=rec)
            cell.font = Font(bold=True, size=11, color=TEAL)
            cell.alignment = Alignment(wrap_text=True, vertical="center")
            ws.row_dimensions[row].height = fit([rec], [sum(widths)], pad=8, floor=20)
            row += 1
            continue
        for j, v in enumerate(rec):
            cell = ws.cell(row=row, column=2 + j, value=v)
            cell.font = Font(size=10)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = BORDER
            if band and i % 2:
                cell.fill = PatternFill("solid", fgColor=BAND)
        row += 1
    return row


def note(ws, row, text, color=TEAL):
    """A footnote, merged across the whole table so a long sentence has somewhere to go."""
    widths = ws._guide_widths
    row += 1
    ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=1 + len(widths))
    c = ws.cell(row=row, column=2, value=text)
    c.font = Font(italic=True, size=9, color=color)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[row].height = fit([text], [sum(widths)])
    return row + 2


# ----------------------------------------------------------------- read the live scorecard
SC = load_workbook(os.path.join(ROOT, "Rating_Scorecard.xlsx"))


def ref_rows(sheet_name, first, last, ncols):
    ws = SC[sheet_name]
    out = []
    for r in range(first, last + 1):
        vals = [ws.cell(row=r, column=c).value for c in range(1, ncols + 1)]
        if any(v is not None for v in vals):
            out.append(vals)
    return out


BANDS = ref_rows("Ref_Bands", 5, 10, 8)
BANDS_FIN = ref_rows("Ref_Bands_Fin", 5, 10, 8)
WEIGHTS = ref_rows("Ref_Weights", 5, 26, 8)
QUAL = ref_rows("Ref_Qualitative", 6, 11, 4)
SCALE = ref_rows("Ref_Scales", 5, 21, 3)


def band_row(b):
    """Turn a five-threshold row into six readable buckets, respecting the direction."""
    metric, direction = b[0], b[1]
    t1, t2, t3, t4, t5, w = [float(x) for x in b[2:8]]
    pct = "%" in metric or "margin" in metric.lower()

    def f(v):
        return ("%.1f%%" % (v * 100)) if pct else ("%.2f" % v)

    if direction == "higher":
        cells = ["< " + f(t1), f(t1) + " - " + f(t2), f(t2) + " - " + f(t3),
                 f(t3) + " - " + f(t4), f(t4) + " - " + f(t5), ">= " + f(t5)]
    else:
        cells = ["> " + f(t5), f(t4) + " - " + f(t5), f(t3) + " - " + f(t4),
                 f(t2) + " - " + f(t3), f(t1) + " - " + f(t2), "<= " + f(t1)]
    return [metric, direction] + cells + [w]


BAND_COLS = ["Metric", "Direction", "Score 6" + NL + "(weakest)", "Score 5", "Score 4",
             "Score 3", "Score 2", "Score 1" + NL + "(strongest)", "Weight"]
BAND_W = [34, 11, 15, 15, 15, 15, 15, 15, 9]

wb = Workbook()
wb.remove(wb.active)

# ================================================================================ 00 README
ws, r = sheet(wb, "00_README", "How a rating is produced here - the complete guide",
              "Every weight, threshold and formula in this workbook is read out of the artefact "
              "that uses it. Nothing is retyped from memory. Regenerate with: "
              "python build_methodology_guide.py", [26, 60, 58])
r = header(ws, r, ["Sheet", "What it answers", "Where its content comes from"])
r = rows(ws, r, [
    "THE PROCESS",
    ["01_Process_19_Steps", "Every step followed, in order, with the artefact each one must "
     "produce and the gate that blocks the next step.", "CLAUDE.md Section 6 (Steps 1 to 21)."],
    "THE DEFINITIONS - binding, agency-published",
    ["02_Debt_Definitions", "How total debt, long-term debt and short-term debt are built: what "
     "is included, excluded and reclassified, for each of the three agencies.",
     "ICRA 927 Financial Ratio Analysis (Sep 2024); CRISIL Section IV; CareEdge "
     "CORPORATE_CONVENTIONS.md."],
    ["03_Ratio_Formulas", "Every ratio: the formula, how each term is built, what the ratio "
     "measures, and why it moves a rating.", "The three methodology sources above, plus "
     "Rating_Scorecard.xlsx's Ratios sheet for the exact cell arithmetic."],
    ["04_Agency_Differences", "The same item, three agencies, side by side - and the specific "
     "error that follows from using one agency's definition in another's report.",
     "The three methodology sources; failure modes 32 and 33 in CLAUDE.md."],
    "THE SCORING - this project's calibration, NOT agency-published",
    ["05_Weights_Blocks", "How much each of the four risk blocks counts, by sector.",
     "Rating_Scorecard.xlsx Ref_Weights, read live."],
    ["06_Weights_Ratios", "How much each of the six financial ratios counts inside the "
     "financial-risk block, and why each carries the weight it does.",
     "Rating_Scorecard.xlsx Ref_Bands, read live."],
    ["07_Threshold_Bands", "The numeric cut-offs that turn a ratio into a 1-to-6 score.",
     "Rating_Scorecard.xlsx Ref_Bands, read live."],
    ["08_Score_to_Grade", "The arithmetic from six ratios to a letter grade: composite, "
     "liquidity adjustment, power curve, support notches, hard caps.",
     "Rating_Scorecard.xlsx Scorecard and Rating sheets - the actual formulas."],
    ["09_LT_ST_Mapping", "The 17-notch scale and the long-term to short-term mapping, including "
     "the liquidity lift.", "Rating_Scorecard.xlsx Ref_Scales; empirical pairs across 655 ICRA "
     "reference rationales."],
    ["10_Qualitative_Rubric", "How the three judgment scores are anchored so two analysts score "
     "alike.", "Rating_Scorecard.xlsx Ref_Qualitative."],
    "LENDERS, VERIFICATION, AND A LIVE CASE",
    ["11_Financial_Sector", "The different metric set used for banks, NBFCs, HFCs and broking - "
     "and which metrics do NOT belong.", "CLAUDE.md failure modes 25, 28, 33 and 34."],
    ["12_Financial_Bands", "The scoring bands used in place of the corporate six when the "
     "entity is a lender.", "Rating_Scorecard.xlsx Ref_Bands_Fin, read live."],
    ["13_Verification", "How every number is proved before it reaches a report - tie-outs, "
     "mutation coverage and the two mechanical gates - plus what they actually reported on the "
     "live case.", "common_tieouts.py, tieout_mutation.py, preflight.py, check_sections.py."],
    ["14_Worked_Ratios", "Alembic Limited: every ratio formula instantiated with a real number, "
     "so nothing on sheet 03 is abstract.", "Companies/alembic-limited/compute_ratios.py."],
    ["15_Worked_Anchor", "The same case walked through the scoring chain of sheets 05 to 09, "
     "ending at a grade.", "The filled Rating_Scorecard_Alembic_Limited.xlsx."],
], band=False)

r = note(ws, r, "THE ONE DISTINCTION TO HOLD ON TO. Sheets 02, 03, 04 and 11 are "
                "AGENCY-PUBLISHED DEFINITIONS - binding, reproduced from the agencies' own "
                "criteria documents. If a definition there will not reproduce an agency's "
                "published figure, the definition is wrong, not the inputs (failure mode 32). "
                "Sheets 05 to 10 and 12 are THIS PROJECT'S OWN CALIBRATION: none of the three "
                "agencies publishes numeric block weights or threshold bands for corporates, so "
                "these were built and back-tested here, on 18-Jul-2026, against 396 rated "
                "issuers. They produce a SCREENING ANCHOR with a plus-or-minus two notch band - "
                "not a rating. Presenting them as agency criteria would be a misrepresentation.",
        color=NAVY)
r = note(ws, r, "The anchor is reliable to about one notch only in the A+ to BBB- range. It "
                "under-rates AA+ and AAA, and over-rates BB-and-below, unless the support notch "
                "and the qualitative rubric are applied. A divergence beyond two notches - or "
                "ANY divergence at AA+/AAA or at BB-and-below - is resolved by the rating "
                "committee, never by averaging the two answers.")
r = note(ws, r, "And the rating itself is a RATING COMMITTEE decision (Step 17c). The analyst "
                "PROPOSES at Step 15; a separate reviewer checks at Step 17b; the committee "
                "decides. The operator who runs the tool supplies documents and confirms inputs "
                "- and does not set the grade.")

# ===================================================================== 01 PROCESS, 19 STEPS
ws, r = sheet(wb, "01_Process_19_Steps", "The process, step by step",
              "Phases 1 to 8. A step is not complete until its named output exists - 'mostly "
              "done' does not exist here. Steps 1a and 17a are MECHANICAL gates: a script must "
              "exit zero before the next step may begin.", [6, 7, 23, 60, 40, 46])
r = header(ws, r, ["Phase", "Step", "Name", "What is actually done", "Required output",
                   "Gate / blocking condition"])
r = rows(ws, r, [
    "PHASE 1 - LEARN AND SCOPE (no numbers yet)",
    ["1", "1", "Input inventory", "Tabulate every document received: period covered, audited or "
     "unaudited, standalone or consolidated. List what is MISSING and how each gap will be "
     "handled. Declare the engagement type - new, surveillance, event-driven, withdrawal, "
     "provisional, or issuer-non-cooperating.", "The inventory table, shown to the operator, "
     "with a missing list and the handling for each item.", "Missing sanction letters or interim "
     "results must be asked for - never silently inherited from a prior report."],
    ["1", "1a", "PRE-FLIGHT (mechanical)", "Run preflight.py BEFORE reading anything. It "
     "searches the reference library and every uploaded document and prints what EXISTS: prior "
     "rating actions and their rated amounts, the annual report's own credit-rating note, "
     "subsidiaries, ESG data, instrument details, capex, promoter stake, auditor opinion, the "
     "sector KPI, aggregate-note contaminants, and any item appearing in two statements with "
     "different values.", "The pre-flight output, pasted VERBATIM into the workpaper Read Log.",
     "BINDING: anything the pre-flight reports PRESENT may never later be written as 'not "
     "available'. Only a second, recorded search can override it."],
    ["1", "1b", "Read every document in full", "Each file individually, end to end - not the "
     "financials alone. For a large annual report that means the MD&A, directors' report, risk "
     "factors, the auditor's report including Key Audit Matters and any Emphasis of Matter, "
     "contingent liabilities, the related-party note, borrowings notes, the segment note, the "
     "BRSR and the ratings disclosure.", "The Document Read Log - one row per file, listing the "
     "material items found in every relevant section.", "Drafting may not begin until the log "
     "covers every file. A file not in the log has not been read."],
    ["1", "2", "Route to methodology", "Entity type plus sector determines which methodology "
     "files apply.", "The named files, plus one line of routing logic.", "-"],
    ["1", "3", "Read the methodology in full", "The applicable sector or entity methodology plus "
     "the cross-cutting files - consolidation, liquidity, parent support, hybrids, outlook "
     "policy, default recognition, complexity - THIS session.", "The list of rating factors that "
     "will structure the analysis.", "VERIFY EACH SCOPE STATEMENT. Citing a methodology whose "
     "scope excludes the entity is failure mode 4. On the live case the Investment Companies "
     "methodology was rejected on exactly this test."],
    ["1", "4", "Learn craft from PEERS", "Read two or three reference rationales of close peers. "
     "Record which metrics the sector narrative quotes, the driver taxonomy, what earns AAA "
     "rather than A in this sector, and the liquidity-argument style.", "Sector-craft notes.",
     "Extract ZERO facts. Do NOT open the company's own prior report yet."],
    "PHASE 2 - INDEPENDENT DATA WORK (company documents only)",
    ["2", "5", "Extract into code", "Every line item from the audited statements into "
     "compute_ratios.py. Units are written at extraction and converted INLINE - a separate "
     "conversion pass creates a stale copy that the mutation harness cannot reach. Both bases "
     "are captured where they exist, and the basis is chosen per the Consolidation methodology, "
     "not by the operator.", "The extraction script, plus a generated Financial Spreads workbook "
     "with Extraction, RatioSuite and TieOut tabs.", "The script is the single source of truth. "
     "The Excel is generated FROM it, and never hand-typed."],
    ["2", "6", "Compute the full ratio suite", "Profitability, leverage, coverage, working "
     "capital and cash flow over three to five years, in the selected agency's conventions. A "
     "ratio that is not meaningful is marked n/m with its reason, never silently dropped.",
     "The computed table, plus a component-level tie-out note.", "External tie-out: headline "
     "figures reconciled against an independent public source AND against the annual report's "
     "own headline metrics. A component-level tie-out catches the single-cell error that a "
     "matching grand total hides."],
    ["2", "7", "Trace every qualitative claim", "Shareholding, board, order book, concentration "
     "computed from the segment note rather than asserted, contingent liabilities and their "
     "movement, capex and its funding, litigation, auditor observations, the subsidiary list "
     "with stakes, instrument terms.", "A qualitative fact register with a source location for "
     "every claim.", "Traced is not verified. Where a second source exists it must be grepped "
     "and reconciled - a figure can be perfectly traceable to a real document and still be "
     "wrong, because the source was an OCR'd chart or a mis-aligned row."],
    ["2", "7b", "Extract instrument details", "Search the annual report for ISINs, NCD coupons "
     "and amounts, commercial paper outstanding, and the credit-rating note. A rated amount not "
     "in the issuer's own documents may be imported from a CRA publication only if all five "
     "conditions below this table are met.", "The Annexure I instrument table, plus a one-line "
     "borrowings-versus-rated-amount reconciliation.", "A rated amount is a LIMIT; balance-sheet "
     "borrowings are DRAWN debt. They differ, and must never be conflated in either direction "
     "(failure modes 13 and 31)."],
    ["2", "8", "Materiality sweep", "Walk every section the analysis has not touched, in every "
     "file, hunting for regulatory or tax change, exceptional items, settlements, guarantees, "
     "related-party movements, governance gaps, restatements, capex, JV or M&A events, and "
     "covenant disclosures.", "The sweep list, with a written include-or-exclude decision and "
     "reason for each finding.", "Materiality is DEFINED: at least 1% of tangible net worth, or "
     "at least 5% of PBT, or plausibly worth one notch, or ANY regulatory, governance, default, "
     "covenant, fraud or going-concern item regardless of size."],
    ["2", "9", "Save the workpaper", "Computed suite, trend commentary, fact register, sweep "
     "decisions, caveats.", "Company_Ratio_Workpaper_date.md", "-"],
    "PHASE 3 - INDEPENDENT ANALYSIS AND RATING VIEW",
    ["3", "10", "Apply the methodology factor by factor", "Industry, then business, then "
     "financial, then management and governance, then ESG - filling a compliance map as you go.",
     "The Methodology Compliance Map: every rating factor named as the methodology names it, the "
     "company's evidence, the assessment against the indicative band, and its weight in the "
     "conclusion.", "Every indicative-metrics table in the applicable methodology must appear, "
     "scored with actual numbers or marked data-unavailable. A rating view without its map is "
     "redone."],
    ["3", "11", "Liquidity", "Sources-versus-claims arithmetic over roughly twelve months.",
     "The computation, and only then the descriptor.", "The descriptor is the CONCLUSION of the "
     "arithmetic, never an adjective chosen first. And cash is not liquidity until it is shown "
     "to be UNENCUMBERED (failure mode 34)."],
    ["3", "12", "Forward view", "The default is a five-year three-statement model with a Credit "
     "Ratios tab and a Debt Breakup tab, plus a stress case flexing the variables the "
     "methodology names. A lighter treatment is allowed, but must be JUSTIFIED IN WRITING.",
     "The model - or a scaled artefact plus a step12_scaling_decision recorded in case.json.",
     "MECHANICAL: check_sections.py fails any case folder with neither a model nor a recorded "
     "scaling decision. A rating is a forward-looking opinion; shipping one with no forward view "
     "is a different job, not a lighter one (failure mode 35)."],
    ["3", "12b", "Fill the scorecard (the ANCHOR)", "Copy Rating_Scorecard.xlsx into the case "
     "folder and fill every input cell FROM THE EXTRACTION SCRIPT - never retyped. Score the "
     "three qualitative factors against the rubric, with one written justification each.",
     "The filled workbook, plus a note in the workpaper stating the anchor grade and the "
     "justifications.", "The anchor is a SCREENING cross-check with a two-notch band. It is not "
     "the rating. See sheets 05 to 09."],
    ["3", "12c", "Scope the workbook to ONE agency, then annotate and recalculate it",
     "Rating_Scorecard.xlsx is a TRI-AGENCY TEMPLATE - it carries the ICRA, CRISIL and CareEdge "
     "scales, bands and operating-profit conventions side by side, and its Rating sheet prints "
     "the anchor formatted exactly like an assigned rating. A filled copy is NOT deliverable as "
     "it stands. Run: python annotate_scorecard.py <case-slug>. It clears the other two "
     "agencies' rows and states only the rating agency's own convention; writes the proposed "
     "rating from the rationale beside the anchor grade, with the support notches, the pre-cap "
     "index and the hard cap applied; and recalculates the cached formula values so the "
     "workbook is readable outside Excel.",
     "A single-agency workbook that explains its own divergence on its face.",
     "MECHANICAL: three check_sections.py probes - cached values present, anchor annotated, and "
     "no agency named other than the one being rated. Order is recalculate, annotate, "
     "recalculate: openpyxl saves formulas with no cached value, so an un-recalculated workbook "
     "displays BLANK outside Excel, and annotating first quotes None for every figure it reads "
     "(failure mode 40)."],
    ["3", "13", "Form the rating view", "Standalone assessment, then support notching with the "
     "criteria quoted verbatim, then instrument-level adjustments, then the long-term to "
     "short-term mapping consistency check, then the outlook per the outlook policy.",
     "The written view, with its chain of reasoning.", "This happens BEFORE the company's own "
     "prior report is opened."],
    ["3", "14", "Only NOW open the prior report", "Compare rating, outlook, drivers, liquidity "
     "descriptor and figures against the independent view.", "A divergence table - every "
     "difference explained as: my analysis found something, or this postdates the anchor, or I "
     "correct my view, with the reason.", "Mandate details found only in the anchor are flagged "
     "as requiring issuer confirmation. If no prior report exists, benchmark against peers and "
     "say so."],
    ["3", "15", "Analytical package", "Present the gaps and their handling, the assumptions, the "
     "stress result, the PROPOSED view, the divergence and peer tables, the anchor divergence, "
     "amounts needing confirmation, and every judgment call.", "The package, in chat.",
     "This is completeness sign-off, NOT grade approval. The grade is decided at Step 17c."],
    "PHASE 4 - DRAFTING",
    ["4", "16", "Draft the rationale", "Start from the report skeleton, in the correct agency's "
     "variant, using the sector narrative conventions learned at Step 4.", "The rationale, in "
     "the agency's own section order and house style.", "Every number COPIED from the workpaper "
     "output - never retyped from notes, from memory, or from the anchor."],
    ["4", "17", "Re-verify the draft", "Numbers drift while writing. Re-run the script against "
     "every number appearing in the draft.", "TWO drift-check results: computed figures against "
     "the script, AND non-computed figures - segment mix, capacity, order book, shareholding, "
     "contingent-liability quanta - against source plus a corroborating second source.",
     "A single 'all figures match' that silently covers only the computed set is failure mode 8: "
     "verification claimed but not evidenced."],
    ["4", "17a", "SECTION AUDIT (mechanical)", "Run check_sections.py. It is agency-aware and "
     "matches section HEADERS only. It also runs quality probes: the ESG section carries a "
     "company-disclosed number; the liquidity descriptor is named; the rated amount is stated or "
     "explicitly marked to-be-confirmed; CRA-published amounts are date-stamped; Annexure I "
     "lines sum to their total; operating-profit normalisation is stated; there is no verbatim "
     "reuse of an agency publication; absence claims are evidenced.", "A zero exit code.",
     "A NON-ZERO EXIT BLOCKS DELIVERY. When a check fires, verify the finding against the "
     "document before 'fixing' it - a checker is evidence, not a verdict."],
    "PHASE 5 - DECISION AND GOVERNANCE (the rating is MADE here)",
    ["5", "17b", "Independent reviewer (four eyes)", "A reviewer separate from the analyst "
     "re-ties the numbers and checks methodology fit and scope, that the basis is the "
     "methodology's basis, that materiality was applied, that the anchor divergence was resolved "
     "rather than buried, and that every mandated disclosure is present.", "Sign-off, or a "
     "return list naming the failing step.", "A return sends the case back to the failing step, "
     "not forward."],
    ["5", "17c", "RATING COMMITTEE", "The committee, separate from the analyst, decides the "
     "rating and outlook on the complete, re-verified package - the draft included.",
     "Minutes: members, proposed versus decided rating, vote, dissent, express resolution of the "
     "anchor divergence, and the decision rationale.", "A material number change loops the case "
     "back to Step 17."],
    "PHASES 6 TO 8 - ISSUER REVIEW, DELIVERY, SURVEILLANCE",
    ["6", "18b", "Issuer factual review", "Share the draft for factual accuracy only - not grade "
     "negotiation. Handle any appeal through a fresh committee look. Confirm no material event "
     "between the data cut-off and publication.", "Corrections or none; the appeal outcome; a "
     "clean bring-down.", "-"],
    ["7", "18", "Deliver", "Report, workpaper, spreads, model, scorecard and committee minutes "
     "together - with the data-cut-off limitation, the computation-basis footnotes and the "
     "caveats INSIDE the report.", "The delivered set.", "Never a bare file: each artefact ships "
     "with written reasoning."],
    ["7", "19", "Log lessons the same day", "Any mistake found at any stage becomes a rule.",
     "A new entry in the failure-mode list.", "META-RULE: no failure mode may be added as prose "
     "alone. It must ship with a probe in preflight.py, a rule in check_sections.py, or an "
     "explicit written statement of why no mechanical check is possible."],
    ["8", "20-21", "Surveillance", "Record the next scheduled review - at least annual - the "
     "triggers forcing an event-driven review, the one-day-one-rupee default-monitoring "
     "obligation, and the data feed. On schedule or on a trigger, re-run as a surveillance "
     "engagement.", "A surveillance register entry.", "A rating is a living opinion. Delivery "
     "sets up monitoring; it does not close the file."],
])
r = note(ws, r, "THE FIVE CONDITIONS for importing a rated-amount table from a CRA publication "
                "(Step 7b). (1) That CRA's primary published rationale for THIS issuer is "
                "available - the reference library counts. (2) It is reproduced VERBATIM, every "
                "line, with the publication DATE stamped in the report. (3) It is labelled "
                "CRA-published, not issuer-confirmed, with issuer confirmation recorded as "
                "outstanding. (4) The line-integrity arithmetic is verified: the lines sum to "
                "the published total. (5) The rated-limits-versus-drawn-debt distinction is "
                "stated explicitly. Absent any one of the five, the amount is marked 'to be "
                "confirmed by issuer'. Nothing else may be imported from a CRA publication - not "
                "a fact, not a figure, not a phrasing.")

# ======================================================================= 02 DEBT DEFINITIONS
ws, r = sheet(wb, "02_Debt_Definitions", "Debt: what counts, and why the split matters",
              "Debt is the single most consequential definition in a rating. It is the numerator "
              "of gearing, of debt-to-EBITDA and of net debt, and the denominator of "
              "accruals-to-debt - so getting it wrong moves every leverage ratio at once.",
              [28, 46, 46, 46])
r = header(ws, r, ["", "ICRA", "CRISIL", "CareEdge"])
r = rows(ws, r, [
    "THE TOTAL-DEBT DEFINITION, THREE WAYS",
    ["Term used", "Total Debt", "Adjusted total debt", "Total debt"],
    ["Published definition",
     "Long-term and short-term debt, plus lease liabilities, plus off-balance-sheet liabilities "
     "such as receivables discounted, plus the debt component of hybrid instruments as assessed "
     "by ICRA on the instruments' contractual terms.",
     "All forms of debt: short-term and long-term borrowings, off-balance-sheet liabilities, "
     "preference shares, subordinated debt, optionally convertible debentures, deferred payment "
     "credit and bills discounted. Guarantees, factored receivables, pension liabilities, "
     "derivatives and contingent liabilities are EVALUATED - the likelihood of devolvement and "
     "the recoverability of exposures, including management intent, are assessed before "
     "anything is included.",
     "All short- and long-term debt, redeemable preference capital, optionally convertible "
     "debentures, interest-free loans, foreign-currency loans, vehicle loans, fixed deposits, "
     "unsecured loans, commercial paper, inter-corporate borrowings, borrowings from promoters, "
     "associates and group entities, bills discounted, ACCEPTANCES AND CREDITORS ON LC (capex "
     "LCs included), LEASE LIABILITY, and mobilisation advances backed by financial bank "
     "guarantees."],
    ["Excluded or netted off",
     "Cash reserves EARMARKED for servicing specific debt - a DSRA - are netted off gross debt "
     "to give net leverage, and are then NOT counted again in the liquidity assessment.",
     "Not separately specified; the evaluation approach above governs.",
     "Debt fully backed by dedicated or lien-marked fixed deposits, or by cash margin."],
    ["Reclassified into equity",
     "The equity component of hybrids, as assessed on their contractual terms.",
     "Not separately specified.",
     "Promoter and related-party borrowings SUBORDINATED to outside loans move into tangible net "
     "worth - but their interest expense stays a normal interest expense."],
    ["The adjusted (stressed) variant",
     "Adjusted gearing, netting investments in group entities out of net worth - for the case "
     "where a low headline gearing is an artefact of a lending-margin structure rather than a "
     "virtue.",
     "Guarantees and loans extended to group entities are assessed for devolvement and folded "
     "into the gearing calculation.",
     "Any corporate guarantee given to lenders of subsidiaries or group entities is ADDED for "
     "adjusted leverage. Gearing is also adjusted for exposure to group entities, and the impact "
     "of non-fund-based limits availed is weighed."],
    ["Hybrid treatment", "Equity credit assigned instrument by instrument on contractual terms.",
     "Preference shares and optionally convertible debentures counted as debt.",
     "Redeemable preference shares are DEBT - fixed tenure, fixed dividend - unless issued to "
     "promoters and redeemable only after the outstanding term debt, in which case quasi-equity. "
     "Compulsorily convertible instruments are QUASI-EQUITY unless the investor has an exit "
     "option or conversion is conditional. Optionally convertible instruments are DEBT, because "
     "redemption cannot be ruled out until conversion actually happens."],
    None,
    "WHY THE LONG-TERM / SHORT-TERM SPLIT IS MADE AT ALL",
    ["The two different questions",
     "Long-term debt asks whether the capital structure is sound over the life of the assets it "
     "funds. Short-term debt asks whether the company survives the next twelve months. A company "
     "can be comfortably geared and still default because its short-term book will not roll - "
     "which is precisely why liquidity is a separate step (Step 11) with its own descriptor, "
     "rather than an output of the leverage ratios.", "", ""],
    ["Long-term debt", "Non-current borrowings per the balance sheet, PLUS the current maturities "
     "of long-term debt (which the balance sheet reports inside current liabilities), PLUS "
     "non-current lease liabilities.",
     "The same components. CRISIL's cash DSCR references 'debt payable within one year' "
     "explicitly in its denominator, so current maturities must be identified separately "
     "whatever else is done with them.",
     "The long-term debt-equity ratio is explicitly defined as total LONG-TERM debt INCLUDING "
     "ITS CURRENT PORTION, over tangible net worth - so current maturities stay with the "
     "long-term book for that particular ratio."],
    ["Short-term debt", "Current borrowings: working-capital facilities such as cash credit and "
     "overdraft, short-term loans, commercial paper, bills discounted, and current lease "
     "liabilities.",
     "The same, plus factored receivables and deferred payment credit where present.",
     "The same, plus acceptances and creditors on LC - which makes CareEdge's short-term "
     "definition the widest of the three, and is the most common single reason a CareEdge "
     "gearing will not reproduce."],
    ["The trap that keeps recurring",
     "A rating attaches to a SANCTIONED FACILITY, not to a drawdown. A long-term/short-term "
     "facility carries a long-term rating whether it is drawn long, drawn short, or entirely "
     "undrawn. 'All drawn borrowings mature inside twelve months' therefore says NOTHING about "
     "whether a long-term rating exists - and inferring otherwise once removed an entire "
     "long-term rating, its outlook and its rating action from a report (failure mode 31).",
     "The mirror image is equally wrong: presenting sanctioned limits as though they were drawn "
     "debt overstates leverage (failure mode 13). Rated limits include undrawn non-fund-based "
     "and unallocated lines; drawn debt does not. State both, and expect them not to match.",
     "The rating table carries LIMITS, or the words 'to be confirmed by issuer' - never an "
     "outstanding balance. Outstandings belong in the financial indicators and in the liquidity "
     "section. A rated limit is almost never in an annual report; it lives in the CRA press "
     "release, so 'not found in the issuer's documents' is the EXPECTED state for that data "
     "item, not a finding about it."],
    None,
    "WORKED EXAMPLE - Alembic Limited, standalone, as on 31-Mar-2026 (Rs crore)",
    ["Non-current borrowings (note 18)", "6.61",
     "Balance sheet, non-current financial liabilities.", "LONG-TERM"],
    ["Current borrowings (note 22)", "4.03", "Balance sheet, current financial liabilities.",
     "SHORT-TERM"],
    ["Lease liabilities", "Nil", "No lease-liability line is disclosed separately on either "
     "basis in any year - searched. ICRA's convention includes leases; here there is nothing to "
     "include, and that nil is DECLARED in the engine, so it fails the moment someone changes it "
     "without revisiting the note.", "-"],
    ["Off-balance-sheet / discounted receivables", "Nil", "None disclosed.", "-"],
    ["Debt component of hybrids", "Nil", "No hybrid instrument outstanding.", "-"],
    ["TOTAL DEBT", "10.64", "= 6.61 + 4.03. Reconciles to the standalone balance sheet.", ""],
    ["Less: unencumbered cash and liquid investments", "(92.02)",
     "Cash 1.10 + other bank balances 1.87 + current investments 89.05. No lien or encumbrance "
     "is disclosed against any of the three - CHECKED in notes 10, 12 and 13, not assumed.", ""],
    ["NET DEBT", "(81.38)", "A net CASH position, and it has deepened every year: (3.90) in "
     "FY2024, (39.30) in FY2025, (81.38) in FY2026.", ""],
    ["Rated LIMITS, for contrast", "56.4", "20.9 + 25.5 + 10.0, per the CRA's published action "
     "of 30-May-2025. A different measure from the 10.64 crore of drawn debt, and the report "
     "says so explicitly.", ""],
])
r = note(ws, r, "Why the definition matters more than it looks. On this issuer, substituting "
                "rated limits (Rs 56.4 crore) for drawn debt (Rs 10.64 crore) would move gearing "
                "from 0.01x to 0.07x, and Total debt/OPBDIT from 0.12x to 0.64x. Neither changes "
                "the grade HERE, because the company sits so far from any threshold. On an "
                "issuer sitting at 2.5x, the same substitution is a two-notch error.")

# ========================================================================= 03 RATIO FORMULAS
ws, r = sheet(wb, "03_Ratio_Formulas", "Every ratio: formula, meaning, and why it rates",
              "Each row gives the exact arithmetic, how each term is built, what the ratio is "
              "trying to see, and the specific way it moves a rating. Sheet 14 instantiates "
              "every one of these with a real number.", [25, 38, 50, 60, 42])
r = header(ws, r, ["Ratio", "Formula", "How each term is built",
                   "What it measures, and why it matters for the rating", "Agency variation"])
r = rows(ws, r, [
    "PROFITABILITY - can the business generate a surplus at all",
    ["Operating margin" + NL + "(OPBDIT/OI, EBITDA margin, PBILDT/TOI)",
     "Operating profit / Operating income",
     "ICRA: OPBDIT = PBT + finance cost + depreciation - other income, with other income "
     "stripped UNCONDITIONALLY. CRISIL: the operating measure RETAINS recurring non-operating "
     "income. CareEdge: PBILDT = TOI less all operating expenses, with interest, dividend and "
     "rental income excluded from TOI even when recurring.",
     "The first line of defence. Margin is the room between revenue and the cost base before "
     "interest is even reached, so it sets how far revenue can fall before coverage breaks. A "
     "margin that is high AND stable across a cycle is worth more than a higher one that swings "
     "- a rating is about the bad year, not the average one.",
     "MATERIAL. Conflating ICRA's and CRISIL's treatment of other income is failure mode 32 and "
     "33. On the live case this single choice moved the FY2025 margin from 41.78% to 55.5%."],
    ["PAT margin", "Profit after tax / Operating income",
     "PAT as reported - after tax, after exceptional items, and (on a consolidated basis) after "
     "the associate pick-up.",
     "The bottom-line survivor of everything above it: interest, depreciation, tax and one-offs. "
     "CRISIL treats it as the most cross-industry-comparable profitability measure, precisely "
     "because operating margins carry industry-specific characteristics that make them "
     "incomparable between sectors.", "Broadly common to the three."],
    ["Return on capital employed (ROCE)",
     "PBIT / (Total debt + Tangible net worth + Deferred tax liability)",
     "ICRA's capital employed also DEDUCTS capital work-in-progress and capital advances - work "
     "that is not yet earning should not sit in the denominator. CareEdge uses AVERAGE capital "
     "employed and folds other comprehensive income into the numerator.",
     "Whether the business earns more than its capital costs. A company earning below its cost "
     "of debt is destroying the very cushion that services that debt - which is why a low ROCE "
     "at high leverage is a far worse signal than either reading taken alone.",
     "CareEdge: average capital, includes OCI, annualised by 12/months. Note that deferred tax "
     "sits INSIDE the ROCE denominator while being excluded from net worth for gearing - the "
     "same split CRISIL applies."],
    "LEVERAGE - how much of the balance sheet is other people's money",
    ["Gearing / overall gearing", "Total debt / Tangible net worth",
     "Numerator per sheet 02. Denominator: net worth LESS revaluation reserves and miscellaneous "
     "expenditure not written off, PLUS minority interest, share application money and the "
     "equity component of hybrids. Deferred tax liability is NOT in shareholders' funds - it "
     "arises from timing differences that are expected to reverse.",
     "The headline measure of dependence on borrowed funds. Borrowed money carries fixed "
     "obligations whatever the cash generation; equity does not. Lower gearing means more room "
     "to absorb a downturn AND more capacity to raise fresh capital when one arrives - and the "
     "second effect is why gearing matters even for a company with ample current coverage.",
     "CareEdge INCLUDES acceptances and creditors on LC in the numerator, the widest of the "
     "three. All three exclude revaluation reserves from the denominator."],
    ["Total outside liabilities / TNW" + NL + "(total indebtedness ratio)",
     "Total outside liabilities / Tangible net worth",
     "TOL = total debt plus ALL other external liabilities: deferred tax liability, creditors, "
     "and operating and non-operating liabilities. CareEdge nets DTL and DTA out of TOL.",
     "Gearing's blind spot, corrected. A company funding working capital through non-fund-based "
     "lines or stretched supplier credit shows a flattering gearing, because neither appears in "
     "borrowings. TOL/TNW normalises that away and shows the total claims on the balance sheet.",
     "Near-identical across the three; CareEdge alone nets deferred tax out."],
    ["Total debt / operating profit" + NL + "(debt-to-profit)", "Total debt / Operating profit",
     "Both terms as defined above; the profit term inherits whichever agency's operating-profit "
     "convention is in force.",
     "How many years of current operating profit the debt represents. It is the leverage ratio "
     "that speaks in time rather than in proportion, which is why it travels across balance "
     "sheets of very different sizes. Read it WITH the repayment schedule: two companies at the "
     "same multiple carry different risk if one amortises over three years and the other over "
     "ten.",
     "Called Total debt/OPBDIT by ICRA, Debt/PBDIT by CRISIL, Total debt/PBILDT by CareEdge. "
     "Same arithmetic; the profit term differs as above."],
    ["Net cash accruals to total debt" + NL + "(NCATD, accruals-to-debt)",
     "(PAT + Depreciation - Dividend) / Total debt",
     "Dividends on both equity and preference shares are CHARGED OFF. The ratio deliberately "
     "treats payouts as non-discretionary and sticky rather than as a buffer that could be "
     "withdrawn.",
     "Its reciprocal is the number of years needed to repay the debt out of current accruals. "
     "Most informative where debt amortises and dividends are sticky. Read with the debt "
     "maturity profile: a high ratio still leaves refinancing risk if the average maturity is "
     "short.",
     "Common to all three. CareEdge excludes right-of-use depreciation from the add-back while "
     "still deducting it in PAT - an asymmetry that has to be applied deliberately, or gross "
     "cash accruals inflate."],
    "COVERAGE - can the cash flow actually service the obligations",
    ["Interest coverage", "Operating profit / Gross interest expense",
     "GROSS interest - interest income from loans and advances is NOT netted off. CareEdge "
     "additionally deducts amortisation of debenture premium and capitalised interest from the "
     "denominator.",
     "The cushion between operating profit and the cost of debt. Below 1.0x the company cannot "
     "cover even interest from operations, and default probability is high. At 10x, profits must "
     "collapse before interest is threatened. It does NOT tell you whether anything is left for "
     "PRINCIPAL - which is why DSCR exists, and why this ratio is most informative where debt is "
     "non-amortising.",
     "The denominator detail differs (the CareEdge deductions); the numerator inherits the "
     "agency's operating-profit convention."],
    ["Debt service coverage ratio (DSCR)",
     "(PAT + Gross interest + Depreciation) / (Gross interest + Repayment + Preference dividend)",
     "The denominator is the FULL fixed obligation for the period, principal included. CareEdge "
     "subtracts internal accruals committed to capex from the numerator, and adds standalone "
     "commercial paper and short-term repayment to the denominator.",
     "The complete debt-service question that interest coverage only half answers. Below 1.0x "
     "the company cannot meet its obligations from internal accruals and depends on refinancing "
     "- which is a market-access assumption, not a fundamental one, and it can be withdrawn "
     "exactly when it is most needed.",
     "CRISIL's cash DSCR deducts 25% of the incremental net working capital. CareEdge's deducts "
     "25% of the working-capital INCREASE, the other 75% assumed funded by working-capital "
     "borrowing."],
    "LIQUIDITY AND WORKING CAPITAL - survival over the next twelve months",
    ["Current ratio",
     "Current assets (incl. marketable securities) / Current liabilities (incl. current "
     "maturities of long-term debt)",
     "Both sides built from balance-sheet components. The current maturities of long-term debt "
     "must be INSIDE current liabilities, or the ratio flatters.",
     "The crudest near-term solvency check, useful mainly as a cross-check on the "
     "working-capital cycle. Its weakness is that it treats slow-moving inventory as though it "
     "were cash.", "Common to the three."],
    ["Working-capital cycle (days)", "Inventory days + Collection days - Creditor days",
     "CareEdge is explicit that each leg uses AVERAGE(t, t-1) x 30 x number of months over the "
     "relevant cost or sales base - not a closing-balance snapshot.",
     "How long cash is trapped between paying for an input and collecting for the output. A "
     "lengthening cycle consumes cash even in a profitable, growing company - which is the "
     "classic route to a liquidity default with healthy reported earnings.",
     "CareEdge specifies the averaging explicitly; the others apply it as practice."],
    ["Net debt", "Total debt - unencumbered cash and liquid investments",
     "UNENCUMBERED is the load-bearing word. Excluded: DSRA balances, margin money, deposits "
     "earmarked against a facility, and investments in or loans to GROUP entities - the last "
     "because their availability depends on the group entity's own credit profile.",
     "Debt net of what could repay it tomorrow. The discipline is entirely in the exclusions: "
     "counting encumbered cash as liquidity overstates the position, and doing so has produced "
     "an 18-fold overstatement in this project's own past work (failure mode 34).",
     "All three exclude encumbered cash; CareEdge documents the exclusion list most explicitly."],
    ["Gross cash accruals days (GCA days)",
     "Total current assets related to operations / Operating income",
     "Operations-related current assets only.",
     "Working-capital intensity expressed in days of revenue. It is the sector-defining metric "
     "for distribution and trading businesses, where the rating turns on how much capital the "
     "business must carry to move a rupee of goods.",
     "A CRISIL emphasis; reported for traders and distributors."],
])
r = note(ws, r, "A ratio that is not meaningful for the entity is marked n/m WITH ITS REASON, "
                "never silently omitted. And a metric belonging to another sector is not reported "
                "at all: cost-to-income for an NBFC, gearing for a bank, or RevPAR for a "
                "manufacturer is arithmetic that is correct and answers the wrong question "
                "(failure mode 28). The exclusion itself must cite a published report of THAT "
                "agency in THAT sector - never a rule generalised from a different one (failure "
                "mode 33). See sheet 11.")

# ====================================================================== 04 AGENCY DIFFERENCES
ws, r = sheet(wb, "04_Agency_Differences", "The same item, three agencies",
              "Where the three diverge - and the specific error that follows from carrying one "
              "agency's definition into another agency's report.", [22, 38, 36, 50, 46])
r = header(ws, r, ["Item", "ICRA", "CRISIL", "CareEdge",
                   "What goes wrong if this is got wrong"])
r = rows(ws, r, [
    ["Operating profit is called", "OPBDIT", "EBITDA / PBDIT / OPBDIT", "PBILDT",
     "Cosmetic on its own - but the label signals a different computation underneath it."],
    ["Other income in operating profit",
     "STRIPPED UNCONDITIONALLY. OPBDIT = PBT + finance cost + depreciation - other income.",
     "RECURRING non-operating income is RETAINED in the operating measure.",
     "Interest, dividend and rental income are EXCLUDED from TOI even when recurring. "
     "Core-related items ARE included: job-work income, scrap sales, duty drawback, export "
     "incentives, cash discount received, and non-debt foreign-exchange gain.",
     "THE MOST CONSEQUENTIAL DIFFERENCE ON THIS SHEET. On the live case it moved FY2025 "
     "operating income from Rs 214.36 crore to Rs 280.6 crore, and the margin from 41.78% to "
     "55.5% - with PAT identical on both readings."],
    ["Indirect taxes in revenue", "Per the issuer's Ind AS presentation.",
     "Per the issuer's Ind AS presentation.",
     "GST, excise, sales tax and service tax are NETTED OFF gross sales to reach core sales.",
     "Reading excise as an expense line leaves revenue gross of excise - the issuer's "
     "presentation, not CareEdge's TOI. Every margin then reads low."],
    ["Tangible net worth",
     "Net worth, less revaluation reserves and miscellaneous expenditure not written off, plus "
     "minority interest, share application money and the equity component of hybrids.",
     "Adjusted networth: net worth adjusted for revaluation reserves and for miscellaneous "
     "expenditure that has not been written off.",
     "CORPORATE: includes subordinated promoter loans, share warrants, share application money, "
     "ESOPs outstanding and minority interest; excludes revaluation reserve; deducts "
     "miscellaneous expenditure and accumulated losses; excludes intangibles EXCEPT where "
     "critical to core operations - telecom licence fees, mining surface rights, media rights, "
     "and intellectual property in IT and pharma. FINANCIAL SECTOR: deducts deferred tax assets "
     "AND all intangibles, with no critical-to-operations exception.",
     "CareEdge's two definitions DIFFER, and carrying the corporate one into a broking case "
     "produced a published net worth roughly Rs 99 crore too high and a gearing 0.44x too low "
     "(failure mode 32)."],
    ["Acceptances and creditors on LC",
     "Treated per methodology; not named in the base total-debt definition.",
     "Evaluated as an off-balance-sheet item, with the likelihood of devolvement assessed.",
     "INCLUDED in total debt outright, capex LCs included.",
     "Omitting them understates CareEdge gearing. Including them silently in an ICRA computation "
     "is an undisclosed divergence (failure mode 6) - it must be footnoted."],
    ["Lease liability", "INCLUDED in total debt.",
     "Included within 'all forms of debt' and the off-balance-sheet assessment.",
     "INCLUDED in total debt, and interest on the lease liability is a finance charge. But "
     "right-of-use depreciation is deducted in PAT and NOT added back in GCA.",
     "The CareEdge GCA asymmetry is easy to miss, and inflates gross cash accruals if the "
     "add-back is made out of habit."],
    ["Rating symbol style", "[ICRA]AA- (Stable) / [ICRA]A1+", "Crisil AA-/Stable / Crisil A1+",
     "CARE AA-; Stable / CARE A1+",
     "The wrong prefix or punctuation immediately marks the report as not that agency's."],
    ["Liquidity descriptors", "Superior / Strong / Adequate / Stretched / Poor",
     "Superior / Strong / Adequate / Stretched / Poor",
     "Superior-Strong / Adequate / Stretched / Poor",
     "The descriptor must be the CONCLUSION of the sources-versus-claims arithmetic. "
     "check_sections.py fails a report that names no descriptor at all."],
    ["Default recognition", "One day, one rupee on rated instruments.",
     "One day, one rupee on rated instruments.",
     "One day, one rupee on listed debt and on any facility with a pre-defined repayment "
     "schedule. More than 30 days continuously overdrawn for cash credit and overdraft, packing "
     "credit, bill discounting and buyer's credit. More than 30 days from LC devolvement or BG "
     "invocation. Curing: generally 90 days to move out of D into speculative grade, and "
     "generally 365 days to reach investment grade.",
     "A delay IS a default. There is no grace concept to apply, and non-servicing in "
     "anticipation of a restructuring approval is still a default."],
    ["What a prior report may supply",
     "NOTHING. It teaches craft: sector narrative conventions, driver taxonomy, calibration, "
     "liquidity-argument style.", "The same.", "The same.",
     "A delivered rationale may share no run of twelve or more consecutive words with any agency "
     "publication for the same issuer, outside the mandated scaffolding. Enforced by a "
     "check_sections.py probe (failure mode 37). The compounding harm is that borrowing a "
     "framing means not doing the arithmetic - and a borrowed framing has been wrong on the "
     "issuer's own numbers."],
])
r = note(ws, r, "THIS SHEET IS THE REFERENCE, NOT THE DELIVERABLE. It shows three agencies side "
                "by side so the differences can be studied. A DELIVERED SCORECARD MUST NOT: it "
                "supports a rating by exactly one agency, and offering the reader three "
                "conventions lets them apply the wrong one to the numbers in front of them. "
                "Step 12c scopes the workbook down to the agency being rated before it ships.",
        color=NAVY)
r = note(ws, r, "THE GOVERNING RULE for every row above: if a definition will not reproduce the "
                "agency's own published figure for a year where one exists, THE DEFINITION IS "
                "WRONG - and the fix is the definition, never adjusting the inputs to force the "
                "tie. This is fully knowable without the agency's report, because the definitions "
                "reconcile exactly once they are applied correctly.")

# ======================================================================= 05 WEIGHTS - BLOCKS
ws, r = sheet(wb, "05_Weights_Blocks", "Weightings, level 1: the four risk blocks by sector",
              "READ LIVE from Rating_Scorecard.xlsx Ref_Weights. THIS IS THIS PROJECT'S "
              "CALIBRATION, NOT AGENCY-PUBLISHED WEIGHTS - none of the three agencies publishes "
              "numeric block weights for corporates. They describe the factors and let committee "
              "judgment combine them; these weights make that combination reproducible and "
              "testable.", [30, 15, 16, 16, 13, 16, 9, 13])
r = header(ws, r, ["Sector", "Industry base score" + NL + "(1 best, 6 worst)",
                   "w Industry /" + NL + "operating environment",
                   "w Business risk /" + NL + "market position", "w Financial" + NL + "risk",
                   "w Management &" + NL + "governance", "Sum", "Framework"])
r = rows(ws, r, [[rec[0], rec[1], rec[2], rec[3], rec[4], rec[5],
                  round(sum(x for x in rec[2:6] if isinstance(x, (int, float))), 2), rec[7]]
                 for rec in WEIGHTS])
r = note(ws, r, "How to read a row. For Real Estate / Construction the composite is 0.25 x "
                "industry + 0.20 x business + 0.40 x financial + 0.15 x management, and the "
                "industry score DEFAULTS to 4.5 unless the analyst overrides it with a written "
                "reason. Financial risk carries the largest single weight in every sector, "
                "between 0.40 and 0.45, because it is the block that is MEASURED rather than "
                "judged - but it is never a majority, because a rating that ignored industry and "
                "management would miss every governance failure and every structurally declining "
                "industry.")
r = note(ws, r, "The industry base score is the sector's own operating-environment risk before "
                "anything about the issuer is considered: 2.0 for FMCG, 4.5 for real estate and "
                "construction. It is what makes an identically-levered company rate differently "
                "in a stable industry and in a cyclical one.", color=NAVY)

# ======================================================================= 06 WEIGHTS - RATIOS
ws, r = sheet(wb, "06_Weights_Ratios",
              "Weightings, level 2: the six ratios inside the financial-risk block",
              "READ LIVE from Rating_Scorecard.xlsx Ref_Bands. The financial-risk score is the "
              "weighted average of these six 1-to-6 scores, and each is assessed on the AVERAGE "
              "OF THE LATEST ACTUAL YEAR AND THE FIRST PROJECTED YEAR - never on the latest year "
              "alone. That is what makes the anchor forward-looking rather than a snapshot of "
              "history.", [34, 12, 10, 15, 72])
r = header(ws, r, ["Ratio", "Direction", "Weight", "Share of the" + NL + "financial block",
                   "Why it carries this weight"])
WHY = {
    "Interest coverage (x)":
        "The heaviest single ratio, and deliberately so. It is the closest thing here to a "
        "direct read on default - below 1.0x the company cannot cover interest out of "
        "operations - and it responds to profitability AND leverage at the same time.",
    "Gearing - Total debt/TNW (x)":
        "The structural leverage measure: how much of the balance sheet is borrowed, and "
        "therefore how much room exists to raise fresh capital in a downturn.",
    "Total debt/EBITDA (x)":
        "Leverage expressed in years of profit rather than in proportion, so it travels across "
        "balance sheets of very different sizes. Weighted equally with gearing because the two "
        "answer the same question from opposite sides.",
    "EBITDA margin (%)":
        "The buffer between revenue and the cost base. Weighted below the leverage pair because "
        "margin is strongly industry-specific - a 6% distribution margin and a 25% pharma margin "
        "are not comparable, and making that comparison is what the industry block exists for.",
    "Gross cash accruals/Total debt (x)":
        "The cash-repayment view: how many years of accrual the debt represents. It overlaps "
        "with debt-to-EBITDA, which is why it carries a lower weight than either leverage "
        "measure.",
    "Current ratio (x)":
        "The lightest weight, because it is the crudest measure here and treats slow inventory "
        "as though it were cash. Liquidity does its real work through a separate descriptor "
        "adjustment (sheet 08), not through this ratio.",
}
FIN_TOTAL = sum(float(b[7]) for b in BANDS)
r = rows(ws, r, [[b[0], b[1], float(b[7]), "%.0f%%" % (100 * float(b[7]) / FIN_TOTAL),
                  WHY.get(b[0], "")] for b in BANDS])
r = note(ws, r, "The six weights sum to %.2f. Note the deliberate asymmetry between the two kinds "
                "of score that feed the composite: these six are COMPUTED from audited figures "
                "and cannot be argued with, while the three qualitative scores (sheet 10) are "
                "JUDGMENTS, each of which must carry a one-line written justification in the "
                "methodology's own factor language. Both feed the same weighted average, and only "
                "one of them can be disputed." % FIN_TOTAL)

# ====================================================================== 07 THRESHOLD BANDS
ws, r = sheet(wb, "07_Threshold_Bands", "The bands that turn a ratio into a 1-to-6 score",
              "Five thresholds create six buckets. 'Direction = higher' means a higher value is "
              "better, and the score counts how many thresholds the value clears. THIS PROJECT'S "
              "CALIBRATION, built in the style of the three agencies' criteria - not published "
              "bands.", BAND_W)
r = header(ws, r, BAND_COLS)
r = rows(ws, r, [band_row(b) for b in BANDS])
r = note(ws, r, "Worked read, using the live case. Alembic's FY2026 interest coverage of 55.95x "
                "clears every threshold including 8.0x, so it scores 1. Its gearing of 0.01x is "
                "below 0.50x, so it scores 1. Its EBITDA margin of 37.81% is above 25%, so 1 "
                "again. The financial-risk block therefore lands near the top of the range - "
                "which is correct, and is exactly why that rating is held back by the OTHER three "
                "blocks rather than by this one.")
r = note(ws, r, "The bands are absolute, not sector-relative. Sector is handled separately, "
                "through the industry base score and the block weights on sheet 05 - so a "
                "cyclical business is not given easier leverage thresholds, it is given a worse "
                "industry score and a heavier industry weight.", color=NAVY)

# ======================================================================= 08 SCORE TO GRADE
ws, r = sheet(wb, "08_Score_to_Grade", "From six ratios to a letter grade - the full arithmetic",
              "Every step below is a live formula in Rating_Scorecard.xlsx, reproduced here "
              "exactly. Follow it top to bottom and the anchor is reproducible by hand.",
              [5, 26, 54, 74])
r = header(ws, r, ["#", "Step", "Formula, as it exists in the workbook",
                   "What it does, and why it is done this way"])
r = rows(ws, r, [
    ["1", "Financial-risk score",
     "SUM(score x weight) / SUM(weight), across the six ratios of sheet 06, each assessed on "
     "AVERAGE(latest actual year, first projected year)",
     "Turns six ratios into one number on the 1-to-6 scale. Using the average of actual and "
     "projected is what makes the anchor forward-looking: a company whose coverage is about to "
     "halve does not get to score on last year's figure."],
    ["2", "Composite score",
     "SUM(block score x sector weight) / SUM(sector weight), across the four blocks of sheet 05",
     "Combines the measured financial score with the three judged scores, at the sector's own "
     "weights. Still on the 1-to-6 scale."],
    ["3", "Liquidity adjustment",
     "Superior -0.25  |  Strong -0.10  |  Adequate 0.00  |  Stretched +0.75  |  Poor +1.50",
     "Liquidity enters as an ADJUSTMENT rather than as a weighted block, and the scale is "
     "deliberately asymmetric: strong liquidity helps a little, weak liquidity hurts a lot. That "
     "asymmetry is the entire point - companies default because they run out of cash, not "
     "because they had too much of it."],
    ["4", "Adjusted composite", "MIN(6, MAX(1, composite + liquidity adjustment))",
     "Clamped to the 1-to-6 scale, so an adjustment cannot push the score off the end of it."],
    ["5", "Map onto the 17-notch scale",
     "index = MIN(16, MAX(0, ROUND(16 x ((adjusted - 1) / 5) ^ 1.4, 0)))   where 0 = AAA and "
     "16 = C",
     "The power p = 1.4 is the calibration. The map was LINEAR until 18-Jul-2026; back-testing "
     "against 396 rated issuers plus two hard cases showed the linear map carried a 2.1-notch "
     "downward bias, so the curve was softened through the investment-grade zone with both "
     "endpoints preserved. Note what was NOT changed: the financial bands were tested and were "
     "not the constraint."],
    ["6", "Support notches", "index = MIN(16, MAX(0, index - support notches))",
     "Parent, group or government support, applied AFTER the standalone score, with positive "
     "notches improving the grade. Every notch must quote the support methodology's criterion "
     "VERBATIM and show which side of it the entity falls on."],
    ["7", "Hard caps",
     "CORPORATE: negative net worth caps at B- (index at least 15); interest coverage below 1.0x "
     "caps at B+ (index at least 13).   FINANCIAL SECTOR: CRAR below 9% caps at index 10.",
     "Conditions under which no amount of qualitative strength should be allowed to produce an "
     "investment-grade anchor. A weighted average can otherwise be dragged upward by good scores "
     "elsewhere while the company cannot cover its own interest."],
    ["8", "Long-term grade", "INDEX(scale, index + 1) - see sheet 09",
     "The 17-notch long-term scale, AAA down to C."],
    ["9", "Short-term grade",
     "The published long-term to short-term mapping, LIFTED ONE LEVEL in the overlap bands when "
     "liquidity is Superior or Strong - see sheet 09",
     "Short-term ratings are about the next twelve months, so liquidity legitimately moves them "
     "where it would not move the long-term grade. AAA down to AA- map to A1+ regardless."],
    ["10", "Format in house style",
     "ICRA: [ICRA]grade (outlook) / [ICRA]st     CRISIL: Crisil grade/outlook / Crisil st     "
     "CareEdge: CARE grade; outlook / CARE st",
     "Each agency's own punctuation. Getting it wrong marks the report as not that agency's."],
])
r = note(ws, r, "AND THEN THE ANCHOR IS NOT THE RATING. It is a screening cross-check with a "
                "plus-or-minus two notch band, reliable to about one notch only in the A+ to "
                "BBB- range. Where the analyst's judgment view diverges from it by more than two "
                "notches - or by any amount at AA+/AAA or at BB-and-below - the workpaper must "
                "say WHICH qualitative or support factor the scorecard cannot see. The rating "
                "committee resolves the divergence; it is never settled by averaging the two "
                "answers.")

# ======================================================================== 09 LT-ST MAPPING
ws, r = sheet(wb, "09_LT_ST_Mapping", "The 17-notch scale and the short-term mapping",
              "READ LIVE from Rating_Scorecard.xlsx Ref_Scales. The short-term mapping comes from "
              "empirical pairs observed across 655 ICRA reference rationales. It is a CONSISTENCY "
              "CHECK, not a suggestion: a long-term AA sitting beside a short-term A2 is "
              "internally contradictory, and is caught at Step 13.", [12, 20, 26, 32, 26])
r = header(ws, r, ["Scale" + NL + "index", "Long-term" + NL + "grade",
                   "Short-term" + NL + "(normal liquidity)",
                   "Short-term" + NL + "(Superior / Strong liquidity)", "Broad band"])


def grade_band(i):
    if i <= 3:
        return "Highest / high safety"
    if i <= 6:
        return "Adequate safety"
    if i <= 9:
        return "Moderate safety"
    if i <= 12:
        return "Speculative"
    return "High risk / default-prone"


r = rows(ws, r, [[i, s[0], s[1], s[2], grade_band(i)] for i, s in enumerate(SCALE)])
r = note(ws, r, "The liquidity lift applies only in the OVERLAP bands. AAA, AA+, AA and AA- map "
                "to A1+ whatever the liquidity, because at those long-term levels the short-term "
                "answer is not in doubt. The lift bites from A+ downward, where a company's "
                "twelve-month position genuinely can differ from its long-run one - and that is "
                "the whole reason short-term ratings exist as a separate scale.")
r = note(ws, r, "Outlook is separate from all of this and follows the outlook policy: Stable, "
                "Positive, Negative, or Not applicable. A Rating Watch replaces the outlook "
                "entirely and carries an '&' suffix, with Positive, Negative or Developing "
                "Implications - because a watch says the direction is about to be resolved by a "
                "specific identified event, not that it is drifting.", color=NAVY)

# ==================================================================== 10 QUALITATIVE RUBRIC
ws, r = sheet(wb, "10_Qualitative_Rubric", "The three judgment scores, anchored",
              "READ LIVE from Rating_Scorecard.xlsx Ref_Qualitative. The financial score is "
              "computed and cannot be argued with. These three are judgments - so they are "
              "anchored to written descriptions, and each score used in a case must carry a "
              "one-line justification in the methodology's own factor language.",
              [8, 48, 48, 48])
r = header(ws, r, ["Score", "Industry / operating-environment risk",
                   "Business risk / market position", "Management & governance"])
r = rows(ws, r, [[q[0], q[1], q[2], q[3]] for q in QUAL])
r = note(ws, r, "The industry score may be left blank in a case, in which case the sector base "
                "score from sheet 05 applies. It is overridden only when the entity's specific "
                "operating environment genuinely differs from its sector's - and the override "
                "must say why.")
r = note(ws, r, "WHAT A GOOD JUSTIFICATION LOOKS LIKE, from the live case, management score 3: "
                "'FY2026 audit opinion unmodified on both bases, with an Emphasis of Matter on "
                "the electricity-duty litigation. Not a 2, for two documented reasons: FY2023 "
                "drew a QUALIFIED opinion on a Rs 10.61 crore transfer from General Reserve to "
                "the P&L, and related-party dealing is dense - Rs 38.67 crore of rent income from "
                "the wholly-owned subsidiary and Rs 38.86 crore of dividend to the 63.06% holding "
                "company.' Note the shape: the score, the evidence, and specifically why NOT the "
                "adjacent score. A justification that does not rule out the neighbouring score "
                "has not done its job.", color=NAVY)

# ===================================================================== 11 FINANCIAL SECTOR
ws, r = sheet(wb, "11_Financial_Sector", "Lenders and brokers - a different metric set entirely",
              "A financial-sector entity is not a corporate with different numbers; it is a "
              "different analysis. Using the corporate set on a lender - or one lender type's set "
              "on another - is failure mode 28, and it marks the report as written by someone "
              "outside the sector.", [18, 60, 64])
r = header(ws, r, ["Entity type", "The required metric set", "What does NOT belong, and why"])
r = rows(ws, r, [
    "THE METRIC SETS",
    ["Bank / SFB",
     "NIM; GNPA and NNPA; provision coverage ratio; CRAR and CET-1, measured against the "
     "ENTITY-SPECIFIC minima including the capital conservation buffer and any D-SIB buffer; "
     "CASA; cost-to-income; RoA; RoE; LCR and NSFR; slippage. Also NNPA over CET-1 as a solvency "
     "read.",
     "Gearing, TOL/TNW, interest coverage and working-capital days are corporate metrics that "
     "mean nothing on a deposit-taking balance sheet. 'Stage III' is also wrong here - that is "
     "Ind AS and NBFC vocabulary, not bank vocabulary."],
    ["NBFC / HFC",
     "AUM; AUM over TNW; opex as a percentage of AVERAGE TOTAL ASSETS; credit cost percentage; "
     "GS3 and NS3; CRAR and Tier I; gearing on TANGIBLE net worth; return on total assets; "
     "return on net worth.",
     "GNPA is BANK vocabulary. An Ind AS lender reports Stage 3 and Stage III in its ECL movement "
     "tables, so searching only for 'GNPA' returns nothing and produces a FALSE ABSENCE CLAIM "
     "(failure mode 25) - which has happened here, with 28 hits for 'Stage 3' sitting in the very "
     "document that was declared not to contain the data. Cost-to-income is a bank metric in this "
     "context; opex over average total assets is the right one."],
    ["Broking / securities",
     "Cost-to-income; return on net worth on AVERAGE tangible net worth; gearing INCLUDING "
     "non-fund-based limits utilised; the margin trading facility book; average daily turnover; "
     "active clients.",
     "Note the reversal against the row above: cost-to-income IS a standard reported metric for "
     "broking, even though it is the wrong metric for an NBFC. This is exactly why a metric may "
     "be excluded only after checking a published report of THAT agency in THAT sector, with the "
     "exclusion note citing the report checked - never a rule generalised from a different sector "
     "(failure mode 33)."],
    ["Corporate (for contrast)",
     "OPBDITA margin; gearing; TOL/TNW; interest coverage; NCATD; RoCE; current ratio; "
     "working-capital days.", "NIM, GNPA, CRAR and AUM."],
    None,
    "TWO TRAPS THAT ARE SPECIFIC TO LENDERS AND BROKERS",
    ["Cash is not liquidity",
     "For a broker, the line 'bank balance other than cash and cash equivalents' is "
     "overwhelmingly CLIENT FUNDS and exchange margin - it is not the company's money. Taking it "
     "at face value once produced a claimed liquid-asset figure of Rs 9,622.71 crore against an "
     "actual unencumbered Rs 422 crore: an 18-fold overstatement (failure mode 34).",
     "The rule that follows: before a figure becomes the numerator or denominator of a published "
     "ratio, state what it MEASURES and WHO IT BELONGS TO."],
    ["A denominator has to mean something",
     "Average daily turnover for a broker very likely includes derivative NOTIONAL turnover, "
     "against which revenue is not a meaningful denominator. A 'yield on turnover' built on it "
     "collapses mechanically whenever derivative mix rises.",
     "That describes a change in product mix as though it were a change in pricing - and it was "
     "published here as 'the defining operating fact of the year' before the denominator was "
     "questioned."],
])

# ====================================================================== 12 FINANCIAL BANDS
ws, r = sheet(wb, "12_Financial_Bands", "Scoring bands for banks, NBFCs and HFCs",
              "READ LIVE from Rating_Scorecard.xlsx Ref_Bands_Fin. These six replace the "
              "corporate six of sheet 07 whenever the sector type is Bank, NBFC or HFC. THIS "
              "PROJECT'S CALIBRATION, reflecting the agencies' bank and NBFC frameworks and RBI "
              "norms - not published bands.", BAND_W)
r = header(ws, r, BAND_COLS)
r = rows(ws, r, [band_row(b) for b in BANDS_FIN])
r = note(ws, r, "For NBFCs and HFCs, CRAR is what captures leverage - a higher CRAR means lower "
                "gearing - which is why it carries the heaviest weight in this set. NIM for an "
                "NBFC is the net interest spread. The hard cap for the financial sector is CRAR "
                "below 9%, reflecting the regulatory minimum: below it, no combination of other "
                "scores should be allowed to produce an investment-grade anchor.")

# ========================================================================== 13 VERIFICATION
ws, r = sheet(wb, "13_Verification", "How every number is proved before it reaches a report",
              "A rating is only as good as the extraction underneath it. Every material error "
              "this project has made was an EXTRACTION error, not a judgment error - so this is "
              "where the effort goes.", [22, 58, 32, 60])
r = header(ws, r, ["Layer / measure", "What it does, or what it reported", "How it runs",
                   "What it catches, or what it means"])
r = rows(ws, r, [
    "THE FOUR LAYERS",
    ["Tie-outs", "Each check is a five-tuple: description, computed value, disclosed value, "
     "tolerance, source. Four kinds. PRINTED - the figure against the document's own printed row. "
     "EXACT - an identity that must hold to the paisa, such as equity plus liabilities equals "
     "total assets. INTERNAL - a containment or plausibility check. CORROBORATED - does this "
     "exact figure appear anywhere in the source documents at all.",
     "python compute_ratios.py in the case folder. rate_engine.py aborts with exit 1 if any check "
     "fails, and produces no rating by either route.",
     "A dropped digit, a misplaced decimal, a value copied into the wrong year's slot, a subtotal "
     "that does not equal its components. Note what CORROBORATED does NOT catch: a figure can be "
     "present in the documents and still belong to another year, entity or basis - which is why "
     "the two labels are kept distinct rather than merged."],
    ["Mutation coverage", "Perturbs EVERY numeric input in turn, re-runs the tie-outs, and "
     "reports which inputs no check is sensitive to. This answers the real question - not 'how "
     "many checks passed' but 'which inputs would any check notice if they were wrong'.",
     "python tieout_mutation.py <case-slug>",
     "TWO things a green suite hides: a CIRCULAR check that compares a value to itself and can "
     "never fail, and an input that no check is downstream of. A suite here once reported 22 of "
     "22 passing while four of those checks were circular AND a figure that was wrong in both "
     "magnitude and sign was covered by nothing at all (failure mode 39)."],
    ["Pre-flight (entry gate)", "Searches the reference library and every uploaded document "
     "BEFORE reading begins, and prints what EXISTS. Includes probes for operating metrics across "
     "documents, aggregate-note contaminants, and any item appearing in two statements with "
     "values that do not intersect.", "python preflight.py <case-slug>, at Step 1a",
     "The most damaging error class: claiming data is unavailable without having looked. It once "
     "produced a rating a full notch wrong while the correct answer sat in four separate places "
     "in the issuer's own annual report."],
    ["Section audit (delivery gate)", "Agency-aware section-completeness check plus quality "
     "probes, matching section HEADERS only - matching body text produced a false pass in an "
     "early version of the checker.", "python check_sections.py \"<report>.md\", at Step 17a",
     "A mandatory section silently dropped; an unevidenced absence claim; an undated "
     "CRA-attributed amount; Annexure lines that do not sum to their stated total; an "
     "operating-profit figure with no normalisation stated; verbatim reuse of an agency "
     "publication."],
    None,
    "THE TWO RULES THAT PRODUCED THIS LAYER",
    ["Decomposition is not verification", "An aggregate note must be decomposed to its line items "
     "before any of it feeds an operating-profit measure - but decomposing alone proves nothing. "
     "The decomposition must be TIED BACK to the note's own printed total.", "",
     "That tie-back is what converts every line inside the note - forex, bad debts, CSR - from a "
     "typed number into a checked one."],
    ["A check that cannot fail its control is not a check", "Every probe is exercised against a "
     "KNOWN BREAK before it is trusted.", "",
     "One gate written here passed its own positive control, because it searched the whole "
     "document for the substrings '1.8' and '7.3' - which occur inside 11.87 and 7,460.33. It "
     "proved nothing, and would have reported success forever."],
    None,
    "WHAT THE LAYERS ACTUALLY REPORTED ON THE LIVE CASE (Alembic Limited, 31-Aug-2026)",
    ["Tie-outs", "204 of 205 reconcile, 1 acknowledged", "",
     "The one non-reconciling check is a 6.6% implied tax rate, below the 8-45% plausibility band. "
     "It is DECLARED, not suppressed: the engine states the reason - a Section 80M inter-corporate "
     "dividend deduction - and the mechanism accepts the declaration ONLY because that same reason "
     "also appears in the case's disclosed differences, so it reaches the committee and the "
     "report rather than just the checker."],
    ["Mutation coverage", "100.0% - 151 inputs perturbed, 151 register on a check", "",
     "No input in the engine is invisible to every check."],
    ["Section audit", "PASS - all mandatory sections present, all quality probes clean", "", ""],
    ["Computed drift-check", "53 of 53 figures in the draft match the engine verbatim", "",
     "Numbers drift while writing; this is the re-run that catches it."],
    ["Non-computed drift-check", "All corroborated against source except two, which were REMOVED",
     "", "A 2004 notice date and a High Court ruling appeared only in the prior agency "
     "publication, not in the annual reports. Anchor-inherited facts (failure mode 1) - deleted, "
     "and the litigation paragraph rewritten from the annual report alone."],
])

# ======================================================================= 14 WORKED - RATIOS
ws, r = sheet(wb, "14_Worked_Ratios", "Alembic Limited - every ratio with a real number",
              "Standalone, Rs crore, audited, as on 31-Mar-2026. Source: "
              "Companies/alembic-limited/compute_ratios.py. Nothing below is typed by hand: each "
              "figure passed the tie-out and mutation layers of sheet 13.",
              [26, 46, 12, 12, 12, 58])
r = header(ws, r, ["Line", "Formula, with the actual numbers substituted", "FY2024", "FY2025",
                   "FY2026", "Reading"])
r = rows(ws, r, [
    "INPUTS - from the audited standalone statements",
    ["Operating income", "Revenue from operations", "152.25", "214.36", "231.93",
     "Up 52% over two years."],
    ["Other income (note 28)", "The note's own printed total", "54.62", "74.51", "72.77",
     "Decomposed to line items before any use - see the note below this table."],
    ["Finance cost (note 33)", "As printed", "0.69", "1.83", "1.57", ""],
    ["Depreciation (notes 4, 5)", "As printed", "7.46", "10.24", "12.01", ""],
    ["Profit before tax", "As printed", "102.72", "151.99", "146.89", ""],
    ["Profit after tax", "As printed", "92.89", "141.95", "124.54",
     "The FY2026 fall is a tax-line effect, not an operating one."],
    ["Total debt", "Non-current borrowings + current borrowings", "9.15", "14.45", "10.64",
     "No lease liability disclosed in any year - a DECLARED nil, not an assumed one."],
    ["Tangible net worth", "Equity share capital + other equity", "808.76", "853.19", "821.46",
     "Fell in FY2026 despite Rs 124.54 crore of profit, because of a Rs 102.98 crore OCI markdown "
     "on a listed holding."],
    ["Total assets", "As printed", "945.87", "1,009.83", "957.70", ""],
    None,
    "COMPUTED RATIOS - the formulas of sheet 03, instantiated",
    ["OPBDIT (ICRA convention)",
     "PBT + finance cost + depreciation - other income" + NL + "= 146.89 + 1.57 + 12.01 - 72.77",
     "56.25", "89.55", "87.69",
     "Other income stripped UNCONDITIONALLY - ICRA's convention, and the opposite of CRISIL's."],
    ["OPBDIT / OI", "87.69 / 231.93", "36.95%", "41.78%", "37.81%",
     "Peaked in FY2025. The easing is real-estate project mix, not demand."],
    ["PAT / OI", "124.54 / 231.93", "61.01%", "66.22%", "53.70%", ""],
    ["Gearing", "Total debt / TNW = 10.64 / 821.46", "0.01", "0.02", "0.01",
     "Scores 1 - the strongest band starts at 0.50x."],
    ["TOL / TNW", "(Total assets - TNW) / TNW = (957.70 - 821.46) / 821.46", "0.17", "0.18",
     "0.17", ""],
    ["Total debt / OPBDIT", "10.64 / 87.69", "0.16", "0.16", "0.12",
     "Roughly six weeks of operating profit."],
    ["Interest coverage", "OPBDIT / finance cost = 87.69 / 1.57", "81.85", "48.94", "55.95",
     "Scores 1 - the strongest band starts at 8.0x."],
    ["Net debt", "Total debt - (cash + bank + current investments) = 10.64 - 92.02", "(3.90)",
     "(39.30)", "(81.38)", "A net CASH position, deepening every year."],
    ["Current ratio", "Current assets / current liabilities = 186.85 / 96.31", "1.50", "1.81",
     "1.94", "Tied to the annual report's OWN printed current-ratio disclosure - which is what "
     "verifies all eleven working-capital components at once, rather than one at a time."],
    None,
    "THE FIGURE THAT ACTUALLY DRIVES THIS RATING",
    ["Market value of quoted investments", "The company's own note 6 disclosure", "5,823.75",
     "5,490.20", "3,885.89",
     "DOWN 33% FROM THE FY2024 PEAK. The direction is as much the finding as the level, and it is "
     "why a four-year series was extracted rather than a closing figure (failure mode 16)."],
    ["Market value / total debt", "3,885.89 / 10.64", "636.5", "380.0", "365.3",
     "Financial flexibility of a completely different order from the balance sheet it sits on."],
    ["Dividend income", "Note 28 component for FY2025-26; FY2024 from the standalone cash-flow "
     "statement's 'Dividend received' line", "45.91", "62.95", "62.95",
     "Recurring cash. It covers total debt 5.9 times and finance cost 40 times on its own - and "
     "it did NOT fall while the portfolio's market value fell 29%."],
])
r = note(ws, r, "WHY THE OTHER-INCOME NOTE IS DECOMPOSED BEFORE USE (failure mode 36). A caption "
                "like 'Other Income' is a COMPOSITE, and a composite is not a ratio input until "
                "its components have been read. The structural trap is that the same economic "
                "item migrates between the two notes WITH ITS SIGN: a foreign-exchange gain sits "
                "in Other Income, a foreign-exchange loss sits in Other Expenses. The convention "
                "'minus other income' therefore strips the gain automatically and RETAINS THE "
                "LOSS - manufacturing a margin decline out of an item that is not operating in "
                "either direction. On this case forex was checked and is a gain in every year, "
                "with no loss anywhere in other expenses, so the asymmetry does not arise - but "
                "it was CHECKED rather than assumed. Getting it wrong on another case in this "
                "project produced a rating one notch low, and a rationale built on a margin "
                "compression that had not happened.")
r = note(ws, r, "AND WHY THESE RATIOS STILL DIFFER FROM THE PRIOR PUBLISHED ACTION. That action "
                "reported FY2025 operating income of Rs 280.6 crore against Rs 214.36 crore here, "
                "because it treated the issuer as an investment company and counted dividend "
                "income as operating revenue. PAT reconciles to the rupee, which localises the "
                "whole difference to above the PAT line - and solving for the implied add-back "
                "three independent ways (from the published margin, from the published interest "
                "cover, from the published operating income) gives 66.11, 66.17 and 66.24, "
                "agreeing to within Rs 0.15 crore. One classification choice, fully explained, "
                "and disclosed in the rationale rather than buried in a workpaper.", color=NAVY)

# ======================================================================= 15 WORKED - ANCHOR
ws, r = sheet(wb, "15_Worked_Anchor", "Alembic Limited through the scoring chain, end to end",
              "The same case walked through sheets 05 to 09, from sector selection to a letter "
              "grade. Read back through the workbook's own formula chain with: python "
              "rate_engine.py alembic-limited --engine local", [24, 40, 30, 62])
r = header(ws, r, ["Step", "Input", "Result", "Why"])
r = rows(ws, r, [
    ["Sector (sheet 05)", "Real Estate / Construction",
     "Industry base 4.5; weights 0.25 / 0.20 / 0.40 / 0.15",
     "The nearest of the 22 sectors: real estate is 80% of revenue and 93% of segment profit."],
    ["Financial-risk block" + NL + "(sheets 06, 07)",
     "Interest coverage 55.95x; gearing 0.01x; total debt/EBITDA 0.12x; EBITDA margin 37.81%; "
     "GCA over total debt; current ratio 1.94x", "Near the top of the 1-to-6 range",
     "Effectively unlevered - every leverage and coverage ratio clears the strongest band."],
    ["Business risk (sheet 10)", "Score 4", "Judged",
     "Modest, single-city operating scale: Rs 231.93 crore of revenue, 80% of it from one city's "
     "real estate. Not a 3, because the concentration is geographic as well as segmental."],
    ["Management & governance" + NL + "(sheet 10)", "Score 3", "Judged",
     "Unmodified FY2026 opinion, held off a 2 by the FY2023 qualified opinion and by dense "
     "related-party dealing."],
    ["Industry risk (sheet 05)", "Not overridden", "Sector base 4.5 applies",
     "The issuer's operating environment does not differ materially from its sector's."],
    ["Liquidity (sheet 08, step 3)", "Superior", "Adjustment -0.25",
     "Rs 92.02 crore of unencumbered liquidity against Rs 10.64 crore of debt; dividend income "
     "alone covers total debt 5.9 times. The descriptor is the conclusion of that arithmetic, not "
     "an adjective."],
    ["Support notches (step 6)", "0", "No change",
     "The 63.06% holding company cannot be assessed - no financials for it exist in the document "
     "set, searched - so NO UPLIFT is taken. But no cap either: the issuer needs no support in "
     "any evidenced scenario, and capping a self-sufficient subsidiary on an unassessable parent "
     "would be a conclusion the evidence does not support."],
    ["Hard caps (step 7)", "Net worth positive; interest coverage 55.95x", "None applied", ""],
    None,
    "THE THREE ANSWERS, AND WHETHER THEY AGREE",
    ["ANCHOR GRADE", "The scorecard's own formula chain, evaluated offline", "AA-",
     "Deterministic and byte-identical on every run."],
    ["Independent judgment view", "Formed at Step 13, BEFORE the prior report was opened",
     "[ICRA]AA- (Stable) / [ICRA]A1+",
     "Exceptional financial flexibility and effectively nil leverage, held back by modest "
     "operating scale and by a portfolio whose value has fallen a third in two years."],
    ["Prior published action", "Opened only at Step 14", "[ICRA]AA- (Stable) / [ICRA]A1+",
     "Dated 30-May-2025, on Rs 56.4 crore of rated limits."],
    ["DIVERGENCE", "", "NONE - all three coincide",
     "The first case in this project where anchor, judgment view and prior action agree with "
     "nothing to resolve. Worth noting WHY: AA- sits inside the A+ to BBB- range where the "
     "back-test says the anchor is reliable to about one notch. The two preceding cases both read "
     "one notch low at the AA+/AAA boundary - which is the documented calibration limit, not a "
     "surprise."],
])
r = note(ws, r, "What this walk-through is NOT. It is not the rating. Steps 17b and 17c still have "
                "to happen: an independent reviewer re-ties the numbers and checks methodology "
                "fit, and a rating committee separate from the analyst decides the grade and "
                "outlook on the complete package, with minutes recording the vote, any dissent, "
                "and the express resolution of any anchor divergence. Everything on sheets 05 to "
                "09 produces a PROPOSAL.")

wb.save(OUT)
print("wrote", OUT)
print("%d sheets: %s" % (len(wb.sheetnames), ", ".join(wb.sheetnames)))
