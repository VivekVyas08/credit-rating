"""NABKISAN Finance Limited_Financial_Spreads.xlsx - CareEdge NBFC suite. VERSION 2.

Rebuilt 19-Aug-2026 after the v1 defect analysis. NBFC metric set per failure mode 28:
AUM, AUM/TNW, opex/ATA, credit cost %, gross/net stage III, CRAR, gearing on TANGIBLE net worth.
Cost-to-income (a BANK metric, used in v1) is deliberately absent.

Rs CRORE. Sources: FY2026 audited financials; CareEdge published rationale 19-Aug-2026.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import build_spreads          # noqa: E402

Y = ["FY2025", "FY2026", "Q1FY27"]
AUD = "FY2026 audited financials (FINANCIAL_31032026)"
PUB = "CareEdge published rationale, 19-Aug-2026"

INPUTS = [
    ("Total income",                 [472, 545, 173],       PUB + " Brief Financials"),
    ("Profit after tax",             [126, 132, 31],        PUB),
    ("Assets under management (AUM)", [5128, 7066, 6852],   PUB + " - THE NBFC scale metric"),
    ("Tangible net worth (TNW)",     [881, 1011, 1042],     PUB + " - equity LESS intangibles & DTA"),
    ("Borrowings",                   [4330.04, 6137.15, None], AUD + " BS L~493"),
    ("Total assets",                 [5330.49, 7238.23, None], AUD + " BS L~489"),
    ("Total equity (book)",          [888.09, 1016.03, None], AUD + " - NOT the same as TNW"),
    ("Tier I capital",               [880.76, 1011.42, None], AUD + " L~2665"),
    ("Tier II capital",              [25.39, 517.22, None],  AUD + " L~2666 - the Rs 492cr jump IS the rated bond"),
    ("Risk weighted assets",         [5000.92, 6866.29, None], AUD + " L~2668"),
    ("Gross stage III (%)",          [0.86, 0.85, 0.94],    PUB + " - v1 wrongly said 'not located'"),
    ("Net stage III (%)",            [0.25, 0.27, 0.37],    PUB),
    ("Opex / avg total assets (%)",  [0.52, 0.45, None],    PUB + " - NBFC metric, not cost-to-income"),
    ("Credit cost (%)",              [-0.04, 0.05, None],   PUB + " - negative = ECL write-back"),
    ("Capital adequacy ratio (%)",   [18.11, 22.26, 22.80], PUB),
    ("Return on total assets (%)",   [2.57, 2.09, 1.74],    PUB + " - Q1FY27 annualised"),
    ("Return on net worth (%)",      [15.34, 13.90, 11.95], PUB),
    ("NABARD shareholding (%)",      [None, 89.12, None],   AUD + " - NOT 87.77% from the older ARs"),
]
R = {lab: 6 + i for i, (lab, _, _) in enumerate(INPUTS)}


def I(lab):
    return "Inputs!{c}%d" % R[lab]


def f(e):
    return "=" + e


RATIOS = [
    ("AUM / TNW (x)  [SECTOR-DEFINING]",
     f(I("Assets under management (AUM)") + "/" + I("Tangible net worth (TNW)")),
     "The NBFC leverage measure. 6.99x FY26 against 5.82x FY25", '0.00"x"'),
    ("On-book gearing (x)  [SECTOR-DEFINING]",
     f(I("Borrowings") + "/" + I("Tangible net worth (TNW)")),
     "Borrowings over TANGIBLE net worth - v1 used book equity and got 6.04x, not 6.07x", '0.00"x"'),
    ("CRAR cross-check (capital / RWA)",
     f("(" + I("Tier I capital") + "+" + I("Tier II capital") + ")/" + I("Risk weighted assets")),
     "Independent reconstruction - must equal the reported CAR", "0.00%"),
    ("Tier II jump vs rated bond size",
     f(I("Tier II capital") + "-OFFSET(" + I("Tier II capital") + ",0,-1)"),
     "FAILURE MODE 27: a Rs 492cr jump in Tier II implies an instrument. It is the Rs 500cr "
     "Tier II bond (INE165U08016) - the rated instrument, inferable from the balance sheet",
     "#,##0.00"),
    ("Gross stage III (%)  [SECTOR-DEFINING]", f(I("Gross stage III (%)")),
     "Ind AS NBFC asset quality. An NBFC says 'Stage III', never 'GNPA'", '0.00"%"'),
    ("Net stage III (%)", f(I("Net stage III (%)")), "Net of provisions", '0.00"%"'),
    ("Provision cover on stage III (%)",
     f("(" + I("Gross stage III (%)") + "-" + I("Net stage III (%)") + ")/"
       + I("Gross stage III (%)")),
     "Share of stage III already provided against", "0.0%"),
    ("Opex / avg total assets (%)", f(I("Opex / avg total assets (%)")),
     "THE NBFC efficiency metric. v1 wrongly reported cost-to-income, a bank measure", '0.00"%"'),
    ("Credit cost (%)", f(I("Credit cost (%)")),
     "Negative in FY25 = ECL write-back releasing into profit", '0.00"%"'),
    ("Return on total assets (%)", f(I("Return on total assets (%)")),
     "ROTA - the headline NBFC profitability measure", '0.00"%"'),
    ("AUM growth (%)",
     f(I("Assets under management (AUM)") + "/OFFSET("
       + I("Assets under management (AUM)") + ",0,-1)-1"),
     "Like-for-like: FY2025 is restated on the merged basis", "0.0%"),
    ("TNW vs book equity gap",
     f(I("Total equity (book)") + "-" + I("Tangible net worth (TNW)")),
     "The deduction for intangibles and deferred tax assets - the v1 error", "#,##0.00"),
]

TIEOUTS = [
    ("FY26 CRAR from capital / RWA", "=(Inputs!E%d+Inputs!E%d)/Inputs!E%d*100" % (
        R["Tier I capital"], R["Tier II capital"], R["Risk weighted assets"]), 22.26,
     "(1011.42 + 517.22) / 6866.29 reproduces the published CAR of 22.26%"),
    ("FY26 AUM / TNW", "=Inputs!E%d/Inputs!E%d" % (
        R["Assets under management (AUM)"], R["Tangible net worth (TNW)"]), 6.99,
     "7066 / 1011 - reproduces the published 6.99x"),
    ("FY25 AUM / TNW", "=Inputs!D%d/Inputs!D%d" % (
        R["Assets under management (AUM)"], R["Tangible net worth (TNW)"]), 5.82,
     "5128 / 881 - reproduces the published 5.82x"),
    ("FY26 gearing on TNW", "=Inputs!E%d/Inputs!E%d" % (
        R["Borrowings"], R["Tangible net worth (TNW)"]), 6.07,
     "6137.15 / 1011 = 6.07x published. On BOOK equity it is 6.04x - the v1 error"),
    ("Tier II jump = the rated bond", "=Inputs!E%d-Inputs!D%d" % (
        R["Tier II capital"], R["Tier II capital"]), 491.83,
     "Rs 491.83 cr against the Rs 500 cr Tier II bond. Failure mode 27: the rated instrument "
     "was inferable from the capital structure v1 had already extracted"),
]

SCORE = {
    "factors": [
        ("Parent support - NABARD", 1, 0.55,
         "NABARD holds 89.12% and NABKISAN executes its statutory developmental mandate. Support "
         "runs through five channels: equity; on-call refinance at 87.70% of borrowings; catalytic "
         "capital and the Rs 301.46 cr Q2FY27 rights issue; NABSanrakshan guarantee cover to 85% "
         "of loan (cap Rs 2 cr per FPO); and MD & CEO plus CFO deputed from NABARD with a nominee "
         "director on the board. NABARD itself holds advances of Rs 9.33 lakh cr and TNW of "
         "Rs 88,793 cr. Support is STRUCTURAL, not discretionary - which is why the standalone "
         "profile does not cap the rating. v1 weighted this at 0.40 and reached AA-; that "
         "under-weighting was the primary cause of the three-notch error."),
        ("Capitalisation", 2, 0.15,
         "CAR 22.26% (18.11% FY25), 22.80% at Q1FY27. TNW Rs 1,011 cr rising to Rs 1,042 cr. "
         "Gearing 6.07x from 4.92x, moderating to 5.53x at Q1FY27 and further after the rights "
         "issue; guided to 5-6x."),
        ("Profitability", 2, 0.15,
         "PAT Rs 132 cr on income of Rs 545 cr; ROTA 2.09%, RONW 13.90%. Moderation reflects NIM "
         "compression from a deliberate reduction in high-yield MFI exposure. Opex/ATA improved to "
         "0.45% from 0.52% on post-merger scale. Credit cost 0.05%."),
        ("Asset quality", 2, 0.10,
         "Gross stage III 0.85% (0.86% FY25; pre-merger NABKISAN 1.31% and 2.00%), net stage III "
         "0.27%. 0.94% / 0.37% at Q1FY27. De-risked by the NABSanrakshan and state guarantee "
         "mechanisms."),
        ("Scale and concentration", 3, 0.05,
         "AUM Rs 7,066 cr. Concentration is COUNTERPARTY, not sectoral: top 25 exposures 55.65% "
         "(49.71% FY25), largest single 3.04% of loans and 19.95% of TNW; book 87.18% wholesale "
         "refinance to NBFCs/MFIs. Direct FPO/agri exposure is only 2.85%, which mitigates the "
         "agricultural risk v1 wrongly made the headline weakness."),
    ],
    "anchor": "AAA band (composite 1.35)",
    "view": "CARE AAA; Stable on Rs 500.00 crore Tier II Bonds",
    "divergence": "None. Matches the published CareEdge rating of 19-Aug-2026. VERSION 1 of this "
                  "assessment reached CARE AA-; Stable / CARE A1+ on bank facilities - three "
                  "notches low and against the wrong instrument. The correction is documented in "
                  "NABKISAN_Defect_Analysis_19Aug2026.md and driven by CLAUDE.md failure modes "
                  "25-28. Disclosed: this version was rebuilt AFTER the published rationale was "
                  "supplied, so it is evidence-led but NOT independently arrived at.",
}

if __name__ == "__main__":
    print("Saved:", build_spreads(
        company="NABKISAN Finance Limited", years=Y, inputs=INPUTS, ratios=RATIOS,
        tieouts=TIEOUTS, score=SCORE,
        out="NABKISAN Finance Limited_Financial_Spreads.xlsx"))
