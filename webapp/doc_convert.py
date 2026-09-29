"""Convert an uploaded document to Markdown for the SOP's document-reading tools.

Excel workbooks are never converted - a company-supplied .xlsx is a legitimate document in its
own right (compute_ratios.py and icra-doc-extract both expect financial figures to sometimes
arrive as native spreadsheets), and .md files need no conversion. Everything else that has a
converter here - PDF, Word, plain text/CSV, HTML - is turned into a .md file with the same
stem, so every downstream tool (preflight.py's rglob("*.md"), icra-doc-extract's section map,
the ratio-extraction skills) sees one consistent format regardless of what the operator upload.

Each converter takes a `progress` callback: `progress(done, total)`, called at least once per
unit of work, so a caller can drive a progress bar. Callers must treat `progress` as optional
(pass a no-op if untracked).
"""

from __future__ import annotations

import csv
import io
import shutil
from pathlib import Path
from typing import Callable

Progress = Callable[[int, int], None]


def _noop(done: int, total: int) -> None:
    pass


# Extensions with a converter below. Anything not in this set (images, .pptx, .zip, etc.) is
# left as uploaded rather than silently dropped - see webapp/app.py's handling of "unsupported".
CONVERTIBLE_EXTS = {".pdf", ".docx", ".doc", ".txt", ".csv", ".htm", ".html"}
# Extensions that need no conversion - they land in the slot folder as-is.
NATIVE_EXTS = {".md", ".markdown", ".xlsx", ".xls", ".xlsm"}


def needs_conversion(path: Path) -> bool:
    return path.suffix.lower() in CONVERTIBLE_EXTS


def is_native(path: Path) -> bool:
    return path.suffix.lower() in NATIVE_EXTS


# --------------------------------------------------------------------------------------- PDF
def convert_pdf(src: Path, progress: Progress = _noop) -> str:
    """Page-by-page conversion so progress can be reported, with OCR fallback per page.

    Mirrors the page_to_markdown logic in the standalone pdf-to-markdown tool: a page with
    almost no extractable text is treated as scanned and sent to Tesseract if available.
    """
    import pymupdf

    OCR_TEXT_THRESHOLD = 20
    ocr = _ocr_backend()

    doc = pymupdf.open(src)
    try:
        total = doc.page_count
        parts = []
        for i in range(total):
            plain = doc[i].get_text().strip()
            if ocr is not None and len(plain) < OCR_TEXT_THRESHOLD:
                text = ocr(doc, i)
                parts.append((text or plain) + "\n\n")
            else:
                try:
                    import pymupdf4llm
                    parts.append(pymupdf4llm.to_markdown(doc, pages=[i]))
                except Exception:                                         # noqa: BLE001
                    # pymupdf4llm occasionally chokes on unusual table layouts; fall back to
                    # plain text for just that page rather than failing the whole document.
                    parts.append(plain + "\n\n")
            progress(i + 1, total)
        return "".join(parts)
    finally:
        doc.close()


def _ocr_backend():
    """Return a `(doc, page_index) -> str` OCR function, or None if Tesseract is unavailable."""
    try:
        import pytesseract
        from PIL import Image

        tess = shutil.which("tesseract")
        if not tess:
            for candidate in (
                r"C:\Program Files\Tesseract-OCR\tesseract.exe",
                r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
            ):
                if Path(candidate).exists():
                    tess = candidate
                    break
        if not tess:
            return None
        pytesseract.pytesseract.tesseract_cmd = tess

        def run(doc, index):
            pix = doc[index].get_pixmap(dpi=300)
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            return pytesseract.image_to_string(img).strip()

        return run
    except Exception:                                                     # noqa: BLE001
        return None


