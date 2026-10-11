# -*- coding: utf-8 -*-
"""Step 12 for Equitas SFB - LENDING model (pre-flight [1c]: book growth -> NII -> credit cost -> PAT,
balance sheet, capital, Credit Ratios, Debt Breakup), scaled per case.json step12_scaling_decision.
Writes Equitas_SFB_Lending_Model_10Oct2026.xlsx + charts/. Historical columns come from
compute_ratios.py (R6). Credit Ratios tab = Excel FORMULAS off the statement tabs; run
tools/recalc_workbook.py on the output to cache them."""
import importlib.util
import os
import zipfile

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cr", os.path.join(HERE, "compute_ratios.py"))
E = importlib.util.module_from_spec(spec)
spec.loader.exec_module(E)
R = E.compute()
kv, v = E.kv, E.v
H = E.YEARS
P = ["FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E"]
OUT = os.path.join(HERE, "Equitas_SFB_Lending_Model_10Oct2026.xlsx")


def hist(p):
    return dict(
        adv=kv(E.BS_ASSET, "Advances", p), inv=kv(E.BS_ASSET, "Investments", p),
        cash=kv(E.BS_ASSET, "Cash and balances with RBI", p) + kv(E.BS_ASSET, "Balances with banks, call money", p),
        oth_a=kv(E.BS_ASSET, "Fixed assets", p) + kv(E.BS_ASSET, "Other assets", p),
        ta=E.total_assets(p), dep=kv(E.BS_LIAB, "Deposits", p), bor=kv(E.BS_LIAB, "Borrowings", p),
        oth_l=kv(E.BS_LIAB, "Other liabilities and provisions", p), nw=E.net_worth(p), tnw=E.tnw(p),
        ii=kv(E.PL, "Interest earned", p), ie=kv(E.PL, "Interest expended", p), nii=E.nii(p),
        oi=kv(E.PL, "Other income", p), opex=kv(E.PL, "Operating expenses", p),
        ppop=R[p]["Pre-provision operating profit"], cc=E.credit_cost_abs(p), pbt=R[p]["PBT"],
        tax=E.tax(p), pat=E.pat(p), div=0.0,
        t1=v(E.CAP, "CET1 / Tier I capital", p), t2=v(E.CAP, "Tier II capital", p), rwa=v(E.CAP, "RWA", p))


HIST = {p: hist(p) for p in H}
F = HIST["FY2026"]
TAX = 25.17
MIX = {k: F[k] / F["ta"] for k in ("adv", "inv", "cash", "oth_a")}   # FY2026 asset mix
OTH_L_PCT = F["oth_l"] / F["ta"]
RWA_DENSITY = F["rwa"] / F["ta"]
INTANG_DTA = F["nw"] - F["tnw"]                                        # held flat

BASE = dict(growth=[18.0, 18.0, 17.0, 16.0, 15.0], nim=[6.00, 6.10, 6.20, 6.20, 6.20],
            oi=[1.80] * 5, opex=[5.50, 5.40, 5.30, 5.20, 5.10], cc=[1.20, 1.10, 1.10, 1.10, 1.10],
            payout=[0.0, 10.0, 10.0, 10.0, 10.0], equity=[0.0] * 5)
STRESS = dict(BASE, growth=[10.0, 8.0, 12.0, 15.0, 15.0], nim=[5.60, 5.50, 5.80, 6.00, 6.10],
              oi=[1.60, 1.50, 1.70, 1.80, 1.80], opex=[5.60, 5.70, 5.50, 5.30, 5.20],
              cc=[3.00, 2.50, 1.60, 1.20, 1.10], payout=[0.0] * 5)
TAIL = dict(STRESS, cc=[5.00, 3.50, 2.00, 1.30, 1.10], growth=[5.0, 5.0, 10.0, 15.0, 15.0])
SCEN = {"Base": BASE, "Stress (MFI-type shock)": STRESS, "Tail (Utkarsh-type shock)": TAIL}

