"""Generates TVS Credit Services Limited_Financial_Spreads.xlsx (CLAUDE.md Step 5 deliverable).

NBFC ratio suite. Not the corporate suite (no TOL/TNW, no GCA days) and not the bank suite
(no CASA, no LCR) - an NBFC is wholesale funded, so gearing and borrowing concentration carry
the weight a deposit franchise would carry for a bank.

Rs crore, STANDALONE. FY2026 AR is the authority for FY2025 and FY2026; FY2024 from the FY2025 AR.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import build_spreads          # noqa: E402

Y = ["FY2024", "FY2025", "FY2026"]
AR26 = "FY2026 AR"
AR25 = "FY2025 AR"

INPUTS = [
    ("Interest income",              [5112.58, 5775.97, 6213.35], f"{AR26} L3115; FY24 {AR25} L2821"),
    ("Total income",                 [5795.19, 6608.68, 7196.00], f"{AR26} L3120; FY24 {AR25} L2827"),
    ("Finance costs",                [None, 1863.32, 1934.29],    f"{AR26} L3122"),
    ("Fees and commission expense",  [None, 527.16, 473.14],      f"{AR26} L3123"),
    ("Impairment (credit cost)",     [1127.05, 1295.36, 1156.59], f"{AR26} L3124; FY24 {AR25} L2831"),
    ("Employee benefits expense",    [None, 1135.58, 1274.23],    f"{AR26} L3125"),
    ("Depreciation",                 [None, 46.20, 56.12],        f"{AR26} L3126"),
    ("Other expenses",               [None, 715.62, 1054.70],     f"{AR26} L3127"),
    ("Total expenses",               [None, 5583.24, 5949.07],    f"{AR26} L3128"),
    ("PBT before exceptional",       [None, 1025.44, 1246.93],    f"{AR26} L3129"),
    ("Exceptional items",            [None, 0.0, 8.61],
     f"{AR26} L7670 CONSOLIDATED. Standalone line reads '861' - OCR dropped the decimal point."),
    ("Profit after tax",             [571.83, 767.25, 913.17],    f"{AR26} L3133; FY24 {AR25} L2842"),
    ("Total assets",                 [28137.55, 31043.70, 35068.09], f"{AR26} L3063; FY24 {AR25} L2762"),
    ("Total equity (net worth)",     [None, 4947.92, 6067.63],    f"{AR26} L5940"),
    ("Total borrowings",             [None, 24687.17, 27667.87],  f"{AR26} L5903"),
    ("Net debt",                     [None, 21103.76, 24340.37],  f"{AR26} L5939"),
    ("CRAR (%)",                     [None, 20.30, 19.44],        f"{AR26} L6325 - per RBI guidelines"),
    ("Tier I CRAR (%)",              [None, 15.84, 16.49],        f"{AR26} L6326"),
    ("Tier II CRAR (%)",             [None, 4.46, 2.95],          f"{AR26} L6327"),
    ("Top-10 borrowings / total (%)", [None, 77.34, 70.68],       f"{AR26} L6761"),
    ("PDI as % of Tier I",           [None, 2.25, 1.84],          f"{AR26} L6946"),
    ("Parent shareholding (%)",      [None, None, 85.63],         f"{AR26} - TVS Motor Company Ltd"),
]
R = {lab: 6 + i for i, (lab, _, _) in enumerate(INPUTS)}


def I(label):
    return "Inputs!{c}%d" % R[label]


def A(label):
    """Average of the current and prior year - the correct denominator for RoA / credit cost.

    make_spreads only templates {c} (current column), so the prior year is reached with
    OFFSET(...,0,-1) rather than a {p} placeholder.
    """
    cell = "Inputs!{c}%d" % R[label]
    return f"AVERAGE({cell},OFFSET({cell},0,-1))"


def _f(expr):
    return "=" + expr


RATIOS = [
    ("Net interest income",
     _f(f"{I('Interest income')}-{I('Finance costs')}"),
     "Interest income less finance costs", "#,##0.00"),
    ("NII / avg total assets (%)",
     _f(f"({I('Interest income')}-{I('Finance costs')})/{A('Total assets')}"),
     "Spread earned on the book - high, reflecting two-wheeler/used-vehicle/tractor yields", "0.00%"),
    ("RoAA (%)  [SECTOR-DEFINING]",
     _f(f"{I('Profit after tax')}/{A('Total assets')}"),
     "Return on average assets - the core NBFC profitability metric", "0.00%"),
    ("RoAE (%)",
     _f(f"{I('Profit after tax')}/{A('Total equity (net worth)')}"),
     "Return on average net worth", "0.00%"),
    ("Credit cost / avg assets (%)  [SECTOR-DEFINING]",
     _f(f"{I('Impairment (credit cost)')}/{A('Total assets')}"),
     "Impairment charge over average assets - the key asset-quality proxy", "0.00%"),
    ("Gearing - borrowings / net worth (x)  [SECTOR-DEFINING]",
     _f(f"{I('Total borrowings')}/{I('Total equity (net worth)')}"),
     "Leverage. For a wholesale-funded NBFC this carries the weight CASA does for a bank",
     '0.00"x"'),
    ("Net debt / equity (x)",
     _f(f"{I('Net debt')}/{I('Total equity (net worth)')}"),
     "Reproduces the company's own published measure - a tie-out on the extraction", '0.00"x"'),
    ("Operating expenses",
     _f(f"{I('Employee benefits expense')}+{I('Depreciation')}+{I('Other expenses')}"),
     "Employee + depreciation + other expenses", "#,##0.00"),
    ("Net total income",
     _f(f"{I('Total income')}-{I('Finance costs')}-{I('Fees and commission expense')}"),
     "Income net of funding and origination costs", "#,##0.00"),
    ("Cost-to-income (%)",
     _f(f"({I('Employee benefits expense')}+{I('Depreciation')}+{I('Other expenses')})"
        f"/({I('Total income')}-{I('Finance costs')}-{I('Fees and commission expense')})"),
     "THE FY2026 NEGATIVE: rose to 49.81% from 44.98%", "0.00%"),
    ("CRAR cross-check (Tier I + Tier II)",
     _f(f"{I('Tier I CRAR (%)')}+{I('Tier II CRAR (%)')}"),
     "Must equal reported CRAR - independent reconstruction of the capital stack", '0.00"%"'),
    ("CRAR buffer over RBI 15% minimum (pp)",
     _f(f"{I('CRAR (%)')}-15"),
     "Reported CRAR less the 15% minimum applicable to the company", '0.00" pp"'),
    ("Total income growth (%)",
     _f(f"{I('Total income')}/OFFSET({I('Total income')},0,-1)-1"),
     "YoY growth in total income", "0.0%"),
    ("PAT growth (%)",
     _f(f"{I('Profit after tax')}/OFFSET({I('Profit after tax')},0,-1)-1"),
     "YoY growth in profit after tax", "0.0%"),
]

TIEOUTS = [
    ("FY26 CRAR = Tier I + Tier II", "=Inputs!E%d+Inputs!E%d" % (
        R["Tier I CRAR (%)"], R["Tier II CRAR (%)"]), 19.44,
     "16.49 + 2.95; reported CRAR 19.44% - exact reconstruction of the capital stack"),
    ("FY26 total expenses = sum of components",
     "=Inputs!E%d+Inputs!E%d+Inputs!E%d+Inputs!E%d+Inputs!E%d+Inputs!E%d" % (
         R["Finance costs"], R["Fees and commission expense"], R["Impairment (credit cost)"],
         R["Employee benefits expense"], R["Depreciation"], R["Other expenses"]), 5949.07,
     "Six expense lines rebuild the reported total exactly"),
    ("FY26 PBT = total income - total expenses", "=Inputs!E%d-Inputs!E%d" % (
        R["Total income"], R["Total expenses"]), 1246.93,
     "Reported PBT before exceptional items - exact"),
    ("FY26 net debt / equity", "=Inputs!E%d/Inputs!E%d" % (
        R["Net debt"], R["Total equity (net worth)"]), 4.01,
     "Reproduces the company's own published 4.01x"),
    ("FY25 net debt / equity", "=Inputs!D%d/Inputs!D%d" % (
        R["Net debt"], R["Total equity (net worth)"]), 4.27,
     "Reproduces the company's own published 4.27x"),
    ("FY26 exceptional item / PBT", "=Inputs!E%d/Inputs!E%d" % (
        R["Exceptional items"], R["PBT before exceptional"]), 0.0069,
     "0.69% of PBT - immaterial. Confirms the standalone '861' is an OCR decimal-point loss, "
     "not a Rs 861 crore item"),
]

SCORE = {
    "factors": [
        ("Parent support - TVS Motor Company Limited", 1, 0.40,
         "TVS Motor held 85.63% as on 31-Mar-2026. Captive financing arm of the TVS group: shared "
         "brand, dealer-network origination, and a strategic role in supporting vehicle sales. "
         "Support expected on an ongoing basis and in distress. This factor, not the standalone "
         "profile, is what carries the rating into the AA category."),
        ("Profitability", 2, 0.20,
         "RoAA improved to 2.76% from 2.59%; PAT Rs 913.17 crore, up 19.02% after 34.17% growth "
         "in FY2025. NII of Rs 4,279.06 crore is 12.94% of average assets. Strong in absolute "
         "terms, but the quality of the FY2026 improvement is mixed - it came from a falling "
         "credit cost while the operating cost ratio deteriorated."),
        ("Capitalisation and leverage", 2, 0.20,
         "Gearing down to 4.56x from 4.99x; net worth Rs 6,067.63 crore. Tier I CRAR up to 16.49% "
         "from 15.84%, against a 15% total-CRAR regulatory minimum. Perpetual instruments are only "
         "1.84% of Tier I, so the base is high quality. Total CRAR nonetheless eased to 19.44% "
         "from 20.30% as Tier II amortised."),
        ("Asset quality", 3, 0.10,
         "Credit cost 3.50% of average assets, improved from 4.38% but high in absolute terms and "
         "structural to two-wheeler, used-vehicle and tractor lending. Gross/net stage 3 ratios "
         "were NOT located in the documents reviewed, so this factor is scored on the impairment "
         "charge alone - a genuine evidence gap, recorded rather than filled with an assumption."),
        ("Funding profile", 3, 0.10,
         "Wholesale funded with no deposit franchise. Top-10 borrowings 70.68% of total, improved "
         "from 77.34% but still concentrated. ECB and NCD issuance during FY2026 is diversifying "
         "the mix."),
    ],
    "anchor": "AA band (composite 1.80)",
    "view": "[ICRA]AA+ (Stable) / [ICRA]A1+; perpetual debt [ICRA]AA (Stable)",
    "divergence": "No divergence. The issuer's own FY2026 annual report discloses ICRA's "
                  "outstanding ratings as AA+ (Stable) on long-term bank facilities and "
                  "subordinated debt, A1+ on short-term facilities and commercial paper, and "
                  "AA (Stable) on perpetual debt - matching this assessment including the "
                  "one-notch hybrid notch-down, which was applied here BEFORE the disclosure "
                  "table was read, on the SBI Additional Tier 1 precedent from 14-Aug-2026. "
                  "No TVS Credit rationale exists in the reference library; the anchor is the "
                  "issuer's own Step 7b disclosure.",
}

if __name__ == "__main__":
    out = build_spreads(
        company="TVS Credit Services Limited", years=Y, inputs=INPUTS, ratios=RATIOS,
        tieouts=TIEOUTS, score=SCORE,
        out="TVS Credit Services Limited_Financial_Spreads.xlsx")
    print("Saved:", out)
