"""Step 12 forecast model - Balkrishna Industries Limited (5-yr 3-statement corporate model
with term debt, per CLAUDE.md Step 12 - a manufacturer with a live multi-year capex programme).

Debt is DERIVED from the funding gap (capex less retained internal accrual) every year, never
extrapolated from the historical trend (failure mode 18). The company's own FY2026 cash flow
shows this precisely: capex of Rs 3,003.29 crore was funded 75% from operating cash flow
(Rs 2,249.32 crore) and only the remainder from net new borrowing - the model reproduces that
same funding-gap logic forward rather than assuming a leverage trajectory.

Interest expense is priced on OPENING debt, not average or closing debt, to avoid a circular
reference: closing debt depends on retained earnings, which depends on PAT, which depends on
interest expense. This is stated as a simplification (mildly conservative on a growing debt
book), the same fix applied in the Repco Home Finance lending model earlier this project.
"""
import sys
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from make_spreads import _cache_values, _force_recalc                     # noqa: E402

OUT = "Balkrishna Industries Limited_5yr_Model.xlsx"
YEARS = ["FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E"]
N = len(YEARS)
COLS = [get_column_letter(3 + i) for i in range(N)]
NOTE_COL = get_column_letter(3 + N)

HDR = PatternFill("solid", fgColor="1B2A4A")
INP = PatternFill("solid", fgColor="FFF9E6")
BAND = PatternFill("solid", fgColor="EAF0F8")
BOX = Border(*[Side("thin", color="D6DEE8")] * 4)
WHITE = Font(color="FFFFFF", bold=True, size=11)
SMALL = Font(size=8, color="666666")
BOLD = Font(bold=True)


def sheet(wb, name, title, blurb):
    ws = wb.create_sheet(name)
    ws.column_dimensions["B"].width = 54
    for c in COLS:
        ws.column_dimensions[c].width = 15
    ws.column_dimensions[NOTE_COL].width = 86
    ws.merge_cells("B2:%s2" % NOTE_COL)
    ws["B2"].value, ws["B2"].fill, ws["B2"].font = title, HDR, WHITE
    ws.merge_cells("B3:%s3" % NOTE_COL)
    ws["B3"].value, ws["B3"].font = blurb, SMALL
    ws["B3"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[3].height = 48
    ws.cell(row=5, column=2, value="Line").font = BOLD
    for i, p in enumerate(YEARS):
        c = ws.cell(row=5, column=3 + i, value=p)
        c.font, c.fill, c.border = BOLD, BAND, BOX
        c.alignment = Alignment(horizontal="center")
    ws.cell(row=5, column=3 + N, value="Derivation / source").font = BOLD
    ws.freeze_panes = "C6"
    return ws


def row(ws, r, label, make, note="", fmt="#,##0.0", inp=False, bold=False):
    c = ws.cell(row=r, column=2, value=label)
    c.border = BOX
    if bold:
        c.font = BOLD
    for i in range(N):
        v = make[i] if isinstance(make, list) else make(i, COLS[i], COLS[i - 1] if i else None)
        cell = ws.cell(row=r, column=3 + i, value=v)
        cell.number_format, cell.border = fmt, BOX
        if inp:
            cell.fill = INP
        if bold:
            cell.font = BOLD
    n = ws.cell(row=r, column=3 + N, value=note)
    n.font, n.border = SMALL, BOX
    n.alignment = Alignment(wrap_text=True, vertical="top")
    return r + 1


def band(ws, r, text):
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3 + N)
    c = ws.cell(row=r, column=2, value=text)
    c.fill, c.font = BAND, BOLD
    return r + 1


def flat(v):
    return [v] * N


def f(tmpl):
    return lambda i, c, p: tmpl.format(c=c, p=p or c)


def chain(first, tmpl):
    return lambda i, c, p: first if i == 0 else tmpl.format(c=c, p=p)


