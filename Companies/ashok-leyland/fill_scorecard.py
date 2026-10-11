"""Fills Rating_Scorecard_Ashok Leyland Limited.xlsx (CLAUDE.md Step 12b, Stage 1 only).

Sector 'Auto OEM'. Historicals FY2024-FY2026 are AL STANDALONE audited actuals from
compute_ratios.py (the rated entity; the only basis with a full balance sheet - the automotive
view lacks a segment balance sheet, so it is cited in the notes instead). FY+1/FY+2 are COPIED
(never linked) from the Step 12 model's base case, each noting "source: forecast model".
Stage 2/3 (Committee overlay) is left empty here and filled at Step 17c.
"""
import importlib.util
import shutil
import sys
from pathlib import Path

import openpyxl

CASE = Path(__file__).resolve().parent
ROOT = CASE.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from make_spreads import _cache_values, _force_recalc  # noqa: E402

spec = importlib.util.spec_from_file_location("cr", CASE / "compute_ratios.py")
E = importlib.util.module_from_spec(spec)
spec.loader.exec_module(E)
R = E.compute()
v, tot = E.v, E.tot
OUT = CASE / "Rating_Scorecard_Ashok Leyland Limited.xlsx"
MODEL = CASE / "Ashok Leyland_Financial_Model_10Oct2026.xlsx"
Y3 = ["FY2024", "FY2025", "FY2026"]


def model_row(tab, label):
    ws = openpyxl.load_workbook(MODEL, data_only=True)[tab]
    for row in ws.iter_rows(values_only=True):
        if row[0] == label:
            return row[1:10]  # FY2023..FY2031E
    raise KeyError(label)


rev = model_row("Income Statement", "Revenue from operations")
opb = model_row("Income Statement", "OPBDITA (ICRA: excludes all other income)")
pat = model_row("Income Statement", "PROFIT AFTER TAX")
fc = model_row("Income Statement", "Finance costs (incl. unwinding of discount)")
capex = model_row("Cash Flow", "Capex (purchase of PPE and intangibles)")
div = model_row("Cash Flow", "Dividends paid")
repay = model_row("Cash Flow", "Repayment of borrowings")
newb = model_row("Cash Flow", "Proceeds from borrowings")
# index 3 = FY2026, 4 = FY2027E, 5 = FY2028E

shutil.copy(ROOT / "Rating_Scorecard.xlsx", OUT)
wb = openpyxl.load_workbook(OUT)
ws = wb["Inputs"]
ws["C4"], ws["C5"], ws["C6"], ws["C7"] = "Ashok Leyland Limited", "ICRA", "Auto OEM", "10-Oct-2026"

hist = [
    (12, [v(E.SA_PL, "Revenue from operations", p) for p in Y3], "Revenue from operations, standalone P&L"),
    (13, [R[p]["OPBDITA"] for p in Y3],
     "ICRA OPBDITA = revenue - operating costs; excludes ALL other income and exceptional items; "
     "equals the company's published EBITDA (4,607 / 4,931 / 5,732) - engine tie-outs"),
    (14, [v(E.SA_PL, "Depreciation and amortisation", p) for p in Y3], "standalone P&L"),
    (15, [v(E.SA_PL, "Finance costs", p) for p in Y3],
     "standalone P&L, total finance costs incl. non-cash unwinding of discount (conservative)"),
    (16, [v(E.SA_PL_PRINTED, "Profit for the year", p) for p in Y3],
     "reported PAT, after exceptional items (FY2026 Labour Codes 308.48 + litigation 40.00)"),
    (17, [R[p]["Total debt"] for p in Y3],
     "borrowings + leases, standalone. AUTOMOTIVE view (consolidated ex-financial services) adds "
     "non-FS subsidiary borrowings of 1,607.50 / 2,418.99 / 3,538.63 - debt/OPBDITA 0.95x / "
     "0.93x / 0.98x at the low OPBDITA bound (engine table B)"),
    (18, [E.sa_free_liquidity(p) for p in Y3],
     "UNENCUMBERED only: excludes unclaimed-dividend, escrow, the FY2024 Rs 1,453.48 crore "
     "dividend account and the FY2026 Rs 100 crore Debenture Redemption Fund deposit (FM45)"),
    (19, [R[p]["Tangible net worth"] for p in Y3], "total equity; no revaluation reserve"),
    (20, [R[p]["Total outside liabilities"] for p in Y3], "total liabilities (incl. held-for-sale)"),
    (21, [tot(E.SA_CA, p) for p in Y3], "standalone balance sheet, total current assets"),
    (22, [tot(E.SA_CL, p) for p in Y3], "standalone balance sheet, total current liabilities"),
    (23, [v(E.SA_CF, "Capex (purchase of PPE & intangibles)", p) for p in Y3], "standalone cash flow"),
    (24, [v(E.SA_CF, "Dividend paid", p) for p in Y3], "standalone cash flow"),
]
for r, vals, note in hist:
    for j, x in enumerate(vals):
        ws.cell(r, 3 + j, round(x, 2))
    ws.cell(r, 6, note)

