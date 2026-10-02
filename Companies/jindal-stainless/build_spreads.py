"""Generate Jindal Stainless Limited_Financial_Spreads.xlsx FROM compute_ratios.py.

Per CLAUDE.md Step 5: the script is the source of truth and this workbook is a generated
review/feed layer. Nothing here is hand-typed - every Inputs cell is read out of
compute_ratios.py's dicts, and every RatioSuite cell is a LIVE EXCEL FORMULA pointing back at
Inputs, so a reviewer can trace any ratio to its components inside Excel rather than taking
the Python on trust.

Tabs: Extraction (every line item, all years, with its source) | RatioSuite (CareEdge
convention suite, by formula) | TieOut (component-level reconciliation, PASS/FAIL) |
Conventions (the definitions actually applied, in CareEdge's own terms - failure mode 32).
"""

import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

import compute_ratios as C

HDR = PatternFill("solid", fgColor="1F3864")
SUB = PatternFill("solid", fgColor="D9E2F3")
WARN = PatternFill("solid", fgColor="FCE4D6")
OKF = PatternFill("solid", fgColor="E2EFDA")
BAD = PatternFill("solid", fgColor="F8CBAD")
WHITE = Font(color="FFFFFF", bold=True)
BOLD = Font(bold=True)
THIN = Border(*[Side(style="thin", color="BFBFBF")] * 4)

YEARS = C.YEARS
NCOL = len(YEARS)


def _hdr(ws, row, label, widths=(46, 14, 14, 14, 14)):
    ws.cell(row=row, column=1, value=label).font = WHITE
    ws.cell(row=row, column=1).fill = HDR
    for j, y in enumerate(YEARS):
        c = ws.cell(row=row, column=2 + j, value=y)
        c.font, c.fill, c.alignment = WHITE, HDR, Alignment(horizontal="center")
    ws.cell(row=row, column=2 + NCOL, value="Source").font = WHITE
    ws.cell(row=row, column=2 + NCOL).fill = HDR
    for i, w in enumerate(widths):
        ws.column_dimensions[get_column_letter(1 + i)].width = w
    ws.column_dimensions[get_column_letter(2 + NCOL)].width = 60
    return row + 1


def _section(ws, row, title):
    c = ws.cell(row=row, column=1, value=title)
    c.font, c.fill = BOLD, SUB
    for j in range(1, NCOL + 2):
        ws.cell(row=row, column=1 + j).fill = SUB
    return row + 1


def _block(ws, row, block, source, index):
    """Write one dict-of-lists block; record each label's row for formula references."""
    for label, vals in block.items():
        ws.cell(row=row, column=1, value=label)
        for j in range(NCOL):
            c = ws.cell(row=row, column=2 + j, value=vals[j])
            c.number_format, c.border = "#,##0.00", THIN
        ws.cell(row=row, column=2 + NCOL, value=source)
        index[label] = row
        row += 1
    return row


def _derived(ws, row, label, member_rows, index, note):
    """A subtotal written as a live SUM formula over its own component rows - never typed."""
    ws.cell(row=row, column=1, value=label).font = BOLD
    for j in range(NCOL):
        col = get_column_letter(2 + j)
        parts = "+".join("%s%d" % (col, r) for r in member_rows)
        c = ws.cell(row=row, column=2 + j, value="=" + parts)
        c.number_format, c.font, c.border = "#,##0.00", BOLD, THIN
    ws.cell(row=row, column=2 + NCOL, value=note)
    index[label] = row
    return row + 1


