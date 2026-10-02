"""Gate oracles for the Jindal Stainless Limited CareEdge rating (see GATES.md).

Usage:  python verify_jsl.py <gate> [--control]

Every gate prints a single decisive success token and exits non-zero on failure. Gates whose
job is to detect an ABSENCE carry a --control that INJECTS the break they are supposed to
catch, so "it passed" can be distinguished from "it never looked" - the failure that bit twice
on the Balkrishna case, where a control silently became a no-op and reported success.
"""

import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
RATIONALE = HERE / "Jindal Stainless Limited_26 Aug 2026_CARE_Rating Rationale.md"
SPREADS = HERE / "Jindal Stainless Limited_Financial_Spreads.xlsx"
MODEL = HERE / "Jindal Stainless Limited_5yr_Model.xlsx"
SCORECARD = HERE / "Rating_Scorecard_Jindal Stainless Limited.xlsx"

_findings = []


def check(cond, msg):
    if not cond:
        _findings.append(msg)


def read(p):
    return Path(p).read_text(encoding="utf-8", errors="replace")


# ------------------------------------------------------------------ G1 routing
def g_routing():
    rat = read(RATIONALE)
    meth = ROOT / "CareEdge" / "Methodology"
    check(meth.is_dir(), "CareEdge/Methodology not found - wrong agency library")
    names = " ".join(f.name.lower() for f in meth.iterdir())
    check("manufacturing" in names, "no Manufacturing Companies criteria in CareEdge library")
    check("financial_ratios_non_financial" in names.replace(" ", "_")
          or "financial ratios" in names,
          "no non-financial-sector Financial Ratios criteria in CareEdge library")
    check(re.search(r"manufacturing companies", rat, re.I) is not None,
          "rationale does not name the Manufacturing Companies criteria")
    check(re.search(r"financial ratios[^\n]{0,40}non[- ]financial", rat, re.I) is not None,
          "rationale does not name the non-financial-sector Financial Ratios criteria")
    check(re.search(r"liquidity analysis", rat, re.I) is not None,
          "rationale does not name the Liquidity Analysis criteria")
    # It must NOT cite another agency's methodology (AGENCIES.md).
    check(re.search(r"ICRA'?s? rating methodology|CRISIL'?s? criteria", rat, re.I) is None,
          "rationale cites a non-CareEdge methodology")
    return "ROUTING VERIFIED"


# ------------------------------------------------------------------ G2 rated amounts
WRONG_ENTITIES = ["Jindal Steel", "Jindal Saw", "Jindal Poly", "Jindal Drilling"]
PUBLISHED_LINES = [("5,900.00", "Long-term bank facilities"),
                   ("11,000.00", "Short-term bank facilities"),
                   ("99.00", "Non-convertible debentures"),
                   ("1,000.00", "Non-convertible debentures")]


def _inject_wrong_entity(rat):
    """Replace the LT bank facilities amount with a figure belonging to a DIFFERENT issuer.

    Regex on the ROW rather than an exact-string replace on a whole line: hard-coding the
    line text is what made the equivalent Balkrishna control decay into a silent no-op once
    the surrounding prose changed. Returns (text, count) so the caller can assert the
    substitution actually happened.
    """
    pattern = re.compile(r"(\|Long-term bank facilities\|)5,900\.00(\|)")
    return pattern.subn(lambda m: m.group(1) + "13,750.00 (Jindal Steel)" + m.group(2), rat, 1)


def g_rated_amounts(control=False):
    rat = read(RATIONALE)
    if control:
        rat, n = _inject_wrong_entity(rat)
        check(n == 1, "CONTROL SETUP FAILED - the injection matched nothing, so this control "
                      "proves nothing about the oracle")

    for amt, label in PUBLISHED_LINES:
        check(amt in rat, "published line missing from the rating table: %s %s" % (label, amt))
    # Line integrity (failure mode 12).
    check("17,999.00" in rat, "published total 17,999.00 not stated")
    check(abs((5900.00 + 11000.00 + 99.00 + 1000.00) - 17999.00) < 0.005,
          "published lines do not sum to the published total")
    # Condition (2): date stamped. Condition (3): labelled CRA-published.
    check(re.search(r"October 0?9,? 2025", rat) is not None,
          "publication date of the imported table not stamped")
    check(re.search(r"CRA[- ]published", rat, re.I) is not None,
          "imported amounts not labelled CRA-published rather than issuer-confirmed")
    # Condition (5): limits vs drawn debt distinguished.
    check(re.search(r"LIMITS", rat) is not None and "7,460.33" in rat,
          "rated-limits-vs-drawn-debt distinction not stated with both figures")
    # No wrong-entity amount may appear.
    for ent in WRONG_ENTITIES:
        check(ent not in rat,
              "an amount or reference belonging to %s appears in this report" % ent)

    if control:
        if _findings:
            print("CONTROL OK - oracle rejected the injected break (%d finding(s))"
                  % len(_findings))
            return None
        print("CONTROL FAILED - oracle ACCEPTED a wrong-entity amount")
        sys.exit(1)
    return "RATED AMOUNTS SOUND"


