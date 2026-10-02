# Happy Forgings Limited - 5-year 3-statement model (CLAUDE.md Step 12).
# All historical figures traced to compute_ratios.py / the workpaper (audited AR).
# FY27-28 projection assumptions are BLENDED BROKER CONSENSUS (ICICI Securities +
# Motilal Oswal, both 05-Aug-2026), same as fed into the scorecard's Inputs sheet.
# FY29-31 are THIS ANALYSIS'S OWN JUDGMENT (fade pattern beyond the brokers' 2-3yr
# horizon) - explicitly labelled, never presented as company or broker fact.
# Values are computed once in Python (this script = source of truth) and written as
# literal numbers into the workbook, per this project's Financial_Spreads convention -
# avoids Excel-formula caching risk for a presentation/computation workbook.
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

HIST_YEARS = ["FY2024", "FY2025", "FY2026"]
PROJ_YEARS = ["FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E"]
ALL_YEARS = HIST_YEARS + PROJ_YEARS

# ---------------------------------------------------------------- historical (Rs cr)
H = {
    "revenue":       [1358.24, 1408.89, 1546.34],
    "ebitda":        [388, 407, 471],
    "depreciation":  [64.73, 77.06, 89.04],
    "interest":      [11.78, 7.53, 10.47],
    "other_income":  [13.36, 37.57, 30.81],
    "pat":           [242.99, 267.57, 301.64],
    "debt":          [143.31, 227.29, 329.62],
    "cash_liquid":   [121.73, 216.12, 289.88],
    "equity":        [1612.49, 1849.69, 2128.28],
    "total_assets":  [1885.95, 2214.64, 2632.96],
    "dtl":           [31.62, 39.33, 48.99],
    "cwip":          [121.94, 116.28, 229.31],
    "capex":         [194, 281, 461],
    "dividend":      [37.68, 37.68, 28.28],
    "receivables":   [356.92, 426.54, 394.78],
    "inventory":     [224.17, 232.42, 232.76],
    "payables":      [55.53, 45.36, 59.43],
    "curr_assets":   [741.65, 918.60, 1070.99],
    "curr_liab":     [241.83, 325.63, 455.69],
}

# ------------------------------------------------------ projection assumptions
REV_GROWTH   = [0.25, 0.22, 0.18, 0.15, 0.13]   # FY27-28 broker blend; FY29-31 own fade judgment
EBITDA_MGN   = [0.310, 0.315, 0.315, 0.310, 0.310]
CAPEX        = [380, 400, 350, 300, 280]         # FY27-28 broker guidance; FY29-31 post-ramp taper (own judgment)
NET_NEW_DEBT = [50, 40, 30, 20, 10]              # modest WC-linked growth; co. has zero term-debt history
INT_RATE     = 0.07                               # within Note 14A's disclosed WC facility rate bands (5.5-9.3%)
TAX_RATE     = 0.25
DIV_PAYOUT   = 0.125
DEP_PCT_OF_GROSS_BLOCK_GROWTH = 0.12             # depreciation scales with capex-driven asset base growth

# end-market / geography mix (latest disclosed, FY26/Q1FY27) - held flat through the
# projection window (no company guidance on mix drift beyond "Industrial to double in
# 3-4 yrs" qualitative steer, which is NOT quantified into these numbers - see model notes)
MIX = {
    "Commercial Vehicles": 0.37, "Farm Equipment": 0.32, "Off-Highway": 0.11,
    "Industrials": 0.14, "Passenger Vehicles": 0.06,  # FY26; sums to exactly 1.00 - validated
}
GEO_MIX = {"Domestic": 0.74, "Direct exports": 0.15, "Deemed/indirect exports": 0.11}
# A mix that does not sum to 100% is a MIS-READ, not rounding (icra-doc-extract PATTERNS.md).
# This assert is the cheap validator that would have caught the 11-Aug-2026 CV mis-alignment.
assert abs(sum(MIX.values()) - 1.0) < 0.005, f"segment mix must sum to 100%, got {sum(MIX.values()):.1%}"
assert abs(sum(GEO_MIX.values()) - 1.0) < 0.005, f"geography mix must sum to 100%, got {sum(GEO_MIX.values()):.1%}"

