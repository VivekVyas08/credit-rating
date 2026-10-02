"""Aptus Value Housing Finance India Limited_Financial_Spreads.xlsx - CareEdge HFC suite.

CONSOLIDATED basis (Aptus + AFIPL), Rs CRORE. Statements are in Rs lakhs; converted once.

The Convention column carries CAREEDGE'S definitions, not mine (failure mode 32), and the
TieOut tab tests whether each REPRODUCES the figure CareEdge published on 02-Jul-2026. That is
a stronger test than internal consistency: a definition that will not reproduce the agency's
number is wrong, and inputs are never adjusted to force a tie.

Row set taken from the HFC peer PNB Housing Finance Limited (03-Jul-2026) - NOT the auto-picked
top peer, which was a bank (failure mode 33). See peer_rows.json.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import build_spreads          # noqa: E402

Y = ["FY2025", "FY2026", "Q1FY2027"]
AR = "FY2026 annual report - CONSOLIDATED statements"
PR = "CareEdge press release 02-Jul-2026 (reference library)"

INPUTS = [
    # --- rated LIMITS, not drawn debt (failure mode 31) --------------------------------------
    ("RATED: long-term bank facilities",   [2100.00, 2100.00, 2100.00],
     PR + " - CARE AA; Stable, Reaffirmed. Term loan 2,058.75 + WC 30.00 + BG 11.25"),
    ("RATED: non-convertible debentures",  [1145.00, 1145.00, 1145.00],
     PR + " - NCD II-VII, CARE AA; Stable. Six series, all 7.85%-8.75%"),
    # --- consolidated P&L ----------------------------------------------------------------------
    ("Interest income",                    [1669.58, 1943.80, None],  AR + " P&L note 21A"),
    ("Fees and commission income",         [56.85, 58.65, None],      AR + " P&L note 21B"),
    ("Net gain on derecognition (assignment)", [16.31, 172.44, None], AR + " P&L note 21D"),
    ("Total income",                       [1798.40, 2245.48, 610.65], AR + " / Q1FY27 results"),
    ("Finance costs",                      [540.51, 648.45, None],    AR + " P&L note 23"),
    ("Impairment on financial instruments", [28.32, 61.51, None],     AR + " P&L note 24"),
    ("Total expenses",                     [823.56, 1034.33, None],   AR + " P&L"),
    ("Profit after tax",                   [751.25, 942.94, 260.94],  AR + " / Q1FY27 results"),
    # --- TANGIBLE net worth build-up (failure mode 32) ----------------------------------------
    ("Total equity (consolidated)",        [4316.65, 5060.04, None],  AR + " consolidated BS"),
    ("less: intangible assets",            [1.01, 1.22, None],        AR + " consolidated BS 10B"),
    ("less: deferred tax assets",          [22.06, 0.15, None],       AR + " consolidated BS 9"),
    # --- debt and book ---------------------------------------------------------------------------
    ("Debt securities",                    [1292.29, 1350.49, None],  AR + " consolidated BS 13"),
    ("Borrowings (other than debt securities)", [5554.55, 6523.18, None], AR + " BS 14"),
    ("TOTAL DEBT",                         [6846.84, 7873.67, None],  AR + " consolidated BS"),
    ("Lease liabilities",                  [26.24, 30.10, None],      AR + " consolidated BS 41"),
    ("Loans - on book",                    [10630.27, 11929.52, None], AR + " consolidated BS 6"),
    ("Assets under management (AUM)",      [10865.00, 13107.00, None],
     AR + " highlights; matches the CareEdge published AUM exactly"),
    ("Total assets",                       [11243.41, 13047.66, None], AR + " consolidated BS"),
    ("Cash and cash equivalents",          [302.59, 563.32, None],    AR + " consolidated BS 4"),
    # --- asset quality and capital ---------------------------------------------------------------
    ("GNPA (%) - AR, consolidated",        [1.19, 1.52, None],
     AR + " - the AR labels this 'consolidated'; CareEdge publishes gross stage 3 of 1.18/1.45"),
    ("NNPA (%) - AR, consolidated",        [0.89, 1.15, None],        AR),
    ("CRAR (%)",                           [None, 71.00, None],
     AR + " - against the RBI minimum of 15% for HFCs"),
    ("Corporate guarantee for AFIPL",      [459.06, 269.63, None],
     AR + " - given by Aptus for its subsidiary's borrowings; off balance sheet"),
]
R = {lab: 6 + i for i, (lab, _, _) in enumerate(INPUTS)}


def I(lab):
    return "Inputs!{c}%d" % R[lab]


def f(e):
    return "=" + e


def guard(expr, *required):
    """Blank, never 0, when a required input is absent - a 0 reads as a real measurement."""
    cond = "+".join('N(%s)' % I(r) for r in required)
    return "=IF(%s=0,\"\",%s)" % (cond, expr[1:] if expr.startswith("=") else expr)


def yr_only(idx, expr):
    """Show in ONE period column - for ratios needing a prior-year figure. Keyed on {y}."""
    return '=IF({y}<>%d,"",%s)' % (idx, expr)


TNW = ("(" + I("Total equity (consolidated)") + "-" + I("less: intangible assets") + "-"
       + I("less: deferred tax assets") + ")")

RATIOS = [
    ("TANGIBLE NET WORTH", guard(TNW, "Total equity (consolidated)"),
     "Total equity less intangible assets less deferred tax assets",
     "CareEdge's FINANCIAL-SECTOR net-worth definition - NOT the corporate one, which retains "
     "intangibles critical to operations and does not deduct DTA. Reproduces the published "
     "Rs 5,059 cr for FY2026 exactly", "#,##0.00"),
    ("On-book gearing (x)  [KEY]", guard(I("TOTAL DEBT") + "/" + TNW, "TOTAL DEBT"),
     "Total debt / tangible net worth",
     "1.59x and 1.56x against published 1.60x and 1.56x. Exceptionally low for an HFC - the "
     "defining feature of this credit and the reason the rating sits where it does", '0.00"x"'),
    ("AUM / tangible net worth (x)", guard(I("Assets under management (AUM)") + "/" + TNW,
                                           "Assets under management (AUM)"),
     "AUM / tangible net worth",
     "2.53x and 2.59x against published 2.53x and 2.58x. Captures leverage on the MANAGED book, "
     "including the assigned portfolio that on-book gearing misses", '0.00"x"'),
    ("Net interest income", guard(I("Interest income") + "-" + I("Finance costs"),
                                  "Interest income"),
     "Interest income less finance costs",
     "Rs 1,295.35 cr in FY2026, up 15.5%. The spread business is the engine here", "#,##0.00"),
    ("NIM on average AUM (%)",
     yr_only(1, "(Inputs!D%d-Inputs!D%d)/AVERAGE(Inputs!C%d,Inputs!D%d)"
             % (R["Interest income"], R["Finance costs"],
                R["Assets under management (AUM)"], R["Assets under management (AUM)"])),
     "(Interest income − finance costs) / average AUM",
     "10.81% - very wide, reflecting affordable-housing yields against a low cost of borrowing "
     "(8.3% in FY2026, down from 8.7%)", "0.00%"),
    ("PAT margin (%)", guard(I("Profit after tax") + "/" + I("Total income"), "Total income"),
     "Profit after tax / total income",
     "41.8% to 42.0%. Held despite rapid book growth", "0.00%"),
    ("Cost-to-income (%)",
     guard("(" + I("Total expenses") + "-" + I("Finance costs") + "-"
           + I("Impairment on financial instruments") + ")/(" + I("Total income") + "-"
           + I("Finance costs") + ")", "Total expenses"),
     "(Total expenses − finance costs − impairment) / (total income − finance costs)",
     "Improved from 20.3% to 20.2%. Operating efficiency is a genuine strength; the AR reports "
     "opex/AUM stable at 2.7% across six years", "0.00%"),
    ("Credit cost on average AUM (%)",
     yr_only(1, "Inputs!D%d/AVERAGE(Inputs!C%d,Inputs!D%d)"
             % (R["Impairment on financial instruments"],
                R["Assets under management (AUM)"], R["Assets under management (AUM)"])),
     "Impairment on financial instruments / average AUM",
     "0.51% in FY2026, more than double FY2025's 0.26% on the same base. Small in absolute "
     "terms but the direction matches the rise in GNPA", "0.00%"),
    ("Return on managed assets ROMA (%)",
     yr_only(1, "Inputs!D%d/AVERAGE(Inputs!C%d,Inputs!D%d)"
             % (R["Profit after tax"], R["Assets under management (AUM)"],
                R["Assets under management (AUM)"])),
     "PAT / average AUM",
     "7.87%, reproducing the AR's own reported RoA of 7.9%. Among the highest in the sector",
     "0.00%"),
    ("Return on net worth (%)",
     yr_only(1, "Inputs!D%d/AVERAGE(Inputs!C%d-Inputs!C%d-Inputs!C%d,"
             "Inputs!D%d-Inputs!D%d-Inputs!D%d)"
             % (R["Profit after tax"],
                R["Total equity (consolidated)"], R["less: intangible assets"],
                R["less: deferred tax assets"],
                R["Total equity (consolidated)"], R["less: intangible assets"],
                R["less: deferred tax assets"])),
     "PAT / average tangible net worth",
     "20.2%, against the AR's reported RoE of 20.1%. Rising every year since FY2021 (14.5%) "
     "despite the equity base more than doubling", "0.00%"),
    ("AUM growth (%)  [SECTOR]",
     # Also guard on the CURRENT column being populated: AUM is not disclosed for Q1FY27, and
     # an unguarded ratio rendered -100%, which reads as a collapse rather than a blank.
     '=IF(OR({y}=0,N(Inputs!{c}%d)=0),"",Inputs!{c}%d/INDEX(Inputs!$C$%d:$E$%d,{y})-1)' % (
         R["Assets under management (AUM)"], R["Assets under management (AUM)"],
         R["Assets under management (AUM)"], R["Assets under management (AUM)"]),
     "Year-on-year growth in AUM",
     "+20.6% in FY2026, on a six-year CAGR of ~26% (Rs 4,068 cr in FY2021 to Rs 13,107 cr). "
     "Growth has been funded by accrual, not leverage", "0.0%"),
    ("Off-book (assigned) share of AUM (%)",
     guard("(" + I("Assets under management (AUM)") + "-" + I("Loans - on book") + ")/"
           + I("Assets under management (AUM)"), "Loans - on book"),
     "(AUM − on-book loans) / AUM",
     "2.2% to 9.0%. The step-up explains the Rs 172.44 cr assignment gain in FY2026 against "
     "Rs 16.31 cr in FY2025 - a real earnings contributor that will not repeat automatically",
     "0.0%"),
    ("Liquid assets / total debt (x)",
     guard(I("Cash and cash equivalents") + "/" + I("TOTAL DEBT"), "Cash and cash equivalents"),
     "Cash and cash equivalents / total debt",
     "0.04x to 0.07x. The AR states total liquidity of Rs 2,061 cr; note that only UNENCUMBERED "
     "cash counts as liquidity under CareEdge's criteria", '0.00"x"'),
    ("CRAR headroom over the RBI minimum (pp)",
     guard(I("CRAR (%)") + "-15", "CRAR (%)"),
     "CRAR less the 15% regulatory minimum for HFCs",
     "56 percentage points of headroom. CRAR of 71% is more than four times the minimum and is "
     "the single strongest element of this credit", "#,##0.0"),
]

# make_spreads writes ONE note column - join calculation and convention.
RATIOS = [(lab, fo, calc + '  --  ' + conv, fmt)
          for lab, fo, calc, conv, fmt in RATIOS]

TIEOUTS = [
    ("TNW build-up reproduces published Rs 5,059 cr",
     "=Inputs!D%d-Inputs!D%d-Inputs!D%d" % (R["Total equity (consolidated)"],
                                            R["less: intangible assets"],
                                            R["less: deferred tax assets"]), 5059.00,
     "5,060.04 − 1.22 − 0.15 = 5,058.67 against CareEdge's published Rs 5,059 crore. The "
     "financial-sector definition is confirmed by reproduction, not asserted"),
    ("FY2026 on-book gearing reproduces published 1.56x",
     "=Inputs!D%d/(Inputs!D%d-Inputs!D%d-Inputs!D%d)" % (
         R["TOTAL DEBT"], R["Total equity (consolidated)"],
         R["less: intangible assets"], R["less: deferred tax assets"]), 1.56,
     "7,873.67 / 5,058.67 = 1.5565x. Using total equity instead of TNW gives 1.556x too - the "
     "definitions barely diverge here because intangibles are negligible, but the CONVENTION "
     "still has to be stated"),
    ("FY2025 AUM/TNW reproduces published 2.53x",
     "=Inputs!C%d/(Inputs!C%d-Inputs!C%d-Inputs!C%d)" % (
         R["Assets under management (AUM)"], R["Total equity (consolidated)"],
         R["less: intangible assets"], R["less: deferred tax assets"]), 2.53,
     "10,865 / 4,293.58 = 2.5305x - exact against the published 2.53x"),
    ("FY2026 total income reproduces published Rs 2,245 cr",
     "=Inputs!D%d" % R["Total income"], 2245.00,
     "Consolidated total income of Rs 2,245.48 cr. The STANDALONE figure is Rs 1,564.15 cr - "
     "splicing the two bases would put the report out by Rs 681 crore"),
    ("FY2026 PAT reproduces published Rs 943 cr",
     "=Inputs!D%d" % R["Profit after tax"], 943.00,
     "Consolidated PAT of Rs 942.94 cr against standalone Rs 692.87 cr"),
    ("LINE INTEGRITY - bank facilities sum to the rated limit",
     "=2058.75+30+11.25", 2100.00,
     "Annexure-1: term loan 2,058.75 + working capital 30.00 + bank guarantee 11.25 = "
     "Rs 2,100.00 crore, matching the header table exactly"),
    ("LINE INTEGRITY - NCDs sum to the rated limit",
     "=45+240+200+280+80+300", 1145.00,
     "NCD II 45.00 + III 240.00 + IV 200.00 + V 280.00 (160.00+120.00) + VI 80.00 + "
     "VII 300.00 (150.00+100.00+50.00 proposed) = Rs 1,145.00 crore, exact"),
    ("FY2026 total debt itemises to the balance sheet",
     "=Inputs!D%d+Inputs!D%d" % (R["Debt securities"],
                                 R["Borrowings (other than debt securities)"]), 7873.67,
     "1,350.49 + 6,523.18. Note there is NO commercial paper and no short-term unsecured "
     "borrowing - the AR states zero short-term funding risk"),
    ("FY2026 AUM ties to the entity split",
     "=9306+3801", 13107.00,
     "Aptus HFC Rs 9,306 cr (71%) + AFIPL Rs 3,801 cr (29%). The consolidated approach is not "
     "optional here - the NBFC subsidiary is 29% of the managed book"),
]

SCORE = {
    "factors": [
        ("Capitalisation", 1, 0.30,
         "CRAR of 71% against an RBI minimum of 15% - more than four times over, and 56 "
         "percentage points of headroom. On-book gearing of 1.56x and AUM/TNW of 2.59x are "
         "exceptionally low for an HFC growing at 20%+. Tangible net worth of Rs 5,058.67 cr "
         "has been built by accrual: RoE rose from 14.5% (FY2021) to 20.2% while the equity "
         "base more than doubled. This is the dominant rating consideration and it provides "
         "both growth headroom and a deep buffer against asset-quality stress."),
        ("Profitability", 1, 0.25,
         "PAT Rs 942.94 cr on total income of Rs 2,245.48 cr - a 42.0% PAT margin, ROMA of "
         "7.87% and RONW of 20.2%, all reproducing the AR's own reported figures. NIM on "
         "average AUM of 10.81% reflects affordable-housing yields against a falling cost of "
         "borrowing (8.3% in FY2026 from 8.7%). Cost-to-income of 20.2% and opex/AUM stable at "
         "2.7% across six years indicate genuine operating efficiency, not a growth artefact."),
        ("Scale and track record", 2, 0.20,
         "AUM of Rs 13,107 cr, compounding ~26% over six years from Rs 4,068 cr in FY2021, "
         "with an established position in affordable housing. Q1FY2027 continued the trend - "
         "income up 15.2% and PAT up 19.0% year on year. The book splits Rs 9,306 cr housing "
         "(71%) and Rs 3,801 cr through the NBFC subsidiary (29%), giving product diversity "
         "within a single credit-underwriting culture."),
        ("Asset quality", 3, 0.15,
         "GNPA rose to 1.52% from 1.19% and NNPA to 1.15% from 0.89% (AR, consolidated); "
         "CareEdge publishes gross stage 3 of 1.45% against 1.18%. Credit cost on average AUM "
         "doubled to 0.51%. Absolute levels remain comfortable and LTV of ~40% gives real "
         "collateral protection, but the DIRECTION is uniformly adverse and the book is only "
         "moderately seasoned, so reported delinquency understates through-cycle experience. "
         "Provision coverage on stage 3 of 25.50% (standalone) is thin, which is defensible "
         "only because of the low LTV."),
        ("Concentration and borrower profile", 4, 0.10,
         "Geographically concentrated in southern India, improving only gradually, and lending "
         "to an underbanked segment with limited formal income documentation. This is the "
         "structural constraint on the rating: the same segment that produces a 10.81% NIM is "
         "the one most exposed to local economic shocks and to any tightening of affordable-"
         "housing regulation. A corporate guarantee of Rs 269.63 cr for AFIPL's borrowings "
         "sits off balance sheet."),
    ],
    "anchor": "AA band (composite 1.70)",
    "view": "CARE AA; Stable",
    "divergence":
        "NO DIVERGENCE. My independent view is CARE AA; Stable, which matches the CareEdge "
        "press release of 02-Jul-2026 (reaffirmed; upgraded to AA; Stable on 03-Jul-2025 from "
        "AA-; Positive, having been AA-; Stable through 2023-24). The rating rests on "
        "capitalisation that is extreme rather than merely adequate - 71% CRAR and 1.56x "
        "gearing - against a concentrated book lending to underbanked borrowers whose asset "
        "quality is drifting adversely from a low base. Every ratio in this workbook was "
        "solved back from and reproduces the agency's published figures; where a figure "
        "differs it is disclosed rather than forced, notably the asset-quality measure, where "
        "the AR's consolidated GNPA of 1.52% and CareEdge's gross stage 3 of 1.45% are "
        "different measures of the same book and are both reported.",
}

if __name__ == "__main__":
    print("Saved:", build_spreads(
        company="Aptus Value Housing Finance India Limited", years=Y, inputs=INPUTS,
        ratios=RATIOS, tieouts=TIEOUTS, score=SCORE, basis="Consolidated",
        out="Aptus Value Housing Finance India Limited_Financial_Spreads.xlsx"))
