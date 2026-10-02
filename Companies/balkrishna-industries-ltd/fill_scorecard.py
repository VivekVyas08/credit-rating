"""Fills Rating_Scorecard_Balkrishna Industries Limited.xlsx (CLAUDE.md Step 12b).

Uses the TEMPLATE'S OWN Inputs -> Scorecard -> Rating mechanism (sector = 'Auto components'),
so the anchor grade is the template's own formula chain reading back its own output.

Historicals: FY2024-FY2026 consolidated, from compute_ratios.py / the annual reports.
FY+1/FY+2 assumptions: COPIED (never linked) from the Step 12 model
(Balkrishna Industries Limited_5yr_Model.xlsx), each cell noting "source: forecast model" -
CLAUDE.md Step 12(e).
"""
import shutil
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
# make_spreads.py moved to tools/ when the project root was decluttered (01-Sep-2026).
sys.path.insert(0, str(ROOT / "tools"))
from make_spreads import _cache_values, _force_recalc          # noqa: E402

SRC = ROOT / "Rating_Scorecard.xlsx"
OUT = Path(__file__).resolve().parent / "Rating_Scorecard_Balkrishna Industries Limited.xlsx"


def main():
    shutil.copy(SRC, OUT)
    wb = openpyxl.load_workbook(OUT)
    ws = wb["Inputs"]

    ws["C4"] = "Balkrishna Industries Limited"
    ws["C5"] = "ICRA"
    ws["C6"] = "Auto components"
    ws["C7"] = "24-Aug-2026"

    # ---- historical financials (Rs crore, audited, consolidated) - FY2024/FY2025/FY2026
    hist = [
        ("Total operating income", 9368.87, 10446.95, 10823.08,
         "Revenue from operations, AR consolidated statement of profit and loss"),
        ("EBITDA (OPBDIT / PBILDT)", 2255.37, 2457.60, 2590.44,
         "OPBDITA = PBT + finance cost + depreciation - other income + non-operating charges "
         "inside Other Expenses (compute_ratios.py). FY2026 includes the Rs 290.01 cr forex-loss "
         "add-back required by failure mode 36 - without it the margin reads 21.25% instead of "
         "23.93% and the anchor is fed a decline that did not happen."),
        ("Depreciation & amortisation", 650.72, 680.66, 774.96, "AR consolidated P&L"),
        ("Interest expense", 112.87, 128.34, 133.62, "AR consolidated P&L, 'Finance costs'"),
        ("Profit after tax (PAT)", 1471.49, 1654.96, 1243.10,
         "AR consolidated P&L - FY2026 fell 24.9% on the North America tariff shock"),
        ("Total debt (incl. lease liabilities)", 3099.44, 3267.45, 4110.82,
         "NC + C borrowings + NC + C lease liabilities, compute_ratios.py"),
        ("Cash & liquid investments", 1428.99, 1789.03, 1391.99,
         "cash + other bank balances + CURRENT investments, compute_ratios.py"),
        ("Tangible net worth", 8853.82, 10387.60, 10955.29,
         "total equity - no material intangible/revaluation adjustment (intangibles peak at "
         "Rs 7.32 cr = 0.07% of equity), compute_ratios.py CONVENTIONS"),
        ("Total outside liabilities", 4830.72, 5247.06, 6811.05, "total assets - total equity"),
        ("Current assets", 4644.06, 5571.40, 5154.47, "AR consolidated balance sheet"),
        ("Current liabilities", 3660.44, 4226.65, 5089.00, "AR consolidated balance sheet"),
        ("Capital expenditure", 1098.55, 1483.00, 3003.29,
         "AR consolidated cash flow, 'Purchase of Property, Plant and equipment'"),
        ("Dividends paid", 309.45, 309.51, 309.19, "AR consolidated cash flow, 'Dividend paid'"),
    ]
    row_of = {"Total operating income": 12, "EBITDA (OPBDIT / PBILDT)": 13,
              "Depreciation & amortisation": 14, "Interest expense": 15,
              "Profit after tax (PAT)": 16, "Total debt (incl. lease liabilities)": 17,
              "Cash & liquid investments": 18, "Tangible net worth": 19,
              "Total outside liabilities": 20, "Current assets": 21,
              "Current liabilities": 22, "Capital expenditure": 23, "Dividends paid": 24}
    for label, fy24, fy25, fy26, note in hist:
        r = row_of[label]
        ws.cell(row=r, column=3, value=fy24)
        ws.cell(row=r, column=4, value=fy25)
        ws.cell(row=r, column=5, value=fy26)
        ws.cell(row=r, column=6, value=note)

    # ---- projection assumptions (FY+1/FY+2) - COPIED from the Step 12 model, never linked
    proj = [
        (29, "Revenue growth (%)", 0.08, 0.10,
         "source: forecast model (Assumptions!A_GROWTH) - FY2027E 8.0%, FY2028E 10.0%"),
        (30, "EBITDA margin (%)", 0.235, 0.235,
         "source: forecast model (Assumptions!A_MARGIN) - held near the FY2026 actual of 23.93%. "
         "ICRA's own 25-Aug-2026 rationale expects the rising share of lower-margin on-highway "
         "tyres to cause 'some moderation in blended profitability' that is 'largely offset by "
         "operating efficiencies' - i.e. roughly flat, not the recovery-from-a-trough the "
         "pre-correction version assumed."),
        (31, "Capital expenditure (Rs crore)", 1900, 1200,
         "source: forecast model (Assumptions!A_CAPEX) - against the Rs 6,800 cr cumulative "
         "announced programme and Rs 2,711.84 cr of FY2026 capital commitments"),
        (32, "Net new debt + / (repayment) (Rs crore)", -4110.82, 0,
         "source: forecast model (Balance_Sheet!S_DEBT_RAW) - the model's funding-gap "
         "arithmetic shows FULL repayment of the Rs 4,110.82 cr FY2026 debt stock in FY2027E, "
         "reaching a net-cash position by FY2028E and beyond (CareEdge's own 05-Mar-2026 "
         "rationale names 'a net debt free profile' as an achievable positive trigger for "
         "this issuer)"),
        (33, "Average interest rate on debt (%)", 0.075, 0.075,
         "source: forecast model (Assumptions!A_COF) - set above the FY2026 actual blended "
         "rate of ~4.1% (which reflects low-cost offshore subsidiary working-capital lines) "
         "since incremental Indian rupee term debt/NCD funding is assumed"),
        (34, "Tax rate (%)", 0.244, 0.244, "source: forecast model (Assumptions!A_TAX)"),
        (35, "Dividend payout (% of PAT)", 0.22, 0.22,
         "source: forecast model (Assumptions!A_DIV) - cash-flow basis, averaging the two "
         "observed years' cash-paid-to-PAT ratios (24.87% FY2026, 18.70% FY2025)"),
    ]
    for r, _lab, fy1, fy2, note in proj:
        ws.cell(row=r, column=3, value=fy1)
        ws.cell(row=r, column=4, value=fy2)
        ws.cell(row=r, column=5, value=note)

    # ---- qualitative assessment
    ws["B39"] = ("Industry risk override (blank = use sector base 3.5 from Ref_Weights) - "
                 "left BLANK. Auto components is a moderately cyclical, capital-intensive "
                 "global-export sector and the template's own base score for it is accepted "
                 "as-is.")
    ws["C40"] = 2
    ws["E40"] = ("Business risk / market position - largest Indian exporter of off-highway "
                 "tyres (CareEdge, 05-Mar-2026), present in 160+ countries, SKUs grown from "
                 "~2,700 (FY2019) to 3,600+ (CRISIL, 27-Feb-2026), replacement/OEM channel "
                 "mix 70.1%/28.7% (FY2026 AR) gives revenue stability. The geographic "
                 "diversification is also what transmitted the FY2026 tariff shock (North "
                 "America revenue -28.1%), which is why this scores 2 (strong) rather than 1.")
    ws["C41"] = 2
    ws["E41"] = ("Long-tenured promoter management (Poddar family), unmodified consolidated "
                 "audit opinion in every year reviewed (FY2023-FY2026), no restatements, "
                 "qualifications or governance red flags found in the materiality sweep. "
                 "Backward-integrated carbon black operations and demonstrated logistics "
                 "cost discipline (4.40% of revenue in FY2026 vs a 7.9%-9% industry "
                 "benchmark, company MD&A) evidence operational execution quality.")
    ws["C42"] = 0
    ws["E42"] = "No parent/group support notch - BKT is itself the ultimate listed entity."
    ws["C43"] = "Strong"
    ws["E43"] = ("Not Superior: DSCR 4.31x and ISCR 70.76x (company's own Reg 52(4) "
                 "disclosure, FY2026) and gearing that has stayed in a 0.31x-0.44x band "
                 "across FY2023-FY2026 are comfortable, but on-balance-sheet cash and liquid "
                 "investments of Rs 1,391.99 crore (FY2026) is moderate relative to the "
                 "capex programme scale (Rs 6,800 crore cumulative), and current ratio has "
                 "fallen to 1.01x (FY2026) from 1.32x (FY2025) as the capex programme drew "
                 "down working-capital-adjacent balances.")
    ws["C44"] = "Stable"

    wb.save(OUT)
    _force_recalc(OUT)
    _cache_values(OUT)

    wbv = openpyxl.load_workbook(OUT, data_only=True)
    rat = wbv["Rating"]
    print("Saved:", OUT.name)
    print("  Sector type          :", rat["F6"].value)
    print("  Composite (pre-notch):", rat["C6"].value)
    print("  Scale index pre-notch :", rat["C7"].value)
    print("  Support notches       :", rat["C8"].value)
    print("  Index after notches   :", rat["C9"].value)
    print("  Hard cap check        :", rat["C10"].value)
    print("  Index after caps      :", rat["C11"].value)
    print("  LONG-TERM ANCHOR GRADE :", rat["C12"].value)
    print("  SHORT-TERM ANCHOR GRADE:", rat["C13"].value)
    print("  Combined rating line   :", rat["C19"].value)
    sc = wbv["Scorecard"]
    print("\n  Financial-risk block (rows 6-11), score column F:")
    for r in range(6, 12):
        print("   ", sc.cell(row=r, column=2).value, "->", sc.cell(row=r, column=6).value)
    print("\n  Risk blocks (rows 17-24):")
    for r in range(17, 25):
        vals = [sc.cell(row=r, column=c).value for c in range(2, 6)]
        if vals[0]:
            print("   ", vals)


if __name__ == "__main__":
    main()
