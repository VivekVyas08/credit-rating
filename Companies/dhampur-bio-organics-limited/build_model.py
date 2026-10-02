"""Step 5 spreads + Step 12 forward model + Step 12b scorecard for Dhampur Bio Organics.

Produces, all FROM the ratio engine (never hand-typed - R6):
  DBOL_Financial_Spreads.xlsx    Extraction / RatioSuite / TieOut          (Step 5)
  DBOL_5yr_Model.xlsx            Assumptions / P&L / Debt / CreditRatios /
                                 DebtBreakup / Stress                      (Step 12)
  Rating_Scorecard_Dhampur Bio Organics Limited.xlsx                       (Step 12b)

EVERY forward driver is labelled with its source in the Assumptions tab. Where a driver is
analyst judgment it says so - Step 12 requires the label, not the pretence of a source.

The debt path is DERIVED from the funding gap (failure mode 18): capex less internal accrual
less dividend = external funding need, year by year. It is not carried forward from the
historical pattern.
"""
import importlib.util
import pathlib
import shutil

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

CASE = pathlib.Path(__file__).resolve().parent
ROOT = CASE.parent.parent
CO = "Dhampur Bio Organics Limited"

spec = importlib.util.spec_from_file_location("dbol_engine", CASE / "compute_ratios.py")
ENG = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ENG)
R = ENG.compute()
HIST = ENG.YEARS
FY26 = R["FY2026"]

BOLD = Font(bold=True)
HDR = PatternFill("solid", fgColor="1F3864")
HDRF = Font(bold=True, color="FFFFFF")
YEL = PatternFill("solid", fgColor="FFF2CC")

# ---------------------------------------------------------------- Step 12 assumptions
PROJ = ["FY2027", "FY2028", "FY2029", "FY2030", "FY2031"]

ASSUMPTIONS = [
    ("Crushing capacity (TCD)", [20500] * 5,
     "Q1FY27 investor presentation, 15-Jul-2026 - Asmoli 12,500 + Mansurpur 8,000. FIXED: "
     "capacity fell from 29,500 on the Meerganj divestment and no expansion is announced."),
    ("Distillery capacity (KLPD)", [312.5] * 5,
     "Q1FY27 investor presentation - 312.5 KLPD on B-heavy molasses, including 100 KLPD "
     "dual-feed (molasses and grain)."),
    ("Net TOI growth (%)", [6.0, 7.0, 6.0, 5.0, 5.0],
     "ANALYST JUDGMENT. Volume is capacity-capped, so growth is realisation- and mix-led: "
     "full-year contribution from the dual-feed distillery and a richer ethanol mix. No "
     "capacity expansion is assumed because none is announced."),
    ("PBILDT margin (%)", [6.80, 7.20, 7.50, 7.60, 7.60],
     "ANALYST JUDGMENT anchored on the FY2024 actual of 7.32%. Recovery assumes the FY2026 "
     "cane-cost step-up (SAP +Rs 30/quintal) is absorbed by realisation and that administered "
     "ethanol prices are revised at least once over the horizon. It does NOT assume a return "
     "to the pre-red-rot recovery rates."),
    ("Maintenance capex (Rs cr)", [45.0, 45.0, 50.0, 50.0, 50.0],
     "ANALYST JUDGMENT. Maintenance-level only, consistent with a capacity-capped asset base "
     "and no announced expansion; stepped modestly for the ageing distillery."),
    ("Scheduled LT debt repayment (Rs cr)", [26.0, 26.0, 26.0, 26.0, 26.0],
     "ANALYST JUDGMENT on the reduced post-divestment term-debt base."),
    ("Average interest rate (%)", [6.2, 6.2, 6.3, 6.3, 6.3],
     "Derived from FY2026 actuals: finance cost 62.98 on average total debt of 1,111.40 "
     "(FY2025 1,162.34 and FY2026 1,060.46) = 5.67%; rounded up for the working-capital mix."),
    ("Effective tax rate (%)", [25.2, 25.2, 25.2, 25.2, 25.2],
     "Statutory rate under s.115BAA. FY2026 actual effective rate was 38.4% on a small PBT "
     "base, distorted by the deferred-tax charge; the statutory rate is the better forward "
     "assumption."),
    ("Dividend payout (% of PAT)", [20.0, 20.0, 20.0, 20.0, 20.0],
     "ANALYST JUDGMENT consistent with the company's recent dividend record."),
]

