"""Write COMPUTED VALUES back into a formula workbook so every viewer can read it.

THE PROBLEM THIS FIXES
----------------------
openpyxl cannot evaluate formulas, and when it saves a workbook it writes every formula cell
as `<f>...</f><v></v>` - the formula is preserved, the cached result is EMPTY. Microsoft Excel
hides this, because it recalculates on load. Nothing else does. The webapp's own preview,
LibreOffice, Google Sheets, pandas, and openpyxl's own `data_only=True` all read the cached
value, so a filled scorecard appears to contain nothing but its inputs: the Ratios, Scorecard
and Rating sheets render blank, INCLUDING the final grade.

That is why a scorecard filled correctly by fill_scorecard.py still looks unfilled.

THE FIX
-------
Evaluate the workbook with the `formulas` package - the same evaluator rate_engine.py already
uses for its offline `local` engine, so the numbers written here are by construction the same
ones the anchor is read from - then inject each result into that cell's `<v>` element in the
sheet XML. The `<f>` element is left untouched, so the workbook stays live: open it in Excel,
change an input, and everything still recalculates.

    python recalc_workbook.py <file.xlsx> [more.xlsx ...]
    python recalc_workbook.py --all-scorecards

Verification is built in: after writing, the file is re-read with openpyxl `data_only=True`
and the count of formula cells that now carry a value is reported. A run that writes nothing
says so rather than reporting success.
"""

import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # this script now lives in tools/,
# one level below the project root - moved here 01-Sep-2026 to declutter the root.


# ------------------------------------------------------------------ evaluate with `formulas`
def evaluate(path: Path) -> dict:
    """{(SHEETNAME, 'C12'): value} for every cell the workbook computes."""
    import warnings
    warnings.filterwarnings("ignore")
    import formulas

    xl = formulas.ExcelModel().loads(str(path)).finish()
    sol = xl.calculate()
    key = re.compile(r"^'\[[^\]]+\]([^']+)'!([A-Z]+\d+)$")
    out = {}
    for k, v in sol.items():
        m = key.match(k)
        if not m:
            continue
        try:
            val = v.value[0, 0]
        except Exception:                                                 # noqa: BLE001
            continue
        out[(m.group(1).upper(), m.group(2))] = val
    return out


def as_cell(val):
    """Return (text, type-attr) for the XML `<v>` payload, or None to leave the cell alone."""
    import numpy as np

    # The evaluator returns a schedula Token for a genuinely empty cell. Detect it by TYPE.
    # Testing str(val) against a list of sentinel spellings was wrong and silently dropped a
    # real result: Rating!C10 evaluates to the STRING "None" - the workbook's own wording for
    # "no hard caps applied" - and a string test discarded it on every healthy issuer.
    if type(val).__name__ == "Token" or str(type(val)).startswith("<class 'schedula"):
        return None
    if isinstance(val, np.generic):
        val = val.item()
    if val is None:
        return None
    if isinstance(val, bool):
        return ("1" if val else "0", "b")
    if isinstance(val, (int, float)):
        if isinstance(val, float) and (val != val or val in (float("inf"), float("-inf"))):
            return ("#NUM!", "e")
        return (repr(round(val, 10)) if isinstance(val, float) else str(val), None)
    s = str(val)
    if s.startswith("#") and s.endswith(("!", "?", "A")):        # #REF! #VALUE! #N/A
        return (s, "e")
    return (s, "str")


# --------------------------------------------------------------------------- rewrite the XML
CELL_RE = re.compile(rb'(<c\b[^>]*?r="([A-Z]+\d+)"[^>]*?>)((?:(?!</c>).)*?)(</c>)', re.S)


def inject(xml: bytes, sheet: str, values: dict) -> tuple[bytes, int]:
    written = 0

    def repl(m):
        nonlocal written
        open_tag, ref, inner, close = m.group(1), m.group(2).decode(), m.group(3), m.group(4)
        if b"<f" not in inner:
            return m.group(0)
        got = values.get((sheet, ref))
        cell = as_cell(got)
        if cell is None:
            return m.group(0)
        text, typ = cell
        payload = ("<v>%s</v>" % _esc(text)).encode()
        # replace an existing <v>...</v> (openpyxl leaves it empty) or append after </f>
        if re.search(rb"<v>.*?</v>", inner, re.S):
            inner2 = re.sub(rb"<v>.*?</v>", payload, inner, count=1, flags=re.S)
        else:
            inner2 = inner + payload
        # the cell's type attribute must match the payload
        tag = re.sub(rb'\s+t="[^"]*"', b"", open_tag)
        if typ:
            tag = tag[:-1] + (' t="%s">' % typ).encode()
        written += 1
        return tag + inner2 + close

    return CELL_RE.sub(repl, xml), written


