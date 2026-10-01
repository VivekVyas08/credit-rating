# Credit Rating - Document Intake & Output Viewer
# Companion web view for the Credit Rating project.
# Cases live in <project root>/Companies/<slug>/ ; outputs (rationale/workpaper .md/.pdf)
# are auto-detected in the project root and the case folder.

import json
import re
import shutil
import sys
import threading
import unicodedata
import uuid
from datetime import datetime
from pathlib import Path

import markdown as md_lib
from flask import (Flask, abort, flash, jsonify, redirect,
                   render_template_string, request, send_file, url_for)
from markupsafe import escape as h
from werkzeug.utils import secure_filename

sys.path.insert(0, str(Path(__file__).resolve().parent))
import doc_convert                                                       # noqa: E402

ROOT = Path(__file__).resolve().parent.parent          # Credit Rating/
CASES_DIR = ROOT / "Companies"
CASES_DIR.mkdir(exist_ok=True)

app = Flask(__name__)
app.secret_key = "credit-rating-local-tool"
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 1024  # 1 GB per request

# ------------------------------------------------------------- upload conversion jobs
# Uploads of anything other than .md/.xlsx are converted to Markdown in a background thread
# (PDF conversion in particular can take real time on a long annual report), so the browser
# polls this registry for progress instead of blocking on the upload request. Job entries are
# small and short-lived; no persistence is needed across a server restart.
UPLOAD_JOBS: dict[str, dict] = {}
UPLOAD_JOBS_LOCK = threading.Lock()

# ---------------------------------------------------------------- checklist
DOC_SLOTS = [
    {"key": "annual_reports",    "label": "Annual Reports (3+ years)",
     "hint": "Audited annual reports for at least the last three fiscal years.",
     "required": True,  "min_files": 3},
    {"key": "quarterly_results", "label": "Latest Quarterly / Interim Results",
     "hint": "Most recent quarterly or half-yearly results (unaudited is fine, disclose cutoff).",
     "required": True,  "min_files": 1},
    {"key": "term_sheets",       "label": "Instrument Term Sheets / Sanction Letters",
     "hint": "Rated amounts are never inherited from prior reports - these documents fix them.",
     "required": True,  "min_files": 1},
    {"key": "sector_assumptions","label": "Sector Assumptions Document",
     "hint": "Published sector-assumptions note used for base-case projections.",
     "required": True,  "min_files": 1},
    {"key": "pillar3",           "label": "Pillar 3 Disclosures",
     "hint": "Banks / SFBs / AIFIs only - capital, LCR/NSFR, exposures.",
     "required": False, "min_files": 1},
    {"key": "prior_report",      "label": "Prior Rating Report (any agency)",
     "hint": "Optional. Opened only AFTER the independent view is formed (SOP Step 14).",
     "required": False, "min_files": 1},
    {"key": "other",             "label": "Other Supporting Documents",
     "hint": "Shareholding, order book, litigation, investor presentations, etc.",
     "required": False, "min_files": 1},
]
SLOT_KEYS = {s["key"] for s in DOC_SLOTS}

STOPWORDS = {"of", "and", "the", "&"}

# ---------------------------------------------------------------- agencies
# Each agency's reference library: (display, methodology dir, rationale dir, KB dir)
# relative to ROOT. ICRA lives at the root; CRISIL/CareEdge in their own folders.
# "scale" = rating-symbol style, "tag" = token used in deliverable filenames.
AGENCIES = {
    "ICRA":     {"methodology": "Methodology",
                 "reports": "Report for Reference",
                 "kb": "Knowledge Base",
                 "scale": "[ICRA]AAA ... [ICRA]D / [ICRA]A1+ ... A4, D",
                 "tag": ""},
    "CRISIL":   {"methodology": "CRISIL/Methodology",
                 "reports": "CRISIL/Report for Reference",
                 "kb": "Knowledge Base",
                 "scale": "Crisil AAA ... Crisil D / Crisil A1+ ... A4, D",
                 "tag": "CRISIL"},
    "CareEdge": {"methodology": "CareEdge/Methodology",
                 "reports": "CareEdge/Report for Reference",
                 "kb": "Knowledge Base",
                 "scale": "CARE AAA ... CARE D / CARE A1+ ... A4, D",
                 "tag": "CARE"},
}
DEFAULT_AGENCY = "ICRA"


def agency_of(case: dict) -> str:
    a = case.get("agency", DEFAULT_AGENCY)
    return a if a in AGENCIES else DEFAULT_AGENCY


def agency_brief(agency: str) -> str:
    """Folder-routing paragraph injected into prompts and request files."""
    cfg = AGENCIES[agency]
    lines = [
        "PROCESS: follow `UNIFIED_RATING_GUIDE.md` at the project root - ONE flow for "
        "all three agencies, 19 steps, each with a STOP-AND-ASK gate: ask the question "
        "and WAIT for my answer before proceeding. Never assume an answer.",
        f"Rating agency for this case: {agency}. Produce the rating outcome in "
        f"{agency}'s style on {agency}'s scale ({cfg['scale']}).",
        f"- Methodology: read from `{cfg['methodology']}/` ONLY (per AGENCIES.md, "
        f"never apply another agency's methodology text).",
        f"- Knowledge base (SHARED, all three agencies): `{cfg['kb']}/`"
        + (" (start with 01_Methodology_Index.md)."
           if (ROOT / cfg["kb"] / "01_Methodology_Index.md").is_file()
           else " (no index yet; route directly from the Methodology folder)."),
        f"- Report format & house style: learn from `{cfg['reports']}/` "
        f"reference rationales; do not assume the format from memory.",
    ]
    if cfg["tag"]:
        lines.append(f"- Name the deliverable `<Company>_<date>_{cfg['tag']}_Rating Rationale.md`.")
    else:
        lines.append("- Name the deliverable `<Company>_<date>_Rating Rationale.md`.")
    lines.append("- Forecasting (SOP Step 12): run the equity-research plugin's "
                 "initiating-coverage Tasks 1-4 individually (research -> 5-yr 3-statement "
                 "Excel model, plugin-native format -> valuation -> charts) into "
                 "`Companies/<slug>/`. Task 1 research: uploaded documents first, then "
                 "INDIAN sources via web search (AR/investor decks, BSE/NSE, screener.in, "
                 "agency rationales, business press) - never SEC EDGAR. Model adds TWO tabs: "
                 "Credit Ratios (agency-convention suite, all years, by formula) and Debt "
                 "Breakup (statutory LT/ST/lease decomposition tied to the AR and "
                 "screener.in; instrument/currency view from AR disclosures; the AR's own "
                 "net-debt bridge; rated-limits-vs-drawn-debt panel with the carried "
                 "table's DATE). Add a methodology-variable stress case; copy (never link) "
                 "base-case outputs into the scorecard assumptions. Skip Task 5. Deliver "
                 "the model + scorecard .xlsx WITH written reasoning, never a bare file.")
    lines.append("- Quantitative anchor (SOP Step 12b): fill a copy of `Rating_Scorecard.xlsx` "
                 "as `Companies/<slug>/Rating_Scorecard_<Company>.xlsx` (same agency; closest "
                 "scorecard sector), note the anchor grade in the workpaper, and explain any "
                 ">1-notch divergence from your rating view.")
    return "\n".join(lines)


# ---------------------------------------------- per-case methodology picker
def list_methodology(agency: str) -> list[str]:
    d = ROOT / AGENCIES[agency]["methodology"]
    return sorted((p.name for p in d.iterdir()
                   if p.is_file() and p.suffix.lower() == ".md"),
                  key=str.lower) if d.is_dir() else []


# Routing-category defaults: filename substrings (normalised: lowercase,
# -/_ -> space) that anchor each category's base methodology per agency.
CATEGORY_DEFAULTS = {
    "ICRA": {
        "corporate":  ["corporate credit rating"],
        "bank":       ["banks & financial institutions"],
        "nbfc":       ["nbfcs"],
        "financial":  [],
        "insurance":  [],
        "infra":      [],
        "structured": [],
        "public":     [],
    },
    "CRISIL": {
        "corporate":  ["manufacturing trading and corporate services"],
        "bank":       ["banks and financial institutions"],
        "nbfc":       ["finance and securities"],
        "financial":  ["finance and securities"],
        "insurance":  ["insurance companies"],
        "infra":      ["infrastructure sectors"],
        "structured": ["securitisation transactions"],
        "public":     ["public finance"],
    },
    "CareEdge": {
        "corporate":  ["manufacturing companies", "services sector"],
        "bank":       ["methodology banks", "hybrid instruments issued by banks",
                       "financial ratios financial sector"],
        "nbfc":       ["nbfc criteria", "housing finance companies",
                       "financial ratios financial sector"],
        "financial":  ["financial ratios financial sector"],
        "insurance":  ["insurance"],
        "infra":      ["infrastructure sector ratings"],
        "structured": ["securitisation transactions"],
        "public":     ["state governments"],
    },
}

SECTOR_STOP = {"&", "and", "of", "the", "no", "specific", "sector",
               "methodology", "company", "companies", "producers"}