# ------------------------------------------------------------------ G3/G4 spreads
def g_spreads():
    check(SPREADS.exists(), "spreads workbook missing")
    if _findings:
        return None
    import compute_ratios as C
    sys.path.insert(0, str(HERE))
    import _xlread
    cells = _xlread.load(str(SPREADS))
    sheets = {k[0] for k in cells}
    for want in ("EXTRACTION", "RATIOSUITE", "TIEOUT", "CONVENTIONS"):
        check(want in sheets, "tab missing from workbook: %s" % want)

    # Every TieOut verdict cell must read PASS - the workbook checks itself, live.
    verdicts = [v for (sh, c, r), v in cells.items()
                if sh == "TIEOUT" and c == "D" and isinstance(v, str) and v in ("PASS", "FAIL")]
    check(len(verdicts) >= 10, "too few TieOut verdict rows evaluated (%d)" % len(verdicts))
    check(all(v == "PASS" for v in verdicts),
          "%d TieOut row(s) FAIL in the workbook" % sum(1 for v in verdicts if v != "PASS"))

    # The workbook's LIVE formulas must reproduce the Python engine, not merely exist.
    R = C.compute()
    cols = {"FY2023": "B", "FY2024": "C", "FY2025": "D", "FY2026": "E"}
    for y, cl in cols.items():
        wb_pbildt = _xlread.num(cells, "RATIOSUITE", cl, 5)      # PBILDT row
        check(wb_pbildt is not None
              and abs(wb_pbildt - R[y]["PBILDT"]) < 0.01,
              "workbook PBILDT for %s (%s) does not reproduce the engine (%.2f)"
              % (y, wb_pbildt, R[y]["PBILDT"]))
    return "SPREADS OK"


# ------------------------------------------------------------------ G5 step 12
def g_step12():
    check(MODEL.exists(), "5-yr model missing")
    if _findings:
        return None
    sys.path.insert(0, str(HERE))
    import _xlread
    cells = _xlread.load(str(MODEL))
    sheets = {k[0] for k in cells}
    for want in ("ASSUMPTIONS", "P_AND_L", "BALANCE_SHEET", "CREDIT_RATIOS",
                 "DEBT_BREAKUP", "STRESS_CASE"):
        check(want in sheets, "model tab missing: %s" % want)

    # No projected cell may be blank or an error.
    bad = [k for k, v in cells.items()
           if isinstance(v, str) and v.startswith("#")]
    check(not bad, "%d model cell(s) resolve to an Excel error: %s" % (len(bad), bad[:5]))

    # Finance costs must be NON-ZERO in every projected year. The first build of this model
    # referenced a section header instead of the opening-debt row and projected finance costs
    # of zero for all five years while looking entirely plausible - this gate exists for that.
    for cl in "FGHIJ":
        fc = _xlread.num(cells, "P_AND_L", cl, 5)
        check(fc is not None and fc > 0,
              "projected finance costs in column %s are %s - the interest formula is not "
              "reaching the opening-debt row" % (cl, fc))

    # Debt must be DERIVED (a formula), not a typed input (failure mode 18).
    from openpyxl import load_workbook
    wb = load_workbook(str(MODEL))
    ws = wb["Balance_Sheet"]
    for cl in "FGHIJ":
        v = ws["%s11" % cl].value
        check(isinstance(v, str) and v.startswith("=") and "MAX" in v,
              "closing debt in %s11 is not a derived formula: %r" % (cl, v))
    # The rationale QUOTES the stress result in prose. Prose is computed by nothing, so it can
    # drift from the tab that IS computed - and it did: an earlier draft asserted "approximately
    # 1.9 times and approximately 4.1 times" while this tab computes 1.76 and 7.29. The 4.1x had
    # never been derived from any figure at all.
    #
    # The FIRST version of this check searched the WHOLE document for the substring "1.8"/"7.3"
    # and passed its own control, because those digits occur inside unrelated numbers - "11.87",
    # "7,460.33", "5,451.81". Scope the search to the stress SENTENCE and require the quoted
    # figure to be a standalone number, or the check is decorative.
    rat = read(RATIONALE)
    i = rat.find("A stress case")
    check(i != -1, "the rationale does not state a stress case at all")
    if i != -1:
        sentence = rat[i:rat.find(chr(10), i)]
        quoted = [float(x) for x in re.findall(r"approximately ([\d.]+) times", sentence)]
        check(len(quoted) >= 2,
              "the stress sentence does not quote both stress ratios: %r" % sentence[:160])
        for row, label in ((13, "total debt/PBILDT"), (14, "interest coverage")):
            val = _xlread.num(cells, "STRESS_CASE", "B", row)
            if val is None:
                check(False, "Stress_Case row %d did not evaluate" % row)
                continue
            check(any(abs(q - val) <= 0.05 for q in quoted),
                  "stress %s computed on the Stress_Case tab is %.2f, but the rationale quotes "
                  "%s - prose and model disagree" % (label, val, quoted))
    return "STEP 12 SATISFIED"