def _esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def sheet_map(z: zipfile.ZipFile) -> dict:
    """{xl/worksheets/sheetN.xml: SHEETNAME} via the workbook relationships."""
    wb = z.read("xl/workbook.xml").decode("utf-8", "replace")
    rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8", "replace")
    tgt = {}
    for m in re.finditer(r'<Relationship\b[^>]*>', rels):
        rid = re.search(r'Id="([^"]+)"', m.group(0))
        t = re.search(r'Target="([^"]+)"', m.group(0))
        if rid and t:
            tgt[rid.group(1)] = t.group(1)
    out = {}
    for m in re.finditer(r'<sheet\b[^>]*/?>', wb):
        nm = re.search(r'name="([^"]+)"', m.group(0))
        rid = re.search(r'r:id="([^"]+)"', m.group(0)) or re.search(r'Id="([^"]+)"', m.group(0))
        if not (nm and rid):
            continue
        path = tgt.get(rid.group(1), "")
        if not path:
            continue
        # A relationship Target may be absolute ("/xl/worksheets/sheet1.xml") or relative to
        # the xl/ directory ("worksheets/sheet1.xml"). Prefixing blindly produced
        # "xl/xl/worksheets/..." and matched no zip entry, so nothing was ever written - the
        # verification step is what caught it.
        path = path.lstrip("/")
        if not path.startswith("xl/"):
            path = "xl/" + path
        out[path] = nm.group(1).upper()
    return out


def recalc(path: Path) -> tuple[int, int]:
    values = evaluate(path)
    src = zipfile.ZipFile(path)
    names = sheet_map(src)
    tmp = path.with_suffix(".recalc.tmp")
    total = 0
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as out:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename in names:
                data, n = inject(data, names[item.filename], values)
                total += n
            elif item.filename == "xl/workbook.xml":
                # Belt and braces: tell Excel to recalculate on open anyway, so a stale cached
                # value can never outlive an input change made by hand.
                txt = data.decode("utf-8", "replace")
                if "<calcPr" in txt:
                    txt = re.sub(r"<calcPr\b[^>]*/>",
                                 '<calcPr calcId="191029" fullCalcOnLoad="1"/>', txt, count=1)
                else:
                    txt = txt.replace("</workbook>",
                                      '<calcPr calcId="191029" fullCalcOnLoad="1"/></workbook>')
                data = txt.encode()
            out.writestr(item, data)
    src.close()
    shutil.move(str(tmp), str(path))
    return total, len(values)


def verify(path: Path) -> tuple[int, int]:
    """How many formula cells now carry a cached value, checked at the XML level.

    openpyxl's data_only read collapses an empty cached string ("<v></v>", written for a
    formula that legitimately evaluates to "") back to None - indistinguishable from a formula
    that was never recalculated at all. inject() writes a real "<v>" element either way, so
    this function checks for that element's PRESENCE in the raw XML - what was actually
    written - rather than trusting openpyxl's lossy round-trip. Found 02-Sep-2026 when
    Rating!D14 and D30 (both legitimately blank on most issuers) were reported "still blank"
    on every freshly-recalculated workbook, which made --all abort mid-batch believing the
    recalculation had failed when it had not.
    """
    src = zipfile.ZipFile(path)
    names = sheet_map(src)
    have = miss = 0
    for filename in names:
        xml = src.read(filename)
        for m in CELL_RE.finditer(xml):
            open_tag, inner = m.group(1), m.group(3)
            if b"<f" not in inner:
                continue
            v = re.search(rb"<v>(.*?)</v>", inner, re.S)
            # openpyxl's OWN untouched formula cell also carries an empty "<v></v>" with no
            # "t" attribute - presence of the tag alone does not prove recalc() ever ran.
            # inject() is the only writer that ever sets t="str"/"e"/"b" on a formula cell, so
            # that attribute - not bare "<v>" presence - is the reliable signal a real result
            # (even a legitimately empty string) was actually written.
            has_content = bool(v and v.group(1))
            was_typed = bool(re.search(rb'\st="(?:str|e|b)"', open_tag))
            if has_content or was_typed:
                have += 1
            else:
                miss += 1
    src.close()
    return have, miss


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--all-scorecards":
        targets = sorted(ROOT.glob("Companies/*/Rating_Scorecard*.xlsx"))
    else:
        targets = [Path(a) for a in argv]
    if not targets:
        print("no workbooks matched")
        return 1
    bad = 0
    for t in targets:
        if not t.is_file():
            print("MISSING  %s" % t)
            bad += 1
            continue
        try:
            written, computed = recalc(t)
            have, miss = verify(t)
        except Exception as e:                                            # noqa: BLE001
            print("FAILED   %-58s %s" % (t.name, e))
            bad += 1
            continue
        rel = t.relative_to(ROOT) if ROOT in t.parents else t.name
        if have + miss == 0:
            # A hand-built workbook with no formula cells needs nothing doing to it. Reporting
            # that as PARTIAL would be a false alarm, and a checker that cries wolf gets ignored.
            print("%-8s %-58s no formula cells - nothing to recalculate" % ("SKIP", rel))
            continue
        ok = miss == 0
        print("%-8s %-58s wrote %3d of %3d formula cells; still blank: %d"
              % ("OK" if ok else "PARTIAL", rel, written, have + miss, miss))
        if not ok:
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
