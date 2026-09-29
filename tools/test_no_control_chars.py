"""Guard against control characters silently substituted into source, especially in regexes.

WHY THIS EXISTS. Six times on 06-Sep-2026, an edit that intended to write the two characters
backslash-b into a regex instead wrote byte 0x08 - a literal BACKSPACE - because the editing
path collapsed one level of escaping. The result compiles, imports, and runs. It just never
matches, so the check silently passes everything:

    r"\bCRISIL[ ]+INFRA..."   intended - a word boundary
    r"<0x08>CRISIL[ ]+INFRA..."  written - a literal backspace, matches nothing

Every instance was caught only because a positive control failed. That is the system working,
but it is an expensive way to find a one-byte defect, and a probe WITHOUT a control would have
shipped broken and silent - which is the worst failure shape this project has (failure mode 39:
a check that cannot fail is not a check). This test makes the defect visible directly.

It scans for the C0 control characters that have no business in Python source: everything below
0x20 except tab (0x09) and newline (0x0A), plus DEL (0x7F). Carriage return (0x0D) is allowed
so the test does not fight line endings on Windows.

Run: python tools/test_no_control_chars.py
"""
import sys
import unicodedata
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ALLOWED = {0x09, 0x0A, 0x0D}


def scan(path: Path):
    """Return [(line_no, col, codepoint, line_text), ...] for stray control characters."""
    hits = []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return hits
    for i, line in enumerate(text.splitlines(), 1):
        for j, ch in enumerate(line, 1):
            cp = ord(ch)
            if cp in ALLOWED:
                continue
            if cp < 0x20 or cp == 0x7F:
                hits.append((i, j, cp, line))
    return hits


def main():
    files = sorted(TOOLS.glob("*.py"))
    total = 0
    for f in files:
        for line_no, col, cp, line in scan(f):
            total += 1
            try:
                name = unicodedata.name(chr(cp))
            except ValueError:
                name = "unnamed control character"
            print(f"[FAIL] {f.name}:{line_no}:{col} - U+{cp:04X} ({name})")
            print(f"        {line.strip()[:100]}")
            if cp == 0x08:
                print("        This is almost certainly a backslash-b word boundary that lost "
                      "one level of escaping. The regex will never match.")
    print()
    if total:
        print(f"{total} stray control character(s) across {len(files)} file(s) - FAILED")
        return 1
    print(f"clean - no stray control characters in {len(files)} tool file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