SOURCES = [
    ("Gross advances growth (%)", "growth",
     "ANALYST JUDGMENT. FY2026 +18.0% (RBI gross advances 36,922.42 -> 43,580.10, asset-quality note); "
     "FY2025 +17.5%. Moderates as the base grows. Stress/Tail slow growth to conserve capital."),
    ("NIM on average total assets (%)", "nim",
     "ANALYST JUDGMENT anchored on FY2026 5.98% (CareEdge basis, engine) and FY2025 6.63%. The "
     "microfinance book (~10% of advances, down from 18%) earns the highest yield; its shrinkage caps "
     "the recovery. Stress compresses NIM via interest reversals on slippages."),
    ("Other income / avg total assets (%)", "oi", "FY2026 actual 1.89% (engine); includes PSLC fees "
                                                  "and recoveries from written-off accounts."),
    ("Opex / avg total assets (%)", "opex", "FY2026 actual 5.64% (engine); gradual operating leverage "
                                            "assumed (1,060 branches already built)."),
    ("Credit cost / avg total assets (%)", "cc",
     "ANALYST JUDGMENT. FY2026 2.00%, FY2025 2.31% (engine). Base normalises as the MFI stress "
     "passes: Q1 FY2027 PBT Rs 244.07 crore vs a Rs 297.48 crore loss in Q1 FY2026 (segment note). "
     "Stress repeats FY2025-26-type costs; Tail is a severe shock (peer Utkarsh: GNPA 12.42%)."),
    ("Dividend payout (% of PAT)", "payout", "No dividend for FY2025 or FY2026 (Board). Base resumes "
                                             "10% from FY2028; none under stress."),
]


def project(a):
    rows, pv = [], dict(F)
    for i in range(5):
        h = {}
        h["adv"] = pv["adv"] * (1 + a["growth"][i] / 100)
        h["ta"] = h["adv"] / MIX["adv"]
        for k_ in ("inv", "cash", "oth_a"):
            h[k_] = h["ta"] * MIX[k_]
        ata = (h["ta"] + pv["ta"]) / 2
        h["nii"] = ata * a["nim"][i] / 100
        h["oi"] = ata * a["oi"][i] / 100
        h["opex"] = ata * a["opex"][i] / 100
        h["ppop"] = h["nii"] + h["oi"] - h["opex"]
        h["cc"] = ata * a["cc"][i] / 100
        h["pbt"] = h["ppop"] - h["cc"]
        h["tax"] = h["pbt"] * TAX / 100          # negative PBT -> deferred tax credit
        h["pat"] = h["pbt"] - h["tax"]
        h["div"] = max(0.0, h["pat"]) * a["payout"][i] / 100
        h["nw"] = pv["nw"] + h["pat"] - h["div"] + a["equity"][i]
        h["tnw"] = h["nw"] - INTANG_DTA
        h["bor"] = pv["bor"]
        h["oth_l"] = h["ta"] * OTH_L_PCT
        h["dep"] = h["ta"] - h["nw"] - h["bor"] - h["oth_l"]
        h["ie"] = None
        h["ii"] = None
        h["t1"] = pv["t1"] + h["pat"] - h["div"] + a["equity"][i]
        h["t2"] = pv["t2"]
        h["rwa"] = h["ta"] * RWA_DENSITY
        rows.append(h)
        pv = h
    return rows


RUNS = {n: project(a) for n, a in SCEN.items()}
B = RUNS["Base"]


def ratios(h, pv):
    ata = (h["ta"] + pv["ta"]) / 2
    return dict(nim=100 * h["nii"] / ata, rota=100 * h["pat"] / ata, ccr=100 * h["cc"] / ata,
                crar=100 * (h["t1"] + h["t2"]) / h["rwa"], t1=100 * h["t1"] / h["rwa"],
                ronw=100 * h["pat"] / ((h["tnw"] + pv["tnw"]) / 2), cd=100 * h["adv"] / h["dep"],
                gearing=(h["dep"] + h["bor"]) / h["tnw"])


# breakeven: the FY2027 credit cost at which CRAR falls to the 15% SFB minimum (Base other drivers)
def crar_at(cc):
    return ratios(project(dict(BASE, cc=[cc] + BASE["cc"][1:], payout=[0.0] * 5))[0], F)["crar"]


