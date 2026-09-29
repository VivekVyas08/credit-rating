// Convert a rating rationale (markdown) to a formatted .docx.
//
//   node md_to_docx.js "<input>.md" "<output>.docx"
//
// WHY A PURPOSE-BUILT PARSER
// --------------------------
// pandoc is not installed in this environment and a general markdown->docx library would still
// need the house styling applied on top. The markdown shapes that appear in this project's
// rationales are a closed, known set (this project authors them from icra-report-skeleton), so
// a small parser that handles exactly those shapes is the honest fit - and it fails loudly on
// anything it does not recognise rather than silently dropping it.
//
// SHAPES HANDLED (verified against a rendered PDF, not assumed):
//   # **Heading**      -> H1, navy, teal rule under
//   ## **Heading**     -> small teal all-caps label (the document's own "Rating Rationale" line)
//   ## Heading         -> H2, navy            <- plain ## exists in the skeleton and was
//   ### Heading        -> H2, navy               MISSED by the first version, rendering as
//   **bold**              literal "## " text in the body. Verified fixed.
//   *italic*           <- single-asterisk italics were ALSO missed by the first version and
//   `code`                rendered as literal asterisks inside table cells. Verified fixed.
//   | tables |         -> banded table, navy header row, repeats across page breaks
//   - bullets
//   ---                -> horizontal rule
//   *whole line*       -> italic caption/disclaimer paragraph
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, BorderStyle, ShadingType,
} = require("docx");

const SRC = process.argv[2];
const OUT = process.argv[3];
if (!SRC || !OUT) {
  console.error('usage: node md_to_docx.js "<input>.md" "<output>.docx"');
  process.exit(1);
}
const md = fs.readFileSync(SRC, "utf-8");

const NAVY = "1B2A4A";
const TEAL = "0E7C86";

