"""Step 5 spreads + Step 12 forward model + Step 12b scorecard for Cochin Minerals and Rutile.

All figures come FROM compute_ratios.py (Rs crore, converted once from lakh). Every forward
driver is labelled in the Assumptions tab as document-sourced or analyst judgment.

The debt path is derived from the funding gap (failure mode 18). For this issuer that produces
an unusual but correct result: the company is already in NET CASH and generates accruals far
above its capex, so the gap is negative throughout and cash builds. The model is still built -
failure mode 35 is explicit that "proportionate" governs which artefact, never whether one
exists - but the forward view here is about EARNINGS RECOVERY and RAW MATERIAL ACCESS, not
about leverage, and the assumptions say so.
"""
import importlib.util
import pathlib
import shutil

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

CASE = pathlib.Path(__file__).resolve().parent
ROOT = CASE.parent.parent
CO = "Cochin Minerals and Rutile Limited"

spec = importlib.util.spec_from_file_location("cmrl_engine", CASE / "compute_ratios.py")
ENG = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ENG)
R = ENG.compute()
HIST = ENG.YEARS
FY26 = R["FY2026"]
Q1 = ENG.Q1FY27

BOLD = Font(bold=True)
HDR = PatternFill("solid", fgColor="1F3864")
HDRF = Font(bold=True, color="FFFFFF")

PROJ = ["FY2027", "FY2028", "FY2029", "FY2030", "FY2031"]

# Q1 FY2027 annualised is the anchor for FY2027, not an extrapolation of FY2026.
_q1_rev_annualised = Q1["revenue"] * 4 / 100.0          # Rs crore
_q1_pbildt = (Q1["pbt_before_exc"] + Q1["depreciation"] - Q1["other_income"]) / 100.0
_q1_margin = _q1_pbildt / (Q1["revenue"] / 100.0) * 100

ASSUMPTIONS = [
    ("Synthetic rutile capacity (MT)", [50000] * 5,
     "AR 2025-26. FIXED - no expansion is assumed, and the metallisation project that would "
     "have added capacity was impaired and abandoned in FY2026 for want of ilmenite."),
    ("Revenue (Rs crore)", [420.0, 450.0, 470.0, 490.0, 505.0],
     "FY2027 ANCHORED ON Q1 FY2027 ACTUALS, not extrapolated from FY2026. Q1 revenue of "
     "131.26 crore annualises to %.0f crore; FY2027 is set BELOW that at 420 because one "
     "quarter is not a run-rate and Q1 is not seasonally adjusted. Thereafter growth is "
     "capacity- and ilmenite-constrained, so it is realisation- and mix-led."
     % _q1_rev_annualised),
    ("PBILDT margin (%)", [10.50, 10.00, 10.00, 10.25, 10.25],
     "Q1 FY2027 actual margin was %.1f%%, against 7.96%% in FY2026 and 12.61%% in FY2024. "
     "FY2027 is set at 10.5%% - a clear recovery from the trough but BELOW the Q1 print and "
     "well below FY2024, because the ilmenite price/availability squeeze the company itself "
     "describes has not been resolved, only eased." % _q1_margin),
    ("Capex (Rs crore)", [12.0, 12.0, 15.0, 15.0, 15.0],
     "ANALYST JUDGMENT. Maintenance level. FY2026 capex was modest and the one growth project "
     "was abandoned; no new project is announced."),
    ("Average interest rate (%)", [8.5, 8.5, 8.5, 8.5, 8.5],
     "Working-capital rate. Immaterial to the outcome: total debt is 6.21 crore."),
    ("Effective tax rate (%)", [25.2] * 5,
     "Statutory rate under s.115BAA. FY2026 effective rate is distorted by the exceptional "
     "impairment."),
    ("Dividend payout (% of PAT)", [25.0] * 5,
     "ANALYST JUDGMENT, consistent with the company's dividend record and its unpaid-dividend "
     "account."),
]

