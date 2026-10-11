# -*- coding: utf-8 -*-
"""Step 12 for Reliance Industries Limited (consolidated - basis per R12, see compute_ratios.py).

Equity-research initiating-coverage Task 2 (model) + Task 3 (valuation tab) + Task 4 (charts).
Writes:
  RIL_Financial_Model_10Oct2026.xlsx
     Assumptions | Revenue Model | Income Statement | Cash Flow | Balance Sheet | Scenarios |
     DCF Inputs | Valuation | Credit Ratios (Excel FORMULAS off the three statements) | Debt Breakup
  charts/chart_*.png + RIL_Charts_10Oct2026.zip

Historical columns come from compute_ratios.py (never retyped). Every forward driver is in the
scenario dictionaries with its source; analyst judgment is labelled as such. The debt path is
DERIVED from the funding gap (failure mode 18): new borrowing happens only when cash and liquid
investments would fall below the floor. Run, then tools/recalc_workbook.py on the output.
"""
import importlib.util
import os

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cr", os.path.join(HERE, "compute_ratios.py"))
E = importlib.util.module_from_spec(spec)
spec.loader.exec_module(E)
R = E.compute()
v, tot = E.v, E.tot
H = E.YEARS
P = ["FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E"]
OUT = os.path.join(HERE, "RIL_Financial_Model_10Oct2026.xlsx")
SEGS = ["O2C", "Oil and Gas", "Retail", "Digital Services", "Others"]


# ===================================================================== historical statements
def hist(p):
    s = lambda t, *ks: sum(v(t, k, p) for k in ks)  # noqa: E731
    cdpl = v(E.DEBT_NOTES, "Current maturities of deferred payment liabilities", p)
    h = dict(
        voss=v(E.PL, "Value of sales and services", p), gst=v(E.PL, "GST recovered", p),
        rev=v(E.PL, "Revenue from operations", p),
        pbdit=E.pbdit(p), onetime=v(E.ONE_TIME_INCOME, "Profit on sale of listed investments", p),
        da=v(E.PL, "Depreciation and amortisation", p), fc=v(E.PL, "Finance costs", p),
        capint=v(E.CAPITALISED_INTEREST, "Interest capitalised", p),
        tax=v(E.PL, "Current tax", p) + v(E.PL, "Deferred tax", p),
        dtax=v(E.PL, "Deferred tax", p),
        assoc=v(E.PL, "Share of associates and JVs", p) + v(E.PL, "Profit from discontinued operations", p),
        nci_pat=v(E.PL_PRINTED, "Attributable to NCI", p),
        block=s(E.NCA, "Property, plant and equipment", "Spectrum", "Other intangible assets", "Goodwill",
                "Capital work-in-progress", "Spectrum under development", "Intangibles under development"),
        onca=s(E.NCA, "Non-current investments", "Non-current loans", "Other non-current financial assets",
               "Deferred tax assets", "Other non-current assets"),
        inv=v(E.CA, "Inventories", p), rec=v(E.CA, "Trade receivables", p),
        cash=v(E.CA, "Cash and cash equivalents", p) + v(E.CA, "Current investments", p),
        oca=s(E.CA, "Current loans", "Other current financial assets", "Other current assets"),
        eq=v(E.EQUITY, "Equity share capital", p) + v(E.EQUITY, "Other equity", p),
        nci=v(E.EQUITY, "Non-controlling interest", p),
        borr=E.borrowings(p), lease=E.leases(p), dpl=E.dpl(p),
        dtl=v(E.NCL, "Deferred tax liabilities", p),
        oncl=s(E.NCL, "Other non-current financial liabilities", "Non-current provisions",
               "Other non-current liabilities"),
        pay=v(E.CL, "Trade payables", p),
        ocl=s(E.CL, "Other current financial liabilities", "Other current liabilities", "Current provisions") - cdpl,
        cfo=v(E.CF, "Net cash from operating activities", p),
        capex=v(E.CF, "Capex (PPE, spectrum, intangibles)", p),
        dplpay=v(E.CF, "Payment of deferred payment liabilities", p),
        div=v(E.CF, "Dividend paid to owners", p) + v(E.CF, "Dividend paid to NCI", p),
        intpaid=v(E.CF, "Interest paid", p),
    )
    for k in SEGS:
        h["rev_" + k] = v(E.SEG_REV, k, p)
        h["ebitda_" + k] = v(E.SEG_EBITDA, k, p)
    h["interseg"] = v(E.SEG_REV_ELIM, "Inter-segment transfers", p)
    return finish(h)


def finish(h):
    h["pbt"] = h["pbdit"] + h["onetime"] - h["da"] - h["fc"]
    h["pat"] = h["pbt"] - h["tax"] + h["assoc"]
    h["pat_owner"] = h["pat"] - h["nci_pat"]
    h["int_crisil"] = h["fc"] + h["capint"]
    h["adj_debt"] = h["borr"] + h["lease"] + h["dpl"]
    h["ta"] = sum(h[k] for k in ("block", "onca", "inv", "rec", "cash", "oca"))
    h["tle"] = sum(h[k] for k in ("eq", "nci", "borr", "lease", "dpl", "dtl", "oncl", "pay", "ocl"))
    return h


HIST = {p: hist(p) for p in H}
for p in H:  # the grouping must reproduce the printed totals before anything is projected
    h = HIST[p]
    assert abs(h["pat"] - v(E.PL_PRINTED, "Profit for the year", p)) < 0.5, (p, h["pat"])
    assert abs(h["ta"] - v(E.BS_PRINTED, "Total assets", p)) < 0.5, (p, h["ta"])
    assert abs(h["tle"] - h["ta"]) < 0.5, (p, h["tle"], h["ta"])
    assert abs(h["adj_debt"] - R[p]["Adjusted total debt"]) < 0.5, p
F = HIST["FY2026"]
F25 = HIST["FY2025"]

