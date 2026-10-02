"""Gate oracles for the Balkrishna Industries Limited rating (GATES.md).

Each subcommand MEASURES a claim from the delivered artefacts and prints a success-only token
as its LAST line, exiting 0 only when every assertion passed.

Usage: python verify_bil.py <gate> [--control]
"""
import re
import sys
from pathlib import Path

import openpyxl

HERE = Path(__file__).resolve().parent
RATIONALE = HERE / "Balkrishna Industries Limited_25 Aug 2026_Rating Rationale.md"
SPREADS = HERE / "Balkrishna Industries Limited_Financial_Spreads.xlsx"
MODEL = HERE / "Balkrishna Industries Limited_5yr_Model.xlsx"
SCORECARD = HERE / "Rating_Scorecard_Balkrishna Industries Limited.xlsx"
CORP_METH = HERE.parents[1] / "Methodology" / "960~Corporate Credit Rating Methodology, Jul 2025.md"
AUTO_METH = HERE.parents[1] / "Methodology" / "931~Auto Components, Rating Methodology, Oct 2024.md"
CRISIL_REF = (HERE.parents[1] / "CRISIL" / "Report for Reference"
              / "Balkrishna Industries Limited_27 Feb 2026_RR_390225.md")
CAREEDGE_REF = (HERE.parents[1] / "CareEdge" / "Report for Reference"
                / "Balkrishna Industries Limited_05 Mar 2026.md")

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)
    return cond


def read(p):
    if not p.exists():
        fails.append("MISSING FILE %s" % p.name)
        return ""
    return p.read_text(encoding="utf-8", errors="replace")


# ------------------------------------------------------------------ G1 routing
def g_routing():
    check(CORP_METH.exists(), "Corporate Credit Rating Methodology file missing")
    auto = read(AUTO_METH)
    check(bool(auto), "Auto Components methodology unreadable")
    check(re.search(r"tyres?", auto, re.I) is not None,
          "Auto Components methodology does not mention tyres anywhere - routing unverified")
    rat = read(RATIONALE)
    check("Corporate Credit Rating Methodology (July 2025)" in rat,
          "rationale does not name the Corporate methodology with vintage")
    check("Auto Components (October 2024)" in rat,
          "rationale does not name the Auto Components methodology with vintage")
    return "ROUTING VERIFIED"


# ------------------------------------------------------------------ G2 / G2C peer-agency amounts
def _inject_numeric_amount(rat):
    """Replace the bank-facilities row's 'To be confirmed by issuer' cell with a bare figure.

    Regex on the ROW, not an exact-string replace on the whole line: the first version of this
    control hard-coded the line including "[ICRA]AA (Stable)". When the rating was corrected to
    AA+, that exact string stopped existing, the replace became a silent no-op, and the control
    reported "oracle ACCEPTED a broken input" when no break had actually been introduced. Return
    (new_text, count) so the caller can assert the substitution really happened.
    """
    pattern = re.compile(
        r"(\|\s*Long-term fund-based bank facilities\s*\|[^|]*\|)\s*"
        r"To be confirmed by issuer\s*(\|)")
    return pattern.subn(lambda m: m.group(1) + " 2,000.00 " + m.group(2), rat, count=1)


def g_peer_agency_amounts(control=False):
    rat = read(RATIONALE)
    if control:
        rat, k = _inject_numeric_amount(rat)
        check(k == 1, "CONTROL SETUP FAILED - the injection did not match any row, so no break "
                      "was actually introduced and this control tests nothing")
    head = rat.split("## Rationale")[0]
    m = re.search(r"## Summary of rating action(.*?)\n##", rat, re.S)
    table = m.group(1) if m else head
    # every data row of the Summary table must carry NO bare numeric current-rated-amount -
    # "to be confirmed by issuer" or "Not applicable" only. A bare figure in ANY row (not just
    # Total) is the injected-break pattern this control exists to catch.
    bad_rows = []
    for line in table.splitlines():
        if not line.strip().startswith("|") or "Instrument" in line or "---" in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        current_amt = cells[2]
        if re.search(r"\d{1,3}(,\d{3})*\.\d{2}", current_amt) and \
                "confirmed" not in current_amt.lower():
            bad_rows.append(line.strip()[:80])
    check(not bad_rows, "row(s) in the Summary-of-rating-action table carry a NUMERIC current "
          "rated amount instead of 'to be confirmed by issuer': %s" % bad_rows)
    check("to be confirmed by issuer" in rat.lower(),
          "no 'to be confirmed by issuer' marking found for the ICRA rated amount")
    check(re.search(r"never (been )?imported|never substituted|not.{0,20}imported", rat, re.I)
          is not None,
          "rationale does not explicitly state that CRISIL/CareEdge amounts were not imported")
    check("2,000.00" in rat and "CRISIL" in rat, "CRISIL's own rated amount not shown as a "
          "labelled peer-agency reference")
    return "PEER AGENCY AMOUNTS CORRECTLY EXCLUDED"