STRESS = [
    ("Revenue (Rs crore)", [300.0, 285.0, 300.0, 315.0, 330.0],
     "STRESS: the Q1 FY2027 recovery does not hold and volumes fall back to the FY2026 trough "
     "or below, on renewed ilmenite shortage or import disruption - the variable the company "
     "itself names as the reason its capex project was abandoned."),
    ("PBILDT margin (%)", [6.50, 5.50, 6.00, 6.50, 7.00],
     "STRESS: synthetic rutile realisations fall further while ilmenite does not follow - the "
     "exact asymmetry described in the FY2025-26 annual report."),
]


def project(rev, margin, capex, rate, taxr, payout):
    rows, debt, da = [], FY26["Total debt"], FY26["Depreciation & amortisation"]
    cash = FY26["Unencumbered cash"]
    for i in range(5):
        pbildt = rev[i] * margin[i] / 100.0
        da = da * 1.05
        interest = debt * rate[i] / 100.0
        pbt = pbildt - da - interest
        tax = max(0.0, pbt) * taxr[i] / 100.0
        pat = pbt - tax
        div = max(0.0, pat) * payout[i] / 100.0
        gca = pat + da
        gap = capex[i] + div - gca              # negative gap = cash builds
        cash = cash - gap
        rows.append(dict(year=PROJ[i], rev=rev[i], pbildt=pbildt, margin=margin[i], da=da,
                         interest=interest, pbt=pbt, pat=pat, gca=gca, capex=capex[i],
                         dividend=div, gap=gap, debt=debt, cash=cash,
                         netdebt=debt - cash,
                         icr=pbildt / interest if interest else 0.0))
    return rows


def a(n):
    return [r[1] for r in ASSUMPTIONS if r[0] == n][0]


BASE = project(a("Revenue (Rs crore)"), a("PBILDT margin (%)"), a("Capex (Rs crore)"),
               a("Average interest rate (%)"), a("Effective tax rate (%)"),
               a("Dividend payout (% of PAT)"))
SBASE = project([r[1] for r in STRESS if r[0] == "Revenue (Rs crore)"][0],
                [r[1] for r in STRESS if r[0] == "PBILDT margin (%)"][0],
                a("Capex (Rs crore)"), a("Average interest rate (%)"),
                a("Effective tax rate (%)"), a("Dividend payout (% of PAT)"))


def style(ws):
    for c in ws[1]:
        if c.value is not None:
            c.fill, c.font = HDR, HDRF
            c.alignment = Alignment(horizontal="center", wrap_text=True)
    for col in ws.columns:
        m = max((len(str(c.value)) for c in col if c.value is not None), default=8)
        ws.column_dimensions[col[0].column_letter].width = min(max(m + 2, 11), 62)


# ---------------------------------------------------------------- Financial Spreads (Step 5)
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Extraction"
ws.append(["Line item (Rs LAKH as printed)", *HIST, "Source"])
for table, lab in ((ENG.PL, "P&L"), (ENG.BS, "BALANCE SHEET"), (ENG.BANK_SPLIT, "NOTE 12")):
    ws.append([lab]); ws.cell(ws.max_row, 1).font = BOLD
    for k, (vals, src) in table.items():
        ws.append([k, *vals, src])
style(ws)

ws = wb.create_sheet("RatioSuite")
ws.append(["Ratio (Rs CRORE, CareEdge convention)", *HIST])
for k in [x for x in R[HIST[-1]] if x not in ENG.PL and x not in ENG.BS]:
    ws.append([k, *[R[y].get(k) for y in HIST]])
style(ws)

ws = wb.create_sheet("TieOut")
ws.append(["#", "Check", "Computed", "Printed", "Tol", "Result", "Source"])
for i, (d, c, dd, tol, src) in enumerate(ENG.tieouts(R), 1):
    ws.append([i, d, round(c, 4), round(dd, 4), tol,
               "PASS" if abs(c - dd) <= tol else "FAIL", src])
style(ws)
wb.save(CASE / "CMRL_Financial_Spreads.xlsx")
print("wrote CMRL_Financial_Spreads.xlsx (%d tie-outs)" % len(ENG.tieouts(R)))

