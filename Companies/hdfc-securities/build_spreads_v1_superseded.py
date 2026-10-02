"""HDFC Securities Limited_Financial_Spreads.xlsx - CareEdge broking suite.

STANDALONE basis, Rs CRORE. Source figures are Rs LAKHS in the statements and Rs CRORE in the
highlights table; converted ONCE at extraction in compute_ratios.py.

THE LONG-TERM / SHORT-TERM SPLIT IS EVIDENCED, NOT ESTIMATED (failure mode 29).
The FY2026 contractual maturity table places EVERY rupee of borrowing in the "less than 1 year"
bucket: long-term debt is NIL. The rated instrument is therefore short-term only.

Sector-defining metrics for broking are average daily turnover and active clients, carried on
their own rows - NOT a lending-company or manufacturing metric set (failure mode 28).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import build_spreads          # noqa: E402

Y = ["FY2025", "FY2026"]
AR = "FY2026 annual report (04-08-2026)"

INPUTS = [
    # --- profitability, Rs crore as printed -------------------------------------------------
    ("Total income",                       [3264.8, 3110.2],   AR + " highlights L1092"),
    ("Total expenses (excl. depreciation)", [1699.1, 1790.3],  AR + " highlights"),
    ("Depreciation and amortisation",      [69.6, 82.8],       AR + " highlights"),
    ("Profit before tax",                  [1496.1, 1237.1],   AR + " highlights"),
    ("Tax expense",                        [371.1, 307.1],     AR + " highlights"),
    ("Profit after tax",                   [1125.0, 929.9],    AR + " highlights"),
    ("Dividend (interim + final)",         [898.3, 740.1],     AR + " appropriation table"),
    # --- DEBT by type. Lakhs / 100 -> crore --------------------------------------------------
    ("Commercial paper (amortised cost)",  [7677.51, 12827.38], AR + " borrowings note L4669"),
    ("Interest accrued on CP",             [64.01, 103.96],     AR + " borrowings note L4670"),
    ("Debt securities - total",            [7741.52, 12931.33], AR + " balance sheet L3049"),
    ("Borrowings other than debt secs (secured loan)",
                                           [202.25, 2182.55],   AR + " BS L3050, note L4695"),
    ("Lease liabilities",                  [85.63, 80.80],      AR + " balance sheet L3051"),
    ("TOTAL DEBT (borrowings incl. debt securities)",
                                           [7943.77, 15113.88], AR + " L6630"),
    ("LONG-TERM DEBT (maturity beyond 1 year)",
                                           [0.0, 0.0],
     AR + " maturity tables L6424-6434 (FY25) and L6405-6417 (FY26) - NIL in BOTH years. "
          "Every borrowing sits in the <1 year bucket in each table"),
    ("Total equity",                       [3348.59, 3595.92],  AR + " L6633"),
    # --- liquidity and ALM --------------------------------------------------------------------
    ("Cash and cash equivalents",          [830.98, 1783.98],   AR + " BS L3022"),
    ("Bank balances other than above",     [4862.46, 7838.73],  AR + " balance sheet L3023"),
    ("Loans (margin funding book)",        [5511.87, 7132.66],  AR + " BS L3026"),
    ("Investments",                        [1050.87, 2761.99],  AR + " BS L3027"),
    ("Financial assets due within 12 months", [12525.74, 18229.85],
     AR + " ALM tables L6822 (FY25) and L6768 (FY26)"),
    ("Financial liabilities - carrying amount", [10586.01, 18065.10],
     AR + " maturity tables L6435 (FY25) and L6417 (FY26)"),
    # --- sector-defining broking metrics -------------------------------------------------------
    # CORRECTED 20-Aug-2026: the first pass took these from the FY2024/FY2025 reports and had
    # the branch trend BACKWARDS. All four now come from the FY2026 report (failure mode 26).
    ("Average daily turnover (Rs trillion)", [1.6, 3.0],
     AR + " highlights - stated as risen 82%, Rs 1.6 Tr at 31-03-2025 to Rs 3 Tr at 31-03-2026"),
    ("Brokerage and fee income",            [None, 1516.0], AR + " highlights"),
    ("Branches (no.)",                      [134, 128],
     "FY2025 AR (134 across 106 cities at 31-03-2025) and " + AR + " (128 at 31-03-2026). "
     "FY2024 AR states 184 across 139 cities - the network is CONTRACTING"),
    ("Cities covered (no.)",                [106, 100],
     AR + ' states "more than 100 towns and cities" at 31-03-2026, against 106 at 31-03-2025 '
          "and 139 at 31-03-2024. 100 used as the stated floor"),
]
R = {lab: 6 + i for i, (lab, _, _) in enumerate(INPUTS)}


def I(lab):
    return "Inputs!{c}%d" % R[lab]


def f(e):
    return "=" + e


def growth(lab):
    """YoY growth. Only defined for the second year, so the FY2025 cell resolves to blank.
    OFFSET is avoided deliberately: it does not evaluate in the cache pass, and one column
    left of the first year column is the LABEL column, not a prior year."""
    r = R[lab]
    return '=IF({y}=1,Inputs!D%d/Inputs!C%d-1,"")' % (r, r)


RATIOS = [
    ("Gearing - total debt / equity (x)  [KEY]",
     f(I("TOTAL DEBT (borrowings incl. debt securities)") + "/" + I("Total equity")),
     "Total debt divided by total equity",
     "Rose 2.37x to 4.20x as debt grew 90% against 7% equity accretion. Elevated, but the "
     "liability funds a secured, self-liquidating margin book - read with the ALM rows below"),
    ("LONG-TERM debt as % of total debt  [NIL]",
     f(I("LONG-TERM DEBT (maturity beyond 1 year)") + "/"
       + I("TOTAL DEBT (borrowings incl. debt securities)")),
     "Long-term debt divided by total debt",
     "ZERO in both years - so funding is 100% SHORT-TERM. THE defining structural fact of this "
     "credit: both maturity tables place every borrowing inside 12 months, leaving the company "
     "wholly refinancing-dependent and making the ALM gap rows the decisive test"),
    ("PBILDT (income less cash operating expenses)",
     f(I("Total income") + "-" + I("Total expenses (excl. depreciation)")),
     "Total income less operating expenses before depreciation",
     "CareEdge earnings measure. Fell 15.7% to Rs 1,319.8 cr"),
    ("PBILDT margin (%)",
     f("(" + I("Total income") + "-" + I("Total expenses (excl. depreciation)") + ")/"
       + I("Total income")),
     "PBILDT divided by total income",
     "Contracted 550bps to 42.4% - costs rose 5.4% while income fell 4.7%"),
    ("PAT margin (%)",
     f(I("Profit after tax") + "/" + I("Total income")),
     "Profit after tax divided by total income",
     "34.5% to 29.9%. Still strong in absolute terms for the sector"),
    ("Return on equity (%)",
     f(I("Profit after tax") + "/" + I("Total equity")),
     "Profit after tax divided by total equity",
     "33.6% to 25.9%. Remains high; the fall is earnings-driven, not capital-driven"),
    ("Dividend payout (%)",
     f(I("Dividend (interim + final)") + "/" + I("Profit after tax")),
     "Dividend divided by profit after tax",
     "Held near 80% in BOTH years. Distributing four-fifths of a FALLING profit while debt "
     "doubled is why equity grew only 7% - a deliberate upstreaming to the parent"),
    ("Internal capital generation (%)",
     f("(" + I("Profit after tax") + "-" + I("Dividend (interim + final)") + ")/"
       + I("Total equity")),
     "Retained profit divided by total equity",
     "Only 5.3% retained in FY2026. High payout caps the equity base against a growing book"),
    ("Liquid assets (cash + bank balances)",
     f(I("Cash and cash equivalents") + "+" + I("Bank balances other than above")),
     "Cash and cash equivalents plus other bank balances",
     "Rs 9,622.71 cr at 31-03-2026 against CP of Rs 12,931.33 cr"),
    ("Liquid assets / commercial paper (x)",
     f("(" + I("Cash and cash equivalents") + "+" + I("Bank balances other than above") + ")/"
       + I("Debt securities - total")),
     "Cash and bank balances divided by outstanding CP",
     "FLAT at ~0.74x in both years - the company holds a consistent cash cover of roughly "
     "three-quarters of CP outstanding, and scaled liquidity with the borrowing. Cash alone "
     "still does not fully cover CP, so the ALM gap row below remains the decisive test"),
    ("ALM gap - assets <12m less total financial liabilities",
     f(I("Financial assets due within 12 months") + "-"
       + I("Financial liabilities - carrying amount")),
     "Financial assets maturing within 12 months less financial liabilities",
     "Positive in both years, but the cushion NARROWED 92% from Rs 1,939.73 cr to Rs 164.75 cr "
     "as debt grew 90% and assets did not keep pace. Still the structural mitigant to 100% "
     "short-term funding, but a materially thinner one than a year ago"),
    ("Margin funding book growth (%)",
     growth("Loans (margin funding book)"),
     "Year-on-year growth in the loan book",
     "Up 29.4% to Rs 7,132.66 cr. This, with investments up 163%, is WHERE the incremental debt "
     "went - asset growth, not loss funding"),
    ("Total income growth (%)",
     growth("Total income"),
     "Year-on-year growth in total income",
     "NEGATIVE 4.7% - the cyclical downturn in cash and derivative volumes"),
    ("PAT growth (%)",
     growth("Profit after tax"),
     "Year-on-year growth in profit after tax",
     "NEGATIVE 17.3%, falling faster than income through operating leverage"),
    ("Total debt growth (%)",
     growth("TOTAL DEBT (borrowings incl. debt securities)"),
     "Year-on-year growth in total debt",
     "POSITIVE 90.3% in the same year profit fell 17.3%. The central tension of this credit"),
    ("Branch network change (%)  [SECTOR]",
     growth("Branches (no.)"),
     "Year-on-year change in branch count",
     "NEGATIVE 4.5%: 134 to 128 branches, and 184 as recently as 31-03-2024 - a 30% reduction "
     "in two years. This is deliberate consolidation toward digital delivery, NOT expansion"),
    ("Average daily turnover growth (%)  [SECTOR]",
     growth("Average daily turnover (Rs trillion)"),
     "Year-on-year growth in average daily turnover",
     "The AR STATES +82%; the rounded endpoints (Rs 1.6 Tr to Rs 3 Tr) imply 87.5%, because "
     "the true FY2026 figure is about Rs 2.91 Tr rounded up to 3 in the highlights. Take the "
     "issuer's 82%. Either way, set it against total income DOWN 4.7%: volume is growing "
     "strongly and is NOT converting to revenue"),
    ("Revenue yield on turnover (income / ADTO)",
     f(I("Total income") + "/" + I("Average daily turnover (Rs trillion)")),
     "Total income divided by average daily turnover",
     "COLLAPSED from 2,040 to 1,037 - a 49% fall in revenue per unit of turnover, or 48% on "
     "the unrounded Rs 2.91 Tr. The clearest single measure of the yield compression in FY2026: "
     "derivative volumes carry far lower revenue per rupee traded than cash delivery"),
]
# number formats, positionally matched to RATIOS above
FMTS = ['0.00"x"', "0%", "#,##0.00", "0.00%", "0.00%", "0.00%", "0.0%", "0.00%",
        "#,##0.00", '0.00"x"', "#,##0.00", "0.0%", "0.0%", "0.0%", "0.0%",
        "0.0%", "0.0%", "#,##0"]
assert len(FMTS) == len(RATIOS), (len(FMTS), len(RATIOS))
# make_spreads writes ONE note column, so calculation and convention are joined into it
RATIOS = [(lab, formula, calc + " -- " + conv, FMTS[i])
          for i, (lab, formula, calc, conv) in enumerate(RATIOS)]

TIEOUTS = [
    ("FY26 debt securities = CP + interest accrued",
     "=Inputs!D%d+Inputs!D%d" % (R["Commercial paper (amortised cost)"],
                                 R["Interest accrued on CP"]), 12931.33,
     "12,827.38 + 103.96. Reconciles to the balance sheet figure of Rs 12,931.33 cr"),
    ("FY26 total debt = debt securities + secured loan",
     "=Inputs!D%d+Inputs!D%d" % (R["Debt securities - total"],
                                 R["Borrowings other than debt secs (secured loan)"]), 15113.88,
     "12,931.33 + 2,182.55 against the disclosed total of Rs 15,113.88 cr - exact"),
    ("FY26 LONG-TERM DEBT IS NIL",
     "=Inputs!D%d" % R["LONG-TERM DEBT (maturity beyond 1 year)"], 0.0,
     "The contractual maturity table shows nil in the 1-2 year, 2-3 year and beyond-3-year "
     "buckets for BOTH debt securities and other borrowings. The entire Rs 15,113.88 cr is "
     "short-term. This is the issuer's own disclosure, not an inference"),
    ("FY26 PAT = PBT less tax",
     "=Inputs!D%d-Inputs!D%d" % (R["Profit before tax"], R["Tax expense"]), 929.9,
     "1,237.1 - 307.1 = 930.0 against a printed 929.9. The 0.1 difference is SOURCE rounding - "
     "the highlights table is printed to one decimal in Rs crore and rounds each line "
     "independently. Figures are NOT adjusted to force a tie"),
    ("FY26 ALM gap is POSITIVE",
     "=Inputs!D%d-Inputs!D%d" % (R["Financial assets due within 12 months"],
                                 R["Financial liabilities - carrying amount"]), 164.75,
     "18,229.85 less 18,065.10. Assets inside 12 months exceed total financial liabilities - "
     "the answer to why 100% short-term funding is tolerable here"),
    ("DEBT DOUBLED WHILE PROFIT FELL",
     "=(Inputs!D%d/Inputs!C%d-1)*100" % (R["TOTAL DEBT (borrowings incl. debt securities)"],
                                         R["TOTAL DEBT (borrowings incl. debt securities)"]),
     90.26,
     "Debt +90.3% against PAT -17.3%. Flagged as a tie-out because it is the single most "
     "important movement in the file and must not be lost in the averages"),
]

SCORE = {
    "factors": [
        ("Parentage and group linkage", 1, 0.40,
         "HDFC Bank Limited holds 94.01% - near-wholly-owned, sharing the HDFC brand, and "
         "operating as the broking arm of the parent's retail franchise. Client acquisition, "
         "the three-in-one account and distribution all run through the bank. Under CareEdge's "
         "Notching by Factoring Linkages with Parent, this is a strategically important "
         "subsidiary of a highest-credit-quality parent, and the short-term rating draws "
         "directly on that. This factor dominates the assessment."),
        ("Liquidity and asset-liability management", 1, 0.20,
         "Financial assets maturing within 12 months of Rs 18,229.85 cr against total financial "
         "liabilities of Rs 18,065.10 cr - a POSITIVE gap of Rs 164.75 cr. Cash and bank "
         "balances of Rs 9,622.71 cr, and a margin funding book of Rs 7,132.66 cr secured "
         "against listed securities that self-liquidates. The funding is 100% short-term, but "
         "the asset side is short-dated to match."),
        # CORRECTED 20-Aug-2026 - this factor carried the year-misattributed metrics
        # (failure mode 30) and read the branch trend backwards.
        ("Market position and franchise", 2, 0.15,
         "Average daily turnover UP 82% to about Rs 3 trillion, derivative volumes up 83%, "
         "derivatives market share up 1.7x and retail equity delivery share retained. Over "
         "1 million customers access services digitally; brokerage and fee income Rs 1,516 cr, "
         "48.7% of total income. Against that, revenue per unit of turnover roughly HALVED and "
         "the branch network CONTRACTED 30% in two years (184 -> 134 -> 128), a deliberate "
         "shift to digital. Strong on volume and share, weak on converting either to revenue; "
         "competing against zero-brokerage discount platforms. A wholly-owned IFSC subsidiary "
         "extends the offering."),
        ("Profitability", 3, 0.15,
         "PAT Rs 929.9 cr on income of Rs 3,110.2 cr - a 29.9% net margin and 25.9% return on "
         "equity, strong in absolute terms. But BOTH fell: income -4.7%, PAT -17.3%, PBILDT "
         "margin down 550bps as costs rose 5.4% into falling revenue. The cyclical downturn in "
         "cash and derivative volumes is being felt, and operating leverage works both ways."),
        ("Capital structure and retention", 4, 0.10,
         "Gearing rose 2.37x to 4.20x as debt grew 90.3% to Rs 15,113.88 cr. Dividend payout "
         "held near 80% in both years, so internal capital generation was only 5.3% and equity "
         "grew just 7% against a book that grew far faster. Distributing four-fifths of a "
         "FALLING profit while leverage doubles is the weakest element of the file - though the "
         "upstreaming goes to the parent that also stands behind the credit."),
    ],
    "anchor": "A1+ band (composite 1.70 on the short-term scale)",
    "view": "CARE A1+ (short-term)",
    "divergence":
        "NO SAME-ISSUER RATIONALE EXISTS and none was assumed. The pre-flight search of the "
        "reference library returned HDFC Bank Limited (the PARENT, rated amount Rs 1,50,000 cr) "
        "and unrelated broking peers including Almondz - both flagged by the entity-confirmation "
        "guard as NOT importable to this issuer. The FY2026 annual report contains only two "
        "'credit rating' mentions, both generic references in the investment policy, and neither "
        "discloses a rating on this company's own instruments. The rated PROGRAMME SIZE is "
        "therefore genuinely not evidenced in any document held - which is stated openly rather "
        "than filled with a placeholder. What IS evidenced, and is reported in full, is the "
        "OUTSTANDING debt: Rs 12,931.33 cr of commercial paper and Rs 2,182.55 cr of secured "
        "borrowing, Rs 15,113.88 cr in total, 100% short-term, long-term debt NIL.",
}

if __name__ == "__main__":
    print("Saved:", build_spreads(
        company="HDFC Securities Limited", years=Y, inputs=INPUTS, ratios=RATIOS,
        tieouts=TIEOUTS, score=SCORE, basis="Standalone",
        out="HDFC Securities Limited_Financial_Spreads.xlsx"))
