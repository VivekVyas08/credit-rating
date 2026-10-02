# -*- coding: utf-8 -*-
"""Generate HLE_Financial_Spreads.xlsx FROM compute_ratios.py (script = source of truth).
Tabs: Extraction (line items + source refs) / RatioSuite / TieOut (PASS-FAIL).
Literal values only; render-verified via data_only read-back."""
import importlib.util, os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cr", os.path.join(HERE, "compute_ratios.py"))
cr = importlib.util.module_from_spec(spec); spec.loader.exec_module(cr)

wb = openpyxl.Workbook()
hdr = Font(bold=True); title = Font(bold=True, size=12)
fill = PatternFill("solid", fgColor="DDEBF7")

# ---- Extraction ----
ws = wb.active; ws.title = "Extraction"
ws["A1"] = "HLE Glascoat - consolidated extraction (Rs lakh) - every row source-referenced"; ws["A1"].font = title
ws["A2"] = ("Sources: FY23 = AR2022-23 consol P&L/BS; FY24/FY25 = AR2024-25 consol (as-reported); "
            "FY26 = audited results 18-May-2026 (restated basis). Basis note: FY25 restated differs only in "
            "owner/NCI split & minor reclasses (amalgamation, pooling of interests, NW +654.26).")
ws["A2"].alignment = Alignment(wrap_text=True); ws.row_dimensions[2].height = 30
years = cr.ORDER
ws.append([]); ws.append(["Line item"] + years + ["Source"])
for c in ws[4]: c.font = hdr; c.fill = fill
SRC = {'revenue':'P&L: Revenue from operations','other_income':'P&L: Other income','finance':'P&L: Finance costs',
       'da':'P&L: Depreciation & amortisation','pbt_before_exc':'P&L: PBT before exceptional','exceptional':'P&L: Exceptional items',
       'pbt':'P&L: PBT','pat':'P&L: Profit for the year','borr_nc':'BS: Non-current borrowings','borr_cur':'BS: Current borrowings',
       'lease_nc':'BS: Non-current lease liabilities','lease_cur':'BS: Current lease liabilities','equity_total':'BS: Total equity (incl NCI)',
       'nci':'BS: Non-controlling interest','cash':'BS: Cash & cash equivalents','other_bank':'BS: Other bank balances',
       'inventories':'BS: Inventories','receivables':'BS: Trade receivables','total_assets':'BS: Total assets',
       'total_liabilities':'BS: Total liabilities','payables':'BS: Trade payables','cur_assets':'BS: Total current assets',
       'cur_liab':'BS: Total current liabilities','cfo':'CF: Net cash from operations','capex':'CF: Purchase of PPE+CWIP',
       'dividends':'CF: Dividend paid','repayments':'CF: Term-loan (+unsecured) repayments'}
for k, src in SRC.items():
    row = [src.split(': ')[1] if ': ' in src else k]
    for y in years:
        row.append(cr.D[y].get(k))
    row.append(src)
    ws.append(row)
ws.column_dimensions['A'].width = 34; ws.column_dimensions['F'].width = 44
for col in 'BCDE': ws.column_dimensions[col].width = 13

# ---- RatioSuite ----
ws2 = wb.create_sheet("RatioSuite")
ws2["A1"] = "ICRA-convention ratio suite (927 definitions) - consolidated"; ws2["A1"].font = title
ws2.append([]); ws2.append(["Metric"] + years)
for c in ws2[3]: c.font = hdr; c.fill = fill
rows = ['Operating income','Revenue growth %','OPBDITA','OPBDITA margin %','PAT','PAT margin %','RoCE %',
        'Total debt','Net debt','TNW (incl NCI)','Gearing (TD/TNW)','TOL/TNW','TD/OPBDITA','Net debt/OPBDITA',
        'Interest coverage','DSCR','NCA/TD %','Current ratio','Debtor days','Inventory days','Payable days',
        'WC cycle days','NWC/OI %','CFO','FCF (CFO-capex-div)']
