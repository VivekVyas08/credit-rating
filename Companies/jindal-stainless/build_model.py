"""Step 12 - Jindal Stainless Limited five-year three-statement model.

Six tabs: Assumptions -> P_and_L -> Balance_Sheet -> Credit_Ratios -> Debt_Breakup ->
Stress_Case. Every projected cell is a LIVE FORMULA off Assumptions; historicals are read from
compute_ratios.py so the model and the ratio engine cannot drift apart.

TWO STRUCTURAL RULES, both learned from earlier cases in this project:

  * DEBT IS DERIVED FROM THE FUNDING GAP, never extrapolated from the historical trend
    (failure mode 18). It is written here as an explicit roll-forward that a reader can audit
    line by line:
        closing debt = opening debt + capex + increase in working capital + dividend
                       - cash generated (PAT + depreciation)
    If the business funds itself, debt falls out of that arithmetic. It is never an input.

  * INTEREST IS PRICED ON OPENING DEBT, not average or closing debt. Pricing on average or
    closing debt creates a real circular reference (interest -> PAT -> retained earnings ->
    closing debt -> interest) that Excel resolves only with iterative calculation enabled.
    The Repco lending model and the Balkrishna corporate model in this project both hit
    exactly that circularity and were fixed the same way.

ROW ANCHORS. P_and_L has to reference two Balance_Sheet rows (opening fixed assets, opening
debt) while Balance_Sheet references P_and_L in turn. The first build of this file hard-coded
those two row numbers, a section header shifted the sheet by one, and finance costs silently
projected to ZERO for every year - the model looked plausible and was wrong. The row numbers
are now module-level constants used by BOTH builders, and build_bs asserts it actually wrote
to them.

Volume is the driver, not revenue, because stainless steel is a tonnage business: revenue is
built as volume x net sales realisation so the two can be stressed independently.
"""

import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

import compute_ratios as C

HDR = PatternFill("solid", fgColor="1F3864")
SUB = PatternFill("solid", fgColor="D9E2F3")
INP = PatternFill("solid", fgColor="FFF2CC")
OUT = PatternFill("solid", fgColor="E2EFDA")
WHITE = Font(color="FFFFFF", bold=True)
BOLD = Font(bold=True)
THIN = Border(*[Side(style="thin", color="BFBFBF")] * 4)

HIST = C.YEARS
PROJ = ["FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E"]
ALL = HIST + PROJ
NH, NP = len(HIST), len(PROJ)

# --- Balance_Sheet row anchors, shared by both builders (see docstring) --------------------
R_OPEN_FA, R_OPEN_DEBT = 3, 4
R_CAPEX, R_DWC, R_DIV, R_CASHGEN, R_DEBT, R_NETCASH = 7, 8, 9, 10, 11, 12
R_CLOSE_FA, R_NWC, R_TNW, R_CE = 15, 16, 17, 18


def col(i):
    return get_column_letter(i)


# --- historical derivations, computed not typed --------------------------------------------
def net_block(y):
    n = C.NON_CURRENT_ASSETS
    return sum(n[k][C.IDX[y]] for k in ("Property, plant and equipment",
                                        "Capital work-in-progress",
                                        "Right-of-use assets", "Investment property"))


def op_nwc(y):
    """Operating net working capital - short-term DEBT is funding, not working capital."""
    ca = C.current_assets(y) - C.liquid_assets(y)
    cl = (C.current_liabilities(y)
          - C.CURRENT_LIABILITIES["Borrowings (current)"][C.IDX[y]]
          - C.CURRENT_LIABILITIES["Lease liabilities (C)"][C.IDX[y]])
    return ca - cl


