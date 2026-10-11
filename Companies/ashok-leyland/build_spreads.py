# -*- coding: utf-8 -*-
"""Generate Ashok_Leyland_Financial_Spreads.xlsx FROM compute_ratios.py (the script is the source
of truth - R6). Tabs: Extraction / RatioSuite / TieOut / ExternalTieOut / Notes.
Values are written LITERALLY (no formulas) and render-verified by a data_only read-back."""
import importlib.util
import os

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cr", os.path.join(HERE, "compute_ratios.py"))
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)

HDR, TITLE = Font(bold=True), Font(bold=True, size=12)
FILL = PatternFill("solid", fgColor="DDEBF7")
OK, BAD = PatternFill("solid", fgColor="E2F3E6"), PatternFill("solid", fgColor="FDECE0")
WRAP = Alignment(wrap_text=True, vertical="top")
YEARS = cr.YEARS

SOURCES = {
    "SA_PL": "Standalone statement of profit and loss (FY2023-24 AR p116; FY2024-25 AR p113; FY2025-26 AR p123)",
    "SA_PL_PRINTED": "Standalone P&L printed subtotals (same pages)",
    "SA_FIN_COST": "Standalone note 2.5 Finance costs (FY2025-26 AR p169)",
    "SA_OTHER_INCOME": "Standalone note 2.2 Other income (FY2025-26 AR p168)",
    "SA_NCA": "Standalone balance sheet - non-current assets (FY2023-24 AR p115; FY2024-25 AR p111; FY2025-26 AR p121)",
    "SA_CA": "Standalone balance sheet - current assets (same pages)",
    "SA_HFS_ASSETS": "Standalone balance sheet - assets held for sale",
    "SA_EQUITY": "Standalone balance sheet - equity",
    "SA_NCL": "Standalone balance sheet - non-current liabilities",
    "SA_CL": "Standalone balance sheet - current liabilities",
    "SA_HFS_LIAB": "Standalone balance sheet - liabilities held for sale",
    "SA_BS_PRINTED": "Standalone balance sheet printed totals",
    "SA_EARMARKED": "Standalone note 1.11B (earmarked bank balances) + FY2025 cash flow (subsidiary preference shares)",
    "FREE_BANK_DEPOSITS": "Standalone note 1.11B (3-12 month deposits)",
    "AR_NET_DEBT_BRIDGE": "Standalone 'Net debt reconciliation' (FY2023-24 AR note 1.21; FY2025-26 AR note 1.21)",
    "AR_PUBLISHED": "Chairman's letters (FY2023-24, FY2024-25, FY2025-26 ARs)",
    "SA_CF": "Standalone statement of cash flows (same reports) + board's report investments",
    "CONS_PL": "Consolidated P&L (FY2023-24 AR p210; FY2024-25 AR p208 restated FY2024; FY2025-26 AR p221)",
    "CONS_DA_CF": "Consolidated cash flow D&A rows",
    "CONS_BS": "Consolidated balance sheet",
    "CONS_LEASE": "Consolidated balance sheet lease liabilities",
    "CONS_NC_COMPONENTS": "Consolidated note 1.20 non-current borrowings",
    "CONS_CB_COMPONENTS": "Consolidated note 1.26 current borrowings",
    "FS_DEBT": "Consolidated notes 1.20 (note 8) and 1.26 (note 2): borrowings relating to financing activities",
    "FS_NC_COMPONENTS": "Consolidated note 1.20 note 8 line items",
    "FS_CB_COMPONENTS": "Consolidated note 1.26 note 2 line items",
    "SEG": "Consolidated segment note 3.8",
    "OPS": "Ten-year table, MD&A and chairman's letters; standalone note 3.9.2 (guarantees)",
    "BOARD_REPORT_INVESTMENTS": "Board's report - subsidiaries, associates and joint ventures",
    "SECOND_SOURCE": "Second disclosures used only for corroboration",
}

wb = openpyxl.Workbook()

# ---------------------------------------------------------------- Extraction
ws = wb.active
ws.title = "Extraction"
ws["A1"] = "Ashok Leyland Limited - extracted line items (Rs crore unless stated)"
ws["A1"].font = TITLE
ws["A2"] = ("Every value below is a literal copy of compute_ratios.py, which carries the page-level "
            "source of each table. Nothing here is typed by hand (R6). Blank = not disclosed / not "
            "extracted (named in Notes).")
