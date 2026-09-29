#!/usr/bin/env python3
"""Financial_Spreads generator — the Excel that ships WITH every workpaper (CLAUDE.md Step 5).

Produces <Company>_Financial_Spreads.xlsx with four tabs:
  1. Inputs      - every extracted line item, all years, with the AR/filing source per row
  2. RatioSuite  - the ratio suite as LIVE EXCEL FORMULAS referencing Inputs, so the reader can
                   click any cell and see the arithmetic. Each row also carries the formula in
                   words and the applicable convention note.
  3. TieOut      - corroboration checks against company-disclosed figures, PASS/FAIL by formula
  4. RatingScore - factor scores, weights, weighted composite, indicative anchor grade, and the
                   analyst's rating view with the divergence explained

WHY FORMULAS, NOT VALUES: a workpaper that hands over numbers asks to be trusted; one that hands
over the arithmetic can be checked. openpyxl writes formulas with NO cached result, so Excel
shows blanks until it recalculates - `fullCalcOnLoad` is set on the workbook to force that.

USAGE (from a company folder, driven by that company's compute_ratios.py):
    from make_spreads import build_spreads
    build_spreads(company="...", years=[...], inputs=[...], ratios=[...],
                  tieouts=[...], score=..., out="<Company>_Financial_Spreads.xlsx")
"""
import re
import zipfile
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

NAVY, TEAL, AMBER = "1B2A4A", "0E7C86", "B45309"
HDR = PatternFill("solid", fgColor=NAVY)
SUB = PatternFill("solid", fgColor="EAF0F8")
INFILL = PatternFill("solid", fgColor="FFF9E6")     # yellow = an input, not a computation
OKFILL = PatternFill("solid", fgColor="E2F3E6")
BADFILL = PatternFill("solid", fgColor="FDECE0")
WHITE_BOLD = Font(color="FFFFFF", bold=True)
NOTE = Font(italic=True, size=9, color="666666")
thin = Side(style="thin", color="D6DEE8")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)