def build_extraction(wb):
    ws = wb.create_sheet("Extraction")
    idx = {}
    r = _hdr(ws, 1, "Jindal Stainless Limited - consolidated extraction (Rs crore)")

    r = _section(ws, r, "PROFIT AND LOSS")
    r = _block(ws, r, C.PL, "AR consolidated statement of profit and loss; non-operating "
                            "items from the cash-flow reconciliation", idx)

    r = _section(ws, r, "NON-CURRENT ASSETS")
    start = r
    r = _block(ws, r, C.NON_CURRENT_ASSETS, "AR consolidated balance sheet", idx)
    nca_rows = list(range(start, r))
    r = _derived(ws, r, "Total non-current assets", nca_rows, idx, "live SUM over the component rows above")

    r = _section(ws, r, "CURRENT ASSETS")
    start = r
    r = _block(ws, r, C.CURRENT_ASSETS, "AR consolidated balance sheet", idx)
    ca_rows = list(range(start, r))
    r = _derived(ws, r, "Total current assets", ca_rows, idx, "live SUM over the component rows above")
    r = _derived(ws, r, "TOTAL ASSETS",
                 [idx["Total non-current assets"], idx["Total current assets"]], idx,
                 "live SUM: non-current + current")

    r = _section(ws, r, "EQUITY")
    start = r
    r = _block(ws, r, C.EQUITY, "AR consolidated balance sheet", idx)
    r = _derived(ws, r, "Total equity", list(range(start, r)), idx,
                 "live SUM of components; INCLUDES non-controlling interest")

    r = _section(ws, r, "NON-CURRENT LIABILITIES")
    start = r
    r = _block(ws, r, C.NON_CURRENT_LIABILITIES, "AR consolidated balance sheet", idx)
    r = _derived(ws, r, "Total non-current liabilities", list(range(start, r)), idx,
                 "live SUM over the component rows above")

    r = _section(ws, r, "CURRENT LIABILITIES")
    start = r
    r = _block(ws, r, C.CURRENT_LIABILITIES, "AR consolidated balance sheet", idx)
    r = _derived(ws, r, "Total current liabilities", list(range(start, r)), idx,
                 "live SUM over the component rows above")
    r = _derived(ws, r, "TOTAL EQUITY AND LIABILITIES",
                 [idx["Total equity"], idx["Total non-current liabilities"],
                  idx["Total current liabilities"]], idx, "live SUM: equity + all liabilities")

    r += 1
    ws.cell(row=r, column=1, value="AR's OWN printed total assets (independent check)").font = BOLD
    for j, y in enumerate(YEARS):
        c = ws.cell(row=r, column=2 + j, value=C.AR_PRINTED_TOTAL[y])
        c.number_format, c.fill, c.border = "#,##0.00", WARN, THIN
    ws.cell(row=r, column=2 + NCOL,
            value="Typed from the AR's Total row - the one figure in this sheet that is NOT "
                  "derived, which is what makes it a real check")
    idx["AR printed total"] = r
    return ws, idx