proj = [
    (29, rev[4] / rev[3] - 1, rev[5] / rev[4] - 1, "Revenue Model (volume +5%/+5%, realisation +1.5%)"),
    (30, opb[4] / rev[4], opb[5] / rev[5], "Assumptions (OPBDITA margin 13.0% / 13.0%)"),
    (31, capex[4], capex[5], "Assumptions (capex)"),
    (32, (newb[4] or 0) - repay[4], (newb[5] or 0) - repay[5],
     "Cash Flow (scheduled repayment 483.82 then 129.47; no funding-gap draw in the base case)"),
    (33, 0.063, 0.063, "Assumptions (6.3% on borrowings; total finance cost also carries the "
     "Rs 95.69 crore unwinding of discount)"),
    (34, 0.255, 0.255, "Assumptions (effective tax 25.5%)"),
    (35, div[4] / pat[4], div[5] / pat[5],
     "Cash Flow / Income Statement: FY+1 includes the Rs 1,468.46 crore 2nd interim declared "
     "28-May-2026 plus a Rs 1/share interim; FY+2 = 55% of prior-year PAT"),
]
for r, a, b, src in proj:
    ws.cell(r, 3, round(a, 4))
    ws.cell(r, 4, round(b, 4))
    ws.cell(r, 5, "source: forecast model (Ashok Leyland_Financial_Model_10Oct2026.xlsx, %s)" % src)

ws["C39"] = 3.5
ws["F39"] = ("Override 3.0 -> 3.5. The 'Auto OEM' base blends passenger and two-wheeler OEMs; CVs "
             "are more cyclical. AL's own ten-year table: vehicles 1,97,366 (FY2019) -> 1,00,725 "
             "(FY2021), -49%, and a Rs 314 crore loss in FY2021. ICRA 1006 treats demand "
             "cyclicality as the central industry risk.")
ws["C40"] = 2
ws["F40"] = ("2 - established second-largest domestic M&HCV maker (30.3% share FY2026, MD&A) and "
             "bus leader (34.1%); LCV 74,322 units and 12.7% VAHAN share; spares Rs 4,450 crore "
             "and Power Solutions Rs 1,414 crore broaden the revenue base. Not 1: M&HCV share has "
             "eroded 31.8% -> 30.3% (trucks 32.3% -> 30.0%) since FY2023, CVs are still 82% of "
             "gross revenue, and exports only 7.0% (note 3.7.1).")
ws["C41"] = 3
ws["F41"] = ("3 - clean audits (PwC, unmodified FY2024-26) and a conservative balance sheet, BUT "
             "inter-corporate deposits to seven Hinduja promoter-group companies peaked at Rs 670 "
             "crore in FY2026 (Rs 490 crore FY2025; note 3.9.1) and Rs 2,670 crore of equity went "
             "into loss-making EV subsidiaries in FY2024-26 (Optare carrying value a KAM) - ICRA "
             "960 names 'financial support to group entities' as a governance consideration.")
ws["C42"] = 0
ws["F42"] = ("0 - no uplift claimed: AL is the operating flagship, not a supported subsidiary. Any "
             "group DRAG (HLF capital needs, EV subsidiaries, promoter-group ICDs) is argued at "
             "Stage 2 / Step 13, not netted here.")
ws["C43"] = "Superior"
ws["F43"] = ("Step 11 arithmetic: free liquidity Rs 6,950.80 crore + undrawn lines Rs 2,854.34 "
             "crore vs FY2027 debt repayments of Rs 483.82 crore (Rs 100 crore of it pre-funded "
             "in the DRF deposit); even the Tail scenario keeps free liquidity above Rs 2,700 "
             "crore with no new borrowing (model Scenarios tab).")
ws["C44"] = "Stable"
# ---- Stage 2: Rating Committee decision, Step 17c (see Committee_Minutes_10Oct2026.md) ----
ws["C63"] = 1
ws["D63"] = ("+1 Peer benchmarking / calibration (Committee, 10-Oct-2026): the financial composite "
             "(1.54) sits in the AA+/AAA cohort - standalone Total debt/OPBDITA 0.21x, interest "
             "coverage 33.77x, net cash Rs 5,755.76 crore, Superior liquidity that survives a "
             "repeat of FY2019-21 without borrowing (model Scenarios tab) - and the 18-Jul-2026 "
             "back-test documents that the composite-to-grade map under-rates AA+/AAA issuers. "
             "Not +2 (AAA): CV cyclicality, an eroding #2 M&HCV position and group cash calls "
             "(promoter-group ICDs up to Rs 670 crore, Rs 2,670 crore into subsidiaries FY2024-26).")
wb.save(OUT)
_force_recalc(OUT)
_cache_values(OUT)

wbv = openpyxl.load_workbook(OUT, data_only=True)
rat, sc = wbv["Rating"], wbv["Scorecard"]
for r in range(4, 40):
    a, b = rat.cell(r, 2).value, rat.cell(r, 3).value
    if a and b is not None:
        print("  Rating!C%-3d %-55s %s" % (r, str(a)[:55], b))
for r in range(37, 46):
    a, b = sc.cell(r, 2).value, sc.cell(r, 3).value
    if a:
        print("  Scorecard!C%-3d %-52s %s" % (r, str(a)[:52], b))