lo, hi = 0.0, 20.0
for _ in range(60):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if crar_at(mid) > 15.0 else (lo, mid)
BREAKEVEN_CC = lo

# sanity: historical python ratios reproduce the engine
for p, q in zip(H[1:], H[:-1]):
    r = ratios(HIST[p], HIST[q])
    assert abs(r["nim"] - R[p]["NIM (%)"]) < 0.01 and abs(r["rota"] - R[p]["ROTA (%)"]) < 0.01, p
    assert abs(r["crar"] - R[p]["CRAR (%)"]) < 0.01, p

# =========================================================================== workbook
HDR = PatternFill("solid", fgColor="1F3864")
HDRF = Font(bold=True, color="FFFFFF")
PROJF = PatternFill("solid", fgColor="FFF2CC")
BOLD = Font(bold=True)
COLS = H + P
ROWS = {}


def sheet(wb, title, first="Rs crore"):
    ws = wb.create_sheet(title)
    ws.append([first, *COLS, "Source / note"])
    for c in ws[1]:
        c.fill, c.font = HDR, HDRF
    ws.column_dimensions["A"].width = 50
    for i in range(2, 2 + len(COLS)):
        ws.column_dimensions[get_column_letter(i)].width = 12
    ws.column_dimensions[get_column_letter(2 + len(COLS))].width = 70
    ws.freeze_panes = "B2"
    return ws


def put(ws, key, label, hv, pv_, note="", fmt="#,##0.00", bold=False):
    ws.append([label, *[None if x is None else round(x, 4) for x in list(hv) + list(pv_)], note])
    r = ws.max_row
    ROWS[(ws.title, key)] = r
    for j in range(2, 2 + len(COLS)):
        ws.cell(r, j).number_format = fmt
        if j >= 2 + len(H):
            ws.cell(r, j).fill = PROJF
    if bold:
        for c in ws[r]:
            c.font = BOLD


def series(key, rows=B):
    return [HIST[p][key] for p in H], [r[key] for r in rows]


wb = openpyxl.Workbook()
wb.remove(wb.active)
ws = wb.create_sheet("Assumptions")
ws.append(["Equitas Small Finance Bank - standalone lending model (Rs crore). Base case on the statement "
           "tabs; Scenarios tab carries Stress and Tail. Generated by build_model.py from compute_ratios.py."])
ws.cell(1, 1).font = Font(bold=True, size=12)
ws.append([])
ws.append(["Driver", *P, "Source / basis"])
for c in ws[ws.max_row]:
    c.fill, c.font = HDR, HDRF
for lab, key, src in SOURCES:
    for n, a in SCEN.items():
        ws.append(["%s - %s" % (lab, n), *a[key], src if n == "Base" else ""])
ws.append([])
for lab, val, src in (
        ("FY2026 asset mix held: advances / investments / cash / other (% of total assets)",
         " / ".join("%.1f" % (100 * MIX[k_]) for k_ in ("adv", "inv", "cash", "oth_a")), "balance sheet FY2026"),
        ("RWA density (RWA / total assets, %)", round(100 * RWA_DENSITY, 2), "FY2026: 32,028.39 / 60,610.36"),
        ("Tier II capital held at FY2026 level (Rs crore)", F["t2"], "assumes the two Rs 500 crore 9.6% Lower Tier II "
         "bonds (maturity 2030) are refinanced as Basel II discounting begins - analyst assumption"),
        ("Borrowings held flat (Rs crore)", round(F["bor"], 2), "deposits are the funding plug"),
        ("Tax rate (%)", TAX, "statutory; FY2026 effective 19.6% on a small PBT"),
        ("Breakeven FY2027 credit cost for CRAR = 15% (% of avg total assets)", round(BREAKEVEN_CC, 2),
         "solved in code, base-case other drivers, no dividend")):
    ws.append([lab, val, "", "", "", "", src])
ws.column_dimensions["A"].width = 72
ws.column_dimensions["G"].width = 100