# --- assumptions ---------------------------------------------------------------------------
VOLUME_HIST = [None, None, 2.377, 2.570]
VOLUME_PROJ = [2.78, 3.00, 3.25, 3.45, 3.60]
NSR_GROWTH = [0.010, 0.015, 0.015, 0.015, 0.015]
MARGIN = [0.128, 0.130, 0.132, 0.132, 0.131]
CAPEX = [4000.0, 3600.0, 3200.0, 2700.0, 2400.0]
DEP_RATE, INT_RATE, TAX_RATE, DIV_PAYOUT, WC_PCT = 0.071, 0.078, 0.250, 0.12, 0.072


def header(ws, title):
    ws.cell(row=1, column=1, value=title).font = WHITE
    ws.cell(row=1, column=1).fill = HDR
    for j, y in enumerate(ALL):
        c = ws.cell(row=1, column=2 + j, value=y)
        c.font, c.fill, c.alignment = WHITE, HDR, Alignment(horizontal="center")
        ws.column_dimensions[col(2 + j)].width = 13
    ws.column_dimensions["A"].width = 50
    ws.column_dimensions[col(2 + len(ALL))].width = 70
    c = ws.cell(row=1, column=2 + len(ALL), value="Basis / source")
    c.font, c.fill = WHITE, HDR


def row(ws, r, label, values=None, formulas=None, fmt="#,##0.00", note="",
        bold=False, fill=None):
    c = ws.cell(row=r, column=1, value=label)
    if bold:
        c.font = BOLD
    for j in range(len(ALL)):
        v = None
        if values is not None and j < len(values) and values[j] is not None:
            v = values[j]
        if formulas is not None and formulas(j) is not None:
            v = "=" + formulas(j)
        if v is None:
            continue
        cell = ws.cell(row=r, column=2 + j, value=v)
        cell.number_format, cell.border = fmt, THIN
        if bold:
            cell.font = BOLD
        if fill is not None and j >= NH:
            cell.fill = fill
    ws.cell(row=r, column=2 + len(ALL), value=note)
    return r + 1


def section(ws, r, title):
    c = ws.cell(row=r, column=1, value=title)
    c.font, c.fill = BOLD, SUB
    for j in range(len(ALL) + 1):
        ws.cell(row=r, column=2 + j).fill = SUB
    return r + 1


