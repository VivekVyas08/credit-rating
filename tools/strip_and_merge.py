"""Strip boilerplate footers from methodology files and merge into large chunks.

Every ICRA/CRISIL methodology file ends with an identical contact/About/Disclaimer
block that carries zero analytical content but is ~20-40% of each file's bytes.
Truncating at the first boilerplate marker and merging many files into one large
chunk cuts both the token cost of reading the corpus and the number of Read calls
needed (fewer, bigger reads beat many small ones).
"""
import os, re, sys

MARKERS = [
    r"^#?\s*\*?\*?RELATIONSHIP CONTACT",
    r"^#?\s*\*?\*?MEDIA AND PUBLIC RELATIONS CONTACT",
    r"^#?\s*\*?\*?About ICRA Limited",
    r"^#?\s*\*?\*?About Crisil Ratings Limited",
    r"^#?\s*\*?\*?About Crisil\b",
    r"^#?\s*\*?\*?Crisil Privacy",
    r"^Sensitivity Label\s*:\s*Public\s*$",
    r"^#?\s*\*?\*?ICRA Limited\*?\*?\s*$",
]
MARKER_RE = re.compile("|".join(MARKERS), re.I)


# Every ICRA page repeats a "picture text" span for its logo/footer -- the URL, the
# "Sensitivity Label" tag, the running "ICRA Rating Methodology ... <SECTOR>" header,
# and (as separate spans) the "Weakest"/"Strongest" diagram-arrow labels that already
# duplicate the real pipe-table two rows below. None of it is analytical, and on a
# 700-line file it was multiplying read cost several times over. Strip every such span
# (start marker .. end marker, same-line combined or not) plus bare "Page |N" lines.
PICTURE_RE = re.compile(r"<!--\s*Start of picture text\s*-->.*?<!--\s*End of picture text\s*-->",
                        re.I | re.S)
PAGE_NUM_RE = re.compile(r"^\s*Page\s*\|\s*\d+\s*$", re.I)


def strip(text):
    lines = text.splitlines()
    end = len(lines)
    for i, ln in enumerate(lines):
        if MARKER_RE.match(ln.strip()):
            end = i
            break
    body = "\n".join(lines[:end])
    body = PICTURE_RE.sub("", body)
    kept = [ln for ln in body.splitlines() if not PAGE_NUM_RE.match(ln)]
    out, blanks = [], 0
    for ln in kept:
        if ln.strip() == "":
            blanks += 1
            if blanks <= 1:
                out.append(ln)
        else:
            blanks = 0
            out.append(ln)
    return "\n".join(out).rstrip()


def merge(src_dir, out_dir, chunk_files, prefix):
    files = sorted(f for f in os.listdir(src_dir) if f.endswith(".md"))
    os.makedirs(out_dir, exist_ok=True)
    saved_before = saved_after = 0
    chunk_no = 0
    buf = []
    for i, f in enumerate(files):
        raw = open(os.path.join(src_dir, f), encoding="utf-8", errors="replace").read()
        stripped = strip(raw)
        saved_before += len(raw)
        saved_after += len(stripped)
        buf.append("\n\n" + "=" * 100 + f"\nFILE: {f}\n" + "=" * 100 + "\n\n" + stripped)
        if len(buf) >= chunk_files or i == len(files) - 1:
            chunk_no += 1
            path = os.path.join(out_dir, f"{prefix}_chunk{chunk_no:02d}.md")
            open(path, "w", encoding="utf-8").write("".join(buf))
            buf = []
    return len(files), chunk_no, saved_before, saved_after


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(root, "Docs", "corpus_review", "merged")
    n1, c1, b1, a1 = merge(os.path.join(root, "Methodology"), out, 10, "ICRA")
    n2, c2, b2, a2 = merge(os.path.join(root, "CRISIL", "Methodology"), out, 10, "CRISIL")
    print(f"ICRA:   {n1} files -> {c1} chunks, {b1} -> {a1} bytes ({100*a1/b1:.0f}% kept)")
    print(f"CRISIL: {n2} files -> {c2} chunks, {b2} -> {a2} bytes ({100*a2/b2:.0f}% kept)")
