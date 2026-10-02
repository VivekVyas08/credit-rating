"""Gujarat Energy Limited_Financial_Spreads.xlsx - CareEdge CGD suite.

TWO BASES, deliberately kept separate (failure mode 26):
  MERGED     - Q4 FY2026 press release, 30-May-2026. FY2025 comparative restated. Like-for-like.
  STANDALONE - FY2024-25 annual report, Gujarat Gas pre-scheme. Used ONLY for capital structure,
               which the press release does not disclose.
FY2025 total income differs by Rs 10,323 cr between the two - never combine them.

Sector-defining metric for CGD is SALES VOLUME in mmscmd, carried on its own rows.
Rs CRORE.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import build_spreads          # noqa: E402

Y = ["FY2024", "FY2025", "FY2026"]
PR = "Q4 FY2026 press release 30-May-2026 (MERGED basis)"
AR = "FY2024-25 annual report (Gujarat Gas STANDALONE, pre-scheme)"

INPUTS = [
    # --- merged basis: scale and profitability -------------------------------------------
    ("MERGED revenue from operations", [None, 27718, 24198], PR),
    ("MERGED EBITDA",                  [None, 3677, 3772],   PR),
    ("MERGED profit after tax",        [None, None, 2299],   PR),
    ("MERGED net worth",               [None, None, 18517],  PR + " - as on 31-03-2026"),
    ("MERGED EPS (Rs)",                [None, None, 24.50],  PR),
    # --- standalone basis: capital structure ---------------------------------------------
    ("STANDALONE revenue from ops",    [16292.97, 17184.97, None], AR + " P&L"),
    ("STANDALONE other income",        [107.75, 209.97, None],     AR + " P&L"),
    ("STANDALONE excise duty",         [602.78, 698.02, None],     AR + " - an EXPENSE line"),
    ("STANDALONE finance costs",       [29.31, 32.49, None],       AR + " P&L"),
    ("STANDALONE depreciation",        [474.30, 510.64, None],     AR + " P&L"),
    ("STANDALONE profit before tax",   [1536.21, 1546.60, None],   AR + " P&L"),
    ("STANDALONE profit after tax",    [1142.77, 1145.51, None],   AR + " P&L"),
    ("STANDALONE borrowings",          [0.0, 0.0, None],           AR + " BS - NIL both years"),
    ("STANDALONE lease liabilities",   [117.77, 115.16, None],     AR + " BS"),
    ("STANDALONE cash + bank",         [926.12, 359.40, None],     AR + " BS"),
    ("STANDALONE total equity",        [7689.26, 8453.65, None],   AR + " BS"),
    ("STANDALONE total assets",        [11658.35, 12615.12, None], AR + " BS"),
    # --- sector-defining metric ------------------------------------------------------------
    ("VOLUME CGD segment (mmscmd)",    [None, None, 8.69],   PR),
    ("VOLUME gas trading (mmscmd)",    [None, None, 4.94],   PR),
    ("VOLUME CNG (mmscmd)",            [None, None, 3.43],   PR),
    ("CNG stations (no.)",             [None, None, 839],    PR),
    ("PNG households (lakh)",          [None, None, 24.18],  PR),
]
R = {lab: 6 + i for i, (lab, _, _) in enumerate(INPUTS)}


def I(lab):
    return "Inputs!{c}%d" % R[lab]


def f(e):
    return "=" + e


RATIOS = [
    ("MERGED EBITDA margin (%)",
     f(I("MERGED EBITDA") + "/" + I("MERGED revenue from operations")),
     "Expanded 232bps as low-margin gas TRADING revenue shrank - a mix effect, not pricing",
     "0.00%"),
    ("MERGED revenue growth (%)",
     f(I("MERGED revenue from operations") + "/OFFSET("
       + I("MERGED revenue from operations") + ",0,-1)-1"),
     "FELL 12.7% - but EBITDA rose. Read with the margin row above", "0.0%"),
    ("MERGED EBITDA growth (%)",
     f(I("MERGED EBITDA") + "/OFFSET(" + I("MERGED EBITDA") + ",0,-1)-1"),
     "Rose 2.6% on 12.7% lower revenue", "0.0%"),
    ("STANDALONE PBILDT",
     f(I("STANDALONE profit before tax") + "+" + I("STANDALONE finance costs") + "+"
       + I("STANDALONE depreciation") + "-" + I("STANDALONE other income")),
     "CareEdge earnings measure on the standalone basis", "#,##0.00"),
    ("STANDALONE adjusted debt (leases only)",
     f(I("STANDALONE borrowings") + "+" + I("STANDALONE lease liabilities")),
     "Borrowings are NIL - adjusted debt is lease liabilities alone", "#,##0.00"),
    ("STANDALONE net cash",
     f(I("STANDALONE cash + bank") + "-" + I("STANDALONE borrowings") + "-"
       + I("STANDALONE lease liabilities")),
     "POSITIVE = net cash. The dominant rating consideration", "#,##0.00"),
    ("STANDALONE overall gearing (x)  [KEY]",
     f("(" + I("STANDALONE borrowings") + "+" + I("STANDALONE lease liabilities") + ")/"
       + I("STANDALONE total equity")),
     "0.014x. No leverage threshold is remotely in play", '0.000"x"'),
    ("STANDALONE interest coverage (x)",
     f("(" + I("STANDALONE profit before tax") + "+" + I("STANDALONE finance costs") + "+"
       + I("STANDALONE depreciation") + "-" + I("STANDALONE other income") + ")/"
       + I("STANDALONE finance costs")),
     "57.9x FY2025, 65.9x FY2024", '0.0"x"'),
    ("STANDALONE TOL / TNW (x)",
     f("(" + I("STANDALONE total assets") + "-" + I("STANDALONE total equity") + ")/"
       + I("STANDALONE total equity")),
     "Total outside liabilities to net worth", '0.00"x"'),
    ("STANDALONE revenue net of excise",
     f(I("STANDALONE revenue from ops") + "-" + I("STANDALONE excise duty")),
     "Excise is an expense line, so reported revenue is GROSS of excise", "#,##0.00"),
    ("VOLUME total (mmscmd)  [SECTOR-DEFINING]",
     f(I("VOLUME CGD segment (mmscmd)") + "+" + I("VOLUME gas trading (mmscmd)")),
     "CGD 8.69 + trading 4.94 = 13.63, matching the published total", '0.00" mmscmd"'),
    ("VOLUME CNG share of CGD (%)",
     f(I("VOLUME CNG (mmscmd)") + "/" + I("VOLUME CGD segment (mmscmd)")),
     "CNG is the fastest-growing CGD category, +12% YoY to a record 3.60 mmscmd in Q4", "0.0%"),
]

TIEOUTS = [
    ("FY25 standalone total income", "=Inputs!E%d+Inputs!E%d" % (
        R["STANDALONE revenue from ops"], R["STANDALONE other income"]), 17394.94,
     "Reported total income - exact"),
    ("FY25 standalone borrowings are NIL", "=Inputs!E%d" % R["STANDALONE borrowings"], 0.0,
     "Nil in both FY2024 and FY2025 - the defining fact of this credit"),
    ("FY25 standalone net cash is POSITIVE", "=Inputs!E%d-Inputs!E%d-Inputs!E%d" % (
        R["STANDALONE cash + bank"], R["STANDALONE borrowings"],
        R["STANDALONE lease liabilities"]), 244.24,
     "Cash 359.40 less lease liabilities 115.16 - the company is in net cash"),
    ("FY26 volumes reconcile", "=Inputs!F%d+Inputs!F%d" % (
        R["VOLUME CGD segment (mmscmd)"], R["VOLUME gas trading (mmscmd)"]), 13.63,
     "8.69 + 4.94 against the published total of 13.63 mmscmd"),
    ("BASIS GAP: merged FY25 vs standalone FY25", "=Inputs!E%d-(Inputs!E%d+Inputs!E%d)" % (
        R["MERGED revenue from operations"], R["STANDALONE revenue from ops"],
        R["STANDALONE other income"]), 10323.06,
     "Rs 10,323 cr - the incoming trading/E&P/wind businesses. PROOF the two bases differ and "
     "must never be spliced into one series"),
]

SCORE = {
    "factors": [
        ("Capital structure", 1, 0.35,
         "BORROWINGS ARE NIL in FY2024 and FY2025. Adjusted debt is lease liabilities of "
         "Rs 115.16 cr against equity of Rs 8,453.65 cr - gearing 0.014x - and the company is in "
         "net cash of Rs 244.24 cr with interest coverage of 57.9x. Net worth grew entirely "
         "through accrual. This is the dominant rating consideration."),
        ("Market position", 1, 0.25,
         "India's largest city gas distribution company. FY2026 CGD volume 8.69 mmscmd, total "
         "13.63 mmscmd including trading. 839 CNG stations and 24.18 lakh PNG households give the "
         "position durability; CNG volume hit a record 3.60 mmscmd in Q4, +12% YoY."),
        ("Ownership and group linkage", 1, 0.20,
         "Gujarat state government company (CIN ...SGC...), IAS officers as Chairman and Managing "
         "Director, within the GSPC group. All three rating agencies hold the issuer at the "
         "highest long-term grade per the issuer's own disclosure."),
        ("Profitability and volume growth", 2, 0.10,
         "Merged-basis EBITDA Rs 3,772 cr, margin expanding 232bps to 15.59% as low-margin gas "
         "trading contracted. PAT Rs 2,299 cr, EPS Rs 24.50, highest-ever dividend recommended. "
         "Morbi cluster consumption grew from 0.36 to 7.8 MMSCMD."),
        ("Sector and structural risk", 3, 0.10,
         "Gas price and availability volatility with lagged pass-through; PNGRB tariff regulation; "
         "and the composite scheme effective 01-May-2026, AFTER the balance-sheet date, so the "
         "merged-entity capital structure and residual post-demerger obligations are not yet "
         "evidenced. That is the principal open question in this assessment."),
    ],
    "anchor": "AAA band (composite 1.35)",
    "view": "CARE AAA; Stable / CARE A1+",
    "divergence": "No divergence. The issuer's FY2024-25 annual report discloses CARE AAA; Stable / "
                  "CARE A1+ (09-09-2024), IND AAA/Stable / IND A1+ and CRISIL AAA/Stable - all "
                  "three agencies at the highest long-term grade, and the FY2022-23 report records "
                  "an upgrade TO AAA/Stable. A CareEdge rationale for Gujarat Gas Limited "
                  "(29-Sep-2025) exists in the reference library and was NOT opened before this "
                  "view was formed; the view rests on the debt-free balance sheet and the "
                  "issuer's own Step 7b disclosure.",
}

if __name__ == "__main__":
    print("Saved:", build_spreads(
        company="Gujarat Energy Limited", years=Y, inputs=INPUTS, ratios=RATIOS,
        tieouts=TIEOUTS, score=SCORE,
        out="Gujarat Energy Limited_Financial_Spreads.xlsx"))