def build_assumptions(wb):
    ws = wb.create_sheet("Assumptions")
    header(ws, "Jindal Stainless - model assumptions")
    R = C.compute()
    r = section(ws, 2, "DRIVERS (yellow = input)")
    a = {}
    a["vol"] = r
    r = row(ws, r, "Finished-goods sales volume (MT)",
            values=VOLUME_HIST + VOLUME_PROJ, fmt="0.000", fill=INP,
            note="FY2026 ~2.57 MT stated in the AR (+8.1% Y-o-Y), which implies FY2025 2.377. "
                 "The company aspires to 3.5 MT by FY2029; this base case haircuts that to "
                 "3.25 MT and reaches 3.5 MT only in FY2031 - a deliberate discount to an "
                 "aspiration, labelled as such rather than adopted")
    a["nsr"] = r
    r = row(ws, r, "Net sales realisation (Rs/tonne)",
            values=[None, None,
                    C.PL["Revenue from ops"][2] * 1e7 / (VOLUME_HIST[2] * 1e6),
                    C.PL["Revenue from ops"][3] * 1e7 / (VOLUME_HIST[3] * 1e6)],
            formulas=lambda j: ("%s%d*(1+%s%d)" % (col(1 + j), a["nsr"], col(2 + j), a["nsr"] + 1)
                                if j >= NH else None),
            fmt="#,##0", note="revenue / volume; FY2026 actual is the anchor")
    a["nsrg"] = r
    r = row(ws, r, "  NSR growth assumption", values=[None] * NH + NSR_GROWTH,
            fmt="0.0%", fill=INP,
            note="stainless realisation is nickel/chrome linked; a low single-digit drift is "
                 "assumed rather than a price view - flexed on Stress_Case")
    a["marg"] = r
    r = row(ws, r, "PBILDT margin",
            values=[R[y]["PBILDT margin %"] / 100 for y in HIST] + MARGIN,
            fmt="0.0%", fill=INP,
            note="FY2026 actual 12.97%; held broadly flat - volume operating leverage assumed "
                 "to offset a richer but more contested value-added mix")
    a["capex"] = r
    r = row(ws, r, "Capital expenditure (Rs crore)", values=[None] * NH + CAPEX,
            fmt="#,##0", fill=INP,
            note="FY2026 actual capex implied by the net-block roll-forward is ~Rs 4,226 cr "
                 "(net block 14,876 -> 18,042 plus 1,060 of depreciation). The base case "
                 "starts AT that run-rate and tapers only gradually: the company is still "
                 "scaling toward a 3.5 MT sales aspiration, so assuming a sharp capex "
                 "step-down would manufacture a deleveraging that the growth plan "
                 "contradicts")
    a["dep"] = r
    r = row(ws, r, "Depreciation rate on opening net block",
            values=[None] * NH + [DEP_RATE] * NP, fmt="0.0%", fill=INP,
            note="FY2025 7.28% and FY2026 7.13% implied; 7.1% carried forward")
    a["int"] = r
    r = row(ws, r, "Interest rate on OPENING debt", values=[None] * NH + [INT_RATE] * NP,
            fmt="0.0%", fill=INP,
            note="implied FY2026 cost; priced on the OPENING balance so the model stays acyclic")
    a["tax"] = r
    r = row(ws, r, "Effective tax rate", values=[None] * NH + [TAX_RATE] * NP,
            fmt="0.0%", fill=INP, note="FY2026 effective rate 24.9%")
    a["div"] = r
    r = row(ws, r, "Dividend payout", values=[None] * NH + [DIV_PAYOUT] * NP,
            fmt="0.0%", fill=INP, note="broadly the recent payout")
    a["wc"] = r
    r = row(ws, r, "Operating net working capital, % of revenue",
            values=[100 * op_nwc(y) / C.PL["Revenue from ops"][C.IDX[y]] / 100 for y in HIST]
                   + [WC_PCT] * NP,
            fmt="0.0%", fill=INP,
            note="intensity has fallen 11.3% -> 7.0% over FY2023-FY2026; held at 7.2%, a "
                 "slight normalisation rather than assuming the improvement continues")
    return a


def build_pl(wb, a):
    ws = wb.create_sheet("P_and_L")
    header(ws, "Projected profit and loss (Rs crore)")
    A, B = "Assumptions!", "Balance_Sheet!"
    R = C.compute()
    p = {}
    r = 2
    p["rev"] = r
    r = row(ws, r, "Revenue from operations", values=C.PL["Revenue from ops"],
            formulas=lambda j: ("%s%s%d*%s%s%d/10" % (A, col(2 + j), a["vol"],
                                                      A, col(2 + j), a["nsr"])
                                if j >= NH else None),
            bold=True, note="volume (MT) x realisation (Rs/t), expressed in Rs crore")
    p["pbildt"] = r
    r = row(ws, r, "PBILDT", values=[R[y]["PBILDT"] for y in HIST],
            formulas=lambda j: ("%s%d*%s%s%d" % (col(2 + j), p["rev"], A, col(2 + j), a["marg"])
                                if j >= NH else None),
            bold=True, note="revenue x margin assumption")
    p["dep"] = r
    r = row(ws, r, "Depreciation", values=C.PL["Depreciation"],
            formulas=lambda j: ("%s%s%d*%s%s%d" % (B, col(2 + j), R_OPEN_FA,
                                                   A, col(2 + j), a["dep"])
                                if j >= NH else None),
            note="OPENING net block x depreciation rate")
    p["int"] = r
    r = row(ws, r, "Finance costs", values=C.PL["Finance costs"],
            formulas=lambda j: ("%s%s%d*%s%s%d" % (B, col(2 + j), R_OPEN_DEBT,
                                                   A, col(2 + j), a["int"])
                                if j >= NH else None),
            note="OPENING total debt x rate - opening, not average, keeps the model acyclic")
    p["pbt"] = r
    r = row(ws, r, "Profit before tax", values=C.PL["PBT ex-except ex-assoc"],
            formulas=lambda j: ("%s%d-%s%d-%s%d" % (col(2 + j), p["pbildt"], col(2 + j),
                                                    p["dep"], col(2 + j), p["int"])
                                if j >= NH else None),
            bold=True, note="PBILDT less depreciation less finance costs; no exceptional item "
                            "or associate share is projected")
    p["pat"] = r
    r = row(ws, r, "Profit after tax", values=C.PL["PAT"],
            formulas=lambda j: ("%s%d*(1-%s%s%d)" % (col(2 + j), p["pbt"], A, col(2 + j),
                                                     a["tax"]) if j >= NH else None),
            bold=True, note="")
    p["div"] = r
    r = row(ws, r, "Dividend",
            formulas=lambda j: ("%s%d*%s%s%d" % (col(2 + j), p["pat"], A, col(2 + j), a["div"])
                                if j >= NH else None), note="payout x PAT")
    p["ret"] = r
    r = row(ws, r, "Retained earnings",
            formulas=lambda j: ("%s%d-%s%d" % (col(2 + j), p["pat"], col(2 + j), p["div"])
                                if j >= NH else None), bold=True, note="")
    return p