# ---------------------------------------------------------------- compute P&L
revenue = list(H["revenue"])
for g in REV_GROWTH:
    revenue.append(round(revenue[-1] * (1 + g), 1))

ebitda = list(H["ebitda"])
for i, m in enumerate(EBITDA_MGN):
    ebitda.append(round(revenue[3 + i] * m, 1))

gross_block_growth = [0] * 3 + [round(c * DEP_PCT_OF_GROSS_BLOCK_GROWTH, 1) for c in CAPEX]
depreciation = list(H["depreciation"])
for i in range(5):
    depreciation.append(round(depreciation[-1] + gross_block_growth[3 + i], 1))

debt = list(H["debt"])
for d in NET_NEW_DEBT:
    debt.append(round(debt[-1] + d, 1))

interest = list(H["interest"])
for i in range(5):
    avg_debt = (debt[2 + i] + debt[3 + i]) / 2
    interest.append(round(avg_debt * INT_RATE, 1))

other_income = list(H["other_income"])
for i in range(5):
    other_income.append(round(other_income[-1] * 1.05, 1))  # modest growth on treasury income, own assumption

pbt = [ebitda[i] - depreciation[i] - interest[i] + other_income[i] for i in range(8)]
tax = [round(p * TAX_RATE, 1) if i < 3 else round(p * TAX_RATE, 1) for i, p in enumerate(pbt)]
pat = [round(pbt[i] - tax[i], 1) for i in range(8)]
# overwrite historical PAT with actual reported (tax rate varies slightly historically)
pat[0], pat[1], pat[2] = H["pat"]
tax[0] = round(pbt[0] - pat[0], 1)
tax[1] = round(pbt[1] - pat[1], 1)
tax[2] = round(pbt[2] - pat[2], 1)

dividend = list(H["dividend"])
for i in range(5):
    dividend.append(round(pat[3 + i] * DIV_PAYOUT, 1))

capex_all = list(H["capex"]) + CAPEX

equity = list(H["equity"])
for i in range(5):
    equity.append(round(equity[-1] + pat[3 + i] - dividend[3 + i], 1))

cash_liquid = list(H["cash_liquid"])
for i in range(5):
    ocf = pat[3 + i] + depreciation[3 + i]  # simplified indirect-method proxy (no WC build below)
    ending_cash = cash_liquid[-1] + ocf - capex_all[3 + i] - dividend[3 + i] + NET_NEW_DEBT[i]
    cash_liquid.append(round(max(ending_cash, 0), 1))

# ---------------------------------------------------------------- workbook
wb = openpyxl.Workbook()
wb.remove(wb.active)

NAVY = "1B2A4A"
TEAL = "0E7C86"
HDR_FILL = PatternFill("solid", fgColor=NAVY)
HDR_FONT = Font(color="FFFFFF", bold=True)
PROJ_FILL = PatternFill("solid", fgColor="FFF6E5")
LABEL_FONT = Font(bold=True)
NOTE_FONT = Font(italic=True, size=9, color="666666")
thin = Side(style="thin", color="DDDDDD")
BORDER = Border(top=thin, bottom=thin, left=thin, right=thin)


def write_header(ws, title, note, start_row=1):
    ws["B" + str(start_row)] = title
    ws["B" + str(start_row)].font = Font(bold=True, size=14, color=NAVY)
    if note:
        ws["B" + str(start_row + 1)] = note
        ws["B" + str(start_row + 1)].font = NOTE_FONT
    return start_row + 3


def write_year_row(ws, row, years=ALL_YEARS, start_col=3):
    for i, y in enumerate(years):
        c = ws.cell(row=row, column=start_col + i, value=y)
        c.font = HDR_FONT
        c.fill = HDR_FILL
        c.alignment = Alignment(horizontal="center")
        if y.endswith("E"):
            pass  # projected years get PROJ_FILL applied per-data-row below


def write_data_row(ws, row, label, values, start_col=3, fmt="#,##0.0", bold=False, pct=False):
    lc = ws.cell(row=row, column=2, value=label)
    if bold:
        lc.font = LABEL_FONT
    for i, v in enumerate(values):
        c = ws.cell(row=row, column=start_col + i, value=v)
        c.number_format = "0.0%" if pct else fmt
        c.border = BORDER
        if start_col + i - 3 >= len(HIST_YEARS):
            c.fill = PROJ_FILL
        if bold:
            c.font = LABEL_FONT