# ---------------------------------------------------------------- 5-year model (Step 12)
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Assumptions"
ws.append(["Driver", *PROJ, "Source / basis"])
for n, v, s in ASSUMPTIONS:
    ws.append([n, *v, s])
ws.append([])
ws.append(["STRESS CASE - the variables the manufacturing criteria and the company itself name"])
ws.cell(ws.max_row, 1).font = BOLD
for n, v, s in STRESS:
    ws.append([n, *v, s])
ws.append([])
ws.append(["Q1 FY2027 ACTUAL (the anchor for FY2027)", "", "", "", "", "", Q1["note"]])
style(ws)

for tab, data in (("P&L_Base", BASE), ("Stress", SBASE)):
    ws = wb.create_sheet(tab)
    ws.append(["Rs crore", *[r["year"] for r in data]])
    for k, lab in (("rev", "Revenue"), ("pbildt", "PBILDT"), ("margin", "PBILDT margin (%)"),
                   ("da", "Depreciation"), ("interest", "Interest"), ("pbt", "PBT"),
                   ("pat", "PAT"), ("gca", "Gross cash accruals")):
        ws.append([lab, *[round(r[k], 2) for r in data]])
    style(ws)

ws = wb.create_sheet("Debt")
ws.append(["Rs crore", *[r["year"] for r in BASE]])
for k, lab in (("capex", "Capex"), ("dividend", "Dividend"),
               ("gca", "Less: gross cash accruals"), ("gap", "= FUNDING GAP (derived)"),
               ("debt", "Total debt"), ("cash", "Unencumbered cash"),
               ("netdebt", "NET DEBT / (NET CASH)")):
    ws.append([lab, *[round(r[k], 2) for r in BASE]])
ws.append([])
ws.append(["Funding gap = capex + dividend - internal accrual. It is NEGATIVE throughout: this "
           "issuer funds its capex from accruals and accumulates cash. The debt path is "
           "derived, not extrapolated (failure mode 18)."])
style(ws)

ws = wb.create_sheet("CreditRatios")
ws.append(["CareEdge convention", *HIST, *[r["year"] for r in BASE]])
ws.append(["PBILDT margin (%)", *[round(R[y]["PBILDT margin (%)"], 2) for y in HIST],
           *[round(r["margin"], 2) for r in BASE]])
ws.append(["Overall gearing (x)", *[round(R[y]["Overall gearing (x)"], 3) for y in HIST],
           *["-"] * 5])
ws.append(["Interest coverage (x)", *[round(R[y]["Interest coverage (x)"], 1) for y in HIST],
           *[round(r["icr"], 1) for r in BASE]])
ws.append(["Net debt / (net cash)", *[round(R[y]["Net debt / (net cash)"], 2) for y in HIST],
           *[round(r["netdebt"], 2) for r in BASE]])
ws.append(["RoCE (%)", *[round(R[y]["RoCE (%)"], 2) for y in HIST], *["-"] * 5])
style(ws)

ws = wb.create_sheet("DebtBreakup")
ws.append(["Component (Rs crore, standalone)", *HIST, "Source"])
for k in ("Borrowings - long term", "Borrowings - short term"):
    ws.append([k, *[round(R[y][k], 2) for y in HIST], ENG.BS[k][1]])
ws.append(["TOTAL DEBT", *[round(R[y]["Total debt"], 2) for y in HIST], "sum of the above"])
ws.append(["Unencumbered cash", *[round(R[y]["Unencumbered cash"], 2) for y in HIST],
           "cash and cash equivalents PLUS 3-12 month deposits; margin money against BG/LC and "
           "unpaid dividend EXCLUDED (note 12)"])
ws.append(["Encumbered bank balances",
           *[(round(R[y]["Encumbered bank balances"], 2)
              if R[y]["Encumbered bank balances"] is not None else "not split") for y in HIST],
           "margin money vs BG/LC + unpaid dividend"])
ws.append(["NET DEBT / (NET CASH)", *[round(R[y]["Net debt / (net cash)"], 2) for y in HIST],
           "derived on UNENCUMBERED cash"])