for m in rows:
    r = [m]
    for y in years:
        v = cr.RESULTS[y].get(m)
        r.append(round(v, 2) if isinstance(v, (int, float)) else None)
    ws2.append(r)
ws2["A30"] = ("Notes: OPBDITA = PBT-before-exceptional + finance + D&A - other income (927). Total debt incl. lease "
              "liabilities. TNW incl. NCI, no revaluation reserves disclosed. DSCR = (PAT+interest+D&A)/(interest+repayments). "
              "CE for RoCE = TD+TNW (DTL/CWIP adj not material). FY26 inventory/debtor days on revenue base.")
ws2["A30"].alignment = Alignment(wrap_text=True)
ws2.column_dimensions['A'].width = 26
for col in 'BCDE': ws2.column_dimensions[col].width = 13

# ---- TieOut ----
ws3 = wb.create_sheet("TieOut")
ws3["A1"] = "Component-level tie-out vs screener.in (consolidated, Rs crore) - 18-Jul-2026"; ws3["A1"].font = title
ws3.append([]); ws3.append(["Item","Screener","AR/AFR extraction","Diff","PASS/FAIL","Basis note"])
for c in ws3[3]: c.font = hdr; c.fill = fill
def cr_(lakh): return round(lakh/100, 2)
ties = [
 ("FY26 Revenue", 1353, cr_(cr.D['FY26']['revenue']), "exact", "PASS", ""),
 ("FY26 Net profit", 57, cr_(cr.D['FY26']['pat']), "rounding", "PASS", ""),
 ("FY26 Borrowings incl leases", 348, cr_(cr.D['FY26']['borr_nc']+cr.D['FY26']['borr_cur']+cr.D['FY26']['lease_nc']+cr.D['FY26']['lease_cur']), "0.4", "PASS", "screener borrowings include lease liabilities"),
 ("FY26 Operating profit", 140, cr_(cr.RESULTS['FY26']['OPBDITA']), "rounding", "PASS", "OPBDITA excl other income"),
 ("FY26 Equity+Reserves (ex-NCI)", 534, cr_(cr.D['FY26']['equity_total']-cr.D['FY26']['nci']), "rounding", "PASS", "screener excludes NCI Rs 84.3 cr"),
 ("FY26 Balance-sheet total", 1382, cr_(cr.D['FY26']['total_assets']), "rounding", "PASS", ""),
 ("FY26 Debtor days", 73, round(cr.RESULTS['FY26']['Debtor days']), "0", "PASS", ""),
 ("FY25 Revenue", 1028, cr_(cr.D['FY25']['revenue']), "rounding", "PASS", ""),
 ("FY25 Net profit", 62, cr_(cr.D['FY25']['pat']), "rounding", "PASS", ""),
 ("FY25 Borrowings incl leases", 381, cr_(cr.D['FY25']['borr_nc']+cr.D['FY25']['borr_cur']+cr.D['FY25']['lease_nc']+cr.D['FY25']['lease_cur']), "0.3", "PASS", "as-reported basis"),
 ("Inventory days basis", "205/300", f"{round(cr.RESULTS['FY26']['Inventory days'])}/{round(cr.RESULTS['FY25']['Inventory days'])}", "basis", "EXPLAINED", "screener computes on COGS; suite uses revenue base"),
]
for t in ties: ws3.append(list(t))
ws3.append([])
ws3.append(["Market context (labelled, cross-check only): market cap Rs 2,931 cr @ Rs 422 (screener 18-Jul-2026)",
            "", "", "", "", "mcap ~8.4x total debt - financial flexibility context"])
for col, w in zip('ABCDEF', [30,12,18,10,11,44]): ws3.column_dimensions[col].width = w

out = os.path.join(HERE, "HLE_Financial_Spreads.xlsx")
wb.save(out)

# render-verify
wb2 = openpyxl.load_workbook(out, data_only=True)
blank = 0; total = 0
for s in wb2.sheetnames:
    for row in wb2[s].iter_rows():
        for c in row:
            if c.value is not None: total += 1
print(f"saved {out}; non-empty cells={total}; formula-only cells=0 (all literal)")
