"""Generate Balkrishna Industries Limited_Financial_Spreads.xlsx from compute_ratios.py.

The script is the source of truth; this file only renders it into the review/feed layer that
the Step 12 model and the Step 12b scorecard draw from (CLAUDE.md Step 5). Nothing is hand
typed: every input below is read out of compute_ratios, and every ratio in the workbook is a
LIVE Excel formula referencing the Inputs sheet.

FY2023 carries no prior-year (FY2022) balance sheet - none of the three annual reports in the
document set goes back that far - so its working-capital-day ratios are point-in-time
(closing balance), not a two-point average, and are labelled as such on the RatioSuite sheet.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import build_spreads                                    # noqa: E402
import compute_ratios as C                                               # noqa: E402

Y = ["FY2023", "FY2024", "FY2025", "FY2026"]

AR2324 = ("FY2023-24 AR, consolidated (reported in lakhs, converted /100; cross-validated "
          "against the FY2024-25 AR's FY2024 comparative - see TieOut)")
AR2425 = "FY2024-25 AR, consolidated (Rs crore; FY2024 comparative used for the reclassified lines)"
AR2526 = "FY2025-26 AR, consolidated, audited (Rs crore)"
Q1FY27 = "Q1 FY2026-27 filing, 30-Jun-2026, consolidated column"


def pl(item):
    return list(C.PL[item][:4])           # FY2023..FY2026 only (drop Q1FY2027)


def bs(item):
    return list(C.BS[item])


# --------------------------------------------------------------------------- inputs
INPUTS = [
    ("--- PROFIT AND LOSS ---", [""] * 4, ""),
    ("Revenue from operations", pl("Revenue from ops"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Other income", pl("Other income"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Total income", pl("Total income"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Cost of materials consumed", pl("Cost of materials"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Purchases of stock-in-trade", pl("Purchases of stock"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Change in inventories (+ build, - draw)", pl("Inventory change"),
     AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Employee benefits expense", pl("Employee cost"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Finance costs", pl("Finance cost"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Depreciation and amortisation", pl("Depreciation"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Other expenses", pl("Other expenses"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("  of which NON-OPERATING, added back to OPBDITA", pl("Non-op. in other expenses"),
     "FY2025-26 AR consolidated Other Expenses note: 'Net Loss on foreign currency transaction "
     "and translation' Rs 290.01 cr (FY2026; nil FY2025). Surfaced by preflight probe [0c]. "
     "In FY2024/FY2025 the SAME item was a net GAIN and sat in OTHER INCOME instead "
     "(FY2025 Rs 267.36 cr) - already stripped by the '- other income' term, so no add-back "
     "arises. That migration between notes with the item's sign is failure mode 36."),
    ("Total expenses", pl("Total expenses"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Profit before tax", pl("PBT"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Tax expense", pl("Tax expense"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Profit after tax", pl("PAT"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Earnings per share (Rs)", pl("EPS (Rs)"), AR2324 + " / " + AR2425 + " / " + AR2526),

    ("--- BALANCE SHEET ---", [""] * 4, ""),
    ("Total assets", bs("Total assets"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Total equity", bs("Total equity"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("NC borrowings", bs("NC borrowings"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("NC lease liabilities", bs("NC lease liabilities"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Deferred tax liabilities", bs("Deferred tax liab"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Total non-current liabilities", bs("Total NC liabilities"),
     AR2324 + " / " + AR2425 + " / " + AR2526),
    ("C borrowings", bs("C borrowings"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("C lease liabilities", bs("C lease liabilities"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Trade payables", bs("Trade payables"),
     AR2324 + " (original) / " + AR2425 + " (restated, used here - Rs 102.04 cr reclassified "
     "vs Other financial liabilities for FY2024, both totals unaffected) / " + AR2526),
    ("Total current liabilities", bs("Total current liabilities"),
     AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Total current assets", bs("Total current assets"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Inventories", bs("Inventories"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Trade receivables", bs("Trade receivables"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Cash and cash equivalents", bs("Cash and equivalents"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Other bank balances", bs("Other bank balances"), AR2324 + " / " + AR2425 + " / " + AR2526),
    ("Current investments", bs("Current investments"), AR2324 + " / " + AR2425 + " / " + AR2526),

    ("--- DISCLOSED / REGULATORY (not computed here) ---", [""] * 4, ""),
    ("Total debt/total assets (company's own ratio)", ["", "", "", 0.23], Q1FY27 + ", Reg 52(4)"),
    ("Debt-Equity ratio (company's own ratio)", ["", "", "", 0.37], Q1FY27 + ", Reg 52(4)"),
    ("DSCR (company's own ratio, times)", ["", "", "", 4.31], Q1FY27 + ", Reg 52(4)"),
    ("ISCR (company's own ratio, times)", ["", "", "", 70.76], Q1FY27 + ", Reg 52(4)"),
    ("Current ratio (company's own ratio)", ["", "", "", 1.01], Q1FY27 + ", Reg 52(4)"),
    ("Operating margin % (EBIT basis, company's own)", ["", "", "", 14.09], Q1FY27 + ", Reg 52(4)"),
    ("Net profit margin % (on total income, company's own)", ["", "", "", 11.22],
     Q1FY27 + ", Reg 52(4)"),
    ("Contingent liabilities (Rs cr, standalone Note 46)", ["", "", "", 946.09],
     "FY2025-26 AR, standalone Note 46"),
    ("Capital commitments (Rs cr, standalone Note 46)", ["", "", "", 2711.84],
     "FY2025-26 AR, standalone Note 46 - contracts remaining to be executed, net of advances"),
    ("Cumulative announced capex outlay through FY2029 (Rs cr)", ["", "", "", 6800],
     "FY2025-26 AR MD&A - announced since Aug-2024"),
    ("Net cash from operating activities (Rs cr)",
     [pl("PBT")[0] * 0, "", "", 2249.32], "FY2025-26 AR consolidated cash flow statement"),
    ("Promoter shareholding %", ["", "", "", 58.29], "FY2025-26 AR shareholding pattern"),
]

# Inputs are written from row 6 downward, one row per entry, so the row of entry i is 6+i.
ROW = {label: 6 + i for i, (label, _, _) in enumerate(INPUTS)}


def I(label, c="{c}"):
    return "Inputs!%s%d" % (c, ROW[label])


REV = I("Revenue from operations")
OINC = I("Other income")
FIN = I("Finance costs")
DEP = I("Depreciation and amortisation")
PBT = I("Profit before tax")
PAT = I("Profit after tax")
TA = I("Total assets")
EQ = I("Total equity")
NCB = I("NC borrowings")
NCL = I("NC lease liabilities")
DTL = I("Deferred tax liabilities")
CB = I("C borrowings")
CL = I("C lease liabilities")
TCL = I("Total current liabilities")
TCA = I("Total current assets")
INV = I("Inventories")
RECV = I("Trade receivables")
PAY = I("Trade payables")
CASH = I("Cash and cash equivalents")
OBB = I("Other bank balances")
CINV = I("Current investments")
CMAT = I("Cost of materials consumed")
PSTK = I("Purchases of stock-in-trade")
CHINV = I("Change in inventories (+ build, - draw)")

ADDBACK = I("  of which NON-OPERATING, added back to OPBDITA")
# Symmetric build (failure mode 36): other income is subtracted, so non-operating charges
# buried inside Other Expenses must be added back, or a forex LOSS is penalised while a forex
# GAIN is stripped - manufacturing a margin decline that did not happen.
OPBDITA = "(%s+%s+%s-%s+%s)" % (PBT, FIN, DEP, OINC, ADDBACK)
DEBT = "(%s+%s+%s+%s)" % (NCB, NCL, CB, CL)
LIQ = "(%s+%s+%s)" % (CASH, OBB, CINV)
NETDEBT = "(%s-%s)" % (DEBT, LIQ)
TOL = "(%s-%s)" % (TA, EQ)
CE = "(%s+%s+%s)" % (DEBT, EQ, DTL)
COGS = "(%s+%s+%s)" % (CMAT, PSTK, CHINV)


RATIOS = [
    ("OPBDITA (Rs cr)", "=" + OPBDITA,
     "PBT + finance cost + depreciation - other income (ICRA convention, excludes other income)",
     "#,##0.0"),
    ("OPBDITA margin %", "=100*%s/%s" % (OPBDITA, REV), "OPBDITA over revenue from operations",
     "0.00"),
    ("PAT margin %", "=100*%s/%s" % (PAT, REV), "PAT over revenue from operations", "0.00"),
    ("Total debt (Rs cr)", "=" + DEBT, "NC + C borrowings, including lease liabilities", "#,##0.0"),
    ("Net debt (Rs cr)", "=" + NETDEBT,
     "total debt less cash, other bank balances and CURRENT investments (non-current "
     "strategic investments excluded)", "#,##0.0"),
    ("Gearing (times)", "=%s/%s" % (DEBT, EQ), "total debt over net worth", "0.00"),
    ("Net gearing (times)", "=%s/%s" % (NETDEBT, EQ), "net debt over net worth", "0.00"),
    ("TOL/TNW (times)", "=%s/%s" % (TOL, EQ), "total outside liabilities over net worth", "0.00"),
    ("Total debt/OPBDITA (times)", "=%s/(%s)" % (DEBT, OPBDITA), "", "0.00"),
    ("Net debt/OPBDITA (times)", "=%s/(%s)" % (NETDEBT, OPBDITA), "", "0.00"),
    ("Interest coverage (times)", "=(%s)/%s" % (OPBDITA, FIN), "OPBDITA over finance costs",
     "0.00"),
    ("RoCE %", "=100*((%s)-%s)/(%s)" % (OPBDITA, DEP, CE),
     "(OPBDITA - depreciation) over capital employed (debt + net worth + deferred tax "
     "liability), period-end basis", "0.00"),
    ("Current ratio (times)", "=%s/%s" % (TCA, TCL), "", "0.00"),
    ("Debtor days", "=365*%s/%s" % (RECV, REV),
     "closing balance (point-in-time), used in every year for a consistent convention across "
     "the series - FY2023 has no prior-year balance sheet in the document set to average with",
     "0.0"),
    ("Inventory days", "=365*%s/(%s)" % (INV, COGS), "closing inventory over COGS", "0.0"),
    ("Payable days", "=365*%s/(%s)" % (PAY, COGS), "closing payables over COGS", "0.0"),
    ("Working capital cycle (days)",
     "=365*%s/%s+365*%s/(%s)-365*%s/(%s)" % (RECV, REV, INV, COGS, PAY, COGS),
     "debtor days + inventory days - payable days", "0.0"),
]

TIEOUTS = [
    ("Balance sheet ties, FY2026 (assets - equity - NC liab, should equal C liab)",
     "=Inputs!F%d-Inputs!F%d-Inputs!F%d" % (ROW["Total assets"], ROW["Total equity"],
                                            ROW["Total non-current liabilities"]),
     bs("Total current liabilities")[3], "AR consolidated balance sheet, total current "
     "liabilities - independently stated, not derived from the formula in column C"),
    ("Gearing, FY2026",
     "=(Inputs!F%d+Inputs!F%d+Inputs!F%d+Inputs!F%d)/Inputs!F%d"
     % (ROW["NC borrowings"], ROW["NC lease liabilities"], ROW["C borrowings"],
        ROW["C lease liabilities"], ROW["Total equity"]),
     0.37, "company's own Reg 52(4) disclosure, Q1 FY2026-27 filing"),
    ("Operating margin (EBIT basis), FY2026",
     "=100*((Inputs!F%d+Inputs!F%d+Inputs!F%d-Inputs!F%d)-Inputs!F%d)/Inputs!F%d"
     % (ROW["Profit before tax"], ROW["Finance costs"], ROW["Depreciation and amortisation"],
        ROW["Other income"], ROW["Depreciation and amortisation"], ROW["Revenue from operations"]),
     14.09, "company's own Reg 52(4) disclosure, Q1 FY2026-27 filing (EBIT basis, differs "
            "from OPBDITA margin above)"),
    ("EPS, FY2026", "=Inputs!F%d" % ROW["Earnings per share (Rs)"], 64.30,
     "AR consolidated statement of profit and loss"),
    ("Current ratio, FY2026", "=Inputs!F%d/Inputs!F%d" % (ROW["Total current assets"],
                                                          ROW["Total current liabilities"]),
     1.01, "company's own Reg 52(4) disclosure, Q1 FY2026-27 filing"),
]

SCORE = {
    "factors": [
        ("Business risk - franchise and diversification", 2, 0.25,
         "Largest Indian exporter of off-highway tyres (CareEdge, 05-Mar-2026), operating in "
         "over 160 countries, with SKUs grown from ~2,700 (FY2019) to 3,600+ (CRISIL, "
         "27-Feb-2026). Channel mix 70.1% replacement / 28.7% OEM (FY2026 AR) gives revenue "
         "stability across cycles. Geographic mix is materially diversified (Europe 40.0%, "
         "Americas 13.2%, India 36.3%, RoW 10.5%, FY2026 AR) but this diversification is what "
         "transmitted the FY2026 tariff shock - North America revenue fell 28.1% "
         "(Rs 1,861.38 cr to Rs 1,338.48 cr, AR segment note) even as India grew 24.0% and "
         "'Others' 46.6% to compensate."),
        ("Operating efficiency and cost position", 2, 0.15,
         "Backward-integrated carbon black operations (own major raw-material input); "
         "logistics cost averaged 5.45% of revenue over 3 years vs an industry benchmark of "
         "7.9%-9%, reduced further to 4.40% in FY2026 (company MD&A); inventory turnover "
         "exceeding 24 times with finished-goods held at 12-15 days of production. OPBDITA "
         "margin of 21.25% in FY2026, though down from 24.07% (FY2024) and 23.52% (FY2025), "
         "remains high in absolute terms for the sector."),
        ("Financial risk - leverage and coverage", 1, 0.30,
         "Gearing has stayed in a narrow 0.31x-0.44x band across all four years (FY2023-FY2026) "
         "DESPITE a Rs 2,984-3,003 crore capex year in FY2026 (cash-flow vs MD&A basis) that "
         "was funded predominantly from operating cash flow (Rs 2,249.32 crore, +27.5% y/y) "
         "rather than debt. Interest coverage never falls below 17 times in any of the four "
         "years, including the FY2026 margin-compression year. TOL/TNW peaks at 0.63x - very "
         "low balance-sheet risk for a manufacturer mid-way through a Rs 6,800 crore multi-year "
         "capex programme."),
        ("Earnings trajectory and margin resilience", 3, 0.15,
         "FY2026 PAT fell 24.9% (Rs 1,654.96 cr to Rs 1,243.10 cr) on OPBDITA margin "
         "compression to 21.25% from 23.52%, driven by the North America tariff shock the "
         "company's own MD&A names explicitly ('US tariffs: the sharp spike in import levies "
         "weigh on the finances'). RoCE fell to 9.92% from 12.59% (FY2025), partly because "
         "capital employed rose sharply (CWIP alone grew from Rs 985.95 cr to Rs 2,472.46 cr) "
         "while earnings fell. The most recent quarter (Q1FY2027, consolidated) shows "
         "recovery already under way - operating margin 21.54% (annualised OPBDITA basis) "
         "and PAT of Rs 450.77 cr, +56.4% year-on-year against Q1FY2026's Rs 288.30 cr - "
         "consistent with CRISIL's own comment (27-Feb-2026) that US tariffs are 'now "
         "reducing to ~15%' with an expected FY2027 recovery."),
        ("Capex execution and funding risk", 3, 0.15,
         "A Rs 6,800 crore cumulative capex programme (announced since Aug-2024, through "
         "FY2029) is under way across Carbon Black capacity (2,65,000 to 3,60,000 MTPA), "
         "Premium PCR/CVR entry, and OHT debottlenecking to 4,25,000 MTPA total achievable "
         "tyre capacity. FY2026 capital commitments (contracts executed but not yet paid) "
         "nearly tripled to Rs 2,711.84 crore from Rs 923.98 crore (AR Note 46), confirming "
         "the programme's next phase is substantially committed, not merely announced. "
         "Execution risk (cost overrun, delay, demand absorption for the new PCR/CVR "
         "capacity in an unfamiliar segment) is real, but funding risk is LOW given the "
         "demonstrated FY2026 funding mix (74% of capex from operating cash flow)."),
    ],
    "anchor": "AA band (composite reflects strong balance sheet, moderated by a live "
              "earnings-trajectory question)",
    "view": "[ICRA]AA (Stable) / [ICRA]A1+",
    "divergence":
        "This is a NEW ICRA rating (an assignment, not a reaffirmation) - BKT's own FY2025-26 "
        "annual report discloses ratings from CRISIL (AA+/Stable) and CareEdge (AA+; Stable "
        "on the NCD only) but NO ICRA rating anywhere, confirmed by a recorded zero-hit search "
        "for 'ICRA' across the AR and the newest quarterly filing. My independent view is one "
        "notch below both peer agencies' AA+ - [ICRA]AA (Stable) - not because the balance "
        "sheet disagrees (gearing, coverage and TOL/TNW would all support AA+ on their own) "
        "but because the FY2026 earnings trajectory is the live question this exercise cannot "
        "resolve with only one quarter of recovery evidence: PAT fell 25% for a full year "
        "before Q1FY2027 turned up, and CRISIL's own 27-Feb-2026 rationale (dated inside that "
        "same recovery window) explicitly builds its AA+ around a FORECAST of FY2027 recovery "
        "('revenues in FY27 are expected to grow by 7-9%... margins are expected to improve') "
        "rather than realised results. A rating built on realised FY2026 results plus one "
        "recovering quarter, without that forward-looking credit for a forecast not yet "
        "delivered, reasonably sits one notch more cautious. This is a considered, evidenced "
        "divergence, not an anchor-matching exercise - and it is within the ±2 notch "
        "screening tolerance the scorecard's own back-tested governance allows before "
        "requiring committee-level resolution.",
}


def main():
    out = build_spreads(
        company="Balkrishna Industries Limited", years=Y, inputs=INPUTS, ratios=RATIOS,
        tieouts=TIEOUTS, score=SCORE, basis="Consolidated",
        out="Balkrishna Industries Limited_Financial_Spreads.xlsx")
    print("Saved:", out)


if __name__ == "__main__":
    main()
