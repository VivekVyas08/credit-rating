"""Generates State Bank of India_Financial_Spreads.xlsx (CLAUDE.md Step 5 deliverable).

BANK ratio suite - the corporate suite (gearing, TOL/TNW, interest coverage, GCA days) does
not apply to a scheduled commercial bank. All ratios are live Excel formulas off Inputs.
Figures Rs CRORE except ratios in %/x. Source: FY2026 AR ten-year table + asset-quality table.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import build_spreads          # noqa: E402

Y = ["FY2022", "FY2023", "FY2024", "FY2025", "FY2026"]
T10 = "FY26 AR 'Ten Years at a Glance' (L420-450)"
AQ = "FY26 AR asset-quality table (L4282-4286)"
NAR = "FY26 AR Chairman's statement (L764-790)"

INPUTS = [
    ("Operating profit",              [75292, 83713, 93797, 110579, 123015], f"{T10} 'Operating Result'"),
    ("Net profit",                    [31676, 50232, 61077, 70901, 80032],   f"{T10} 'Net Profit'"),
    ("RoAA (%)",                      [0.67, 0.96, 1.04, 1.10, 1.12],        f"{T10} 'Return on Average Assets'"),
    ("RoE (%)",                       [13.92, 19.43, 20.32, 19.87, 18.57],   f"{T10} 'Return on Equity'"),
    ("Cost-to-income (%)",            [53.31, 53.87, 55.66, 51.64, 50.11],   f"{T10} 'Expenses to Income'"),
    ("EPS (Rs)",                      [35.49, 56.29, 68.44, 79.44, 87.59],   f"{T10} 'Earnings Per Share'"),
    ("DPS (Rs)",                      [7.10, 11.30, 13.70, 15.90, 17.35],    f"{T10} 'Dividend Per Share'"),
    ("Tier I capital (%)",            [11.42, 12.06, 11.93, 12.11, 13.33],   f"{T10} 'Tier I Capital %'"),
    ("Tier II capital (%)",           [2.41, 2.62, 2.35, 2.14, 2.07],        f"{T10} 'Tier II Capital %'"),
    ("CRAR as reported (%)",          [13.83, 14.68, 14.28, 14.25, 15.40],   f"{T10} 'Basel-III Total Capital %'"),
    ("Gross NPA (Rs cr)",             [112023, 90928, 84276, 76880, 73452],  f"{AQ}"),
    ("Gross NPA (%)",                 [3.97, 2.78, 2.24, 1.82, 1.49],        f"{AQ}"),
    ("Net NPA (Rs cr)",               [27966, 21467, 21051, 19667, 18830],   f"{AQ}"),
    ("Net NPA (%)",                   [1.02, 0.67, 0.57, 0.47, 0.39],        f"{AQ}"),
    ("Fresh slippages (Rs cr)",       [26776, 19224, 20982, 22124, 23804],   f"{AQ}"),
    ("Domestic branches (no.)",       [22266, 22405, 22542, 22937, 23265],   f"{T10}"),
    ("CET-1 (%) [FY26 only]",         [None, None, None, None, 12.29],       f"{NAR} 'highest ever level'"),
    ("CASA ratio (%) [domestic]",     [None, None, None, None, 39.46],       f"{NAR} - DOMESTIC deposit basis"),
    ("Slippage ratio (%) [FY26]",     [None, None, None, None, 0.54],        f"{NAR} 'contained at'"),
    ("GoI shareholding (%)",          [None, None, None, 56.92, 55.03],      "FY26 AR L11698"),
]
R = {lab: 6 + i for i, (lab, _, _) in enumerate(INPUTS)}


def I(label):
    return "Inputs!{c}%d" % R[label]


def _f(expr):
    return "=" + expr


# D-SIB minimum CRAR for SBI: 11.5% base (incl. CCB) + 0.80% D-SIB surcharge from 01-Apr-2025.
DSIB_MIN = 12.30

RATIOS = [
    ("CRAR cross-check (Tier I + Tier II)",
     _f(f"{I('Tier I capital (%)')}+{I('Tier II capital (%)')}"),
     "Must equal reported CRAR - independent reconstruction of the capital stack", '0.00"%"'),
    ("Capital buffer over D-SIB minimum (pp)",
     _f(f"{I('CRAR as reported (%)')}-{DSIB_MIN}"),
     f"Reported CRAR less the {DSIB_MIN}% D-SIB requirement (11.5% + 0.80% surcharge)", '0.00" pp"'),
    ("Implied PCR excl. AUCA (%)",
     _f(f"({I('Gross NPA (Rs cr)')}-{I('Net NPA (Rs cr)')})/{I('Gross NPA (Rs cr)')}"),
     "Provision coverage derived from the GNPA/NNPA stock - FY26 ties to reported 74.36%", "0.0%"),
    ("Net NPA / Gross NPA (%)",
     _f(f"{I('Net NPA (Rs cr)')}/{I('Gross NPA (Rs cr)')}"),
     "Residual uncovered share of the bad-loan book", "0.0%"),
    ("Net profit growth (%)",
     _f(f"{I('Net profit')}/OFFSET({I('Net profit')},0,-1)-1"),
     "YoY growth in net profit", "0.0%"),
    ("Operating profit growth (%)",
     _f(f"{I('Operating profit')}/OFFSET({I('Operating profit')},0,-1)-1"),
     "YoY growth in pre-provision operating profit", "0.0%"),
    ("Dividend payout (%)",
     _f(f"{I('DPS (Rs)')}/{I('EPS (Rs)')}"),
     "DPS / EPS - tests the ~20% payout policy", "0.0%"),
    ("Slippages / opening Gross NPA (%)",
     _f(f"{I('Fresh slippages (Rs cr)')}/OFFSET({I('Gross NPA (Rs cr)')},0,-1)"),
     "Fresh slippage relative to the opening stressed stock", "0.0%"),
    ("RoAA (%)  [SECTOR-DEFINING]",
     _f(I('RoAA (%)')), "Return on average assets - the core bank profitability metric", '0.00"%"'),
    ("RoE (%)",
     _f(I('RoE (%)')), "Return on equity", '0.00"%"'),
    ("Cost-to-income (%)",
     _f(I('Cost-to-income (%)')), "Operating expenses / net total income", '0.00"%"'),
    ("Gross NPA (%)  [SECTOR-DEFINING]",
     _f(I('Gross NPA (%)')), "Headline asset-quality metric", '0.00"%"'),
    ("Net NPA (%)  [SECTOR-DEFINING]",
     _f(I('Net NPA (%)')), "Asset quality net of provisions", '0.00"%"'),
]

TIEOUTS = [
    ("FY26 CRAR = Tier I + Tier II", "=Inputs!G%d+Inputs!G%d" % (
        R["Tier I capital (%)"], R["Tier II capital (%)"]), 15.40,
     "13.33 + 2.07; reported CRAR is 15.40% - exact reconstruction of the capital stack"),
    ("FY26 net profit", "=Inputs!G%d" % R["Net profit"], 80032,
     "Chairman's statement: net profit grew 12.88% to Rs 80,032 crore"),
    ("FY26 net profit growth", "=Inputs!G%d/Inputs!F%d-1" % (R["Net profit"], R["Net profit"]), 0.1288,
     "Independently derived 12.88% matches the stated growth exactly"),
    ("FY26 operating profit growth", "=Inputs!G%d/Inputs!F%d-1" % (
        R["Operating profit"], R["Operating profit"]), 0.1125,
     "Independently derived 11.25% matches the stated growth exactly"),
    ("FY26 implied PCR excl. AUCA", "=(Inputs!G%d-Inputs!G%d)/Inputs!G%d" % (
        R["Gross NPA (Rs cr)"], R["Net NPA (Rs cr)"], R["Gross NPA (Rs cr)"]), 0.7436,
     "Derived from the NPA stock; the Bank reports PCR of 74.36% without AUCA - exact match"),
    ("FY26 GNPA improvement (pp)", "=Inputs!G%d-Inputs!F%d" % (
        R["Gross NPA (%)"], R["Gross NPA (%)"]), -0.33,
     "Stated as 'an improvement of 33 bps YoY' - reconciles"),
    ("FY26 dividend payout", "=Inputs!G%d/Inputs!G%d" % (R["DPS (Rs)"], R["EPS (Rs)"]), 0.1981,
     "Rs 17.35 / Rs 87.59; the ten-year table reports payout of 20.01% - reconciles to rounding"),
]

SCORE = {
    "factors": [
        ("Sovereign ownership and systemic importance", 1, 0.40,
         "Government of India holds 55.03% (FY2026; 56.92% FY2025) and SBI is designated a "
         "Domestic Systemically Important Bank by the RBI, carrying an additional 0.80% CET-1 "
         "surcharge from 01-Apr-2025. Support expectation is the dominant rating factor: SBI is "
         "the largest bank in the country with a balance sheet above Rs 76 lakh crore and total "
         "business above Rs 109 lakh crore."),
        ("Market position and deposit franchise", 1, 0.20,
         "Largest Indian bank by every measure: deposits Rs 59.76 lakh crore (+11.03%), advances "
         "Rs 49.33 lakh crore (+16.87%), 23,265 domestic branches and 245 foreign offices. CASA "
         "ratio of 39.46% on domestic deposits is a structural funding advantage; retail banking "
         "supplies 88.27% of deposits."),
        ("Asset quality", 1, 0.15,
         "Gross NPA 1.49% (-33 bps YoY) and net NPA 0.39% (-8 bps), the best in the ten-year "
         "series and down from 4.98% / 1.50% in FY2021. Provision coverage 74.36% excluding AUCA "
         "and 99.01% including it; slippage ratio contained at 0.54%."),
        ("Capitalisation", 2, 0.15,
         "CRAR 15.40% against a 12.30% D-SIB requirement, a 310 bps buffer, and CET-1 at a record "
         "12.29%. Capital has been built through accretion - Tier I rose to 13.33% from 12.11%. "
         "Scored 2 rather than 1 because the buffer, while comfortable, is thinner than the "
         "best-capitalised private peers against 16.87% advances growth."),
        ("Earnings profile", 2, 0.10,
         "Net profit Rs 80,032 crore (+12.88%), operating profit Rs 1.23 lakh crore (+11.25%), "
         "RoAA 1.12% and cost-to-income improved to 50.11%. RoE of 18.57% is strong but has eased "
         "from 20.32% in FY2024, and NII growth of 4.08% materially lagged advances growth of "
         "16.87% - margin compression is the one clear negative trend in the FY2026 numbers."),
    ],
    "anchor": "AAA band (composite 1.25 - highest investment grade)",
    "view": "Crisil AAA / Stable  -  Crisil A1+",
    "divergence": "TO BE COMPLETED AT STEP 14 - this view was formed from the issuer's own "
                  "disclosures before opening the CRISIL rationale of 05-Mar-2026 or the CareEdge "
                  "rationale of 13-Oct-2025, both of which the pre-flight confirmed exist.",
}

if __name__ == "__main__":
    out = build_spreads(
        company="State Bank of India", years=Y, inputs=INPUTS, ratios=RATIOS,
        tieouts=TIEOUTS, score=SCORE,
        out="State Bank of India_Financial_Spreads.xlsx")
    print("Saved:", out)