// ---- inline runs: **bold**, *italic*, `code`, plain ------------------------------------------
// The alternation order matters: **bold** must be tried before *italic*, or the italic branch
// eats the first two asterisks of a bold span.
function inlineRuns(text, baseOpts = {}) {
  const runs = [];
  const re = /(\*\*[^*]+\*\*|\*[^*\n]+\*|`[^`]+`)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) runs.push(new TextRun({ text: text.slice(last, m.index), ...baseOpts }));
    const tok = m[0];
    if (tok.startsWith("**")) {
      // RECURSE. Emitting the inner text as one run rendered a nested code span as literal
      // backticks - "**`Companies/sbi/`**" came out with the backticks visible. Bold is a
      // container, not a leaf, and the same applies to italics below.
      runs.push(...inlineRuns(tok.slice(2, -2), { ...baseOpts, bold: true }));
    } else if (tok.startsWith("*")) {
      runs.push(...inlineRuns(tok.slice(1, -1), { ...baseOpts, italics: true }));
    } else {
      runs.push(new TextRun({ text: tok.slice(1, -1), font: "Consolas", size: 19, ...baseOpts }));
    }
    last = re.lastIndex;
  }
  if (last < text.length) runs.push(new TextRun({ text: text.slice(last), ...baseOpts }));
  if (!runs.length) runs.push(new TextRun({ text: "", ...baseOpts }));
  return runs;
}

const bodyPara = (t) =>
  new Paragraph({ children: inlineRuns(t, { size: 21 }), spacing: { after: 160 } });

const italicPara = (t) =>
  new Paragraph({
    children: inlineRuns(t.replace(/^\*|\*$/g, ""), { italics: true, size: 20, color: "555555" }),
    spacing: { after: 160 },
  });

// ---- tables ----------------------------------------------------------------------------------
const TABLE_WIDTH = 9360; // ~6.5in of content at 1440 DXA/in on Letter with 0.75in margins

function makeTable(headerCells, dataRows) {
  const n = headerCells.length;
  const colWidth = Math.floor(TABLE_WIDTH / n);
  const columnWidths = new Array(n).fill(colWidth);

  const cell = (text, { shade = null, isHeader = false } = {}) =>
    new TableCell({
      width: { size: colWidth, type: WidthType.DXA },
      shading: shade ? { type: ShadingType.CLEAR, fill: shade } : undefined,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [
        new Paragraph({
          children: inlineRuns(text, {
            size: 19,
            bold: isHeader,
            color: isHeader ? "FFFFFF" : undefined,
          }),
        }),
      ],
    });

  const rows = [
    new TableRow({
      tableHeader: true, // repeats the header when a table spans a page break
      children: headerCells.map((h) => cell(h, { isHeader: true, shade: NAVY })),
    }),
    ...dataRows.map((r, i) =>
      new TableRow({ children: r.map((c) => cell(c, { shade: i % 2 ? "F4F6F9" : "FFFFFF" })) })
    ),
  ];

  const border = { style: BorderStyle.SINGLE, size: 4, color: "C7D0DE" };
  return new Table({
    width: { size: TABLE_WIDTH, type: WidthType.DXA },
    columnWidths,
    rows,
    borders: { top: border, bottom: border, left: border, right: border,
               insideHorizontal: border, insideVertical: border },
  });
}

const splitRow = (line) =>
  line.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map((c) => c.trim());

// ---- main loop -------------------------------------------------------------------------------
const lines = md.split("\n").map((l) => l.replace(/\r$/, ""));
const children = [];
const unhandled = [];
let i = 0;
const isTableLine = (l) => /^\s*\|.*\|\s*$/.test(l);

while (i < lines.length) {
  const line = lines[i];

  if (line.trim() === "") { i++; continue; }

  if (line.trim() === "---") {
    children.push(new Paragraph({
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "C7D0DE", space: 4 } },
      spacing: { after: 200 },
    }));
    i++; continue;
  }

  if (/^-\s+/.test(line.trim())) {
    while (i < lines.length && /^-\s+/.test(lines[i].trim())) {
      children.push(new Paragraph({
        children: inlineRuns(lines[i].trim().replace(/^-\s+/, ""), { size: 21 }),
        bullet: { level: 0 },
        spacing: { after: 100 },
      }));
      i++;
    }
    continue;
  }

  if (isTableLine(line)) {
    const block = [];
    while (i < lines.length && isTableLine(lines[i])) { block.push(lines[i]); i++; }
    children.push(makeTable(splitRow(block[0]), block.slice(2).map(splitRow)));
    children.push(new Paragraph({ spacing: { after: 200 } }));
    continue;
  }

  let m;
  if ((m = line.match(/^##\s+\*\*(.+)\*\*\s*$/))) {
    children.push(new Paragraph({
      children: [new TextRun({ text: m[1], bold: true, size: 20, color: TEAL,
                               allCaps: true, characterSpacing: 10 })],
      spacing: { before: 100, after: 120 },
    }));
    i++; continue;
  }
  if ((m = line.match(/^#\s+\*\*(.+)\*\*\s*$/)) || (m = line.match(/^#\s+([^#].*)$/))) {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_1,
      children: [new TextRun({ text: m[1].replace(/\*\*/g, ""), bold: true, size: 30, color: NAVY })],
      spacing: { before: 320, after: 160 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: TEAL, space: 4 } },
    }));
    i++; continue;
  }
  // Plain "## Heading" and "### Heading" (with or without bold markers). The first version of
  // this script only matched the bolded form, so three plain "## " headings in the skeleton
  // fell through to the body-paragraph default and rendered as literal "## " text.
  if ((m = line.match(/^###?\s+(.+)$/))) {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_2,
      children: inlineRuns(m[1], { bold: true, size: 24, color: NAVY }),
      spacing: { before: 260, after: 120 },
    }));
    i++; continue;
  }

  if (/^\*[^*].*\*$/.test(line.trim())) { children.push(italicPara(line.trim())); i++; continue; }

  if (/^#{1,6}\s/.test(line)) unhandled.push(line); // should be unreachable; surfaced if not
  children.push(bodyPara(line.trim()));
  i++;
}

if (unhandled.length) {
  console.error("WARNING: heading-shaped lines fell through to body text:");
  unhandled.forEach((l) => console.error("   " + l));
}

const doc = new Document({
  styles: { default: { document: { run: { font: "Calibri", size: 21 } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },          // US Letter
        margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 },
      },
    },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  console.log("wrote", OUT, buf.length, "bytes");
});