# -------------------------------------------------------------------------------------- DOCX
def convert_docx(src: Path, progress: Progress = _noop) -> str:
    """Paragraphs become text (headings by style name), tables become Markdown tables.

    python-docx exposes the body as a flat sequence of paragraphs and tables with no combined
    document-order iterator, so the underlying XML element order is walked directly to keep
    tables in their correct position relative to surrounding text - reading paragraphs() and
    tables() as two separate lists would silently move every table to the end of the document.
    """
    from docx import Document
    from docx.table import Table
    from docx.text.paragraph import Paragraph

    doc = Document(str(src))
    body = doc.element.body
    block_items = list(body.iterchildren())
    total = max(1, len(block_items))
    lines: list[str] = []

    for i, child in enumerate(block_items):
        if child.tag.endswith("}tbl"):
            table = Table(child, doc)
            lines.append(_table_to_markdown(table))
        elif child.tag.endswith("}p"):
            para = Paragraph(child, doc)
            style = (para.style.name or "").lower() if para.style else ""
            text = para.text.strip()
            if text:
                if style.startswith("heading"):
                    level = "".join(c for c in style if c.isdigit()) or "1"
                    lines.append("#" * min(6, int(level)) + " " + text)
                elif style == "title":
                    lines.append("# " + text)
                else:
                    lines.append(text)
                lines.append("")
        progress(i + 1, total)

    return "\n".join(lines)


def _table_to_markdown(table) -> str:
    rows = [[cell.text.strip().replace("\n", " ") for cell in row.cells] for row in table.rows]
    if not rows:
        return ""
    out = ["| " + " | ".join(rows[0]) + " |",
           "|" + "|".join(["---"] * len(rows[0])) + "|"]
    for row in rows[1:]:
        out.append("| " + " | ".join(row) + " |")
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------------- TXT / CSV
def convert_txt(src: Path, progress: Progress = _noop) -> str:
    text = src.read_text(encoding="utf-8", errors="replace")
    progress(1, 1)
    return text


def convert_csv(src: Path, progress: Progress = _noop) -> str:
    with src.open(encoding="utf-8", errors="replace", newline="") as f:
        rows = list(csv.reader(f))
    progress(1, 2)
    if not rows:
        return ""
    out = ["| " + " | ".join(rows[0]) + " |",
           "|" + "|".join(["---"] * len(rows[0])) + "|"]
    for row in rows[1:]:
        row = row + [""] * (len(rows[0]) - len(row))
        out.append("| " + " | ".join(row[:len(rows[0])]) + " |")
    progress(2, 2)
    return "\n".join(out)


# --------------------------------------------------------------------------------------- HTML
def convert_html(src: Path, progress: Progress = _noop) -> str:
    """Strip tags to plain text. No layout preservation - good enough for a fallback source."""
    import re

    html = src.read_text(encoding="utf-8", errors="replace")
    html = re.sub(r"(?is)<(script|style).*?</\1>", "", html)
    html = re.sub(r"(?i)<br\s*/?>", "\n", html)
    # Any closing block-level tag becomes a paragraph break, not just </p> - otherwise
    # "<h1>Title</h1><p>Hello</p>" collapses to "TitleHello" with no separator at all.
    html = re.sub(r"(?i)</(p|div|h[1-6]|li|tr|table|section|article)>", "\n\n", html)
    text = re.sub(r"<[^>]+>", "", html)
    text = re.sub(r"\n{3,}", "\n\n", text)
    progress(1, 1)
    return text.strip()


CONVERTERS = {
    ".pdf": convert_pdf,
    ".docx": convert_docx,
    ".doc": convert_docx,             # python-docx cannot open legacy .doc; caller catches this
    ".txt": convert_txt,
    ".csv": convert_csv,
    ".htm": convert_html,
    ".html": convert_html,
}


def convert(src: Path, progress: Progress = _noop) -> str:
    """Dispatch to the right converter. Raises for an extension with no converter."""
    fn = CONVERTERS.get(src.suffix.lower())
    if fn is None:
        raise ValueError("no converter for %s" % src.suffix)
    return fn(src, progress)
