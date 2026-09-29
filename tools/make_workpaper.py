"""Generate a case's Ratio Workpaper (Step 9) from its OWN engine output.

    python tools/make_workpaper.py <case-slug> [--all] [--force]

WHAT THIS BUILDS, AND WHAT IT DELIBERATELY DOES NOT
---------------------------------------------------
Step 9 requires a workpaper carrying: the computed suite, trend commentary, the Document Read
Log, the qualitative fact register, materiality-sweep decisions, the Methodology Compliance Map
and the caveats. Some of that is DERIVABLE from the engine and the case folder; some of it is
analyst judgment that only exists once a person has read the documents.

This tool builds the derivable half from real data and NAMES the other half as outstanding. It
does not invent a Read Log, a sweep decision or a Compliance Map, because a fabricated one is
worse than a missing one - it reads as diligence and stops anyone looking (failure mode 20, and
the reason failure mode 37 exists at all). Every figure it writes comes from `compute()`,
`tieouts()`, the mutation harness or the case's own rationale, and every section says where it
came from.

A generated workpaper therefore CLOSES the delivery-audit's "ratio workpaper delivered" check
while leaving the analytical gap visible in the document itself. That is the honest position:
the extraction and verification record is complete and checkable; the document-reading sections
are listed by name as still owed.
"""
from __future__ import annotations

import argparse
import ast
import contextlib
import datetime as dt
import importlib.util
import io
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
CASES = ROOT / "Companies"

# Sections that require a document to have been read. Never generated - only listed.
ANALYST_SECTIONS = [
    ("Document Read Log (Step 1b)",
     "one row per uploaded file: what it is, the key facts it contributes, the material items "
     "it flags. A file not in the log has not been read."),
    ("Qualitative fact register (Step 7)",
     "every non-computed claim traced to a document location, and corroborated against a second "
     "source where one exists (response protocol 2(e))."),
    ("Materiality sweep (Step 8)",
     "the untouched sections of every file walked for credit-relevant items, each tagged "
     "material/immaterial against the R13 test with a written include/exclude decision."),
    ("Methodology Compliance Map (Step 10)",
     "one row per rating factor as the methodology names it, scored with the company's actual "
     "numbers against the indicative band, every notching criterion quoted verbatim."),
    ("Liquidity computation (Step 11)",
     "sources-vs-claims arithmetic over ~12 months; the descriptor is the conclusion of that "
     "arithmetic, never an adjective."),
]


def load_engine(path: pathlib.Path):
    spec = importlib.util.spec_from_file_location("wp_engine_%s" % abs(hash(str(path))), path)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):        # engines print on import guard-free
        spec.loader.exec_module(mod)
    return mod


def coverage_for(slug: str):
    """(coverage_pct, [(table, key, period, value), ...]) from the mutation harness."""
    script = HERE / "tieout_mutation.py"
    if not script.is_file():
        return None, []
    try:
        p = subprocess.run([sys.executable, str(script), slug], cwd=str(ROOT.parent),
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=900)
    except subprocess.TimeoutExpired:
        return None, []
    out = p.stdout + p.stderr
    m = re.search(r"coverage\s*:\s*([\d.]+)%", out)
    cov = float(m.group(1)) if m else None
    rows, table = [], None
    seen_header = False
    for ln in out.splitlines():
        if "INPUTS NO TIE-OUT" in ln:
            seen_header = True
            continue
        if not seen_header:
            continue
        if re.match(r"^  \S", ln):
            table = ln.strip()
        elif re.match(r"^      \S", ln):
            parts = ln.split()
            if len(parts) >= 2:
                rows.append((table or "?", " ".join(parts[:-2]), parts[-2], parts[-1]))
    return cov, rows


def source_register(mod):
    """[(table, key, source)] for engines whose inputs carry a source annotation."""
    out = []
    for name in dir(mod):
        if name.startswith("_") or not name.isupper():
            continue
        obj = getattr(mod, name)
        if not isinstance(obj, dict) or not obj:
            continue
        for k, v in obj.items():
            if (isinstance(v, tuple) and len(v) == 2 and isinstance(v[0], list)
                    and isinstance(v[1], str)):
                out.append((name, str(k), v[1]))
    return out


def named_gaps(src: str):
    """[(title, body)] from the engine's own DISCLOSED_DIFFERENCES / UNVERIFIED_INPUTS."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for t in node.targets:
            if isinstance(t, ast.Name) and t.id in ("DISCLOSED_DIFFERENCES",
                                                    "UNVERIFIED_INPUTS"):
                try:
                    val = ast.literal_eval(node.value)
                except Exception:                                         # noqa: BLE001
                    continue
                for item in val:
                    if isinstance(item, (tuple, list)) and len(item) >= 2:
                        out.append((str(item[0]), str(item[1])))
                    else:
                        out.append((str(item), ""))
    return out


def rationale_facts(case_dir: pathlib.Path):
    """(filename, headline, [section headers]) from the case's own rationale."""
    cands = [p for p in sorted(case_dir.glob("*Rating Rationale*.md"))
             if "SUPERSEDED" not in p.name.upper()]
    if not cands:
        return None, None, []
    f = cands[-1]
    txt = f.read_text(encoding="utf-8", errors="replace")
    head = ""
    for ln in txt.splitlines():
        s = ln.strip().lstrip("#").strip()
        if s and not s.startswith("*") and len(s) > 12:
            head = s.strip("*_ ")
            break
    secs = [ln.strip().lstrip("#").strip() for ln in txt.splitlines()
            if re.match(r"^#{1,3} ", ln)]
    return f.name, head, secs[:24]