STRESS = [
    ("Net TOI growth (%)", [0.0, -2.0, 2.0, 3.0, 3.0],
     "STRESS: an adverse cane year (red-rot recurrence / poor recovery) plus flat ethanol "
     "offtake. These are the variables the CareEdge sugar methodology names."),
    ("PBILDT margin (%)", [5.00, 4.80, 5.50, 6.00, 6.20],
     "STRESS: SAP rises with no realisation pass-through and ethanol prices stay administered "
     "and unchanged - the single most rating-sensitive combination for this issuer."),
]


def project(growth, margin, capex, repay, rate, taxr, payout):
    """Five-year path. Debt is DERIVED from the funding gap, never assumed (failure mode 18)."""
    rows = []
    toi = FY26["TOI (net of excise)"]
    debt = FY26["Total debt (incl leases)"]
    da = FY26["Depreciation & amortisation"]
    for i in range(5):
        toi = toi * (1 + growth[i] / 100.0)
        pbildt = toi * margin[i] / 100.0
        da = da * 1.02                       # slow drift on a capacity-capped asset base
        interest = debt * rate[i] / 100.0
        pbt = pbildt - da - interest
        tax = max(0.0, pbt) * taxr[i] / 100.0
        pat = pbt - tax
        div = max(0.0, pat) * payout[i] / 100.0
        gca = pat + da
        # funding gap = capex + dividend + scheduled repayment - internal accrual
        gap = capex[i] + div + repay[i] - gca
        debt = debt + gap                    # gap > 0 draws debt; gap < 0 repays it
        rows.append(dict(year=PROJ[i], toi=toi, pbildt=pbildt, margin=margin[i], da=da,
                         interest=interest, pbt=pbt, tax=tax, pat=pat, gca=gca, capex=capex[i],
                         dividend=div, repay=repay[i], gap=gap, debt=debt,
                         icr=pbildt / interest if interest else 0.0,
                         td_pbildt=debt / pbildt if pbildt else 0.0,
                         td_gca=debt / gca if gca else 0.0))
    return rows


def a(name):
    return [r[1] for r in ASSUMPTIONS if r[0] == name][0]


BASE = project(a("Net TOI growth (%)"), a("PBILDT margin (%)"), a("Maintenance capex (Rs cr)"),
               a("Scheduled LT debt repayment (Rs cr)"), a("Average interest rate (%)"),
               a("Effective tax rate (%)"), a("Dividend payout (% of PAT)"))
SBASE = project([r[1] for r in STRESS if r[0] == "Net TOI growth (%)"][0],
                [r[1] for r in STRESS if r[0] == "PBILDT margin (%)"][0],
                a("Maintenance capex (Rs cr)"), a("Scheduled LT debt repayment (Rs cr)"),
                a("Average interest rate (%)"), a("Effective tax rate (%)"),
                a("Dividend payout (% of PAT)"))


def style_header(ws, row=1):
    for c in ws[row]:
        if c.value is not None:
            c.fill, c.font = HDR, HDRF
            c.alignment = Alignment(horizontal="center", wrap_text=True)


def autosize(ws, wide=0):
    for col in ws.columns:
        m = max((len(str(c.value)) for c in col if c.value is not None), default=8)
        ws.column_dimensions[col[0].column_letter].width = min(max(m + 2, 10), 62 if wide else 30)


# ================================================================ Financial Spreads (Step 5)
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Extraction"
ws.append(["Line item", *HIST, "Source as the engine records it"])
for table, label in ((ENG.PL, "P&L"), (ENG.BS, "Balance sheet")):
    ws.append([label.upper()])
    ws.cell(ws.max_row, 1).font = BOLD
    for k, (vals, src) in table.items():
        ws.append([k, *[v for v in vals], src])
style_header(ws)
autosize(ws, wide=1)

ws = wb.create_sheet("RatioSuite")
labels = [k for k in R[HIST[-1]] if k not in ENG.PL and k not in ENG.BS]
ws.append(["Ratio (CareEdge corporate convention)", *HIST])
for k in labels:
    ws.append([k, *[R[y].get(k) for y in HIST]])
style_header(ws)
autosize(ws)

ws = wb.create_sheet("TieOut")
ws.append(["#", "Check", "Computed", "Printed", "Tol", "Result", "Source"])
for i, (d, c, dd, tol, src) in enumerate(ENG.tieouts(R), 1):
    ws.append([i, d, round(c, 4), round(dd, 4), tol,
               "PASS" if abs(c - dd) <= tol else "FAIL", src])