# ===================================================================== assumptions
GST_PCT = 100 * F["gst"] / F["voss"]                                    # 8.52%
INTERSEG_PCT = 100 * F["interseg"] / sum(F["rev_" + k] for k in SEGS)   # 10.51%
DA_RATE = 100 * F["da"] / F25["block"]                                  # 4.57% of opening block
INV_DAYS_PCT = 100 * F["inv"] / F["rev"]
REC_PCT = 100 * F["rec"] / F["rev"]
PAY_PCT = 100 * F["pay"] / F["rev"]
YIELD = 4.3       # unallocated interest income / avg cash & MS FY2026 = 10,395 / 2,40,076
UNALLOC = -4000.0  # other unallocable (net) ex one-time: -2,393 / -3,024 / -5,794 FY2024-26
RATE = 8.0        # gross interest (excl. lease, forex) / avg (borrowings + DPL) FY2026 = 8.2%
LEASE_INT = 2006.0
TAX = 23.0        # FY2026 effective 22.4% (27,552 / 1,23,162)
DEF_SHARE = 50.0  # deferred share of tax: FY2024-26 46.6% / 49.4% / 64.7%
NCI_SHARE = 15.6  # FY2026 NCI 14,979 / 95,754
FLOOR = 200000.0  # cash + current investments floor before new borrowing (FY2024 2,03,395)
DPL_REPAY = [4962.0, 5300.0, 5650.0, 6050.0, 6450.0]
DIV_FY27 = 8119.0 + 450.0  # Rs 6/share recommended for FY2026 (note 45) + NCI dividends ~FY2026 436

BASE = dict(
    g={"O2C": [5, 3, 3, 3, 3], "Oil and Gas": [-5] * 5, "Retail": [12, 12, 11, 11, 10],
       "Digital Services": [13, 12, 12, 11, 10], "Others": [10] * 5},
    m={"O2C": [9.0] * 5, "Oil and Gas": [76, 75, 74, 73, 72], "Retail": [7.3, 7.4, 7.5, 7.5, 7.5],
       "Digital Services": [44.0, 44.5, 45.0, 45.0, 45.0], "Others": [13.5] * 5},
    capex=[150000, 145000, 135000, 130000, 125000], capshare=[40, 35, 30, 25, 20],
    wc_shock=[0, 0, 0, 0, 0], payout=10.0)
BULL = dict(BASE, g=dict(BASE["g"], **{"Retail": [14] * 5, "Digital Services": [15, 14, 13, 12, 12]}),
            m=dict(BASE["m"], **{"O2C": [10.5] * 5, "Digital Services": [45, 46, 47, 47, 47]}))
BEAR = dict(BASE,
            g={"O2C": [-10, -5, 3, 3, 3], "Oil and Gas": [-10] * 5, "Retail": [6, 6, 8, 9, 9],
               "Digital Services": [8, 8, 9, 9, 9], "Others": [5] * 5},
            m={"O2C": [6.5, 6.5, 7.5, 8.0, 8.5], "Oil and Gas": [70, 68, 66, 65, 65],
               "Retail": [6.5, 6.5, 7.0, 7.0, 7.0], "Digital Services": [42, 42, 43, 43, 43],
               "Others": [11] * 5},
            capex=[172500, 166750, 155250, 140000, 130000],
            wc_shock=[-100000, 0, 0, 0, 0], payout=10.0)
TAIL = dict(BEAR,
            g={"O2C": [-20, -5, 5, 5, 5], "Oil and Gas": [-15] * 5, "Retail": [3, 3, 6, 8, 8],
               "Digital Services": [5, 5, 7, 8, 8], "Others": [0] * 5},
            m={"O2C": [5.0, 5.0, 6.5, 8.0, 8.5], "Oil and Gas": [65] * 5, "Retail": [6.0] * 5,
               "Digital Services": [40, 40, 41, 42, 43], "Others": [10] * 5},
            capex=[175000, 175000, 160000, 140000, 130000],
            wc_shock=[-150000, -30000, 0, 0, 0], payout=10.0)
SCEN = {"Base": BASE, "Bull": BULL, "Bear / rating stress": BEAR, "Tail": TAIL}

ASSUMPTION_TEXT = [
    ("Segment revenue growth (%)",
     "ANALYST JUDGMENT anchored on FY2024-26 segment history (audited segment information): O2C "
     "5,64,749 -> 6,62,401 (+8.3% CAGR, crude-price driven); Oil & Gas 24,439 -> 23,861 with KG D6 "
     "output 260.3 -> 248.8 BCFe (natural decline); Retail 3,06,848 -> 3,71,085 (+10.0% CAGR); Digital "
     "1,32,938 -> 1,76,164 (+15.1% CAGR); Others 80,516 -> 80,522."),
    ("Segment EBITDA margin (%)",
     "ANALYST JUDGMENT anchored on FY2024-26 margins (engine): O2C 11.0 / 8.8 / 9.1; Oil & Gas 82.6 / "
     "84.0 / 79.8; Retail 7.5 / 7.6 / 7.3; Digital 42.6 / 42.2 / 43.5; Others 10.5 / 15.3 / 13.5. Q1 "
     "FY2027 (release 17-Jul-2026): O2C EBITDA +17.2% YoY, JPL margin 53.3% on operating revenue."),
    ("Capex - cash (Rs crore)",
     "ANALYST JUDGMENT: company capex excl. spectrum 1,31,769 / 1,31,107 / 1,44,271 (FY2024-26 "
     "releases); Q1 FY2027 38,682 (annualised ~1.55 lakh crore); capital commitments rose to 66,517 "
     "from 31,629 (note 34). Bear adds a 15% overrun on new-energy / O2C projects (CRISIL project "
     "risk: projects large relative to operations)."),
    ("Share of gross interest capitalised (%)",
     "FY2026 16,091 of 38,358 gross = 42%; FY2025 18,283 of 38,987 = 47%. Falls as 5G / new-energy "
     "assets commission (Q1 FY2027 release: finance cost +18.5% 'due to ... capitalisation of 5G assets')."),
    ("Working-capital shock (Rs crore, cash outflow)",
     "STRESS VARIABLE (CRISIL cash-flow adequacy): FY2026 contract liabilities rose 1,09,196 to 1,72,201 "
     "(note 23) and trade/other payables added 86,609 to CFO; supplier finance is 76,377 (note 44). "
     "Bear unwinds 1,00,000 in FY2027; Tail 1,50,000 + 30,000."),
]
FIXED = [
    ("GST recovered (% of value of sales and services)", round(GST_PCT, 2), "FY2026 1,00,244 / 11,75,919"),
    ("Inter-segment transfers (% of gross segment revenue)", round(INTERSEG_PCT, 2), "FY2026 1,38,114 / 13,14,033"),
    ("D&A (% of opening capital block incl. CWIP)", round(DA_RATE, 2), "FY2026 57,688 / FY2025 block 12,61,751"),
    ("Inventory / receivables / payables (% of revenue)", "%.1f / %.1f / %.1f" % (INV_DAYS_PCT, REC_PCT, PAY_PCT),
     "FY2026 balance sheet / revenue from operations"),
    ("Treasury yield on opening cash and current investments (%)", YIELD,
     "FY2026 unallocated interest income 10,395 / average cash & MS 2,40,076 (segment information)"),
    ("Other unallocable income / (expense), net (Rs crore)", UNALLOC,
     "FY2024-26: -2,393 / -3,024 / -5,794 after removing the 8,924 one-time gain"),
    ("Gross interest rate on borrowings + DoT liabilities (%)", RATE,
     "FY2026 (22,050 + 16,091 + 217) / avg (borrowings + DPL) 4,67,807 = 8.2%"),
    ("Lease interest (Rs crore, flat; leases held flat)", LEASE_INT, "note 29 FY2026"),
    ("Tax rate (%) / deferred share (%)", "%.0f / %.0f" % (TAX, DEF_SHARE), "FY2026 effective 22.4%; deferred 64.7%"),
    ("NCI share of profit (%)", NCI_SHARE, "FY2026 14,979 / 95,754"),
    ("Cash + current investments floor (Rs crore)", FLOOR,
     "ANALYST JUDGMENT: FY2024 level 2,03,395; below it the funding gap is BORROWED (failure mode 18)"),
    ("DoT instalments (Rs crore)", ", ".join("%.0f" % x for x in DPL_REPAY),
     "FY2027 = current maturity 4,962 (note 22); later years grow with the annuity profile (judgment)"),
    ("Dividend FY2027 (Rs crore) / later payout (% of prior-year owners' PAT)", "%.0f / 10%%" % DIV_FY27,
     "Rs 6/share recommended for FY2026 = 8,119 (note 45) + NCI ~450; FY2026 payout 8,119 / 80,775 = 10%"),
]