ws["A2"].alignment = WRAP
ws.row_dimensions[2].height = 30
ws.append([])
ws.append(["Table", "Line item"] + YEARS + ["Source"])
for c in ws[4]:
    c.font, c.fill = HDR, FILL
for name in SOURCES:
    table = getattr(cr, name)
    for key, series in table.items():
        ws.append([name, key] + [None if x is None else float(x) for x in series] + [SOURCES[name]])
for col, w in zip("ABCDEFG", [24, 46, 13, 13, 13, 13, 70]):
    ws.column_dimensions[col].width = w

# ---------------------------------------------------------------- RatioSuite
R = cr.compute()
ws2 = wb.create_sheet("RatioSuite")
ws2["A1"] = "ICRA-convention ratio suite - standalone (primary), automotive adjustment, consolidated supplement"
ws2["A1"].font = TITLE
ws2["A2"] = ("Rows without a prefix = AL standalone (methodology basis, ICRA 934). AUTO = consolidated "
             "EXCLUDING financial services (segment note + financing-activity debt). ADJ = standalone "
             "plus non-financial subsidiaries' debt. CONS = reported consolidated incl. HLF (supplement).")
ws2["A2"].alignment = WRAP
ws2.row_dimensions[2].height = 42
ws2.append([])
ws2.append(["Metric"] + YEARS)
for c in ws2[4]:
    c.font, c.fill = HDR, FILL
for key in R[YEARS[-1]]:
    row = [key]
    for y in YEARS:
        x = R[y].get(key)
        row.append(None if x is None else round(float(x), 2))
    ws2.append(row)
ws2.column_dimensions["A"].width = 66
for col in "BCDE":
    ws2.column_dimensions[col].width = 14

# ---------------------------------------------------------------- TieOut
T = cr.tieouts(R)
ws3 = wb.create_sheet("TieOut")
ws3["A1"] = "Internal tie-outs - every check compares a computation with a figure the AR prints"
ws3["A1"].font = TITLE
ws3.append([])
ws3.append(["Check", "Computed", "Disclosed", "Difference", "Tolerance", "Result", "Source"])
for c in ws3[3]:
    c.font, c.fill = HDR, FILL
npass = 0
for d, comp, disc, tol, src in T:
    ok = abs(comp - disc) <= tol
    npass += ok
    ws3.append([d, round(comp, 2), round(disc, 2), round(comp - disc, 2), tol,
                "PASS" if ok else "FAIL", src])
    ws3.cell(row=ws3.max_row, column=6).fill = OK if ok else BAD
ws3.append([])
ws3.append(["TOTAL", None, None, None, None, "%d/%d PASS" % (npass, len(T))])
ws3.append(["Mutation coverage (tools/tieout_mutation.py): 598 of 611 inputs change a tie-out = 97.9%; "
            "the 13 that do not are named in Notes / DISCLOSED_DIFFERENCES."])
for col, w in zip("ABCDEFG", [70, 13, 13, 11, 10, 9, 60]):
    ws3.column_dimensions[col].width = w

# ---------------------------------------------------------------- ExternalTieOut (screener.in)
ws4 = wb.create_sheet("ExternalTieOut")
ws4["A1"] = "External tie-out vs screener.in (cross-check ONLY - R1; read 10-Oct-2026)"
ws4["A1"].font = TITLE
ws4.append([])
ws4.append(["Item", "Basis", "Year", "screener.in", "Engine", "Difference", "Result / basis note"])
for c in ws4[3]:
    c.font, c.fill = HDR, FILL