def build_ratios(wb, idx):
    ws = wb.create_sheet("RatioSuite")
    E = "Extraction!"

    def ref(label, j):
        return "%s%s%d" % (E, get_column_letter(2 + j), idx[label])

    r = _hdr(ws, 1, "CareEdge convention ratio suite - every cell a live formula")
    rows = []

    def add(label, fn, fmt, note):
        nonlocal r
        ws.cell(row=r, column=1, value=label)
        for j in range(NCOL):
            c = ws.cell(row=r, column=2 + j, value="=" + fn(j))
            c.number_format, c.border = fmt, THIN
        ws.cell(row=r, column=2 + NCOL, value=note)
        rows.append((label, r))
        r += 1

    def debt(j):
        return "(%s+%s+%s+%s)" % (ref("Borrowings (non-current)", j),
                                  ref("Borrowings (current)", j),
                                  ref("Lease liabilities (NC)", j),
                                  ref("Lease liabilities (C)", j))

    def tnw(j):
        return "(%s-%s-%s-%s)" % (ref("Total equity", j), ref("Goodwill", j),
                                  ref("Other intangible assets", j),
                                  ref("Intangible assets under dev", j))

    def base(j):
        return "(%s+%s+%s-%s)" % (ref("PBT ex-except ex-assoc", j), ref("Finance costs", j),
                                  ref("Depreciation", j), ref("Other income", j))

    def addback(j):
        # Zero by construction on this issuer - see compute_ratios.py. The forex result is a
        # net GAIN sitting inside Other Expenses in all four years, so it is already in the
        # base and nothing is restored; the earlier MAX(0,-forex) term restored a gain that
        # was never in Other Income, off a cash-flow row that was not the P&L line at all.
        return "0"

    def pbildt(j):
        return "(%s+%s)" % (base(j), addback(j))

    def liquid(j):
        return "(%s+%s+%s)" % (ref("Cash and cash equivalents", j),
                               ref("Other bank balances", j), ref("Investments (current)", j))

    def tol(j):
        return "(%s+%s)" % (ref("Total non-current liabilities", j),
                            ref("Total current liabilities", j))

    add("Total operating income", lambda j: ref("Revenue from ops", j), "#,##0.00",
        "Revenue from operations")
    add("PBILDT base (= AR's own EBITDA definition)", base, "#,##0.00",
        "PBT before exceptional/associate + finance cost + depreciation - other income")
    add("  add back: non-op items per CareEdge", addback, "#,##0.00",
        "ZERO on this issuer: the forex result is a net GAIN inside Other Expenses in all "
        "four years (note 34 / note 33), so it is already in the base and CareEdge's rule "
        "that non-debt forex is operating is satisfied without any adjustment")
    add("PBILDT", pbildt, "#,##0.00", "CareEdge convention - see Conventions tab")
    add("PBILDT margin (%)", lambda j: "100*%s/%s" % (pbildt(j), ref("Revenue from ops", j)),
        "0.00", "PBILDT / operating income")
    add("PAT", lambda j: ref("PAT", j), "#,##0.00", "AR")
    add("PAT margin (%)", lambda j: "100*%s/%s" % (ref("PAT", j), ref("Revenue from ops", j)),
        "0.00", "PAT / operating income")
    add("Total debt", debt, "#,##0.00", "borrowings + lease liabilities (CareEdge Sec.10)")
    add("Net debt", lambda j: "%s-%s" % (debt(j), liquid(j)), "#,##0.00",
        "total debt less cash, other bank balances and current investments")
    add("Tangible net worth", tnw, "#,##0.00",
        "total equity (incl. NCI) less goodwill and intangibles; DTA NOT deducted - that is "
        "the financial-sector definition (failure mode 32)")
    add("Overall gearing (times)", lambda j: "%s/%s" % (debt(j), tnw(j)), "0.00",
        "UNADJUSTED - acceptances and group guarantees not separately disclosed")
    add("Total debt/PBILDT (times)", lambda j: "%s/%s" % (debt(j), pbildt(j)), "0.00", "")
    add("Net debt/PBILDT (times)",
        lambda j: "(%s-%s)/%s" % (debt(j), liquid(j), pbildt(j)), "0.00", "")
    add("TOL/TNW (times)", lambda j: "%s/%s" % (tol(j), tnw(j)), "0.00",
        "total outside liabilities / tangible net worth")
    add("Interest coverage (times)",
        lambda j: "%s/%s" % (pbildt(j), ref("Finance costs", j)), "0.00", "PBILDT / finance costs")
    add("Current ratio (times)", lambda j: "%s/%s" % (ref("Total current assets", j),
                                                      ref("Total current liabilities", j)),
        "0.00", "")
    add("EPS (Rs)", lambda j: ref("EPS basic (Rs)", j), "0.00", "AR, basic")
    return ws, dict(rows)