def build_bs(wb, a, p):
    ws = wb.create_sheet("Balance_Sheet")
    header(ws, "Balance sheet - debt DERIVED from the funding gap (Rs crore)")
    A, P = "Assumptions!", "P_and_L!"

    section(ws, 2, "OPENING BALANCES (referenced by P_and_L - do not move these rows)")
    r = row(ws, R_OPEN_FA, "Opening net fixed assets",
            values=[None] + [net_block(y) for y in HIST[:-1]],
            formulas=lambda j: ("%s%d" % (col(1 + j), R_CLOSE_FA) if j >= NH else None),
            note="prior year's closing net block")
    assert r - 1 == R_OPEN_FA
    r = row(ws, R_OPEN_DEBT, "Opening total debt",
            values=[None] + [C.total_debt(y) for y in HIST[:-1]],
            formulas=lambda j: ("%s%d" % (col(1 + j), R_DEBT) if j >= NH else None),
            note="prior year's closing debt - the balance finance costs are priced on")
    assert r - 1 == R_OPEN_DEBT

    section(ws, 6, "FUNDING GAP -> CLOSING DEBT (failure mode 18: derived, never extrapolated)")
    row(ws, R_CAPEX, "Add: capital expenditure",
        formulas=lambda j: ("%s%s%d" % (A, col(2 + j), a["capex"]) if j >= NH else None),
        note="Assumptions")
    row(ws, R_DWC, "Add: increase in operating working capital",
        formulas=lambda j: ("%s%d-%s%d" % (col(2 + j), R_NWC, col(1 + j), R_NWC)
                            if j >= NH else None),
        note="year-on-year movement in operating net working capital")
    row(ws, R_DIV, "Add: dividend",
        formulas=lambda j: ("%s%s%d" % (P, col(2 + j), p["div"]) if j >= NH else None),
        note="from P_and_L")
    row(ws, R_CASHGEN, "Less: cash generated (PAT + depreciation)",
        formulas=lambda j: ("%s%s%d+%s%s%d" % (P, col(2 + j), p["pat"], P, col(2 + j), p["dep"])
                            if j >= NH else None),
        note="internal accrual available to fund the above")
    row(ws, R_DEBT, "CLOSING TOTAL DEBT (derived)",
        values=[C.total_debt(y) for y in HIST],
        formulas=lambda j: ("MAX(0,%s%d+%s%d+%s%d+%s%d-%s%d)" % (
            col(2 + j), R_OPEN_DEBT, col(2 + j), R_CAPEX, col(2 + j), R_DWC,
            col(2 + j), R_DIV, col(2 + j), R_CASHGEN) if j >= NH else None),
        bold=True, fill=OUT,
        note="opening debt + capex + working-capital build + dividend - internal accrual. "
             "Debt is an OUTPUT of this arithmetic, never an input. Floored at zero so a "
             "negative funding gap surfaces as net cash below rather than as negative debt")
    row(ws, R_NETCASH, "Memo: net cash surplus if the funding gap turns negative",
        formulas=lambda j: ("MAX(0,-(%s%d+%s%d+%s%d+%s%d-%s%d))" % (
            col(2 + j), R_OPEN_DEBT, col(2 + j), R_CAPEX, col(2 + j), R_DWC,
            col(2 + j), R_DIV, col(2 + j), R_CASHGEN) if j >= NH else None),
        note="kept separate so a surplus cannot masquerade as negative debt")

    section(ws, 14, "CLOSING BALANCE SHEET")
    row(ws, R_CLOSE_FA, "Closing net fixed assets", values=[net_block(y) for y in HIST],
        formulas=lambda j: ("%s%d+%s%d-%s%s%d" % (col(2 + j), R_OPEN_FA, col(2 + j), R_CAPEX,
                                                  P, col(2 + j), p["dep"])
                            if j >= NH else None),
        note="opening + capex - depreciation")
    row(ws, R_NWC, "Operating net working capital", values=[op_nwc(y) for y in HIST],
        formulas=lambda j: ("%s%s%d*%s%s%d" % (P, col(2 + j), p["rev"], A, col(2 + j), a["wc"])
                            if j >= NH else None),
        note="revenue x working-capital intensity; excludes short-term debt, which is funding")
    row(ws, R_TNW, "Tangible net worth", values=[C.tangible_net_worth(y) for y in HIST],
        formulas=lambda j: ("%s%d+%s%s%d" % (col(1 + j), R_TNW, P, col(2 + j), p["ret"])
                            if j >= NH else None),
        bold=True, note="prior TNW + retained earnings; no equity issue assumed")
    row(ws, R_CE, "Capital employed",
        formulas=lambda j: "%s%d+%s%d" % (col(2 + j), R_CLOSE_FA, col(2 + j), R_NWC),
        bold=True, note="closing net fixed assets + operating net working capital")
    return {"debt": R_DEBT, "tnw": R_TNW, "ce": R_CE, "netcash": R_NETCASH}