def _norm_fname(name: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[-_]", " ", name.lower()))


def selected_methodologies(case: dict) -> list[str]:
    """The case's saved selection, dropping files that no longer exist."""
    files = set(list_methodology(agency_of(case)))
    return [m for m in case.get("methodologies", []) if m in files]


def suggest_methodologies(agency: str, sector: str, category: str) -> list[str]:
    """Sector-relevant subset of an agency's methodology files: the routing
    category's base file(s) plus filename matches on the sector name."""
    # superseded criteria stay listed for manual ticking but are never suggested
    files = [f for f in list_methodology(agency) if "archived" not in f.lower()]
    normed = {f: _norm_fname(f) for f in files}
    picked = []
    for anchor in CATEGORY_DEFAULTS.get(agency, {}).get(category, []):
        picked += [f for f in files if anchor in normed[f] and f not in picked]
    tokens = [t for t in re.split(r"[^a-z0-9]+", (sector or "").lower())
              if len(t) >= 3 and t not in SECTOR_STOP
              and t not in ("master", "criteria", "general")]
    if tokens:
        def word_hit(tok, words):
            # word-boundary plural-tolerant match: 'ports' hits 'port' but
            # 'port' must not hit 'airport'
            s = tok.rstrip("s")
            return any(w == tok or w == s or w.startswith(tok) or w.startswith(s + "s")
                       for w in words)
        for f in files:
            words = re.split(r"[^a-z0-9]+", normed[f])
            hit = sum(1 for t in tokens if word_hit(t, words))
            # 1-2 token sectors need every token; longer names allow half
            need_all = len(tokens) <= 2
            if hit and ((hit == len(tokens)) if need_all
                        else hit / len(tokens) >= 0.5) and f not in picked:
                picked.append(f)
    return picked

# ------------------------------------------------------------------- sectors
# Grouped by ICRA methodology routing category (Section 5 of the master prompt).
# Each group is (display label, routing category code, [sector names]).
# The routing category drives which methodology bundle the agent reads.
SECTOR_GROUPS = [
    ("Non-financial corporate", "corporate", [
        "Corporate (no specific sector methodology)",
        "Agrochemicals", "Auto Components", "Automobile Dealers",
        "Cement", "Chemicals", "Commercial Vehicles", "Construction",
        "Construction Vehicles", "Cut & Polished Diamonds",
        "Diagnostic Service Providers", "Edible Oil", "Fertilisers",
        "FMCG", "Footwear", "Higher Education", "Hospitals", "Hotels",
        "Iron & Steel", "IT (Software & Services)",
        "IT-Hardware-related Services", "Jewellery-Retail", "Media (Films)",
        "Mining", "Non-Ferrous Metals", "Oil Exploration & Production",
        "Oilfield Services", "Paper", "Passenger Cars",
        "Passenger Road Transport", "Pharmaceuticals", "Print Media",
        "Real Estate", "Realty (Leasing)", "Refining and Marketing",
        "Retail", "Rice Mills", "Shipping", "Sugar", "TV Broadcasting",
        "Tea", "Telecom Services", "Textiles (Apparels)",
        "Textiles (Fabric)", "Textiles (Spinning)", "Tractors",
        "Trading Companies", "Two Wheelers",
    ]),
    ("Bank / SFB / AIFI", "bank", [
        "Bank / SFB / AIFI (Banks & Financial Institutions)",
    ]),
    ("NBFC / HFC / MFI", "nbfc", [
        "NBFC", "Housing Finance Company (HFC)", "Microfinance (MFI)",
    ]),
    ("Other financial", "financial", [
        "Investment Company", "Mutual Fund",
        "Alternative Investment Fund (AIF)", "Primary Dealer",
        "Stockbroking & Allied Services",
    ]),
    ("Insurance", "insurance", [
        "General Insurance", "Life Insurance",
    ]),
    ("Infrastructure / project", "infra", [
        "Airports", "City Gas Distribution", "Ports",
        "Power (Thermal)", "Power (Transmission)", "Power (Distribution)",
        "Power (Solar and Wind)", "Wind Power Producers",
        "Roads (Hybrid Annuity)", "Roads (BOT Toll)", "Roads (Annuity)",
        "Telecom Towers", "Project Finance",
        "Infrastructure Investment Trust (InvIT)",
        "Real Estate Investment Trust (REIT)",
    ]),
    ("Structured finance", "structured", [
        "Securitisation Transactions", "Collateralised Debt Obligation",
        "Pooled Loan Issuance", "Security Receipts",
    ]),
    ("Public finance", "public", [
        "State Government", "Urban Local Body",
    ]),
]
SECTOR_TO_CATEGORY = {sec: cat for _, cat, secs in SECTOR_GROUPS for sec in secs}

# Per-agency sector lists: each agency's dropdown only offers sectors its own
# methodology library actually covers. ICRA = the full list above; CRISIL's
# consolidated masters cover sectors as internal Sections; CareEdge has one
# paper per sector. Names are chosen to token-match that agency's filenames.
CRISIL_SECTOR_GROUPS = [
    ("Non-financial corporate (manufacturing/trading/services master)", "corporate", [
        "Corporate - Manufacturing & Services (master criteria)",
        "Trading Companies", "Education Institutions",
        "Materials (Cement / Steel / Metals / Mining / Chemicals)",
        "Industrial Sector", "Automotive & Auto Components",
        "Consumer Staples & Discretionary (FMCG / Retail / Textiles)",
        "Pharmaceuticals", "IT (Software & Services)",
        "Telecom (Mobile Telephony)", "Oil & Gas",
    ]),
    ("Bank / financial institutions", "bank", [
        "Bank / FI (Banks & Financial Institutions)",
    ]),
    ("Finance & securities companies", "nbfc", [
        "NBFC / Finance Company", "Housing Finance Company (HFC)",
        "Securities / Broking Company",
    ]),
    ("Other financial", "financial", [
        "Bond Fund (Credit Quality Rating)", "Capital Protection-Oriented Fund",
        "Mutual Fund (Intraday Borrowing)", "Investment Holding Company",
    ]),
    ("Insurance", "insurance", [
        "General Insurance", "Life Insurance",
    ]),
    ("Infrastructure & real assets", "infra", [
        "Infrastructure (general criteria)", "Power",
        "Roads (Annuity / Hybrid Annuity)", "Roads (Toll)",
        "Real Estate / LRD / CMBS", "REIT / InvIT",
        "Expected Loss Rating (Infrastructure Projects)",
    ]),
    ("Structured finance", "structured", [
        "Securitisation (ABS / RMBS / CDO)", "Covered Bonds",
        "Future Flow Transactions", "Security Receipts",
        "ICE - Residual Debt (Stressed Assets)",
    ]),
    ("Public finance", "public", [
        "Urban Local Body / Municipal", "State Government",
    ]),
]

CAREEDGE_SECTOR_GROUPS = [
    ("Non-financial corporate", "corporate", [
        "Corporate - Manufacturing (master criteria)",
        "Corporate - Services (master criteria)",
        "Cement", "Iron & Steel", "Non-Ferrous Metals", "Fertilizer",
        "Pesticides & Agrochemicals", "Pharmaceutical", "Paper & Paper Products",
        "Cotton Textile", "Cut & Polished Diamonds", "Sugar",
        "Auto Components", "Commercial Vehicles", "Auto Dealership",
        "Organized Retail", "Wholesale Trading", "Hotel", "Hospital",
        "Education", "Shipping", "Telecom (Mobile Service Providers)",
        "City Gas Distribution", "Construction", "Real Estate", "REIT",
    ]),
    ("Bank", "bank", [
        "Bank / SFB / RRB",
    ]),
    ("NBFC / HFC", "nbfc", [
        "NBFC", "Housing Finance Company (HFC)",
    ]),
    ("Other financial", "financial", [
        "Broking Company", "Investment Holding Company",
        "Fund Credit Quality (Debt MF)", "Capital Protection-Oriented MF Scheme",
        "Market Linked Debentures",
    ]),
    ("Insurance", "insurance", [
        "Non-Life Insurance", "Life Insurance (financial ratios)",
    ]),
    ("Infrastructure & project", "infra", [
        "Infrastructure (general criteria)", "Power (Thermal)",
        "Power (Solar)", "Power (Wind)", "Power Generation (general)",
        "Power Transmission", "Power Distribution",
        "Roads (Toll)", "Roads (Hybrid Annuity)", "Roads (Annuity)",
        "Airport", "Port", "Urban Infrastructure", "InvIT",
        "Expected Loss Rating (Infrastructure)", "Project Stage Entity",
    ]),
    ("Structured finance & credit enhancement", "structured", [
        "Securitisation (Asset / Mortgage Backed)",
        "Pools Backed by Wholesale Assets", "Lease Rentals Discounting (LRD)",
        "Credit Enhanced Debt", "Recovery Rating (Security Receipts)",
        "Independent Credit Evaluation - Residual Debt",
    ]),
    ("Public finance", "public", [
        "State Government",
    ]),
]

AGENCY_SECTOR_GROUPS = {
    "ICRA": SECTOR_GROUPS,
    "CRISIL": CRISIL_SECTOR_GROUPS,
    "CareEdge": CAREEDGE_SECTOR_GROUPS,
}
AGENCY_SECTOR_TO_CATEGORY = {
    ag: {sec: cat for _, cat, secs in groups for sec in secs}
    for ag, groups in AGENCY_SECTOR_GROUPS.items()
}

# Words that appear in company names / descriptions but carry no sector signal.
SECTOR_QUERY_STOP = SECTOR_STOP | {
    "limited", "ltd", "llp", "pvt", "private", "group", "industries",
    "industry", "india", "co", "inc", "corp", "corporation", "holdings",
}


def _sector_tokens(text: str) -> set[str]:
    return {t for t in re.split(r"[^a-z0-9]+", (text or "").lower())
            if len(t) >= 3 and t not in SECTOR_QUERY_STOP}


def suggest_sectors(agency: str, text: str, top_n: int = 3) -> list[tuple[str, str, int]]:
    """Rank an agency's sectors by keyword overlap with a free-text company
    name/description - e.g. 'manufactures cement and clinker' -> Cement."""
    q = _sector_tokens(text)
    if not q:
        return []
    scored = []
    for _label, cat, secs in AGENCY_SECTOR_GROUPS.get(agency, []):
        for sec in secs:
            hit = q & _sector_tokens(sec)
            if hit:
                scored.append((sec, cat, len(hit)))
    scored.sort(key=lambda x: -x[2])
    return scored[:top_n]


# ------------------------------------------------------------------- helpers
def slugify(name: str) -> str:
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s or "company"


def acronym(name: str) -> str:
    words = [w for w in re.split(r"\s+", name) if w and w.lower() not in STOPWORDS]
    a = "".join(w[0].upper() for w in words)
    return a if len(a) >= 2 else ""       # 1-letter acronyms match too much


def case_path(slug: str) -> Path:
    p = (CASES_DIR / slug).resolve()
    if not str(p).startswith(str(CASES_DIR.resolve())):
        abort(404)
    return p


def load_case(slug: str) -> dict:
    f = case_path(slug) / "case.json"
    if not f.exists():
        abort(404)
    data = json.loads(f.read_text(encoding="utf-8"))
    # case.json is hand-edited by the rating workflow, so "isins" arrives either as the full
    # record the UI expects or as a bare list of ISIN strings. A string reached ins.get() and
    # 500'd the whole company page (hdfc-securities, 20-Aug-2026). Normalise once here, where
    # every caller routes through, rather than guarding each template and mutation route.
    data["isins"] = [
        ins if isinstance(ins, dict)
        else {"isin": str(ins), "name": "", "amount": "", "uploaded": False}
        for ins in (data.get("isins") or [])
    ]
    for ins in data["isins"]:
        ins.setdefault("isin", "")
        ins.setdefault("name", "")
        ins.setdefault("amount", "")
        ins.setdefault("uploaded", False)
    return data


def save_case(slug: str, data: dict) -> None:
    (case_path(slug) / "case.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def list_cases() -> list[dict]:
    cases = []
    for d in sorted(CASES_DIR.iterdir()):
        f = d / "case.json"
        if f.is_file():
            try:
                c = json.loads(f.read_text(encoding="utf-8"))
                c["slug"] = d.name
                cases.append(c)
            except json.JSONDecodeError:
                continue
    return cases


def slot_files(slug: str, key: str) -> list[Path]:
    d = case_path(slug) / "documents" / key
    return sorted(p for p in d.iterdir() if p.is_file()) if d.is_dir() else []


def checklist_state(slug: str) -> list[dict]:
    out = []
    for slot in DOC_SLOTS:
        files = slot_files(slug, slot["key"])
        out.append({**slot, "files": files,
                    "done": len(files) >= slot["min_files"]})
    return out


def match_names(case: dict) -> set[str]:
    names = {case["name"].lower()}
    a = acronym(case["name"])
    # 2-letter acronyms are too generic to be safe even with word-boundary matching
    # ("IT" for Indus Towers would still claim a file literally starting "IT ").
    if a and len(a) >= 3:
        names.add(a.lower())
    names.update(x.strip().lower() for x in case.get("aliases", [])
                 if len(x.strip()) >= 2)
    return names


def _name_matches(name: str, filename_lower: str) -> bool:
    """Whole-word match of `name` in a filename.

    Substring matching (the original implementation) produced cross-company false
    positives: the auto-acronym 'IT' for "Indus Towers" matched every "ITC Limited_*"
    file via startswith, and the alias 'Indus' matched "DOMS **Indus**tries" via the
    ' '+n test. Separators are normalised to spaces so word boundaries behave, then
    the name must not be flanked by another alphanumeric.
    """
    norm = re.sub(r"[_\-]+", " ", filename_lower)
    return re.search(r"(?<![a-z0-9])" + re.escape(name) + r"(?![a-z0-9])", norm) is not None


# The words that mark a file as a deliverable rather than working scaffolding. Named once so
# the discovery filter and the legal-name derivation below cannot drift apart.
OUTPUT_WORDS = ("rationale", "workpaper", "research", "scorecard", "model", "valuation",
                "chart", "spreads", "ratio")

# Deliverables only. `.py` was added here on 01-Sep-2026 while fixing the missing-rationale
# bug and REMOVED the same day: it filled the Output panel with compute_ratios.py,
# fill_scorecard.py and build_spreads.py, which are the machinery that produces the
# deliverables, not the deliverables. This panel is "rationale, workpaper & research"; the
# scripts live in the case folder for anyone who wants them.
OUTPUT_SUFFIXES = (".md", ".pdf", ".xlsx", ".docx", ".png")


def derived_names(slug: str) -> set[str]:
    """Extra names this case answers to, read off its OWN folder's deliverables.

    WHY THIS EXISTS. A case is registered under whatever the operator typed - often an
    acronym or short form ("Vi", "SBI") - while its deliverables are filed under the issuer's
    LEGAL name ("Vodafone Idea Limited", "State Bank of India"). Files inside the case folder
    are matched by ownership and so were always found; files in the SHARED project root are
    matched by name, and for those cases the rationale was invisible in the tool. That is the
    same defect recorded in the comment inside find_outputs() for the case folder, arriving
    from the other side.

    A file in the case's own folder belongs to that case BY CONSTRUCTION, so the issuer name
    embedded in its filename is evidence about this case and nothing else. Deriving from it
    widens root matching without weakening the cross-contamination guard: a case with no such
    deliverable derives nothing and behaves exactly as before.

    The candidate must be at least TWO tokens. Single tokens produce false names - a file
    called compute_ratios.py would otherwise contribute "compute" - and a one-word name is
    precisely the kind that collides across issuers.
    """
    folder = case_path(slug)
    if not folder.is_dir():
        return set()
    out = set()
    for p in folder.iterdir():
        if not p.is_file() or p.suffix.lower() not in OUTPUT_SUFFIXES:
            continue
        low = p.name.lower()
        # Derive only from DELIVERABLES, on the same test discovery uses. Without this,
        # COMPANY_CONTEXT.md contributed the "name" company context.
        if not any(w in low for w in OUTPUT_WORDS):
            continue
        stem = re.sub(r"[_\-]+", " ", p.stem.lower())
        toks = [t for t in stem.split() if t]
        # Keep the leading run of tokens up to the first word that describes the ARTEFACT
        # rather than the issuer, and stop at the first date-like or numeric token.
        lead = []
        for t in toks:
            if t in OUTPUT_WORDS or t.startswith("rating") or re.search(r"\d", t):
                break
            lead.append(t)
        # Drop a leading artefact word ("rating_scorecard_<issuer>") before giving up.
        if not lead:
            rest = toks
            while rest and (rest[0] in OUTPUT_WORDS or rest[0].startswith("rating")):
                rest = rest[1:]
            for t in rest:
                if t in OUTPUT_WORDS or re.search(r"\d", t):
                    break
                lead.append(t)
        # A leading script verb means the filename describes an ACTION, not an issuer -
        # compute_ratios.py would otherwise contribute "compute ratios" as a company name.
        if lead and lead[0] in ("compute", "build", "fill", "cache", "make", "generate",
                                "verify", "check", "run"):
            continue
        if len(lead) >= 2:
            out.add(" ".join(lead))
    return out


def find_outputs(case: dict, slug: str) -> list[dict]:
    """Rationale / workpaper files in the project root or the case folder."""
    names = match_names(case) | derived_names(slug)
    hits, seen = [], set()
    for folder in (ROOT, case_path(slug)):
        # A file inside the case's OWN folder belongs to that case by construction, so it needs
        # no filename match. Name matching exists only to disambiguate the SHARED project root
        # (that is what the Indus Towers cross-contamination fix was for, and it still applies
        # there). Requiring it in the case folder produced a silent FALSE NEGATIVE: the case
        # named "SBI" could not see its own deliverables, which are filed under the issuer's
        # legal name "State Bank of India". Found 14-Aug-2026.
        own_folder = folder != ROOT
        if not folder.is_dir():
            continue
        for p in folder.iterdir():
            if not p.is_file() or p.suffix.lower() not in OUTPUT_SUFFIXES:
                continue
            low = p.name.lower()
            # "spreads"/"ratio" added 14-Aug-2026: the ratio Excel (<Company>_Financial_Spreads
            # .xlsx) is a STANDING deliverable for every case, but matched none of these terms,
            # so it was invisible in the tool for every case that had one.
            if not any(w in low for w in OUTPUT_WORDS):
                continue
            # A file the analyst explicitly retired is not a deliverable. Without this the
            # tool lists compute_ratios_v1_superseded.py beside the live engine, which is
            # exactly the ambiguity the rename was meant to remove.
            if "superseded" in low or "deprecated" in low:
                continue
            if not own_folder and not any(_name_matches(n, low) for n in names):
                continue
            if p.name in seen:
                continue
            seen.add(p.name)
            kind = ("Workpaper" if "workpaper" in low
                    else "Ratio Excel" if ("spreads" in low or "ratio" in low)
                    and p.suffix.lower() == ".xlsx"
                    else "Scorecard" if "scorecard" in low
                    else "Forecast Model" if "model" in low
                    else "Valuation" if "valuation" in low
                    else "Chart" if "chart" in low
                    else "Research Note" if "research" in low
                    else "Rating Rationale")
            hits.append({"path": p, "rel": str(p.relative_to(ROOT)),
                         "kind": kind,
                         "mtime": datetime.fromtimestamp(p.stat().st_mtime)})
    return sorted(hits, key=lambda h: h["mtime"], reverse=True)


def _auto_clear_delivered_requests(case: dict, slug: str, outs: list[dict]) -> None:
    """Self-heal a stale 'requested' flag: if a Rating Rationale / Research Note
    output already exists newer than the request timestamp, the SOP has already
    delivered it - drop the flag and the *_REQUEST.md file instead of leaving
    the UI stuck showing 'still pending' next to a finished deliverable."""
    changed = False
    for flag, kind, reqfile in (("rating_requested", "Rating Rationale", "RATING_REQUEST.md"),
                                 ("research_requested", "Research Note", "RESEARCH_REQUEST.md")):
        ts = case.get(flag)
        if not ts:
            continue
        try:
            requested_at = datetime.fromisoformat(ts)
        except ValueError:
            continue
        if any(o["kind"] == kind and o["mtime"] >= requested_at for o in outs):
            case.pop(flag, None)
            changed = True
            f = case_path(slug) / reqfile
            if f.is_file():
                f.unlink()
    if changed:
        save_case(slug, case)
        write_context(slug)


def kickoff_prompt(case: dict, slug: str) -> str:
    agency = agency_of(case)
    lines = [f"New company: {case['name']}.",
             "Follow the SOP phase by phase and show me the evidence for each step. "
             "Create the rating report.",
             agency_brief(agency),
             f"Company documents are in: Companies/{slug}/documents/"]
    sel = selected_methodologies(case)
    if sel:
        mdir = AGENCIES[agency]["methodology"]
        lines.append(f"Applicable methodology files (selected for this case - read ALL "
                     f"of them from `{mdir}/`, and verify each file's scope statement "
                     "matches the company):")
        lines += [f"  - {m}" for m in sel]
        lines.append("Apply cross-cutting approaches (consolidation, parent/govt "
                     "notching, hybrids) and the policy layer on top as relevant.")
    if case.get("sector"):
        route_note = ("Route to the applicable ICRA methodology per Section 5"
                      if agency == "ICRA" else
                      f"Route to the applicable {agency} methodology via its "
                      "methodology index / Methodology folder (see AGENCIES.md)")
        lines.append(f"Sector: {case['sector']} (routing category: "
                     f"{case.get('entity_type','corporate')}). {route_note} "
                     "and verify each scope statement.")
    up = [f"  - {s['label']}: " + ", ".join(f.name for f in s["files"])
          for s in checklist_state(slug) if s["files"]]
    if up:
        lines.append("Uploaded documents:")
        lines += up
    missing = [s["label"] for s in checklist_state(slug)
               if s["required"] and not s["done"]]
    if missing:
        lines.append("Known gaps (handle per SOP Step 1): " + "; ".join(missing))
    isins = case.get("isins", [])
    if isins:
        lines.append("Instruments to rate:")
        lines += [f"  - {i['isin'] or '(ISIN pending)'} | {i['name']} | "
                  f"Rs. {i['amount'] or '-'} crore | term sheet "
                  f"{'uploaded' if i.get('uploaded') else 'NOT uploaded - ask me'}"
                  for i in isins]
    return "\n".join(lines)


def session_prompt(case: dict, slug: str) -> str:
    """Kickoff for a NEW, dedicated Claude session for this company."""
    agency = agency_of(case)
    return (
        f"Company session: {case['name']}.\n"
        f"This session is DEDICATED to {case['name']} "
        f"({case.get('sector', 'sector n/a')}; routing: {case.get('entity_type', 'corporate')}; "
        f"rating agency: {agency}). "
        "Keep all research, analysis and rating work for this company in this session.\n"
        f"{agency_brief(agency)}\n"
        f"1. Read Companies/{slug}/COMPANY_CONTEXT.md first - the intake app keeps it current.\n"
        f"2. Read every document in Companies/{slug}/documents/ one by one per Step 1b of "
        "CLAUDE.md - build the Document Read Log BEFORE any drafting, and re-open the "
        "documents whenever a later question needs them.\n"
        "3. Then await my instructions - e.g. \"run the full rating SOP\" (icra-rating skill) "
        "or \"build the research fact pack\" (finance-research skill)."
    )


def write_context(slug: str) -> None:
    """(Re)generate Companies/<slug>/COMPANY_CONTEXT.md - the standing briefing a
    dedicated session loads first. Called after every mutation of the case."""
    case = load_case(slug)
    lines = [
        f"# COMPANY CONTEXT - {case['name']}",
        "*Auto-generated by the intake web app; regenerated on every change. "
        "A session dedicated to this company should read this file first, then the "
        "documents below one by one (Step 1b of CLAUDE.md).*",
        "",
        f"- **Company:** {case['name']}",
        f"- **Rating agency:** {agency_of(case)} (produce the outcome in this agency's "
        f"style and scale; see AGENCIES.md)",
        f"- **Sector:** {case.get('sector', '-')}  |  **Routing category:** {case.get('entity_type', 'corporate')}",
        f"- **Aliases (output matching):** {', '.join(case.get('aliases', [])) or '-'}",
        f"- **Case created:** {case.get('created', '-')}",
        f"- **Rating requested:** {case.get('rating_requested', 'no')}  |  "
        f"**Research requested:** {case.get('research_requested', 'no')}  |  "
        f"**Delivered:** {case.get('rating_delivered', '-')}",
        "",
        "## Documents (read each one, per slot)",
    ]
    for s in checklist_state(slug):
        files = ", ".join(f.name for f in s["files"]) or "(none)"
        lines.append(f"- **{s['label']}**: {files}")
    sel = selected_methodologies(case)
    lines.append("")
    lines.append("## Applicable methodology (selected in the intake app)")
    if sel:
        mdir = AGENCIES[agency_of(case)]["methodology"]
        lines += [f"- `{mdir}/{m}`" for m in sel]
        lines.append("- Apply cross-cutting approaches and the policy layer on top as relevant.")
    else:
        lines.append("- none selected; route via the agency's methodology index")
    isins = case.get("isins", [])
    lines.append("")
    lines.append("## Instruments (ISINs)")
    if isins:
        lines += [f"- {i['isin'] or '(ISIN pending)'} | {i['name']} | Rs. {i['amount'] or '-'} crore | "
                  f"term sheet {'uploaded' if i.get('uploaded') else 'not uploaded'}"
                  for i in isins]
    else:
        lines.append("- none recorded; extract from the annual report per Step 7b of CLAUDE.md")
    lines += [
        "",
        "## Standing instructions",
        "- Master prompt: `CLAUDE.md` at the project root (19-step SOP); skills: `icra-rating`, `finance-research`.",
        agency_brief(agency_of(case)),
        "- Facts come ONLY from this company's documents; reference reports teach craft only.",
        "- Deliverables are saved to the project root (`<Company>_..._Rating Rationale.md`, "
        "`<Company>_Ratio_Workpaper_...md`, `<Company>_Research_Note_...md`) - the web app "
        "auto-detects them by company name/alias.",
    ]
    (case_path(slug) / "COMPANY_CONTEXT.md").write_text("\n".join(lines), encoding="utf-8")


# ------------------------------------------------------------------ template
PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ title }}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap">
<style>
:root { --bg:#F4F6F9; --panel2:#EDF1F7; --card:#FFFFFF; --line:#DDE3EC;
        --ink:#1F2733; --mut:#68738A; --faint:#95A0B4; --edge:#8894AB;
        --navy:#1b2a4a; --navy2:#233a63; --teal:#0e7c86; --teal2:#12a0ac;
        --accent:#0e7c86; --accent-ink:#0b5f67; --decide:#dceef0;
        --ok:#1a7f37; --warn:#b45309;
        --serif:"Source Serif 4",Georgia,serif;
        --sans:"IBM Plex Sans","Segoe UI",system-ui,sans-serif;
        --mono:"IBM Plex Mono",ui-monospace,Consolas,monospace;
        --shadow:0 1px 2px rgba(27,42,74,.06), 0 1px 1px rgba(27,42,74,.04);
        --shadow-hov:0 16px 36px -20px rgba(27,42,74,.28); }