def project(a):
    rows, prev = [], dict(F)
    for i in range(5):
        h = {"onetime": 0.0}
        for k in SEGS:
            h["rev_" + k] = prev["rev_" + k] * (1 + a["g"][k][i] / 100)
            h["ebitda_" + k] = h["rev_" + k] * a["m"][k][i] / 100
        gross = sum(h["rev_" + k] for k in SEGS)
        h["interseg"] = gross * INTERSEG_PCT / 100
        h["voss"] = gross - h["interseg"]
        h["gst"] = h["voss"] * GST_PCT / 100
        h["rev"] = h["voss"] - h["gst"]
        seg = sum(h["ebitda_" + k] for k in SEGS)
        h["treasury"] = prev["cash"] * YIELD / 100
        h["pbdit"] = seg + h["treasury"] + UNALLOC
        h["da"] = prev["block"] * DA_RATE / 100
        h["capex"] = a["capex"][i]
        h["dplpay"] = DPL_REPAY[i]
        h["dpl"] = prev["dpl"] - h["dplpay"]
        h["lease"], h["onca"], h["oca"], h["oncl"] = prev["lease"], prev["onca"], prev["oca"], prev["oncl"]
        h["inv"], h["rec"], h["pay"] = (h["rev"] * INV_DAYS_PCT / 100, h["rev"] * REC_PCT / 100,
                                        h["rev"] * PAY_PCT / 100)
        h["ocl"] = prev["ocl"] + a["wc_shock"][i]
        h["assoc"] = 0.0
        h["div"] = DIV_FY27 if i == 0 else a["payout"] / 100 * max(0.0, prev["pat_owner"]) * 1.06
        h["newb"] = 0.0
        for _ in range(60):
            borr_close = prev["borr"] + h["newb"]
            gross_int = RATE / 100 * ((prev["borr"] + prev["dpl"]) + (borr_close + h["dpl"])) / 2
            h["capint"] = gross_int * a["capshare"][i] / 100
            h["fc"] = gross_int - h["capint"] + LEASE_INT
            h["pbt"] = h["pbdit"] - h["da"] - h["fc"]
            h["tax"] = max(0.0, h["pbt"]) * TAX / 100
            h["dtax"] = h["tax"] * DEF_SHARE / 100
            h["pat"] = h["pbt"] - h["tax"]
            h["nci_pat"] = h["pat"] * NCI_SHARE / 100
            h["pat_owner"] = h["pat"] - h["nci_pat"]
            h["cfo"] = (h["pat"] + h["da"] + h["dtax"] - (h["inv"] - prev["inv"]) - (h["rec"] - prev["rec"])
                        + (h["pay"] - prev["pay"]) + (h["ocl"] - prev["ocl"]))
            pre = prev["cash"] + h["cfo"] - h["capex"] - h["capint"] - h["dplpay"] - h["div"]
            need = max(0.0, FLOOR - pre)
            if abs(need - h["newb"]) < 0.01:
                break
            h["newb"] = need
        h["cash"] = pre + h["newb"]
        h["borr"] = prev["borr"] + h["newb"]
        h["block"] = prev["block"] + h["capex"] + h["capint"] - h["da"]
        h["dtl"] = prev["dtl"] + h["dtax"]
        nci_div = 450.0 if i == 0 else 0.1 * h["div"]
        h["eq"] = prev["eq"] + h["pat_owner"] - (h["div"] - nci_div)
        h["nci"] = prev["nci"] + h["nci_pat"] - nci_div
        h["intpaid"] = h["fc"] + h["capint"] - LEASE_INT
        h = finish(h)
        assert abs(h["ta"] - h["tle"]) < 0.5, ("balance sheet does not balance", i, h["ta"], h["tle"])
        rows.append(h)
        prev = h
    return rows


RUNS = {name: project(a) for name, a in SCEN.items()}
B = RUNS["Base"]


def ratios(h, prev=None):
    nw = h["eq"] + h["nci"]
    out = dict(adj_debt=h["adj_debt"], nw=nw, gearing=h["adj_debt"] / nw,
               tol=(h["ta"] - nw) / nw, debt_pbdit=h["adj_debt"] / h["pbdit"],
               icr=h["pbdit"] / h["int_crisil"], margin=100 * h["pbdit"] / h["rev"],
               net_debt=h["adj_debt"] - h["cash"], nd_pbdit=(h["adj_debt"] - h["cash"]) / h["pbdit"],
               ncatd=(h["pat"] - h["div"] + h["da"]) / h["adj_debt"], cash=h["cash"])
    if prev is not None:
        ce = lambda x: x["adj_debt"] + x["eq"] + x["nci"] + x["dtl"]  # noqa: E731
        out["roce"] = 100 * (h["pbdit"] - h["da"]) / ((ce(h) + ce(prev)) / 2)
    return out


