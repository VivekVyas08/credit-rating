"""Generate Repco Home Finance Limited_Financial_Spreads.xlsx from compute_ratios.py.

The script is the source of truth; this file only renders it into the review/feed layer that
the Step 12 model and the Step 12b scorecard draw from (CLAUDE.md Step 5). Nothing is hand
typed: every input below is read out of compute_ratios, and every ratio in the workbook is a
LIVE Excel formula referencing the Inputs sheet.

FY2026 carries an audited P&L but no balance sheet anywhere in the document set, so every
balance-sheet-dependent ratio guards on the FY2026 total-assets cell being empty and shows
"NA" - which is what ICRA itself publishes when a period's figure is unavailable (see the
CRAR row of GIC Housing Finance Limited, 10-Oct-2025).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import build_spreads                                    # noqa: E402
import compute_ratios as C                                               # noqa: E402

Y = ["FY2023", "FY2024", "FY2025", "FY2026", "Q1FY2027"]
NA = ""          # empty cell -> the IF() guards below render "NA"

AR23 = "FY2023 AR, standalone balance sheet / P&L (audited)"
AR25 = "FY2025 AR, standalone balance sheet / P&L (audited; FY2024 comparative column)"
Q1 = ("Q1FY2027 filing, 11-Aug-2026: audited year-ended-31-Mar-2026 column for FY2026 P&L; "
      "Reg 54(3) security-cover certificate for the 30-Jun-2026 balance sheet")
REG52 = "Reg 52(4) disclosure in the Q1FY2027 filing, 30-Jun-2026"
MDA = "FY2025 AR, management discussion and analysis / regulatory notes"


def bs(item):
    """FY2023, FY2024, FY2025 from the annual reports; FY2026 absent; Q1FY2027 = 30-Jun-2026."""
    v = C.BS[item]
    return [v[1], v[2], v[3], NA, v[5]]


def pl(item):
    return list(C.PL[item])


def d(metric):
    m = C.DISCLOSED[metric]
    return [m.get(k, NA) for k in ["FY2023", "FY2024", "FY2025", "FY2026", "Q1FY2027"]]


# --------------------------------------------------------------------------- inputs
INPUTS = [
    ("--- PROFIT AND LOSS ---", [NA] * 5, ""),
    ("Interest income", pl("Interest income"), AR23 + " / " + AR25 + " / " + Q1),
    ("Revenue from operations", pl("Revenue from ops"), AR23 + " / " + AR25 + " / " + Q1),
    ("Other income", pl("Other income"), AR23 + " / " + AR25 + " / " + Q1),
    ("Total income", pl("Total income"), AR23 + " / " + AR25 + " / " + Q1),
    ("Finance costs", pl("Finance costs"), AR23 + " / " + AR25 + " / " + Q1),
    ("Employee cost", pl("Employee cost"), AR23 + " / " + AR25 + " / " + Q1),
    ("Depreciation and amortisation", pl("Depreciation"), AR23 + " / " + AR25 + " / " + Q1),
    ("Other expenses", pl("Other expenses"), AR23 + " / " + AR25 + " / " + Q1),
    ("Impairment on financial instruments (+ charge / - write-back)", pl("Impairment"),
     AR23 + " / " + AR25 + " / " + Q1 + " - sign as reported; negative = write-back"),
    ("Profit before tax", pl("PBT"), AR23 + " / " + AR25 + " / " + Q1),
    ("Tax expense", pl("Tax expense"), AR23 + " / " + AR25 + " / " + Q1),
    ("Profit after tax", pl("PAT"), AR23 + " / " + AR25 + " / " + Q1),

    ("--- BALANCE SHEET ---", [NA] * 5, ""),
    ("Cash and cash equivalents", bs("Cash and equivalents"), AR23 + " / " + AR25 + " / " + Q1),
    ("Bank balances other than cash", bs("Other bank balances"), AR23 + " / " + AR25 + " / " + Q1),
    ("Loans (net of impairment allowance)", bs("Loans (net of ECL)"),
     AR23 + " / " + AR25 + " / " + Q1),
    ("Investments", bs("Investments"), AR23 + " / " + AR25 + " / " + Q1),
    ("Other intangible assets", bs("Other intangible assets"), AR23 + " / " + AR25 + " / " + Q1),
    ("Intangible assets under development", bs("Intangibles under development"),
     AR23 + " / " + AR25 + " / " + Q1),
    ("Total assets", bs("Total assets"), AR23 + " / " + AR25 + " / " + Q1),
    ("Debt securities", bs("Debt securities"),
     AR25 + " (nil to FY2025) / " + Q1 + " - listed secured NCD 125.49 + other 73.70"),
    ("Borrowings other than debt securities", bs("Borrowings (other)"),
     AR23 + " / " + AR25 + " / " + Q1 + " - bank 10,992.79 + others 895.03 at 30-Jun-2026"),
    ("Total liabilities", bs("Total liabilities"), AR23 + " / " + AR25 + " / " + Q1),
    ("Total equity (net worth)", bs("Total equity"),
     AR23 + " / " + AR25 + " / " + REG52 + " (4,018.65, independently published)"),
    ("Impairment allowance on loans", bs("Impairment allowance"),
     AR23 + " / " + AR25 + " - not disclosed after FY2025"),
    ("Opening total assets (prior period)",
     [C.BS["Total assets"][0], C.BS["Total assets"][1], C.BS["Total assets"][2], NA,
      C.BS["Total assets"][4]],
     "prior-period column of the same statement; 30-Sep-2025 for Q1FY2027 averaging"),
    ("Opening total equity (prior period)",
     [C.BS["Total equity"][0], C.BS["Total equity"][1], C.BS["Total equity"][2], NA,
      C.BS["Total equity"][4]],
     "prior-period column of the same statement; 30-Sep-2025 for Q1FY2027 averaging"),
    ("Opening impairment allowance (prior period)",
     [C.BS["Impairment allowance"][0], C.BS["Impairment allowance"][1],
      C.BS["Impairment allowance"][2], NA, NA],
     "prior-period column of the same statement"),

    ("--- DISCLOSED / REGULATORY (not computed here) ---", [NA] * 5, ""),
    ("AUM - loan book as reported (Rs cr)", d("AUM (loan book, Rs cr)"), MDA),
    ("Disbursements (Rs cr)", d("Disbursements (Rs cr)"), MDA),
    ("Gross NPA % - excluding interest accrued and EIR", d("GNPA % (excl int accrued)"),
     MDA + " / " + REG52),
    ("Net NPA % - excluding interest accrued and EIR", d("NNPA % (excl int accrued)"),
     MDA + " / " + REG52),
    ("Gross NPA % - including interest accrued (RBI sectoral format)",
     d("GNPA % (incl int accrued)"), REG52 + "; FY2025 equivalent is 3.99% per the AR"),
    ("Capital-to-risk-weighted-assets ratio %", d("CRAR %"),
     MDA + " Note 32.1 - not disclosed in any FY2026/FY2027 quarterly filing"),
    ("Tier I ratio %", d("Tier I %"), MDA + " Note 32.1"),
    ("Provision coverage ratio %", d("PCR %"), REG52),
    ("Liquidity coverage ratio %", d("LCR %"), REG52),
    ("Branches", d("Branches"), MDA),
    ("Home equity (non-housing) book (Rs cr)", d("Home equity book (Rs cr)"),
     "FY2025 AR six-year highlights table"),
    ("Undisbursed sanction commitment (Rs cr)", d("Off-balance-sheet exposure"),
     "FY2025 AR Note 39.2 Commitments - sanction pending disbursement, NOT an assigned book"),
]

# Inputs are written from row 6 downward, one row per entry, so the row of entry i is 6+i.
ROW = {label: 6 + i for i, (label, _, _) in enumerate(INPUTS)}
COL = {"FY2023": "C", "FY2024": "D", "FY2025": "E", "FY2026": "F", "Q1FY2027": "G"}


def I(label, c="{c}"):
    return "Inputs!%s%d" % (c, ROW[label])


TA = I("Total assets")
TA0 = I("Opening total assets (prior period)")
EQ = I("Total equity (net worth)")
EQ0 = I("Opening total equity (prior period)")
ECL = I("Impairment allowance on loans")
ECL0 = I("Opening impairment allowance (prior period)")
DEBT = "(%s+%s)" % (I("Debt securities"), I("Borrowings other than debt securities"))
TNW = "(%s-%s-%s)" % (EQ, I("Other intangible assets"),
                      I("Intangible assets under development"))
MA = "(%s+%s)" % (TA, ECL)
MA0 = "(%s+%s)" % (TA0, ECL0)
AVG_MA = "((%s+%s)/2)" % (MA, MA0)
AVG_TA = "((%s+%s)/2)" % (TA, TA0)
AVG_EQ = "((%s+%s)/2)" % (EQ, EQ0)
# Q1FY2027 is a single quarter: {y} is the zero-based year index, so index 4 annualises.
ANN = "(IF({y}=4,4,1))"
PAT = I("Profit after tax")
NII = "(%s-%s)" % (I("Revenue from operations"), I("Finance costs"))
OPEX = "(%s+%s+%s)" % (I("Employee cost"), I("Depreciation and amortisation"),
                       I("Other expenses"))


def guard(expr):
    """Balance-sheet ratios show NA in FY2026, where no balance sheet exists."""
    return '=IF(%s="","NA",%s)' % (TA, expr)


RATIOS = [
    ("Net interest income (Rs cr)", "=" + NII, "revenue from operations less finance costs",
     "#,##0.0"),
    ("Pre-provision operating profit (Rs cr)",
     "=%s+%s" % (I("Profit before tax"), I("Impairment on financial instruments (+ charge / - write-back)")),
     "PBT add back the impairment line, so the credit-cost swing is visible", "#,##0.0"),
    ("Operating expenses (Rs cr)", "=" + OPEX, "employee + depreciation + other expenses",
     "#,##0.0"),
    ("Total managed assets (Rs cr)", guard(MA),
     "total assets + impairment allowance (ICRA definition)", "#,##0.0"),
    ("Total debt (Rs cr)", guard(DEBT), "debt securities + borrowings; leases excluded",
     "#,##0.0"),
    ("Tangible net worth (Rs cr)", guard(TNW),
     "equity less intangibles and intangibles under development", "#,##0.0"),

    ("Net interest margin % (on average total assets)",
     guard("100*%s*%s/%s" % (NII, ANN, AVG_TA)),
     "annualised NII over average total assets", "0.00"),
    ("Operating expenses / average total assets %",
     guard("100*%s*%s/%s" % (OPEX, ANN, AVG_TA)),
     "ICRA's NBFC efficiency measure, not cost-to-income", "0.00"),
    ("Cost-to-income %",
     "=100*%s/(%s-%s)" % (OPEX, I("Total income"), I("Finance costs")),
     "secondary cross-reference only; bank vocabulary", "0.00"),
    ("Credit cost % (on average managed assets)",
     guard("100*%s*%s/%s" % (I("Impairment on financial instruments (+ charge / - write-back)"),
                             ANN, AVG_MA)),
     "negative = write-back releasing provisions into profit", "0.00"),
    ("Return on average managed assets %", guard("100*%s*%s/%s" % (PAT, ANN, AVG_MA)),
     "ICRA's headline HFC return measure", "0.00"),
    ("Return on average total assets %", guard("100*%s*%s/%s" % (PAT, ANN, AVG_TA)),
     "reproduces the AR's 3.1% and CareEdge's 3.11% for FY2025", "0.00"),
    ("Return on average net worth %", guard("100*%s*%s/%s" % (PAT, ANN, AVG_EQ)),
     "average denominator; the AR uses opening equity", "0.00"),

    ("Gearing (times)", guard("%s/%s" % (DEBT, EQ)), "total debt over net worth", "0.00"),
    ("Gearing on tangible net worth (times)", guard("%s/%s" % (DEBT, TNW)),
     "same numerator, intangibles stripped from the denominator", "0.00"),
    ("Managed assets / tangible net worth (times)", guard("%s/%s" % (MA, TNW)),
     "balance-sheet leverage including the provision cushion", "0.00"),
    ("Equity / total assets %", guard("100*%s/%s" % (EQ, TA)), "book capitalisation", "0.00"),
    ("Book value per share (Rs)", guard("%s/6.2561362" % EQ),
     "62,561,362 shares, unchanged throughout", "#,##0.0"),
    ("Basic EPS (Rs)", "=%s*%s/6.2561362" % (PAT, ANN), "annualised for the quarter", "#,##0.0"),
    ("Liquid assets - cash and bank (Rs cr)",
     guard("%s+%s" % (I("Cash and cash equivalents"), I("Bank balances other than cash"))),
     "on-balance-sheet cash only; excludes undrawn lines, which are not disclosed", "#,##0.0"),
    ("Non-housing (home equity) share of book %",
     '=IF(%s="","NA",100*%s/%s)' % (I("Home equity (non-housing) book (Rs cr)"),
                                    I("Home equity (non-housing) book (Rs cr)"),
                                    I("AUM - loan book as reported (Rs cr)")),
     "the mix shift that carries the higher delinquency", "0.00"),
]

TIEOUTS = [
    ("Balance sheet ties, FY2025",
     "=Inputs!E%d-Inputs!E%d-Inputs!E%d" % (ROW["Total assets"], ROW["Total liabilities"],
                                            ROW["Total equity (net worth)"]),
     0.0, "assets less (liabilities + equity); FY2025 AR"),
    ("Balance sheet ties, 30-Jun-2026",
     "=Inputs!G%d-Inputs!G%d-Inputs!G%d" % (ROW["Total assets"], ROW["Total liabilities"],
                                            ROW["Total equity (net worth)"]),
     0.0, "Reg 54(3) security-cover certificate, 30-Jun-2026"),
    ("Total debt / total assets, 30-Jun-2026",
     "=(Inputs!G%d+Inputs!G%d)/Inputs!G%d" % (ROW["Debt securities"],
                                              ROW["Borrowings other than debt securities"],
                                              ROW["Total assets"]),
     0.74, "company's own Reg 52(4) disclosure - proves the assembled debt figure"),
    ("Net worth, 30-Jun-2026", "=Inputs!G%d" % ROW["Total equity (net worth)"], 4018.65,
     "company's own Reg 52(4) disclosure"),
    ("Net profit margin, Q1FY2027",
     "=100*Inputs!G%d/Inputs!G%d" % (ROW["Profit after tax"], ROW["Total income"]), 24.40,
     "company's own Reg 52(4) disclosure"),
    ("Net interest income, FY2025",
     "=Inputs!E%d-Inputs!E%d" % (ROW["Revenue from operations"], ROW["Finance costs"]), 719.0,
     "FY2025 AR six-year highlights - proves the NII convention"),
    ("Net interest income, FY2024",
     "=Inputs!D%d-Inputs!D%d" % (ROW["Revenue from operations"], ROW["Finance costs"]), 679.0,
     "FY2025 AR six-year highlights"),
    ("Basic EPS, FY2025", "=Inputs!E%d/6.2561362" % ROW["Profit after tax"], 70.24,
     "FY2025 AR statement of profit and loss"),
    ("Gross loan exposure, FY2025",
     "=Inputs!E%d+Inputs!E%d" % (ROW["Loans (net of impairment allowance)"],
                                 ROW["Impairment allowance on loans"]), 14542.57,
     "FY2025 AR sector-wise NPA table - proves the impairment allowance"),
    ("Return on average total assets, FY2025",
     "=100*Inputs!E%d/((Inputs!E%d+Inputs!E%d)/2)"
     % (ROW["Profit after tax"], ROW["Total assets"],
        ROW["Opening total assets (prior period)"]), 3.11,
     "CareEdge press release 30-Sep-2025 (3.11%) and the FY2025 AR chart (3.1%)"),
    ("FY2026 PAT = PBT less tax",
     "=Inputs!F%d-Inputs!F%d" % (ROW["Profit before tax"], ROW["Tax expense"]), 452.77,
     "Q1FY2027 filing, audited FY2026 column"),
    ("CRAR FY2025 = Tier I + Tier II", "=Inputs!E%d+0.68" % ROW["Tier I ratio %"], 37.09,
     "FY2025 AR Note 32.1"),
]

SCORE = {
    "factors": [
        ("Franchise and scale", 4, 0.15,
         "A 25-year-old HFC with a defensible niche in tier-2/tier-3 south India, but small: "
         "AUM of Rs 14,492 crore (FY2025) against PNB Housing's Rs 98,000 crore and LIC "
         "Housing's far larger book. Growth is the weak point - AUM compounded 7.2% a year "
         "from Rs 11,759 crore in FY2022, and the network expansion (159 to 189 branches, 192 "
         "to 233 touchpoints over FY2023-FY2025) has not yet converted into faster book "
         "growth. Disbursements of Rs 3,284 crore in FY2025 grew only 4.8%."),
        ("Asset quality", 4, 0.25,
         "The direction is unambiguously favourable and sustained across four years - GNPA "
         "7.0% (FY2022) to 5.8% to 4.08% to 3.26% (FY2025) to 2.67% at 30-Jun-2026, all "
         "excluding interest accrued - and net NPA 1.46% to 1.32% to 1.23%. But the LEVEL "
         "remains weak for the sector: ICRA's own NBFC methodology puts HFCs at strongest "
         "below 1.5% and weakest above 5.5% on 90+ dpd, so 2.67% sits mid-band, against 0.9% "
         "for PNB Housing and 1.2% for Aptus. Two live qualifiers: the restructured pool of "
         "Rs 253.49 crore (30-Sep-2025) is still slipping - Rs 10.15 crore then Rs 15.89 "
         "crore into NPA in successive half-years - and provision coverage of 43.48% is thin, "
         "defensible only because the book is fully mortgage-secured. Non-housing loans, at "
         "27% of the book and rising, carry the higher delinquency (4.14% vs 3.93%)."),
        ("Capitalisation", 2, 0.25,
         "The clearest strength. CRAR of 37.09% at FY2025 (Tier I 36.41%) against a 15% "
         "regulatory minimum is 22 percentage points of headroom; gearing has fallen from "
         "3.94x (FY2023) to 3.01x at 30-Jun-2026 and equity funds 24.74% of the balance "
         "sheet. Net worth of Rs 4,018.65 crore supports the current book more than twice "
         "over at the HFC leverage ceiling of 12x net owned funds. Capital is not the "
         "constraint on this rating in any foreseeable case."),
        ("Earnings", 3, 0.20,
         "Headline returns are strong - RoAMA 3.00% and return on average net worth 14.16% in "
         "FY2025 - and comfortably above CareEdge's own 2.00% downgrade trigger. The "
         "qualification is what produced them. Impairment was a WRITE-BACK in each of FY2024 "
         "(Rs 0.51 crore), FY2025 (Rs 37.57 crore) and FY2026 (Rs 31.07 crore); "
         "pre-provision operating profit was Rs 524.21, Rs 549.92 and Rs 554.97 crore across "
         "those years - growth of 4.9% then 0.9%. FY2026 profit before tax of Rs 586.04 crore "
         "was FLAT on FY2025's Rs 587.49 crore and PAT rose only because a Rs 14.40 crore "
         "deferred-tax liability on the Section 36(1)(viii) special reserve was reversed. In "
         "Q1FY2027 the impairment line turned back to a charge of Rs 9.69 crore. Core "
         "earnings power is adequate and stable, not growing."),
        ("Resource profile", 5, 0.15,
         "The weakest factor and the one that most constrains the rating. At 31-Mar-2025 "
         "funding was 100% bank and NHB term borrowing - commercial paper, ECB, secured NCDs, "
         "subordinated Tier-II and public deposits all nil (AR Note 34(iv)). Twelve "
         "significant counterparties accounted for 96.69% of total liabilities and the top "
         "ten borrowings for 93.34% of total borrowings. The first NCD issuance came only in "
         "FY2026 and stood at Rs 199.19 crore at 30-Jun-2026, 1.6% of debt. Cash of Rs 142.12 "
         "crore covers 1.2% of debt, and Rs 791.11 crore of sanctioned-but-undisbursed "
         "commitments is a further near-term call. The offsets are real - LCR of 202.13%, an "
         "uninterrupted repayment record, and a book that is entirely amortising retail "
         "mortgage - but a lender with one funding channel is exposed to that channel."),
    ],
    "anchor": "AA- / A+ band",
    "view": "[ICRA]AA- (Stable) / [ICRA]A1+",
    "divergence":
        "My independent view, formed at Step 13 before any prior rating was opened for the "
        "conclusion, is [ICRA]AA- (Stable) on the long-term facilities and [ICRA]A1+ on "
        "commercial paper. The company's own FY2025 annual report (Note 32.17 and the "
        "corporate governance report) records that ICRA already rates it AA- (Stable) on "
        "long-term fund-based term loans and NCDs and A1+ on commercial paper, and CareEdge "
        "independently rates it AA-; Stable / A1+ (press release 30-Sep-2025). There is "
        "therefore NO divergence to resolve. The rating balances capitalisation that is "
        "genuinely exceptional - 37% CRAR, 3.01x gearing - and an asset-quality trajectory "
        "that has improved for four consecutive years, against a resource profile that is "
        "effectively single-channel and a franchise whose growth has not accelerated. The "
        "case for a higher grade fails on the resource profile and scale, not on capital or "
        "asset quality; the case for a lower grade fails because every adverse metric is "
        "improving and capital cover is extreme. NOTE ON THE [ICRA]AAA(SO) IN THE LIBRARY: "
        "ICRA's file dated 25-Feb-2026 titled 'Repco Home Finance Limited' rates SECURITISATION "
        "NOTES issued by the PRATHAM 12 2025 trust, backed by a pool of Repco-originated LAP "
        "receivables, on which Repco is the ORIGINATOR and servicer. [ICRA]AAA(SO) on Rs 92.80 "
        "crore of Series A1 notes and [ICRA]AA-(SO) on Rs 4.99 crore of equity-tranche notes "
        "are structured-obligation ratings on that trust's paper. Neither is Repco's issuer "
        "rating and neither has been imported here.",
}


def main():
    out = build_spreads(
        company="Repco Home Finance Limited", years=Y, inputs=INPUTS, ratios=RATIOS,
        tieouts=TIEOUTS, score=SCORE, basis="Standalone",
        out="Repco Home Finance Limited_Financial_Spreads.xlsx")
    print("Saved:", out)


if __name__ == "__main__":
    main()
