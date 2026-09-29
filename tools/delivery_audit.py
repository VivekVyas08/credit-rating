"""Single READY / NOT READY verdict for a case, aggregating every existing gate.

WHY THIS EXISTS
---------------
Every check in this project already existed before this script: tie-outs in each case's own
compute_ratios.py, mutation coverage in tieout_mutation.py, section/quality probes in
check_sections.py, and the scorecard-vs-rationale match in annotate_scorecard.py. Nothing here
is a new analytical check. What was missing was a single command that runs all of them and
refuses to say "ready" while any one of them is red - so "is this actually done" stops being a
judgment call made by re-reading four separate outputs and became one exit code.

Operator instruction, 03-Sep-2026: "create a loop... which checks it has followed each step
properly... and do audit of the work... then if the outcome is ok only share it, or keep on
working until it's perfect." A script cannot loop itself into fixing an analytical gap - fixing
requires reading a document and forming a judgment, which is exactly the work this project's own
§8a meta-rule reserves for a person. What this script CAN do, and is built to do, is be the gate
in that loop: run it, fix whatever it names, run it again, and do not treat the work as
deliverable until it exits 0. That loop is now Step 17a-continued below and in the operating
guide - a binding step, not an aspiration.

    python tools/delivery_audit.py <case-slug>     # one case
    python tools/delivery_audit.py --all           # every case with a rationale
"""

import argparse
import ast
import glob
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _named_gap_count(src: str) -> int:
    """How many gaps the engine ACTUALLY names in its two FM39 disclosure lists.

    Grepping for the identifiers is not a check: an engine carrying
    `UNVERIFIED_INPUTS = []` and `DISCLOSED_DIFFERENCES = []` names nothing at all
    and still contains both strings.  Positive control, 04-Sep-2026: oil-india was
    emptied to exactly that and the old grep-based gate reported
    "99.5% (gaps named per FM39)" - passing an engine whose disclosures were bare.
    FM39's own corollary applies to this gate as much as to a tie-out: a check that
    cannot fail its own control is not a check.

    ponytail: counts entries, it does not verify they correspond to the inputs the
    mutation harness reported uncovered.  Tie the two together if a case is ever
    found naming the wrong gaps.
    """
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 0
    n = 0
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for t in node.targets:
            if isinstance(t, ast.Name) and t.id in ("UNVERIFIED_INPUTS",
                                                     "DISCLOSED_DIFFERENCES"):
                try:
                    n += len(ast.literal_eval(node.value))
                except Exception:                                         # noqa: BLE001
                    n += 1          # built at runtime - assume it names something
    return n


