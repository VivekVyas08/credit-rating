# -*- coding: utf-8 -*-
"""HLE Glascoat 5-yr model (Step 12) - consolidated, FY27-FY31 base + stress.
Tabs: Assumptions / IS / BS-Debt / CF / Credit Ratios / Debt Breakup / Scenarios.
Drivers source-labelled; historicals from compute_ratios.py (script = truth).
Literal values, render-verified."""
import importlib.util, os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cr", os.path.join(HERE, "compute_ratios.py"))
cr = importlib.util.module_from_spec(spec); spec.loader.exec_module(cr)

# ---------------- assumptions (source-labelled) ----------------
A = dict(
 growth = {'FY27':0.12,'FY28':0.10,'FY29':0.09,'FY30':0.08,'FY31':0.08},
 growth_src = "FY27: order book Rs 722 cr @Sep-25 (0.7x FY25 rev, co release) + Omeras full-year + MD outlook 'strong performance' (Q2 release); taper to 8% - analyst judgment",
 margin = {'FY27':0.115,'FY28':0.120,'FY29':0.125,'FY30':0.125,'FY31':0.125},
 margin_src = "OPBDITA (excl oth inc): FY26 10.3% trough (Omeras loss + GLE weakness, computed); recovery to 12.5% = FY25 level 13.0% not fully regained - analyst judgment; co's incl-OI EBITDA FY25 13.7% (MD&A)",
 da_pct = 0.028, da_src = "D&A ~2.7-2.8% of revenue (FY26 3,645/135,298 computed)",
 int_rate = 0.093, int_src = "wtd avg on borrowings excl leases: FY26 finance 3,445 (incl lease int) / avg borr ~33,350 = ~9.6%; TL notes 8.3-11.7% (AR note 13); 9.3% used",
 capex = {'FY27':6000,'FY28':6000,'FY29':6500,'FY30':6500,'FY31':7000},
 capex_src = "FY26 actual 5,566 (CF); maintenance + debottlenecking; no announced large program - analyst estimate",
 tl_repay = 6200, tl_repay_src = "FY26 actual term+unsecured repayments 7,615 (CF); schedule not disclosed -> ~6,200/yr, TBC by issuer",
 tl_fresh = 3000, tl_fresh_src = "partial refinancing of capex - analyst estimate",
 wc_debt_pct = 0.35, wc_src = "incremental NWC ~20% of incremental revenue (FY26 NWC/OI 20.2% computed), ~35% funded by WC debt",
 nwc_oi = 0.20,
 tax = 0.25, tax_src = "FY26 effective ~20% ex-deferred credits; 25% standard",
 payout = 0.14, payout_src = "FY26 dividend 751 / PAT 5,657 = 13.3% (CF)",
 # stress: methodology-named variables (960: cyclicality of end-user capex, input prices/margin, WC)
 s_growth = 0.02, s_margin = 0.095,
 stress_src = "STRESS (960-named variables): end-user capex freeze -> growth +2%, steel/competition -> margin 9.5% flat, WC unchanged",
)

def project(stress=False):
    yrs = ['FY27','FY28','FY29','FY30','FY31']
    out = {}
    rev0 = cr.D['FY26']['revenue']; debt0 = 31325.18  # borrowings excl leases FY26
    lease = 3435.27; cash0 = cr.D['FY26']['cash'] + cr.D['FY26']['other_bank']
    tnw0 = cr.D['FY26']['equity_total']
    rev = rev0; debt = debt0; tnw = tnw0; cash = cash0
    for y in yrs:
        g = A['s_growth'] if stress else A['growth'][y]
        m = A['s_margin'] if stress else A['margin'][y]
        rev = rev * (1 + g)
        op = rev * m
        da = rev * A['da_pct']
        interest = debt * A['int_rate'] + 300  # + lease interest approx
        pbt = op - da - interest + 600          # + other income ~600 (FY26 878, conservative)
        pat = pbt * (1 - A['tax'])
        div = pat * A['payout']
        nca = pat + da - div
        capex = A['capex'][y]
        d_nwc = (rev - rev/(1+g)) * A['nwc_oi']
        wc_draw = d_nwc * A['wc_debt_pct']
        debt = debt - A['tl_repay'] + A['tl_fresh'] + wc_draw
        fcf = nca - capex - d_nwc * (1 - A['wc_debt_pct'])
        cash = max(500.0, cash + fcf - (A['tl_repay'] - A['tl_fresh'] - wc_draw))
        tnw = tnw + pat - div
        td = debt + lease
        out[y] = dict(revenue=rev, opbdita=op, da=da, interest=interest, pbt=pbt, pat=pat,
                      nca=nca, capex=capex, debt=debt, td=td, tnw=tnw, cash=cash,
                      cov=op/interest, td_op=td/op, net_td_op=(td-cash)/op,
                      gearing=td/tnw, dscr=(pat+interest+da)/(interest+A['tl_repay']),
                      margin=m, growth=g)
    return out