def _title(ws, text, note, ncols):
    ws["B2"] = text
    ws["B2"].font = Font(bold=True, size=13, color=NAVY)
    ws["B3"] = note
    ws["B3"].font = NOTE
    ws.merge_cells(start_row=3, start_column=2, end_row=3, end_column=max(3, ncols))
    ws["B3"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[3].height = 42


def _hdr_row(ws, row, labels, widths=None):
    for i, lab in enumerate(labels):
        c = ws.cell(row=row, column=2 + i, value=lab)
        c.font, c.fill, c.border = WHITE_BOLD, HDR, BOX
        c.alignment = Alignment(horizontal="center", wrap_text=True)
    if widths:
        for i, w in enumerate(widths):
            ws.column_dimensions[get_column_letter(2 + i)].width = w


def build_spreads(company, years, inputs, ratios, tieouts, score, out,
                  basis="Consolidated", unit="Rs crore"):
    """inputs : [(label, [v per year], source)]
       ratios : [(label, excel_formula_template, plain_english, number_format)]
                 template may use {c} for the current column letter and {y} for the year index
       tieouts: [(check, computed_formula, disclosed_value, note)]
       score  : dict(factors=[(factor, score_1_6, weight, justification)], anchor=str,
                     view=str, divergence=str)
    """
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    ycols = [get_column_letter(3 + i) for i in range(len(years))]

    # ---------------------------------------------------------------- 1. Inputs
    ws = wb.create_sheet("Inputs")
    _title(ws, f"{company} - extracted line items ({basis}, {unit})",
           "Yellow cells are EXTRACTED INPUTS traced to the source in the final column - nothing "
           "here is computed. Every downstream ratio references this sheet, so correcting a value "
           "here reflows the entire workbook.", len(years) + 2)
    _hdr_row(ws, 5, ["Line item"] + years + ["Source"], [46] + [14] * len(years) + [64])
    r = 6
    row_of = {}
    for label, vals, src in inputs:
        ws.cell(row=r, column=2, value=label).border = BOX
        for i, v in enumerate(vals):
            c = ws.cell(row=r, column=3 + i, value=v)
            c.number_format = "#,##0.0"
            c.fill, c.border = INFILL, BOX
        s = ws.cell(row=r, column=3 + len(years), value=src)
        s.font, s.border = NOTE, BOX
        s.alignment = Alignment(wrap_text=True, vertical="top")
        row_of[label] = r
        r += 1
    ws.freeze_panes = "C6"

    # ---------------------------------------------------------------- 2. RatioSuite
    ws = wb.create_sheet("RatioSuite")
    _title(ws, f"{company} - ratio suite ({basis}, {unit}; agency conventions applied)",
           "Every value is a LIVE FORMULA referencing the Inputs sheet - click any cell to see the "
           "arithmetic. 'Calculation' states the same formula in words; 'Convention' records the "
           "definitional choice (lease treatment, normalisation, netting) so the basis is auditable.",
           len(years) + 3)
    _hdr_row(ws, 5, ["Ratio"] + years + ["Calculation", "Convention / note"],
             [40] + [14] * len(years) + [46, 52])
    r = 6
    for label, tmpl, plain, fmt in ratios:
        ws.cell(row=r, column=2, value=label).border = BOX
        for i, col in enumerate(ycols):
            f = tmpl.format(c=col, y=i)
            c = ws.cell(row=r, column=3 + i, value=f if f.startswith("=") else None)
            c.number_format = fmt
            c.border = BOX
        p = ws.cell(row=r, column=3 + len(years), value=plain)
        p.font, p.border = NOTE, BOX
        p.alignment = Alignment(wrap_text=True, vertical="top")
        r += 1
    ws.freeze_panes = "C6"

    # ---------------------------------------------------------------- 3. TieOut
    ws = wb.create_sheet("TieOut")
    _title(ws, f"{company} - tie-out to company-disclosed figures",
           "Binding gate (CLAUDE.md Step 6): headline computed figures must reconcile to the "
           "company's OWN disclosed numbers before the workpaper is issued. PASS/FAIL is itself a "
           "formula - it re-evaluates if any input changes.", 5)
    _hdr_row(ws, 5, ["Check", "Computed", "Company-disclosed", "Result", "Note"],
             [44, 16, 18, 12, 60])
    r = 6
    for chk, comp_f, disc, note in tieouts:
        ws.cell(row=r, column=2, value=chk).border = BOX
        c = ws.cell(row=r, column=3, value=comp_f); c.number_format = "#,##0.00"; c.border = BOX
        d = ws.cell(row=r, column=4, value=disc); d.number_format = "#,##0.00"; d.border = BOX
        res = ws.cell(row=r, column=5,
                      value=f'=IF(ABS(C{r}-D{r})<=MAX(1,ABS(D{r})*0.005),"PASS","CHECK")')
        res.border, res.alignment = BOX, Alignment(horizontal="center")
        res.font = Font(bold=True)
        n = ws.cell(row=r, column=6, value=note); n.font, n.border = NOTE, BOX
        n.alignment = Alignment(wrap_text=True, vertical="top")
        r += 1
    ws.cell(row=r + 1, column=2, value="Tolerance: 0.5% of the disclosed figure, floor Rs 1 "
                                       "- tighter than rounding, loose enough for basis differences.").font = NOTE

    # ---------------------------------------------------------------- 4. RatingScore
    ws = wb.create_sheet("RatingScore")
    _title(ws, f"{company} - rating scorecard and view",
           "Factor scores 1 (strongest) to 6 (weakest), weighted to a composite. The anchor is a "
           "SCREENING cross-check with a +/-2 notch band, NOT the rating - the analyst view and any "
           "divergence are stated below and the divergence must be explained, never buried.", 5)
    _hdr_row(ws, 5, ["Rating factor", "Score (1-6)", "Weight", "Weighted", "Justification"],
             [34, 12, 10, 12, 70])
    r = 6
    first = r
    for fac, sc, wt, just in score["factors"]:
        ws.cell(row=r, column=2, value=fac).border = BOX
        c = ws.cell(row=r, column=3, value=sc); c.fill, c.border = INFILL, BOX
        c.alignment = Alignment(horizontal="center")
        w = ws.cell(row=r, column=4, value=wt); w.number_format = "0%"; w.fill, w.border = INFILL, BOX
        ws.cell(row=r, column=5, value=f"=C{r}*D{r}").number_format = "0.00"
        ws.cell(row=r, column=5).border = BOX
        j = ws.cell(row=r, column=6, value=just); j.font, j.border = NOTE, BOX
        j.alignment = Alignment(wrap_text=True, vertical="top")
        r += 1
    last = r - 1
    ws.cell(row=r, column=2, value="Weight check (must be 100%)").font = Font(bold=True)
    ws.cell(row=r, column=4, value=f"=SUM(D{first}:D{last})").number_format = "0%"
    ws.cell(row=r, column=4).font = Font(bold=True)
    ws.cell(row=r, column=5, value=f"=SUM(E{first}:E{last})").number_format = "0.00"
    ws.cell(row=r, column=5).font = Font(bold=True)
    ws.cell(row=r, column=6,
            value='=IF(ABS(D{0}-1)<0.001,"weights sum to 100%","ERROR: weights must sum to 100%")'
            .format(r)).font = Font(bold=True)
    r += 2
    for lab, val in (("Weighted composite score", f"=E{last+1}"),
                     ("Indicative anchor grade (screening only, +/-2 band)", score["anchor"]),
                     ("ANALYST RATING VIEW", score["view"]),
                     ("Divergence from anchor - explanation", score["divergence"])):
        ws.cell(row=r, column=2, value=lab).font = Font(bold=True)
        c = ws.cell(row=r, column=3, value=val)
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=6)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c.font = Font(bold=True, color=TEAL) if "VIEW" in lab else Font()
        ws.row_dimensions[r].height = 30 if len(str(val)) > 90 else 16
        r += 1

    wb.save(out)
    _force_recalc(out)
    _cache_values(out)
    return out