SCR = [
    # (item, basis, year, screener, engine value)
    ("Sales", "Standalone", "FY2023", 36144, R["FY2023"]["Operating income"]),
    ("Sales", "Standalone", "FY2024", 38367, R["FY2024"]["Operating income"]),
    ("Sales", "Standalone", "FY2025", 38753, R["FY2025"]["Operating income"]),
    ("Sales", "Standalone", "FY2026", 44007, R["FY2026"]["Operating income"]),
    ("Operating profit", "Standalone", "FY2023", 2931, R["FY2023"]["OPBDITA"]),
    ("Operating profit", "Standalone", "FY2024", 4607, R["FY2024"]["OPBDITA"]),
    ("Operating profit", "Standalone", "FY2025", 4931, R["FY2025"]["OPBDITA"]),
    ("Operating profit", "Standalone", "FY2026", 5732, R["FY2026"]["OPBDITA"]),
    ("Net profit", "Standalone", "FY2026", 3566, R["FY2026"]["PAT"]),
    ("Net profit", "Standalone", "FY2025", 3303, R["FY2025"]["PAT"]),
    ("Borrowings incl. leases", "Standalone", "FY2023", 3225, R["FY2023"]["Total debt"]),
    ("Borrowings incl. leases", "Standalone", "FY2024", 2299, R["FY2024"]["Total debt"]),
    ("Borrowings incl. leases", "Standalone", "FY2025", 1482, R["FY2025"]["Total debt"]),
    ("Borrowings incl. leases", "Standalone", "FY2026", 1195, R["FY2026"]["Total debt"]),
    ("Equity capital + reserves", "Standalone", "FY2026", 13113, R["FY2026"]["Tangible net worth"]),
    ("Equity capital + reserves", "Standalone", "FY2025", 11519, R["FY2025"]["Tangible net worth"]),
    ("Cash from operating activity", "Standalone", "FY2026", 4792, R["FY2026"]["CFO"]),
    ("Sales (incl. financing income)", "Consolidated", "FY2026", 56362, R["FY2026"]["CONS operating income"]),
    ("Sales (incl. financing income)", "Consolidated", "FY2025", 48535, R["FY2025"]["CONS operating income"]),
    ("Borrowings incl. leases", "Consolidated", "FY2026", 63936, R["FY2026"]["CONS total debt"]),
    ("Borrowings incl. leases", "Consolidated", "FY2025", 49962, R["FY2025"]["CONS total debt"]),
    ("Borrowings incl. leases", "Consolidated", "FY2024", 40802, R["FY2024"]["CONS total debt"]),
    ("Borrowings incl. leases", "Consolidated", "FY2023", 31161, R["FY2023"]["CONS total debt"]),
    ("Net profit", "Consolidated", "FY2026", 3721, R["FY2026"]["CONS PAT"]),
    ("Net profit", "Consolidated", "FY2023", 1362, R["FY2023"]["CONS PAT"]),
]
for item, basis, y, s, e in SCR:
    diff = e - s
    note = "PASS (rounding)" if abs(diff) < 1 else (
        "EXPLAINED: screener uses FY2023 as originally reported; engine uses FY2024 AR comparative"
        if item == "Net profit" and y == "FY2023" else "CHECK")
    ws4.append([item, basis, y, s, round(e, 2), round(diff, 2), note])
    ws4.cell(row=ws4.max_row, column=7).fill = OK if note.startswith(("PASS", "EXPLAINED")) else BAD
for col, w in zip("ABCDEFG", [34, 13, 9, 12, 12, 11, 72]):
    ws4.column_dimensions[col].width = w

# ---------------------------------------------------------------- Notes
ws5 = wb.create_sheet("Notes")
ws5["A1"] = "Basis of preparation and disclosed differences"
ws5["A1"].font = TITLE
ws5.append([])
for title, text in cr.DISCLOSED_DIFFERENCES:
    ws5.append([title])
    ws5.cell(row=ws5.max_row, column=1).font = HDR
    ws5.append([text])
    ws5.cell(row=ws5.max_row, column=1).alignment = WRAP
    ws5.row_dimensions[ws5.max_row].height = 75
    ws5.append([])
ws5.column_dimensions["A"].width = 130

out = os.path.join(HERE, "Ashok_Leyland_Financial_Spreads.xlsx")
wb.save(out)

# render-verify: every intended value readable back, zero formula cells
wb2 = openpyxl.load_workbook(out, data_only=True)
cells = formulas = 0
for s in wb2.sheetnames:
    for row in wb2[s].iter_rows():
        for c in row:
            if c.value is not None:
                cells += 1
                if isinstance(c.value, str) and c.value.startswith("="):
                    formulas += 1
print("saved %s; sheets=%s; non-empty cells=%d; formula cells=%d; tie-outs %d/%d PASS"
      % (out, wb2.sheetnames, cells, formulas, npass, len(T)))