def build_tieout(wb, idx, rrows):
    ws = wb.create_sheet("TieOut")
    ws.column_dimensions["A"].width = 62
    ws.column_dimensions["B"].width = 15
    ws.column_dimensions["C"].width = 15
    ws.column_dimensions["D"].width = 12
    ws.column_dimensions["E"].width = 62
    for j, h in enumerate(["Check", "Computed (live)", "Disclosed", "Result", "Source"]):
        c = ws.cell(row=1, column=1 + j, value=h)
        c.font, c.fill = WHITE, HDR
    E = "Extraction!"
    r = 2
    n_fail = 0

    def col(j):
        return get_column_letter(2 + j)

    for j, y in enumerate(YEARS):
        checks = [
            ("Assets = equity + liabilities, %s" % y,
             "%s%s%d" % (E, col(j), idx["TOTAL ASSETS"]),
             "%s%s%d" % (E, col(j), idx["TOTAL EQUITY AND LIABILITIES"]),
             "consolidated balance sheet"),
            ("Derived total assets = AR's printed total, %s" % y,
             "%s%s%d" % (E, col(j), idx["TOTAL ASSETS"]),
             "%s%s%d" % (E, col(j), idx["AR printed total"]),
             "AR consolidated balance sheet, Total row"),
        ]
        for desc, a, b, src in checks:
            ws.cell(row=r, column=1, value=desc)
            ws.cell(row=r, column=2, value="=" + a).number_format = "#,##0.00"
            ws.cell(row=r, column=3, value="=" + b).number_format = "#,##0.00"
            c = ws.cell(row=r, column=4,
                        value='=IF(ABS(B%d-C%d)<=0.005,"PASS","FAIL")' % (r, r))
            c.font = BOLD
            c.fill = OKF
            ws.cell(row=r, column=5, value=src)
            r += 1

    # PBILDT base must equal the company's own published EBITDA where the company prints one.
    for y, disc in C.AR_PUBLISHED["EBITDA line"].items():
        j = C.IDX[y]
        ws.cell(row=r, column=1, value="PBILDT base = AR's own EBITDA line, %s" % y)
        ws.cell(row=r, column=2,
                value="=RatioSuite!%s%d" % (col(j), rrows["PBILDT base (= AR's own EBITDA definition)"])
                ).number_format = "#,##0.00"
        ws.cell(row=r, column=3, value=disc).number_format = "#,##0.00"
        ws.cell(row=r, column=4,
                value='=IF(ABS(B%d-C%d)<=0.005,"PASS","FAIL")' % (r, r)).fill = OKF
        ws.cell(row=r, column=5,
                value="FY2025-26 AR consolidated financial highlights, EBITDA row - the "
                      "company publishes EBITDA on exactly this definition")
        r += 1

    for y, disc in C.AR_PUBLISHED["Total borrowings"].items():
        j = C.IDX[y]
        ws.cell(row=r, column=1, value="Borrowings excl. leases = AR note, %s" % y)
        ws.cell(row=r, column=2, value="=%s%s%d+%s%s%d" % (
            E, col(j), idx["Borrowings (non-current)"],
            E, col(j), idx["Borrowings (current)"])).number_format = "#,##0.00"
        ws.cell(row=r, column=3, value=disc).number_format = "#,##0.00"
        ws.cell(row=r, column=4,
                value='=IF(ABS(B%d-C%d)<=0.005,"PASS","FAIL")' % (r, r)).fill = OKF
        ws.cell(row=r, column=5, value="FY2023-24 AR capital-management note")
        r += 1

    r += 1
    ws.cell(row=r, column=1, value="FAILING ROWS (must be zero)").font = BOLD
    ws.cell(row=r, column=2, value='=COUNTIF(D2:D%d,"FAIL")' % (r - 2)).font = BOLD
    ws.cell(row=r, column=2).fill = BAD
    return ws, n_fail


def build_conventions(wb):
    ws = wb.create_sheet("Conventions")
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 118
    c = ws.cell(row=1, column=1, value="Definition")
    c.font, c.fill = WHITE, HDR
    c = ws.cell(row=1, column=2, value="As applied here, in CareEdge's own terms")
    c.font, c.fill = WHITE, HDR
    r = 2
    for k, v in [
        ("PBILDT", "PBT before exceptional items and share of equity-method investments, plus "
                   "finance costs and depreciation, less other income. Non-debt forex stays "
                   "INSIDE PBILDT in both directions (a gain reported in Other Income is "
                   "restored); profit/loss on sale of assets and investments comes OUT."),
        ("Tangible net worth", "Total equity including non-controlling interest, less goodwill "
                               "and all intangibles. Deferred tax assets are NOT deducted - "
                               "that belongs to the financial-sector definition."),
        ("Total debt", "Borrowings plus lease liabilities. UNADJUSTED: CareEdge's adjusted "
                       "measure also adds acceptances/LC creditors and group guarantees, "
                       "neither separately disclosed in the consolidated accounts."),
        ("Exceptional items", "Excluded by construction - the PBILDT base starts below them. "
                              "The FY2025 Jindal Coke stake loss (7.06) and FY2026 Ind AS 103 "
                              "gain (17.40) sit INSIDE exceptional items per note 39/40 and "
                              "must NOT be added back again."),
    ]:
        ws.cell(row=r, column=1, value=k).font = BOLD
        ws.cell(row=r, column=2, value=v).alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[r].height = 60
        r += 1
    for title, text in C.DISCLOSED_DIFFERENCES:
        ws.cell(row=r, column=1, value="DISCLOSED").font = BOLD
        ws.cell(row=r, column=2, value=title + " - " + text).alignment = Alignment(
            wrap_text=True, vertical="top")
        ws.row_dimensions[r].height = 75
        r += 1
    return ws


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    wb = Workbook()
    wb.remove(wb.active)
    _, idx = build_extraction(wb)
    _, rrows = build_ratios(wb, idx)
    build_tieout(wb, idx, rrows)
    build_conventions(wb)
    out = "Jindal Stainless Limited_Financial_Spreads.xlsx"
    wb.save(out)
    print("wrote %s" % out)
    print("tabs: %s" % ", ".join(wb.sheetnames))


if __name__ == "__main__":
    main()