# ------------------------------------------------------------------ G6 step 12b
def g_step12b():
    check(SCORECARD.exists(), "scorecard workbook missing")
    if _findings:
        return None
    sys.path.insert(0, str(HERE))
    import _xlread
    cells = _xlread.load(str(SCORECARD))
    anchor = cells.get(("RATING", "C", 12))
    check(isinstance(anchor, str)
          and re.fullmatch(r"(AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?|C+|D)", anchor.strip()),
          "Rating!C12 does not carry a recognised grade: %r" % anchor)
    rat = read(RATIONALE)
    check(re.search(r"anchor grade of \*\*%s\*\*" % re.escape(str(anchor).strip()), rat)
          or re.search(r"anchor[^\n]{0,80}%s" % re.escape(str(anchor).strip()), rat),
          "the rationale does not disclose the scorecard anchor (%r)" % anchor)
    return "STEP 12B SATISFIED"


# ------------------------------------------------------------------ G7 delivery gate
def g_gate():
    r = subprocess.run([sys.executable, str(ROOT / "check_sections.py"), str(RATIONALE)],
                       capture_output=True, text=True)
    out = r.stdout + r.stderr
    check(r.returncode == 0, "check_sections.py exited %d" % r.returncode)
    check("[PASS]" in out, "delivery gate did not report PASS:\n" + out[-1500:])
    check("QUALITY:" not in out, "a quality probe fired:\n" + out[-1500:])
    return "DELIVERY GATE CLEAN"


# ------------------------------------------------------------------ G8 opm normalisation
def g_opm_normalisation(control=False):
    rat = read(RATIONALE)
    if control:
        # Strip the whole normalisation paragraph, leaving the margin figures in place.
        rat, n = re.subn(r"\*\*Computation basis, stated rather than implied\.\*\*.*?"
                         r"(?=\*\*Tangible net worth\*\*)", "", rat, flags=re.S)
        check(n == 1, "CONTROL SETUP FAILED - the normalisation paragraph was not found, so "
                      "this control proves nothing")

    check(re.search(r"foreign[- ]exchange|forex", rat, re.I) is not None,
          "the operating-profit build does not name its foreign-exchange treatment")
    check(re.search(r"exceptional items are excluded", rat, re.I) is not None,
          "the report does not state how exceptional items are treated")
    check("78.41" in rat and "154.37" in rat and "190.04" in rat and "68.48" in rat,
          "the P&L forex line is not quantified for all four years. NB these must be the "
          "OTHER EXPENSES note figures, not the cash-flow reconciliation's unrealised rows "
          "- confusing the two put FY2026 in as an 87.15 LOSS against an audited 78.41 GAIN")
    check(re.search(r"not[^\n]{0,40}added back a second time|double[- ]count", rat, re.I)
          is not None,
          "the report does not state that exceptional items are not added back twice")
    check("11.61" in rat,
          "the unadjusted asset-disposal item is not quantified and disclosed")

    if control:
        if _findings:
            print("CONTROL OK - oracle rejected the injected break (%d finding(s))"
                  % len(_findings))
            return None
        print("CONTROL FAILED - oracle ACCEPTED a report with no normalisation statement")
        sys.exit(1)
    return "OPM NORMALISATION VERIFIED"