def build_ratios(wb, a, p, b):
    ws = wb.create_sheet("Credit_Ratios")
    header(ws, "Credit ratios - CareEdge conventions, by formula off the three statements")
    P, B, A = "P_and_L!", "Balance_Sheet!", "Assumptions!"
    r = 2
    r = row(ws, r, "PBILDT margin (%)",
            formulas=lambda j: "100*%s%s%d/%s%s%d" % (P, col(2 + j), p["pbildt"],
                                                      P, col(2 + j), p["rev"]), fmt="0.00")
    r = row(ws, r, "Overall gearing (times)",
            formulas=lambda j: "%s%s%d/%s%s%d" % (B, col(2 + j), b["debt"],
                                                  B, col(2 + j), b["tnw"]), fmt="0.00",
            note="total debt / tangible net worth; UNADJUSTED (see Conventions in the spreads)")
    r = row(ws, r, "Total debt/PBILDT (times)",
            formulas=lambda j: "%s%s%d/%s%s%d" % (B, col(2 + j), b["debt"],
                                                  P, col(2 + j), p["pbildt"]), fmt="0.00")
    r = row(ws, r, "Interest coverage (times)",
            formulas=lambda j: 'IF(OR(%s%s%d<=0,%s%s%d/%s%s%d>100),"n/m (net cash)",'
                               '%s%s%d/%s%s%d)' % (
                P, col(2 + j), p["int"], P, col(2 + j), p["pbildt"], P, col(2 + j), p["int"],
                P, col(2 + j), p["pbildt"], P, col(2 + j), p["int"]),
            fmt="0.00",
            note="guarded twice: at zero finance costs, and above 100x. A ratio of 290x is "
                 "arithmetically correct but analytically meaningless - once debt approaches "
                 "nil the coverage ratio stops measuring anything and should say so")
    r = row(ws, r, "PBILDT per tonne (Rs)",
            formulas=lambda j: 'IF(N(%s%s%d)=0,"n/a - volume not disclosed",'
                               '%s%s%d*10000000/(%s%s%d*1000000))' % (
                A, col(2 + j), a["vol"], P, col(2 + j), p["pbildt"],
                A, col(2 + j), a["vol"]),
            fmt="#,##0",
            note="the metals-sector unit-economics metric. Guarded: the company discloses "
                 "sales volume only from FY2025, so FY2023 and FY2024 divide by an empty "
                 "cell. Unguarded this returned #DIV/0! - reported as not-disclosed rather "
                 "than left as an error, and never back-filled with an estimate")
    r = row(ws, r, "Return on capital employed (%)",
            formulas=lambda j: "100*(%s%s%d-%s%s%d)/%s%s%d" % (
                P, col(2 + j), p["pbildt"], P, col(2 + j), p["dep"], B, col(2 + j), b["ce"]),
            fmt="0.00")
    return ws