style_header(ws)
autosize(ws, wide=1)
wb.save(CASE / "DBOL_Financial_Spreads.xlsx")
print("wrote DBOL_Financial_Spreads.xlsx  (%d tie-outs)" % len(ENG.tieouts(R)))

# ================================================================ 5-year model (Step 12)
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Assumptions"
ws.append(["Driver", *PROJ, "Source / basis (Step 12: every driver labelled)"])
for name, vals, src in ASSUMPTIONS:
    ws.append([name, *vals, src])
ws.append([])
ws.append(["STRESS CASE - variables the CareEdge sugar methodology names"])
ws.cell(ws.max_row, 1).font = BOLD
for name, vals, src in STRESS:
    ws.append([name, *vals, src])
style_header(ws)
autosize(ws, wide=1)

for tab, data in (("P&L_Base", BASE), ("Stress", SBASE)):
    ws = wb.create_sheet(tab)
    ws.append(["Rs crore", *[r["year"] for r in data]])
    for key, lab in (("toi", "TOI (net of excise)"), ("pbildt", "PBILDT"),
                     ("margin", "PBILDT margin (%)"), ("da", "Depreciation"),
                     ("interest", "Interest"), ("pbt", "PBT"), ("tax", "Tax"),
                     ("pat", "PAT"), ("gca", "Gross cash accruals")):
        ws.append([lab, *[round(r[key], 2) for r in data]])
    style_header(ws)
    autosize(ws)

ws = wb.create_sheet("Debt")
ws.append(["Rs crore", *[r["year"] for r in BASE]])
for key, lab in (("capex", "Capex"), ("dividend", "Dividend"), ("repay", "Scheduled repayment"),
                 ("gca", "Less: gross cash accruals"), ("gap", "= FUNDING GAP (derived)"),
                 ("debt", "Closing total debt")):
    ws.append([lab, *[round(r[key], 2) for r in BASE]])
ws.append([])
ws.append(["Funding gap = capex + dividend + scheduled repayment - internal accrual. The debt "
           "path is DERIVED from this identity, not carried forward from the historical "
           "pattern (failure mode 18)."])
style_header(ws)
autosize(ws)

ws = wb.create_sheet("CreditRatios")
ws.append(["CareEdge convention", *HIST, *[r["year"] for r in BASE]])
ws.append(["PBILDT margin (%)", *[round(R[y]["PBILDT margin % (net TOI)"], 2) for y in HIST],
           *[round(r["margin"], 2) for r in BASE]])
ws.append(["Interest coverage (x)", *[round(R[y]["Interest coverage (x)"], 2) for y in HIST],
           *[round(r["icr"], 2) for r in BASE]])
ws.append(["Total debt / PBILDT (x)", *[round(R[y]["Total debt / PBILDT (x)"], 2) for y in HIST],
           *[round(r["td_pbildt"], 2) for r in BASE]])
ws.append(["Total debt / GCA (x)", *[round(R[y]["Total debt / GCA (x)"], 2) for y in HIST],
           *[round(r["td_gca"], 2) for r in BASE]])
ws.append(["Overall gearing (x)", *[round(R[y]["Overall gearing (x)"], 2) for y in HIST],
           *["-"] * 5])
ws.append(["Total debt (Rs cr)", *[round(R[y]["Total debt (incl leases)"], 2) for y in HIST],
           *[round(r["debt"], 2) for r in BASE]])
style_header(ws)
autosize(ws)

ws = wb.create_sheet("DebtBreakup")
ws.append(["Component (consolidated, as printed)", *HIST, "Source"])
for k in ("Borrowings - non-current", "Borrowings - current", "Lease liabilities - NC",
          "Lease liabilities - current"):
    ws.append([k, *[R[y][k] for y in HIST], ENG.BS[k][1]])
ws.append(["TOTAL DEBT (incl leases)", *[round(R[y]["Total debt (incl leases)"], 2) for y in HIST],
           "sum of the four lines above - tied to the balance-sheet subtotals"])
ws.append(["Unencumbered cash", *[round(R[y]["Unencumbered cash"], 2) for y in HIST],
           "note 13 ONLY - other bank balances are margin/earmarked (FM34)"])
ws.append(["NET DEBT", *[round(R[y]["Net debt (on unencumbered cash)"], 2) for y in HIST],
           "derived on UNENCUMBERED cash"])