# ------------------------------------------------------------------ G3 (compute_ratios.py itself)

# ------------------------------------------------------------------ G4 spreads
def g_spreads():
    if not SPREADS.exists():
        fails.append("MISSING WORKBOOK %s" % SPREADS.name)
        return "SPREADS OK"
    wb = openpyxl.load_workbook(SPREADS, data_only=True)
    for sh in ("Inputs", "RatioSuite", "TieOut", "RatingScore"):
        check(sh in wb.sheetnames, "spreads workbook missing sheet %s" % sh)
    if "TieOut" in wb.sheetnames:
        ws = wb["TieOut"]
        bad = tot = 0
        for r in range(6, ws.max_row + 1):
            c, d = ws.cell(row=r, column=3).value, ws.cell(row=r, column=4).value
            if isinstance(c, (int, float)) and isinstance(d, (int, float)):
                tot += 1
                if abs(c - d) > max(0.01, abs(d) * 0.005):
                    bad += 1
        check(tot >= 3, "only %d tie-out rows found" % tot)
        check(bad == 0, "%d of %d TieOut rows FAIL" % (bad, tot))
    return "SPREADS OK"


# ------------------------------------------------------------------ G5 Step 12
def g_step12():
    if not MODEL.exists():
        fails.append("MISSING MODEL %s" % MODEL.name)
        return "STEP 12 SATISFIED"
    wf = openpyxl.load_workbook(MODEL, data_only=False)
    wv = openpyxl.load_workbook(MODEL, data_only=True)
    need = ["Assumptions", "P_and_L", "Balance_Sheet", "Credit_Ratios", "Debt_Breakup",
            "Stress_Case"]
    for sh in need:
        check(sh in wf.sheetnames, "5-yr model missing sheet %s" % sh)
    blanks = 0
    for sh in wf.sheetnames:
        for r in range(6, wf[sh].max_row + 1):
            for c in range(3, wf[sh].max_column + 1):
                fv = wf[sh].cell(row=r, column=c).value
                if isinstance(fv, str) and fv.startswith("="):
                    if wv[sh].cell(row=r, column=c).value is None:
                        blanks += 1
    check(blanks == 0, "%d formula cells resolve to blank - a circular reference or broken "
          "link" % blanks)
    # funding-gap discipline (FM18): debt must be a FORMULA off assets/equity, never a bare
    # input constant carried forward from the historical trend
    debt_row = None
    for r in range(6, wf["Balance_Sheet"].max_row + 1):
        if "FUNDING GAP" in str(wf["Balance_Sheet"].cell(row=r, column=2).value or ""):
            debt_row = r
            break
    check(debt_row is not None, "no 'FUNDING GAP' debt row found in Balance_Sheet")
    if debt_row:
        fv = wf["Balance_Sheet"].cell(row=debt_row, column=3).value
        check(isinstance(fv, str) and fv.startswith("=") and "MAX" in fv,
              "the FUNDING GAP debt row is not a live formula derived from the balance sheet")
    return "STEP 12 SATISFIED"


# ------------------------------------------------------------------ G6 Step 12b
def g_step12b():
    if not SCORECARD.exists():
        fails.append("MISSING SCORECARD %s" % SCORECARD.name)
        return "STEP 12B SATISFIED"
    wv = openpyxl.load_workbook(SCORECARD, data_only=True)
    check("Rating" in wv.sheetnames, "scorecard missing Rating sheet")
    grade = wv["Rating"]["C12"].value if "Rating" in wv.sheetnames else None
    check(isinstance(grade, str) and len(grade) > 0,
          "scorecard's Rating!C12 (long-term anchor grade) is blank")
    check(bool(re.match(r"^(AAA|AA[+-]?|A[+-]?|BBB[+-]?|BB[+-]?|B[+-]?|C)$", grade or "")),
          "scorecard anchor grade '%s' is not a recognised LT grade" % grade)
    return "STEP 12B SATISFIED"


# ------------------------------------------------------------------ G7 delivery gate
def g_gate():
    import subprocess
    r = subprocess.run(
        [sys.executable, str(HERE.parents[1] / "check_sections.py"), str(RATIONALE)],
        capture_output=True, text=True)
    out = r.stdout + r.stderr
    check(r.returncode == 0, "check_sections.py exited %d" % r.returncode)
    check("[PASS]" in out, "check_sections.py output did not show [PASS]: %s" % out[-800:])
    return "DELIVERY GATE CLEAN"


