"""Add the BUSINESS-RISK GATE to Rating_Scorecard.xlsx and every filled case workbook.

WHY (failure mode 53, Cochin Minerals and Rutile Limited, 13-Sep-2026):
`Scorecard!E22` computes the Stage 1 composite as
    SUM(E17:E20)/SUM(D17:D20)
i.e. it takes a WEIGHTED AVERAGE of Industry risk, Business risk, Financial risk and
Management. That is the defect. Neither ICRA's Corporate Credit Rating Methodology nor
CareEdge's Manufacturing methodology gives ANY formula for converting a business-risk
judgement ("small scale", "single-product concentration") into a number of notches - both
score Financial Risk against explicit numeric bands and Business Risk in descriptive
language only. Averaging an invented business number against a real financial one lets a
debt-free small issuer's financial cleanliness outvote the business weakness that should
have bounded it. CMRL: gearing 0.04x and interest coverage 122x carried the composite to an
AA- anchor, delivered CARE A-, against CareEdge's own published BBB. Two notches.

WHAT THIS ADDS - the gate BOUNDS Stage 1, it is never averaged into it:
  Scorecard!B37:D43   the gate block. Computes the business-vs-financial divergence and
                      raises a flag; reads the ceiling the analyst entered.
  Inputs!B68:F70      the ceiling grade + its written justification (the input side).
  Rating!C15          the anchor index now takes MAX(caps result, ceiling index). Index 0 is
                      AAA and 16 is C, so a ceiling on the achievable GRADE is a floor on the
                      INDEX - MAX is the correct operator, and MAX(x, 0) is a no-op when no
                      ceiling is set, so an untouched workbook behaves exactly as before.
  Rating!B19          a one-line note so the sheet explains the gate on its own face.

DESIGN NOTE - why the flag is derived but the ceiling is typed. The project's own rule is
that a number which can be derived must be derived (Rating!C34). But deriving the CEILING
itself would re-commit the original error: inventing a business-risk-score-to-notch formula
that neither agency publishes. So the sheet derives what it legitimately can - that business
risk is materially weaker than financial risk, and therefore that this case is one where the
averaging defect bites - and requires a human ceiling with a written reason, exactly the way
`Inputs!C67`/`D67` handles a hard-cap disapplication. That pattern is already proven here.

USAGE
    python tools/add_business_risk_gate.py            # template + every case workbook
    python tools/add_business_risk_gate.py <slug>     # one case
    python tools/add_business_risk_gate.py --selftest # positive control, writes nothing
"""
import shutil
import sys
from pathlib import Path

from copy import copy

from openpyxl import Workbook, load_workbook

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "Rating_Scorecard.xlsx"
COMPANIES = ROOT / "Companies"

# Divergence at which the gate fires. Two points on the 1-6 scale is a full band - the
# distance between "strong" and "moderate" - and is the smallest gap at which averaging can
# move the anchor by more than the map's own +/-1 screening tolerance. Below that the
# composite and the gate agree anyway, so a lower threshold would fire on cases it cannot
# change and train the reader to ignore it.
GATE_TRIGGER = 2


def _set(ws, coord, value, bold=False):
    c = ws[coord]
    c.value = value
    if bold:
        f = copy(c.font)
        f.bold = True
        c.font = f
    return c