ws.append([])
ws.append(["RATED LIMITS vs DRAWN DEBT (failure modes 13/31)"])
ws.cell(ws.max_row, 1).font = BOLD
ws.append(["Rated limits", "TO BE CONFIRMED BY ISSUER", "", "",
           "NO same-issuer CRA publication exists. The pre-flight's hits were Cochin SHIPYARD "
           "and Sarda Energy & MINERALS - different companies. Importing a peer's rated amount "
           "would be worse than leaving it TBC (failure mode 29)."])
ws.append(["Drawn borrowings, 31-Mar-2026", round(FY26["Total debt"], 2), "", "",
           "short-term only; no long-term debt since FY2025"])
style(ws)
wb.save(CASE / "CMRL_5yr_Model.xlsx")
print("wrote CMRL_5yr_Model.xlsx")
print("  base FY2027: rev %.0f, margin %.2f%%, PAT %.2f, net cash %.2f"
      % (BASE[0]["rev"], BASE[0]["margin"], BASE[0]["pat"], -BASE[0]["netdebt"]))
print("  STRESS FY2028 trough: rev %.0f, margin %.2f%%, PAT %.2f, net cash %.2f"
      % (SBASE[1]["rev"], SBASE[1]["margin"], SBASE[1]["pat"], -SBASE[1]["netdebt"]))

# ---------------------------------------------------------------- scorecard (Step 12b)
tgt = CASE / ("Rating_Scorecard_%s.xlsx" % CO)
shutil.copy2(ROOT / "Rating_Scorecard.xlsx", tgt)
wb = openpyxl.load_workbook(tgt)
ws = wb["Inputs"]


def put(r, v, note=None):
    ws.cell(r, 3).value = v
    if note:
        ws.cell(r, 4).value = note


put(4, CO); put(5, "CareEdge"); put(6, "Chemicals / Agrochemicals"); put(7, "13-Sep-2026")
# AUDITED ACTUALS only (Step 12b: the anchor must not be fed the analyst's forward view).
put(12, round(FY26["TOI"], 2))
put(13, round(FY26["PBILDT"], 2))
put(14, round(FY26["Depreciation & amortisation"], 2))
put(15, round(FY26["Finance costs"], 2))
put(16, round(FY26["Profit after tax"], 2))
put(17, round(FY26["Total debt"], 2))
put(18, round(FY26["Unencumbered cash"], 2))
put(19, round(FY26["Tangible net worth"], 2))
put(20, round(FY26["Total assets"] - FY26["Tangible net worth"], 2))
put(21, round(FY26["Total current assets"], 2))
put(22, round(FY26["Total current liabilities"], 2))
put(23, a("Capex (Rs crore)")[0])
put(24, round(FY26["Profit after tax"] * 0.25, 2))
# Projections copied (never linked) from the model above.
put(29, round(BASE[0]["rev"] / FY26["TOI"] - 1, 4))
put(30, a("PBILDT margin (%)")[0] / 100.0)
put(31, a("Capex (Rs crore)")[0])
put(32, round(BASE[0]["gap"], 2))
put(33, a("Average interest rate (%)")[0] / 100.0)
put(34, a("Effective tax rate (%)")[0] / 100.0)
put(35, a("Dividend payout (% of PAT)")[0] / 100.0)
put(40, 4, "4 - small scale (TOI 294.92 crore), a SINGLE product (synthetic rutile) from a "
           "single site, and a raw material the company states is in 'short supply' "
           "domestically, forcing imports. It impaired and abandoned its one growth project "
           "for exactly that reason. Partly offset by an established position in the TiO2 "
           "feedstock chain.")
put(41, 3, "3 - long-established listed company, unqualified audit opinion, no governance "
           "qualification found. Not better than 3: the metallisation project absorbed capital "
           "for years before being written off.")
put(42, 0, "No parent or group support claimed; standalone listed issuer.")
put(43, "Strong")
put(44, "Stable")
wb.save(tgt)
print("wrote %s" % tgt.name)