@media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){
        --bg:#0f1729; --panel2:#16213a; --card:#172137; --line:#28344f;
        --ink:#e7ecf5; --mut:#9aa8c4; --faint:#6b7a99; --edge:#5f6f8f;
        --navy:#e7ecf5; --navy2:#e7ecf5; --teal:#3ab6c2; --teal2:#4fc9d4;
        --accent:#3ab6c2; --accent-ink:#8fd8df; --decide:#123642;
        --ok:#57c07a; --warn:#e0a54a;
        --shadow:0 1px 2px rgba(0,0,0,.3); --shadow-hov:0 20px 44px -22px rgba(0,0,0,.6); } }
* { box-sizing:border-box; margin:0; }
html { scroll-behavior:smooth; }
body { font:15px/1.6 var(--sans); background:var(--bg); color:var(--ink);
       -webkit-font-smoothing:antialiased; }
a { color:var(--teal); text-decoration:none; } a:hover { text-decoration:underline; }
header { background:linear-gradient(135deg,#1b2a4a,#233a63); color:#fff; padding:8px 28px; min-height:58px;
         display:flex; align-items:center; gap:16px; flex-wrap:wrap; position:sticky; top:0; z-index:20;
         box-shadow:0 2px 12px rgba(15,23,42,.20); }
header .brand { font-size:17px; font-weight:600; letter-spacing:.01em; display:flex; align-items:center; gap:9px; }
header .brand a { color:#fff; display:flex; align-items:center; gap:9px; }
header .brand a:hover { text-decoration:none; }
header .brand .mark { width:26px; height:26px; border-radius:7px; background:linear-gradient(135deg,#12a0ac,#15c7b8);
       display:inline-flex; align-items:center; justify-content:center; font-size:12px; font-weight:700; color:#04302f; }
header nav { display:flex; gap:2px; margin-left:10px; }
header nav a { color:#c3d0ea; font-size:14px; padding:7px 13px; border-radius:7px; transition:background .15s,color .15s; }
header nav a:hover { background:rgba(255,255,255,.08); color:#fff; text-decoration:none; }
header nav a.active { background:rgba(255,255,255,.14); color:#fff; font-weight:600; }
header .sub { font-family:var(--mono); color:#93a6cc; font-size:11.5px; letter-spacing:.06em; margin-left:auto; }
main { max-width:1120px; margin:28px auto 70px; padding:0 20px; }
h1 { font-family:var(--serif); font-size:30px; font-weight:700; margin-bottom:5px; letter-spacing:-.02em; line-height:1.1; }
h2 { font-family:var(--serif); font-size:20px; margin:30px 0 10px; font-weight:700; color:var(--ink); display:flex; align-items:center; gap:10px; letter-spacing:-.01em; }
.mut { color:var(--mut); font-size:13px; }
.card { background:var(--card); border:1px solid var(--line); border-radius:12px;
        padding:18px 22px; margin-top:14px; box-shadow:var(--shadow); scroll-margin-top:76px;
        transition:box-shadow .15s; }
.card:hover { box-shadow:var(--shadow-hov); }
table { border-collapse:collapse; width:100%; font-size:14px; }
th,td { text-align:left; padding:10px 12px; border-bottom:1px solid var(--line); vertical-align:top; }
th { color:var(--mut); font-weight:600; font-size:11.5px; text-transform:uppercase; letter-spacing:.5px;
     border-bottom:2px solid var(--line); }
tbody tr { transition:background .12s; }
tbody tr:hover { background:#f7f9fc; }
.btn { display:inline-flex; align-items:center; gap:6px; background:var(--accent); color:#fff; border:0;
       border-radius:8px; padding:8px 16px; font-size:13.5px; font-weight:500; cursor:pointer;
       box-shadow:0 1px 2px rgba(14,124,134,.24); transition:filter .12s,box-shadow .12s,transform .05s; }
.btn:hover { filter:brightness(1.07); box-shadow:0 4px 12px -2px rgba(14,124,134,.34); text-decoration:none; }
.btn:active { transform:translateY(1px); }
.btn.ghost { background:transparent; color:var(--ink); border:1px solid var(--line); box-shadow:none; }
.btn.ghost:hover { background:var(--panel2); border-color:var(--edge); }
.btn.small { padding:4px 11px; font-size:12.5px; }
.btn.danger { background:#fff; color:#b3261e; border:1px solid #e3b6b3; box-shadow:none; }
.btn.danger:hover { background:#fdf2f1; }
label.field-label { display:block; font-size:12px; font-weight:600; color:var(--mut);
       text-transform:uppercase; letter-spacing:.4px; margin-bottom:4px; }
input[type=text], input[type=password], select { border:1px solid var(--line); border-radius:8px; padding:8px 11px;
       font-size:14px; width:100%; background:#fff; transition:border-color .12s,box-shadow .12s; }
input[type=text]:focus, input[type=password]:focus, select:focus { outline:none; border-color:var(--teal2);
       box-shadow:0 0 0 3px rgba(18,160,172,.18); }
input[type=file] { font-size:13px; max-width:230px; }
.tick { font-size:17px; font-weight:700; }
.tick.ok { color:var(--ok); } .tick.no { color:#c2c9d6; }
.badge { display:inline-flex; align-items:center; gap:4px; font-size:11px; padding:3px 10px; border-radius:99px;
         font-weight:700; letter-spacing:.3px; }
.badge.req { background:#fdece0; color:var(--warn); }
.badge.opt { background:#e8edf4; color:var(--mut); }
.badge.done { background:#e2f3e6; color:var(--ok); }
.progress { height:9px; background:#e8edf4; border-radius:99px; overflow:hidden; margin:8px 0 2px; }
.progress i { display:block; height:100%; background:linear-gradient(90deg,var(--teal),var(--teal2)); transition:width .3s; }
.flash { background:#e2f3e6; border:1px solid #bfe3c8; color:#14532d; padding:10px 15px;
         border-radius:9px; margin-top:12px; font-size:14px; box-shadow:var(--shadow); }
textarea.prompt { width:100%; min-height:150px; font:12.5px/1.5 Consolas,monospace;
         border:1px solid var(--line); border-radius:9px; padding:11px; background:#fbfcfe; }
.rowform { display:flex; gap:10px; flex-wrap:wrap; align-items:flex-end; }
.rowform > * { flex:1 1 140px; } .rowform .btn { flex:0 0 auto; }
/* settings page */
.pill { display:inline-block; padding:2px 10px; border-radius:999px; font-size:12px;
        font-weight:600; margin-right:8px; vertical-align:1px; }
.pill.ok   { background:#e3f4ec; color:#136c45; }
.pill.warn { background:#fdf1dc; color:#8a5a08; }
.pill.bad  { background:#fdecec; color:#9a2020; }
table.kv { border-collapse:collapse; margin-top:10px; font-size:13.5px; }
table.kv td { padding:5px 16px 5px 0; vertical-align:top; }
table.kv td:first-child { color:#6b7891; white-space:nowrap; }
pre.cmd { background:#1b2a4a; color:#dfe8f7; padding:11px 14px; border-radius:8px;
          font-family:var(--mono); font-size:13px; overflow-x:auto; margin:10px 0; }
.rowform input[type=password] { min-width:260px; font-family:ui-monospace,Consolas,monospace; }
.upstat { font-size:12.5px; color:var(--teal); margin-top:4px; min-height:16px; font-weight:600; }
.upprogress { margin-top:6px; }
.upprogress-bar { background:#e3e8f0; border-radius:6px; height:8px; overflow:hidden; }
.upprogress-fill { background:var(--teal); height:100%; width:0%; transition:width .3s ease; }
.upprogress-label { font-size:12px; margin-top:4px; }
.steps { counter-reset:s; padding-left:0; list-style:none; }
.steps li { counter-increment:s; margin:7px 0; padding-left:34px; position:relative; font-size:14px; }
.steps li:before { content:counter(s); position:absolute; left:0; top:1px; width:22px; height:22px;
       border-radius:50%; background:var(--navy); color:#fff; font-size:12.5px; font-weight:600;
       display:flex; align-items:center; justify-content:center; }
.secnum { flex:0 0 auto; width:24px; height:24px; border-radius:50%;
       background:linear-gradient(135deg,var(--teal),var(--teal2)); color:#fff; font-size:12.5px;
       font-weight:800; display:inline-flex; align-items:center; justify-content:center; }
.jumpnav { display:flex; flex-wrap:wrap; gap:6px; margin:14px 0 0; position:sticky; top:58px; z-index:10;
       background:var(--bg); padding:8px 0; }
.jumpnav a { background:var(--card); border:1px solid var(--line); color:var(--navy); font-size:12.5px;
       font-weight:600; padding:6px 12px; border-radius:99px; box-shadow:var(--shadow); transition:all .12s; }
.jumpnav a:hover { border-color:var(--teal2); color:var(--teal); text-decoration:none; transform:translateY(-1px); }
.agency-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:16px; margin-top:18px; }
.agency-card { display:block; background:var(--card); border:1px solid var(--line); border-radius:14px;
       padding:22px 22px 20px; box-shadow:var(--shadow); transition:box-shadow .15s,transform .15s,border-color .15s; }
.agency-card:hover { box-shadow:var(--shadow-hov); transform:translateY(-2px); border-color:var(--teal2);
       text-decoration:none; }
.agency-card h2 { color:var(--navy); font-size:21px; }
.reqbox { background:#fef8ec; border:1px solid #f0dcb0; border-radius:9px;
       padding:11px 15px; margin-top:10px; font-size:13.5px; }
.md { font-size:14.5px; }
.md h1,.md h2,.md h3 { margin:18px 0 8px; color:var(--navy); }
.md table { margin:10px 0; } .md th,.md td { border:1px solid var(--line); }
.md p,.md ul,.md ol { margin:8px 0 8px 0; } .md ul,.md ol { padding-left:22px; }
.md code { background:#eef1f6; padding:1px 5px; border-radius:4px; font-size:12.5px; }
@media (max-width:640px) {
  header { padding:12px 16px; } header .sub { display:none; }
  main { margin:18px auto 50px; padding:0 14px; }
  .card { padding:15px; }
  .rowform > * { flex-basis:100%; }
}
</style></head><body>
<header>
  <span class="brand"><a href="{{ url_for('agency_picker') }}"><span class="mark">RA</span>Rating Agent</a></span>
  <nav>
    <a href="{{ url_for('agency_picker') }}"{{ ' class=active' if active=='cases' else '' }}>Cases</a>
    <a href="{{ url_for('library') }}"{{ ' class=active' if active=='library' else '' }}>Reference Library</a>
    <a href="{{ url_for('process_flow') }}"{{ ' class=active' if active=='process' else '' }}>Process Flow</a>
    <a href="{{ url_for('settings') }}"{{ ' class=active' if active=='settings' else '' }}>Settings</a>
  </nav>
  <span class="sub">ICRA &middot; CRISIL &middot; CareEdge</span>
</header>
<main>
{% with msgs = get_flashed_messages() %}{% for m in msgs %}<div class="flash">&#10003; {{ m }}</div>{% endfor %}{% endwith %}
{{ body|safe }}
</main>
<script>
function copyPrompt(){ const t=document.getElementById('kickoff');
  t.select(); document.execCommand('copy');
  document.getElementById('copybtn').textContent='Copied!';
  setTimeout(()=>document.getElementById('copybtn').textContent='Copy prompt',1500); }
function filtMeth(q){ q=q.toLowerCase();
  document.querySelectorAll('#methlist label.methrow').forEach(l => {
    l.style.display = l.textContent.toLowerCase().includes(q) ? 'block' : 'none'; }); }
function copySession(){ const t=document.getElementById('sesskick');
  t.select(); document.execCommand('copy');
  document.getElementById('sesscopybtn').textContent='Copied!';
  setTimeout(()=>document.getElementById('sesscopybtn').textContent='Copy session prompt',1500); }

/* Auto-upload on file selection: each chosen batch is sent immediately via fetch, so picking
   files in several rows can never lose a selection to a page reload. Non-Excel/Markdown files
   are converted to Markdown in a background job on the server; this polls that job's progress
   and drives a bar until it completes, then reloads so the new documents appear. */
let pendingUploads = 0;

async function pollUploadJob(jobId, bar, fill, label, stat, fileCount) {
  while (true) {
    let resp;
    try {
      resp = await fetch('/upload-progress/' + jobId);
    } catch (e) {
      label.textContent = 'Lost contact with the server - reload the page to check status.';
      return;
    }
    if (resp.status === 404) { label.textContent = 'Conversion job finished.'; return; }
    const job = await resp.json();

    const pct = job.total ? Math.round(100 * job.done / job.total) : 0;
    fill.style.width = pct + '%';
    let text = 'Converting ' + job.done + ' of ' + job.total + ' file(s) to Markdown';
    if (job.current_file) {
      text += ' - ' + job.current_file;
      if (job.current_progress) {
        text += ' (page ' + job.current_progress[0] + ' of ' + job.current_progress[1] + ')';
      }
    }
    label.textContent = text;

    if (job.status === 'complete') {
      let msg = 'Converted ' + job.converted.length + ' file(s)' +
                (fileCount > job.total ? ', ' + (fileCount - job.total) + ' saved as-is' : '') + '.';
      if (job.failed.length) {
        msg += ' ' + job.failed.length + ' failed and were kept as uploaded, unconverted: ' +
               job.failed.join('; ');
      }
      stat.textContent = msg;
      bar.style.display = 'none';
      return;
    }
    await new Promise(r => setTimeout(r, 500));
  }
}

document.querySelectorAll('form.upform').forEach(f => {
  const inp = f.querySelector('input[type=file]');
  const btn = f.querySelector('button');
  if (btn) btn.style.display = 'none';          // JS active: button not needed
  const stat = f.parentElement.querySelector('.upstat');
  const bar = f.parentElement.querySelector('.upprogress');
  const fill = f.parentElement.querySelector('.upprogress-fill');
  const label = f.parentElement.querySelector('.upprogress-label');
  inp.addEventListener('change', async () => {
    if (!inp.files.length) return;
    if (inp.disabled) return;   // this slot's own upload is still in flight - ignore a re-trigger
    const fileCount = inp.files.length;
    const fd = new FormData(f);   // capture BEFORE disabling - a disabled field is dropped from FormData
    stat.textContent = 'Uploading ' + fileCount + ' file(s)...';
    pendingUploads++;
    inp.disabled = true;
    try {
      const r = await fetch(f.action, { method: 'POST', body: fd });
      if (!r.ok) {
        stat.textContent = 'Upload failed (HTTP ' + r.status + ') - try again.';
      } else {
        const result = await r.json();
        if (result.job_id) {
          stat.textContent = '';
          bar.style.display = 'block';
          fill.style.width = '0%';
          await pollUploadJob(result.job_id, bar, fill, label, stat, fileCount);
        } else {
          stat.textContent = 'Uploaded ' + (result.saved_native || fileCount) + ' file(s).';
        }
      }
    } catch (e) { stat.textContent = 'Upload failed - ' + e; }
    inp.disabled = false;
    inp.value = '';
    pendingUploads--;
    if (pendingUploads === 0) setTimeout(() => location.reload(), 600);
  });
});
</script>
</body></html>"""


def page(title: str, body: str, active: str = ""):
    return render_template_string(PAGE, title=title, body=body, active=active)


# --------------------------------------------------------------------- views
@app.get("/")
def agency_picker():
    cases = list_cases()
    cards = ""
    taglines = {
        "ICRA": "India's original credit rating agency scale.",
        "CRISIL": "S&amp;P-affiliated; consolidated-master methodology set.",
        "CareEdge": "Formerly CARE Ratings; per-sector methodology papers.",
    }
    for a, cfg in AGENCIES.items():
        n_cases = sum(1 for c in cases if agency_of(c) == a)
        cards += f"""<a class="agency-card" href="{url_for('agency_dashboard', agency=a)}">
          <h2 style="margin-top:0">{a}</h2>
          <p class="mut">{taglines.get(a, '')}</p>
          <div class="mut">{n_cases} case{'s' if n_cases != 1 else ''} &middot;
            {_lib_counts(cfg['methodology'])} methodology files &middot;
            {_lib_counts(cfg['reports'])} reference rationales</div>
        </a>"""
    body = f"""
    <h1>Rating Agent</h1>
    <p class="mut">Choose which agency's rating you're working on. Each agency has its own
       methodology, house style, rating scale and case list.</p>
    <div class="agency-grid">{cards}</div>
    <p class="mut" style="margin-top:18px"><a href="{url_for('library')}">Browse the full reference library</a>
       across all three agencies without picking one first.</p>"""
    return page("Rating Agent", body, active="cases")


@app.get("/agency/<agency>")
def agency_dashboard(agency):
    if agency not in AGENCIES:
        abort(404)
    cases = [c for c in list_cases() if agency_of(c) == agency]
    rows = ""
    for c in cases:
        slug = c["slug"]
        cl = checklist_state(slug)
        req = [s for s in cl if s["required"]]
        done = sum(1 for s in req if s["done"])
        outs = find_outputs(c, slug)
        status = ('<span class="badge done">%d output file(s)</span>' % len(outs) if outs
                  else '<span class="badge req">rating requested</span>' if c.get("rating_requested")
                  else '<span class="badge opt">pending</span>')
        rows += f"""<tr>
          <td><a href="{url_for('company', slug=slug)}"><b>{h(c['name'])}</b></a>
              <div class="mut">{h(c.get('sector', c.get('entity_type','corporate').upper()))}</div></td>
          <td>{done}/{len(req)} required docs
              <div class="progress" style="max-width:140px"><i style="width:{int(done/len(req)*100)}%"></i></div></td>
          <td>{status}</td>
          <td>{_audit_badge(c)}</td>
        </tr>"""
    table = (f'<table><tr><th>Company</th><th>Document checklist</th>'
             f'<th>Rating output</th><th>Readiness</th></tr>{rows}</table>' if rows
             else f'<p class="mut">No {agency} rating cases yet - create one below.</p>')
    sector_options = "".join(
        '<optgroup label="{}">{}</optgroup>'.format(
            label, "".join(f'<option value="{s}">{s}</option>' for s in secs))
        for label, _cat, secs in AGENCY_SECTOR_GROUPS[agency])
    cfg = AGENCIES[agency]
    body = f"""
    <p><a href="{url_for('agency_picker')}">&larr; Switch agency</a></p>
    <h1>{agency} rating cases</h1>
    <p class="mut">{_lib_counts(cfg['methodology'])} methodology files &middot;
       {_lib_counts(cfg['reports'])} reference rationales &middot;
       <a href="{url_for('library_dir', agency=agency, kind='reports')}">browse {agency}'s library</a></p>
    <div class="card">{table}</div>
    <div class="card">
      <h2 style="margin-top:0"><span class="secnum">+</span> New {agency} rating case</h2>
      <form method="post" action="{url_for('create')}" class="rowform">
        <input type="hidden" name="agency" value="{agency}">
        <div style="flex:2 1 260px"><label class="field-label" for="nameInp">Company name</label>
          <input type="text" id="nameInp" name="name" placeholder="e.g. Titan Company Limited" required></div>
        <div style="flex:1 1 220px"><label class="field-label" for="sectorSel">Sector</label>
          <select name="sector" id="sectorSel">{sector_options}</select></div>
        <div style="flex:1 1 210px"><label class="field-label" for="basisSel">Analytical basis
          <span title="Dhampur Bio Organics, Sep-2026: rated CONSOLIDATED against the agency's
STANDALONE. Both bases are internally consistent, so every tie-out passed and mutation coverage
read 100% while the headline PAT was 22% off. No arithmetic check can separate them - the basis
has to be a recorded decision." style="cursor:help">&#9432;</span></label>
          <select name="basis" id="basisSel" required>
            <option value="" disabled selected>-- must choose --</option>
            <option value="standalone">Standalone</option>
            <option value="consolidated">Consolidated</option>
            <option value="combined">Combined</option>
            <option value="undecided">Decide at Step 5 (record why)</option>
          </select></div>
        <button class="btn" style="align-self:flex-end">Create case</button>
      </form>
      <div class="rowform" style="margin-top:10px; align-items:flex-end">
        <div style="flex:3 1 320px"><label class="field-label" for="descInp">What does the company do? (optional)</label>
          <input type="text" id="descInp" placeholder="e.g. manufactures cement and clinker, operates in Gujarat"
                 onkeydown="if(event.key==='Enter'){{event.preventDefault(); suggestSector();}}"></div>
        <button type="button" class="btn ghost" style="flex:0 0 auto" onclick="suggestSector()">Suggest sector</button>
      </div>
      <div id="sectorSuggest" class="mut" style="margin-top:8px; min-height:16px"></div>
      <p class="mut" style="margin-top:8px">Every case created here is a <b>{agency}</b> rating - the agent
         reads {agency}'s methodology, knowledge base and reference-report format, and rates on {agency}'s
         scale. <b>Sector</b> lists only what {agency}'s methodology library covers and sets the methodology
         the agent routes to. <b>Suggest sector</b> matches the company name/description against the sector
         list by keyword - pick a suggestion or leave the dropdown as-is if none fit.</p>
      <script>
        async function suggestSector() {{
          const name = document.getElementById('nameInp').value.trim();
          const desc = document.getElementById('descInp').value.trim();
          const out = document.getElementById('sectorSuggest');
          if (!name && !desc) {{ out.textContent = 'Enter a company name or a short description first.'; return; }}
          out.textContent = "Matching against {agency}'s sector list...";
          const fd = new FormData();
          fd.append('name', name); fd.append('description', desc); fd.append('agency', '{agency}');
          let data;
          try {{
            const r = await fetch('{url_for("suggest_sector_route")}', {{ method: 'POST', body: fd }});
            data = await r.json();
          }} catch (e) {{ out.textContent = 'Could not reach the suggestion service.'; return; }}
          const matches = data.matches || [];
          if (!matches.length) {{
            out.textContent = 'No confident sector match - pick manually from the dropdown.';
            return;
          }}
          const sel = document.getElementById('sectorSel');
          sel.value = matches[0].sector;
          out.innerHTML = 'Suggested: <b style="color:var(--navy)">' + matches[0].sector + '</b>' +
            (matches.length > 1 ? ' &nbsp;(also close: ' + matches.slice(1).map(m =>
              '<a href="#" onclick="document.getElementById(\\'sectorSel\\').value=this.textContent;return false;">'
              + m.sector + '</a>').join(', ') + ')' : '') +
            ' &mdash; confirm it looks right, then Create case.';
        }}
      </script>
    </div>"""
    return page(f"{agency} Cases", body, active="cases")


@app.post("/suggest-sector")
def suggest_sector_route():
    agency = request.form.get("agency", DEFAULT_AGENCY)
    if agency not in AGENCIES:
        agency = DEFAULT_AGENCY
    text = f"{request.form.get('name', '')} {request.form.get('description', '')}"
    matches = suggest_sectors(agency, text)
    return {"matches": [{"sector": s, "category": c, "score": sc} for s, c, sc in matches]}


@app.post("/create")
def create():
    name = request.form.get("name", "").strip()
    agency = request.form.get("agency", DEFAULT_AGENCY)
    if agency not in AGENCIES:
        agency = DEFAULT_AGENCY
    if not name:
        flash("Company name is required.")
        return redirect(url_for("agency_dashboard", agency=agency))
    slug = slugify(name)
    d = case_path(slug)
    sector_map = AGENCY_SECTOR_TO_CATEGORY[agency]
    sector = request.form.get("sector", "")
    if sector not in sector_map:                      # stale/foreign option
        sector = next(iter(sector_map))               # agency's first sector
    category = sector_map.get(sector, "corporate")
    # ANALYTICAL BASIS - mandatory at intake (added 13-Sep-2026).
    # R12 keeps the basis METHODOLOGY-determined, so this field does not let the operator
    # override the criteria; it forces the basis to be a RECORDED, checkable decision instead
    # of an unstated default. Dhampur Bio Organics was rated consolidated against the agency's
    # standalone while the report asserted "methodology-determined, not elective" - a prose
    # claim of compliance that every gate accepted AS compliance. check_sections.py now
    # cross-checks this value against the report and against the agency's own prior action.
    basis = request.form.get("basis", "").strip().lower()
    if basis not in ("standalone", "consolidated", "combined", "undecided"):
        flash("Analytical basis is required: pick standalone, consolidated, combined, or "
              "'decide at Step 5'. It is the one input that no tie-out can ever check for you.")
        return redirect(url_for("agency_dashboard", agency=agency))
    if (d / "case.json").exists():
        # apply the agency/sector picked on the form to the existing case
        case = load_case(slug)
        changed = []
        if agency_of(case) != agency:
            changed.append(f"agency -> {agency}")
        if case.get("sector") != sector:
            changed.append(f"sector -> {sector}")
        if basis != "undecided" and case.get("basis") != basis:
            changed.append(f"basis -> {basis}")
            case["basis"] = basis
        if changed:
            case["agency"] = agency
            case["sector"] = sector
            case["entity_type"] = category
            case["methodologies"] = suggest_methodologies(agency, sector, category)
            save_case(slug, case)
            write_context(slug)
            flash("A case for this company already exists - opened it and applied "
                  + ", ".join(changed) + " (methodology suggestions refreshed).")
        else:
            flash("A case for this company already exists - opened it.")
        return redirect(url_for("company", slug=slug))
    d.mkdir(parents=True, exist_ok=True)
    (d / "documents").mkdir(exist_ok=True)
    save_case(slug, {"name": name,
                     "agency": agency,
                     "sector": sector,
                     "entity_type": category,
                     # Recorded at intake so the basis is never an unstated default.
                     # "undecided" is an honest state and is allowed through creation, but the
                     # delivery gate refuses a rationale whose basis does not match this field.
                     "basis": basis,
                     "created": datetime.now().isoformat(timespec="seconds"),
                     "aliases": [a for a in [acronym(name)] if a],
                     "methodologies": suggest_methodologies(agency, sector, category),
                     "isins": [],
                     # Step 12 is mandatory in shape-appropriate form; this field is the ONLY
                     # sanctioned way to deliver a case without the model + scorecard, and
                     # check_sections.py refuses the case if both are absent and it is empty.
                     # Seeded blank so it is visible at intake rather than remembered later
                     # (failure mode 35 / R17 / R18).
                     "step12_scaling_decision": ""})
    write_context(slug)
    flash(f"Case created for {name}.")
    return redirect(url_for("company", slug=slug))


@app.get("/company/<slug>")
def company(slug):
    case = load_case(slug)
    if not (case_path(slug) / "COMPANY_CONTEXT.md").exists():
        write_context(slug)          # backfill for cases created before this feature
    cl = checklist_state(slug)

    slot_rows = ""
    for s in cl:
        tick = '<span class="tick ok">&#10003;</span>' if s["done"] else '<span class="tick no">&#9675;</span>'
        badge = ('<span class="badge done">complete</span>' if s["done"] else
                 '<span class="badge opt">optional</span>' if not s["required"] else "")
        files_html = "".join(
            f'<div>&#128196; <a href="{url_for("doc_file", slug=slug, slot=s["key"], fname=f.name)}">{f.name}</a> '
            f'<form style="display:inline" method="post" action="{url_for("delete_doc", slug=slug, slot=s["key"])}"'
            f' onsubmit="return confirm(\'Remove {f.name}?\')">'
            f'<input type="hidden" name="fname" value="{f.name}">'
            f'<button class="btn small danger">remove</button></form></div>'
            for f in s["files"]) or '<span class="mut">no files yet</span>'
        need = f' <span class="mut">({len(s["files"])}/{s["min_files"]} files)</span>' if s["min_files"] > 1 else ""
        slot_rows += f"""<tr>
          <td style="width:30px">{tick}</td>
          <td><b>{s['label']}</b>{need} {badge}<div class="mut">{s['hint']}</div>
              <div style="margin-top:6px">{files_html}</div></td>
          <td style="width:270px">
            <form method="post" action="{url_for('upload', slug=slug, slot=s['key'])}" enctype="multipart/form-data" class="rowform upform">
              <input type="file" name="files" multiple
                     accept=".pdf,.doc,.docx,.md,.markdown,.xlsx,.xls,.xlsm,.txt,.csv,.htm,.html">
              <button class="btn small">Upload</button>
            </form>
            <div class="upstat"></div>
            <div class="upprogress" style="display:none">
              <div class="upprogress-bar"><div class="upprogress-fill"></div></div>
              <div class="upprogress-label mut"></div>
            </div>
            <div class="mut">PDF, Word, text/CSV and HTML are converted to Markdown automatically;
               Excel and Markdown files are used as uploaded. Select several at once (Ctrl-click),
               or add more later.</div>
          </td></tr>"""

    isin_rows = ""
    for i, ins in enumerate(case.get("isins", [])):
        tick = '<span class="tick ok">&#10003;</span>' if ins.get("uploaded") else '<span class="tick no">&#9675;</span>'
        isin_rows += f"""<tr>
          <td style="width:30px">{tick}</td>
          <td><code>{h(ins['isin'] or '-')}</code></td><td>{h(ins['name'])}</td>
          <td>{h(ins['amount'] or '-')}</td>
          <td style="width:230px">
            <form style="display:inline" method="post" action="{url_for('toggle_isin', slug=slug, idx=i)}">
              <button class="btn small ghost">{'Untick' if ins.get('uploaded') else 'Tick as uploaded'}</button></form>
            <form style="display:inline" method="post" action="{url_for('delete_isin', slug=slug, idx=i)}"
                  onsubmit="return confirm('Delete this instrument?')">
              <button class="btn small danger">delete</button></form></td></tr>"""
    isin_table = (f'<table><tr><th></th><th>ISIN</th><th>Instrument</th>'
                  f'<th>Rated amount (Rs. crore)</th><th></th></tr>{isin_rows}</table>'
                  if isin_rows else '<p class="mut">No instruments added yet.</p>')

    outs = find_outputs(case, slug)
    _auto_clear_delivered_requests(case, slug, outs)
    out_rows = "".join(
        f"""<tr><td><span class="badge {'done' if o['kind']=='Rating Rationale' else 'opt'}">{o['kind']}</span></td>
        <td>{'<a href="' + url_for('view_output', rel=o['rel']) + '">' + o['path'].name + '</a>'
             if o['path'].suffix == '.md' else
             '<a href="' + url_for('raw_output', rel=o['rel']) + '">' + o['path'].name + '</a>'}</td>
        <td class="mut">{o['mtime'].strftime('%d %b %Y %H:%M')}</td>
        <td><a class="btn small ghost" href="{url_for('raw_output', rel=o['rel'])}">download</a></td></tr>"""
        for o in outs)
    out_table = (f'<table><tr><th>Type</th><th>File</th><th>Modified</th><th></th></tr>{out_rows}'
                 '</table>' if out_rows else
                 '<p class="mut">No output yet - follow the steps in section 4. The rationale, workpaper or '
                 'research note the agent saves will appear here automatically (click Refresh after the run).</p>')

    req_flag = case.get("rating_requested")
    if req_flag:
        request_html = f"""<div class="reqbox">&#9203; <b>Rating requested</b> on {req_flag[:16].replace('T',' ')} -
          request saved to <code>Companies/{slug}/RATING_REQUEST.md</code>.
          In a Claude session on this project say: <i>"process the pending rating requests"</i>.
          <form style="display:inline" method="post" action="{url_for('cancel_request', slug=slug)}">
            <button class="btn small danger">Cancel request</button></form></div>"""
    else:
        request_html = f"""<form method="post" action="{url_for('request_rating', slug=slug)}" style="display:inline">
          <button class="btn ghost">Request rating (save request file)</button></form>"""

    res_flag = case.get("research_requested")
    if res_flag:
        research_html = f"""<div class="reqbox">&#128269; <b>Research requested</b> on {res_flag[:16].replace('T',' ')} -
          request saved to <code>Companies/{slug}/RESEARCH_REQUEST.md</code>.
          In a Claude session say: <i>"process the pending research requests"</i> (finance-research skill).
          <form style="display:inline" method="post" action="{url_for('cancel_research', slug=slug)}">
            <button class="btn small danger">Cancel</button></form></div>"""
    else:
        research_html = f"""<form method="post" action="{url_for('request_research', slug=slug)}" style="display:inline">
          <button class="btn ghost">Request research (fact pack, no rating)</button></form>"""

    agency = agency_of(case)
    all_meth = list_methodology(agency)
    selected = set(selected_methodologies(case))
    suggested = set(suggest_methodologies(agency, case.get("sector", ""),
                                          case.get("entity_type", "corporate")))
    meth_rows = "".join(
        f"""<label style="display:block; padding:3px 6px; border-radius:5px;
              background:{'#e2f3e6' if m in selected else 'transparent'}" class="methrow">
           <input type="checkbox" name="meth" value="{m}"{' checked' if m in selected else ''}>
           {m}{' <span class="badge opt">suggested</span>' if m in suggested else ''}</label>"""
        for m in sorted(all_meth, key=lambda m: (m not in selected, m not in suggested, m.lower())))
    meth_card = f"""
    <div class="card" id="sec2"><h2 style="margin-top:0"><span class="secnum">2</span> Applicable methodology
        <span class="badge done">{agency}</span></h2>
      <p class="mut">Only the ticked files are named in the kickoff prompt - the agent reads those
         (plus cross-cutting/policy criteria) instead of routing through the whole folder.
         Sector-relevant files were pre-selected from <b>{case.get('sector','-')}</b>;
         tick as many as apply, e.g. a sector paper AND the base master AND a support/notching paper.
         Changing the agency re-suggests this list.</p>
      <form method="post" action="{url_for('save_methodologies', slug=slug)}">
        <input type="text" id="methfilter" placeholder="filter files..." style="max-width:340px; margin-bottom:8px"
               onkeyup="filtMeth(this.value)">
        <div style="max-height:280px; overflow:auto; border:1px solid var(--line); border-radius:8px; padding:8px" id="methlist">
          {meth_rows or '<span class="mut">No methodology files for this agency yet.</span>'}
        </div>
        <p style="margin-top:10px"><button class="btn">Save methodology selection</button>
           <span class="mut">{len(selected)} selected</span></p>
      </form></div>"""

    sess_prompt = session_prompt(case, slug)
    prompt = kickoff_prompt(case, slug)
    safe_name = h(case['name'])
    aliases_val = h(", ".join(case.get("aliases", [])))

    a = case.get("audit")
    if a:
        check_rows = "".join(
            '<tr><td style="width:28px">%s</td><td><b>%s</b><div class="mut">%s</div></td></tr>'
            % ('<span class="tick ok">&#10003;</span>' if c["ok"] is True
               else '<span class="mut">&ndash;</span>' if c["ok"] is None
               else '<span class="tick no" style="color:#c0392b">&#10007;</span>',
               h(c["name"]), h((c.get("detail") or "")[:220]))
            for c in a.get("checks", []))
        verdict = ('<span class="badge done">READY TO SHARE &#10003;</span>' if a.get("ready")
                   else '<span class="badge req">NOT READY - do not deliver</span>')
        audit_inner = (
            f'<p>{verdict} <span class="mut">last checked '
            f'{h((a.get("checked_at") or "")[:16].replace("T", " "))}</span></p>'
            f'<table>{check_rows}</table>')
    else:
        audit_inner = ('<p class="mut">Not checked yet. Runs the same gates as '
                       '<code>delivery_audit.py</code> - tie-outs, mutation coverage, '
                       'section/quality, scorecard match, workpaper, Step-14 diff - and shows one '
                       'READY / NOT READY verdict.</p>')
    audit_card = f"""
    <div class="card" id="sec7"><h2 style="margin-top:0"><span class="secnum">7</span> Delivery readiness
        <form method="post" action="{url_for('run_audit', slug=slug)}" style="float:right; display:inline">
          <button class="btn small">Check readiness</button></form></h2>
      {audit_inner}
      <p class="mut" style="margin-top:8px">A scored case runs several sub-checks and can take a
         little while. This reads files only - it never spends API budget.</p></div>"""
    body = f"""
    <p><a href="{url_for('agency_dashboard', agency=agency_of(case))}">&larr; {agency_of(case)} cases</a></p>
    <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:12px; flex-wrap:wrap">
      <div>
        <h1>{safe_name}</h1>
        <p class="mut"><span class="badge done">{h(agency_of(case))}</span>
           &middot; {h(case.get('sector', case.get('entity_type','corporate').upper()))}
           &middot; routing: {h(case.get('entity_type','corporate'))} &middot; created {h(case.get('created','')[:10])}</p>
        <form method="post" action="{url_for('set_agency', slug=slug)}" class="rowform" style="max-width:340px">
          <select name="agency" style="flex:0 1 150px" onchange="this.form.submit()">{''.join(
              f'<option value="{a}"{" selected" if a == agency_of(case) else ""}>{a}</option>'
              for a in AGENCIES)}</select>
          <button class="btn small ghost">Change agency</button>
        </form>
      </div>
      <form method="post" action="{url_for('delete_case', slug=slug)}"
            onsubmit="return confirm('Delete the case for {safe_name}? This removes its uploaded documents and checklist. Any rating report/workpaper already saved to the project folder is NOT deleted.')">
        <button class="btn danger small">Delete case</button>
      </form>
    </div>
    <nav class="jumpnav">
      <a href="#sec1">1 &middot; Documents</a>
      <a href="#sec2">2 &middot; Methodology</a>
      <a href="#sec3">3 &middot; Instruments</a>
      <a href="#sec4">4 &middot; Session</a>
      <a href="#sec5">5 &middot; Get output</a>
      <a href="#sec6">6 &middot; Output</a>
      <a href="#sec7">7 &middot; Readiness</a>
    </nav>

    <div class="card" id="sec1"><h2 style="margin-top:0"><span class="secnum">1</span> Required documents</h2>
      <table>{slot_rows}</table></div>

    {meth_card}

    <div class="card" id="sec3"><h2 style="margin-top:0"><span class="secnum">3</span> Instruments (ISIN checklist)</h2>
      <p class="mut">Add <b>every</b> instrument to be rated - one row per ISIN; a company can have any number.
         To add several ISINs of the same type in one go, paste them comma-separated in the ISIN box.
         Tick each row once its term sheet / sanction letter is uploaded.</p>
      {isin_table}
      <form method="post" action="{url_for('add_isin', slug=slug)}" class="rowform" style="margin-top:12px">
        <input type="text" name="isin" placeholder="ISIN(s) - e.g. INE467B01029 or several, comma-separated">
        <input type="text" name="iname" placeholder="Instrument (e.g. NCD programme)">
        <input type="text" name="amount" placeholder="Rated amount, Rs. crore">
        <button class="btn">Add instrument(s)</button>
      </form></div>

    <div class="card" id="sec4"><h2 style="margin-top:0"><span class="secnum">4</span> Dedicated company session <span class="badge opt" style="font-weight:600">recommended</span></h2>
      <p class="mut">Give <b>{safe_name}</b> its own context window so the company - and the memory of its
         documents - stays in one place. Open the Claude app &rarr; start a <b>new chat/session</b> on the
         <code>Credit Rating</code> project &rarr; paste this as the first message. The session loads
         <code>Companies/{slug}/COMPANY_CONTEXT.md</code> (kept current by this app), reads every document
         one by one (Step 1b), and then holds all work for this company - so it can go back into the
         documents whenever needed. Alternatively, in an existing session say
         <i>"start a dedicated session for {safe_name}"</i> and the agent will spawn one.</p>
      <textarea id="sesskick" class="prompt" readonly>{h(sess_prompt)}</textarea>
      <p style="margin-top:8px">
        <button id="sesscopybtn" class="btn" onclick="copySession()">Copy session prompt</button>
      </p></div>

    <div class="card" id="sec5"><h2 style="margin-top:0"><span class="secnum">5</span> Get the output (rating or research)</h2>
      <ol class="steps">
        <li>Finish uploading the required documents above (green ticks).</li>
        <li>Click <b>Copy prompt</b> and paste it into the company's dedicated session (section 4) -
            or click <b>Request rating</b> / <b>Request research</b> and later tell Claude to
            <i>"process the pending rating requests"</i> / <i>"process the pending research requests"</i>.</li>
        <li>The agent runs the 19-step SOP (rating) or the fact-pack process (research), pauses for your
            sign-off where required, then saves the deliverables - they appear in section 6 below.</li>
      </ol>
      <textarea id="kickoff" class="prompt" readonly>{h(prompt)}</textarea>
      <p style="margin-top:8px">
        <button id="copybtn" class="btn" onclick="copyPrompt()">Copy prompt</button>
        {request_html}
        {research_html}
      </p></div>

    <div class="card" id="sec6"><h2 style="margin-top:0"><span class="secnum">6</span> Output - rationale, workpaper &amp; research
        <button class="btn small ghost" style="float:right" onclick="location.reload()">Refresh</button></h2>
      {out_table}
      <p class="mut" style="margin-top:10px">Files are matched by company name or alias. Aliases:</p>
      <form method="post" action="{url_for('save_aliases', slug=slug)}" class="rowform" style="max-width:520px">
        <input type="text" name="aliases" value="{aliases_val}" placeholder="e.g. SBI, State Bank">
        <button class="btn small ghost">Save aliases</button>
      </form></div>
    {audit_card}"""
    return page(case["name"], body, active="cases")


def _unique_path(d: Path, name: str) -> Path:
    """Atomically claim a not-yet-used filename in `d` and return it, already created (empty).

    The previous version checked `dest.exists()` and returned the name for the CALLER to write
    later - a classic TOCTOU gap. Two uploads landing close together (a re-upload, two files
    that happen to share a stem, or simply two concurrent requests, which the threaded dev
    server allows) could both see the name as free and both write to it, with the second write
    silently clobbering the first. Reproduced directly: four threads racing this function for
    the same name all got the identical path back, and 3 of 4 "uploads" vanished, leaving only
    the last writer's content - exactly the intermittent "sometimes the document is there,
    sometimes it isn't" the operator reported. `os.O_CREAT | os.O_EXCL` makes the claim atomic
    at the OS level: at most one thread can ever succeed for a given name, so every caller
    (f.save(), write_text()) is writing into a name it alone reserved - collapsing the race to
    the increment-and-retry loop, not a check on a shared, mutable filesystem.
    """
    import os as _os
    dest = d / name
    stem, suffix = dest.stem, dest.suffix
    i = 1
    while True:
        try:
            fd = _os.open(str(dest), _os.O_CREAT | _os.O_EXCL | _os.O_WRONLY)
            _os.close(fd)
            return dest
        except FileExistsError:
            i += 1
            dest = d / f"{stem} ({i}){suffix}"


def _run_upload_conversion(job_id: str, tasks: list[dict]) -> None:
    """Convert each queued file to Markdown, updating UPLOAD_JOBS as it goes.

    `tasks` items: {"src": Path (in originals/), "dest_dir": Path, "stem": str}. The raw file
    stays in originals/ regardless of outcome - conversion never deletes the source, so a
    failed or imperfect conversion can always be redone or read by a person.
    """
    with UPLOAD_JOBS_LOCK:
        UPLOAD_JOBS[job_id]["status"] = "running"

    for idx, task in enumerate(tasks):
        src, dest_dir, stem = task["src"], task["dest_dir"], task["stem"]
        with UPLOAD_JOBS_LOCK:
            UPLOAD_JOBS[job_id]["current_file"] = src.name

        def _cb(done, total, _job_id=job_id, _idx=idx, _name=src.name):
            with UPLOAD_JOBS_LOCK:
                UPLOAD_JOBS[_job_id]["current_file"] = _name
                UPLOAD_JOBS[_job_id]["current_progress"] = (done, total)

        try:
            markdown = doc_convert.convert(src, _cb)
            out_path = _unique_path(dest_dir, stem + ".md")
            out_path.write_text(markdown, encoding="utf-8")
            with UPLOAD_JOBS_LOCK:
                UPLOAD_JOBS[job_id]["done"] += 1
                UPLOAD_JOBS[job_id]["converted"].append(out_path.name)
        except Exception as e:                                            # noqa: BLE001
            with UPLOAD_JOBS_LOCK:
                UPLOAD_JOBS[job_id]["done"] += 1
                UPLOAD_JOBS[job_id]["failed"].append(
                    "%s (%s)" % (src.name, str(e)[:120]))

    with UPLOAD_JOBS_LOCK:
        UPLOAD_JOBS[job_id]["status"] = "complete"


@app.post("/company/<slug>/upload/<slot>")
def upload(slug, slot):
    """Accept any file type. Markdown/Excel land in the slot folder as-is; everything this
    project knows how to read (PDF, Word, txt/csv, HTML) is converted to Markdown in the
    background, with the raw file kept in documents/<slot>/originals/ for provenance. A type
    with no converter is saved directly in the slot folder, same as before this feature -
    nothing the operator uploads is ever rejected or silently dropped.
    """
    load_case(slug)
    if slot not in SLOT_KEYS:
        abort(404)
    d = case_path(slug) / "documents" / slot
    originals = d / "originals"
    d.mkdir(parents=True, exist_ok=True)

    saved_native = 0
    tasks = []
    for f in request.files.getlist("files"):
        if not f or not f.filename:
            continue
        name = secure_filename(f.filename)
        ext = Path(name).suffix.lower()
        if doc_convert.is_native(Path(name)) or ext not in doc_convert.CONVERTIBLE_EXTS:
            # Native (.md/.xlsx) or a type this tool has no converter for - saved directly,
            # exactly as every upload was handled before this feature existed.
            dest = _unique_path(d, name)
            f.save(dest)
            saved_native += 1
        else:
            originals.mkdir(parents=True, exist_ok=True)
            raw_dest = _unique_path(originals, name)
            f.save(raw_dest)
            tasks.append({"src": raw_dest, "dest_dir": d, "stem": Path(name).stem})

    write_context(slug)

    if not tasks:
        flash(f"Uploaded {saved_native} file(s).")
        return jsonify({"job_id": None, "saved_native": saved_native})

    job_id = uuid.uuid4().hex
    with UPLOAD_JOBS_LOCK:
        UPLOAD_JOBS[job_id] = {
            "status": "queued", "total": len(tasks), "done": 0,
            "converted": [], "failed": [], "current_file": None,
            "current_progress": None, "slug": slug,
        }
    threading.Thread(target=_run_upload_conversion, args=(job_id, tasks),
                      daemon=True).start()
    return jsonify({"job_id": job_id, "saved_native": saved_native, "to_convert": len(tasks)})


@app.get("/upload-progress/<job_id>")
def upload_progress(job_id):
    with UPLOAD_JOBS_LOCK:
        job = UPLOAD_JOBS.get(job_id)
        if job is None:
            return jsonify({"status": "unknown"}), 404
        out = dict(job)
    if out["status"] == "complete":
        # Re-run write_context now that the converted .md files exist, so the case's
        # COMPANY_CONTEXT.md (and anything that reads it) reflects the new documents without
        # the operator needing to trigger a separate action.
        write_context(out["slug"])
        with UPLOAD_JOBS_LOCK:
            UPLOAD_JOBS.pop(job_id, None)             # jobs are short-lived; don't leak memory
    return jsonify(out)


@app.post("/company/<slug>/delete/<slot>")
def delete_doc(slug, slot):
    load_case(slug)
    if slot not in SLOT_KEYS:
        abort(404)
    d = case_path(slug) / "documents" / slot
    target = d / secure_filename(request.form.get("fname", ""))
    if target.is_file():
        target.unlink()
        # A converted .md has a raw source of the SAME STEM sitting in originals/ under
        # some other extension - remove it too, or deleting the processed document leaves an
        # orphaned raw file with no UI to ever find or clean it up again.
        originals = d / "originals"
        if originals.is_dir():
            for sibling in originals.glob(target.stem + ".*"):
                sibling.unlink()
        write_context(slug)
        flash("File removed.")
    return redirect(url_for("company", slug=slug))


@app.get("/company/<slug>/file/<slot>/<path:fname>")
def doc_file(slug, slot, fname):
    load_case(slug)
    target = case_path(slug) / "documents" / slot / secure_filename(fname)
    if not target.is_file():
        abort(404)
    return send_file(target)


@app.post("/company/<slug>/isin")
def add_isin(slug):
    case = load_case(slug)
    isin_raw = request.form.get("isin", "").strip().upper()
    name = request.form.get("iname", "").strip() or "-"
    amount = request.form.get("amount", "").strip()
    isins = [t for t in re.split(r"[,\s;]+", isin_raw) if t] or [""]
    if isin_raw or name != "-":
        for tok in isins:
            case.setdefault("isins", []).append(
                {"isin": tok, "name": name, "amount": amount, "uploaded": False})
        save_case(slug, case)
        write_context(slug)
        flash(f"Added {len(isins)} instrument(s).")
    else:
        flash("Enter at least an ISIN or an instrument name.")
    return redirect(url_for("company", slug=slug))


@app.post("/company/<slug>/isin/<int:idx>/toggle")
def toggle_isin(slug, idx):
    case = load_case(slug)
    if 0 <= idx < len(case.get("isins", [])):
        case["isins"][idx]["uploaded"] = not case["isins"][idx].get("uploaded")
        save_case(slug, case)
        write_context(slug)
    return redirect(url_for("company", slug=slug))


@app.post("/company/<slug>/isin/<int:idx>/delete")
def delete_isin(slug, idx):
    case = load_case(slug)
    if 0 <= idx < len(case.get("isins", [])):
        case["isins"].pop(idx)
        save_case(slug, case)
        write_context(slug)
    return redirect(url_for("company", slug=slug))


@app.post("/company/<slug>/agency")
def set_agency(slug):
    case = load_case(slug)
    agency = request.form.get("agency", DEFAULT_AGENCY)
    if agency not in AGENCIES:
        agency = DEFAULT_AGENCY
    case["agency"] = agency
    # filenames differ per agency: re-suggest the methodology selection
    case["methodologies"] = suggest_methodologies(
        agency, case.get("sector", ""), case.get("entity_type", "corporate"))
    save_case(slug, case)
    write_context(slug)
    # keep an already-saved rating request consistent with the new agency
    req = case_path(slug) / "RATING_REQUEST.md"
    if case.get("rating_requested") and req.is_file():
        req.write_text(
            f"# Rating request - {case['name']}\n\nRequested: {case['rating_requested']}\n"
            f"Status: PENDING\n\nInstructions for the rating agent:\n\n"
            f"```\n{kickoff_prompt(case, slug)}\n```\n\n"
            "When the rating is delivered, delete this file (or set Status: DONE).\n",
            encoding="utf-8")
    flash(f"Agency set to {agency}. Prompts and request files now route to "
          f"{agency}'s methodology.")
    return redirect(url_for("company", slug=slug))


@app.post("/company/<slug>/methodologies")
def save_methodologies(slug):
    case = load_case(slug)
    valid = set(list_methodology(agency_of(case)))
    case["methodologies"] = [m for m in request.form.getlist("meth") if m in valid]
    save_case(slug, case)
    write_context(slug)
    # keep an already-saved rating request consistent with the new selection
    req = case_path(slug) / "RATING_REQUEST.md"
    if case.get("rating_requested") and req.is_file():
        req.write_text(
            f"# Rating request - {case['name']}\n\nRequested: {case['rating_requested']}\n"
            f"Agency: {agency_of(case)}\nStatus: PENDING\n\n"
            f"Instructions for the rating agent:\n\n```\n{kickoff_prompt(case, slug)}\n```\n\n"
            "When the rating is delivered, delete this file (or set Status: DONE).\n",
            encoding="utf-8")
    flash(f"Methodology selection saved ({len(case['methodologies'])} file(s)).")
    return redirect(url_for("company", slug=slug))


@app.post("/company/<slug>/aliases")
def save_aliases(slug):
    case = load_case(slug)
    case["aliases"] = [a.strip() for a in request.form.get("aliases", "").split(",")
                       if len(a.strip()) >= 2]
    save_case(slug, case)
    write_context(slug)
    flash("Aliases saved.")
    return redirect(url_for("company", slug=slug))


@app.post("/company/<slug>/request")
def request_rating(slug):
    case = load_case(slug)
    now = datetime.now().isoformat(timespec="seconds")
    case["rating_requested"] = now
    save_case(slug, case)
    (case_path(slug) / "RATING_REQUEST.md").write_text(
        f"# Rating request - {case['name']}\n\nRequested: {now}\n"
        f"Agency: {agency_of(case)}\nStatus: PENDING\n\n"
        f"Instructions for the rating agent:\n\n```\n{kickoff_prompt(case, slug)}\n```\n\n"
        "When the rating is delivered, delete this file (or set Status: DONE).\n",
        encoding="utf-8")
    write_context(slug)
    flash("Rating request saved. Tell Claude: \"process the pending rating requests\".")
    return redirect(url_for("company", slug=slug))


@app.post("/company/<slug>/request/cancel")
def cancel_request(slug):
    case = load_case(slug)
    case.pop("rating_requested", None)
    save_case(slug, case)
    f = case_path(slug) / "RATING_REQUEST.md"
    if f.is_file():
        f.unlink()
    write_context(slug)
    flash("Rating request cancelled.")
    return redirect(url_for("company", slug=slug))


@app.post("/company/<slug>/research")
def request_research(slug):
    case = load_case(slug)
    now = datetime.now().isoformat(timespec="seconds")
    case["research_requested"] = now
    save_case(slug, case)
    body = (
        f"# Research request - {case['name']}\n\n"
        f"Requested: {now}\nStatus: PENDING\n\n"
        "Instructions for the finance-research skill: build the research fact pack (NO rating).\n\n"
        f"```\nResearch company: {case['name']}.\n"
        f"Load Companies/{slug}/COMPANY_CONTEXT.md, read every document in "
        f"Companies/{slug}/documents/ one by one (Step 1b), and deliver "
        f"{case['name']}_Research_Note_<date>.md to the project root.\n```\n\n"
        "When delivered, delete this file (or set Status: DONE).\n")
    (case_path(slug) / "RESEARCH_REQUEST.md").write_text(body, encoding="utf-8")
    write_context(slug)
    flash("Research request saved. Tell Claude: \"process the pending research requests\".")
    return redirect(url_for("company", slug=slug))


@app.post("/company/<slug>/research/cancel")
def cancel_research(slug):
    case = load_case(slug)
    case.pop("research_requested", None)
    save_case(slug, case)
    f = case_path(slug) / "RESEARCH_REQUEST.md"
    if f.is_file():
        f.unlink()
    write_context(slug)
    flash("Research request cancelled.")
    return redirect(url_for("company", slug=slug))


@app.post("/company/<slug>/delete")
def delete_case(slug):
    case = load_case(slug)                 # 404s if it doesn't exist
    name = case.get("name", slug)
    agency = agency_of(case)
    d = case_path(slug)                    # path-traversal guarded in case_path
    if d.is_dir() and d != CASES_DIR:
        shutil.rmtree(d, ignore_errors=True)
    flash(f'Case "{name}" deleted. Any saved report/workpaper in the project '
          "folder was left untouched.")
    return redirect(url_for("agency_dashboard", agency=agency))


def _safe_output(rel: str) -> Path:
    p = (ROOT / rel).resolve()
    if not str(p).startswith(str(ROOT.resolve())) or not p.is_file():
        abort(404)
    return p


@app.get("/output/view/<path:rel>")
def view_output(rel):
    p = _safe_output(rel)
    if p.suffix.lower() != ".md":
        return send_file(p)
    html = md_lib.markdown(p.read_text(encoding="utf-8", errors="replace"),
                           extensions=["tables", "fenced_code"])
    body = f"""<p><a href="javascript:history.back()">&larr; Back</a>
      &middot; <a href="{url_for('raw_output', rel=rel)}">download raw .md</a></p>
      <div class="card md">{html}</div>"""
    return page(p.stem, body)


@app.get("/output/raw/<path:rel>")
def raw_output(rel):
    return send_file(_safe_output(rel), as_attachment=True)


# ----------------------------------------------------- reference library
def _lib_counts(dir_rel: str) -> int:
    d = (ROOT / dir_rel)
    return sum(1 for p in d.iterdir() if p.is_file()) if d.is_dir() else 0


@app.get("/process")
def process_flow():
    """The rating SOP as a flowchart: five phases, six gates, and where each failure loops.

    The chart is a self-contained page in static/ (its own fonts, tokens and dark mode), so it
    is framed rather than inlined - inlining would let its :root and body styles collide with
    this layout's. The frame is sized to its content so the page scrolls as one document.
    """
    src = url_for("static", filename="credit_rating_pipeline.html")
    body = f"""<iframe id="flow" src="{src}" title="Credit rating pipeline"
      style="width:100%;border:0;display:block;min-height:900px"
      onload="try{{this.style.height=this.contentDocument.documentElement.scrollHeight+'px'}}catch(e){{}}"></iframe>
    <p class="mut" style="margin-top:8px"><a href="{src}" target="_blank" rel="noopener">Open the chart on its own page</a></p>"""
    return page("Process Flow", body, active="process")


@app.get("/library")
def library():
    rows = ""
    for name, cfg in AGENCIES.items():
        m, r, k = (_lib_counts(cfg["methodology"]), _lib_counts(cfg["reports"]),
                   _lib_counts(cfg["kb"]))
        rows += f"""<tr>
          <td><b>{name}</b></td>
          <td><a href="{url_for('library_dir', agency=name, kind='methodology')}">{m}</a> methodology files</td>
          <td><a href="{url_for('library_dir', agency=name, kind='reports')}">{r}</a> reference rationales</td>
          <td><a href="{url_for('library_dir', agency=name, kind='kb')}">{k}</a> knowledge-base files</td>
        </tr>"""
    body = f"""
    <h1>Reference Library</h1>
    <p class="mut">Methodology documents, published rating rationales (craft reference) and knowledge-base
       files for each agency. ICRA lives at the project root; CRISIL and CareEdge in their own folders.
       Drop new files straight into the folders on disk - counts refresh on reload.</p>
    <form method="get" action="{url_for('library_search')}" class="rowform" style="max-width:520px">
      <input type="text" name="q" placeholder="search all agencies by filename / issuer, e.g. Titan">
      <button class="btn">Search all libraries</button></form>
    <div class="card"><table>
      <tr><th>Agency</th><th>Methodology</th><th>Reference rationales</th><th>Knowledge base</th></tr>
      {rows}
    </table></div>
    <p class="mut">Folder map &amp; how to produce a report per agency: see <code>AGENCIES.md</code> at the project root.</p>"""
    return page("Reference Library", body, active="library")


@app.get("/library/search")
def library_search():
    """One search box across all three agencies and all three kinds - by file name / issuer.

    Per-agency filtering already exists inside library_dir (?q=); this is the global version, so
    an issuer that is rated by more than one agency doesn't have to be looked up three times.
    """
    qraw = request.args.get("q", "").strip()
    q = qraw.lower()
    rows, total = "", 0
    labels = {"reports": "reference", "methodology": "methodology", "kb": "knowledge base"}
    if len(q) >= 2:
        for agency, cfg in AGENCIES.items():
            for kind in ("reports", "methodology", "kb"):
                d = ROOT / cfg[kind]
                if not d.is_dir():
                    continue
                for p in sorted(d.iterdir()):
                    if not (p.is_file() and q in p.name.lower()):
                        continue
                    total += 1
                    link = (url_for('library_view', agency=agency, kind=kind, fname=p.name)
                            if p.suffix.lower() == '.md'
                            else url_for('library_raw', agency=agency, kind=kind, fname=p.name))
                    rows += (f'<tr><td><a href="{link}">{h(p.name)}</a></td>'
                             f'<td><span class="badge opt">{agency}</span></td>'
                             f'<td class="mut">{labels[kind]}</td>'
                             f'<td class="mut">{p.stat().st_size // 1024} KB</td></tr>')
    if rows:
        inner = (f'<p class="mut">{total} match(es).</p>'
                 f'<table><tr><th>File</th><th>Agency</th><th>Kind</th><th>Size</th></tr>{rows}</table>')
    elif len(q) >= 2:
        inner = '<p class="mut">No matches.</p>'
    else:
        inner = '<p class="mut">Type at least 2 characters.</p>'
    body = f"""
    <p><a href="{url_for('library')}">&larr; Reference Library</a></p>
    <h1>Search all libraries</h1>
    <form method="get" class="rowform" style="max-width:520px">
      <input type="text" name="q" value="{h(qraw)}" placeholder="issuer or filename, e.g. Titan" autofocus>
      <button class="btn">Search</button></form>
    <p class="mut">File-name search across ICRA, CRISIL and CareEdge - methodology, reference
       rationales and knowledge base.</p>
    <div class="card">{inner}</div>"""
    return page("Search libraries", body, active="library")


@app.get("/library/<agency>/<kind>")
def library_dir(agency, kind):
    cfg = AGENCIES.get(agency)
    if not cfg or kind not in ("methodology", "reports", "kb"):
        abort(404)
    d = ROOT / cfg[kind]
    label = {"methodology": "Methodology", "reports": "Reference rationales",
             "kb": "Knowledge base"}[kind]
    files = sorted(p for p in d.iterdir() if p.is_file()) if d.is_dir() else []
    q = request.args.get("q", "").strip().lower()
    if q:
        files = [p for p in files if q in p.name.lower()]
    rows = "".join(
        f"""<tr><td>{'<a href="' + url_for('library_view', agency=agency, kind=kind, fname=p.name) + '">' + p.name + '</a>'
             if p.suffix.lower() == '.md'
             else '<a href="' + url_for('library_raw', agency=agency, kind=kind, fname=p.name) + '">' + p.name + '</a>'}</td>
        <td class="mut">{p.stat().st_size // 1024} KB</td>
        <td><a class="btn small ghost" href="{url_for('library_raw', agency=agency, kind=kind, fname=p.name)}">download</a></td></tr>"""
        for p in files)
    table = (f'<table><tr><th>File</th><th>Size</th><th></th></tr>{rows}</table>' if rows
             else f'<p class="mut">No files yet. Drop {agency} {label.lower()} into '
                  f'<code>{cfg[kind]}/</code>.</p>')
    body = f"""
    <p><a href="{url_for('library')}">&larr; Reference Library</a></p>
    <h1>{agency} &middot; {label}</h1>
    <form method="get" class="rowform" style="max-width:420px">
      <input type="text" name="q" value="{q}" placeholder="filter by filename...">
      <button class="btn small ghost">Filter</button></form>
    <div class="card">{table}</div>"""
    return page(f"{agency} {label}", body, active="library")


def _safe_lib(agency, kind, fname) -> Path:
    cfg = AGENCIES.get(agency)
    if not cfg or kind not in ("methodology", "reports", "kb"):
        abort(404)
    base = (ROOT / cfg[kind]).resolve()
    # Use the basename only (block traversal) but preserve spaces/real chars.
    p = (base / Path(fname).name).resolve()
    if not str(p).startswith(str(base)) or not p.is_file():
        abort(404)
    return p


@app.get("/library/<agency>/<kind>/view/<path:fname>")
def library_view(agency, kind, fname):
    p = _safe_lib(agency, kind, fname)
    if p.suffix.lower() != ".md":
        return send_file(p)
    html = md_lib.markdown(p.read_text(encoding="utf-8", errors="replace"),
                           extensions=["tables", "fenced_code"])
    body = f"""<p><a href="{url_for('library_dir', agency=agency, kind=kind)}">&larr; {agency}</a>
      &middot; <a href="{url_for('library_raw', agency=agency, kind=kind, fname=fname)}">download raw</a></p>
      <div class="card md">{html}</div>"""
    return page(p.stem, body)


@app.get("/library/<agency>/<kind>/raw/<path:fname>")
def library_raw(agency, kind, fname):
    return send_file(_safe_lib(agency, kind, fname), as_attachment=True)


def _e(value) -> str:
    """Escape, returning a plain str - NOT a Markup.

    markupsafe's Markup.__add__ escapes whatever is on the other side of the +, so building
    HTML by concatenating h(...) with literal markup escapes the markup you just wrote and the
    page renders as visible angle brackets. The rest of this file gets away with h() because it
    uses f-strings, where __format__ hands back a plain str before concatenation happens.
    """
    return str(h(value))


# --------------------------------------------------------------------- settings
# The API key had no home in this app: rate_engine.py accepted one on the command line or from
# an environment variable, neither of which is reachable from a browser, so anyone driving the
# tool through this UI had no way to supply a credential at all.
#
# rate_engine is imported lazily, inside the handlers. It is a sibling module in the project
# root rather than a package, and importing it at module scope would make this whole web app
# fail to start if that file had a problem - a document-intake tool should not be taken down by
# a rating-engine import error.
PREF_FILE = Path(__file__).resolve().parent / "ui_prefs.json"


class _KeyArgs:
    """resolve_key() reads argparse attributes; the web app has no command line."""
    api_key = None
    api_key_file = None


def _rate_engine():
    import sys
    # rate_engine.py lives in tools/ (moved out of the project root 01-Sep-2026).
    tools_dir = str(ROOT / "tools")
    if tools_dir not in sys.path:
        sys.path.insert(0, tools_dir)
    import rate_engine
    return rate_engine


def _delivery_audit():
    # Same lazy-import pattern as _rate_engine: a tools/ import problem must not take down intake.
    tools_dir = str(ROOT / "tools")
    if tools_dir not in sys.path:
        sys.path.insert(0, tools_dir)
    import delivery_audit
    return delivery_audit


def _audit_badge(case: dict) -> str:
    """One-line readiness chip for a case card, from the cached last audit (if any)."""
    a = case.get("audit")
    if not a:
        return '<span class="badge opt">readiness not checked</span>'
    when = (a.get("checked_at") or "")[:16].replace("T", " ")
    if a.get("ready"):
        return f'<span class="badge done">READY &#10003;</span> <span class="mut">{when}</span>'
    n = len(a.get("failing") or [])
    return (f'<span class="badge req">NOT READY</span> '
            f'<span class="mut">{n} failing &middot; {when}</span>')


@app.post("/case/<slug>/audit")
def run_audit(slug):
    """Run delivery_audit.audit_case() for this case, cache the verdict in case.json, show it.

    On-demand only (a button, never a page-load) because a scored case runs several sub-processes
    - tie-outs, mutation coverage, section/quality, scorecard, Step-14 diff. It reads files only,
    so it never spends API budget. ponytail: synchronous; if a scored case ever feels too slow
    here, move it onto the upload-conversion background-thread pattern already in this file.
    """
    case = load_case(slug)                       # 404s if the slug is unknown
    try:
        result = _delivery_audit().audit_case(slug)
    except Exception as exc:                                              # noqa: BLE001
        flash("Readiness check could not run: %s" % exc)
        return redirect(url_for("company", slug=slug) + "#sec7")
    checks = [{"name": n, "ok": ok, "detail": d if isinstance(d, str) else str(d)}
              for (n, ok, d) in result["checks"]]
    failing = [c["name"] for c in checks if c["ok"] is False]
    case["audit"] = {
        "ready": result["ready"],
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "failing": failing,
        "checks": checks,
    }
    save_case(slug, case)
    flash("Readiness: %s (%d check(s) failing)."
          % ("READY TO SHARE" if result["ready"] else "NOT READY", len(failing)))
    return redirect(url_for("company", slug=slug) + "#sec7")


def _read_pref() -> dict:
    try:
        return json.loads(PREF_FILE.read_text(encoding="utf-8"))
    except Exception:                                                     # noqa: BLE001
        return {}


def _write_pref(**kw) -> None:
    d = _read_pref()
    d.update(kw)
    PREF_FILE.write_text(json.dumps(d, indent=2), encoding="utf-8")


@app.get("/settings")
def settings():
    try:
        RE = _rate_engine()
        key, source = RE.resolve_key(_KeyArgs())
        fp = RE.fingerprint(key)
        store = RE.KEY_FILE
        stored = store.exists()
        models = RE.MODELS
        default_model = RE.DEFAULT_MODEL
        sentinel = RE.AGENT_SENTINEL
    except Exception as exc:                                              # noqa: BLE001
        return page("Settings",
                    '<h1>Settings</h1><div class="card">'
                    '<p><strong>The rating engine could not be loaded.</strong></p>'
                    '<p class="mut">' + _e(str(exc)) + '</p>'
                    '<p class="mut">This page needs <code>rate_engine.py</code> in '
                    '<code>tools/</code> (' + _e(str(ROOT / "tools")) + '). Everything else in '
                    'this app still works.</p>'
                    '</div>', active="settings")

    chosen = _read_pref().get("model") or default_model
    opts = "".join(
        '<option value="' + _e(m) + '"' + (" selected" if m == chosen else "") + '>'
        + _e(m) + ' &mdash; ' + _e(d) + '</option>'
        for m, d in models.items())

    if key and key == sentinel:
        state = ('<span class="pill warn">Agent route</span> The stored value is the '
                 '<code>' + _e(sentinel) + '</code> sentinel, not an API key. Runs are handed '
                 'to a local Claude Code agent, which needs its own credential.')
    elif key:
        state = '<span class="pill ok">Credential found</span>'
    else:
        # Do NOT infer this from resolve_key's description. The fallback text mentions an
        # `ant auth login` profile whether or not one exists, and matching on that word showed
        # "Credential found" on a machine with no credential at all - a status line asserting
        # something it had not checked. sdk_has_credential() constructs the client, which is
        # the only honest test; it makes no request and bills nothing.
        import os as _os
        if any(_os.environ.get(v) for v in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN")):
            state = '<span class="pill ok">Credential found</span>'
        elif RE.sdk_has_credential():
            state = ('<span class="pill ok">Credential found</span> '
                     'Supplied by the SDK itself (an <code>ant auth login</code> profile).')
        else:
            state = ('<span class="pill bad">No credential</span> '
                     'The API engine cannot run until a key is set below.')

    clear_form = ""
    if stored:
        clear_form = (
            '<form method="post" action="' + url_for('settings_key_clear') + '" '
            'onsubmit="return confirm(\'Delete the stored API key?\')" style="margin-top:10px">'
            '<button class="btn ghost" type="submit">Delete stored key</button></form>')

    body = (
        '<h1>Settings</h1>'
        '<p class="mut">Where the rating engine gets its API key, and which model it uses.</p>'

        '<h2>API key</h2>'
        '<div class="card">'
        '<p>' + state + '</p>'
        '<table class="kv">'
        '<tr><td>In use</td><td><code>' + _e(source) + '</code></td></tr>'
        '<tr><td>Fingerprint</td><td><code>' + _e(fp) + '</code></td></tr>'
        '<tr><td>Stored at</td><td><code>' + _e(str(store)) + '</code>'
        + ('' if stored else ' <span class="mut">(nothing stored yet)</span>')
        + '</td></tr></table>'

        '<form method="post" action="' + url_for('settings_key') + '" class="rowform" '
        'style="margin-top:14px">'
        '<input type="password" name="api_key" autocomplete="off" spellcheck="false" '
        'placeholder="sk-ant-..." aria-label="Anthropic API key" required>'
        '<button class="btn" type="submit">Save key</button></form>'

        '<p class="mut" style="margin-top:8px">Typed characters are hidden, and the key is never '
        'sent back to this page &mdash; only the masked fingerprint above. It is stored in your '
        'home folder, deliberately not inside this project folder, which gets zipped and emailed '
        'with the reports in it. Enter <code>' + _e(sentinel) + '</code> instead of a key to hand '
        'work to a local Claude Code agent rather than the API.</p>'
        + clear_form +
        '</div>'

        '<h2>Model</h2>'
        '<div class="card">'
        '<form method="post" action="' + url_for('settings_model') + '" class="rowform">'
        '<select name="model" aria-label="Model">' + opts + '</select>'
        '<button class="btn" type="submit">Save model</button></form>'
        '<p class="mut" style="margin-top:8px">Used by the API engine. The local scorecard engine '
        'runs offline and ignores this.</p></div>'

        '<h2>Running a rating</h2>'
        '<div class="card">'
        '<p class="mut">This page sets credentials only &mdash; it does not start a rating. An '
        'API or agent run spends money, and that should be an explicit decision taken where you '
        'can see the output, not a button on a settings page. Run one from a terminal in the '
        'project root:</p>'
        '<pre class="cmd">python tools/rate_engine.py &lt;case-slug&gt; --engine local</pre>'
        '<p class="mut">The local scorecard engine is free and offline. Add '
        '<code>--engine api</code> for a model view as well, or <code>--engine both</code> to '
        'compare the two; those use the key above and are capped by '
        '<code>--max-budget-usd</code> (default 2.00).</p>'
        '<p class="mut">For a model view with <b>no key and no internet</b>, use a local model '
        'via <a href="https://ollama.com" target="_blank" rel="noopener">Ollama</a> &mdash; it '
        'runs alongside the scorecard, the offline equivalent of <code>--engine both</code>:</p>'
        '<pre class="cmd">ollama pull qwen2.5:14b   # one-time\n'
        'python tools/rate_engine.py &lt;case-slug&gt; --engine ollama --ollama-model qwen2.5:14b</pre>'
        '<p class="mut">See which models are pulled with '
        '<code>python tools/rate_engine.py --list-models</code>.</p></div>')
    return page("Settings", body, active="settings")


@app.post("/settings/key")
def settings_key():
    key = (request.form.get("api_key") or "").strip()
    if not key:
        flash("No key entered - nothing changed.")
        return redirect(url_for("settings"))
    RE = _rate_engine()
    note = RE.store_key(key)
    if key == RE.AGENT_SENTINEL:
        flash("Agent sentinel stored - runs will be routed to a local Claude Code agent.")
    else:
        # The fingerprint, never the key. Flash messages ride in a session cookie and show up in
        # the browser's history and in any screen recording of it.
        flash("API key saved (%s)." % RE.fingerprint(key))
    if note:
        flash("Note: %s" % note)
    return redirect(url_for("settings"))


@app.post("/settings/key/clear")
def settings_key_clear():
    RE = _rate_engine()
    if RE.KEY_FILE.exists():
        RE.KEY_FILE.unlink()
        flash("Stored API key deleted.")
    else:
        flash("There was no stored key to delete.")
    return redirect(url_for("settings"))


@app.post("/settings/model")
def settings_model():
    RE = _rate_engine()
    m = request.form.get("model") or ""
    if m not in RE.MODELS:
        flash("Unknown model - nothing changed.")
        return redirect(url_for("settings"))
    _write_pref(model=m)
    flash("Model set to %s." % m)
    return redirect(url_for("settings"))


if __name__ == "__main__":
    import os
    # threaded=True: upload conversion runs in a background thread while the browser polls
    # /upload-progress/<job_id> on the same server - the default single-threaded dev server
    # would block the progress-poll requests behind whatever request is currently running.
    #
    # Set RATING_DEV=1 to get Flask's auto-reloader + debugger while editing this file (no more
    # manual kill-and-restart). Off by default: the reloader spawns a watcher child and the
    # debugger allows in-browser code execution, neither of which belongs in normal use. The
    # tool is localhost-only either way.
    dev = os.environ.get("RATING_DEV") == "1"
    app.run(host="127.0.0.1", port=5050, debug=dev, use_reloader=dev, threaded=True)