def autosize(ws, widths):
    for col, w in widths.items():
        ws.column_dimensions[col].width = w


# ============================================================== 1. Revenue Model
ws = wb.create_sheet("Revenue Model")
r = write_header(ws, "Revenue Model - Happy Forgings Limited",
                  "End-market and geography mix held at latest disclosed FY26/Q1FY27 levels through the "
                  "projection window (no quantified company guidance on mix drift beyond qualitative steers "
                  "e.g. 'Industrial to double in 3-4 yrs' - NOT built into these numbers, flagged as upside optionality only).")
write_year_row(ws, r)
r += 1
write_data_row(ws, r, "Total revenue (Rs crore)", revenue, bold=True); r += 2
ws.cell(row=r, column=2, value="By end-market (mix x total revenue)").font = LABEL_FONT; r += 1
for seg, pct in MIX.items():
    write_data_row(ws, r, seg, [round(v * pct, 1) for v in revenue]); r += 1
r += 1
ws.cell(row=r, column=2, value="By geography (mix x total revenue)").font = LABEL_FONT; r += 1
for geo, pct in GEO_MIX.items():
    write_data_row(ws, r, geo, [round(v * pct, 1) for v in revenue]); r += 1
r += 1
write_data_row(ws, r, "Revenue growth %", [None, None, None] + REV_GROWTH, pct=True); r += 1
autosize(ws, {"A": 2, "B": 34, "C": 12, "D": 12, "E": 12, "F": 12, "G": 12, "H": 12, "I": 12})

# ============================================================== 2. Income Statement
ws = wb.create_sheet("Income Statement")
r = write_header(ws, "Income Statement (Rs crore, standalone)",
                  "FY24-26 audited (AR). FY27-28 assumptions blended from ICICI Securities + Motilal Oswal "
                  "broker notes (05-Aug-2026). FY29-31 are this analysis's own fade-pattern judgment, not "
                  "company or broker fact - see Scenarios tab for the range this could fall in.")
write_year_row(ws, r); r += 1
write_data_row(ws, r, "Revenue from operations", revenue, bold=True); r += 1
write_data_row(ws, r, "Other income", other_income); r += 1
total_income = [revenue[i] + other_income[i] for i in range(8)]
write_data_row(ws, r, "Total income", total_income, bold=True); r += 2
write_data_row(ws, r, "EBITDA (OPBDITA)", ebitda, bold=True); r += 1
write_data_row(ws, r, "EBITDA margin %", [ebitda[i] / revenue[i] for i in range(8)], pct=True); r += 1
write_data_row(ws, r, "Depreciation & amortisation", depreciation); r += 1
ebit = [ebitda[i] - depreciation[i] for i in range(8)]
write_data_row(ws, r, "EBIT", ebit, bold=True); r += 1
write_data_row(ws, r, "Finance costs", interest); r += 1
write_data_row(ws, r, "Profit before tax", pbt, bold=True); r += 1
write_data_row(ws, r, "Tax expense", tax); r += 1
write_data_row(ws, r, "Profit after tax", pat, bold=True); r += 1
write_data_row(ws, r, "PAT margin %", [pat[i] / revenue[i] for i in range(8)], pct=True); r += 1
write_data_row(ws, r, "Dividend paid", dividend); r += 1
autosize(ws, {"A": 2, "B": 30, "C": 12, "D": 12, "E": 12, "F": 12, "G": 12, "H": 12, "I": 12})

# ============================================================== 3. Balance Sheet
ws = wb.create_sheet("Balance Sheet")
r = write_header(ws, "Balance Sheet (Rs crore, standalone)",
                  "FY24-26 audited (AR). Projected years derived from the Income Statement + Cash Flow tabs; "
                  "zero non-current/term debt assumption is held through the projection (matches co.'s "
                  "3-year unbroken track record and CARO 'no term loans' disclosure).")