def fmt_val(v):
    if isinstance(v, float):
        return "%,.2f".replace("%,", "{:,").format(v) if False else "{:,.2f}".format(v)
    return str(v)


def build(slug: str, force: bool = False) -> str:
    case_dir = CASES / slug
    engine = case_dir / "compute_ratios.py"
    if not case_dir.is_dir():
        return "no such case folder: %s" % slug
    if not engine.is_file():
        return "%s: no compute_ratios.py - nothing to build a ratio workpaper from" % slug
    existing = list(case_dir.glob("*Workpaper*.md")) + list(case_dir.glob("*workpaper*.md"))
    if existing and not force:
        return "%s: workpaper already exists (%s) - use --force to regenerate" % (
            slug, existing[0].name)

    src = engine.read_text(encoding="utf-8", errors="replace")
    mod = load_engine(engine)
    years = list(getattr(mod, "YEARS", []))
    R = mod.compute()
    T = mod.tieouts(R)
    cov, uncovered = coverage_for(slug)
    gaps = named_gaps(src)
    reg = source_register(mod)
    rat_file, headline, rat_secs = rationale_facts(case_dir)

    case_json = {}
    cj = case_dir / "case.json"
    if cj.is_file():
        try:
            case_json = json.loads(cj.read_text(encoding="utf-8", errors="replace"))
        except Exception:                                                 # noqa: BLE001
            pass
    company = case_json.get("name") or slug.replace("-", " ").title()
    agency = case_json.get("agency", "")

    periods = [p for p in years if p in R] or list(R)
    # every ratio the engine computed, in first-period order then alphabetical
    labels, seen = [], set()
    for p in periods:
        for k in R[p]:
            if k not in seen:
                seen.add(k)
                labels.append(k)

    today = dt.date.today().strftime("%d %b %Y")
    L = []
    A = L.append
    A("# Ratio Workpaper - %s%s" % (company, (" | " + agency) if agency else ""))
    A("")
    A("*Generated %s by `tools/make_workpaper.py` from this case's own "
      "`compute_ratios.py`.*" % today)
    A("")
    A("> **What this document is.** The EXTRACTION AND VERIFICATION record for this case: the "
      "computed ratio suite, every tie-out with its source, the measured coverage of those "
      "tie-outs, and the inputs nothing checks. Every figure below is produced by the engine, "
      "not retyped - re-run `python Companies/%s/compute_ratios.py` to reproduce it." % slug)
    A(">")
    A("> **What this document is NOT.** It does not contain the Document Read Log, the "
      "qualitative fact register, the materiality sweep or the Methodology Compliance Map. "
      "Those require the documents to have been read and are listed by name in section 6 as "
      "outstanding. They are not generated here because a fabricated Read Log reads as "
      "diligence and stops anyone looking - which is failure mode 20, and the reason failure "
      "mode 37 exists.")
    A("")

    # ---------------------------------------------------------------- 1 computed suite
    A("## 1. Computed ratio suite (Step 6)")
    A("")
    A("Basis: periods as the engine declares them. Values as `compute()` returns them.")
    A("")
    A("| Metric | " + " | ".join(periods) + " |")
    A("|---|" + "---|" * len(periods))
    for lab in labels:
        cells = []
        for p in periods:
            v = R[p].get(lab)
            cells.append("{:,.2f}".format(v) if isinstance(v, (int, float))
                         and not isinstance(v, bool) else "-")
        A("| %s | %s |" % (lab, " | ".join(cells)))
    A("")

    # ---------------------------------------------------------------- 2 tie-outs
    bad = [t for t in T if abs(t[1] - t[2]) > t[3]]
    A("## 2. Tie-outs (Step 6 gate) - %d/%d reconcile" % (len(T) - len(bad), len(T)))
    A("")
    A("Each row reconciles a figure this engine DERIVES against one printed somewhere else. "
      "A check that compares a value with itself cannot fail and is not a check (failure "
      "mode 39).")
    A("")
    A("| # | Check | Computed | Disclosed | Tol | Source | |")
    A("|---|---|---|---|---|---|---|")
    for i, (desc, comp, disc, tol, srcstr) in enumerate(T, 1):
        ok = "OK" if abs(comp - disc) <= tol else "**FAIL**"
        A("| %d | %s | %s | %s | %s | %s | %s |"
          % (i, desc, "{:,.2f}".format(comp), "{:,.2f}".format(disc),
             "{:g}".format(tol), srcstr, ok))
    A("")
    if bad:
        A("**%d tie-out(s) do not reconcile - resolve before drafting (Step 17).**" % len(bad))
        A("")

    # ---------------------------------------------------------------- 3 coverage
    A("## 3. Tie-out coverage, measured by mutation (Step 6 / failure mode 39)")
    A("")
    if cov is None:
        A("`tieout_mutation.py` did not return a coverage figure for this case.")
    else:
        A("`python tools/tieout_mutation.py %s` -> **%.1f%% coverage**." % (slug, cov))
        A("")
        A("Coverage is MEASURED, not asserted: the harness perturbs every numeric input and "
          "reports which ones no tie-out notices. A suite can be 100%% green and still verify "
          "nothing, so the count of passing checks is not the question - the question is which "
          "inputs would be caught if they were wrong.")
        A("")
        if uncovered:
            A("Inputs no tie-out is sensitive to (%d):" % len(uncovered))
            A("")
            A("| Table | Input | Period | Value |")
            A("|---|---|---|---|")
            for tb, key, per, val in uncovered[:60]:
                A("| %s | %s | %s | %s |" % (tb, key, per, val))
            if len(uncovered) > 60:
                A("| ... | *%d more* | | |" % (len(uncovered) - 60))
            A("")
        else:
            A("No input is left unchecked by the tie-out suite.")
            A("")

    # ---------------------------------------------------------------- 4 disclosed gaps
    A("## 4. Disclosed differences and unverified inputs (carried from the engine)")
    A("")
    if gaps:
        for title, body in gaps:
            A("- **%s** - %s" % (title, body))
    else:
        A("The engine names none. Where coverage is below 100%%, failure mode 39 requires every "
          "uncovered input to be given a check or named here with the reason.")
    A("")

    # ---------------------------------------------------------------- 5 extraction sources
    if reg:
        A("## 5. Extraction source register (Step 5)")
        A("")
        A("Where the engine annotates an input with its origin, that annotation is reproduced "
          "verbatim. This is a provenance record, not a corroboration record - traced is not "
          "verified (response protocol 2(e)).")
        A("")
        A("| Table | Line item | Source as the engine records it |")
        A("|---|---|---|")
        for tb, key, s in reg[:80]:
            A("| %s | %s | %s |" % (tb, key, s.replace("|", "/")))
        if len(reg) > 80:
            A("| ... | *%d more* | |" % (len(reg) - 80))
        A("")

    # ---------------------------------------------------------------- 6 outstanding
    A("## 6. OUTSTANDING - the sections that require the documents to be read")
    A("")
    A("These are **not** in this document and have **not** been done. They are named here so "
      "the gap is visible rather than silent.")
    A("")
    for name, what in ANALYST_SECTIONS:
        A("- [ ] **%s** - %s" % (name, what))
    A("")

    # ---------------------------------------------------------------- 7 rating view
    A("## 7. Rating view as delivered (Step 13-15, from this case's own rationale)")
    A("")
    if rat_file:
        A("Source: `%s`" % rat_file)
        A("")
        if headline:
            A("> %s" % headline)
            A("")
        if rat_secs:
            A("Sections present in the delivered rationale:")
            A("")
            for s in rat_secs:
                A("- %s" % s)
            A("")
        A("The rating view itself lives in that document; it is referenced here rather than "
          "restated, so the two cannot drift apart.")
    else:
        A("No `*Rating Rationale*.md` found in this case folder.")
    A("")

    A("---")
    A("")
    A("*Reproduce this workpaper: `python tools/make_workpaper.py %s --force`. "
      "Re-verify the case: `python tools/delivery_audit.py %s`.*" % (slug, slug))
    A("")

    name = "%s_Ratio_Workpaper_%s.md" % (company.replace("/", "-"),
                                         dt.date.today().strftime("%d%b%Y"))
    out = case_dir / name
    out.write_text("\n".join(L), encoding="utf-8")
    return "OK  %-42s -> %s  (%d ratios x %d periods, %d/%d tie-outs, %s coverage)" % (
        slug, name, len(labels), len(periods), len(T) - len(bad), len(T),
        ("%.1f%%" % cov) if cov is not None else "n/a")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--all", action="store_true",
                    help="every case that has an engine but no workpaper")
    ap.add_argument("--force", action="store_true", help="regenerate over an existing one")
    a = ap.parse_args()

    if a.all:
        todo = []
        for d in sorted(CASES.iterdir()):
            if not d.is_dir() or not (d / "compute_ratios.py").is_file():
                continue
            has_wp = list(d.glob("*Workpaper*.md")) + list(d.glob("*workpaper*.md"))
            if not has_wp or a.force:
                todo.append(d.name)
        if not todo:
            print("every case with an engine already has a workpaper.")
            return 0
        for s in todo:
            print(build(s, a.force))
        return 0

    if not a.slug:
        ap.error("give a case slug, or --all")
    print(build(a.slug, a.force))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
