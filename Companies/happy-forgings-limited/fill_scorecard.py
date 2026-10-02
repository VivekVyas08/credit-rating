# Fills Rating_Scorecard_Happy Forgings.xlsx Inputs sheet from compute_ratios.py's
# verified figures + broker-consensus projection assumptions (labelled as such).
# Every historical cell traces to compute_ratios.py / the workpaper; nothing retyped
# from memory. Source: Happy_Forgings_Ratio_Workpaper_11Aug2026.md.
import openpyxl

PATH = "Rating_Scorecard_Happy Forgings.xlsx"
wb = openpyxl.load_workbook(PATH, data_only=False)
ws = wb["Inputs"]

ws["C4"] = "Happy Forgings Limited"
ws["C5"] = "CRISIL"
ws["C6"] = "Auto components"
ws["C7"] = "11-Aug-2026"

# Historical financials, Rs crore, standalone (compute_ratios.py DATA / workpaper table)
hist = {
    12: ("Total operating income",        1358.24, 1408.89, 1546.34),
    13: ("EBITDA (OPBDITA)",              388,     407,     471),
    14: ("Depreciation & amortisation",    64.73,   77.06,   89.04),
    15: ("Interest expense",               11.78,    7.53,   10.47),
    16: ("Profit after tax (PAT)",        242.99,  267.57,  301.64),
    17: ("Total debt (incl. leases; nil term debt, all revolving WC)", 143.31, 227.29, 329.62),
    18: ("Cash & liquid investments",     121.73,  216.12,  289.88),
    19: ("Tangible net worth",           1612.49, 1849.69, 2128.28),
    20: ("Total outside liabilities (Total assets - equity)", 273.46, 364.95, 504.68),
    21: ("Current assets",                741.65,  918.60, 1070.99),
    22: ("Current liabilities",           241.83,  325.63,  455.69),
    23: ("Capital expenditure",           194,     281,     461),
    24: ("Dividends paid",                 37.68,   37.68,   28.28),
}
for row, (_label, fy24, fy25, fy26) in hist.items():
    ws[f"C{row}"] = fy24
    ws[f"D{row}"] = fy25
    ws[f"E{row}"] = fy26

# Projection assumptions FY+1/FY+2 (FY2027/FY2028) - BLENDED BROKER CONSENSUS
# (ICICI Securities + Motilal Oswal, both 05-Aug-2026), explicitly labelled as broker
# view in the workpaper/rationale, never company-disclosed fact. Not linked to a
# plugin-built 5-yr model in this pass (see workpaper Sec 6, item 2 - deferred).
ws["C29"], ws["D29"] = 0.25, 0.22       # Revenue growth: ICICI ~24-31%/21%, MOSL ~30%+ - blended, conservative of the two
ws["C30"], ws["D30"] = 0.31, 0.315      # EBITDA margin: ICICI 30.5/31.2%, MOSL ~31.7/32% - blended
ws["C31"], ws["D31"] = 380, 400         # Capex: ICICI FY27E ~Rs 350cr cashflow-tab figure, broker capex guidance ~Rs 350-400cr FY27/28
ws["C32"], ws["D32"] = 50, 40           # Net new debt: modest WC growth in line with revenue (co. has no term debt/no capex debt-funding history)
ws["C33"], ws["D33"] = 0.07, 0.07       # Avg interest rate: within Note 14A's disclosed WC facility rate bands (5.5-9.3%)
ws["C34"], ws["D34"] = 0.25, 0.25       # Tax rate: matches 3-yr historical effective rate (~25%)
ws["C35"], ws["D35"] = 0.125, 0.125     # Dividend payout: matches co.'s FY26 payout and broker DPS/EPS ratio (~12.5%)

# Qualitative assessment - justified against CRISIL Section VII "Auto component suppliers"
# factor language (see workpaper Methodology Compliance Map)
ws["C39"] = None   # Industry risk: accept sector base (Auto components = 3.5, Ref_Weights)
ws["C40"] = 2       # Business risk/market position: 2nd-largest CV/industrial crankshaft
                     # producer in India, high product complexity (0.005mm tolerances),
                     # diversified end-segment/geography mix - strong but not top-tier
                     # absolute scale vs large diversified peers (RKFL/CAL)
ws["C41"] = 2       # Management/governance: clean unqualified audit opinion (single
                     # standard KAM), 50% independent board, no promoter pledge, capex
                     # funded 92% from internal accruals over FY21-26 (capital discipline)
ws["C42"] = 0       # Parent/group support: not applicable, no parent
ws["C43"] = "Strong"  # Liquidity: matches workpaper Sec 7 sources-vs-claims conclusion
ws["C44"] = "Stable"  # Outlook: matches rationale's independent view

wb.save(PATH)
print("Inputs sheet filled and saved:", PATH)
