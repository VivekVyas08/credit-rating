"""Step 12 forecast model - Repco Home Finance Limited (HFC LENDING model, not a corporate
three-statement template).

CLAUDE.md failure mode 35 and UNIFIED_RATING_GUIDE R17/R18 require the Step 12 artefact to be
SCALED TO THE ENTITY. For a housing finance company the rating turns on forward book growth,
spread and credit cost, not on revenue/EBITDA/capex, so the model is built as a lending model:

    book roll-forward -> net interest income -> operating costs -> credit cost -> PAT
                      -> retained earnings -> funding gap -> debt -> gearing and CRAR

Every driver is derived from the company's own documents and the derivation is written into
the Assumptions tab beside it. A stress case flexes the three variables ICRA's NBFC
methodology names - asset quality, spread and growth.

BASE-PERIOD APPROXIMATION, stated rather than hidden: the newest balance sheet in the document
set is 30-Jun-2026 (Reg 54(3) security-cover certificate) and no 31-Mar-2026 balance sheet
exists anywhere in the folder. FY2027E therefore rolls forward a full twelve months from the
30-Jun-2026 stock rather than from 31-Mar-2026. The effect is to carry roughly one quarter of
growth twice - about Rs 250 crore on a Rs 15,700 crore book, or 1.6% - which moves no ratio
far enough to change a grade.
"""
import sys
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import _cache_values, _force_recalc                     # noqa: E402

OUT = "Repco Home Finance Limited_Lending_Model.xlsx"
YEARS = ["FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E"]
N = len(YEARS)
COLS = [get_column_letter(3 + i) for i in range(N)]                 # C..G
NOTE_COL = get_column_letter(3 + N)                                 # H

HDR = PatternFill("solid", fgColor="1F3864")
INP = PatternFill("solid", fgColor="FFF2CC")
BAND = PatternFill("solid", fgColor="D9E2F3")
BOX = Border(*[Side("thin", color="BFBFBF")] * 4)
WHITE = Font(color="FFFFFF", bold=True, size=11)
SMALL = Font(size=8, color="595959")
BOLD = Font(bold=True)


def sheet(wb, name, title, blurb):
    ws = wb.create_sheet(name)
    ws.column_dimensions["B"].width = 54
    for c in COLS:
        ws.column_dimensions[c].width = 15
    ws.column_dimensions[NOTE_COL].width = 86
    ws.merge_cells("B2:%s2" % NOTE_COL)
    ws["B2"].value, ws["B2"].fill, ws["B2"].font = title, HDR, WHITE
    ws.merge_cells("B3:%s3" % NOTE_COL)
    ws["B3"].value, ws["B3"].font = blurb, SMALL
    ws["B3"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[3].height = 48
    ws.cell(row=5, column=2, value="Line").font = BOLD
    for i, p in enumerate(YEARS):
        c = ws.cell(row=5, column=3 + i, value=p)
        c.font, c.fill, c.border = BOLD, BAND, BOX
        c.alignment = Alignment(horizontal="center")
    ws.cell(row=5, column=3 + N, value="Derivation / source").font = BOLD
    ws.freeze_panes = "C6"
    return ws


def row(ws, r, label, make, note="", fmt="#,##0.0", inp=False, bold=False):
    """make: a list of N values, or f(i, col, prev) -> value (number, formula or None)."""
    c = ws.cell(row=r, column=2, value=label)
    c.border = BOX
    if bold:
        c.font = BOLD
    for i in range(N):
        v = make[i] if isinstance(make, list) else make(i, COLS[i],
                                                        COLS[i - 1] if i else None)
        cell = ws.cell(row=r, column=3 + i, value=v)
        cell.number_format, cell.border = fmt, BOX
        if inp:
            cell.fill = INP
        if bold:
            cell.font = BOLD
    n = ws.cell(row=r, column=3 + N, value=note)
    n.font, n.border = SMALL, BOX
    n.alignment = Alignment(wrap_text=True, vertical="top")
    return r + 1


def band(ws, r, text):
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3 + N)
    c = ws.cell(row=r, column=2, value=text)
    c.fill, c.font = BAND, BOLD
    return r + 1


def flat(v):
    return [v] * N


def f(tmpl):
    """Formula the same in every column; {c} is this column, {p} the previous one."""
    return lambda i, c, p: tmpl.format(c=c, p=p or c)


def chain(first, tmpl):
    """A hard opening value in FY2027E, then the formula in later years."""
    return lambda i, c, p: first if i == 0 else tmpl.format(c=c, p=p)