def add_gate(path: Path) -> str:
    """Add the gate to one workbook. Idempotent - re-running does not double-apply."""
    wb = load_workbook(path)
    if "Scorecard" not in wb.sheetnames or "Rating" not in wb.sheetnames:
        return f"SKIP {path.name} - not a three-stage scorecard"
    sc, rt, ip = wb["Scorecard"], wb["Rating"], wb["Inputs"]

    # ---- input side -------------------------------------------------------------------
    _set(ip, "B68", "BUSINESS-RISK GATE (failure mode 53) - business risk BOUNDS the "
                    "anchor; it is never averaged into it", bold=True)
    _set(ip, "B69", "Business-risk ceiling grade (blank = no ceiling)")
    if ip["C69"].value is None:
        _set(ip, "C69", "")
    _set(ip, "D69", ip["D69"].value or "")
    _set(ip, "F69",
         "Enter the BEST grade this issuer can reach on its business risk alone (AAA..C), "
         "regardless of how strong the financial ratios are - e.g. a single-site, "
         "single-product issuer with no pricing power. A written reason in D69 is REQUIRED "
         "whenever the gate below reports YES, and the delivery gate reads it. Leaving it "
         "blank is a decision, not a default: say in D69 why no ceiling applies.")

    # ---- the gate block ---------------------------------------------------------------
    _set(sc, "B37", "3 - BUSINESS-RISK GATE (failure mode 53)", bold=True)
    _set(sc, "B38", "Neither ICRA nor CareEdge publishes a business-risk-to-notch formula. "
                    "Their Financial Risk factors carry numeric bands; their Business Risk "
                    "factors are descriptive only. So business risk sets a CEILING here - it "
                    "is not scored into the Stage 1 composite above.")
    _set(sc, "B39", "Business risk score (1-6)")
    _set(sc, "C39", "=C18")
    _set(sc, "B40", "Financial risk score (1-6)")
    _set(sc, "C40", "=C19")
    _set(sc, "B41", "Business weaker than financial by")
    _set(sc, "C41", "=C39-C40")
    _set(sc, "B42", "GATE")
    _set(sc, "C42", f'=IF(C41>={GATE_TRIGGER},"YES - set a ceiling in Inputs!C69 or state in '
                    f'Inputs!D69 why none applies","No - business and financial risk agree '
                    f'within one band")')
    _set(sc, "B43", "Ceiling grade entered (Inputs!C69)")
    _set(sc, "C43", "=Inputs!C69")
    _set(sc, "D43", "=Inputs!D69")
    # Returns 0 (the AAA index), not "", when no ceiling is set. 0 is the identity for the
    # MAX in Rating!C15, so an unset ceiling is a no-op either way - but a cell that
    # evaluates to blank is indistinguishable from a formula that was never recalculated,
    # and trips the "scorecard carries cached values" probe on every workbook. Found by that
    # probe firing on four cases immediately after this gate was first applied.
    _set(sc, "B44", "Ceiling index (0 = none/AAA ... 16 = C)")
    _set(sc, "C44", '=IF(Inputs!C69="",0,IFERROR(MATCH(Inputs!C69,Ref_Scales!$A$5:$A$21,0)-1,0))')

    # ---- bind it into the anchor ------------------------------------------------------
    # Wrap, never replace: the existing expression is the hard-cap chain and stays exactly as
    # it is. If it has already been wrapped, leave it alone.
    cur = str(rt["C15"].value or "")
    # Migrate the first version of this wrapper, which guarded against a blank C44 that no
    # longer occurs. Left in place it keeps the blank-cell false positive alive.
    _OLD = ',IF(OR(Scorecard!C44="",Scorecard!C44="BAD GRADE"),0,Scorecard!C44))'
    if _OLD in cur:
        cur = cur.replace(_OLD, ",Scorecard!C44)")
        _set(rt, "C15", cur)
    if "Scorecard!C44" not in cur:
        inner = cur[1:] if cur.startswith("=") else cur
        _set(rt, "C15", f"=MAX({inner},Scorecard!C44)")
    _set(rt, "B19", "Stage 1 is bounded above by the business-risk ceiling (Scorecard!B37) - "
                    "a ceiling on the grade is a floor on the index, so it is applied to C15 "
                    "as a MAX. With no ceiling set it has no effect.")

    wb.save(path)
    return f"OK   {path.relative_to(ROOT)}"


def selftest() -> int:
    """Positive control: build a minimal workbook, apply the gate, and confirm that
    (a) the ceiling actually binds the anchor index, and (b) no ceiling is a no-op.

    Formulas are not evaluated by openpyxl, so the arithmetic is checked directly here
    against the same MAX rule the sheet uses - what the workbook test proves is that the
    wrapper was written, points at the right cell, and did not clobber the cap chain.
    """
    ok = True
    tmp = ROOT / "tools" / "_brgate_selftest.xlsx"
    wb = Workbook()
    for n in ("Scorecard", "Rating", "Inputs", "Ref_Scales"):
        wb.create_sheet(n)
    del wb[wb.sheetnames[0]]
    wb["Rating"]["C15"] = "=IF(Inputs!C67=\"N\",C13,MAX(C13,13))"
    wb.save(tmp)
    try:
        add_gate(tmp)
        got = str(load_workbook(tmp)["Rating"]["C15"].value)
        wrapped = got == '=MAX(IF(Inputs!C67="N",C13,MAX(C13,13)),Scorecard!C44)'
        print(f"[{'OK' if wrapped else 'FAIL'}] C15 wraps the cap chain, does not replace it")
        print(f"       -> {got}")
        ok &= wrapped
        add_gate(tmp)
        again = str(load_workbook(tmp)["Rating"]["C15"].value)
        idem = again == got
        print(f"[{'OK' if idem else 'FAIL'}] re-running does not double-wrap")
        ok &= idem
    finally:
        tmp.unlink(missing_ok=True)

    # The arithmetic the sheet relies on: index 0 = AAA (best), 16 = C (worst).
    def anchor(cap_result, ceiling):
        return max(cap_result, 0 if ceiling == "" else ceiling)

    cases = [
        ("no ceiling is a no-op", anchor(4, ""), 4),
        ("ceiling binds a too-good anchor", anchor(4, 9), 9),   # AA- screened, BBB ceiling
        ("ceiling does not improve a worse anchor", anchor(13, 9), 13),
    ]
    for name, got, want in cases:
        good = got == want
        print(f"[{'OK' if good else 'FAIL'}] {name} -> {got} (want {want})")
        ok &= good
    return 0 if ok else 1


def main(argv):
    if len(argv) > 1 and argv[1] == "--selftest":
        return selftest()
    targets = []
    if len(argv) > 1:
        targets = sorted((COMPANIES / argv[1]).glob("Rating_Scorecard*.xlsx"))
        if not targets:
            print(f"no scorecard found for case '{argv[1]}'")
            return 1
    else:
        if TEMPLATE.exists():
            shutil.copy2(TEMPLATE, TEMPLATE.with_suffix(".xlsx.bak"))
            targets.append(TEMPLATE)
        targets += sorted(COMPANIES.glob("*/Rating_Scorecard*.xlsx"))
    for p in targets:
        print(add_gate(p))
    print(f"\n{len(targets)} workbook(s) processed. Now run:")
    print("    python tools/recalc_workbook.py <workbook>   # so cached values follow")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