for p, pp in zip(H[1:], H[:-1]):  # model ratios must reproduce the engine's before projection
    r = ratios(HIST[p], HIST[pp])
    for mine, eng in (("gearing", "Gearing (x)"), ("icr", "Interest coverage (x)"),
                      ("debt_pbdit", "Adjusted debt/PBDIT (x)"), ("roce", "RoCE (%)"), ("tol", "TOL/ANW (x)")):
        assert abs(r[mine] - R[p][eng]) < 0.01, (p, mine, r[mine], R[p][eng])

# ===================================================================== workbook
HDR = PatternFill("solid", fgColor="1F3864")
HDRF = Font(bold=True, color="FFFFFF")
SUBF = PatternFill("solid", fgColor="D9E2F3")
PROJF = PatternFill("solid", fgColor="FFF2CC")
BOLD = Font(bold=True)
COLS = H + P
ROWS = {}


def sheet(wb, title, first="Rs crore"):
    ws = wb.create_sheet(title)
    ws.append([first, *COLS, "Source / note"])
    for c in ws[1]:
        c.fill, c.font = HDR, HDRF
        c.alignment = Alignment(horizontal="center", wrap_text=True)
    ws.column_dimensions["A"].width = 56
    for i in range(2, 2 + len(COLS)):
        ws.column_dimensions[get_column_letter(i)].width = 12
    ws.column_dimensions[get_column_letter(2 + len(COLS))].width = 70
    ws.freeze_panes = "B2"
    return ws


def put(ws, key, label, hv, pv, note="", fmt="#,##0", bold=False):
    ws.append([label, *[None if x is None else round(x, 4) for x in hv + pv], note])
    r = ws.max_row
    ROWS[(ws.title, key)] = r
    for j in range(2, 2 + len(COLS)):
        c = ws.cell(r, j)
        c.number_format = fmt
        if j >= 2 + len(H):
            c.fill = PROJF
    if bold:
        for c in ws[r]:
            c.font = BOLD
    return r


def section(ws, title):
    ws.append([title])
    for c in ws[ws.max_row]:
        c.fill = SUBF
    ws.cell(ws.max_row, 1).font = BOLD


def series(key, rows=B):
    return [HIST[p].get(key) for p in H], [r.get(key) for r in rows]


wb = openpyxl.Workbook()
wb.remove(wb.active)

ws = wb.create_sheet("Assumptions")
ws.append(["Reliance Industries Limited - consolidated 5-year model (Rs crore). Base case on every "
           "statement tab; Scenarios tab carries Bull / Bear (rating stress) / Tail."])
ws.cell(1, 1).font = Font(bold=True, size=12)
ws.append(["Generated by build_model.py from compute_ratios.py (208 tie-outs). FY2023-FY2026 audited; "
           "yellow = projection. Segment history FY2024-FY2026 (FY2023 segment split not extracted)."])
ws.append([])
ws.append(["Driver", *P, "Source / basis"])
for c in ws[ws.max_row]:
    c.fill, c.font = HDR, HDRF
for name, a in SCEN.items():
    section(ws, name.upper())
    for k in SEGS:
        ws.append(["Revenue growth - %s (%%)" % k, *a["g"][k], ASSUMPTION_TEXT[0][1] if (name == "Base" and k == "O2C") else ""])
    for k in SEGS:
        ws.append(["EBITDA margin - %s (%%)" % k, *a["m"][k], ASSUMPTION_TEXT[1][1] if (name == "Base" and k == "O2C") else ""])
    ws.append(["Capex - cash (Rs crore)", *a["capex"], ASSUMPTION_TEXT[2][1] if name == "Base" else ""])
    ws.append(["Share of gross interest capitalised (%)", *a["capshare"], ASSUMPTION_TEXT[3][1] if name == "Base" else ""])
    ws.append(["Working-capital shock (Rs crore)", *a["wc_shock"], ASSUMPTION_TEXT[4][1] if name != "Base" else ""])
ws.append([])
ws.append(["Fixed driver", "Value", "", "", "", "", "Source / basis"])
for c in ws[ws.max_row]:
    c.fill, c.font = HDR, HDRF
for label, val, src in FIXED:
    ws.append([label, val, "", "", "", "", src])
ws.column_dimensions["A"].width = 64
ws.column_dimensions["G"].width = 120
for col in "BCDEF":
    ws.column_dimensions[col].width = 12

ws = sheet(wb, "Revenue Model")
section(ws, "SEGMENT REVENUE (gross value of sales and services, audited segment information)")
for k in SEGS:
    put(ws, "rev_" + k, k, *series("rev_" + k), "segment information (Q4 FY2025 / Q4 FY2026 releases)")
put(ws, "interseg", "Less: inter-segment transfers", *series("interseg"), "segment information")
put(ws, "voss", "VALUE OF SALES AND SERVICES", *series("voss"), "P&L", bold=True)
put(ws, "gst", "Less: GST recovered", *series("gst"), "P&L")
put(ws, "rev", "REVENUE FROM OPERATIONS", *series("rev"), "P&L (engine tie-outs)", bold=True)
section(ws, "SEGMENT EBITDA")
for k in SEGS:
    put(ws, "ebitda_" + k, k, *series("ebitda_" + k), "segment results (EBITDA)")
section(ws, "OPERATING METRICS (history; drive the narrative, not the model)")
for k in ("Jio subscribers (mn)", "Jio ARPU Q4 (Rs/month)", "O2C throughput (MMT)", "KG D6 production (BCFe)",
          "Retail stores (nos.)"):
    put(ws, "op_" + k, k, [R[p][k] for p in H], [None] * 5, "Q4 releases", "#,##0.0")

ws = sheet(wb, "Income Statement")
put(ws, "rev", "Revenue from operations (net of GST)", *series("rev"), "P&L", bold=True)
put(ws, "pbdit", "PBDIT (CRISIL: incl. recurring other income, excl. one-time)", *series("pbdit"),
    "history = engine; projection = segment EBITDA + treasury yield + unallocable", bold=True)