# ------------------------------------------------------------------ G8 tariff driver
def g_earnings_decline_explained():
    """Replaces the former g_tariff_driver (abandoned 26-Aug-2026, see GATES.md G8A).

    The old gate REQUIRED the report to state a 28.1% North America revenue decline and to
    name tariffs as a driver. Both requirements were themselves defective:
      - the 28.1% (and the Rs 1,861.38 -> 1,338.48 crore pair behind it) does not appear
        anywhere in the document set; searches for the figures, for "north america", for
        "external customer" and for an Ind AS 108 geographic-revenue note all return zero;
      - "tariffs" entered the draft from CRISIL's and ICRA's own published rationales, which
        CLAUDE.md section 2 bars as a source of facts for a new report.
    A gate that mandates unsupported content will pass a wrong report and fail a right one,
    so it is replaced rather than relaxed. What the report genuinely must prove is that the
    FY2026 earnings fall is explained with traced arithmetic and that the latest quarter is
    quantified - both testable, and both from the company's own filings.
    """
    rat = read(RATIONALE)
    check("24.9%" in rat, "FY2026 PAT decline percentage not stated")
    check("290.01" in rat and "267.36" in rat,
          "the forex swing that explains the PAT decline is not quantified on both sides")
    check("557.37" in rat, "the two-year forex swing total is not stated")
    check("25.2%" in rat and "56.4%" in rat,
          "Q1 FY2027 revenue and PAT growth not both quantified")
    # Negative half: the unsupported operating-mix figures must not come back.
    for ghost in ["28.1%", "1,861.38", "1,338.48", "3,774.36", "3,044.22", "70.1%", "28.7%"]:
        check(ghost not in rat,
              "unsupported operating-mix figure %s is present; it is not in the "
              "document set" % ghost)
    return "EARNINGS DECLINE EXPLAINED"


# ------------------------------------------------------------------ G9 sector metrics
def g_sector_metrics():
    rat = read(RATIONALE)
    need = {
        "replacement/OEM mix": r"70\.1%|replacement",
        "export share": r"65%|export",
        "capacity": r"MTPA|capacity",
        "capex programme quantum": r"6,800 crore",
    }
    missing = [k for k, p in need.items() if not re.search(p, rat, re.I)]
    check(not missing, "missing sector metrics: %s" % ", ".join(missing))
    return "SECTOR METRICS PRESENT"


# ------------------------------------------------------------------ G11 OPM normalisation (FM36)
def g_opm_normalisation(control=False):
    """The gate this whole incident exists to enforce, run against THIS case's own artefacts.

    Checks (a) the rationale states the forex add-back and the two specific figures, (b) the
    ratio engine's OPBDITA function actually includes the add-back term, not just talks about
    it, and (c) the corrected FY2026 margin (>23%, i.e. a RISE from FY2025) appears rather than
    the original miscomputed 21.25% (a fall).
    """
    rat = read(RATIONALE)
    if control:
        rat = rat.replace("290.01", "0.00").replace("23.93", "21.25")
    check("290.01" in rat, "the Rs 290.01 crore forex-loss add-back is not named in the "
          "rationale")
    check("23.93" in rat, "the corrected FY2026 OPBDITA margin (23.93%) is not stated")
    # 21.25% may appear ONLY inside an explicit "from 21.25% to ..." withdrawal note - any
    # other occurrence means the old, wrong figure is still being asserted as current.
    stray = [m.start() for m in re.finditer(r"21\.25", rat)
             if not re.search(r"from\s+21\.25", rat[max(0, m.start() - 12):m.start() + 8])]
    check(not stray, "the pre-correction 21.25%% margin appears %d time(s) OUTSIDE a 'from "
          "21.25%% to ...' withdrawal note - it is still being asserted as current somewhere"
          % len(stray))
    engine = read(HERE / "compute_ratios.py")
    m = re.search(r"def opbdita\(p\):.*?\n\ndef ", engine, re.S)
    body = m.group(0) if m else engine
    check('"Non-op. in other expenses"' in body,
          "compute_ratios.py's opbdita() does not add back the non-operating-in-other-expenses "
          "line - the fix for failure mode 36 is not actually wired into the function")
    return "OPM NORMALISATION VERIFIED"


GATES = {"routing": g_routing, "peer_agency_amounts": g_peer_agency_amounts,
         "spreads": g_spreads, "step12": g_step12, "step12b": g_step12b, "gate": g_gate,
         "earnings_decline": g_earnings_decline_explained,
         "sector_metrics": g_sector_metrics,
         "opm_normalisation": g_opm_normalisation}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in GATES:
        print("usage: verify_bil.py {%s} [--control]" % "|".join(GATES))
        raise SystemExit(2)
    name = sys.argv[1]
    ctl = "--control" in sys.argv
    fn = GATES[name]
    try:
        token = fn(control=ctl) if fn.__code__.co_argcount else fn()
    except Exception as e:                                    # noqa: BLE001
        print("ORACLE ERROR: %s: %s" % (type(e).__name__, e))
        raise SystemExit(1)
    if ctl:
        if fails:
            print("CONTROL OK - oracle rejected the injected break (%d finding(s))"
                  % len(fails))
            raise SystemExit(0)
        print("CONTROL FAILED - oracle ACCEPTED a deliberately broken input; it proves nothing")
        raise SystemExit(1)
    for f in fails:
        print("FAIL:", f)
    if fails:
        print("%d assertion(s) failed" % len(fails))
        raise SystemExit(1)
    print(token)