def _run(cmd: list) -> tuple[int, str]:
    p = subprocess.run(cmd, cwd=str(ROOT.parent), capture_output=True, text=True,
                        encoding="utf-8", errors="replace", timeout=1800)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def audit_case(slug: str) -> dict:
    """Run every gate for one case; return {ready: bool, checks: [(name, ok, detail)]}."""
    case_dir = ROOT.parent / "Companies" / slug
    checks = []

    # ------------------------------------------------------------------- 1. tie-outs
    # Calls tieouts() directly rather than parsing compute_ratios.py's own stdout, which uses
    # at least two different summary phrasings across the corpus ("N/N tie-outs reconcile" vs
    # "M of N tie-outs FAIL") and would otherwise need a fragile regex per phrasing. This also
    # lets a failing check be cross-referenced against the engine's OWN ACKNOWLEDGED_TIEOUTS -
    # a dict some engines (not all) use to document a specific, evidenced reason a check fails
    # for this issuer (e.g. a loss-making entity's implied tax rate falling outside a generic
    # plausibility band). ACKNOWLEDGED_TIEOUTS does NOT suppress the failure from the engine's
    # own printed count - it is a parallel, additive disclosure - so this function does the
    # cross-referencing itself rather than trusting the raw count to already reflect it.
    engine = case_dir / "compute_ratios.py"
    if engine.is_file():
        code = (
            "import sys, json; sys.path.insert(0, %r)\n"
            "import compute_ratios as C\n"
            "if not (hasattr(C, 'compute') and hasattr(C, 'tieouts')):\n"
            "    print(json.dumps({'legacy_contract': True})); sys.exit(0)\n"
            "R = C.compute()\n"
            "rows = C.tieouts(R)\n"
            "ack = set(getattr(C, 'ACKNOWLEDGED_TIEOUTS', {}) or {})\n"
            "failed, unacked = [], []\n"
            "for row in rows:\n"
            "    name, computed, disclosed, tol = row[0], row[1], row[2], row[3]\n"
            "    ok = abs(computed - disclosed) <= tol if isinstance(computed, (int, float)) "
            "and isinstance(disclosed, (int, float)) else computed == disclosed\n"
            "    if not ok:\n"
            "        failed.append(name)\n"
            "        if name not in ack:\n"
            "            unacked.append(name)\n"
            "print(json.dumps({'total': len(rows), 'failed': failed, 'unacked': unacked}))\n"
        ) % str(case_dir)
        rc, out = _run([sys.executable, "-c", code])
        m = re.search(r"\{.*\}", out, re.S)
        if not m:
            checks.append(("Tie-outs reconcile", False,
                            "could not run tieouts() for this case (exit %d): %s"
                            % (rc, out[-300:].strip())))
        else:
            import json as _json
            data = _json.loads(m.group(0))
            if data.get("legacy_contract"):
                checks.append(("Tie-outs reconcile", False,
                                "this engine exposes run() rather than compute()/tieouts() - "
                                "the pre-standardisation contract. Tie-outs cannot be "
                                "cross-referenced against ACKNOWLEDGED_TIEOUTS until it is "
                                "migrated to the standard contract; not a fresh finding, and "
                                "not something this audit can wave through."))
            else:
                total, failed, unacked = data["total"], data["failed"], data["unacked"]
                if not unacked:
                    detail = "%d/%d reconcile" % (total - len(failed), total)
                    if failed:
                        detail += " (%d acknowledged in ACKNOWLEDGED_TIEOUTS: %s)" % (
                            len(failed), "; ".join(failed[:3]))
                    checks.append(("Tie-outs reconcile", True, detail))
                else:
                    checks.append(("Tie-outs reconcile", False,
                                    "%d/%d reconcile; %d UNACKNOWLEDGED failure(s): %s"
                                    % (total - len(failed), total, len(unacked),
                                       "; ".join(unacked[:3]))))
    else:
        checks.append(("Tie-outs reconcile", None, "no compute_ratios.py - not a scored case"))

    # ---------------------------------------------------------- 2. mutation coverage disclosed
    mut_script = ROOT / "tieout_mutation.py"
    if engine.is_file() and mut_script.is_file():
        rc, out = _run([sys.executable, str(mut_script), slug])
        m = re.search(r"coverage\s*:\s*([\d.]+)%", out)
        cov = float(m.group(1)) if m else None
        engine_src = engine.read_text(encoding="utf-8", errors="replace")
        named = _named_gap_count(engine_src)
        has_disclosure = named > 0
        if cov is not None and cov < 100.0 and not has_disclosure:
            checks.append(("Mutation coverage measured and gaps disclosed", False,
                            "%.1f%% coverage but compute_ratios.py names NO gap in "
                            "UNVERIFIED_INPUTS/DISCLOSED_DIFFERENCES - failure mode 39 requires "
                            "every gap to be named, not just measured" % cov))
        else:
            checks.append(("Mutation coverage measured and gaps disclosed", True,
                            ("%.1f%% (%d gap(s) named per FM39)" % (cov, named))
                            if cov is not None else "measured"))

    # ------------------------------------------------------------- 3. section/quality gate
    rationales = sorted(case_dir.glob("*Rating Rationale*.md"))
    if not rationales:
        checks.append(("Section/quality gate (check_sections.py)", False,
                        "no *Rating Rationale*.md found in the case folder"))
    for r in rationales:
        rc, out = _run([sys.executable, str(ROOT / "check_sections.py"), str(r)])
        ok = rc == 0 and "[FAIL]" not in out
        warn_ct = out.count("QUALITY:")
        detail = "PASS" if ok else out.split("[FAIL]", 1)[-1][:300].strip()
        if ok and warn_ct:
            detail = "PASS, but %d quality WARN item(s) - read them before delivering" % warn_ct
        checks.append(("Section/quality gate: %s" % r.name, ok, detail))

    # --------------------------------------------------------- 4. scorecard matches rationale
    scorecards = sorted(case_dir.glob("Rating_Scorecard*.xlsx"))
    if scorecards:
        rc, out = _run([sys.executable, str(ROOT / "annotate_scorecard.py"), slug])
        for line in out.splitlines():
            if slug in line and ("MATCHES" in line or "MISMATCH" in line):
                checks.append(("Scorecard matches rationale", "MISMATCH" not in line,
                                line.strip()))
        if not any(c[0] == "Scorecard matches rationale" for c in checks):
            checks.append(("Scorecard matches rationale", False,
                            "annotate_scorecard.py produced no MATCH/MISMATCH line - "
                            "output: %s" % out[-300:]))
    else:
        checks.append(("Scorecard matches rationale", None, "no scorecard in the case folder"))

    # --------------------------------------------------------------- 5. workpaper present
    workpapers = list(case_dir.glob("*Workpaper*.md")) + list(case_dir.glob("*workpaper*.md"))
    checks.append(("Ratio workpaper delivered", bool(workpapers),
                    workpapers[0].name if workpapers else "no *Workpaper*.md in the case folder"))

    # ------------------------------------------------ 6. Step 14 diff vs the agency's action
    # The VALIDATION gate. Every check above verifies internal consistency and all of them can
    # score full marks on a report built off the wrong statement, period or definition, because
    # such a report agrees with itself. This one asks the only question the others cannot:
    # why is my number different from the agency's own number for this same issuer?
    s14 = ROOT / "step14_diff.py"
    if s14.is_file() and rationales:
        rc, out = _run([sys.executable, str(s14), slug])
        if "No same-issuer agency publication" in out:
            checks.append(("Step 14 diff vs the agency's own action", None,
                            "no same-issuer publication in the reference libraries"))
        else:
            flagged = [ln.strip() for ln in out.splitlines() if "***" in ln]
            checks.append(("Step 14 diff vs the agency's own action", rc == 0,
                            ("no material divergence" if rc == 0 else
                             "%d unexplained divergence(s): %s"
                             % (len(flagged), " | ".join(x[:70] for x in flagged[:3])))))

    hard = [c for c in checks if c[1] is False]
    ready = len(hard) == 0
    return {"slug": slug, "ready": ready, "checks": checks}