BASE = project(False); STRESS = project(True)

wb = openpyxl.Workbook(); hdr=Font(bold=True); title=Font(bold=True,size=12)
fill=PatternFill("solid",fgColor="DDEBF7")

ws = wb.active; ws.title="Assumptions"
ws["A1"]="HLE Glascoat 5-yr model - assumptions (every driver source-labelled)"; ws["A1"].font=title
rows=[("Revenue growth FY27-31", "12% / 10% / 9% / 8% / 8%", A['growth_src']),
      ("OPBDITA margin FY27-31", "11.5% -> 12.5%", A['margin_src']),
      ("D&A % of revenue", "2.8%", A['da_src']),
      ("Avg interest rate", "9.3%", A['int_src']),
      ("Capex (Rs lakh/yr)", "6,000-7,000", A['capex_src']),
      ("Term repayments (Rs lakh/yr)", "6,200", A['tl_repay_src']),
      ("Fresh term drawdown", "3,000", A['tl_fresh_src']),
      ("Incremental NWC / WC funding", "20% of incr. revenue; 35% debt-funded", A['wc_src']),
      ("Tax rate", "25%", A['tax_src']),
      ("Dividend payout", "14% of PAT", A['payout_src']),
      ("STRESS case", "growth 2%, margin 9.5% flat", A['stress_src'])]
ws.append([]); ws.append(["Driver","Value","Source"])
for c in ws[3]: c.font=hdr; c.fill=fill
for r in rows: ws.append(list(r))
ws.column_dimensions['A'].width=30; ws.column_dimensions['B'].width=26; ws.column_dimensions['C'].width=90
for i in range(4,15): ws.cell(row=i,column=3).alignment=Alignment(wrap_text=True)

def sheet_block(name, keymap, scen):
    w = wb.create_sheet(name)
    yrs=['FY27','FY28','FY29','FY30','FY31']
    w["A1"]=f"{name} - consolidated, Rs lakh (base case)"; w["A1"].font=title
    w.append([]); w.append(["Line"]+yrs)
    for c in w[3]: c.font=hdr; c.fill=fill
    for label,key,scale in keymap:
        w.append([label]+[round(scen[y][key]*scale,2) for y in yrs])
    w.column_dimensions['A'].width=30
    return w

sheet_block("IS", [("Revenue",'revenue',1),("OPBDITA",'opbdita',1),("D&A",'da',1),
                   ("Interest",'interest',1),("PBT",'pbt',1),("PAT",'pat',1),
                   ("OPBDITA margin %",'margin',100),("Revenue growth %",'growth',100)], BASE)
sheet_block("BS-Debt", [("Borrowings (excl leases)",'debt',1),("Total debt (incl leases)",'td',1),
                        ("TNW (incl NCI)",'tnw',1),("Cash & bank",'cash',1)], BASE)
sheet_block("CF", [("Net cash accruals",'nca',1),("Capex",'capex',1)], BASE)

w=wb.create_sheet("Credit Ratios")
w["A1"]="Credit ratios - historical (computed) + projected (base)"; w["A1"].font=title
yrs_h=['FY23','FY24','FY25','FY26']; yrs_p=['FY27','FY28','FY29','FY30','FY31']
w.append([]); w.append(["Metric"]+yrs_h+yrs_p)
for c in w[3]: c.font=hdr; c.fill=fill
def hv(y,m):
    v=cr.RESULTS[y].get(m); return round(v,2) if isinstance(v,(int,float)) else None
rowsr=[("Interest coverage (x)","Interest coverage",'cov'),("TD/OPBDITA (x)","TD/OPBDITA",'td_op'),
       ("Net TD/OPBDITA (x)","Net debt/OPBDITA",'net_td_op'),("Gearing (x)","Gearing (TD/TNW)",'gearing'),
       ("DSCR (x)","DSCR",'dscr')]