# ------------------------------------------------------------------ G9 sector metrics
def g_sector_metrics():
    rat = read(RATIONALE)
    # Metals sector: volume, realisation, per-tonne economics, capacity utilisation context.
    check("2.57" in rat, "finished-goods sales volume (MT) not stated")
    check("21,640" in rat and "19,630" in rat,
          "PBILDT per tonne series not stated - the metals-sector unit-economics metric")
    check(re.search(r"realisation", rat, re.I) is not None, "net sales realisation not stated")
    check("4.2 MTPA" in rat, "group melting capacity not stated")
    check(re.search(r"3\.5 MTPA|3\.5 MT", rat) is not None,
          "the company's own volume aspiration is not stated")
    # The capacity figure must be presented WITH its India/Indonesia split, since the
    # pre-flight flagged a conflicting utilisation figure that had to be resolved, not picked.
    check(re.search(r"3 MTPA in India|approximately 3 MTPA", rat) is not None,
          "the India-vs-Indonesia capacity split is not stated")
    return "SECTOR METRICS PRESENT"


# ------------------------------------------------------------------ G12 tie-out coverage
def g_coverage():
    """Failure mode 39: measure what the tie-outs COVER, don't count what passes."""
    r = subprocess.run([sys.executable, str(ROOT / "tieout_mutation.py"), "jindal-stainless"],
                       capture_output=True, text=True, cwd=str(ROOT))
    out = r.stdout + r.stderr
    check(r.returncode == 0, "tieout_mutation.py exited %d" % r.returncode)
    m = re.search(r"coverage\s*:\s*([\d.]+)%", out)
    check(m is not None, "could not parse coverage from the harness output")
    if not m:
        return None
    pct = float(m.group(1))
    check(pct >= 95.0,
          "tie-out coverage is %.1f%%, below the 95%% floor - inputs that no check is "
          "sensitive to are how the forex error survived three rounds of checking" % pct)

    # The harness's finding must EXACTLY match the set the engine declares. An earlier version
    # merely looked for the input's first word somewhere in DISCLOSED_DIFFERENCES, and passed
    # its own control because "eps" still appeared in an unrelated sentence - the same
    # substring-coincidence failure as the stress check. Compare sets, not substrings.
    found = set()
    for line in out.splitlines():
        m = re.match(r"^\s{6}(\S.*?)\s{2,}(FY\d{4})\s+[-\d]", line)
        if m:
            found.add((m.group(1).strip(), m.group(2)))
    import compute_ratios as C
    declared = {(k, y) for _tbl, k, y in C.UNVERIFIED_INPUTS}
    missing = found - declared
    stale = declared - found
    check(not missing,
          "these inputs are verified by NO tie-out and are not declared in "
          "UNVERIFIED_INPUTS: %s" % sorted(missing))
    check(not stale,
          "UNVERIFIED_INPUTS declares entries the harness no longer reports (a check was "
          "added, or a label changed) - remove them: %s" % sorted(stale))
    print("coverage %.1f%%, %d unverified input(s), all declared" % (pct, len(found)))
    return "COVERAGE MEASURED"


GATES = {"routing": g_routing, "rated_amounts": g_rated_amounts, "spreads": g_spreads,
         "step12": g_step12, "step12b": g_step12b, "gate": g_gate,
         "opm_normalisation": g_opm_normalisation, "sector_metrics": g_sector_metrics, "coverage": g_coverage}


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    if len(sys.argv) < 2 or sys.argv[1] not in GATES:
        print("usage: verify_jsl.py {%s} [--control]" % "|".join(GATES))
        sys.exit(2)
    fn = GATES[sys.argv[1]]
    control = "--control" in sys.argv
    token = fn(control=control) if control and fn in (g_rated_amounts, g_opm_normalisation) \
        else fn()
    if token is None:
        return
    if _findings:
        for f in _findings:
            print("FAIL: %s" % f)
        print("%d assertion(s) failed" % len(_findings))
        sys.exit(1)
    print(token)


if __name__ == "__main__":
    main()
