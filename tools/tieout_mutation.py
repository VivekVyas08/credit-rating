#!/usr/bin/env python3
"""Mutation harness for a case's tie-out suite (CLAUDE.md failure mode 39).

WHY THIS EXISTS
---------------
A tie-out suite tells you how many checks PASS. It does not tell you how much of the engine
those checks actually COVER, and the two are easy to confuse. Jindal Stainless, 26-Aug-2026,
reported "22/22 tie-outs reconcile" while:

  * FOUR of the 22 compared a value to ITSELF - the "EPS" checks read R[p]["EPS"] and
    PL["EPS basic"], which are the same cell. They could never fail in any circumstance.
  * The forex add-back - which turned out to be built on figures taken from the wrong
    statement entirely, wrong in magnitude AND sign - was covered by NO tie-out at all.
    PBILDT was tied to the company's published EBITDA, and the base reproduces that whether
    or not a spurious add-back sits on top of it. The tie-outs verified the base. Nothing
    verified the adjustment.

Counting passes cannot detect either problem. Mutation can: perturb an input, and if no
tie-out notices, that input is UNVERIFIED - either because nothing checks it, or because
whatever checks it moves in lockstep with it.

WHAT IT DOES
------------
For every numeric element of every input table in a case's compute_ratios.py, the harness
perturbs the value, re-runs compute() and tieouts(), and records whether any tie-out flipped
to failing. It then reports the inputs no tie-out is sensitive to.

HOW TO READ THE OUTPUT
----------------------
An unverified input is NOT automatically a defect. Some inputs legitimately have no
independent published figure to check against, and saying so explicitly is the whole point -
it converts a silent gap into a stated one. What is NOT acceptable is not knowing.

    python tieout_mutation.py <case-slug> [--delta 0.07] [--quiet]

Exit codes: 0 always (this is a coverage report, not a gate). Use --strict to exit 1 when the
unverified share exceeds --max-unverified.
"""

import argparse
import copy
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # this script now lives in tools/,
# one level below the project root - moved here 01-Sep-2026 to declutter the root.


def load_engine(slug):
    path = ROOT / "Companies" / slug / "compute_ratios.py"
    if not path.exists():
        sys.exit("no compute_ratios.py for case %r at %s" % (slug, path))
    # Compile from source every time - never serve a cached .pyc. See the note in
    # rate_engine.py: a stale __pycache__ entry once made the loader see a corrupted engine
    # while the file on disk was correct, which would silently invalidate every coverage
    # number this harness reports.
    import types
    sys.path.insert(0, str(path.parent))
    name = "case_engine_%s" % slug.replace("-", "_")
    mod = types.ModuleType(name)
    mod.__file__ = str(path)
    sys.modules[name] = mod
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), mod.__dict__)
    import engine_contract
    gap = engine_contract.require(mod, slug, "tieout_mutation.py")
    if gap:
        sys.exit(gap)
    return mod


def _numeric_list(v):
    """A series of numbers, tolerating None for periods the engine has no figure for.

    Requiring EVERY entry to be numeric silently discarded whole tables. Happy Forgings' main
    DATA dict carries `"norm_pat": [None, None, None]` for a figure the company does not
    disclose; that single row caused the entire table - 57 inputs - to be skipped, and the
    harness then measured only the seven loose series beside it and reported 28.6% as though
    it had looked at everything. A partial measurement presented as a complete one is worse
    than no measurement.
    """
    if not isinstance(v, list) or not v:
        return False
    for x in v:
        if isinstance(x, bool):
            return False
        if not isinstance(x, (int, float)) and x is not None:
            return False
    return True


def _has_number(table, idx):
    """At least one real number somewhere in the table - otherwise it is not data."""
    for v in table.values():
        series = v if idx is None else v[idx]
        if any(isinstance(x, (int, float)) and not isinstance(x, bool) for x in series):
            return True
    return False


def input_tables(mod):
    """Module-level dicts holding this engine's numeric inputs.

    TWO SHAPES are recognised, because both are in use across this project:

        {"Revenue": [1.0, 2.0, 3.0]}                 plain series
        {"CRAR (%)": ([1.0, 2.0], "source note")}    series carrying its own provenance

    The second form is used by the bank and NBFC engines (SBI, TVS Credit, Aptus and others),
    where each row records where it came from. The first version of this harness accepted only
    the plain form, so those engines reported "no input tables found" and were silently
    unmeasurable - the harness looked like it ran and told you nothing, which is precisely the
    hollow-check pattern it exists to detect. Returned as (dict, accessor) so the caller can
    mutate either shape without caring which it is.
    """
    out = {}
    for name in dir(mod):
        if name.startswith("_") or not name.isupper():
            continue
        obj = getattr(mod, name)
        if not isinstance(obj, dict) or not obj:
            continue
        vals = list(obj.values())
        if all(_numeric_list(v) for v in vals) and _has_number(obj, None):
            out[name] = (obj, None)
        elif (all(isinstance(v, tuple) and v and _numeric_list(v[0]) for v in vals)
              and _has_number(obj, 0)):
            out[name] = (obj, 0)          # series lives at position 0 of the tuple

    # THIRD SHAPE: bare module-level series, e.g. `rev_consol = [1.0, 2.0, 3.0]`. Several
    # engines (Yasho, HLE Glascoat, Dhampur) keep every input this way rather than in a dict,
    # and were invisible to this harness - reported as "no input tables found", which reads
    # like a clean result and is actually a refusal to measure. Names are lower-case here, so
    # the isupper() filter above misses them by design; they are collected separately and
    # presented as one pseudo-table.
    if not out:
        loose = {}
        for name in dir(mod):
            if name.startswith("_"):
                continue
            obj = getattr(mod, name)
            if _numeric_list(obj) and len(obj) <= 24:
                loose[name] = obj
        if loose:
            out["(module-level series)"] = (loose, None)
    return out