ws = sheet(wb, "Lending P&L")
put(ws, "nii", "Net interest income", *series("nii"), "Interest earned - interest expended (P&L)", bold=True)
put(ws, "oi", "Other income", *series("oi"), "P&L")
put(ws, "opex", "Operating expenses", *series("opex"), "P&L")
put(ws, "ppop", "Pre-provision operating profit", *series("ppop"), "ties to MD&A operating profit", bold=True)
put(ws, "cc", "Credit cost (provisions & write-offs excl. tax)", *series("cc"), "note 18.14(f) less tax")
put(ws, "pbt", "Profit before tax", *series("pbt"), "")
put(ws, "tax", "Tax", *series("tax"), "note 18.14(f) tax + deferred tax")
put(ws, "pat", "PROFIT AFTER TAX", *series("pat"), "P&L (tied)", bold=True)
put(ws, "div", "Dividend", [0, 0, 0, 0], [r["div"] for r in B], "none declared FY2025-26")

ws = sheet(wb, "Balance Sheet")
for k_, lab in (("adv", "Advances (net)"), ("inv", "Investments"), ("cash", "Cash, RBI and bank balances"),
                ("oth_a", "Fixed and other assets"), ("ta", "TOTAL ASSETS"), ("nw", "Net worth"),
                ("tnw", "Tangible net worth (less DTA and software)"), ("dep", "Deposits"),
                ("bor", "Borrowings (incl. Lower Tier II bonds)"), ("oth_l", "Other liabilities and provisions")):
    put(ws, k_, lab, *series(k_), "balance sheet / tangible net worth tied to Reg 52(4)" if k_ == "tnw" else "",
        bold=k_ in ("ta", "nw"))
put(ws, "chk", "Check: assets - (net worth + deposits + borrowings + other liabilities)",
    [HIST[p]["ta"] - HIST[p]["nw"] - HIST[p]["dep"] - HIST[p]["bor"] - HIST[p]["oth_l"] for p in H],
    [r["ta"] - r["nw"] - r["dep"] - r["bor"] - r["oth_l"] for r in B], "must be zero")

ws = sheet(wb, "Capital")
put(ws, "t1", "Tier I capital (CET1)", *series("t1"), "regulatory capital note; projected = + retained profit")
put(ws, "t2", "Tier II capital", *series("t2"), "regulatory capital note")
put(ws, "rwa", "Risk-weighted assets", *series("rwa"), "regulatory capital note; projected at FY2026 density")

ws = sheet(wb, "Credit Ratios", "CareEdge financial-sector ratios (formulas)")
PL_, BS_, CP_ = "Lending P&L", "Balance Sheet", "Capital"


def ref(tab, key, col):
    return "'%s'!%s%d" % (tab, col, ROWS[(tab, key)])


for key, lab, f in (
    ("nim", "NIM - NII / avg total assets (%)", lambda c, pc: None if pc is None else
     "=100*%s/((%s+%s)/2)" % (ref(PL_, "nii", c), ref(BS_, "ta", c), ref(BS_, "ta", pc))),
    ("rota", "ROTA - PAT / avg total assets (%)", lambda c, pc: None if pc is None else
     "=100*%s/((%s+%s)/2)" % (ref(PL_, "pat", c), ref(BS_, "ta", c), ref(BS_, "ta", pc))),
    ("ronw", "RONW - PAT / avg tangible net worth (%)", lambda c, pc: None if pc is None else
     "=100*%s/((%s+%s)/2)" % (ref(PL_, "pat", c), ref(BS_, "tnw", c), ref(BS_, "tnw", pc))),
    ("ccr", "Credit cost / avg total assets (%)", lambda c, pc: None if pc is None else
     "=100*%s/((%s+%s)/2)" % (ref(PL_, "cc", c), ref(BS_, "ta", c), ref(BS_, "ta", pc))),
    ("opx", "Opex / avg total assets (%)", lambda c, pc: None if pc is None else
     "=100*%s/((%s+%s)/2)" % (ref(PL_, "opex", c), ref(BS_, "ta", c), ref(BS_, "ta", pc))),
    ("cti", "Cost to income - opex / (NII + other income) (%)", lambda c, pc:
     "=100*%s/(%s+%s)" % (ref(PL_, "opex", c), ref(PL_, "nii", c), ref(PL_, "oi", c))),
    ("crar", "CRAR - (Tier I + Tier II) / RWA (%)", lambda c, pc:
     "=100*(%s+%s)/%s" % (ref(CP_, "t1", c), ref(CP_, "t2", c), ref(CP_, "rwa", c))),
    ("t1r", "Tier I / RWA (%)", lambda c, pc: "=100*%s/%s" % (ref(CP_, "t1", c), ref(CP_, "rwa", c))),
    ("gear", "Overall gearing - (deposits + borrowings) / TNW (x)", lambda c, pc:
     "=(%s+%s)/%s" % (ref(BS_, "dep", c), ref(BS_, "bor", c), ref(BS_, "tnw", c))),
    ("cd", "Credit / deposit (%)", lambda c, pc: "=100*%s/%s" % (ref(BS_, "adv", c), ref(BS_, "dep", c))),
):
    ws.append([lab])
    r = ws.max_row
    ROWS[("Credit Ratios", key)] = r
    for j in range(len(COLS)):
        c = get_column_letter(2 + j)
        pc = get_column_letter(1 + j) if j > 0 else None
        ws.cell(r, 2 + j).value = f(c, pc)
        ws.cell(r, 2 + j).number_format = "0.00"
        if j >= len(H):
            ws.cell(r, 2 + j).fill = PROJF
