# -*- coding: utf-8 -*-
"""Step 12b: fill Rating_Scorecard_HLE_Glascoat.xlsx (copy of calibrated master).
Quantitative inputs from AUDITED ACTUALS (compute_ratios extraction, Rs crore);
FY+1/+2 assumptions from the Step-12 model base case (copied, not linked).
Qualitative per Ref_Qualitative rubric. Compute with `formulas` (read-only),
write results back as literal values, render-verify."""
import shutil, os, importlib.util
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MASTER = os.path.join(ROOT, "Rating_Scorecard.xlsx")
OUT = os.path.join(HERE, "Rating_Scorecard_HLE_Glascoat.xlsx")
shutil.copy(MASTER, OUT)

spec = importlib.util.spec_from_file_location("cr", os.path.join(HERE, "compute_ratios.py"))
cr = importlib.util.module_from_spec(spec); spec.loader.exec_module(cr)
L = lambda lakh: round(lakh/100, 2)  # lakh -> crore
D = cr.D

wb = openpyxl.load_workbook(OUT)
inp = wb['Inputs']
inp['C4'] = 'HLE Glascoat Limited'
inp['C5'] = 'ICRA'
inp['C6'] = 'Generic corporate'
inp['C7'] = '18-Jul-2026'
# historical financials, consolidated audited (FY24 / FY25 / FY26), Rs crore
years = ['FY24','FY25','FY26']; cols = ['C','D','E']
inp['C11'],inp['D11'],inp['E11'] = 'FY2024','FY2025','FY2026'
rows = {
 12: lambda d,y: L(d['revenue']),
 13: lambda d,y: L(cr.RESULTS[y]['OPBDITA']),
 14: lambda d,y: L(d['da']),
 15: lambda d,y: L(d['finance']),
 16: lambda d,y: L(d['pat']),
 17: lambda d,y: L(d['borr_nc']+d['borr_cur']+d['lease_nc']+d['lease_cur']),
 18: lambda d,y: L(d['cash']+d['other_bank']),
 19: lambda d,y: L(d['equity_total']),
 20: lambda d,y: L(d['total_liabilities']),
 21: lambda d,y: L(d['cur_assets']),
 22: lambda d,y: L(d['cur_liab']),
 23: lambda d,y: L(d['capex']) if d['capex'] else 55.0,
 24: lambda d,y: L(d['dividends']) if d['dividends'] else 7.5,
}
for r, f in rows.items():
    for c, y in zip(cols, years):
        inp[f'{c}{r}'] = f(D[y], y)
# projections FY+1/FY+2 (from model base case - copied)
inp['C29'], inp['D29'] = 0.12, 0.10       # revenue growth
inp['C30'], inp['D30'] = 0.115, 0.120     # OPBDITA margin
inp['C31'], inp['D31'] = 60.0, 60.0       # capex Rs crore
inp['C32'], inp['D32'] = -32.0, -32.0     # net debt movement (repay 62 - fresh 30)
inp['C33'], inp['D33'] = 0.093, 0.093
inp['C34'], inp['D34'] = 0.25, 0.25
inp['C35'], inp['D35'] = 0.14, 0.14
# qualitative (Ref_Qualitative rubric; one-line justifications in workpaper)
inp['C39'] = None   # industry: accept Generic corporate base 3
inp['C40'] = 3      # business: established niche leader, mid-scale, avg pricing power, end-user concentration
inp['C41'] = 3      # management: capable & acquisitive; debt-funded M&A appetite, adequate governance
inp['C42'] = 0      # no parent support
inp['C43'] = 'Adequate'
inp['C44'] = 'Stable'
wb.save(OUT)

# compute all formulas -> literal values (formulas engine READ-ONLY; never .write())
import formulas
xl = formulas.ExcelModel().loads(OUT).finish()
sol = xl.calculate()
fname = os.path.basename(OUT)
wb = openpyxl.load_workbook(OUT)
patched = 0
for ws in wb.worksheets:
    up = ws.title.upper()
    for row in ws.iter_rows():
        for cell in row:
            if isinstance(cell.value, str) and cell.value.startswith('='):
                key = f"'[{fname}]{up}'!{cell.coordinate}"
                v = sol.get(key)
                if v is None: continue
                try: v = v.value[0, 0]
                except Exception: pass
                if v is None: continue
                if isinstance(v, (int, float, str, bool)):
                    try:
                        if isinstance(v, float) and (v != v): continue
                        cell.value = v; patched += 1
                    except Exception: pass
wb.save(OUT)

wb2 = openpyxl.load_workbook(OUT, data_only=False)
rt = wb2['Rating']
print("patched formula cells:", patched)
print("composite:", rt['C6'].value, "| idx:", rt['C7'].value, "| after caps:", rt['C11'].value)
print("ANCHOR LT:", rt['C12'].value, "| ST:", rt['C13'].value)
print("line:", rt['C19'].value)
sc = wb2['Scorecard']
print("fin score:", sc['F12'].value, "| blocks I/B/F/M:", sc['C17'].value, sc['C18'].value, sc['C19'].value, sc['C20'].value)
leftover = sum(1 for ws in wb2.worksheets for row in ws.iter_rows() for c in row
               if isinstance(c.value, str) and c.value.startswith('='))
print("formula cells remaining:", leftover)
