"""Mine the CareEdge reference corpus into a structured dataset.

Reads EVERY report in CareEdge/Report for Reference and extracts the facts that
can be compared across reports: rating, rated amounts, Brief Financials rows,
liquidity descriptor, analytical approach, industry classification, section set.

Written 2026-09-13 after the Cochin Minerals two-notch miss. The point is that
805 reports cannot be read as prose without glancing; parsed, they answer
questions prose reading cannot -- e.g. what gearing CareEdge actually publishes
for a BBB manufacturer -- which is the calibration that was missing.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(ROOT, "CareEdge", "Report for Reference")

# CareEdge long-term scale, strongest first, with a numeric index.
LT_SCALE = ["AAA", "AA+", "AA", "AA-", "A+", "A", "A-", "BBB+", "BBB", "BBB-",
            "BB+", "BB", "BB-", "B+", "B", "B-", "C+", "C", "C-", "D"]
ST_SCALE = ["A1+", "A1", "A2+", "A2", "A3+", "A3", "A4+", "A4", "D"]
LT_IDX = {g: i for i, g in enumerate(LT_SCALE)}
ST_IDX = {g: i for i, g in enumerate(ST_SCALE)}

# "CARE BBB+; Stable" / "CARE AA-" / "CARE A1+".  The negative lookahead stops
# a bare "A" swallowing the "A" of "A1+" and stops "AA" matching inside "AAA".
LT_RE = re.compile(r"CARE\s+(AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?|C|D)(?![A-Z0-9+])")
ST_RE = re.compile(r"CARE\s+(A1\+|A1|A2\+|A2|A3\+|A3|A4\+|A4)(?![0-9+])")
OUTLOOK_RE = re.compile(
    r"CARE\s+(?:AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?)\s*;\s*(Stable|Positive|Negative)", re.I)


def _f(tok):
    """Parse a table cell into a float; return None when it is not a number."""
    if tok is None:
        return None
    t = tok.strip().replace(",", "").replace("₹", "").replace("%", "")
    neg = t.startswith("(") and t.endswith(")")
    t = t.strip("()").strip()
    if not re.fullmatch(r"-?\d+\.?\d*", t or ""):
        return None
    v = float(t)
    return -v if neg else v


def cells(line):
    """Split a markdown table row into cells, preserving empty ones."""
    if "|" not in line:
        return []
    return [c.strip() for c in line.strip().strip("|").split("|")]


# Brief Financials row labels -> canonical key, matched on a normalised label.
BF_ROWS = [
    ("toi",        r"total operating income|total income from operations"),
    ("pbildt",     r"^pbildt\b|^pbildt\*|profit before interest.*depreciation"),
    ("pat",        r"^pat\b|profit after tax"),
    ("gearing",    r"overall gearing"),
    ("intcov",     r"interest coverage"),
    ("pbildt_mgn", r"pbildt margin"),
    ("tdgca",      r"total debt.*gca|td/gca|total debt to gross cash"),
    ("networth",   r"tangible net worth|^net worth"),
]


def parse_brief_financials(text):
    """Pull the Brief Financials table. Returns ({row: [values]}, headers)."""
    m = re.search(r"Brief Financials.*?\n", text, re.I)
    if not m:
        return {}, []
    seg = text[m.start(): m.start() + 4000]
    out, headers = {}, []
    for ln in seg.splitlines():
        cs = cells(ln)
        if len(cs) < 2:
            continue
        label = re.sub(r"[*_`#]", "", cs[0]).strip().lower()
        if not headers and re.search(r"march|fy|20\d\d|q[1-4]", " ".join(cs), re.I):
            if not any(_f(c) is not None for c in cs[1:]):
                headers = cs[1:]
                continue
        for key, pat in BF_ROWS:
            if re.search(pat, label) and key not in out:
                vals = [_f(c) for c in cs[1:]]
                if any(v is not None for v in vals):
                    out[key] = vals
    return out, headers


def parse_rated_amounts(text):
    """Sum the amounts in the header facilities table (before Annexure-1)."""
    head = text[:6000]
    lt = st = 0.0
    for ln in head.splitlines():
        cs = cells(ln)
        if len(cs) < 3:
            continue
        label = cs[0].lower()
        amt = None
        for c in cs[1:]:
            v = _f(c)
            if v is not None:
                amt = v
                break
        if amt is None:
            continue
        row = " ".join(cs)
        if re.search(r"\btotal\b", label):
            continue
        if "long-term" in label or "long term" in label:
            lt += amt
        elif "short-term" in label or "short term" in label:
            st += amt
        elif ST_RE.search(row) and not LT_RE.search(row):
            st += amt
        elif LT_RE.search(row):
            lt += amt
    return round(lt, 2), round(st, 2)


SECTION_PATTERNS = {
    "rationale":     r"Rationale and key rating drivers",
    "sensitivities": r"Rating sensitivities",
    "analytical":    r"Analytical approach\s*:",
    "outlook":       r"^\s*Outlook\s*:",
    "strengths":     r"Key strengths",
    "weaknesses":    r"Key weaknesses",
    "industry":      r"Industry outlook",
    "liquidity":     r"Liquidity\s*:",
    "criteria":      r"Applicable criteria",
    "about":         r"About the company",
    "brief_fin":     r"Brief Financials",
    "noncoop":       r"Status of non-cooperation",
    "history":       r"Rating history",
    "annex1":        r"Annexure-1",
    "annex2":        r"Annexure-2",
    "esg":           r"ESG|Environment.{0,3}social",
}


def mine(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    base = os.path.basename(path)[:-3]
    issuer, _, date = base.rpartition("_")
    rec = {"file": base, "issuer": issuer.strip(), "date": date.strip(),
           "words": len(text.split())}

    # Ratings come ONLY from the facilities table rows, never from free text.
    #
    # An earlier version scanned the first 6,000 characters and reported Themis
    # Medicare as BBB when its header says BBB-; the "CARE BBB; Stable" it found
    # belonged to an ASSOCIATE company named in the Analytical approach
    # paragraph. That is failure mode 24 -- another entity's rating read as this
    # issuer's -- committed by the tool built to audit for it. Restricting the
    # scan to table rows carrying a facility label removes the whole class.
    head = text[:6000]
    rating_rows = []
    for ln in head.splitlines():
        cs = cells(ln)
        if len(cs) < 3:
            continue
        label = cs[0].lower()
        if not re.search(r"facilit|instrument|bank|term|debenture|paper|deposit|"
                         r"loan|ncd|cash credit|guarantee|letter of credit", label):
            continue
        if re.search(r"^\**\s*total\b", label):
            continue
        rating_rows.append(" ".join(cs))
    scan = "\n".join(rating_rows) if rating_rows else ""
    rec["rating_rows"] = len(rating_rows)
    lts = [g for g in LT_RE.findall(scan) if g in LT_IDX]
    sts = [g for g in ST_RE.findall(scan) if g in ST_IDX]
    # Most frequent grade across the facility rows, ties broken by first
    # appearance -- not the strongest, since a table may also print a previous
    # rating in a "Rating Action" cell.
    def modal(gs):
        return max(gs, key=lambda g: (gs.count(g), -gs.index(g))) if gs else None

    rec["lt"] = modal(lts)
    rec["st"] = modal(sts)
    rec["lt_idx"] = LT_IDX.get(rec["lt"])
    rec["st_idx"] = ST_IDX.get(rec["st"])
    mo = OUTLOOK_RE.search(scan)
    rec["outlook"] = mo.group(1).capitalize() if mo else None

    ma = re.search(r"Analytical approach\s*:?\s*\**\s*([A-Za-z ,/&()-]{3,80})", text)
    rec["approach"] = ma.group(1).strip().rstrip(".") if ma else None
    ml = re.search(r"Liquidity\s*:?\s*\**\s*(Superior|Strong|Adequate|Stretched|Poor)",
                   text, re.I)
    rec["liquidity"] = ml.group(1).capitalize() if ml else None

    rec["lt_amt"], rec["st_amt"] = parse_rated_amounts(text)
    bf, hdrs = parse_brief_financials(text)
    rec["bf"] = bf
    rec["bf_headers"] = hdrs
    rec["sections"] = sorted(k for k, p in SECTION_PATTERNS.items()
                             if re.search(p, text, re.I | re.M))
    mi = re.search(r"Basic industry(.{0,400})", text, re.S)
    rec["industry_block"] = " ".join(mi.group(1).split())[:200] if mi else None
    crit = re.search(r"Applicable criteria(.*?)(?:About the company|Industry classification)",
                     text, re.S)
    rec["criteria"] = ([c.strip() for c in crit.group(1).splitlines() if c.strip()][:15]
                       if crit else [])
    rec["is_suspended"] = bool(
        re.search(r"SUSPEND|Issuer Not Cooperating|ISSUER NOT COOPERATING", text, re.I))
    return rec


def main():
    files = sorted(f for f in os.listdir(LIB) if f.endswith(".md"))
    recs = []
    for f in files:
        try:
            recs.append(mine(os.path.join(LIB, f)))
        except Exception as e:
            recs.append({"file": f, "error": repr(e)})
    out = os.path.join(ROOT, "Docs", "careedge_corpus.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(recs, open(out, "w", encoding="utf-8"), indent=1)
    ok = [r for r in recs if not r.get("error")]
    print("parsed %d/%d reports -> %s" % (len(ok), len(files), out))
    print("  with a long-term grade : %d" % sum(1 for r in ok if r.get("lt")))
    print("  with Brief Financials  : %d" % sum(1 for r in ok if r.get("bf")))
    print("  with gearing published : %d" % sum(1 for r in ok if r.get("bf", {}).get("gearing")))
    print("  errors                 : %d" % sum(1 for r in recs if r.get("error")))


if __name__ == "__main__":
    main()
