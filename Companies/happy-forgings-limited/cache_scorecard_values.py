# Computes all formula values with the `formulas` package (LibreOffice not available
# on this machine) and injects them as cached <v> into the worksheet XML via a zip
# round-trip, per the project's documented gotcha (openpyxl writes formulas with NO
# cached values -> Excel shows blanks without this step). Preserves formulas/dropdowns.
import formulas
import zipfile
import shutil
import re
from pathlib import Path

PATH = "Rating_Scorecard_Happy Forgings.xlsx"
KEYCASE = f"'[{PATH}]"

xl = formulas.ExcelModel().loads(PATH).finish()
sol = xl.calculate()

# Cells we need read back (Rating sheet outputs) + a broad sweep of Ratios/Scorecard/
# Projections so the workbook doesn't show blanks anywhere a formula lives.
targets = {}
for k, v in sol.items():
    if PATH.upper() not in k.upper():
        continue
    m = re.search(r"'\[.*?\](.*?)'!([A-Z]+\d+)$", k)
    if not m:
        continue
    sheet, cell = m.group(1), m.group(2)
    try:
        val = v.value[0, 0] if hasattr(v.value, "shape") else v.value
    except Exception:
        val = v.value
    targets.setdefault(sheet, {})[cell] = val

print("Sheets with computed values:", list(targets.keys()))
for cell in ("C6", "C7", "C9", "C11", "C12", "C13", "C17", "C18", "C19"):
    print("Rating!" + cell, "=", targets.get("RATING", {}).get(cell))

# ---- inject cached values into the xlsx via zip round-trip (sheet name -> sheetN.xml
# order must match workbook.xml's <sheets> order, not alphabetical) ----
import xml.etree.ElementTree as ET

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
ET.register_namespace("", NS["m"])

tmp = Path(PATH + ".tmp")
shutil.copy(PATH, tmp)

with zipfile.ZipFile(tmp, "r") as zin:
    wb_xml = zin.read("xl/workbook.xml").decode("utf-8")
    sheet_tags = re.findall(r"<sheet\b[^>]*/>", wb_xml)
    names_in_order = []
    for tag in sheet_tags:
        nm = re.search(r'name="([^"]+)"', tag)
        rid = re.search(r'r:id="rId(\d+)"', tag)
        if nm and rid:
            names_in_order.append((nm.group(1), rid.group(1)))
    rels = zin.read("xl/_rels/workbook.xml.rels").decode("utf-8")
    rid_to_target = {}
    for rel_tag in re.findall(r"<Relationship\b[^>]*/>", rels):
        rid_m = re.search(r'Id="rId(\d+)"', rel_tag)
        tgt_m = re.search(r'Target="[^"]*?(sheet\d+\.xml)"', rel_tag)
        if rid_m and tgt_m:
            rid_to_target[rid_m.group(1)] = tgt_m.group(1)
    sheet_file_by_name = {name: rid_to_target[rid] for name, rid in names_in_order if rid in rid_to_target}
    assert "Rating" in sheet_file_by_name, f"sheet mapping failed: {sheet_file_by_name}"

    out_files = {}
    for name in zin.namelist():
        out_files[name] = zin.read(name)

for sheet_name_disp, sheet_file in sheet_file_by_name.items():
    key = sheet_name_disp.upper()
    if key not in targets:
        continue
    xml_bytes = out_files[f"xl/worksheets/{sheet_file}"]
    root = ET.fromstring(xml_bytes)
    sheetdata = root.find("m:sheetData", NS)
    cell_map = {c: v for c, v in targets[key].items()}
    for row_el in sheetdata.findall("m:row", NS):
        for c_el in row_el.findall("m:c", NS):
            ref = c_el.get("r")
            if ref not in cell_map:
                continue
            val = cell_map[ref]
            f_el = c_el.find("m:f", NS)
            v_el = c_el.find("m:v", NS)
            if f_el is None:
                continue  # not a formula cell, leave as-is
            if isinstance(val, str):
                # inline string result for a formula (e.g. grade text)
                c_el.set("t", "str")
                if v_el is None:
                    v_el = ET.SubElement(c_el, "{%s}v" % NS["m"])
                v_el.text = val
            else:
                try:
                    if "t" in c_el.attrib and c_el.attrib.get("t") not in ("n",):
                        del c_el.attrib["t"]
                    fval = float(val)
                    if v_el is None:
                        v_el = ET.SubElement(c_el, "{%s}v" % NS["m"])
                    v_el.text = repr(fval)
                except (TypeError, ValueError):
                    continue
    out_files[f"xl/worksheets/{sheet_file}"] = ET.tostring(root, xml_declaration=True, encoding="UTF-8")

# force recalculation on open
wb_xml_bytes = out_files["xl/workbook.xml"]
wb_xml_str = wb_xml_bytes.decode("utf-8")
if "<calcPr" in wb_xml_str:
    wb_xml_str = re.sub(r"<calcPr[^/]*/>", '<calcPr calcId="999999" fullCalcOnLoad="1"/>', wb_xml_str)
else:
    wb_xml_str = wb_xml_str.replace("</workbook>", '<calcPr calcId="999999" fullCalcOnLoad="1"/></workbook>')
out_files["xl/workbook.xml"] = wb_xml_str.encode("utf-8")

with zipfile.ZipFile(PATH, "w", zipfile.ZIP_DEFLATED) as zout:
    for name, data in out_files.items():
        zout.writestr(name, data)

tmp.unlink()
print("\nCached values injected ->", PATH)