put(ws, "onetime", "One-time income (profit on sale of listed investments)", *series("onetime"), "Q4 FY2026 release note 5")
put(ws, "da", "Depreciation, amortisation and depletion", *series("da"), "P&L; projected on opening block")
put(ws, "fc", "Finance costs (P&L, net of capitalised interest)", *series("fc"), "P&L / note 29")
put(ws, "capint", "Memo: interest capitalised", *series("capint"), "note 29 footnote")
put(ws, "pbt", "Profit before tax (before associates)", *series("pbt"), "P&L (tied)")
put(ws, "tax", "Tax expense (current + deferred)", *series("tax"), "P&L")
put(ws, "assoc", "Share of associates / JVs (+ FY2023 discontinued)", *series("assoc"), "P&L; not projected")
put(ws, "pat", "PROFIT FOR THE YEAR", *series("pat"), "P&L printed (tied)", bold=True)
put(ws, "nci_pat", "of which non-controlling interest", *series("nci_pat"), "P&L attribution")
put(ws, "pat_owner", "of which owners of the company", *series("pat_owner"), "P&L attribution")

ws = sheet(wb, "Cash Flow")
put(ws, "cfo", "Net cash from operating activities", *series("cfo"),
    "historical: cash-flow statement; projected: PAT + D&A + deferred tax - change in inventory and "
    "receivables + change in payables and other current liabilities (incl. the stress shock)", bold=True)
put(ws, "capex", "Capex - PPE, spectrum, intangibles", *series("capex"), "cash-flow statement")
put(ws, "capint", "Interest capitalised (paid in cash, added to block)", *series("capint"),
    "inside 'interest paid' historically")
put(ws, "dplpay", "Payment of DoT deferred payment liabilities", *series("dplpay"), "cash-flow statement")
put(ws, "div", "Dividends paid (owners + NCI)", *series("div"), "cash-flow statement")
put(ws, "newb", "New borrowing (DERIVED: funding gap below the cash floor)", [None] * 4,
    [r["newb"] for r in B], "zero unless cash + current investments < floor")
put(ws, "cash", "Closing cash and current investments", *series("cash"), "balance sheet", bold=True)

ws = sheet(wb, "Balance Sheet")
BSL = [("block", "Capital block (PPE, spectrum, intangibles, goodwill, CWIP, under development)"),
       ("onca", "Investments and other non-current assets"), ("inv", "Inventories"),
       ("rec", "Trade receivables"), ("cash", "Cash and current investments"), ("oca", "Other current assets"),
       ("ta", "TOTAL ASSETS"), ("eq", "Equity attributable to owners"), ("nci", "Non-controlling interest"),
       ("borr", "Borrowings (non-current + current)"), ("lease", "Lease liabilities"),
       ("dpl", "DoT deferred payment liabilities (non-current + current)"), ("dtl", "Deferred tax liabilities"),
       ("oncl", "Other non-current liabilities and provisions"), ("pay", "Trade payables (incl. supplier finance)"),
       ("ocl", "Other current liabilities (incl. contract liabilities; excl. current DPL)"),
       ("tle", "TOTAL EQUITY AND LIABILITIES")]
for k, lab in BSL:
    put(ws, k, lab, *series(k), "consolidated balance sheet (grouped; totals tie to the AR)" if k in ("ta", "tle") else "",
        bold=k in ("ta", "tle", "eq"))
put(ws, "chk", "Check: assets - (equity + liabilities)", [HIST[p]["ta"] - HIST[p]["tle"] for p in H],
    [r["ta"] - r["tle"] for r in B], "must be zero in every column")

ws = sheet(wb, "Credit Ratios", "CRISIL convention (formulas)")
IS_, BS_ = "Income Statement", "Balance Sheet"


def ref(tab, key, col):
    return "'%s'!%s%d" % (tab, col, ROWS[(tab, key)])


def cr(key):
    return ROWS[("Credit Ratios", key)]


DEFS = (
    ("m", "PBDIT margin (%)", "0.00", lambda c, pc: "=100*%s/%s" % (ref(IS_, "pbdit", c), ref(IS_, "rev", c))),
    ("pm", "PAT margin (%)", "0.00", lambda c, pc: "=100*%s/%s" % (ref(IS_, "pat", c), ref(IS_, "rev", c))),
    ("ad", "Adjusted total debt (borrowings + leases + DoT liabilities)", "#,##0", lambda c, pc: "=%s+%s+%s" % (
        ref(BS_, "borr", c), ref(BS_, "lease", c), ref(BS_, "dpl", c))),
    ("nw", "Adjusted networth (owners + NCI)", "#,##0", lambda c, pc: "=%s+%s" % (ref(BS_, "eq", c), ref(BS_, "nci", c))),
    ("g", "Gearing - adjusted debt / adjusted networth (x)", "0.00", lambda c, pc: "=%s%d/%s%d" % (c, cr("ad"), c, cr("nw"))),
    ("tol", "TOL / adjusted networth (x)", "0.00", lambda c, pc: "=(%s-%s%d)/%s%d" % (ref(BS_, "ta", c), c, cr("nw"), c, cr("nw"))),
    ("dp", "Adjusted debt / PBDIT (x)", "0.00", lambda c, pc: "=%s%d/%s" % (c, cr("ad"), ref(IS_, "pbdit", c))),
    ("int", "Interest incl. capitalised", "#,##0", lambda c, pc: "=%s+%s" % (ref(IS_, "fc", c), ref(IS_, "capint", c))),
    ("icr", "Interest coverage - PBDIT / interest incl. capitalised (x)", "0.00",
     lambda c, pc: "=%s/%s%d" % (ref(IS_, "pbdit", c), c, cr("int"))),
    ("ncatd", "NCATD - (PAT - dividend + D&A) / adjusted debt (x)", "0.00", lambda c, pc: "=(%s-%s+%s)/%s%d" % (
        ref(IS_, "pat", c), ref("Cash Flow", "div", c), ref(IS_, "da", c), c, cr("ad"))),
    ("roce", "RoCE - PBIT / avg (adj. debt + adj. networth + DTL) (%)", "0.00", lambda c, pc: None if pc is None else
     "=100*(%s-%s)/((%s%d+%s%d+%s+%s%d+%s%d+%s)/2)" % (
         ref(IS_, "pbdit", c), ref(IS_, "da", c), c, cr("ad"), c, cr("nw"), ref(BS_, "dtl", c),
         pc, cr("ad"), pc, cr("nw"), ref(BS_, "dtl", pc))),
    ("nd", "Net adjusted debt (adj. debt - cash and current investments)", "#,##0",
     lambda c, pc: "=%s%d-%s" % (c, cr("ad"), ref(BS_, "cash", c))),
    ("ndp", "Net adjusted debt / PBDIT (x)", "0.00", lambda c, pc: "=%s%d/%s" % (c, cr("nd"), ref(IS_, "pbdit", c))),
)
for key, lab, fmt, f in DEFS:
    ws.append([lab])
    r = ws.max_row
    ROWS[("Credit Ratios", key)] = r
    for j in range(len(COLS)):
        c = get_column_letter(2 + j)
        pc = get_column_letter(1 + j) if j > 0 else None
        cell = ws.cell(r, 2 + j)
        cell.value = f(c, pc)
        cell.number_format = fmt
        if j >= len(H):
            cell.fill = PROJF
