#!/usr/bin/env python3
"""PRE-FLIGHT: run at Step 1b, BEFORE any analysis, for every rating case.

WHY THIS EXISTS
---------------
An audit of this project's guidance on 13-Aug-2026 found:
  * 88% of the 24 named failure modes were PROSE-ONLY - no mechanical check.
  * EVERY significant error made on 11-13 Aug was already covered by written guidance
    (ESG section: in SKELETON.md and CLAUDE.md S7; the AR's credit-rating note: Step 7b;
    the prior rating action: Step 14; naming consolidated entities: failure mode 17).
  * Rules recur after being written - failure mode 17 was authored 11-Aug and violated 13-Aug.
So the deficiency is not content. It is that prose rules do not fire.

The dominant error is CLAIMING SOMETHING IS ABSENT WITHOUT LOOKING - which on 13-Aug caused a
published rating to be one notch wrong, because the correct rating was stated four times in the
issuer's own annual report and once in a reference-library rationale, both declared "not found".

This script LOOKS FIRST and prints what EXISTS, so the false-absence claim becomes impossible.
It answers, with evidence, the questions most often got wrong:
    1. Is there a prior rating action for this issuer?      (Step 14)
    2. Does the AR carry a credit-ratings note?             (Step 7b)
    3. What subsidiaries/entities must be NAMED?            (failure mode 17)
    4. Is ESG data present, and how much?                   (failure mode 19/20)
    5. Which sector KPI must appear, and is it there?       (failure mode 21)
    6. Are instrument details available?                    (Step 7b)

USAGE
    python preflight.py <case-slug>          e.g.  python preflight.py indus-towers
Paste the output into the workpaper's Read Log. Anything reported PRESENT here may never later
be described as "not available" without a second, recorded search that contradicts this one.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # this script now lives in tools/,
# one level below the project root - moved here 01-Sep-2026 to declutter the root.
AGENCY_DIRS = {"ICRA": ROOT / "Report for Reference",
               "CRISIL": ROOT / "CRISIL/Report for Reference",
               "CareEdge": ROOT / "CareEdge/Report for Reference"}

PROBES = [
    ("CREDIT-RATING NOTE in the issuer's own AR  (Step 7b)",
     r"(crisil|icra|care rating|india ratings)[^\n]{0,80}(aaa|aa[+-]?|a1\+|reaffirm|upgrad|assign)"
     r"|rating[s]? (reaffirmed|upgraded|assigned|revised)|credit rating[s]?\b",
     "If PRESENT you already know the outstanding rating - declare the anchor exposure and NEVER "
     "write 'no rating disclosed'."),
    ("SUBSIDIARIES / entities to NAME  (failure mode 17)",
     r"\bAOC-?1\b|wholly[- ]owned subsidiar|subsidiar(y|ies)|joint venture|associate compan",
     "Every entity must be NAMED in the entities-consolidated annexure regardless of materiality."),
    ("ESG data  (failure modes 19/20)",
     r"net[- ]?zero|sbti|science based target|scope [123]|ghg|emission|renewable|solar|"
     r"water positive|ltifr|lost time injury|gender diversity|women direct|csr|biodiversity",
     "If PRESENT you may NOT write 'ESG data not extractable'. Extract and quote the numbers."),
    ("INSTRUMENT details  (Step 7b)",
     r"INE[0-9A-Z]{9,10}|non.?convertible debenture|commercial paper|coupon|debenture trustee",
     "Populate Annexure I from these; mark only genuinely undisclosed amounts as TBC."),
    ("CAPEX / investment cycle",
     r"capital expenditure|capex|capital work.in.progress",
     "Capital-intensive sectors: capex must appear in the rationale."),
    ("SHAREHOLDING / promoter stake",
     r"promoter[s]?[^\n]{0,40}\d{1,2}\.\d{1,2}\s?%|holding[^\n]{0,30}\d{1,2}\.\d{1,2}\s?%",
     "Quantify the controlling stake - never write 'controlling shareholder' bare."),
    ("AUDITOR opinion / KAM / Emphasis of Matter",
     r"key audit matter|emphasis of matter|unmodified opinion|qualified opinion|independent auditor",
     "An EOM or qualification is rating-relevant regardless of quantum (R13)."),
]

SECTOR_KPI = [
    (r"telecom tower|tower (company|operator)|co-location", r"tenancy ratio|sharing ratio", "tenancy / sharing ratio"),
    (r"zinc|smelter|mined metal|mining",     r"cost of production|per tonne",        "cost of production per tonne"),
    (r"forging|forged and machined",         r"capacity utilisation|utilization",    "capacity utilisation"),
    (r"\bdistribut|trading compan",          r"receivable days|gross current asset", "receivable / GCA days"),
    (r"cement",                              r"capacity utilisation|ebitda.{0,3}/.{0,3}tonne", "utilisation / EBITDA per tonne"),
    (r"\bhotel|hospitality",                 r"revpar|occupancy",                    "RevPAR / occupancy"),
    # NBFC listed FIRST and separately from banks. Ind AS NBFC financial statements label bad
    # loans "Stage III" inside ECL movement tables - NOT "GNPA", which is bank vocabulary.
    # Searching only for GNPA returned zero hits on NABKISAN (19-Aug-2026) and produced a FALSE
    # absence claim in a delivered report, while 28 "Stage 3" and 25 "Stage III" hits sat in the
    # documents. The gate passed it because a search WAS cited - it cannot tell whether the
    # search terms were the right ones. This probe supplies the right ones.
    (r"\bnbfc\b|non-banking financial compan|housing finance compan",
     r"stage 3|stage iii|expected credit loss|\becl\b|gross carrying amount|\bcrar\b|"
     r"assets under management|\baum\b",
     "Stage III / ECL / AUM / CRAR  (an NBFC says 'Stage III', never 'GNPA')"),
    (r"\bthe bank\b|scheduled commercial bank|banking regulation act|net interest margin",
     r"\bnim\b|gnpa|\bcrar\b|capital adequacy|casa ratio",
     "NIM / GNPA / CRAR / CASA"),
]

# A name is an acronym-like stub if every token is short; such names yield no usable search
# token under the >3 rule and previously caused an EMPTY search to be reported as evidenced
# absence (SBI, 14-Aug-2026). Minimum token length is now 3, never zero tokens silently.
LEGAL_NAME_RE = re.compile(
    r"\b((?:[A-Z][A-Za-z&.\-]*\s+){1,4}"
    r"(?:Limited|Ltd\.?|Bank of India|Bank|Corporation|Industries|Enterprises))\b")


GENERIC_TOKENS = {
    "industries", "industry", "limited", "corporation", "company", "companies",
    "group", "india", "private", "enterprises", "holdings", "international",
    "bank",  # "State Bank of India" -> search "State", else every bank in the library matches
}


def _brief_financial_rows(text):
    """Row LABELS of a CareEdge 'Brief Financials' table.

    The row set forks by entity type - corporate reports are PBILDT-based, financial-sector
    ones TNW-based, banks NIM/GNPA-based - so it cannot be recalled from memory and must be
    read off a peer. Shared by the [1b] printout and the peer_rows.json the gate verifies.
    """
    # Each agency names this table differently - CareEdge "Brief Financials", CRISIL and ICRA
    # "Key Financial Indicators". Matching only CareEdge's name left the check inert for the
    # other two agencies' cases.
    m = re.search(r"(?:Brief Financials|Key Financial Indicators?|Financial Indicators?)"
                  r"[^\n]*\n(.*?)(?:\n\s*\n|\nA:|\n##)", text, re.S | re.I)
    if not m:
        return []
    out = []
    for line in m.group(1).split("\n"):
        cells = [c.strip(" *_") for c in line.strip().strip("|").split("|")]
        if cells and cells[0] and not set(cells[0]) <= set("-: "):
            lab = re.sub(r"<[^>]+>", "", cells[0]).strip(" *_")
            # Drop header/basis cells, not just legend rows: an ICRA table's first column
            # carries "Standalone", "FY2024" and similar, which are not metrics.
            junk = (r"^(A|UA)\s*:|^Note\b|^Particular|^(Standalone|Consolidated)\b"
                    r"|^(FY\s?)?(19|20)\d{2}\b|^(Q[1-4]|H[12])\b|^\W*$")
            if lab and not re.match(junk, lab, re.I):
                out.append(lab)
    return out[:12]


def word_search(directory: Path, term: str):
    """Word-boundary filename search - substring matching gave 'Indus' -> 'Industries'."""
    if not directory.is_dir():
        return []
    pat = re.compile(r"(?<![a-z0-9])" + re.escape(term.lower()) + r"(?![a-z0-9])")
    return [p.name for p in directory.iterdir()
            if p.is_file() and pat.search(re.sub(r"[_\-]+", " ", p.name.lower()))]


def main(slug):
    case = ROOT / "Companies" / slug
    if not case.is_dir():
        print(f"No such case: {case}")
        return 2
    import json
    meta = json.loads((case / "case.json").read_text(encoding="utf-8"))
    name, agency = meta.get("name", slug), meta.get("agency", "ICRA")
    docs = sorted((case / "documents").rglob("*.md"))
    blob = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in docs)

    print("=" * 78)
    print(f"PRE-FLIGHT  |  {name}  |  agency {agency}  |  {len(docs)} documents, {len(blob.split()):,} words")
    print("=" * 78)

    # ---- 0. DOCUMENTS BY DATE, NEWEST FIRST  (failure mode 26) -----------------------------
    # A stale figure taken from an annual report while a newer filing sat in the same folder
    # caused NABARD's shareholding to be reported as 87.77% when the FY2026 financials said
    # 89.12% (NABKISAN, 19-Aug-2026). Read the newest first; justify any older figure.
    print("\n[0] DOCUMENTS BY DATE - READ THE NEWEST FIRST  (failure mode 26)")
    dated = []
    for d in docs:
        best = 0
        # Require the year NOT to sit inside a longer digit run - upload filenames carry
        # timestamps like "202510141646212034654", from which a naive scan read "2034".
        for m in re.finditer(r"(?<!\d)(20\d{2})(?!\d)", d.name):
            v = int(m.group(1))
            if 2015 <= v <= 2035:
                best = max(best, v)
        dated.append((best, d))
    for yr, d in sorted(dated, key=lambda x: x[0], reverse=True)[:8]:
        tag = f"~{yr}" if yr else " ?  "
        print(f"      {tag}  {d.name[:66]}")
    newest = max((y for y, _ in dated), default=0)
    if newest:
        print(f"    *** Newest content appears to be {newest}. Any figure taken from an older")
        print(f"        document than this must be justified in the workpaper. ***")

    # ---- 0b. SAME METRIC, DIFFERENT DOCUMENTS  (failure mode 30) ---------------------------
    # Reading [0] is not enough. A metric can be extracted from whichever document happens to
    # match the search string, with no check on WHICH YEAR it belongs to. On HDFC Securities
    # (20-Aug-2026) that produced three errors at once: average daily turnover quoted from the
    # FY2025 report, client count from the FY2024 report, and a branch network reported as
    # GROWING 128 -> 134 when the true series was 184 -> 134 -> 128, a 30% contraction. The
    # rationale's whole industry narrative was wrong as a result.
    # So: extract each operating metric from EVERY document and show the series. Whenever one
    # pattern yields different values in different files, the analyst must attribute by year.
    print("\n[0b] OPERATING METRICS ACROSS DOCUMENTS - ATTRIBUTE EACH TO ITS YEAR"
          "  (failure mode 30)")
    metric_pats = {
        "branches":        r"(\d[\d,]*)\s+branch(?:es)?\b",
        "cities/towns":    r"(\d[\d,]*)\s+(?:cities|towns)\b",
        "clients/customers": r"([\d.]+)\s*(?:million|lakh|crore)\+?\s+(?:\w+\s+){0,2}"
                             r"(?:clients?|customers?)\b",
        "turnover risen %": r"turnover has risen\W{0,4}(\d[\d.]*)\s*%",
        "capacity util. %": r"capacity utili[sz]ation\D{0,24}(\d[\d.]*)\s*%",
        "stations":        r"(\d[\d,]*)\s+(?:CNG\s+)?stations\b",
    }
    year_of = {d.name: y for y, d in dated}
    flagged = 0
    for label, pat in metric_pats.items():
        rx = re.compile(pat, re.I)
        per_doc = {}
        for d in docs:
            vals = {m.group(1) for m in rx.finditer(
                d.read_text(encoding="utf-8", errors="replace"))}
            if vals:
                per_doc[d.name] = sorted(vals)
        if not per_doc:
            continue
        distinct = {v for vs in per_doc.values() for v in vs}
        multi = len(per_doc) > 1 and len(distinct) > 1
        # A metric found ONLY in an older document is the subtler trap: nothing conflicts with
        # it, so it reads as current. "Average daily turnover has risen 34%" appeared only in
        # the FY2025 report and was quoted as an FY2026 figure (HDFC Securities, 20-Aug-2026).
        stale = (not multi and newest
                 and max((year_of.get(f, 0) for f in per_doc), default=0) < newest)
        flagged += multi or stale
        print(f"    {'!! ' if (multi or stale) else '   '}{label}:")
        for fn in sorted(per_doc, key=lambda f: year_of.get(f, 0), reverse=True):
            yr = year_of.get(fn) or "?"
            print(f"         ~{yr}  {', '.join(per_doc[fn])[:40]:<40} {fn[:44]}")
        if multi:
            print(f"         ^^ SAME METRIC, DIFFERENT VALUES across documents. Quote the value"
                  f" from the")
            print(f"            NEWEST document, and state the SERIES if it moves - the"
                  f" direction is the finding.")
        elif stale:
            print(f"         ^^ FOUND ONLY IN AN OLDER DOCUMENT (newest content is ~{newest})."
                  f" Nothing")
            print(f"            contradicts it, so it reads as current - it is NOT. Either date"
                  f" it explicitly")
            print(f"            in the rationale or re-search the newest document for its own"
                  f" figure.")
    if not flagged:
        print("    no metric appears with conflicting values across documents")

    # ---- 0c. AGGREGATE-NOTE CONTAMINANTS  (failure mode 36) --------------------------------
    # Balkrishna Industries, 25-Aug-2026. "Other Expenses" was extracted as a single subtotal
    # (Rs 2,699.31 cr) and fed straight into OPBDITA. Inside that note, as one line, sat "Net
    # Loss on foreign currency transaction and translation | 290.01 | -" - nil the prior year.
    # The published OPBDITA margin came out 21.25% against ICRA's actual 24.3%, and the whole
    # rationale was built on a "tariff-driven margin compression" that had not happened. The
    # rating shipped ONE NOTCH LOW as a direct result.
    #
    # The subtotal is not wrong and its caption is not misleading - it is a COMPOSITE, and a
    # composite cannot be used as a ratio input until its components have been seen. Nothing in
    # the report looked wrong, which is exactly why prose could not catch it: the draft even
    # asserted "excludes ... any exceptional item - none disclosed in any year", an absence
    # claim that was false because a forex loss is not captioned "exceptional".
    print("\n[0c] AGGREGATE-NOTE CONTAMINANTS - DECOMPOSE BEFORE USING A SUBTOTAL"
          "  (failure mode 36)")
    # Items that routinely hide inside Other Expenses / Other Income and that must be
    # consciously INCLUDED or EXCLUDED before any operating-profit measure is published.
    # Each pattern requires the label to have P&L-ITEM shape - a gain/loss/expense/income word -
    # not merely to mention the topic. Without that, "Foreign currency risk" (a risk-disclosure
    # note heading) and "Foreign exchange forward contract" (a hedging table) both matched, and
    # a probe that cries wolf trains the reader to ignore it - the precise failure recorded in
    # check_sections.py's own calibration history.
    contaminants = [
        ("forex loss/gain",      r"(?:foreign (?:currency|exchange)|forex)[^|]{0,40}"
                                 r"(?:loss|gain|difference)|(?:loss|gain)[^|]{0,30}"
                                 r"(?:foreign (?:currency|exchange)|forex)"),
        ("exceptional item",     r"exceptional (?:item|income|expense|loss|gain)"),
        ("one-off / non-recurring", r"one[- ]time|one[- ]off|non[- ]recurring|prior period"),
        ("profit/loss on asset sale", r"(?:profit|loss|gain)[^|]{0,24}(?:on )?(?:sale|disposal)"
                                      r"[^|]{0,24}(?:asset|property|plant|equipment|investment)"),
        ("impairment / write-off", r"impairment (?:loss|charge|of)|written? off|write[- ]back|"
                                   r"written back"),
        ("provision written back", r"provision[^|]{0,30}(?:no longer required|written back|"
                                   r"reversal|reversed)"),
        ("interest inside opex", r"^interest (?:to|on) others?\b"),
        ("interest / dividend income", r"interest income|dividend income"),
        ("fair-value change",    r"fair value change|mark[- ]to[- ]market|"
                                 r"net (?:gain|loss) on fair"),
        ("insurance claim",      r"insurance claim"),
        ("govt grant / incentive", r"government grant|export incentive|subsidy|duty drawback"),
    ]
    # Subtotal captions are not components - "V. Profit before exceptional items (III-IV)" is a
    # derived line, not something hiding inside a note.
    SUBTOTAL_RE = re.compile(r"^(?:[IVX]+\s*[.)]|\(?[a-z]\)?\s*[.)]\s*)?\s*"
                             r"(?:total\b|profit (?:before|after|for)\b|"
                             r"(?:sub)?total\b)|\([IVX]+\s*[-+]\s*[IVX]+\)", re.I)
    found_any = 0
    for label, pat in contaminants:
        rx = re.compile(pat, re.I)
        hits = []
        for d in docs:
            for line in d.read_text(encoding="utf-8", errors="replace").splitlines():
                s = line.strip()
                if not s.startswith("|"):
                    continue
                cells = [c.strip() for c in s.strip("|").split("|")]
                if len(cells) < 2:
                    continue
                lab = re.sub(r"[*_`]|<br>", " ", cells[0]).strip()
                if not lab or not rx.search(lab) or SUBTOTAL_RE.search(lab):
                    continue
                # first cell after the label that parses as a real amount
                for c in cells[1:]:
                    m = re.fullmatch(r"\(?\s*([\d,]+\.\d{1,2})\s*\)?", c.replace("`H`", "")
                                     .replace("Rs.", "").replace("₹", "").strip())
                    if m:
                        hits.append((float(m.group(1).replace(",", "")), lab[:52], d.name))
                        break
        if not hits:
            continue
        found_any += 1
        seen, uniq = set(), []
        for amt, lab, fn in sorted(hits, key=lambda x: -x[0]):
            key = (round(amt, 2), lab.lower())
            if key not in seen:
                seen.add(key)
                uniq.append((amt, lab, fn))
        print(f"    !! {label}:")
        for amt, lab, fn in uniq[:4]:
            print(f"         {amt:>12,.2f}   {lab:<52} {fn[:34]}")
    if found_any:
        print("    ^^ BINDING: each line above is a COMPONENT of an aggregate note. Before any")
        print("       operating-profit measure (OPBDIT/OPBDITA/PBILDT/EBITDA) is published, each")
        print("       must carry a WRITTEN include-or-exclude decision in the workpaper's")
        print("       normalisation note. A subtotal may NOT be fed into a ratio until its")
        print("       components have been read. 'No exceptional item was disclosed' is an")
        print("       ABSENCE CLAIM about these documents (failure mode 20) - a forex loss is")
        print("       not captioned 'exceptional', so that sentence does not cover it.")
    else:
        print("    none found - absence is EVIDENCED by this run, safe to state")

    # ---- 0d. SAME ITEM, TWO STATEMENTS  (failure mode 38) ---------------------------------
    # Jindal Stainless, 26-Aug-2026. The engine carried a forex figure of -70.04 (FY2025) and
    # +87.15 (FY2026). Those are the "Net unrealised foreign exchange (gain)/loss" rows from
    # the CASH-FLOW RECONCILIATION. The P&L line, in the Other Expenses NOTE, is a net GAIN of
    # 154.37 and 78.41. FY2026 went in as a LOSS against an audited GAIN - wrong in magnitude
    # AND in sign - and survived three rounds of checking because probe [0c] had done its job
    # (the item WAS decomposed and named) and every tie-out still passed.
    #
    # The two figures are both real, both correctly transcribed, and both describe forex. They
    # are simply DIFFERENT MEASURES: the cash-flow row is the non-cash adjustment needed to get
    # from PBT to operating cash flow - the unrealised slice only - while the note states what
    # the P&L actually booked. Only the note is a P&L line.
    print("\n[0d] SAME ITEM IN TWO STATEMENTS - CASH-FLOW ROW vs P&L NOTE"
          "  (failure mode 38)")
    cf_markers = re.compile(r"unrealised|unrealized|adjustment[s]? for|non[- ]cash", re.I)
    pairs = [
        ("foreign exchange / forex",
         re.compile(r"(?:foreign (?:currency|exchange)|forex)[^|]{0,44}"
                    r"(?:gain|loss|difference)|(?:gain|loss)[^|]{0,30}"
                    r"(?:foreign (?:currency|exchange)|forex)", re.I)),
        ("profit/loss on sale of assets",
         re.compile(r"(?:profit|loss|gain)[^|]{0,24}(?:on )?(?:sale|disposal)"
                    r"[^|]{0,24}(?:asset|property|plant|equipment|investment)", re.I)),
        ("impairment / write-off",
         re.compile(r"impairment (?:loss|charge|of)|written? off|write[- ]back", re.I)),
    ]
    flagged = 0
    for label, pat in pairs:
        buckets = {}
        for d in docs:
            text = d.read_text(encoding="utf-8", errors="replace")
            for line in text.splitlines():
                if not line.strip().startswith("|") or not pat.search(line):
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if not cells:
                    continue
                lab = cells[0]
                amounts = []
                for c in cells[1:]:
                    m = re.fullmatch(r"\(?\s*-?([\d,]+\.\d{1,2})\s*\)?", c
                                     .replace("`H`", "").replace("Rs.", "")
                                     .replace("\u20b9", "").strip())
                    if m:
                        amounts.append(round(float(m.group(1).replace(",", "")), 2))
                if not amounts:
                    continue
                where = "cash-flow" if cf_markers.search(lab) else "note/P&L"
                buckets.setdefault(where, []).append((lab[:46], amounts[:2], d.name[:26]))
        if len(buckets) < 2:
            continue
        # The same economic item appears in BOTH a cash-flow-shaped row and a note row.
        cf_vals = {a for _, amts, _ in buckets.get("cash-flow", []) for a in amts}
        note_vals = {a for _, amts, _ in buckets.get("note/P&L", []) for a in amts}
        if cf_vals and note_vals and not (cf_vals & note_vals):
            flagged += 1
            print(f"    !! {label}: the cash-flow row and the note row DISAGREE")
            for where in ("cash-flow", "note/P&L"):
                for lab, amts, fn in buckets.get(where, [])[:3]:
                    shown = ", ".join(f"{a:,.2f}" for a in amts)
                    print(f"         {where:<10} {lab:<46} {shown:<22} {fn}")
    if flagged:
        print("    ^^ BINDING: these are DIFFERENT MEASURES of the same item, not a discrepancy")
        print("       to reconcile. Only the NOTE states what the profit-and-loss account")
        print("       booked; the cash-flow row is the unrealised / non-cash adjustment. Any")
        print("       figure feeding an operating-profit measure must be taken from the NOTE,")
        print("       and the note's components must be TIED to the note's own printed total -")
        print("       decomposing without tying is what let this error survive (failure mode 39).")
    else:
        print("    no cash-flow-vs-note conflict detected in the parsed tables")

    # ---------------------------------------------------------------- [0e] balance-sheet aggregates
    print("\n[0e] BALANCE-SHEET AGGREGATES - DECOMPOSE BEFORE USING A CAPTION")
    print("     Probe [0c] decomposes P&L notes. Nothing decomposed the BALANCE SHEET, and")
    print("     that is how Dhampur Bio Organics reported current borrowings of Rs 847.19")
    print("     crore as if it were all working capital, when Rs 82.68 crore of it was")
    print("     CURRENT MATURITIES OF LONG-TERM DEBT. Both numbers were in the extraction;")
    print("     neither was split. Long-term debt was understated by the same Rs 82.68 crore")
    print("     (206.98 reported against the agency's 290), and the working-capital number")
    print("     was overstated by it. Two different credit stories, one undecomposed caption.")
    bs_pats = [
        ("current maturities inside CURRENT borrowings",
         re.compile(r"current maturit\w*[^|]{0,40}(long[- ]term|borrowing|debt)", re.I)),
        ("acceptances / bill discounting inside borrowings or payables",
         re.compile(r"acceptance|bills? discount|channel financ|supplier financ", re.I)),
        ("earmarked / margin / restricted balances inside CASH",
         re.compile(r"(margin money|earmark\w*|restricted|unpaid dividend|unclaimed|"
                    r"held as security|lien)[^|]{0,30}", re.I)),
        ("lease liabilities shown apart from borrowings",
         re.compile(r"lease liabilit", re.I)),
    ]
    hits = 0
    for label, pat in bs_pats:
        rows = []
        for d in docs:
            for line in d.read_text(encoding="utf-8", errors="replace").splitlines():
                if not line.strip().startswith("|") or not pat.search(line):
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if not cells:
                    continue
                amts = []
                for c in cells[1:]:
                    m = re.fullmatch(r"\(?\s*-?([\d,]+\.\d{1,2})\s*\)?", c
                                     .replace("`H`", "").replace("Rs.", "")
                                     .replace("₹", "").strip())
                    if m:
                        amts.append(round(float(m.group(1).replace(",", "")), 2))
                if amts:
                    rows.append((cells[0][:50], amts[:3], d.name[:26]))
        if not rows:
            continue
        hits += 1
        print(f"    !! {label}:")
        seen = set()
        for lab, amts, fn in rows:
            key = (lab, tuple(amts))
            if key in seen:
                continue
            seen.add(key)
            shown = ", ".join(f"{a:,.2f}" for a in amts)
            print(f"         {shown:<30} {lab:<50} {fn}")
            if len(seen) >= 4:
                break
    if hits:
        print("    ^^ BINDING: each line above sits INSIDE a balance-sheet caption that a ratio")
        print("       will use. Before publishing overall gearing, working-capital dependence,")
        print("       long-term debt or a liquidity figure, SPLIT the caption and state the")
        print("       split. A caption is not a ratio input until its components have been read")
        print("       - the same rule failure mode 36 applies to the P&L, applied to the")
        print("       balance sheet, where it had no probe at all.")
    else:
        print("    no decomposable balance-sheet caption detected in the parsed tables")

    # ---------------------------------------------------------------- [0f] promoter unsecured loans
    # CRISIL runs a four-factor test (subordination, retention track record, interest rate vs
    # market, deferability/plough-back) to classify a promoter/family unsecured loan as full
    # debt, full equity, or a stated ~75% equity / 25% debt split - see failure mode 48 and
    # CRISIL_CONVENTIONS.md S3 Box 1. No equivalent test exists anywhere in this project's
    # tooling, so a material promoter unsecured-loan balance on a CRISIL case has previously
    # just defaulted to being counted as debt with no test ever run. This probe cannot RUN the
    # test - that requires the loan agreement's actual terms - it can only make sure the
    # analyst cannot miss that the test is due.
    print("\n[0f] PROMOTER / RELATED-PARTY UNSECURED LOANS  (failure mode 48, CRISIL only)")
    if agency != "CRISIL":
        print(f"     n/a - CRISIL's four-factor test does not apply to a {agency} case")
    else:
        pul_pat = re.compile(
            r"unsecured\b[^|]{0,60}(?:promoter|director|related part)"
            r"|(?:promoter|director|related part)[^|]{0,60}unsecured\b", re.I)
        hits = []
        for d in docs:
            for line in d.read_text(encoding="utf-8", errors="replace").splitlines():
                if not line.strip().startswith("|") or not pul_pat.search(line):
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                amts = []
                for c in cells[1:]:
                    m = re.fullmatch(r"\(?\s*-?([\d,]+\.\d{1,2})\s*\)?",
                                     c.replace("₹", "").replace("Rs.", "").strip())
                    if m:
                        amts.append(round(float(m.group(1).replace(",", "")), 2))
                if amts and max(amts) > 0:
                    hits.append((cells[0][:60], amts[:3], d.name[:30]))
        if not hits:
            print("     no promoter/related-party unsecured loan line found in the parsed tables")
        else:
            print("    !! promoter/related-party unsecured loan balance(s) found:")
            seen = set()
            for lab, amts, fn in hits:
                key = (lab, tuple(amts))
                if key in seen:
                    continue
                seen.add(key)
                shown = ", ".join(f"{a:,.2f}" for a in amts)
                print(f"         {shown:<30} {lab:<60} {fn}")
            print("    ^^ BINDING (CRISIL_CONVENTIONS.md S3 Box 1): before defaulting this to")
            print("       debt, run CRISIL's four-factor test in the workpaper - subordination")
            print("       to external borrowings, track record of retention, interest rate vs")
            print("       market, and deferability/plough-back in distress. CRISIL's own stated")
            print("       split for equity-like treatment is ~75% equity / 25% debt, not 50/50.")

    # ---- 1. prior rating action (Step 14) -------------------------------------------------
    print("\n[1] PRIOR RATING ACTION IN THE REFERENCE LIBRARY  (Step 14 / failure mode 24)")
    # Prefer the specific (non-generic) tokens - "Industries"/"Limited" alone false-positive-match
    # half the reference library (e.g. "Yasho Industries" -> "Aarti Industries", "Britannia
    # Industries" ...). Fall back to generic tokens only if nothing specific exists in the name.
    # >=3 not >3: "SBI" is 3 characters and previously produced ZERO tokens, after which the
    # script printed "'no prior action' is EVIDENCED" having searched for nothing at all - the
    # exact false-absence claim this file exists to prevent. Never conclude from an empty search.
    all_tokens = [t for t in re.split(r"[^A-Za-z]+", name) if len(t) >= 3]
    tokens = [t for t in all_tokens if t.lower() not in GENERIC_TOKENS][:2] or all_tokens[:2]
    # An acronym case name ("SBI") will not match a library filed under the expanded legal name
    # ("State Bank of India"), so recover the legal name the documents themselves use.
    if all(len(t) <= 4 for t in tokens):
        from collections import Counter
        # Require >=3 words: "The Bank" is the most frequent match in a bank's own AR but
        # carries no identifying information; "State Bank of India" does.
        cand = Counter(m.group(1).strip() for m in LEGAL_NAME_RE.finditer(blob)
                       if len(m.group(1).split()) >= 3
                       and not m.group(1).lower().startswith("the "))
        for legal, _ in cand.most_common(3):
            extra = [t for t in re.split(r"[^A-Za-z]+", legal)
                     if len(t) >= 3 and t.lower() not in GENERIC_TOKENS]
            if extra:
                tokens += extra[:2]
                print(f"    (acronym case name - also searching legal name seen in documents:"
                      f" {legal!r})")
                break
    # A RENAMED company will never match its own prior rationale by current name:
    # "Gujarat Energy Limited" cannot find "Gujarat Gas Limited". Search former names and
    # aliases too - case.json records them. (failure mode 29, 20-Aug-2026.)
    STOP = {"renamed", "under", "the", "and", "with", "effective", "scheme", "composite",
            "arrangement", "unchanged", "formerly", "known", "was", "from", "into", "per",
            "may", "jan", "feb", "mar", "apr", "jun", "jul", "aug", "sep", "oct", "nov", "dec",
            "cin", "order", "dated", "pursuant", "merger", "amalgamation", "erstwhile"}
    for extra in ([meta.get("former_name", "")] + list(meta.get("aliases", []))):
        # Only the leading proper-noun run - a former_name field often carries a whole
        # explanatory sentence, and tokenising all of it floods the search with noise.
        lead = re.split(r"[(\-—,;.]", str(extra))[0]
        for tk in re.split(r"[^A-Za-z]+", lead)[:4]:
            if len(tk) >= 3 and tk.lower() not in GENERIC_TOKENS and tk.lower() not in STOP:
                tokens.append(tk)
    tokens = list(dict.fromkeys(tokens))
    if len(tokens) > 2:
        print(f"    (searching on {tokens} - includes former name / aliases)")
    found = []
    for ag, d in AGENCY_DIRS.items():
        for tok in tokens:
            for f in word_search(d, tok):
                found.append(f"{ag}: {f}")
    # Rank by how MANY of the issuer's name tokens the filename carries, not alphabetically.
    # "Gujarat Energy Limited" matched a dozen generic *Energy* companies; the real anchor
    # ("Gujarat Gas Limited") sorted below an [:8] cut and never appeared - which is how the
    # Rs 2,900 crore rated amount stayed invisible (failure mode 29, 20-Aug-2026).
    def _score(entry):
        fn = re.sub(r"[_\-]+", " ", entry.split(": ", 1)[1].lower())
        return sum(1 for tk in tokens
                   if re.search(r"(?<![a-z0-9])" + re.escape(tk.lower()) + r"(?![a-z0-9])", fn))
    found = sorted(set(found), key=lambda e: (-_score(e), e))
    if found:
        print("    *** PRESENT - Step 14 IS APPLICABLE. Open these AFTER forming your view, and")
        print("        produce a divergence table. You may NOT write 'no prior rating action'. ***")
        for f in found[:8]:
            print(f"      - {f}")

        # ---- RATED AMOUNTS, extracted here and now  (failure mode 29) ----------------------
        # Deferring the rated-amount table to "Step 14, after forming my view" caused three
        # reports to ship "to be confirmed by issuer" against a number sitting in the library
        # (Riba, NABKISAN, Gujarat Energy). Step 14 defers the RATING CONCLUSION, never the
        # FACILITY SCHEDULE - reading an amount cannot contaminate an independent credit view.
        # So the amounts are printed in the pre-flight itself, where they cannot be overlooked.
        # A rated-amount row ALWAYS carries a rating string in the same row. Requiring one
        # filters out Brief Financials / ratio tables, which also hold decimal amounts and
        # otherwise flooded this probe with irrelevant rows.
        amt_re = re.compile(r"[\d,]+\.\d{2}")
        rating_re = re.compile(
            r"(CARE|CRISIL|\[ICRA\]|ICRA|IND)\s*-?\s*(AAA|AA|A1|A2|A3|A4|BBB|BB|B|C|D)", re.I)
        printed = False
        for entry in found[:8]:
            ag, fname = entry.split(": ", 1)
            d = AGENCY_DIRS.get(ag)
            if not d:
                continue
            fp = d / fname
            if not fp.is_file():
                continue
            head = fp.read_text(encoding="utf-8", errors="replace")[:6000]
            rows = [ln.strip() for ln in head.splitlines()
                    if ln.startswith("|") and amt_re.search(ln) and rating_re.search(ln)
                    and "---" not in ln]
            if rows:
                if not printed:
                    print("\n    >>> RATED AMOUNTS FOUND IN THE LIBRARY <<<")
                    print("      Failure mode 29: never write 'to be confirmed by issuer' while a")
                    print("      SAME-ISSUER line exists. Condition (1) is MET - the library counts.")
                    print("      !! CONFIRM THE ENTITY FIRST. A PARENT, SIBLING OR PEER IS NOT THE")
                    print("         ISSUER - importing a peer's rated amount is a WORSE error than")
                    print("         leaving it TBC. [match n/m] = how many of the issuer's name")
                    print("         tokens the filename carries. Highest score is the candidate;")
                    print("         it still needs your confirmation that it is the same company.")
                    printed = True
                print(f"      from {fname[:56]}  [match {_score(entry)}/{len(tokens)}]")
                for r_ in rows[:6]:
                    clean = re.sub(r"<[^>]+>", " ", r_)
                    clean = re.sub(r"\s+", " ", clean).strip()
                    print(f"        {clean[:104]}")
    elif not tokens:
        print("    !!! INCONCLUSIVE - no usable search token could be derived from the case name.")
        print("        NOTHING WAS SEARCHED. You may NOT write 'no prior rating action'.")
        print("        Search the reference library MANUALLY by the issuer's full legal name.")
    else:
        print(f"    none found (word-boundary search on {tokens}) -> 'no prior action' is EVIDENCED")

    # ---- 1b. PEER REPORTS - SAME AGENCY, SAME SECTOR  (failure modes 32/33) ----------------
    # THE HDFC SECURITIES LESSON. That report invented its own ratio definitions and omitted
    # cost-to-income and ROTA on a misapplied sector rule - while TWO CareEdge broking
    # rationales published six weeks earlier (Angel One 03-Jul-2026, Anand Rathi 06-Jul-2026)
    # sat unopened in this very library, each carrying the exact Brief Financials row set and
    # the "*including non-fund-based limits utilised" gearing footnote.
    # AGENCIES.md item 3 already said "learn the format from the agency's own reference
    # reports" - prose that did not fire. So the peers are now surfaced automatically, WITH
    # their row set, before any drafting happens.
    print(f"\n[1b] PEER REPORTS - {agency.upper()}, SAME SECTOR  (failure modes 32/33)")
    sector = str(meta.get("sector", "")).lower()
    stop = {"and", "the", "of", "for", "limited", "company", "companies", "sector",
            "services", "service", "india", "indian", "other", "general"}
    sec_tokens = [w for w in re.findall(r"[a-z]{3,}", sector) if w not in stop]
    # Use the AGENCY_DIRS map, not a constructed path: ICRA's library sits at the ROOT, not
    # under an "ICRA/" folder, so building the path by hand silently found nothing for every
    # ICRA case while appearing to work for CRISIL and CareEdge.
    ref_dir = AGENCY_DIRS.get(agency, ROOT / agency / "Report for Reference")
    if not sec_tokens:
        print("    case.json has no usable 'sector' - cannot match peers. Set it, then re-run.")
    elif not ref_dir.is_dir():
        print(f"    no reference library at {ref_dir}")
    else:
        # Score with cheap IDF. A raw token count made "City Gas Distribution / integrated
        # energy" match an ASSET MANAGER first, because "distribution", "energy" and "state"
        # appear in a quarter of the library. A token carried by many reports identifies no
        # sector, so it earns no weight - the same lesson as GENERIC_TOKENS in the name search.
        heads = {}
        for p in ref_dir.glob("*.md"):
            try:
                heads[p] = p.read_text(encoding="utf-8", errors="replace")[:6000].lower()
            except OSError:
                continue
        import math
        n_docs = max(1, len(heads))
        df = {w: sum(1 for h in heads.values() if w in h) for w in sec_tokens}
        # IDF weight. A term in a quarter of the library identifies no sector; a rare one like
        # "broking" or "gas" all but names it. Raw counts ranked an ASSET MANAGER top for a city
        # gas case, because "scheme" and "distribution" appear there dozens of times in an
        # unrelated sense. Weighting by rarity fixes both directions at once.
        weight = {w: math.log(n_docs / max(1, df[w])) for w in sec_tokens}
        useful = [w for w in sec_tokens if weight[w] > 0.35]      # drops df > ~70% of library
        if not useful:
            useful = sorted(sec_tokens, key=lambda w: -weight[w])[:2]
            print(f"    (all sector tokens are common here; using the rarest: {useful})")
        dropped = [w for w in sec_tokens if w not in useful]
        if dropped:
            print(f"    ignoring generic sector tokens {dropped} - they identify no sector")
        # Score on DISTINCT tokens present, not total occurrences. Summing counts let a single
        # word dominate: an asset-manager report says "scheme" and "distribution" dozens of
        # times in a wholly different sense, and outranked every gas peer for a CGD case.
        scored = []
        for p, head in heads.items():
            present = [w for w in useful if w in head]
            if present:
                score = sum(weight[w] * min(3, head.count(w)) for w in present)
                scored.append((score, present, p))
        scored.sort(key=lambda t: (-t[0], t[2].name))
        scored = [(f"score {sc:.1f} on {'+'.join(pr[:3])}", p) for sc, pr, p in scored]
        if not scored:
            print(f"    no peer found for sector tokens {sec_tokens}")
        for hits, p in scored[:3]:
            print(f"    * {p.name[:70]}   ({hits})")
            t = p.read_text(encoding="utf-8", errors="replace")
            labels = _brief_financial_rows(t)
            if labels:
                print("        Brief Financials rows THIS AGENCY USES IN THIS SECTOR:")
                for lab in labels:
                    print(f"          - {lab[:64]}")
            for note in re.findall(r"\*\s*(includ\w+[^\n|]{0,70})", t, re.I)[:2]:
                print(f"        ratio footnote: *{note.strip()[:70]}")
        if scored:
            print("    *** These rows are the REQUIRED set, and the footnotes are the agency's")
            print("        RATIO DEFINITIONS. Reproduce them. A metric may be omitted only after")
            print("        checking a peer above - never by reasoning from another sector. ***")
            # SURFACING IS NOT VERIFYING. Printing the row set only helps if something later
            # checks that the delivered report actually carries it, so persist it for the
            # delivery gate. check_sections.py reads this file from the report's own folder.
            top = scored[0][1]
            rows = _brief_financial_rows(top.read_text(encoding="utf-8", errors="replace"))

            # DO THE TOP PEERS AGREE? Sector tokens are ambiguous: on an HFC case the word
            # "hfc" matched HFCL Limited (a telecom cable maker) and "housing finance" matched
            # a BANK, which outranked the correct HFC peer. When the top peers disagree on the
            # row set, the sector match is unreliable and the analyst must pick - so say so
            # loudly rather than let peer_rows.json enshrine the wrong one.
            sets = []
            for _, p in scored[:3]:
                r = _brief_financial_rows(p.read_text(encoding="utf-8", errors="replace"))
                if r:
                    sets.append((p.name, {x.lower().replace(" ", "") for x in r}))
            if len(sets) >= 2:
                base = sets[0][1]
                overlap = min(len(base & s) / max(1, len(base | s)) for _, s in sets[1:])
                if overlap < 0.5:
                    print("    !! TOP PEERS DISAGREE ON THE ROW SET - the sector match is")
                    print("       AMBIGUOUS. Confirm which peer is the same ENTITY TYPE before")
                    print("       relying on peer_rows.json, and overwrite it if the top hit is")
                    print("       the wrong kind of company.")

            # ---- PEER NORM: what does this agency normally RATE in this sector? -----------
            # The HSL error that no check caught was a REASONING failure: drawn debt was
            # allowed to define the rated universe, so an entire long-term rating and its
            # outlook vanished. No regex anticipates a bad inference - but the CONCLUSION was
            # contrary to the sector norm, and that is measurable. 9 of 15 CareEdge broking
            # peers carry a long-term rating. Stating that up front makes the deviation
            # visible before it is written, and the gate then demands a justification.
            norm = [p for _, p in scored[:20]]
            lt = st = 0
            for p in norm:
                h = heads[p][:3500]
                # heads[] is LOWERCASED for token matching, so this must be case-insensitive.
                # A case-sensitive pattern silently returned 0 of 14 against a true 9 of 15 -
                # and a check that always reads zero is worse than no check, because it looks
                # like evidence of conformity.
                lt += bool(re.search(r"(aaa|aa[+-]?|a[+-]?|bbb[+-]?)\s*;\s*"
                                     r"(stable|positive|negative)", h, re.I))
                st += bool(re.search(r"\ba1\+?\b|\ba2\+?\b", h))
            print(f"    PEER NORM over {len(norm)} peers: {lt} carry a LONG-TERM rating,"
                  f" {st} a short-term rating.")
            if lt > len(norm) / 2:
                print("        -> A long-term rating is NORMAL in this sector. If your report"
                      " assigns none,")
                print("           that is a DEVIATION and must be justified in writing -"
                      " never inferred")
                print("           from the absence of long-term DRAWN debt (failure mode 31).")
            if rows or norm:
                (case / "peer_rows.json").write_text(json.dumps(
                    {"agency": agency, "sector": sector, "peer": top.name,
                     "required_rows": rows,
                     "peers_sampled": len(norm), "peers_with_long_term_rating": lt,
                     "peers_with_short_term_rating": st}, indent=2), encoding="utf-8")
                print(f"    -> wrote peer_rows.json ({len(rows)} rows from {top.name[:40]};"
                      f" peer norm {lt}/{len(norm)} LT). check_sections.py VERIFIES both.")

    # ---- 1c. STEP 12 SHAPE - decided at the START, not remembered at the end (FM35) ---------
    # Batch processing silently dropped the forward view on every case delivered after
    # 14-Aug-2026. Naming the required artefact here, before any analysis, makes the choice
    # deliberate; check_sections.py then refuses delivery unless it was built or scoped.
    etype = str(meta.get("entity_type", "")).lower()
    sect = str(meta.get("sector", "")).lower()
    if any(k in etype or k in sect for k in ("nbfc", "hfc", "bank", "financial", "housing finance")):
        shape = ("LENDING model - book/AUM growth -> NII -> credit cost -> PAT, plus balance "
                 "sheet, Credit-Ratios and Debt-Breakup tabs. The corporate 3-statement "
                 "template does NOT fit a lender.")
    elif "public" in etype or "government" in sect:
        shape = "5-yr 3-statement model, or a focused sensitivity if this is stable IG surveillance."
    else:
        shape = "Full 5-yr 3-statement model (corporate with term debt)."
    print("\n[1c] STEP 12 - THE FORWARD VIEW IS NOT OPTIONAL  (failure mode 35)")
    print(f"    entity_type '{meta.get('entity_type','?')}' -> required artefact:")
    for line in [shape[i:i + 86] for i in range(0, len(shape), 86)]:
        print(f"      {line}")
    print("    PLUS Step 12b: fill Rating_Scorecard_<Company>.xlsx from AUDITED ACTUALS.")
    print("    If a lighter treatment is right, record WHY in case.json as")
    print("    'step12_scaling_decision' - the delivery gate refuses the case without one.")

    # ---- 2..n content probes ---------------------------------------------------------------
    for i, (label, pattern, why) in enumerate(PROBES, start=2):
        hits = len(re.findall(pattern, blob, re.I))
        state = "PRESENT" if hits else "absent"
        flag = "***" if hits else "   "
        print(f"\n[{i}] {label}")
        print(f"    {flag} {state} - {hits} match(es)")
        if hits:
            print(f"        {why}")
            for m in list(re.finditer(pattern, blob, re.I))[:2]:
                s = blob[max(0, m.start() - 55): m.end() + 55].replace("\n", " ")
                s = re.sub(r"\s+", " ", s).encode("ascii", "replace").decode("ascii")
                print(f"        e.g. ...{s.strip()[:110]}...")
        else:
            print(f"        absence is now EVIDENCED - safe to state, cite this run")

    # ---- sector KPI ------------------------------------------------------------------------
    print(f"\n[{len(PROBES)+2}] SECTOR-DEFINING METRIC  (failure mode 21)")
    low = blob.lower()
    # Rank by weight of evidence, not first match: in a 500k-word corpus almost every trigger
    # appears once somewhere (a stationery maker's AR mentions "mining"), so first-match picked
    # the wrong sector for 2 of 5 cases. Same bug class as check_sections.py's ITC-hotels miss.
    scored = sorted(((len(re.findall(trig, low)), trig, kpi, label) for trig, kpi, label in SECTOR_KPI),
                    reverse=True, key=lambda t: t[0])
    hits, _, kpi, label = scored[0]
    runner_up = scored[1]
    if hits < 5:
        print("    sector not auto-detected (no trigger above threshold) - name the defining"
              " metric manually before drafting")
    else:
        n = len(re.findall(kpi, low))
        print(f"    sector detected ({hits} trigger hits; next best '{runner_up[3]}' at"
              f" {runner_up[0]}) -> the rationale MUST quote: {label}")
        print(f"    {'*** PRESENT' if n else '    ABSENT'} in documents - {n} match(es)"
              f"{' -> EXTRACT IT' if n else ' -> confirm genuinely undisclosed'}")
        if runner_up[0] > hits * 0.5:
            print(f"    !! ambiguous - verify the sector manually before relying on this")

    # ---- methodology table integrity ---------------------------------------------------------
    # Failure mode 49. Step 3 reads the routed methodology and scores the issuer against its
    # indicative-band tables; a table whose data cells were lost in PDF-to-markdown conversion
    # still LOOKS present (header row, row labels, pipe structure intact) and would be read as
    # authoritative. That has to be known BEFORE the methodology is relied on, not after - which
    # is why the scan lives at the entry gate rather than the delivery gate.
    print(f"\n[{len(PROBES)+3}] METHODOLOGY TABLE INTEGRITY  (failure mode 49)")
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from corpus_table_integrity import AGENCY_METHODOLOGY_DIRS, scan_dir
        corrupt = [x for d in AGENCY_METHODOLOGY_DIRS for x in scan_dir(d)]
        if not corrupt:
            print("    no corrupted methodology tables detected across the three corpora")
        for f, heading, lbl, n in corrupt:
            print(f"    !! CORRUPTED  {f.name}")
            print(f"       section {heading!r}, {n} labelled row(s) with every data cell blank")
            print(f"       -> do NOT quote a threshold from this table; re-extract from a clean PDF")
    except Exception as e:                                                     # noqa: BLE001
        print(f"    scan unavailable ({e}) - run tools/corpus_table_integrity.py separately")

    print("\n" + "=" * 78)
    print("Paste this into the workpaper Read Log. Anything marked PRESENT may NEVER be described")
    print("as 'not available' later without a second recorded search contradicting this one.")
    print("=" * 78)
    return 0


def selftest():
    """The substring-matching bug shipped twice (webapp + here). Guard it."""
    pat = lambda term, fn: re.compile(  # noqa: E731
        r"(?<![a-z0-9])" + re.escape(term.lower()) + r"(?![a-z0-9])"
    ).search(re.sub(r"[_\-]+", " ", fn.lower())) is not None
    cases = [
        ("Indus", "Indus Towers Limited_18 Jul 2025_RR.md", True),
        ("Indus", "DOMS Industries Ltd_RR.md", False),      # 'Industries' must NOT match
        ("Towers", "Indus-Towers-AR-2026.md", True),        # hyphens normalise
        ("ITC", "ITC Limited_RR.md", True),
        ("IT", "ITC Limited_RR.md", False),                 # acronym must not prefix-match
        ("Vedanta", "Vedanta_Ltd_2025.md", True),
        ("Zinc", "Hindustan Zinc Limited.md", True),
    ]
    for term, fn, want in cases:
        assert pat(term, fn) is want, f"word_search({term!r}, {fn!r}) != {want}"

    # Regression (SBI, 14-Aug-2026): a short/acronym case name must still yield a search token.
    # It previously yielded NONE, and the empty search was printed as evidenced absence while a
    # CRISIL rationale for the issuer sat in the library.
    for nm in ("SBI", "ITC", "Yasho Industries", "Vedanta"):
        toks = [t for t in re.split(r"[^A-Za-z]+", nm) if len(t) >= 3]
        assert toks, f"no search token derived from {nm!r} - empty search reported as absence"

    print(f"selftest ok - {len(cases)} word-boundary cases + 4 token-derivation cases")
    return 0


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    sys.exit(selftest() if arg == "--selftest" else main(arg))