ws.append([])
ws.append(["SFB regulatory minimum: CRAR 15%, Tier I 7.5% (Basel II); leverage ratio 4.5% (CareEdge Banks "
           "methodology, March 2025)."])

ws = wb.create_sheet("Scenarios")
ws.append(["Scenario / metric", *P])
for c in ws[1]:
    c.fill, c.font = HDR, HDRF
ws.column_dimensions["A"].width = 46
SCEN_OUT = {}
for n, rows in RUNS.items():
    ws.append([n.upper()])
    ws.cell(ws.max_row, 1).font = BOLD
    rr = [ratios(h, pv) for h, pv in zip(rows, [F] + rows[:-1])]
    SCEN_OUT[n] = rr
    for lab, fn in (("Gross advances growth (%)", lambda h, r, i: SCEN[n]["growth"][i]),
                    ("PAT", lambda h, r, i: h["pat"]), ("ROTA (%)", lambda h, r, i: r["rota"]),
                    ("Credit cost / ATA (%)", lambda h, r, i: r["ccr"]),
                    ("Tier I (%)", lambda h, r, i: r["t1"]), ("CRAR (%)", lambda h, r, i: r["crar"]),
                    ("Tangible net worth", lambda h, r, i: h["tnw"])):
        ws.append([lab, *[round(fn(h, r, i), 2) for i, (h, r) in enumerate(zip(rows, rr))]])
ws.append([])
ws.append(["Breakeven: FY2027 credit cost that takes CRAR to the 15%% minimum = %.2f%% of average total "
           "assets (FY2026 actual 2.00%%; FY2025 2.31%%)." % BREAKEVEN_CC])

ws = wb.create_sheet("Debt Breakup")
ws.column_dimensions["A"].width = 64
for col in "BCD":
    ws.column_dimensions[col].width = 13
ws.column_dimensions["E"].width = 84
ws.append(["(i) FUNDING MIX (Rs crore)", "FY2024", "FY2025", "FY2026", "Source"])
for c in ws[1]:
    c.fill, c.font = HDR, HDRF
for lab, key in (("Demand - from banks", "Demand - from banks"), ("Demand - from others", "Demand - from others"),
                 ("Savings bank", "Savings bank"), ("Term - from banks", "Term - from banks"),
                 ("Term - from others", "Term - from others")):
    ws.append([lab, *[round(kv(E.DEPOSITS, key, p), 2) for p in H[1:]], "Schedule 3"])
ws.append(["TOTAL DEPOSITS", *[round(R[p]["Deposits"], 2) for p in H[1:]], "Schedule 3 total (engine tie-out)"])
ws.append(["CASA ratio (%)", *[round(R[p]["CASA ratio (%)"], 2) for p in H[1:]], "(demand + savings) / deposits"])
ws.append(["Borrowings", *[round(R[p]["Borrowings"], 2) for p in H[1:]],
           "Schedule 4: all from 'other institutions and agencies'; Lower Tier II bonds Rs 500 crore "
           "(Dec-2024) + Rs 500 crore (Jul-2025) inside; split of the remainder not disclosed"])