write_year_row(ws, r); r += 1
ws.cell(row=r, column=2, value="Equity & Liabilities").font = LABEL_FONT; r += 1
write_data_row(ws, r, "Total equity", equity, bold=True); r += 1
write_data_row(ws, r, "Non-current borrowings", [0] * 8); r += 1
write_data_row(ws, r, "Current borrowings", debt); r += 1
write_data_row(ws, r, "Deferred tax liabilities", H["dtl"] + [round(H["dtl"][-1] * (1 + 0.06 * i), 1) for i in range(1, 6)]); r += 1
tol_proj = [equity[i] * 0.24 for i in range(3, 8)]   # held at FY26's TOL/equity ratio - own simplifying assumption
curr_liab_all = list(H["curr_liab"]) + [round(v, 1) for v in tol_proj]
write_data_row(ws, r, "Total current liabilities (incl. current borrowings)", curr_liab_all); r += 1
ws.cell(row=r, column=2, value="Note: FY24-26 = actual current liabilities (AR); FY27E-31E is a TOL/equity-ratio "
                               "proxy for ALL liabilities beyond equity (current+non-current combined) used to "
                               "balance the plugged Balance Sheet - the Current borrowings and DTL rows above are "
                               "subsets already inside this total, not additive to it. Credit Ratios tab computes "
                               "gearing/coverage directly from the Debt/Equity/EBITDA figures, NOT from this plug.").font = NOTE_FONT
r += 2
ws.cell(row=r, column=2, value="Assets").font = LABEL_FONT; r += 1
write_data_row(ws, r, "Cash & liquid investments", cash_liquid); r += 1
cwip_proj = [round(H["cwip"][-1] * 0.6, 1)] * 5  # tapering as heavy-forging capacity is commissioned FY27-28
cwip_all = list(H["cwip"]) + cwip_proj
write_data_row(ws, r, "Capital work-in-progress", cwip_all); r += 1
net_block = [None, None, None]
gross_block_est = 1097.0  # FY26 net PP&E per AR, Rs crore, as base
for i in range(5):
    gross_block_est = gross_block_est + capex_all[3 + i] - depreciation[3 + i]
    net_block.append(round(gross_block_est, 1))
write_data_row(ws, r, "Net PP&E (estimated roll-forward)", net_block); r += 1
curr_assets_all = list(H["curr_assets"]) + [round(equity[i] + curr_liab_all[i] - net_block[i] - cwip_all[i] - cash_liquid[i], 1) for i in range(3, 8)]
write_data_row(ws, r, "Other current assets (plug: receivables+inventory+other)", curr_assets_all); r += 1
total_assets_all = [round(net_block[i] + cwip_all[i] + cash_liquid[i] + curr_assets_all[i], 1) if i >= 3 else H["total_assets"][i] for i in range(8)]
write_data_row(ws, r, "Total assets", total_assets_all, bold=True); r += 1
autosize(ws, {"A": 2, "B": 42, "C": 12, "D": 12, "E": 12, "F": 12, "G": 12, "H": 12, "I": 12})

# ============================================================== 4. Cash Flow Statement
ws = wb.create_sheet("Cash Flow Statement")
r = write_header(ws, "Cash Flow Statement (Rs crore, standalone, simplified indirect method)",
                  "FY24-26 audited (AR). Projected years: PAT + depreciation as operating-cash proxy (no "
                  "working-capital build modelled explicitly - a simplification flagged here, not hidden; "
                  "the company's actual FY24-26 OCF/EBITDA ratio ranged 49-94% reflecting real WC swings "
                  "this proxy does not capture).")
write_year_row(ws, r); r += 1
ocf_hist = [189, 292, 445]  # Rs crore, from Q1FY27 deck cumulative table (co.-disclosed, cross-checked)
ocf_proj = [round(pat[3 + i] + depreciation[3 + i], 1) for i in range(5)]
ocf_all = ocf_hist + ocf_proj
write_data_row(ws, r, "Net cash from operating activities", ocf_all, bold=True); r += 1
write_data_row(ws, r, "Capital expenditure", [-c for c in capex_all]); r += 1
write_data_row(ws, r, "Net new debt raised / (repaid)", [None, None, None] + NET_NEW_DEBT); r += 1
write_data_row(ws, r, "Dividend paid", [-d for d in dividend]); r += 1
fcf = [ocf_all[i] - capex_all[i] for i in range(8)]
write_data_row(ws, r, "Free cash flow (OCF - capex)", fcf, bold=True); r += 2