ws.append([])
ws.append(["Supplier finance (note 44) is NOT in adjusted debt here; adding it (76,377 FY2026) takes gearing "
           "to 0.53x and adjusted debt/PBDIT to 2.91x (engine 'incl. SF' rows). Net-debt rows use cash + "
           "current investments only; the AR's own 'cash and marketable securities' also adds 6,296 of "
           "other marketable securities (FY2026)."])

ws = wb.create_sheet("Scenarios")
ws.append(["Scenario / metric", *P, "Note"])
for c in ws[1]:
    c.fill, c.font = HDR, HDRF
ws.column_dimensions["A"].width = 58
ws.column_dimensions["G"].width = 60
SCEN_OUT = {}
for name, rows in RUNS.items():
    section(ws, name.upper())
    prevs = [F] + rows[:-1]
    rr = [ratios(h, pv) for h, pv in zip(rows, prevs)]
    SCEN_OUT[name] = rr
    for lab, f, fmt in (("Revenue from operations", lambda h, r: h["rev"], "#,##0"),
                        ("PBDIT", lambda h, r: h["pbdit"], "#,##0"),
                        ("PBDIT margin (%)", lambda h, r: r["margin"], "0.00"),
                        ("PAT", lambda h, r: h["pat"], "#,##0"),
                        ("Cash and current investments", lambda h, r: r["cash"], "#,##0"),
                        ("New borrowing drawn (funding gap)", lambda h, r: h["newb"], "#,##0"),
                        ("Adjusted total debt", lambda h, r: r["adj_debt"], "#,##0"),
                        ("Gearing (x)", lambda h, r: r["gearing"], "0.00"),
                        ("Adjusted debt / PBDIT (x)", lambda h, r: r["debt_pbdit"], "0.00"),
                        ("Net adjusted debt / PBDIT (x)", lambda h, r: r["nd_pbdit"], "0.00"),
                        ("Interest coverage incl. capitalised (x)", lambda h, r: r["icr"], "0.00"),
                        ("NCATD (x)", lambda h, r: r["ncatd"], "0.00"),
                        ("RoCE (%)", lambda h, r: r["roce"], "0.00")):
        ws.append([lab, *[None if f(h, r) is None else round(f(h, r), 2) for h, r in zip(rows, rr)]])
        for j in range(2, 7):
            ws.cell(ws.max_row, j).number_format = fmt

# ---- DCF Inputs + Valuation (Task 3: financial flexibility only, never the grade) ----
ws = sheet(wb, "DCF Inputs")
nwc = lambda h: h["inv"] + h["rec"] - h["pay"] - h["ocl"]  # noqa: E731
ufcf = []
for i, h in enumerate(B):
    pv_ = F if i == 0 else B[i - 1]
    ufcf.append(h["pbdit"] - h["treasury"] - TAX / 100 * (1 - DEF_SHARE / 100) * (h["pbdit"] - h["treasury"] - h["da"])
                - h["capex"] - (nwc(h) - nwc(pv_)))
put(ws, "pbdit", "PBDIT", *series("pbdit"), "Income Statement")
put(ws, "treas", "Less: treasury income (valued separately as cash)", [None] * 4, [h["treasury"] for h in B], "")
put(ws, "capex", "Less: capex", *series("capex"), "")
put(ws, "ufcf", "UNLEVERED FREE CASH FLOW (after cash tax on EBIT, capex and working capital)", [None] * 4, ufcf, "",
    bold=True)

WACC, G = 11.0, 5.0
SHARES = 1353.2472634  # crore shares (FY2026 AR shareholding distribution: 1353,24,72,634)
PRICE, MCAP = 1170.0, 1583713.0  # screener.in, read 10-Oct-2026 (not exchange-verified)


def dcf(wacc, g):
    pv = sum(cf / (1 + wacc / 100) ** (i + 1) for i, cf in enumerate(ufcf))
    tv = ufcf[-1] * (1 + g / 100) / ((wacc - g) / 100)
    return pv + tv / (1 + wacc / 100) ** 5


ND26 = R["FY2026"]["Net adjusted debt"]
NCI_BOOK = F["nci"]
ws = wb.create_sheet("Valuation")
ws.append(["Valuation (Rs crore) - informs financial flexibility only (Step 12(f)); it does not move the grade."])
ws.cell(1, 1).font = BOLD
ws.append(["ANALYST ASSUMPTIONS: WACC 11.0% (cost of equity ~12%, post-tax cost of debt ~6%, ~20% debt weight); "
           "terminal growth 5.0% nominal. Minority interests deducted at book (no market value disclosed)."])
EV = dcf(WACC, G)
EQV = EV - ND26 - NCI_BOOK
for lab, val, note in (
        ("Enterprise value (WACC 11.0%, g 5.0%)", EV, ""),
        ("Less: net adjusted debt 31-Mar-2026 (incl. DoT, leases; cash and marketable securities netted)", ND26, "engine"),
        ("Less: non-controlling interest at book 31-Mar-2026", NCI_BOOK, "balance sheet"),
        ("Implied equity value", EQV, ""),
        ("Implied value per share (Rs)", EQV / SHARES, "1,353.25 crore shares"),
        ("Market price (Rs, screener.in 10-Oct-2026; not exchange-verified)", PRICE, "52-week range Rs 1,160-1,612"),
        ("Market capitalisation (Rs crore, screener.in)", MCAP, ""),
        ("Market capitalisation / adjusted total debt 31-Mar-2026 (x)", MCAP / R["FY2026"]["Adjusted total debt"],
         "the financial-flexibility reading: equity cushion over debt"),
        ("Market capitalisation / adjusted debt incl. supplier finance (x)",
         MCAP / R["FY2026"]["Adjusted total debt incl. supplier finance"], "")):
    ws.append([lab, round(val, 2), note])