ws.append(["Total borrowings / total assets (%)", *[round(100 * R[p]["Borrowings"] / R[p]["Total assets"], 2)
                                                     for p in H[1:]], "bank prints 4.04% / 9.52% (Reg 52(4))"])
ws.append(["Top-20 depositors (% of deposits)", "", 17.60, 20.61, "concentration note"])
ws.append([])
ws.append(["(ii) INSTRUMENTS (bank's own documents)", "", "", "", ""])
ws.append(["Lower Tier II bond INE063P08112", "", "", 500.00, "allotted 05-Dec-2024; 9.6% p.a.; maturity 05-Dec-2030 (FY2025 AR)"])
ws.append(["Lower Tier II bond INE063P08120", "", "", 500.00, "allotted 31-Jul-2025; 9.6% p.a.; maturity 31-Jul-2030 (FY2026 AR)"])
ws.append(["Inter-bank participation certificates (IBPC) issued", "", 0.00, 2000.00,
           "Schedule 9 footnote; maturities 2 days-2 months (ALM note)"])
ws.append(["Certificates of deposit outstanding", "", "", "n/d", "not disclosed separately in the documents"])
ws.append([])
ws.append(["(iii) RATED LIMITS vs DRAWN", "", "", "Rs crore", ""])
ws.append(["CareEdge rated programme - CRA-PUBLISHED 06-Oct-2025, NOT issuer-confirmed", "", "", 2500.00,
           "Lower Tier II 500 + 500 (fully issued) + CD 1,500 (programme limit) + issuer rating"])
ws.append(["Lower Tier II outstanding (drawn) vs rated 1,000", "", "", 1000.00, "fully utilised"])
for row in ws.iter_rows(min_row=2):
    if row[0].value and str(row[0].value).startswith("("):
        for c in row:
            c.fill, c.font = HDR, HDRF

# valuation (Task 3 - flexibility only)
ws = wb.create_sheet("Valuation")
MCAP, PRICE = 7554.0, 66.0
ws.append(["Market data (screener.in, close 09-Oct-2026; third-party, not exchange-verified)"])
ws.cell(1, 1).font = BOLD
for lab, val in (("Share price (Rs)", PRICE), ("Market capitalisation (Rs crore)", MCAP),
                 ("Price / book (x) on FY2026 net worth 6,124.83", round(MCAP / F["nw"], 2)),
                 ("Price / tangible book (x) on FY2026 TNW 5,582.45", round(MCAP / F["tnw"], 2)),
                 ("Market cap / FY2026 Tier I capital (x)", round(MCAP / F["t1"], 2))):
    ws.append([lab, val])
ws.column_dimensions["A"].width = 60
wb.move_sheet("Assumptions", offset=-len(wb.sheetnames))
wb.save(OUT)
print("wrote", os.path.basename(OUT), wb.sheetnames)
for n, rr in SCEN_OUT.items():
    rows = RUNS[n]
    print("%-28s FY27 PAT %7.0f ROTA %5.2f%% CRAR %5.2f%% | min CRAR %5.2f%% | FY31 PAT %6.0f ROTA %5.2f%%"
          % (n, rows[0]["pat"], rr[0]["rota"], rr[0]["crar"], min(r["crar"] for r in rr), rows[-1]["pat"],
             rr[-1]["rota"]))
print("breakeven FY27 credit cost for CRAR 15%%: %.2f%%" % BREAKEVEN_CC)

# =========================================================================== charts (Task 4)
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

plt.rcParams.update({"font.family": "Times New Roman", "font.size": 10})
CH = os.path.join(HERE, "charts")
os.makedirs(CH, exist_ok=True)
NAVY, TEAL, AMBER, RED, GREY = "#1F3864", "#2E8B8B", "#F5B041", "#C0392B", "#9E9E9E"
Y = [p.replace("FY20", "FY") for p in H]
YP = [p.replace("FY20", "FY") for p in P]
INDEX = []