# ---- FUNDING-GAP DERIVATION (CLAUDE.md failure mode 18: derive the debt path, never
# assume it from the historical pattern; write the arithmetic down so a divergent view
# is visible rather than buried in a smooth assumption) ----
ws.cell(row=r, column=2, value="Funding-gap derivation (external funding need = capex + dividend - OCF)").font = LABEL_FONT
r += 1
funding_gap = [round(capex_all[i] + dividend[i] - ocf_all[i], 1) for i in range(8)]
write_data_row(ws, r, "  External funding need (+) / surplus (-)", funding_gap); r += 1
write_data_row(ws, r, "  Net new debt assumed in this model", [None, None, None] + NET_NEW_DEBT); r += 1
implied_cash = [round((NET_NEW_DEBT[i - 3] if i >= 3 else 0) - funding_gap[i], 1) for i in range(8)]
write_data_row(ws, r, "  Implied cash build (+) / drawdown (-)", [None, None, None] + implied_cash[3:]); r += 2
ws.cell(row=r, column=2, value=(
    "SENSITIVITY (stated explicitly, not buried): this model's base case has internal accrual covering "
    "the capex programme with only Rs {} crore of cumulative new debt over FY27-28. A view that assumes "
    "less internal funding - e.g. a heavier or faster-drawn capex, or working-capital absorption this "
    "simplified OCF proxy does not capture - produces a materially larger debt build. For reference, the "
    "rating agency's own published view on comparable capex assumed ~Rs 300 crore of incremental debt. "
    "Neither path changes the grade (gearing stays below 0.3x on both), but the arithmetic is shown here "
    "so the divergence is visible and testable rather than implicit."
).format(sum(NET_NEW_DEBT[:2]))).font = NOTE_FONT
r += 1
autosize(ws, {"A": 2, "B": 44, "C": 12, "D": 12, "E": 12, "F": 12, "G": 12, "H": 12, "I": 12})

# ============================================================== 5. Scenarios
ws = wb.create_sheet("Scenarios")
r = write_header(ws, "Scenarios - Bull / Base / Bear (FY2028E, Rs crore)",
                  "Base case = this model's Income Statement. Bull/Bear flex the two variables CRISIL's own "
                  "methodology names as central to this sector: revenue growth (order-book execution / demand "
                  "cyclicality) and EBITDA margin (mix/pass-through/competitive intensity). Own construction, "
                  "not broker- or company-sourced.")
scen_years = ["FY2027E", "FY2028E"]
write_year_row(ws, r, years=scen_years); r += 1
scenarios = {
    "Bull (order-book converts faster, richer mix)": (0.30, 0.27, 0.325, 0.335),
    "Base (this model)": (REV_GROWTH[0], REV_GROWTH[1], EBITDA_MGN[0], EBITDA_MGN[1]),
    "Bear (CV/farm demand slows, export tariff/FX shock)": (0.12, 0.08, 0.275, 0.26),
}
for name, (g1, g2, m1, m2) in scenarios.items():
    ws.cell(row=r, column=2, value=name).font = LABEL_FONT; r += 1
    rev1 = revenue[2] * (1 + g1)
    rev2 = rev1 * (1 + g2)
    write_data_row(ws, r, "  Revenue growth %", [g1, g2], pct=True); r += 1
    write_data_row(ws, r, "  Revenue (Rs cr)", [round(rev1, 1), round(rev2, 1)]); r += 1
    write_data_row(ws, r, "  EBITDA margin %", [m1, m2], pct=True); r += 1
    write_data_row(ws, r, "  EBITDA (Rs cr)", [round(rev1 * m1, 1), round(rev2 * m2, 1)]); r += 2
autosize(ws, {"A": 2, "B": 46, "C": 14, "D": 14})

# ============================================================== 6. DCF Inputs
ws = wb.create_sheet("DCF Inputs")
r = write_header(ws, "DCF Inputs (Rs crore unless stated) - financial-flexibility context only, NOT the rating driver",
                  "Per CLAUDE.md Step 12(f): valuation informs financial flexibility (market-cap cushion) only, "
                  "never the credit grade. WACC/beta not independently derived - flagged as a gap; broker target "
                  "prices (ICICI Rs 2,200, Motilal Oswal Rs 2,095) are shown as attributed market context instead "
                  "of building an unsupported discount-rate assumption from scratch.")