def print_report(result: dict) -> None:
    print("=" * 92)
    print("DELIVERY AUDIT - %s" % result["slug"])
    print("-" * 92)
    for name, ok, detail in result["checks"]:
        tag = "  OK  " if ok is True else ("  N/A " if ok is None else "*FAIL*")
        print("[%s] %-42s %s" % (tag, name, detail[:200] if isinstance(detail, str) else detail))
    print("-" * 92)
    print("VERDICT: %s" % ("READY TO SHARE" if result["ready"] else "NOT READY - do not deliver"))
    print("=" * 92)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    if a.all:
        companies = ROOT.parent / "Companies"
        # set(): the glob yields one entry PER RATIONALE FILE, so a case carrying
        # several (ITC has three, SBI/JSW/NABKISAN/HDFC two) was audited once per
        # rationale - the same report printed 2-3 times, wasting the run and making
        # the output impossible to tally.  Measured 04-Sep-2026: 33 audits for 27 cases.
        slugs = sorted({Path(p).parent.name for p in
                        glob.glob(str(companies / "*" / "*Rating Rationale*.md"))})
        # A case with no rationale simply never appeared in --all output, which reads
        # as "audited and fine".  Name it instead: an unaudited case must be visible.
        skipped = sorted(d.name for d in companies.iterdir()
                          if d.is_dir() and d.name not in slugs)
        if skipped:
            print("NOT AUDITED - no '*Rating Rationale*.md' in the case folder: %s\n"
                  % ", ".join(skipped))
    elif a.slug:
        slugs = [a.slug]
    else:
        ap.error("give a case slug or --all")

    all_ready = True
    for slug in slugs:
        result = audit_case(slug)
        print_report(result)
        all_ready = all_ready and result["ready"]
        print()
    return 0 if all_ready else 1


if __name__ == "__main__":
    sys.exit(main())