def series_of(table, key, idx):
    """The mutable numeric list for one row, whichever shape the table uses."""
    return table[key] if idx is None else table[key][idx]


def failing_count(mod):
    """Number of tie-outs currently failing. Tolerant of engines that raise mid-run."""
    try:
        R = mod.compute()
        T = mod.tieouts(R)
    except Exception:                                                     # noqa: BLE001
        return None
    bad = 0
    for row in T:
        try:
            _, comp, disc, tol, _ = row
            if abs(comp - disc) > tol:
                bad += 1
        except Exception:                                                 # noqa: BLE001
            continue
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--delta", type=float, default=0.07,
                    help="relative perturbation (default 7%%)")
    ap.add_argument("--floor", type=float, default=1.0,
                    help="absolute perturbation for near-zero inputs")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--max-unverified", type=float, default=100.0)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    mod = load_engine(args.slug)
    tables = input_tables(mod)
    if not tables:
        sys.exit("no input tables found - engine does not use the expected dict-of-lists shape")

    years = getattr(mod, "YEARS", None)
    baseline = failing_count(mod)
    if baseline is None:
        sys.exit("the engine raised before any mutation - fix it before measuring coverage")

    total = 0
    unverified = []
    originals = {name: copy.deepcopy(tbl) for name, (tbl, _ix) in tables.items()}

    for name, (tbl, ix) in tables.items():
        for key in list(tbl):
            series = series_of(tbl, key, ix)
            for i in range(len(series)):
                base = series[i]
                if base is None:            # no figure for this period - nothing to perturb
                    continue
                bump = abs(base) * args.delta
                if bump < args.floor:
                    bump = args.floor
                series[i] = base + bump
                total += 1
                after = failing_count(mod)
                series[i] = base                              # restore immediately
                if after is None or after <= (baseline or 0):
                    label = years[i] if years and i < len(years) else "col%d" % i
                    unverified.append((name, key, label, base))

        # belt and braces: restore every series from its pristine copy
        for key in tbl:
            series_of(tbl, key, ix)[:] = (originals[name][key] if ix is None
                                          else originals[name][key][ix])

    covered = total - len(unverified)
    pct = 100.0 * covered / total if total else 0.0

    print("=" * 88)
    print("TIE-OUT COVERAGE BY MUTATION - %s" % args.slug)
    print("=" * 88)
    print("inputs perturbed        : %d" % total)
    print("changed a tie-out       : %d" % covered)
    print("changed NOTHING         : %d" % len(unverified))
    print("coverage                : %.1f%%  <- ARITHMETIC SELF-CONSISTENCY ONLY" % pct)
    if baseline:
        print("NOTE: %d tie-out(s) already failing at baseline" % baseline)
    # Added 13-Sep-2026. Dhampur Bio Organics scored 100.0% here and shipped with the wrong
    # analytical basis, a rated amount overstated by Rs 72.40 crore, liquidity overstated ~8x
    # and the sector's defining operating metric absent. The number was true and it was read as
    # assurance it could never provide, so it now states its own limit on every run.
    print("")
    print("WHAT THIS NUMBER MEANS: no input can be changed without some tie-out noticing.")
    print("WHAT IT DOES NOT MEAN: that the figures were read off the right STATEMENT, for the")
    print("  right PERIOD, on the right DEFINITION, or that the metric that matters most in")
    print("  this sector is present at all. A report built on the wrong basis is perfectly")
    print("  self-consistent and scores 100%%. For that, run: tools/step14_diff.py %s"
          % args.slug)

    if unverified and not args.quiet:
        print("\n" + "-" * 88)
        print("INPUTS NO TIE-OUT IS SENSITIVE TO")
        print("-" * 88)
        print("Each of these can be changed without any tie-out noticing. That is not")
        print("automatically a defect - some inputs have no independently published figure to")
        print("check against. It IS a defect to not know which is which, so decide for each:")
        print("either add a check, or state in DISCLOSED_DIFFERENCES that none is possible.\n")
        by_table = {}
        for name, key, label, base in unverified:
            by_table.setdefault(name, []).append((key, label, base))
        for name in sorted(by_table):
            print("  %s" % name)
            for key, label, base in by_table[name]:
                print("      %-42s %-8s %12.2f" % (key[:42], label, base))

    if args.strict and pct < (100.0 - args.max_unverified):
        sys.exit(1)


if __name__ == "__main__":
    main()