write_year_row(ws, r, years=PROJ_YEARS); r += 1
ebit_proj = ebit[3:]
nopat = [round(e * (1 - TAX_RATE), 1) for e in ebit_proj]
write_data_row(ws, r, "EBIT", ebit_proj); r += 1
write_data_row(ws, r, "NOPAT (EBIT x (1-tax))", nopat); r += 1
write_data_row(ws, r, "+ Depreciation", depreciation[3:]); r += 1
write_data_row(ws, r, "- Capex", [-c for c in CAPEX]); r += 1
ufcf = [round(nopat[i] + depreciation[3 + i] - CAPEX[i], 1) for i in range(5)]
write_data_row(ws, r, "Unlevered FCF", ufcf, bold=True); r += 2
ws.cell(row=r, column=2, value="Market context (broker-attributed, NOT this analysis's valuation)").font = LABEL_FONT; r += 1
ws.cell(row=r, column=2, value="Market cap (CMP Rs 1,817, per both brokers 05-Aug-2026)"); ws.cell(row=r, column=3, value="Rs 171bn / $1.8bn"); r += 1
ws.cell(row=r, column=2, value="ICICI Securities TP (40x Sep'28E EPS)"); ws.cell(row=r, column=3, value="Rs 2,200 (+21%)"); r += 1
ws.cell(row=r, column=2, value="Motilal Oswal TP (33x FY28E EPS)"); ws.cell(row=r, column=3, value="Rs 2,095 (+15%)"); r += 1
autosize(ws, {"A": 2, "B": 50, "C": 14, "D": 14, "E": 14, "F": 14, "G": 14})

# ============================================================== 7. Credit Ratios (CRISIL convention)
ws = wb.create_sheet("Credit Ratios")
r = write_header(ws, "Credit Ratios (CRISIL convention, all years by computation)",
                  "Matches criteria-for-manufacturing-trading-and-corporate-services-sector.md Section IV. "
                  "All historical years tie to compute_ratios.py; projected years computed from this model's "
                  "Income Statement/Balance Sheet above.")
write_year_row(ws, r); r += 1
gearing = [debt[i] / equity[i] for i in range(8)]
write_data_row(ws, r, "Gearing (adj. debt / adj. networth)", gearing, fmt="0.00\"x\""); r += 1
int_cov = [ebitda[i] / interest[i] if interest[i] else None for i in range(8)]
write_data_row(ws, r, "Interest coverage (EBITDA/finance cost)", int_cov, fmt="0.0\"x\""); r += 1
tol_tnw = [0.17, 0.20, 0.24] + [tol_proj[i] / equity[3 + i] for i in range(5)]
write_data_row(ws, r, "TOL/TNW", tol_tnw, fmt="0.00\"x\""); r += 1
td_ebitda = [debt[i] / ebitda[i] for i in range(8)]
write_data_row(ws, r, "Total debt/EBITDA", td_ebitda, fmt="0.00\"x\""); r += 1
gca_days_hist = [199, 238, 253]
gca_days_proj = [253] * 5  # held at FY26 level - own simplifying assumption, flagged
gca_days_all = gca_days_hist + gca_days_proj
gca_all = [revenue[i] * gca_days_all[i] / 365 for i in range(8)]
td_gca = [debt[i] / gca_all[i] for i in range(8)]
write_data_row(ws, r, "Total debt/GCA", td_gca, fmt="0.00\"x\""); r += 1
current_ratio = [3.07, 2.82, 2.35] + [(curr_assets_all[3 + i] + cash_liquid[3 + i]) / curr_liab_all[3 + i] for i in range(5)]
write_data_row(ws, r, "Current ratio", current_ratio, fmt="0.00\"x\""); r += 1
net_debt = [debt[i] - cash_liquid[i] for i in range(8)]
write_data_row(ws, r, "Net debt (Rs crore)", net_debt); r += 1
net_debt_ebitda = [net_debt[i] / ebitda[i] for i in range(8)]
write_data_row(ws, r, "Net debt/EBITDA", net_debt_ebitda, fmt="0.00\"x\""); r += 1
roce = [18.8, 17.4, 16.5] + [round(100 * ebit[3 + i] / (debt[3 + i] + equity[3 + i]), 1) for i in range(5)]
write_data_row(ws, r, "RoCE %", [v / 100 for v in roce], pct=True); r += 1
cdscr = [2.1, 1.5, 1.2] + [round((pat[3 + i] + depreciation[3 + i] + interest[3 + i]) / (NET_NEW_DEBT[i] * 0 + interest[3 + i] + 20), 1) for i in range(5)]
# projected DSCR: no scheduled term repayment (all revolving WC per Note 14A), so denominator uses finance cost + a
# nominal placeholder WC-renewal buffer of Rs 20cr rather than a fabricated repayment schedule - flagged as n/m,
# same as in compute_ratios.py's historical treatment
write_data_row(ws, r, "CDSCR (n/m for FY27E+ - no scheduled term debt, see note)", cdscr, fmt="0.0\"x\""); r += 1
autosize(ws, {"A": 2, "B": 46, "C": 12, "D": 12, "E": 12, "F": 12, "G": 12, "H": 12, "I": 12})