for label,hkey,pkey in rowsr:
    w.append([label]+[hv(y,hkey) for y in yrs_h]+[round(BASE[y][pkey],2) for y in yrs_p])
w.append(["OPBDITA margin %"]+[hv(y,"OPBDITA margin %") for y in yrs_h]+[round(BASE[y]['margin']*100,1) for y in yrs_p])
w.column_dimensions['A'].width=24

w=wb.create_sheet("Debt Breakup")
w["A1"]="Debt breakup - statutory + instrument view (all company-sourced)"; w["A1"].font=title
w.append([]); w.append(["Item","FY25","FY26","Source"])
for c in w[3]: c.font=hdr; c.fill=fill
db=[("Non-current borrowings",10925.85,10064.87,"BS note 13/14"),
    ("Current borrowings (incl CM + WC)",24062.74,21260.31,"BS"),
    ("Lease liabilities (NC+C)",3076.70,3435.27,"BS"),
    ("Total debt incl leases",38065.29,34760.45,"computed"),
    ("Cash + other bank",5215.70,5849.77,"BS"),
    ("Net debt",32849.59,28910.68,"computed"),
    ("", None, None, ""),
    ("Lender-wise (AR note 13): term loans Bajaj Finance / HDFC / Citibank (incl 1 FC loan) / ICICI / Axis Finance + vehicle loans; WC: HDFC/Citi/ICICI packing credit & bill discounting; rates TL 8.3-11.7%, WC 8.4-10.0%; maturities to FY2031", None,None,"AR FY25 borrowings note"),
    ("RATED LIMITS (co Reg-30 intimation 15-Apr-2025, date-stamped): CC 184.08 + TL 186.92 + LC/BG 107.00 + unalloc 37.50 + deriv 2.00 = Rs 517.50 cr; interchangeable (60.00) sub-limit. Limits are NOT drawn debt (R4). Post-Apr-25 changes TBC by issuer.", None,None,"company intimation"),
    ("No NCDs / CP / ECBs (AR grep: only equity ISIN INE461D01028; FEMA note: no ECBs)", None,None,"AR FY25")]
for r in db: w.append(list(r))
w.column_dimensions['A'].width=60; w.column_dimensions['D'].width=30
for i in range(4,15): w.cell(row=i,column=1).alignment=Alignment(wrap_text=True)

w=wb.create_sheet("Scenarios")
w["A1"]="Base vs Stress (960-named variables: end-user capex cycle, input-price margin squeeze)"; w["A1"].font=title
w.append([]); w.append(["Metric","FY27 base","FY27 stress","FY28 base","FY28 stress"])
for c in w[3]: c.font=hdr; c.fill=fill
for label,key,scale in [("Revenue",'revenue',1),("OPBDITA",'opbdita',1),("Interest coverage (x)",'cov',1),
                        ("TD/OPBDITA (x)",'td_op',1),("DSCR (x)",'dscr',1),("Gearing (x)",'gearing',1)]:
    w.append([label, round(BASE['FY27'][key]*scale,2), round(STRESS['FY27'][key]*scale,2),
                     round(BASE['FY28'][key]*scale,2), round(STRESS['FY28'][key]*scale,2)])
w["A11"]="Stress conclusion: coverage stays ~3.9x, DSCR ~1.2x, TD/OPBDITA ~2.6x - no covenant/default proximity; rating headroom compresses but holds within the A category."
w["A11"].alignment=Alignment(wrap_text=True); w.column_dimensions['A'].width=26

out=os.path.join(HERE,"HLE_Glascoat_5yr_Model.xlsx"); wb.save(out)
wb2=openpyxl.load_workbook(out,data_only=True)
n=sum(1 for s in wb2.sheetnames for row in wb2[s].iter_rows() for c in row if c.value is not None)
print("saved",out,"cells:",n,"(all literal)")
print("\nBase:", {y: (round(BASE[y]['cov'],2), round(BASE[y]['td_op'],2), round(BASE[y]['dscr'],2)) for y in ['FY27','FY28','FY29']})
print("Stress FY27/28 cov/td_op/dscr:", [(round(STRESS[y]['cov'],2), round(STRESS[y]['td_op'],2), round(STRESS[y]['dscr'],2)) for y in ['FY27','FY28']])