ws.append([])
ws.append(["Sensitivity: equity value (Rs crore)", *["g %.1f%%" % g for g in (4.0, 4.5, 5.0, 5.5, 6.0)]])
SENS = {}
for w in (10.0, 10.5, 11.0, 11.5, 12.0):
    SENS[w] = [dcf(w, g) - ND26 - NCI_BOOK for g in (4.0, 4.5, 5.0, 5.5, 6.0)]
    ws.append(["WACC %.1f%%" % w, *[round(x, 0) for x in SENS[w]]])
ws.column_dimensions["A"].width = 90
for col in "BCDEF":
    ws.column_dimensions[col].width = 14

# ---- Debt Breakup ----
ws = wb.create_sheet("Debt Breakup")
ws.column_dimensions["A"].width = 70
for col in "BCDE":
    ws.column_dimensions[col].width = 13
ws.column_dimensions["F"].width = 90


def drow(*vals):
    ws.append(list(vals))


drow("(i) STATUTORY BORROWINGS - consolidated (Rs crore)", "FY2023", "FY2024", "FY2025", "FY2026", "Source")
drow("Non-current borrowings", *[v(E.NCL, "Non-current borrowings", p) for p in H], "balance sheet (note 16)")
drow("Current borrowings (incl. current maturities)", *[v(E.CL, "Current borrowings", p) for p in H], "balance sheet (note 20)")
drow("  of which current maturities of non-current borrowings",
     *[v(E.DEBT_NOTES, "Current maturities of NC borrowings", p) for p in H], "note 20")
drow("  of which commercial paper", *[v(E.DEBT_NOTES, "Commercial paper", p) for p in H], "note 20")
drow("GROSS DEBT (company definition)", *[E.borrowings(p) for p in H], "equals note 35 gross debt; screener.in tie in spreads")
drow("Lease liabilities (non-current + current)", *[E.leases(p) for p in H], "balance sheet")
drow("DoT deferred payment liabilities (note 17 + current maturity in note 22)", *[E.dpl(p) for p in H], "notes 17, 22")
drow("ADJUSTED TOTAL DEBT (CRISIL)", *[R[p]["Adjusted total debt"] for p in H], "engine")
drow("Supplier-finance arrangements (in trade payables / other financial liabilities)",
     None, None, E.supplier_finance("FY2025"), E.supplier_finance("FY2026"), "note 44; first disclosed for FY2025")
drow("ADJUSTED DEBT incl. supplier finance", None, None, R["FY2025"]["Adjusted total debt incl. supplier finance"],
     R["FY2026"]["Adjusted total debt incl. supplier finance"], "wide measure")
drow()
drow("(ii) INSTRUMENT VIEW (note 16 / 20, FY2025-26 AR)", "", "", "FY2025", "FY2026", "")
for k in E.NC_BORROW_LINES:
    drow("NC: " + k, "", "", v(E.NC_BORROW_LINES, k, "FY2025"), v(E.NC_BORROW_LINES, k, "FY2026"), "note 16")
for k in E.CB_LINES:
    drow("Current: " + k, "", "", v(E.CB_LINES, k, "FY2025"), v(E.CB_LINES, k, "FY2026"), "note 20")
drow("Secured NCDs: 7.79% Rs 20,000 crore (15,000 due 2033-34; 5,000 due 2032-33)", "", "", "", 20000,
     "note 16.3 (face); unsecured NCDs 7,389 at 8.65-9.05% due 2028-29")
drow("DoT liabilities by auction: Mar-2021 7.30% / Aug-2022 7.20% / Jul-2024 8.65%", "", "", "",
     "30,213 / 73,425 / 876", "note 17 footnote")
drow("Currency mix", "", "", "", "", "foreign-currency bonds 57,274 (NC) + 510 (current); FC term loans and "
     "ECBs inside term loans - split not disclosed in the notes read")
drow()
drow("(iii) THE AR'S OWN NET-DEBT BRIDGE (note 35)", "FY2023", "FY2024", "FY2025", "FY2026", "")
for k in ("Gross debt", "Cash and marketable securities", "Net debt", "Equity attributable to owners"):
    drow(k, *[v(E.AR_NET_DEBT, k, p) for p in H], "note 35 capital management")
drow("Arithmetic: gross debt - cash & MS", *[v(E.AR_NET_DEBT, "Gross debt", p) - v(E.AR_NET_DEBT, "Cash and marketable securities", p)
                                             for p in H], "equals printed net debt every year")
drow("Company net gearing (x)", *[round(R[p]["Company net gearing (x)"], 2) for p in H], "printed 0.18 / 0.15 / 0.14 / 0.14")
drow("Analyst net adjusted debt (adds leases + DoT liabilities)", *[R[p]["Net adjusted debt"] for p in H],
     "basis difference: company net debt excludes leases (23,579) and DoT liabilities (1,04,514) in FY2026")
drow()
drow("(iv) RATED LIMITS vs DRAWN DEBT", "", "", "", "Rs crore", "")
drow("CRISIL bank facilities - CRA-PUBLISHED 30-Mar-2026 (Credit Bulletin), NOT issuer-confirmed", "", "", "",
     "see rationale Annexure", "ECB 23,424 + fund-based 22,740 + non-fund-based 50,510 + proposed 326 + term loan 3,000")
drow("Drawn borrowings 31-Mar-2026 (consolidated, all entities)", "", "", "", E.borrowings("FY2026"),
     "limits (RIL facilities) and consolidated drawn debt are different measures and are not expected to reconcile")
for row in ws.iter_rows(min_row=1):
    if row[0].value and str(row[0].value).startswith("("):
        for c in row:
            c.fill, c.font = HDR, HDRF

wb.move_sheet("Assumptions", offset=-len(wb.sheetnames))
wb.save(OUT)
print("wrote", os.path.basename(OUT), "sheets:", wb.sheetnames)