# ============================================================== 8. Debt Breakup
ws = wb.create_sheet("Debt Breakup")
r = write_header(ws, "Debt Breakup (Rs crore) - as at 31-Mar-2026, per the FY26 Annual Report",
                  "Per CLAUDE.md Step 12(d). Facility-LEVEL detail (bank-by-bank sanctioned/outstanding, Note "
                  "14A) is NOT reproduced here - the source AR table converted with corrupted/transposed cells "
                  "(OCR artifact) and reconstructing it would risk a mis-split rated-amount line (named failure "
                  "mode in CLAUDE.md Section 8, item 12). Only the clean, unambiguous totals below are used.")
r += 1
rows = [
    ("Statutory decomposition (Note 14.2, AR FY26)", None),
    ("  Long-term (non-current) borrowings", 0),
    ("  Short-term (current) borrowings", 329.62),
    ("    of which: secured", 104.55),
    ("    of which: unsecured", 225.07),
    ("  Lease liabilities", "None disclosed as a separate line"),
    ("  TOTAL DRAWN BORROWINGS", 329.62),
    (None, None),
    ("Instrument-type view (from AR disclosures)", None),
    ("  Working-capital loans / cash credit / bill discounting / vendor financing", "See Note 14A (facility-level detail not reproduced - see note above)"),
    ("  NCDs outstanding", 0),
    ("  Commercial paper outstanding", 0),
    (None, None),
    ("AR's own net-debt bridge (company convention)", None),
    ("  Cash & bank + current liquid assets (co. broader convention)", "~421 (Q1FY27 IR deck)"),
    ("  Drawn borrowings", 329.62),
    ("  Net cash position per company convention", "~(91) i.e. net cash"),
    ("  Net debt per this workpaper's narrower cash convention (cash+curr.inv. only)", 39.74),
    (None, None),
    ("Rated-limits-vs-drawn-debt panel", None),
    ("  Total rated bank-facility LIMITS (fund-based + non-fund-based, aggregate)", "485.00 (AR FY26 credit-rating disclosure, dated - see below)"),
    ("  Total DRAWN borrowings (balance-sheet debt, distinct measure)", 329.62),
    ("  Undrawn headroom (limits - drawn, approximate)", "~155 (aggregate; facility-level split not available)"),
    ("  Carried-table date", "AR FY26 Board's Report, dated 21-May-2026 (year-end 31-Mar-2026); amount confirmed "
                             "unchanged in a 15-Sep-2025 CRISIL credit bulletin (context only, not a data source)"),
]
for label, val in rows:
    if label is None:
        r += 1
        continue
    c = ws.cell(row=r, column=2, value=label)
    if val is None:
        c.font = LABEL_FONT
    else:
        vc = ws.cell(row=r, column=4, value=val)
        vc.number_format = "#,##0.00" if isinstance(val, (int, float)) else "General"
    r += 1
autosize(ws, {"A": 2, "B": 62, "C": 4, "D": 40})

OUT = "Happy Forgings Limited_Financial_Model_11Aug2026.xlsx"
wb.save(OUT)
print("Saved", OUT)
print("\nSanity check - revenue/EBITDA/PAT FY24-31:")
for i, y in enumerate(ALL_YEARS):
    print(f"  {y}: rev={revenue[i]:.0f}  ebitda={ebitda[i]:.0f} ({100*ebitda[i]/revenue[i]:.1f}%)  pat={pat[i]:.0f}")