def build():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    # ================================================================= Assumptions
    A = sheet(wb, "Assumptions",
              "Balkrishna Industries Limited - forecast drivers (Rs crore; consolidated)",
              "Yellow cells are the DRIVERS. Every one is derived from the company's own "
              "documents (annual reports, MD&A, cash flow statement) or from the CRISIL/"
              "CareEdge same-issuer rationales dated Feb/Mar-2026, used here only as a "
              "cross-reference on FORECAST assumptions - never as a source of historical fact. "
              "FY2027E opens on the FY2026 audited actuals (31-Mar-2026), the most recent "
              "balance sheet in the document set.")
    r = 6
    r = band(A, r, "REVENUE")
    A_GROWTH = r
    r = row(A, r, "Revenue growth (%)", [8.0, 10.0, 10.5, 10.0, 9.0],
            "FY2026 actual growth was 3.6% (Rs 10,446.95 cr to Rs 10,823.08 cr), depressed by "
            "the North America tariff shock. CRISIL's 27-Feb-2026 rationale (peer-agency "
            "cross-reference, not a fact source) guides 'FY27 expected to grow by 7-9%... "
            "thereafter revenues are expected to grow at upwards of 10%', driven by continued "
            "India OHT volumes, carbon black scale-up and the new CVR/PCR segments. Base case "
            "takes 8.0% for FY2027E (low end, since a full tariff resolution is not assumed) "
            "and 9-10.5% thereafter as the new segments ramp.", fmt="0.00", inp=True)

    r = band(A, r, "MARGIN")
    A_MARGIN = r
    r = row(A, r, "OPBDITA margin (%)", [23.5, 23.3, 23.3, 23.3, 23.3],
            "Actuals (add-back convention, failure mode 36): 24.07% (FY2024), 23.52% (FY2025), "
            "23.93% (FY2026) - core operating profitability was RESILIENT through the North "
            "America volume shock, not compressed; the FY2026 PAT decline was a non-operating "
            "currency swing (a Rs 290.01 cr forex loss against a Rs 267.36 cr gain the prior "
            "year), disclosed in compute_ratios.py. ICRA's own 25-Aug-2026 rationale frames "
            "the forward path the same way: the rising share of lower-margin on-highway tyres "
            "(TBR/PCR/2W, launched/launching through FY2027) 'could result in some moderation "
            "in blended profitability' but 'the impact is expected to be largely offset by "
            "operating efficiencies'. Base case therefore holds margin NEAR the FY2026 actual "
            "rather than modelling either a compression-and-recovery arc or continued "
            "expansion - a mild, structural mix-driven give-back (23.93% to ~23.3%) offset by "
            "efficiency gains, roughly flat through the forecast horizon.",
            fmt="0.00", inp=True)

    r = band(A, r, "CAPEX AND WORKING CAPITAL")
    A_CAPEX = r
    r = row(A, r, "Capital expenditure (Rs cr)", [1900, 1200, 1000, 1100, 1150],
            "The company's own MD&A: 'cumulatively announced a capex outlay of Rs 6,800 crore "
            "[since Aug-2024], to be deployed through FY 2028-29' [sic; the AR text elsewhere "
            "reads FY2029], of which Rs 2,984 crore (MD&A) / Rs 3,003.29 crore (cash flow) was "
            "already spent in FY2026. Capital commitments (AR Note 46) of Rs 2,711.84 crore "
            "(FY2026, up from Rs 923.98 crore FY2025) show the NEXT phase is substantially "
            "contracted, not merely announced - so FY2027E is set high (Rs 1,900 crore, close "
            "to that committed quantum), tapering through FY2029E as the ANNOUNCED programme "
            "completes against its Rs 6,800 crore cumulative ceiling (2,984 FY2026 + 1,900 + "
            "1,200 + 1,000 = 7,084 - modestly over the announced figure, since FY2029E also "
            "carries normal replacement capex beyond the specific announced tranche). "
            "FY2030E-FY2031E are held ABOVE the FY2026 depreciation run-rate (not tapered to a "
            "bare maintenance level below it) - a capital-intensive manufacturer replacing "
            "newly-built assets and continuing the 'Vision 2030' growth plans the company's "
            "own MD&A describes does not structurally shrink its net fixed-asset base once "
            "one announced tranche completes; a model that let it do so was an artefact of "
            "over-tapering, not a considered forecast, and has been corrected here.",
            inp=True)
    A_WC = r
    r = row(A, r, "Working capital as % of incremental revenue", flat(18.0),
            "FY2026 working capital cycle was 111.36 days (RatioSuite); net working capital "
            "(current assets less current liabilities excluding cash/debt) as a share of "
            "revenue has run 15-20% across FY2023-FY2026. Held at 18%, near the FY2026 level, "
            "since the new CVR/PCR segments are not expected to structurally shorten the "
            "cycle in their ramp-up years.", fmt="0.00", inp=True)

    r = band(A, r, "FINANCING")
    A_COF = r
    r = row(A, r, "Cost of debt on opening balance (%)", flat(7.50),
            "FY2026 finance cost / opening total debt = 133.62 / 3,267.45 = 4.09%; FY2025 "
            "128.34 / 3,099.44 = 4.14%. These are LOW because a material share of BKT's "
            "consolidated debt is working-capital/export-credit lines in foreign subsidiaries "
            "at low offshore rates. Set materially higher at 7.50% for the FORECAST debt, "
            "which is assumed to be incremental RUPEE term debt/NCD funding raised in India "
            "(the company's own Rs 750 crore NCD priced AA+/CARE AA+ in Mar-2026) - "
            "conservative, since blending the low-cost offshore stock with new onshore debt "
            "would understate interest cost.", fmt="0.00", inp=True)
    A_TAX = r
    r = row(A, r, "Effective tax rate (%)", flat(24.4),
            "FY2026: 400.58/1,643.68 = 24.37%. FY2025: 532.43/2,187.39 = 24.34%. Stable across "
            "both years; held flat.", fmt="0.00", inp=True)
    A_DIV = r
    r = row(A, r, "Dividend payout (% of PAT, cash-flow basis)", flat(22.0),
            "FY2026 dividend PAID (consolidated cash flow statement) Rs 309.19 crore / FY2026 "
            "PAT Rs 1,243.10 crore = 24.87%; FY2025 Rs 309.51 crore / Rs 1,654.96 crore = "
            "18.70%. The cash-paid figure lags the DECLARED dividend by a year (a dividend "
            "declared for FY(t) is paid in FY(t+1)), so it is a smoothing average of two "
            "years' declarations rather than a clean current-year payout ratio; held at 22%, "
            "the midpoint of the two observed cash-basis ratios.", fmt="0.00", inp=True)

    # ================================================================= P&L
    P = sheet(wb, "P_and_L", "Projected profit and loss (Rs crore, consolidated)",
              "Revenue grows off the FY2026 base at the assumed rate; OPBDITA margin phases in "
              "toward the assumed level; depreciation grows with the capitalised asset base; "
              "interest is priced on OPENING debt to avoid a circular reference through "
              "closing debt / retained earnings / PAT (see Balance_Sheet note).")
    r = 6
    P_REV0 = r
    r = row(P, r, "Revenue from operations", chain(10823.08, "={p}%d*(1+Assumptions!{c}%d/100)"
                                                    % (P_REV0, A_GROWTH)),
            "FY2027E grows off the FY2026 actual of 10,823.08")
    P_OP = r
    r = row(P, r, "OPBDITA", f("={c}%d*Assumptions!{c}%d/100" % (P_REV0, A_MARGIN)), "",
            bold=True)
    P_DEP0 = r
    r = row(P, r, "Depreciation and amortisation",
            chain(774.96, "={p}%d+Assumptions!{c}%d*0.12" % (P_DEP0, A_CAPEX)),
            "FY2027E opens on the FY2026 actual of 774.96; each year adds 12% of that year's "
            "capex as incremental depreciation - roughly the FY2026 actual's ratio of "
            "depreciation growth (Rs 94.30 crore added) to capex (Rs 3,003.29 crore) = 3.1%, "
            "raised to 12% since a full-year run-rate on assets capitalised only PART-WAY "
            "through the prior year is higher in the following full year")
    P_FIN = r
    r = row(P, r, "Finance costs", flat(None), "")   # patched once Balance_Sheet exists
    P_PBT = r
    r = row(P, r, "Profit before tax", f("={c}%d-{c}%d-{c}%d" % (P_OP, P_DEP0, P_FIN)), "",
            bold=True)
    P_TAX = r
    r = row(P, r, "Tax", f("=-{c}%d*Assumptions!{c}%d/100" % (P_PBT, A_TAX)), "")
    P_PAT = r
    r = row(P, r, "Profit after tax", f("={c}%d+{c}%d" % (P_PBT, P_TAX)),
            "Actuals: 1,471.49 (FY2024), 1,654.96 (FY2025), 1,243.10 (FY2026, the tariff-hit "
            "year) - FY2026 fell 24.9% on the North America revenue decline.", bold=True)
    P_DIV = r
    r = row(P, r, "Dividend (cash-flow basis, current-year accrual)",
            f("=-{c}%d*Assumptions!{c}%d/100" % (P_PAT, A_DIV)), "")
    P_RET = r
    r = row(P, r, "Retained earnings", f("={c}%d+{c}%d" % (P_PAT, P_DIV)), "", bold=True)

    # ================================================================= Balance sheet
    S = sheet(wb, "Balance_Sheet",
              "Projected balance sheet (Rs crore) - debt is the FUNDING GAP, not a trend",
              "Failure mode 18: projected debt is DERIVED from capex less retained accrual, "
              "never extrapolated from the historical leverage pattern. Non-debt assets and "
              "liabilities scale with revenue via the working-capital assumption; PP&E rolls "
              "forward with capex less depreciation; debt is whatever balances the sheet.")
    r = 6
    S_NWC0 = r

    def nwc_formula(i, c, p):
        prev_rev = "10823.08" if i == 0 else "P_and_L!%s%d" % (p, P_REV0)
        return "=(P_and_L!%s%d-%s)*Assumptions!%s%d/100" % (c, P_REV0, prev_rev, c, A_WC)

    r = row(S, r, "Incremental working capital", nwc_formula,
            "revenue growth times the working-capital-intensity assumption; FY2027E measures "
            "growth off the FY2026 actual of 10,823.08")
    S_PPE0 = r
    r = row(S, r, "Fixed assets (PP&E + CWIP + intangibles, net)",
            chain(7326.54 + 2472.46 + 55.61 + 7.32 + 19.92,
                  "={p}%d+Assumptions!{c}%d-P_and_L!{c}%d" % (S_PPE0, A_CAPEX, P_DEP0)),
            "FY2027E opens on the FY2026 consolidated total of PP&E 7,326.54 + CWIP 2,472.46 + "
            "investment property 55.61 + intangibles 7.32 + right-of-use 19.92 = 9,881.85; "
            "each year adds capex and subtracts depreciation")
    S_OTHA0 = r
    r = row(S, r, "Other non-debt-related assets (investments, tax assets, etc)",
            flat(1796.48 + 38.46 + 20.23 + 874.85 + 1327.48),
            "held flat at the FY2026 total of non-current investments 1,796.48 + other "
            "non-current financial assets 38.46 + income tax assets 20.23 + other non-current "
            "assets 874.85 + current investments 1,327.48 = 4,057.50 - these are not driven by "
            "revenue growth in this model")
    S_CASH0 = r
    r = row(S, r, "Cash and bank balances (residual liquidity buffer held flat)",
            flat(60.92 + 3.59), "held flat at the FY2026 total of 64.51 - the model treats "
            "surplus cash generation as debt reduction, not cash accumulation, which is "
            "conservative for a credit view")
    S_TA = r
    r = row(S, r, "Total assets",
            f("=%d+SUM({c}%d:{c}%d)+{c}%d+{c}%d" % (0, S_NWC0, S_NWC0, S_PPE0, S_OTHA0)),
            "placeholder, patched below to accumulate working capital", bold=True)

    r = band(S, r, "FUNDING")
    S_EQ0 = r
    r = row(S, r, "Opening net worth", chain(10955.29, "={p}%d" % (S_EQ0 + 2)),
            "FY2027E opens on the FY2026 consolidated total equity of 10,955.29")
    S_RET = r
    r = row(S, r, "Add: retained earnings", f("=P_and_L!{c}%d" % P_RET), "from P_and_L")
    S_EQ = r
    r = row(S, r, "Closing net worth", f("={c}%d+{c}%d" % (S_EQ0, S_RET)), "", bold=True)
    S_OTHL = r
    r = row(S, r, "Non-debt liabilities (trade payables, provisions, DTL, other)",
            flat(912.26 + 279.82 + 52.95 + 316.84 + 180.37 + 589.11 + 362.87 + 6.01),
            "held flat at the FY2026 total (Rs 2,700.23 crore) - trade payables move inside "
            "the working-capital line above; this captures everything else on the liability "
            "side that is not debt and not equity")
    S_DEBT_RAW = r
    r = row(S, r, "Implied funding position (assets - net worth - non-debt liabilities)",
            f("={c}%d-{c}%d-{c}%d" % (S_TA, S_EQ, S_OTHL)),
            "total assets less closing net worth less non-debt liabilities. NEGATIVE means "
            "retained earnings exceed what the assumed asset base needs, implying a net-cash "
            "position - a plausible outcome for THIS issuer, not a modelling error: "
            "CareEdge's 05-Mar-2026 rationale names 'a net debt free profile' as an achievable "
            "POSITIVE rating trigger. Floored at zero on the next row for the debt actually "
            "carried; the negative excess is shown separately as net cash below.")
    S_DEBT = r
    r = row(S, r, "Total debt (FUNDING GAP, floored at zero)",
            f("=MAX(0,{c}%d)" % S_DEBT_RAW),
            "the debt actually modelled as carried - a company cannot carry negative "
            "borrowings, so the implied funding position above is floored here", bold=True)
    S_NETCASH = r
    r = row(S, r, "Net cash position beyond debt-free (0 if still carrying debt)",
            f("=MAX(0,-{c}%d)" % S_DEBT_RAW),
            "the surplus once the implied funding position turns negative - held as cash/"
            "liquid investments in this simplified model rather than reinvested or returned "
            "to shareholders, which is itself conservative (it understates the payout or "
            "buyback capacity a real net-cash BKT would likely exercise)")
    S_DEBT0 = r
    r = row(S, r, "Opening total debt", chain(4110.82, "={p}%d" % S_DEBT),
            "FY2027E opens on the FY2026 consolidated total debt of 4,110.82 (NC borrowings "
            "888.00 + NC leases 4.07 + C borrowings 3,217.56 + C leases 1.19)")

    # patch total assets to actually sum working capital correctly, and patch finance cost -
    # priced on the FLOORED opening debt, so once the company reaches net cash the interest
    # line goes to zero rather than flipping to an implied interest INCOME at the debt rate
    for i, c in enumerate(COLS):
        S.cell(row=S_TA, column=3 + i).value = (
            "=SUM(%s%d:%s%d)+%s%d+%s%d+%s%d" % (c, S_NWC0, c, S_NWC0, c, S_PPE0, c, S_OTHA0,
                                                c, S_CASH0))
        P.cell(row=P_FIN, column=3 + i).value = (
            "=Balance_Sheet!%s%d*Assumptions!%s%d/100" % (c, S_DEBT0, c, A_COF))
        P.cell(row=P_FIN, column=3 + i).number_format = "#,##0.0"
    P.cell(row=P_FIN, column=3 + N).value = (
        "OPENING total debt (floored at zero) times cost of debt - priced on the opening "
        "balance to avoid a circular reference through closing debt / retained earnings / "
        "PAT / finance costs, the same fix applied in the Repco Home Finance lending model "
        "built earlier this project. Once the company reaches net cash this line goes to "
        "zero rather than an implied interest INCOME, which the model does not attempt to "
        "price (a real net-cash position would earn a materially lower rate than the cost of "
        "debt, and modelling it symmetrically would overstate the benefit).")

    # cumulative working capital needs a running total, not a per-year delta - fix by summing
    for i, c in enumerate(COLS):
        cum = "+".join("%s%d" % (COLS[j], S_NWC0) for j in range(i + 1))
        S.cell(row=S_TA, column=3 + i).value = (
            "=(%s)+%s%d+%s%d+%s%d" % (cum, c, S_PPE0, c, S_OTHA0, c, S_CASH0))

    # ================================================================= Credit ratios
    R = sheet(wb, "Credit_Ratios", "Credit ratios on ICRA corporate conventions, every year",
              "The same convention set as compute_ratios.py, so projected years sit on "
              "identical definitions to the historical RatioSuite.")
    r = 6
    r = row(R, r, "OPBDITA margin %", f("=100*P_and_L!{c}%d/P_and_L!{c}%d" % (P_OP, P_REV0)),
            "Actuals 24.07 / 23.52 / 23.93 (FY2024-FY2026, add-back convention - failure mode "
            "36); core profitability held through the FY2026 currency shock", fmt="0.00")
    r = row(R, r, "Gearing (times)",
            f("=Balance_Sheet!{c}%d/Balance_Sheet!{c}%d" % (S_DEBT, S_EQ)),
            "Actuals 0.35 / 0.31 / 0.38 (FY2024-FY2026); has stayed in a 0.31x-0.44x band "
            "across all four historical years despite the capex programme", fmt="0.00",
            bold=True)
    r = row(R, r, "Total debt/OPBDITA (times)",
            f("=Balance_Sheet!{c}%d/P_and_L!{c}%d" % (S_DEBT, P_OP)),
            "Actuals 1.37 / 1.33 / 1.79 (FY2024-FY2026)", fmt="0.00", bold=True)
    r = row(R, r, "Interest coverage (times)",
            f('=IF(P_and_L!{c}%d<1,"n/m (net cash)",P_and_L!{c}%d/P_and_L!{c}%d)'
              % (P_FIN, P_OP, P_FIN)),
            "Actuals 19.98 / 19.15 / 17.22 (FY2024-FY2026) - never below 17x in any historical "
            "year including the FY2026 margin-compression year. Guarded: once finance costs "
            "fall below Rs 1 crore (the company has become net-cash, see Balance_Sheet), the "
            "ratio is marked not-meaningful rather than printing a distorted, exploding "
            "multiple as the denominator approaches zero.", fmt="0.00", bold=True)
    r = row(R, r, "TOL/TNW (times)",
            f("=(Balance_Sheet!{c}%d-Balance_Sheet!{c}%d)/Balance_Sheet!{c}%d"
              % (S_TA, S_EQ, S_EQ)), "Actuals 0.55 / 0.51 / 0.62 (FY2024-FY2026)", fmt="0.00")
    r = row(R, r, "RoCE % (indicative)",
            f("=100*(P_and_L!{c}%d-P_and_L!{c}%d)/(Balance_Sheet!{c}%d+Balance_Sheet!{c}%d)"
              % (P_OP, P_DEP0, S_DEBT, S_EQ)),
            "Actuals 13.04 / 12.59 / 9.92 (FY2024-FY2026); simplified capital-employed base "
            "(debt + equity, excluding deferred tax liability which this model does not "
            "separately project) - indicative, not a like-for-like reproduction of the "
            "historical RoCE row", fmt="0.00", bold=True)

    # ================================================================= Debt breakup
    D = sheet(wb, "Debt_Breakup", "Debt structure - FY2026 actuals and the projected requirement",
              "Statutory decomposition tied to the FY2025-26 AR consolidated balance sheet and "
              "the rated-limits-versus-drawn-debt distinction (failure modes 13 and 31).")
    r = 6
    r = band(D, r, "ACTUAL DRAWN DEBT AT 31-MAR-2026 (FY2025-26 AR, consolidated)")
    for lab, val, note in [
        ("Non-current borrowings", 888.00, "AR consolidated balance sheet"),
        ("Non-current lease liabilities", 4.07, "AR consolidated balance sheet"),
        ("Current borrowings", 3217.56, "AR consolidated balance sheet"),
        ("Current lease liabilities", 1.19, "AR consolidated balance sheet"),
        ("TOTAL DRAWN DEBT", 4110.82, "sum of the four lines above; reconciles to Total "
         "debt/total assets of 0.23x published in the company's own Reg 52(4) disclosure "
         "(4,110.82 / 17,766.34 = 0.231)"),
    ]:
        r = row(D, r, lab, [val] + [None] * (N - 1), note, bold=lab.startswith("TOTAL"))

    r = band(D, r, "RATED INSTRUMENTS (CRISIL / CareEdge - PEER AGENCY, NOT ICRA)")
    for lab, val, note in [
        ("CRISIL: bank loan facilities", 2000.00,
         "CRISIL rationale, 27-Feb-2026: 'Crisil AA+/Stable' (reaffirmed) - PEER-AGENCY "
         "REFERENCE ONLY, not ICRA's rated universe"),
        ("CRISIL: non-convertible debentures", 750.00,
         "CRISIL rationale, 27-Feb-2026: 'Crisil AA+/Stable' (assigned)"),
        ("CRISIL: commercial paper", 500.00,
         "CRISIL rationale, 27-Feb-2026: 'Crisil A1+' (reaffirmed)"),
        ("CareEdge: non-convertible debentures", 750.00,
         "CareEdge press release, 05-Mar-2026: 'CARE AA+; Stable' (assigned) - the SAME "
         "Rs 750 crore NCD tranche CRISIL also rates; CareEdge rates only this instrument, "
         "not bank facilities or CP"),
        ("ICRA rated amount", None,
         "NO ICRA RATING EXISTS on this issuer as at the data cutoff - confirmed by a "
         "recorded zero-hit search for 'ICRA' across the FY2025-26 AR and the newest "
         "quarterly filing. This is a fresh ASSIGNMENT, not a reaffirmation, and the actual "
         "ICRA-rated quantum will be set by the mandate/sanction letter, not estimated here."),
    ]:
        r = row(D, r, lab, [val] + [None] * (N - 1), note)

    r = band(D, r, "PROJECTED FUNDING REQUIREMENT")
    r = row(D, r, "Closing total debt (funding-gap derived)", f("=Balance_Sheet!{c}%d" % S_DEBT),
            "from Balance_Sheet")
    r = row(D, r, "Incremental borrowing required in the year",
            f("=Balance_Sheet!{c}%d-Balance_Sheet!{c}%d" % (S_DEBT, S_DEBT0)),
            "the annual quantum implied by the capex programme net of internal accrual")

    # ================================================================= Stress case
    T = sheet(wb, "Stress_Case",
              "Stress case - the variables named in ICRA's Corporate and Auto Components "
              "methodologies",
              "Commodity-price/raw-material volatility and demand cyclicality are the two "
              "variables ICRA's Auto Components methodology names explicitly ('earnings "
              "vulnerable to cyclicality in commodity price cycles and automotive demand', per "
              "the MRF Limited peer rationale read for craft). NOTE: FY2026 was NOT actually a "
              "margin-compression year - core OPBDITA margin held at 23.93%, up from 23.52% "
              "(FY2025); the PAT decline that year was a non-operating currency swing, not an "
              "operating one (see the Assumptions sheet's margin-row note and "
              "compute_ratios.py's failure-mode-36 correction). This scenario is therefore a "
              "genuine HYPOTHETICAL departure from the resilient base case - a real margin "
              "shock the company has not yet experienced in this dataset - combined with "
              "slower revenue growth, not a recreation of anything that already happened.")
    r = 6
    T_MARGIN = r
    r = row(T, r, "Stress OPBDITA margin (%)", flat(19.0),
            "the corrected FY2026 actual was 23.93%, essentially flat on FY2025's 23.52%; "
            "stress assumes a full ~490bps of compression sustained for five years - a shock "
            "of a magnitude the company has not shown in FY2023-FY2026, testing resilience to "
            "a genuine future risk (a sustained further tariff escalation, or a raw-material "
            "spike not passed through) rather than modelling a past event", fmt="0.00", inp=True)
    T_GROWTH = r
    r = row(T, r, "Stress revenue growth (%)", flat(3.0),
            "held near the FY2026 actual of 3.6% (itself already a tariff-depressed year) "
            "rather than the base case's assumed acceleration to 9-10.5%", fmt="0.00", inp=True)
    r += 1
    TS_REV = r
    r = row(T, r, "Revenue", chain(10823.08, "={p}%d*(1+{c}%d/100)" % (TS_REV, T_GROWTH)),
            "FY2027E grows off the FY2026 actual of 10,823.08, same starting point as the "
            "base case")
    TS_OP = r
    r = row(T, r, "OPBDITA", f("={c}%d*{c}%d/100" % (TS_REV, T_MARGIN)), "", bold=True)
    TS_DEP = r
    r = row(T, r, "Depreciation (held at base-case level)", f("=P_and_L!{c}%d" % P_DEP0),
            "capex commitments already made are not reversible in a demand-side stress")
    TS_FIN = r
    r = row(T, r, "Finance costs (held at base-case level, first-order)",
            f("=P_and_L!{c}%d" % P_FIN), "a simplification - a true second-order stress would "
            "also re-solve for higher debt; shown as a lower bound on the stress impact")
    TS_PBT = r
    r = row(T, r, "Profit before tax", f("={c}%d-{c}%d-{c}%d" % (TS_OP, TS_DEP, TS_FIN)), "",
            bold=True)
    TS_PAT = r
    r = row(T, r, "Profit after tax",
            f("=IF({c}%d>0,{c}%d*(1-Assumptions!{c}%d/100),{c}%d)"
              % (TS_PBT, TS_PBT, A_TAX, TS_PBT)), "", bold=True)
    r = row(T, r, "Interest coverage in stress (times)",
            f('=IF({c}%d<1,"n/m (net cash)",{c}%d/{c}%d)' % (TS_FIN, TS_OP, TS_FIN)),
            "against the historical low of 17.22x (FY2026) - the sector methodology's own "
            "concern is margin/demand cyclicality, not a leverage covenant breach, and this "
            "row shows why: coverage stays comfortable (or the company is net-cash and the "
            "ratio not meaningful) even under a sustained further "
            "225bps margin hit", fmt="0.00", bold=True)

    wb.move_sheet("Assumptions", offset=-10)
    wb.save(OUT)
    _force_recalc(OUT)
    _cache_values(OUT)
    return OUT


if __name__ == "__main__":
    print("Saved:", build())