def _cache_values(path):
    """Inject a cached <v> result next to each <f> formula, KEEPING the formula intact.

    fullCalcOnLoad alone makes Excel calculate on open, but the file still reads as BLANK to
    anything that is not Excel (openpyxl, pandas, previewers, Drive/Sharepoint thumbnails).
    The workbook must show its numbers everywhere AND keep every formula visible and live -
    the point of the deliverable is that the arithmetic can be inspected and re-driven.
    So this writes <f>..</f><v>result</v>, which is exactly what Excel itself stores.

    Evaluating with `formulas` is also an independent recomputation of the whole ratio suite -
    a genuine second calculation, not a copy of the Python one (CLAUDE.md Step 17).
    """
    try:
        import formulas
    except ImportError:
        print("  ! formulas not installed - values populate on first open in Excel only")
        return
    p = Path(path)
    try:
        xl = formulas.ExcelModel().loads(str(p)).finish()
        sol = xl.calculate()
    except Exception as e:                                     # noqa: BLE001
        print(f"  ! formula evaluation failed ({type(e).__name__}) - Excel will calc on open")
        return

    computed = {}
    for k, v in sol.items():
        m = re.match(r"'\[.+?\]([^']+?)'!([A-Z]+\d+)$", k)
        if not m:
            continue
        try:
            val = v.value[0, 0]
        except Exception:                                      # noqa: BLE001
            continue
        if isinstance(val, (int, float)) and not isinstance(val, bool):
            computed[(m.group(1).strip().upper(), m.group(2))] = float(val)
        elif isinstance(val, str) and val and not val.startswith("#"):
            # TEXT results too - a formula returning a grade ("BBB") or a label is still a
            # computed value, and skipping it left such cells BLANK everywhere except Excel.
            # Error strings (#N/A, #VALUE!) are deliberately not cached.
            computed[(m.group(1).strip().upper(), m.group(2))] = val

    with zipfile.ZipFile(p, "r") as z:
        files = {n: z.read(n) for n in z.namelist()}

    # map sheet name -> sheet xml part, via workbook.xml + its rels
    wbx = files["xl/workbook.xml"].decode("utf-8")
    rels = files["xl/_rels/workbook.xml.rels"].decode("utf-8")
    # attribute order is NOT fixed - openpyxl writes Target before Id, so parse each tag
    rid_target = {}
    for tag in re.findall(r"<Relationship\b[^>]*/>", rels):
        rid = re.search(r'Id="([^"]+)"', tag)
        tgt = re.search(r'Target="([^"]+)"', tag)
        if rid and tgt:
            rid_target[rid.group(1)] = tgt.group(1)
    name_part = {}
    for sheet in re.findall(r"<sheet\b[^>]*/>", wbx):
        nm = re.search(r'name="([^"]+)"', sheet)
        rid = re.search(r'r:id="([^"]+)"', sheet)
        if nm and rid and rid.group(1) in rid_target:
            tgt = rid_target[rid.group(1)].lstrip("/")
            name_part[nm.group(1)] = tgt if tgt.startswith("xl/") else f"xl/{tgt}"

    total = 0
    for sheet_name, part in name_part.items():
        if part not in files:
            continue
        xml = files[part].decode("utf-8")

        def add_v(m, _s=sheet_name):
            nonlocal total
            cell, attrs, inner = m.group(0), m.group(1), m.group(2)
            ref = re.search(r'r="([A-Z]+\d+)"', attrs)
            if not ref or "<f" not in inner:
                return cell
            val = computed.get((_s.strip().upper(), ref.group(1)))
            if val is None:
                return cell
            # openpyxl emits an EMPTY <v></v> placeholder - fill it, don't treat it as cached
            inner = re.sub(r"<v\s*/>|<v>\s*</v>", "", inner)
            if "<v>" in inner:
                return cell
            total += 1
            # strip any cached type attr (t="e"/"str") before setting the right one
            attrs = re.sub(r'\s+t="[^"]*"', "", attrs)
            if isinstance(val, str):
                esc = (val.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
                return f'<c{attrs} t="str">{inner}<v>{esc}</v></c>'
            return f"<c{attrs}>{inner}<v>{val!r}</v></c>"

        # `<c ` with the space matters - `<c([^>]*)>` also swallows <cols>...</cols>
        xml = re.sub(r"<c(\s[^>]*)>(.*?)</c>", add_v, xml, flags=re.S)
        files[part] = xml.encode("utf-8")

    with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED) as z:
        for n, d in files.items():
            z.writestr(n, d)
    print(f"  cached {total} computed values (formulas preserved)")


def _force_recalc(path):
    """openpyxl writes formulas with no cached value; make Excel compute them on open."""
    p = Path(path)
    with zipfile.ZipFile(p, "r") as z:
        files = {n: z.read(n) for n in z.namelist()}
    wbx = files["xl/workbook.xml"].decode("utf-8")
    if "<calcPr" in wbx:
        wbx = re.sub(r"<calcPr[^/]*/>", '<calcPr calcId="999999" fullCalcOnLoad="1"/>', wbx)
    else:
        wbx = wbx.replace("</workbook>", '<calcPr calcId="999999" fullCalcOnLoad="1"/></workbook>')
    files["xl/workbook.xml"] = wbx.encode("utf-8")
    with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED) as z:
        for n, d in files.items():
            z.writestr(n, d)
