"""Corpus-integrity scanner for methodology-folder markdown tables (failure mode 49).

WHY THIS EXISTS: CareEdge's own Rating_of_Short_Term_Instruments_Feb_2025.md carries a fully-
formed LT-ST mapping table - header row, every long-term grade down the side - with every DATA
cell blank, because the source was an image/chart the PDF-to-markdown conversion could not
read. The table LOOKS present: header row intact, row labels intact, pipe-delimited structure
intact. Any check that only verifies "does a table exist under this heading" would PASS it.
Found 13-Sep-2026 reading the CareEdge methodology corpus in full, by eye, not by any tool -
which is exactly why this tool now exists.

WHAT IT DOES: walks every markdown table in every methodology file across all three agencies
and flags a table whose LABEL column (first cell of each row) is populated across N or more
consecutive rows while the DATA cells (every other cell) are empty across that entire run. A
table that is genuinely just a section-heading list (no data columns at all) is not flagged -
only a table that HAS data columns (multiple pipe-separated cells) which are systematically
blank is the CareEdge LT-ST signature.

USAGE
    python tools/corpus_table_integrity.py                 # scan all three agencies
    python tools/corpus_table_integrity.py <file.md> ...    # scan specific files
    python tools/corpus_table_integrity.py --selftest       # positive control
Exit 1 if any corrupted table is found, so it can gate the same way check_sections.py does.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENCY_METHODOLOGY_DIRS = [
    ROOT / "Methodology",
    ROOT / "CRISIL" / "Methodology",
    ROOT / "CareEdge" / "Methodology",
]

MIN_RUN = 3  # a table with fewer than this many consecutive blank-data rows is not flagged -
             # one blank row is very likely a formatting quirk, not a lost chart.


def _row_cells(line: str):
    """Split a markdown table row into cells, preserving genuinely empty ones.

    str.strip("|") strips EVERY leading/trailing pipe character, not just the one table
    delimiter - so a row ending "||||" (several adjacent empty cells) had every one of those
    empty cells silently deleted before this bug was caught by this tool's own positive
    control. Only the single outer delimiter on each side may be removed.
    """
    s = line.strip()
    if "|" not in s:
        return None
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def _is_separator(cells):
    return bool(cells) and all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c.strip())


def find_blank_data_tables(text: str):
    """Returns [(heading, first_row_label, run_length), ...] for each corrupted table found.

    A markdown table's own header row(s) - everything before the "|---|---|" separator - are
    NOT checked for blank data, since a header row's cells are column titles, not values (the
    CareEdge table's header row genuinely reads "A1+ | A1 | A2+ ..." and is correctly populated;
    it is every DATA row beneath it that lost its values). Only rows AFTER the separator count.
    """
    lines = text.splitlines()
    findings = []
    heading = ""
    i = 0
    while i < len(lines):
        h = re.match(r"^\s{0,3}#{1,6}\s*(.+)$", lines[i])
        if h:
            heading = re.sub(r"[*_`]", "", h.group(1)).strip()
            i += 1
            continue
        cells = _row_cells(lines[i])
        if cells is None or len(cells) < 2 or _is_separator(cells):
            i += 1
            continue
        # This is a table HEADER row (first pipe-row of a table, pre-separator). Walk forward:
        # skip any further header rows and the separator, then collect DATA rows only.
        j = i + 1
        while j < len(lines):
            c = _row_cells(lines[j])
            if c is None:
                break
            if _is_separator(c):
                j += 1
                break
            j += 1
        else:
            j = len(lines)
        # A markdown table converted from a two-row-header source (this project's own PDF
        # conversions do this) can put a SECOND header row - sub-column labels, e.g. the short-
        # term grades "A1+ | A1 | A2+ ..." - immediately after the separator, with an empty
        # first cell. Treat any such empty-first-cell row right after the separator as more
        # header, not data, so its populated sub-labels don't mask a genuinely data-less table.
        while j < len(lines):
            c = _row_cells(lines[j])
            if c is not None and len(c) >= 2 and not c[0].strip():
                j += 1
                continue
            break
        data_rows = []
        while j < len(lines):
            c = _row_cells(lines[j])
            if c is None or len(c) < 2:
                break
            data_rows.append(c)
            j += 1
        i = j
        if len(data_rows) < MIN_RUN:
            continue
        blank_data_rows = [r for r in data_rows if r[0].strip()
                           and all(not c.strip() for c in r[1:])]
        has_any_data_value = any(any(c.strip() for c in r[1:]) for r in data_rows)
        if len(blank_data_rows) >= MIN_RUN and not has_any_data_value:
            findings.append((heading, data_rows[0][0][:60], len(blank_data_rows)))
    return findings


def scan_dir(d: Path):
    out = []
    if not d.is_dir():
        return out
    for f in sorted(d.glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        for heading, label, n in find_blank_data_tables(text):
            out.append((f, heading, label, n))
    return out


def selftest():
    """Positive control: a table that lost its data cells (the CareEdge signature) MUST fire;
    a normal populated table, and a genuine one-column list, must NOT."""
    corrupted = """
# Chart: Indicative mapping of ratings

|**Long-term ratings**||**Corresponding short-term ratings**||||
|---|---|---|---|---|---|
||**A1+**|**A1**|**A2+**|**A2**|**A3+**|
|**AAA**||||||
|**AA+**||||||
|**AA**||||||
|**AA-**||||||
"""
    clean_populated = """
# Assessment of asset quality

|Ratio|Strongest|Weakest|
|---|---|---|
|Gross NPA %|<=2%|>=6%|
|Net NPA %|<=0.7%|>=3.3%|
|Slippage rate|<=1%|>=4%|
"""
    clean_list = """
# Contents

|Overview .............................. 1|
|---|
|Business Risk Assessment ............ 2|
|Financial Risk Assessment ........... 4|
|Summing Up ........................... 9|
"""
    r1 = find_blank_data_tables(corrupted)
    r2 = find_blank_data_tables(clean_populated)
    r3 = find_blank_data_tables(clean_list)
    ok = bool(r1) and not r2 and not r3
    print(f"[{'OK' if bool(r1) else 'FAIL'}] fires on a table with lost data cells -> {r1}")
    print(f"[{'OK' if not r2 else 'FAIL'}] does not fire on a normally populated table -> {r2}")
    print(f"[{'OK' if not r3 else 'FAIL'}] does not fire on a one-column heading list -> {r3}")
    return 0 if ok else 1


def main(argv):
    if len(argv) > 1 and argv[1] == "--selftest":
        return selftest()
    files = [Path(a) for a in argv[1:]] if len(argv) > 1 else None
    findings = []
    if files:
        for f in files:
            text = f.read_text(encoding="utf-8", errors="replace")
            for heading, label, n in find_blank_data_tables(text):
                findings.append((f, heading, label, n))
    else:
        for d in AGENCY_METHODOLOGY_DIRS:
            findings.extend(scan_dir(d))

    print(f"Methodology table-integrity scan - {len(findings)} corrupted table(s) found")
    print("=" * 78)
    for f, heading, label, n in findings:
        try:
            rel = f.relative_to(ROOT)
        except ValueError:
            rel = f
        print(f"[CORRUPTED] {rel}")
        print(f"    section: {heading!r}")
        print(f"    table starts at row labelled {label!r}, {n} row(s) with a label but no data")
        print(f"    -> this table looked present to a header/shape check but carries no data;")
        print(f"       do not treat any value from it as verified without re-extracting from a")
        print(f"       clean source (failure mode 49).")
    if not findings:
        print("no corrupted tables detected")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