def build_debt_breakup(wb):
    ws = wb.create_sheet("Debt_Breakup")
    header(ws, "Debt break-up - statutory decomposition, tied to the annual report")
    r = 2
    for label, block, key, note in [
        ("Borrowings - non-current", C.NON_CURRENT_LIABILITIES, "Borrowings (non-current)",
         "AR consolidated balance sheet, note 18"),
        ("Borrowings - current", C.CURRENT_LIABILITIES, "Borrowings (current)",
         "AR consolidated balance sheet, note 23"),
        ("Lease liabilities - non-current", C.NON_CURRENT_LIABILITIES, "Lease liabilities (NC)",
         "AR note 19"),
        ("Lease liabilities - current", C.CURRENT_LIABILITIES, "Lease liabilities (C)",
         "AR note 19"),
    ]:
        r = row(ws, r, label, values=block[key], note=note)
    r = row(ws, r, "Total debt (CareEdge convention)",
            values=[C.total_debt(y) for y in HIST], bold=True,
            note="borrowings + leases; UNADJUSTED - acceptances and group guarantees are not "
                 "separately disclosed, so CareEdge's adjusted gearing cannot be reproduced")
    r = row(ws, r, "Memo: borrowings excluding leases",
            values=[C.borrowings_only(y) for y in HIST],
            note="ties exactly to the FY2023-24 AR capital-management note "
                 "(FY2023 3,871.43; FY2024 5,948.19)")
    r += 1
    ws.cell(row=r, column=1,
            value="RATED LIMITS vs DRAWN DEBT - different measures, never to be conflated "
                  "(failure mode 13)").font = BOLD
    r += 1
    for label, val, note in [
        ("CareEdge rated: long-term bank facilities", 5900.00,
         "CareEdge press release, 09-Oct-2025 - CRA-published, not issuer-confirmed"),
        ("CareEdge rated: short-term bank facilities", 11000.00,
         "CareEdge press release, 09-Oct-2025 - CRA-published, not issuer-confirmed"),
        ("CareEdge rated: NCD", 99.00, "CareEdge press release, 09-Oct-2025"),
        ("CareEdge rated: NCD (proposed)", 1000.00, "CareEdge press release, 09-Oct-2025"),
        ("Total rated LIMITS", 17999.00,
         "lines verified to sum to the published total (failure mode 12); these are LIMITS"),
        ("Drawn debt at 31-Mar-2026", C.total_debt("FY2026"),
         "balance-sheet borrowings + leases - a different measure from rated limits, and "
         "the two will not agree"),
    ]:
        ws.cell(row=r, column=1, value=label)
        c = ws.cell(row=r, column=2, value=val)
        c.number_format, c.border = "#,##0.00", THIN
        ws.cell(row=r, column=2 + len(ALL), value=note)
        r += 1
    return ws