ws.append([])
ws.append(["RATED LIMITS vs DRAWN DEBT (failure modes 13 and 31)"])
ws.cell(ws.max_row, 1).font = BOLD
ws.append(["CareEdge published limits, action dated 04-Sep-2026", 1062.05, "", "",
           "LT 987.05 (CC 770.00 + TL 117.05 + WCDL 100.00) + ST 75.00 BG/LC. "
           "CRA-PUBLISHED under the five-condition amendment, NOT issuer-confirmed."])
ws.append(["Drawn borrowings incl leases, 31-Mar-2026",
           round(FY26["Total debt (incl leases)"], 2), "", "",
           "Limits and drawn debt are DIFFERENT measures and do not reconcile."])
ws.append(["  of which working capital", round(FY26["Working capital borrowings"], 2), "", "",
           "current borrowings 847.19 LESS current maturities of LT debt 82.68"])
ws.append(["  of which long-term (incl current maturities)",
           round(FY26["Long-term debt (incl current maturities)"], 2), "", "",
           "non-current 206.98 PLUS current maturities 82.68 - the split v1 never made"])
style_header(ws)
autosize(ws, wide=1)
wb.save(CASE / "DBOL_5yr_Model.xlsx")
print("wrote DBOL_5yr_Model.xlsx")
print("  base  FY2031: PBILDT margin %.2f%%, ICR %.2fx, TD/PBILDT %.2fx, debt %.0f"
      % (BASE[-1]["margin"], BASE[-1]["icr"], BASE[-1]["td_pbildt"], BASE[-1]["debt"]))
print("  STRESS FY2028 trough: ICR %.2fx, TD/PBILDT %.2fx, debt %.0f"
      % (SBASE[1]["icr"], SBASE[1]["td_pbildt"], SBASE[1]["debt"]))

# ================================================================ scorecard (Step 12b)
tgt = CASE / ("Rating_Scorecard_%s.xlsx" % CO)
shutil.copy2(ROOT / "Rating_Scorecard.xlsx", tgt)
wb = openpyxl.load_workbook(tgt)
ws = wb["Inputs"]


def put(r, v, note=None):
    ws.cell(r, 3).value = v
    if note:
        ws.cell(r, 4).value = note


put(4, CO)
put(5, "CareEdge")
put(6, "Sugar / Agro-processing")
put(7, "04-Sep-2026")
# Historical block - AUDITED ACTUALS only (Step 12b: the anchor must not be fed the analyst's
# own forward assumptions, or the cross-check is contaminated).
put(12, round(FY26["TOI (net of excise)"], 2))
put(13, round(FY26["PBILDT (ex-other income)"], 2))
put(14, round(FY26["Depreciation & amortisation"], 2))
put(15, round(FY26["Finance costs"], 2))
put(16, round(FY26["Profit after tax"], 2))
put(17, round(FY26["Total debt (incl leases)"], 2))
put(18, round(FY26["Unencumbered cash"], 2))
put(19, round(FY26["Tangible net worth"], 2))
put(20, round(FY26["Total assets"] - FY26["Tangible net worth"], 2))
put(21, round(FY26["Total current assets"], 2))
put(22, round(FY26["Total current liabilities"], 2))
put(23, a("Maintenance capex (Rs cr)")[0])
put(24, round(FY26["Profit after tax"] * 0.20, 2))
# Projections - copied (never linked) from the model above.
put(29, a("Net TOI growth (%)")[0] / 100.0)
put(30, a("PBILDT margin (%)")[0] / 100.0)
put(31, a("Maintenance capex (Rs cr)")[0])
put(32, round(BASE[0]["gap"], 2))
put(33, a("Average interest rate (%)")[0] / 100.0)
put(34, a("Effective tax rate (%)")[0] / 100.0)
put(35, a("Dividend payout (% of PAT)")[0] / 100.0)
put(40, 4, "4 - reduced scale after the Meerganj divestment (20,500 TCD, from 29,500), single "
           "state (western/central UP), and a cyclical, administered-price industry. Partly "
           "offset by an integrated distillery at 312.5 KLPD including dual feed.")
put(41, 3, "3 - long-established promoter group and a clean audit report; no governance "
           "qualification found. Not better than 3 given the concentration of operations.")
put(42, 0, "No parent or group support is claimed. DBOL is a standalone listed issuer.")
put(43, "Adequate")
put(44, "Stable")
wb.save(tgt)
print("wrote %s" % tgt.name)