def save(fig, name, title, src):
    fig.savefig(os.path.join(CH, name), dpi=300, bbox_inches="tight")
    plt.close(fig)
    INDEX.append("%s | %s | %s" % (name, title, src))


fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(Y, [R[p]["PAT"] for p in H], color=NAVY, label="PAT (Rs crore)")
ax.set_ylabel("PAT (Rs crore)")
ax2 = ax.twinx()
ax2.plot(Y[1:], [R[p]["ROTA (%)"] for p in H[1:]], color=RED, marker="o", label="ROTA (%)")
ax2.set_ylabel("ROTA (%)")
ax.set_title("Profitability collapse: PAT Rs 799 crore (FY24) -> Rs 103 crore (FY26)")
save(fig, "chart_01_pat_rota.png", "PAT and ROTA FY2023-26", "engine")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(Y, [R[p]["Slippage ratio (%)"] for p in H], marker="o", color=RED, label="Slippage ratio")
ax.plot(Y, [R[p]["GNPA (%)"] for p in H], marker="o", color=NAVY, label="GNPA")
ax.plot([Y[0], Y[2], Y[3]], [R[p]["Write-off ratio (%)"] for p in ("FY2023", "FY2025", "FY2026")], marker="s",
        color=AMBER, label="Write-off ratio")
ax.set_ylabel("% ")
ax.legend()
ax.set_title("Headline GNPA steady at 2.6-2.9% only because slippages are written off")
save(fig, "chart_02_slippage_writeoff_gnpa.png", "Slippage, write-off and GNPA ratios", "engine")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(Y, [R[p]["CASA ratio (%)"] for p in H], marker="o", color=TEAL)
ax.set_ylabel("CASA ratio (%)")
ax.set_title("CASA ratio eroding: 42.2% (FY23) -> 26.2% (FY26)")
save(fig, "chart_03_casa.png", "CASA ratio", "Schedule 3 / engine")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(Y, [R[p]["CRAR (%)"] for p in H], marker="o", color=NAVY, label="CRAR")
ax.plot(Y, [R[p]["Tier I (%)"] for p in H], marker="o", color=TEAL, label="Tier I")
ax.axhline(15, color=RED, ls=":", lw=1)
ax.text(0, 15.3, "SFB minimum CRAR 15%", color=RED, fontsize=8)
ax.legend()
ax.set_title("Capital cushion narrowing but adequate")
save(fig, "chart_04_capital.png", "CRAR and Tier I", "regulatory capital note")

fig, ax = plt.subplots(figsize=(8, 4))
for (n, rr), col in zip(SCEN_OUT.items(), [NAVY, AMBER, RED]):
    ax.plot(YP, [r["crar"] for r in rr], marker="o", color=col, label=n)
ax.axhline(15, color=GREY, ls="--")
ax.set_ylabel("CRAR (%)")
ax.legend(fontsize=8)
ax.set_title("CRAR by scenario (15% SFB minimum dashed)")
save(fig, "chart_05_scenario_crar.png", "Scenario CRAR", "model Scenarios tab")

fig, ax = plt.subplots(figsize=(8, 4))
mfi = [v(E.OPS, "Microfinance gross advances", p) for p in ("FY2023", "FY2024", "FY2025")]
ax.bar(["FY23", "FY24", "FY25"], mfi, color=AMBER)
ax.set_ylabel("Microfinance gross advances (Rs crore)")
ax.set_title("Microfinance book cut 28% in FY2025 (to ~10% of advances by FY2026)")
save(fig, "chart_06_mfi_book.png", "Microfinance book", "FY2023-24 and FY2024-25 ARs")

ZIP = os.path.join(HERE, "Equitas_SFB_Charts_10Oct2026.zip")
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for line in INDEX:
        z.write(os.path.join(CH, line.split(" | ")[0]), line.split(" | ")[0])
    z.writestr("chart_index.txt", "file | title | source\n" + "\n".join(INDEX) + "\n")
print("wrote %d charts" % len(INDEX))