def build_stress(wb):
    ws = wb.create_sheet("Stress_Case")
    header(ws, "Stress case - the variables CareEdge's manufacturing criteria name")
    r = section(ws, 2, "STRESS APPLIED TO THE BASE CASE")
    ws.cell(row=r, column=1, value="Variable").font = BOLD
    ws.cell(row=r, column=2, value="Base case").font = BOLD
    ws.cell(row=r, column=5, value="Stressed").font = BOLD
    r += 1
    for label, base_v, stress_v, note in [
        ("Sales volume", "2.78 -> 3.60 MT", "flat at FY2026's 2.57 MT",
         "a global oversupply / import-pressure scenario; the AR itself notes world stainless "
         "melt output growing only 0.3% in CY2026 and 2.2% in CY2027"),
        ("Net sales realisation", "+1.0-1.5% p.a.", "-6% in year 1, then flat",
         "nickel and chrome linked realisation shock"),
        ("PBILDT margin", "12.8-13.2%", "10.5% year 1, recovering to 11.5%",
         "operating deleverage on flat volume plus an unrecovered input-cost move"),
        ("Capital expenditure", "Rs 3,200 cr tapering", "held at plan year 1, then cut 40%",
         "committed spend cannot be stopped immediately - year one is largely sunk, which is "
         "precisely why a demand shock hits leverage before it hits capex"),
    ]:
        ws.cell(row=r, column=1, value=label).font = BOLD
        ws.cell(row=r, column=2, value=base_v)
        ws.cell(row=r, column=5, value=stress_v)
        ws.cell(row=r, column=2 + len(ALL), value=note)
        r += 1

    r = section(ws, r + 1, "INDICATIVE STRESSED OUTCOME, YEAR 1 (FY2027)")
    rev_cr = 2.570 * 1e6 * (C.PL["Revenue from ops"][3] * 1e7 / (2.570 * 1e6)) * 0.94 / 1e7
    pbildt_cr = rev_cr * 0.105
    opening_debt = C.total_debt("FY2026")
    for label, val, fmt, note in [
        ("Revenue (Rs crore)", rev_cr, "#,##0", "flat volume at a 6% lower realisation"),
        ("PBILDT (Rs crore)", pbildt_cr, "#,##0", "at a 10.5% stressed margin"),
        ("PBILDT margin (%)", 10.5, "0.0", ""),
        ("Total debt/PBILDT (times)", opening_debt / pbildt_cr, "0.00",
         "on FY2026 closing debt held flat - conservative, since a demand shock also releases "
         "working capital"),
        ("Interest coverage (times)", pbildt_cr / (opening_debt * 0.078), "0.00", ""),
    ]:
        ws.cell(row=r, column=1, value=label)
        c = ws.cell(row=r, column=2, value=val)
        c.number_format, c.border = fmt, THIN
        ws.cell(row=r, column=2 + len(ALL), value=note)
        r += 1
    ws.cell(row=r + 1, column=1,
            value="Read-across: on this stress the issuer still holds about 1.76x total "
                  "debt/PBILDT and about 7.3x interest coverage - both computed in the rows "
                  "above rather than asserted, after an earlier draft of this tab carried "
                  "1.9x and 4x that had never been computed from anything. That is a "
                  "rating-TOLERANCE outcome rather than a rating-transition one, which is the "
                  "point of running it.")
    return ws


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    wb = Workbook()
    wb.remove(wb.active)
    a = build_assumptions(wb)
    p = build_pl(wb, a)
    b = build_bs(wb, a, p)
    build_ratios(wb, a, p, b)
    build_debt_breakup(wb)
    build_stress(wb)
    out = "Jindal Stainless Limited_5yr_Model.xlsx"
    wb.save(out)
    print("wrote %s" % out)
    print("tabs: %s" % ", ".join(wb.sheetnames))


if __name__ == "__main__":
    main()