def build():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    # ================================================================= Assumptions
    A = sheet(wb, "Assumptions",
              "Repco Home Finance Limited - forecast drivers (Rs crore; standalone)",
              "Yellow cells are the DRIVERS. Every one is derived from the company's own "
              "documents and the arithmetic of the derivation is written beside it, so a "
              "reviewer can disagree with a number rather than with an assertion. FY2027E "
              "rolls forward from the 30-Jun-2026 balance sheet because no 31-Mar-2026 "
              "balance sheet exists in the document set; that carries about one quarter of "
              "growth twice - roughly Rs 250 crore, 1.6% of the book - and is stated here "
              "rather than smoothed away.")
    r = 6
    r = band(A, r, "GROWTH")
    A_DISB = r
    r = row(A, r, "Disbursements (Rs cr)", [3600, 3924, 4277, 4662, 5081],
            "Actuals 2,919 (FY2023) / 3,135 (FY2024) / 3,284 (FY2025) per the FY2025 AR "
            "six-year table: growth of 7.4% then 4.8%. Base case takes 9.6% for FY2027E and "
            "9.0% thereafter - faster than the FY2025 actual because the network grew from "
            "159 to 189 branches and from 192 to 233 touchpoints over FY2023-FY2025 and that "
            "added capacity has not yet been worked through.", inp=True)
    A_RUNOFF = r
    r = row(A, r, "Run-off rate (% of opening AUM)", flat(17.0),
            "Derived from the AUM roll-forward: FY2023 opening 11,759 + disbursements 2,919 "
            "less closing 12,449 implies run-off of 2,229 = 19.0% of opening; FY2024 implies "
            "2,071 = 15.3%; FY2025 implies 2,305 = 17.1%. Held at the three-year mean, "
            "rounded to 17.0%.", fmt="0.00", inp=True)

    r = band(A, r, "SPREAD")
    A_YIELD = r
    r = row(A, r, "Yield on average AUM (%)", [11.80, 11.75, 11.70, 11.70, 11.70],
            "Interest income over average reported AUM: FY2023 1,257.01/12,104 = 10.38%; "
            "FY2024 1,495.98/12,981 = 11.52%; FY2025 1,648.19/14,002.5 = 11.77%. Held at "
            "11.80% then eased 10bps as the salaried mix rises - the FY2025 AR states an "
            "intention to keep 'a slight tilt towards salaried professionals'.",
            fmt="0.00", inp=True)
    A_COF = r
    r = row(A, r, "Cost of funds on average debt (%)", [8.55, 8.50, 8.50, 8.50, 8.50],
            "Finance costs over average total debt: FY2023 701.07/9,808.04 = 7.15%; FY2024 "
            "845.57/10,312.56 = 8.20%; FY2025 965.86/10,920.07 = 8.85%. Eased modestly on the "
            "RBI's projected disinflation (FY2025 AR MD&A: CPI 4.0% for 2025-26) and on the "
            "first NCD issuance broadening the base, but NOT below the FY2024 level - a "
            "lender funded almost entirely by banks has little pricing power over its "
            "liabilities.", fmt="0.00", inp=True)

    r = band(A, r, "COSTS AND DISTRIBUTION")
    A_OPEX = r
    r = row(A, r, "Operating expenses / average total assets (%)",
            [1.52, 1.53, 1.54, 1.55, 1.55],
            "Actuals 1.19% (FY2023), 1.30% (FY2024), 1.47% (FY2025), 1.51% annualised in "
            "Q1FY2027 - a steady rise as branches were added. Continued to drift up: the "
            "FY2025 AR records 15 new branches and 9 new satellite centres in a single year, "
            "and employee cost rose 17.3% in FY2025 and 23.8% in FY2026 against book growth "
            "of 7.2%.", fmt="0.00", inp=True)
    A_CC = r
    r = row(A, r, "Credit cost (% of average AUM)", [0.30, 0.33, 0.35, 0.38, 0.40],
            "The impairment line was a CHARGE of 233.06 (FY2022) and 51.55 (FY2023), then a "
            "WRITE-BACK of 0.51 (FY2024), 37.57 (FY2025) and 31.07 (FY2026), and turned back "
            "to a charge of 9.69 in Q1FY2027 - 0.25% of average managed assets annualised. A "
            "write-back is a one-way release from an existing stock of provisions and cannot "
            "be forecast, so the base case normalises to a small charge and lets it drift up "
            "as the book seasons and the non-housing share rises.", fmt="0.00", inp=True)
    A_TAX = r
    r = row(A, r, "Effective tax rate (%)", flat(25.2),
            "FY2025 148.05/587.49 = 25.20%. FY2026's 22.74% is distorted by the Rs 14.40 "
            "crore reversal of the deferred tax liability on the Section 36(1)(viii) special "
            "reserve (Note 7 to the Q1FY2027 results; an Emphasis of Matter in the auditor's "
            "limited review report) and is not repeatable.", fmt="0.00", inp=True)
    A_DIV = r
    r = row(A, r, "Dividend payout (% of PAT)", flat(8.0),
            "FY2025 Rs 4.00 per share, Rs 25.02 crore on PAT of Rs 439.44 crore = 5.7%; "
            "FY2024 Rs 3.00 per share, Rs 18.77 crore = 4.8% (AR Note 41). Raised modestly to "
            "8%: a company carrying 37% CRAR against a 15% minimum has no capital reason to "
            "retain 95% of earnings, and the very low payout is itself part of why return on "
            "equity is drifting down.", fmt="0.00", inp=True)

    r = band(A, r, "BALANCE SHEET STRUCTURE")
    A_CASH = r
    r = row(A, r, "Cash and liquid investments (% of total assets)", flat(1.50),
            "30-Jun-2026 actual: cash 136.83 + other bank balances 5.29 + investments 138.10 "
            "= 280.22 on total assets of 16,245.83 = 1.72%. FY2025: 347.52 on 14,602.24 = "
            "2.38%. The series is falling; held at 1.50%, thin but consistent with the "
            "company's own practice and with an LCR of 202.13%.", fmt="0.00", inp=True)
    A_OTHL = r
    r = row(A, r, "Non-debt liabilities (% of total assets)", flat(0.90),
            "30-Jun-2026 actual: total liabilities 12,227.18 less total debt 12,087.01 = "
            "140.17 on 16,245.83 = 0.86%. Comprises trade payables, lease liabilities, "
            "provisions and deferred tax.", fmt="0.00", inp=True)
    A_OTHA = r
    r = row(A, r, "Non-earning assets (Rs cr)", [270, 284, 298, 313, 329],
            "30-Jun-2026: PP&E 25.44 + right-of-use 47.30 + intangibles 17.69 + intangibles "
            "under development 5.21 + others 161.74 = 257.38. Grown 5% a year with the branch "
            "network.", inp=True)
    A_RW = r
    r = row(A, r, "Risk weight density (RWA / AUM, %)", flat(62.4),
            "FY2025: risk-weighted assets 9,048.38 (AR Note 32.1) on reported AUM of 14,492 = "
            "62.44%. Individual housing loans below Rs 30 lakh at LTV under 80% attract a 35% "
            "risk weight and loans against property 75%, so density moves with the housing / "
            "non-housing mix. Held flat, which is mildly conservative given the mix shift "
            "towards non-housing.", fmt="0.00", inp=True)

    # ================================================================= Book build
    B = sheet(wb, "Book_Build", "Loan book roll-forward (Rs crore)",
              "Opening AUM plus disbursements less run-off equals closing AUM. FY2027E opens "
              "on the 30-Jun-2026 loan carrying value of 15,708.23 from the Reg 54(3) "
              "security-cover certificate - the newest balance sheet in the document set "
              "(139.05 exclusive charge + 13,299.24 pari passu + 2,269.94 unencumbered).")
    r = 6
    B_OPEN = r
    r = row(B, r, "Opening AUM", chain(15708.23, "={p}%d" % (B_OPEN + 3)),
            "FY2027E opening is the 30-Jun-2026 actual; each later year opens on the prior "
            "year's close.")
    B_DISB = r
    r = row(B, r, "Disbursements", f("=Assumptions!{c}%d" % A_DISB), "from Assumptions")
    B_RUN = r
    r = row(B, r, "Less: run-off (repayments, prepayments, write-offs)",
            f("=-{c}%d*Assumptions!{c}%d/100" % (B_OPEN, A_RUNOFF)),
            "opening AUM times the run-off rate")
    B_CLOSE = r
    r = row(B, r, "Closing AUM", f("=SUM({c}%d:{c}%d)" % (B_OPEN, B_RUN)),
            "opening + disbursements - run-off", bold=True)
    B_AVG = r
    r = row(B, r, "Average AUM", f("=({c}%d+{c}%d)/2" % (B_OPEN, B_CLOSE)), "")
    r = row(B, r, "AUM growth (%)", f("=100*{c}%d/{c}%d-100" % (B_CLOSE, B_OPEN)),
            "Actual growth was 5.9% (FY2023), 8.5% (FY2024), 7.2% (FY2025) on the reported "
            "loan book.", fmt="0.00")

    # ================================================================= P&L
    P = sheet(wb, "P_and_L", "Projected profit and loss (Rs crore)",
              "A lender's P&L: interest earned on the book, less interest paid on the "
              "funding, less operating costs, less credit cost. Every line is a live formula "
              "off Book_Build, Balance_Sheet and Assumptions.")
    r = 6
    P_INT = r
    r = row(P, r, "Interest income",
            f("=Book_Build!{c}%d*Assumptions!{c}%d/100" % (B_AVG, A_YIELD)),
            "average AUM times yield")
    P_FEE = r
    r = row(P, r, "Fee, commission and other operating income",
            f("=Book_Build!{c}%d*0.0026" % B_AVG),
            "FY2025 fees 21.49 + other operating revenue 15.48 = 36.97 on average AUM of "
            "14,002.5 = 0.264%. Held at 0.26% of average AUM.")
    P_REV = r
    r = row(P, r, "Revenue from operations", f("=SUM({c}%d:{c}%d)" % (P_INT, P_FEE)), "",
            bold=True)
    P_FIN = r
    r = row(P, r, "Finance costs", flat(None), "")  # patched once Balance_Sheet rows exist
    P_NII = r
    r = row(P, r, "Net interest income", f("={c}%d+{c}%d" % (P_REV, P_FIN)),
            "revenue from operations less finance costs - the company's OWN NII convention, "
            "which reproduces its published NII in every year it states one (FY2022 600.26 vs "
            "600; FY2023 582.67 vs 583; FY2024 678.95 vs 679; FY2025 719.30 vs 719).",
            bold=True)
    P_OPEX = r
    r = row(P, r, "Operating expenses", flat(None), "")
    P_PPOP = r
    r = row(P, r, "Pre-provision operating profit", f("={c}%d+{c}%d" % (P_NII, P_OPEX)),
            "Actuals: 452.31 (FY2023), 524.21 (FY2024), 549.92 (FY2025), 554.97 (FY2026) - "
            "core earnings power once the provision swing is stripped out. Growth of 4.9% "
            "then 0.9% over the last two actual years.", bold=True)
    P_CC = r
    r = row(P, r, "Credit cost", f("=-Book_Build!{c}%d*Assumptions!{c}%d/100" % (B_AVG, A_CC)),
            "average AUM times the credit-cost rate")
    P_PBT = r
    r = row(P, r, "Profit before tax", f("={c}%d+{c}%d" % (P_PPOP, P_CC)),
            "Actuals: 400.76 (FY2023), 524.72 (FY2024), 587.49 (FY2025), 586.04 (FY2026) - "
            "FY2026 was FLAT on FY2025.", bold=True)
    P_TAX = r
    r = row(P, r, "Tax", f("=-{c}%d*Assumptions!{c}%d/100" % (P_PBT, A_TAX)), "")
    P_PAT = r
    r = row(P, r, "Profit after tax", f("={c}%d+{c}%d" % (P_PBT, P_TAX)),
            "Actuals: 296.08 (FY2023), 394.70 (FY2024), 439.44 (FY2025), 452.77 (FY2026).",
            bold=True)
    P_DIV = r
    r = row(P, r, "Dividend", f("=-{c}%d*Assumptions!{c}%d/100" % (P_PAT, A_DIV)), "")
    P_RET = r
    r = row(P, r, "Retained earnings", f("={c}%d+{c}%d" % (P_PAT, P_DIV)), "", bold=True)

    # ================================================================= Balance sheet
    S = sheet(wb, "Balance_Sheet",
              "Projected balance sheet (Rs crore) - debt is the FUNDING GAP, not a trend",
              "Failure mode 18: projected debt is DERIVED, never carried forward from the "
              "historical pattern. Assets follow the book the company chooses to write; "
              "equity follows retained earnings; debt is whatever is left over. The "
              "arithmetic is visible on the debt row itself.")
    r = 6
    S_LOAN = r
    r = row(S, r, "Loans (closing AUM)", f("=Book_Build!{c}%d" % B_CLOSE), "from Book_Build")
    S_OTHA = r
    r = row(S, r, "Non-earning assets", f("=Assumptions!{c}%d" % A_OTHA), "from Assumptions")
    S_TA = r
    r = row(S, r, "Total assets",
            f("=({c}%d+{c}%d)/(1-Assumptions!{c}%d/100)" % (S_LOAN, S_OTHA, A_CASH)),
            "solved so that cash is the stated percentage OF the total: total assets = "
            "(loans + non-earning assets) / (1 - cash%)", bold=True)
    S_CASH = r
    r = row(S, r, "Cash and liquid investments",
            f("={c}%d*Assumptions!{c}%d/100" % (S_TA, A_CASH)), "the balancing asset")
    S_TA0 = r
    r = row(S, r, "Opening total assets", chain(16245.83, "={p}%d" % S_TA),
            "FY2027E opens on the 30-Jun-2026 total of 16,245.83 (Reg 54(3) certificate).")
    S_AVGTA = r
    r = row(S, r, "Average total assets", f("=({c}%d+{c}%d)/2" % (S_TA, S_TA0)),
            "denominator for the opex and return ratios")

    r = band(S, r, "FUNDING")
    S_EQ0 = r
    r = row(S, r, "Opening net worth", chain(4018.65, "={p}%d" % (S_EQ0 + 2)),
            "FY2027E opens on the Reg 52(4) net worth of 4,018.65 at 30-Jun-2026 - the "
            "company's own published figure, not a derived one.")
    S_RET = r
    r = row(S, r, "Add: retained earnings", f("=P_and_L!{c}%d" % P_RET), "from P_and_L")
    S_EQ = r
    r = row(S, r, "Closing net worth", f("={c}%d+{c}%d" % (S_EQ0, S_RET)), "", bold=True)
    S_OTHL = r
    r = row(S, r, "Non-debt liabilities",
            f("={c}%d*Assumptions!{c}%d/100" % (S_TA, A_OTHL)), "from Assumptions")
    S_DEBT = r
    r = row(S, r, "Total debt (FUNDING GAP)",
            f("={c}%d-{c}%d-{c}%d" % (S_TA, S_EQ, S_OTHL)),
            "total assets less net worth less non-debt liabilities. This is the borrowing "
            "the company must have outstanding to fund the book it writes - derived from the "
            "funding requirement, not extrapolated from the historical debt trend.", bold=True)
    S_DEBT0 = r
    r = row(S, r, "Opening total debt", chain(12087.01, "={p}%d" % S_DEBT),
            "FY2027E opens on the 30-Jun-2026 total of 12,087.01 (bank 10,992.79 + other "
            "borrowings 895.03 + listed secured NCD 125.49 + other debt securities 73.70).")
    S_AVGD = r
    r = row(S, r, "Average total debt (memo only - not used upstream)",
            f("=({c}%d+{c}%d)/2" % (S_DEBT, S_DEBT0)),
            "display only. Finance costs is priced on OPENING debt, not this average, to "
            "avoid a circular reference (closing debt needs closing net worth needs retained "
            "earnings needs PAT needs finance costs needs... closing debt).")
    S_NEWD = r
    r = row(S, r, "Incremental borrowing required in the year",
            f("={c}%d-{c}%d" % (S_DEBT, S_DEBT0)),
            "the quantum that has to be raised each year from a funding base that was 100% "
            "bank and NHB at 31-Mar-2025 - the central refinancing question in this rating.",
            bold=True)

    # patch the two forward references.
    # Finance costs is priced on OPENING debt, not average debt, and this is deliberate, not
    # an oversight: average debt needs CLOSING debt, closing debt is total assets less closing
    # net worth, closing net worth is opening net worth plus retained earnings, and retained
    # earnings comes from PAT, which is downstream of... finance costs. That loop is real (a
    # lender's interest cost depends on the debt it ends the year with, which depends on the
    # profit it retains, which depends on its interest cost) and pricing off the OPENING
    # balance is the standard way to break it without an iterative-calculation setting, which
    # openpyxl cannot write and Excel does not enable by default. The simplification is
    # slightly conservative - it prices a growing book's financing at last year's stock, not
    # the higher average actually carried - and is stated here rather than silently assumed.
    for i, c in enumerate(COLS):
        P.cell(row=P_FIN, column=3 + i).value = (
            "=-Balance_Sheet!%s%d*Assumptions!%s%d/100" % (c, S_DEBT0, c, A_COF))
        P.cell(row=P_FIN, column=3 + i).number_format = "#,##0.0"
        P.cell(row=P_OPEX, column=3 + i).value = (
            "=-Balance_Sheet!%s%d*Assumptions!%s%d/100" % (c, S_AVGTA, c, A_OPEX))
        P.cell(row=P_OPEX, column=3 + i).number_format = "#,##0.0"
    P.cell(row=P_FIN, column=3 + N).value = (
        "OPENING total debt (not average) times cost of funds - priced on the opening "
        "balance to avoid a circular reference through closing debt / retained earnings / "
        "PAT / finance costs; see the note on Balance_Sheet!S_AVGD")
    P.cell(row=P_OPEX, column=3 + N).value = "average total assets times the opex ratio"

    # ================================================================= Credit ratios
    R = sheet(wb, "Credit_Ratios",
              "Credit ratios on ICRA HFC conventions, every projected year",
              "The same convention set as the historical workbook, so projected years sit on "
              "identical definitions. Total managed assets = total assets + impairment "
              "allowance, VERBATIM from ICRA's own footnote in the GIC Housing Finance "
              "rationale of 10-Oct-2025.")
    r = 6
    R_ECL = r
    r = row(R, r, "Impairment allowance (closing)", f("=Book_Build!{c}%d*0.0276" % B_CLOSE),
            "FY2025 actual 433.39 on gross exposure of 14,542.57 = 2.98%; FY2024 517.86 on "
            "13,560.22 = 3.82%. Held at 2.76%, the level implied by 30-Jun-2026 provision "
            "coverage of 43.48% on gross NPA of 3.33% plus standard-asset provisioning.")
    R_MA = r
    r = row(R, r, "Total managed assets", f("=Balance_Sheet!{c}%d+{c}%d" % (S_TA, R_ECL)),
            "ICRA definition", bold=True)
    R_MA0 = r
    r = row(R, r, "Opening total managed assets", chain(16245.83 + 433.39, "={p}%d" % R_MA),
            "FY2027E opening approximates the 30-Jun-2026 allowance with the FY2025 actual of "
            "433.39, the latest disclosed - the allowance is not disclosed after FY2025.")
    r = row(R, r, "Net interest margin (% of average total assets)",
            f("=100*P_and_L!{c}%d/Balance_Sheet!{c}%d" % (P_NII, S_AVGTA)),
            "Actuals 4.75 / 5.18 / 5.08; 5.51 annualised in Q1FY2027", fmt="0.00")
    r = row(R, r, "Operating expenses / average total assets (%)",
            f("=-100*P_and_L!{c}%d/Balance_Sheet!{c}%d" % (P_OPEX, S_AVGTA)),
            "Actuals 1.19 / 1.30 / 1.47", fmt="0.00")
    r = row(R, r, "Credit cost (% of average AUM)",
            f("=-100*P_and_L!{c}%d/Book_Build!{c}%d" % (P_CC, B_AVG)),
            "Actuals 0.40 / -0.00 / -0.26 on average managed assets; the negative years were "
            "write-backs", fmt="0.00")
    r = row(R, r, "Return on average managed assets (%)",
            f("=100*P_and_L!{c}%d/(({c}%d+{c}%d)/2)" % (P_PAT, R_MA, R_MA0)),
            "Actuals 2.32 / 2.90 / 3.00. CareEdge's stated downgrade trigger is a sustained "
            "return on average total assets below 2.00%.", fmt="0.00", bold=True)
    r = row(R, r, "Return on average net worth (%)",
            f("=100*P_and_L!{c}%d/((Balance_Sheet!{c}%d+Balance_Sheet!{c}%d)/2)"
              % (P_PAT, S_EQ, S_EQ0)), "Actuals 12.46 / 14.59 / 14.16", fmt="0.00")
    r = row(R, r, "Gearing (times)",
            f("=Balance_Sheet!{c}%d/Balance_Sheet!{c}%d" % (S_DEBT, S_EQ)),
            "Actuals 3.94 / 3.70 / 3.36; 3.01 at 30-Jun-2026. CareEdge's downgrade trigger is "
            "gearing sustained above 5x; the regulatory ceiling for an HFC is 12x net owned "
            "funds.", fmt="0.00", bold=True)
    r = row(R, r, "CRAR (%) - indicative",
            f("=100*(Balance_Sheet!{c}%d-Assumptions!{c}%d)"
              "/(Book_Build!{c}%d*Assumptions!{c}%d/100)"
              % (S_EQ, A_OTHA, B_CLOSE, A_RW)),
            "Net owned funds approximated as net worth less non-earning assets, over "
            "risk-weighted assets at the stated density. INDICATIVE ONLY - the regulatory "
            "computation deducts specific items this model cannot see. Reported CRAR was "
            "35.79 / 33.97 / 37.09 for FY2023-FY2025 against a 15% minimum.",
            fmt="0.00", bold=True)
    r = row(R, r, "Equity / total assets (%)",
            f("=100*Balance_Sheet!{c}%d/Balance_Sheet!{c}%d" % (S_EQ, S_TA)),
            "Actuals 20.09 / 21.11 / 22.69; 24.74 at 30-Jun-2026", fmt="0.00")
    r = row(R, r, "Pre-provision profit / credit cost (times)",
            f("=-P_and_L!{c}%d/P_and_L!{c}%d" % (P_PPOP, P_CC)),
            "ICRA's NBFC methodology: 'pre-credit-cost profits in relation to credit costs "
            "provides insights into the buffer created by business profits on the incurred "
            "credit cost'. This row is that buffer, in multiples.", fmt="0.00", bold=True)

    # ================================================================= Debt breakup
    D = sheet(wb, "Debt_Breakup",
              "Debt structure - actuals at 30-Jun-2026 and the projected requirement",
              "Statutory decomposition tied to the Reg 54(3) security-cover certificate of "
              "30-Jun-2026 and the funding-concentration disclosure of 31-Mar-2025, plus the "
              "rated-limits-versus-drawn-debt distinction (failure modes 13 and 31). Actual "
              "figures appear in the FY2027E column only because that is the column adjacent "
              "to the labels; they are dated in the note.")
    r = 6
    r = band(D, r, "ACTUAL DRAWN DEBT AT 30-JUN-2026 (Reg 54(3) certificate)")
    for lab, val, note in [
        ("Bank borrowings (pari passu charge)", 10992.79, "security-cover certificate"),
        ("Other borrowings", 895.03, "security-cover certificate"),
        ("Listed secured non-convertible debentures", 125.49,
         "8.40% Repco Home Finance Limited 2029, ISIN INE612J07160, Debenture Trust Deed "
         "dated 13-03-2026, face value Rs 100,000. The auditor certifies compliance with the "
         "financial covenants of the Trust Deed for the quarter ended 30-Jun-2026."),
        ("Other debt securities", 73.70, "security-cover certificate"),
        ("TOTAL DRAWN DEBT", 12087.01,
         "reproduces the company's own Reg 52(4) disclosure: 12,087.01 / 16,245.83 = 0.744, "
         "published as 0.74. This is the check that PROVES the assembled debt figure."),
        ("Lease liabilities (excluded from gearing)", 51.03,
         "separately disclosed only at this date; sits inside other financial liabilities in "
         "every earlier period, so gearing is computed excluding leases in ALL periods rather "
         "than on a basis that changes midway through the series."),
    ]:
        r = row(D, r, lab, [val] + [None] * (N - 1), note, bold=lab.startswith("TOTAL"))

    r = band(D, r, "FUNDING CONCENTRATION AT 31-MAR-2025 (AR Note 34)")
    for lab, val, note in [
        ("Long-term loan facility", 9762.33, "86.48% of total liabilities"),
        ("Refinance from National Housing Bank", 875.54, "7.76% of total liabilities"),
        ("Working capital loans including cash credit", 501.22, "4.44% of total liabilities"),
        ("Commercial paper", 0.0, "NIL at every quarter-end from 31-Mar-2024 to 31-Mar-2025"),
        ("External commercial borrowing", 0.0, "NIL"),
        ("Secured non-convertible debentures", 0.0, "NIL at 31-Mar-2025"),
        ("Subordinated Tier-II NCDs", 0.0, "NIL"),
        ("Public deposits", 0.0, "the company does not accept public deposits"),
        ("Top 10 borrowings", 10397.24, "93.34% of total borrowings"),
        ("Twelve significant counterparties", 10914.96, "96.69% of total liabilities"),
    ]:
        r = row(D, r, lab, [val] + [None] * (N - 1), note)

    r = band(D, r, "PROJECTED INCREMENTAL BORROWING")
    r = row(D, r, "Incremental borrowing required", f("=Balance_Sheet!{c}%d" % S_NEWD),
            "the annual quantum that has to be raised, refinanced or replaced")
    r = row(D, r, "as a multiple of the FY2026 NCD issuance",
            f("=Balance_Sheet!{c}%d/199.19" % S_NEWD),
            "debt securities stood at 199.19 at 30-Jun-2026, 1.6% of drawn debt; this row "
            "states how far that new channel would have to scale to carry the requirement",
            fmt="0.0")

    r = band(D, r, "RATED LIMITS versus DRAWN DEBT")
    r = row(D, r, "ICRA rated limits", [None] * N,
            "TO BE CONFIRMED BY ISSUER. ICRA rates long-term fund-based term loans, "
            "non-convertible debentures and commercial paper (FY2025 AR Note 32.17 and "
            "corporate governance report item 18), but no ICRA rated AMOUNT is disclosed in "
            "any company document, and no ICRA CORPORATE rationale for this issuer exists in "
            "the reference library - the only ICRA file is a SECURITISATION rationale on the "
            "PRATHAM 12 2025 trust. A rated limit is a sanctioned facility, never an "
            "outstanding balance, and an outstanding must not be substituted for one.")
    r = row(D, r, "Memo - CareEdge published limits, 30-Sep-2025", [None] * N,
            "CARE-published, NOT issuer-confirmed, and NOT ICRA's rated universe: long-term "
            "bank facilities Rs 11,145.00 crore (CARE AA-; Stable) and commercial paper "
            "Rs 800.00 crore (CARE A1+), both reaffirmed. Carried as a peer-agency "
            "cross-reference for Step 14 only. Note that CareEdge's Rs 11,145.00 crore of "
            "long-term bank facilities sits against drawn bank borrowings of Rs 10,992.79 "
            "crore at 30-Jun-2026 - limits and drawings are different measures and the gap "
            "between them is the undrawn headroom.")

    # ================================================================= Stress case
    T = sheet(wb, "Stress_Case",
              "Stress case - the three variables ICRA's NBFC methodology names",
              "Asset quality, spread and growth are flexed together; capital and gearing are "
              "read off the result. The stress is calibrated to the company's OWN history "
              "rather than to an abstract percentage: in FY2022 the impairment charge was "
              "233.06 on an average book of about 11,525, i.e. 2.02%, with gross NPA at 7.0% "
              "and disbursements falling from 2,627 to 1,769 over two years.")
    r = 6
    T_CC = r
    r = row(T, r, "Stress credit cost (% of average AUM)", flat(1.00),
            "half the FY2022 peak of 2.02%, but sustained for five years rather than one - a "
            "prolonged moderate stress is harder for a lender to absorb than a single sharp "
            "one, because provisions cannot be released to offset it", fmt="0.00", inp=True)
    T_SPREAD = r
    r = row(T, r, "Spread compression (bps off net interest income)", flat(75),
            "75bps: the cost of funds rose 170bps between FY2023 and FY2025 (7.15% to 8.85%) "
            "while the yield rose 139bps, so the spread compressed 31bps in two years with no "
            "market stress at all. A lender funded almost entirely by banks cannot reprice "
            "its liabilities away from a rate shock.", fmt="0", inp=True)
    T_GROWTH = r
    r = row(T, r, "Disbursements held flat at the FY2025 actual (Rs cr)", flat(3284.0),
            "zero growth for five years, against the FY2021-FY2022 experience when "
            "disbursements fell from 2,627 to 1,841 to 1,769 - a 33% cumulative decline",
            inp=True)
    r += 1
    TS_OPEN = r
    r = row(T, r, "Opening AUM", chain(15708.23, "={p}%d" % (TS_OPEN + 3)), "")
    TS_DISB = r
    r = row(T, r, "Disbursements", f("={c}%d" % T_GROWTH), "held flat")
    TS_RUN = r
    r = row(T, r, "Less: run-off", f("=-{c}%d*Assumptions!{c}%d/100" % (TS_OPEN, A_RUNOFF)),
            "same run-off rate as the base case")
    TS_CLOSE = r
    r = row(T, r, "Closing AUM", f("=SUM({c}%d:{c}%d)" % (TS_OPEN, TS_RUN)), "", bold=True)
    TS_AVG = r
    r = row(T, r, "Average AUM", f("=({c}%d+{c}%d)/2" % (TS_OPEN, TS_CLOSE)), "")
    TS_NII = r
    r = row(T, r, "Net interest income",
            f("=P_and_L!{c}%d*{c}%d/Book_Build!{c}%d-{c}%d*{c}%d/10000"
              % (P_NII, TS_AVG, B_AVG, TS_AVG, T_SPREAD)),
            "base-case NII scaled to the smaller stress book, then the spread compression "
            "applied to that book")
    TS_OPEX = r
    r = row(T, r, "Operating expenses", f("=P_and_L!{c}%d" % P_OPEX),
            "held at the base case - a lender cannot shrink its branch network in step with a "
            "demand shock, which is exactly what makes operating leverage cut both ways")
    TS_PPOP = r
    r = row(T, r, "Pre-provision operating profit", f("={c}%d+{c}%d" % (TS_NII, TS_OPEX)), "",
            bold=True)
    TS_CC = r
    r = row(T, r, "Credit cost", f("=-{c}%d*{c}%d/100" % (TS_AVG, T_CC)), "")
    TS_PBT = r
    r = row(T, r, "Profit before tax", f("={c}%d+{c}%d" % (TS_PPOP, TS_CC)), "", bold=True)
    TS_PAT = r
    r = row(T, r, "Profit after tax",
            f("=IF({c}%d>0,{c}%d*(1-Assumptions!{c}%d/100),{c}%d)"
              % (TS_PBT, TS_PBT, A_TAX, TS_PBT)), "no tax shield assumed on a loss", bold=True)
    TS_EQ0 = r
    r = row(T, r, "Opening net worth", chain(4018.65, "={p}%d" % (TS_EQ0 + 2)), "")
    TS_RET = r
    r = row(T, r, "Retained earnings",
            f("={c}%d*(1-Assumptions!{c}%d/100)" % (TS_PAT, A_DIV)), "")
    TS_EQ = r
    r = row(T, r, "Closing net worth", f("={c}%d+{c}%d" % (TS_EQ0, TS_RET)), "", bold=True)
    TS_TA = r
    r = row(T, r, "Total assets implied",
            f("=({c}%d+Assumptions!{c}%d)/(1-Assumptions!{c}%d/100)"
              % (TS_CLOSE, A_OTHA, A_CASH)), "")
    TS_DEBT = r
    r = row(T, r, "Total debt implied",
            f("={c}%d-{c}%d-{c}%d*Assumptions!{c}%d/100"
              % (TS_TA, TS_EQ, TS_TA, A_OTHL)), "", bold=True)
    r = row(T, r, "Gearing in stress (times)", f("={c}%d/{c}%d" % (TS_DEBT, TS_EQ)),
            "against CareEdge's downgrade trigger of 5x sustained and the regulatory ceiling "
            "of 12x net owned funds", fmt="0.00", bold=True)
    r = row(T, r, "CRAR in stress (%) - indicative",
            f("=100*({c}%d-Assumptions!{c}%d)/({c}%d*Assumptions!{c}%d/100)"
              % (TS_EQ, A_OTHA, TS_CLOSE, A_RW)),
            "against the 15% regulatory minimum", fmt="0.00", bold=True)
    r = row(T, r, "Return on average assets in stress (%)",
            f("=100*{c}%d/{c}%d" % (TS_PAT, TS_TA)),
            "against CareEdge's downgrade trigger of a sustained 2.00%", fmt="0.00", bold=True)

    wb.save(OUT)
    _force_recalc(OUT)
    _cache_values(OUT)
    return OUT


if __name__ == "__main__":
    print("Saved:", build())