for name, rr in SCEN_OUT.items():
    rows = RUNS[name]
    worst = min(range(5), key=lambda i: rr[i]["icr"])
    print("%-22s FY27 rev %9.0f PBDIT %8.0f | trough %s: ICR %5.2fx debt/PBDIT %4.2fx gearing %4.2fx NCATD %4.2f "
          "cash %8.0f | new debt %7.0f | FY31 debt/PBDIT %4.2fx"
          % (name, rows[0]["rev"], rows[0]["pbdit"], P[worst], rr[worst]["icr"], rr[worst]["debt_pbdit"],
             rr[worst]["gearing"], rr[worst]["ncatd"], rr[worst]["cash"], sum(h["newb"] for h in rows),
             rr[-1]["debt_pbdit"]))
print("DCF equity value Rs %.0f crore (Rs %.0f/share) at WACC %.1f%% g %.1f%%; price Rs %.0f"
      % (EQV, EQV / SHARES, WACC, G, PRICE))

# ===================================================================== Task 4 - charts
import zipfile  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

plt.rcParams.update({"font.family": "Times New Roman", "font.size": 10})
CH = os.path.join(HERE, "charts")
os.makedirs(CH, exist_ok=True)
NAVY, TEAL, GREY, RED, GOLD = "#1F3864", "#2E8B8B", "#9E9E9E", "#C0392B", "#F5B041"
YRS = [p.replace("FY20", "FY") for p in H] + [p.replace("FY20", "FY") for p in P]
INDEX = []


def save(fig, name, title, src):
    fig.savefig(os.path.join(CH, name), dpi=300, bbox_inches="tight")
    plt.close(fig)
    INDEX.append("%s | %s | %s" % (name, title, src))


SY = ["FY24", "FY25", "FY26"] + [p.replace("FY20", "FY") for p in P]
fig, ax = plt.subplots(figsize=(8, 4.2))
stack = [[HIST[p]["ebitda_" + k] for p in H[1:]] + [r["ebitda_" + k] for r in B] for k in SEGS]
ax.stackplot(SY, stack, labels=SEGS, colors=[NAVY, GREY, GOLD, TEAL, "#7FB3D5"])
ax.axvline(2.5, color="black", ls="--", lw=0.8)
ax.set_ylabel("Rs crore")
ax.legend(fontsize=8, loc="upper left")
ax.set_title("Segment EBITDA: consumer businesses overtook energy (FY2024-26 actual, base case FY2027-31)")
save(fig, "chart_01_segment_ebitda.png", "Segment EBITDA mix", "segment information; model base case")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(H, [R[p]["PBDIT margin (%)"] for p in H], color=NAVY, marker="o", label="PBDIT margin (%)")
ax.set_ylabel("PBDIT margin (%)")
ax2 = ax.twinx()
ax2.bar(H, [R[p]["Interest coverage (x)"] for p in H], color=TEAL, alpha=0.35)
ax2.set_ylabel("Interest coverage incl. capitalised interest (x)")
ax.set_title("PBDIT margin and interest coverage (CRISIL definitions), FY2023-26")
save(fig, "chart_02_margin_coverage.png", "Margin and coverage", "engine")

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(H, [R[p]["Adjusted total debt"] for p in H], color=NAVY, label="Adjusted debt")
ax.bar(H, [-R[p]["Cash and marketable securities"] for p in H], color=TEAL, label="Cash & marketable securities (neg.)")
ax.plot(H, [R[p]["Net adjusted debt"] for p in H], color=RED, marker="o", label="Net adjusted debt")
ax.axhline(0, color=GREY, lw=0.6)
ax.legend(fontsize=8)
ax.set_ylabel("Rs crore")
ax.set_title("Adjusted debt, liquidity and net adjusted debt")
save(fig, "chart_03_debt_liquidity.png", "Debt and liquidity", "engine")

fig, ax = plt.subplots(figsize=(8, 4))
for (name, rr), col in zip(SCEN_OUT.items(), [NAVY, TEAL, GOLD, RED]):
    ax.plot([p.replace("FY20", "FY") for p in P], [r["debt_pbdit"] for r in rr], marker="o", color=col, label=name)
ax.set_ylabel("Adjusted debt / PBDIT (x)")
ax.legend(fontsize=8)
ax.set_title("Adjusted debt / PBDIT by scenario")
save(fig, "chart_04_scenario_leverage.png", "Scenario leverage", "model Scenarios tab")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(["FY24", "FY25", "FY26"], [R[p]["Jio subscribers (mn)"] for p in H[1:]], color=NAVY, marker="o")
ax.set_ylabel("Jio subscribers (million)")
ax2 = ax.twinx()
ax2.plot(["FY24", "FY25", "FY26"], [R[p]["Jio ARPU Q4 (Rs/month)"] for p in H[1:]], color=RED, marker="s")
ax2.set_ylabel("Q4 ARPU (Rs/month)")
ax.set_title("Digital Services: subscribers and ARPU")
save(fig, "chart_05_jio_kpis.png", "Jio subscribers and ARPU", "Q4 releases")

fig, ax = plt.subplots(figsize=(6.5, 4))
gs = [4.0, 4.5, 5.0, 5.5, 6.0]
wl = sorted(SENS)
mat = [[SENS[w][j] / SHARES for j in range(5)] for w in wl]
im = ax.imshow(mat, cmap="RdYlGn", aspect="auto")
ax.set_xticks(range(5), ["g %.1f%%" % g for g in gs])
ax.set_yticks(range(5), ["WACC %.1f%%" % w for w in wl])
for i in range(5):
    for j in range(5):
        ax.text(j, i, "%.0f" % mat[i][j], ha="center", va="center", fontsize=8)
fig.colorbar(im, label="Rs per share")
ax.set_title("DCF sensitivity - value per share (Rs)")
save(fig, "chart_06_dcf_sensitivity.png", "DCF sensitivity", "model Valuation tab")

ZIP = os.path.join(HERE, "RIL_Charts_10Oct2026.zip")
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for line in INDEX:
        z.write(os.path.join(CH, line.split(" | ")[0]), line.split(" | ")[0])
    z.writestr("chart_index.txt", "file | title | source\n" + "\n".join(INDEX) + "\n")
print("wrote %d charts + %s" % (len(INDEX), os.path.basename(ZIP)))
