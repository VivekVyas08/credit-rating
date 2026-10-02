"""HDFC Securities Limited_Financial_Spreads.xlsx - CareEdge broking suite. VERSION 2.

Rebuilt 20-Aug-2026 after comparison with the CARE Ratings press release of the same date.
v1 is archived as build_spreads_v1_superseded.py; see HSL_Defect_Analysis_20Aug2026.md.

THE CONVENTION COLUMN NOW CARRIES THE AGENCY'S DEFINITIONS, NOT MINE (failure mode 32).
Every ratio here is defined as CareEdge defines it for broking, and the TieOut tab tests
whether each REPRODUCES CareEdge's published figure. That is a far stronger test than internal
consistency: a definition that will not reproduce the agency's number IS WRONG.
See CareEdge/BROKING_CONVENTIONS.md.

Rs CRORE. Statements are in Rs lakhs; converted once at extraction.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import build_spreads          # noqa: E402

Y = ["FY2025", "FY2026", "Q1FY2027"]
AR = "FY2026 annual report (04-08-2026)"
PR = "CareEdge press release 20-Aug-2026 (operator-supplied)"

INPUTS = [
    # --- rated LIMITS, not outstandings (failure mode 31) -----------------------------------
    ("RATED: commercial paper limit",        [18000.00, 20000.00, 20000.00],
     PR + " header table - enhanced from Rs 18,000.00 cr. NOT an outstanding balance"),
    ("RATED: LT/ST bank facilities limit",   [3000.00, 3000.00, 3000.00],
     PR + " header table - CARE AAA; Stable / CARE A1+, Reaffirmed"),
    # --- profitability ------------------------------------------------------------------------
    ("Total income",                         [3264.86, 3110.15, 950.03], AR + " P&L L3115"),
    ("Total expenses",                       [1768.71, 1873.09, None],   AR + " P&L L3122"),
    ("Finance costs",                        [785.45, 817.40, None],     AR + " P&L L3117"),
    ("Profit after tax",                     [1125.00, 929.90, 297.06],  AR + " / Q1 results"),
    ("Interest income",                      [1418.34, 1497.93, None],   AR + " P&L L3107"),
    ("Fees and commission income",           [1744.20, 1515.83, None],   AR + " P&L"),
    ("Brokerage income",                     [1259.55, 1012.19, None],   AR + " note L5090"),
    ("Dividend (interim + final)",           [898.30, 740.10, None],     AR + " appropriation"),
    # --- TANGIBLE net worth build-up (failure mode 32) ----------------------------------------
    ("Total equity",                         [3348.59, 3595.92, None],   AR + " L6633"),
    ("less: deferred tax assets",            [0.52, 15.57, None],        AR + " BS L3033"),
    ("less: other intangible assets",        [84.24, 78.23, None],       AR + " BS L3038"),
    ("less: intangibles under development",  [7.32, 5.63, None],         AR + " BS L3037"),
    ("TANGIBLE NET WORTH (published)",       [3257.00, 3496.00, 3647.00],
     PR + " Brief Financials - reproduced exactly by the build-up above"),
    # --- debt and OFF-BALANCE-SHEET -----------------------------------------------------------
    ("Debt securities (commercial paper)",   [7741.52, 12931.33, 15765.00], AR + " BS / " + PR),
    ("Borrowings other than debt secs (TREPS)", [202.25, 2182.55, 2183.00], AR + " BS / " + PR),
    ("Loan against deposits",                [None, None, 338.00],       PR + " liquidity para"),
    ("TOTAL FUND-BASED DEBT",                [7943.77, 15113.88, 18286.00], AR + " / " + PR),
    ("Bank guarantees outstanding",          [700.00, 1100.00, None],
     AR + " CONTINGENT LIABILITIES note L5421 - off balance sheet, and CareEdge counts it "
          "in gearing. v1 never extracted this, hence 4.20x against a published 4.64x"),
    ("Total assets",                         [14031.11, 21784.33, None], AR + " BS"),
    # --- MTF: the sector-defining asset --------------------------------------------------------
    ("MTF loan book",                        [5511.87, 7132.66, 10081.00],
     AR + " BS Loans / " + PR + " - Rs 10,081 cr as on 30-Jun-2026"),
    # --- liquidity: UNENCUMBERED only (failure mode 34) ---------------------------------------
    ("UNENCUMBERED cash and equivalents",    [None, None, 422.00],
     PR + " liquidity para. NOT the balance-sheet 'bank balance' line of Rs 7,838.73 cr, which "
          "is overwhelmingly CLIENT funds and exchange margin"),
    ("Unutilised sanctioned lines",          [None, None, 2698.00], PR + " liquidity para"),
    # --- franchise ------------------------------------------------------------------------------
    ("Active clients (lakh)",                [None, None, 10.05],
     PR + " - ~10.05 lakh as on 31-Jul-2026; SIXTH-largest retail stockbroker"),
    ("Branches (no.)",                       [134, 128, 127],
     "FY2025 AR / FY2026 AR / " + PR + ". 184 at 31-Mar-2024 - consolidating toward digital"),
]
R = {lab: 6 + i for i, (lab, _, _) in enumerate(INPUTS)}


def I(lab):
    return "Inputs!{c}%d" % R[lab]


def f(e):
    return "=" + e


def at(lab, col):
    return "Inputs!%s%d" % (col, R[lab])


def guard(expr, *required):
    """Render BLANK when a required input is absent, never 0.

    The formulas cache returns 0 for an empty reference, and a 0 in a ratio column reads as a
    real measurement - e.g. cost-to-income "0.00%" for Q1FY27, where the input simply is not
    disclosed. Blank is the honest output.
    """
    cond = "+".join('N(%s)' % I(r) for r in required)
    return "=IF(%s=0,\"\",%s)" % (cond, expr[1:] if expr.startswith("=") else expr)


def yr_only(idx, expr):
    """Show a value in ONE period column only - for ratios needing a prior-year figure.

    Keyed on the YEAR INDEX {y} (0=FY2025, 1=FY2026, 2=Q1FY2027). An earlier version compared
    {c} - the column LETTER - against a year name, so it matched nothing and blanked every cell.
    """
    return '=IF({y}<>%d,"",%s)' % (idx, expr)


RATIOS = [
    ("TANGIBLE NET WORTH (computed)",
     guard(I("Total equity") + "-" + I("less: deferred tax assets") + "-"
           + I("less: other intangible assets") + "-" + I("less: intangibles under development"),
           "Total equity"),
     "Total equity less deferred tax assets and all intangibles",
     "CareEdge's net-worth definition for financial-sector entities. Reproduces the published "
     "Rs 3,257 cr / Rs 3,496 cr EXACTLY. v1 used total equity and was wrong by ~Rs 100 cr",
     "#,##0.00"),
    ("Overall gearing (x)  [KEY]",
     guard("(" + I("TOTAL FUND-BASED DEBT") + "+" + I("Bank guarantees outstanding") + ")/"
           + I("TANGIBLE NET WORTH (published)"), "Bank guarantees outstanding"),
     "(Total fund-based debt + bank guarantees outstanding) / tangible net worth",
     "INCLUDES non-fund-based limits utilised - CareEdge's own footnote. Reproduces published "
     "2.65x and 4.64x exactly; 5.28x as on 30-Jun-2026. v1 published 4.20x on plain debt/equity",
     '0.00"x"'),
    ("Fund-based gearing (x)",
     f(I("TOTAL FUND-BASED DEBT") + "/" + I("TANGIBLE NET WORTH (published)")),
     "Total fund-based debt / tangible net worth",
     "Borrowings only. Management's stated intent is to hold this below 5x while expanding MTF, "
     "subject to the regulatory leverage cap", '0.00"x"'),
    ("Cost-to-income (%)",
     guard("(" + I("Total expenses") + "-" + I("Finance costs") + ")/("
           + I("Total income") + "-" + I("Finance costs") + ")", "Total expenses"),
     "(Total expenses less finance costs) / (total income less finance costs)",
     "A CareEdge BROKING metric - v1 wrongly excluded it as 'a bank metric' (failure mode 33). "
     "Computes 39.66%/46.04% against published 39.42%/45.54%: within ~0.5pp, the residual being "
     "a small expense line CareEdge's template excludes. Reported as computed, NOT forced",
     "0.00%"),
    ("RONW on AVERAGE TNW (%)",
     yr_only(1, "Inputs!D%d/AVERAGE(Inputs!C%d,Inputs!D%d)"
             % (R["Profit after tax"], R["TANGIBLE NET WORTH (published)"],
                R["TANGIBLE NET WORTH (published)"])),
     "PAT / average of opening and closing tangible net worth",
     "AVERAGE TNW, not closing equity. Reproduces published 27.54% for FY2026. CareEdge also "
     "publishes 51.63% (FY2024) and 43.28% (FY2025) - the compression is the story", "0.00%"),
    ("ROTA on average assets (%)",
     yr_only(1, "Inputs!D%d/AVERAGE(Inputs!C%d,Inputs!D%d)"
             % (R["Profit after tax"], R["Total assets"], R["Total assets"])),
     "PAT / average total assets",
     "5.19% computed against published 5.22%. Quarterly ROTA is annualised (Q1FY27: 6.01%)",
     "0.00%"),
    ("PAT margin (%)",
     f(I("Profit after tax") + "/" + I("Total income")),
     "Profit after tax / total income",
     "Reproduces published 29.90% (FY2026) and 31.27% (Q1FY27) exactly", "0.00%"),
    ("MTF book growth (%)  [SECTOR]",
     '=IF({y}=0,"",Inputs!{c}%d/INDEX(Inputs!$C$%d:$E$%d,{y})-1)' % (
         R["MTF loan book"], R["MTF loan book"], R["MTF loan book"]),
     "Year-on-year / sequential growth in the margin trading facility book",
     "+29.4% in FY2026 then +41.3% in ONE quarter to Rs 10,081 cr. THE driver of borrowing "
     "growth, and the asset whose quality CareEdge names as the key monitorable", "0.0%"),
    ("MTF book / tangible net worth (x)",
     f(I("MTF loan book") + "/" + I("TANGIBLE NET WORTH (published)")),
     "MTF book / tangible net worth",
     "1.69x to 2.04x to 2.76x. The capitalisation buffer against a book secured on volatile "
     "listed collateral - the ratio the key monitorable is really about", '0.00"x"'),
    ("Fees and commission income share (%)",
     guard(I("Fees and commission income") + "/" + I("Total income"),
           "Fees and commission income"),
     "Fees and commission income / total income",
     "48.7% in FY2026, matching CareEdge's stated 48%. Brokerage alone is 32.5% (their 33%); "
     "MTF interest contributes a further 31%", "0.0%"),
    ("Interest income share (%)",
     guard(I("Interest income") + "/" + I("Total income"), "Interest income"),
     "Interest income / total income",
     "Rose to 48.2% of income as MTF scaled - Rs 1,498 cr from Rs 1,418 cr. The diversification "
     "away from pure brokerage that CareEdge credits, and the source of the new risk", "0.0%"),
    ("Dividend payout (%)",
     guard(I("Dividend (interim + final)") + "/" + I("Profit after tax"),
           "Dividend (interim + final)"),
     "Dividend / profit after tax",
     "~80% in both years. CareEdge notes TNW grew only gradually 'despite healthy earnings, "
     "considering sizeable dividend payouts'", "0.0%"),
    ("UNENCUMBERED cash / fund-based debt (x)",
     guard(I("UNENCUMBERED cash and equivalents") + "/" + I("TOTAL FUND-BASED DEBT"),
           "UNENCUMBERED cash and equivalents"),
     "Unencumbered cash / total fund-based borrowings",
     "0.02x as on 30-Jun-2026. v1 claimed 0.74x by counting Rs 7,838.73 cr of CLIENT funds and "
     "exchange margin as company cash - a 23x overstatement (failure mode 34). Cover comes from "
     "the self-liquidating MTF book, unutilised lines of Rs 2,698 cr and parent flexibility",
     '0.00"x"'),
    ("Branches (no.)  [SECTOR]",
     f(I("Branches (no.)")),
     "Branch count at each date",
     "184 (31-Mar-2024) -> 134 -> 128 -> 127 (30-Jun-2026). Deliberate consolidation toward "
     "digital, confirmed by CareEdge; ~95% of Q1FY27 brokerage came from retail clients",
     "#,##0"),
]

# make_spreads writes ONE note column, so calculation and convention are joined into it.
RATIOS = [(lab, formula, calc + chr(8212).join(['  ', '  ']) + conv, fmt)
          for lab, formula, calc, conv, fmt in RATIOS]

TIEOUTS = [
    ("TNW build-up reproduces published FY2026",
     "=Inputs!D%d-Inputs!D%d-Inputs!D%d-Inputs!D%d" % (
         R["Total equity"], R["less: deferred tax assets"],
         R["less: other intangible assets"], R["less: intangibles under development"]),
     3496.00,
     "3,595.92 − 15.57 − 78.23 − 5.63 = 3,496.49 against CareEdge's published Rs 3,496 crore. "
     "The definition is confirmed by reproduction, not asserted"),
    ("TNW build-up reproduces published FY2025",
     "=Inputs!C%d-Inputs!C%d-Inputs!C%d-Inputs!C%d" % (
         R["Total equity"], R["less: deferred tax assets"],
         R["less: other intangible assets"], R["less: intangibles under development"]),
     3257.00, "3,348.59 − 0.52 − 84.24 − 7.32 = 3,256.51 against published Rs 3,257 crore"),
    ("Overall gearing reproduces published FY2026 4.64x",
     "=(Inputs!D%d+Inputs!D%d)/Inputs!D%d" % (
         R["TOTAL FUND-BASED DEBT"], R["Bank guarantees outstanding"],
         R["TANGIBLE NET WORTH (published)"]), 4.64,
     "(15,113.88 + 1,100.00) / 3,496 = 4.64x. Excluding the bank guarantee gives 4.32x and "
     "using total equity gives 4.20x - which is what v1 published"),
    ("Overall gearing reproduces published FY2025 2.65x",
     "=(Inputs!C%d+Inputs!C%d)/Inputs!C%d" % (
         R["TOTAL FUND-BASED DEBT"], R["Bank guarantees outstanding"],
         R["TANGIBLE NET WORTH (published)"]), 2.65,
     "(7,943.77 + 700.00) / 3,257 = 2.65x - the same definition reproduces both years"),
    ("RONW on average TNW reproduces published 27.54%",
     "=Inputs!D%d/AVERAGE(Inputs!C%d,Inputs!D%d)*100" % (
         R["Profit after tax"], R["TANGIBLE NET WORTH (published)"],
         R["TANGIBLE NET WORTH (published)"]), 27.54,
     "930 / ((3,257 + 3,496)/2) = 27.54%. On CLOSING equity it is 25.86%, which v1 published"),
    ("LINE INTEGRITY - CP tranches + proposed = rated limit",
     "=13860+6140", 20000.00,
     "Annexure-1 lists CP tranches summing to Rs 13,860.00 cr plus a Proposed line of "
     "Rs 6,140.00 cr = Rs 20,000.00 cr, matching the header table exactly. Condition (4) of the "
     "five-condition amendment is satisfied"),
    ("LINE INTEGRITY - LT/ST sanctioned + proposed = rated limit",
     "=2250+750", 3000.00,
     "Rs 2,250.00 cr (maturity 06-May-26) + Rs 750.00 cr Proposed = Rs 3,000.00 cr, matching "
     "the header table exactly"),
    ("Q1FY27 fund-based debt itemises to the published total",
     "=Inputs!E%d+Inputs!E%d+Inputs!E%d" % (
         R["Debt securities (commercial paper)"],
         R["Borrowings other than debt secs (TREPS)"], R["Loan against deposits"]), 18286.00,
     "CP 15,765 + TREPS 2,183 + loan against deposits 338 = Rs 18,286 crore"),
    ("RATED LIMIT vs DRAWN - the distinction v1 collapsed",
     "=Inputs!D%d-Inputs!D%d" % (R["RATED: commercial paper limit"],
                                 R["Debt securities (commercial paper)"]), 7068.67,
     "Rs 20,000.00 cr rated against Rs 12,931.33 cr drawn at 31-Mar-2026 - roughly Rs 7,069 cr "
     "of headroom. v1 put the DRAWN figure in the rating table, so this headroom, and the "
     "enhancement from Rs 18,000 cr, were both invisible (failure mode 31)"),
]

SCORE = {
    "factors": [
        ("Parentage and linkage with HDFC Bank", 1, 0.40,
         "HDFC Bank Limited (CARE AAA; Stable / CARE A1+) holds 93.99% as on 30-Jun-2026. "
         "Board representation via HBL's nominee director; the MD & CEO and several key "
         "personnel came from HBL. HBL's network drives lead generation while HSL's clients "
         "strengthen the bank's retail liability franchise. Shared brand, strong financial "
         "flexibility, and expectation of continued need-based support. This dominates."),
        ("Capitalisation and gearing", 2, 0.20,
         "TNW Rs 3,496 cr at 31-Mar-2026 and Rs 3,647 cr at 30-Jun-2026, but overall gearing "
         "rose 2.65x to 4.64x and further to 5.28x - driven by MTF expansion, margin "
         "requirements and investments. ~86% of fund-based borrowing is CP. Management intends "
         "to hold FUND-BASED gearing below 5x. Sizeable ~80% dividend payouts limit accretion."),
        ("Earnings profile", 2, 0.15,
         "FY2026 total income Rs 3,110 cr and PAT Rs 930 cr - PAT margin 29.90%, ROTA 5.22%, "
         "RONW 27.54%. Healthy in absolute terms but moderating: RONW fell 51.63% (FY24) to "
         "43.28% (FY25) to 27.54%. Q1FY27 recovered - income Rs 950 cr, PAT Rs 297 cr, margin "
         "31.27%, RONW 34.0% annualised. Revenue is diversified: fees/commission 48%, MTF "
         "interest 31%, brokerage alone 33%."),
        ("Franchise and market position", 2, 0.15,
         "SIXTH-largest retail stockbroker by active clients (~10.05 lakh as on 31-Jul-2026). "
         "~95% of Q1FY27 brokerage from retail. Branch network deliberately consolidated from "
         "184 (31-Mar-2024) to 127 (30-Jun-2026) in favour of digital, with the 'HDFC Sky' app "
         "targeting new-age investors. Competing against zero-brokerage discount platforms."),
        ("MTF concentration and regulatory risk", 4, 0.10,
         "The MTF book grew to Rs 10,081 cr at 30-Jun-2026 from Rs 7,133 cr and Rs 5,512 cr - "
         "2.76x tangible net worth. Secured on listed collateral, but adverse valuation moves "
         "transmit credit and market risk directly, and CareEdge names MTF asset quality and "
         "the capitalisation buffer as THE key monitorable. Compounding this, RBI's amended "
         "directions of 13-Feb-2026 (effective 01-Jul-2026) require fully collateralised "
         "lending to capital-market intermediaries, higher-quality collateral, minimum "
         "haircuts and MTF backed by high-quality liquid collateral - expected to raise funding "
         "costs. SEBI's Oct-2024 F&O measures already compressed derivative volumes."),
    ],
    "anchor": "A1+ / AAA band (composite 1.85)",
    "view": "CARE A1+ (CP, Rs 20,000.00 cr) and CARE AAA; Stable / CARE A1+ "
            "(LT/ST bank facilities, Rs 3,000.00 cr)",
    "divergence":
        "NO DIVERGENCE - but only after correction, and the correction was not marginal. This "
        "workbook's v1 assigned A1+ on commercial paper alone and stated that no long-term "
        "rating applied and no outlook was assigned, having reasoned from the maturity tables "
        "(all DRAWN borrowings inside 12 months) to the rated universe. CareEdge's press "
        "release of the SAME DATE rates Rs 20,000.00 cr of CP at CARE A1+ AND Rs 3,000.00 cr "
        "of long-term/short-term bank facilities at CARE AAA; Stable, Reaffirmed, with history "
        "to 22-Dec-2023. v1 also used total equity rather than tangible net worth, omitted the "
        "Rs 1,100 cr bank guarantee from gearing, computed return on closing rather than "
        "average net worth, excluded cost-to-income on a misapplied sector rule, and overstated "
        "liquidity 23x by treating client funds as company cash. Every convention in this "
        "version is now solved back from and reproduces CareEdge's published figures.",
}

if __name__ == "__main__":
    print("Saved:", build_spreads(
        company="HDFC Securities Limited", years=Y, inputs=INPUTS, ratios=RATIOS,
        tieouts=TIEOUTS, score=SCORE, basis="Standalone",
        out="HDFC Securities Limited_Financial_Spreads.xlsx"))
