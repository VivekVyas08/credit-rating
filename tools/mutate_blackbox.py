#!/usr/bin/env python3
"""Measure tie-out coverage of ANY engine, without refactoring it.

    python mutate_blackbox.py <case-slug> [--sample N] [--delta 0.07]

WHY THIS EXISTS
---------------
`tieout_mutation.py` measures coverage by importing the engine and calling `compute()` and
`tieouts()`. That is fast and precise, but only 4 of this project's 21 engines expose those
functions - the rest are top-level scripts whose checks live inside `run()`. Those engines were
therefore UNMEASURABLE, and an unmeasurable engine is indistinguishable from an unverified one.

This harness needs no contract at all. It edits a numeric literal in the engine's SOURCE, runs
the script as a subprocess, and reads the reconcile line the engine already prints:

    "34/34 tie-outs reconcile"   /   "2 of 18 tie-outs FAIL"

If the count of failures does not rise when a figure is changed, nothing in that engine checks
that figure. That is the same question `tieout_mutation.py` asks, answered from the outside.

COST AND LIMITS
---------------
One subprocess per mutated literal, so it is far slower - use `--sample N` to test a random
subset and extrapolate. It also only sees literals inside data tables (it skips comments,
strings and anything outside a `KEY = {...}` block), and an engine that prints no reconcile
line cannot be measured by any means short of reading it.
"""

import argparse
import random
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # this script now lives in tools/,
# one level below the project root - moved here 01-Sep-2026 to declutter the root.
RECON = re.compile(r"(\d+)\s*/\s*(\d+)\s+(?:tie-outs?|checks?)?\s*reconcile", re.I)
FAILS = re.compile(r"(\d+)\s+of\s+(\d+)\s+tie-outs?\s+FAIL", re.I)
NUMBER = re.compile(r"(?<![\w.])(-?\d+\.\d+)(?![\w.])")


def failures(src_path, cwd):
    r = subprocess.run([sys.executable, str(src_path)], cwd=str(cwd),
                       capture_output=True, text=True, timeout=300)
    out = (r.stdout or "") + (r.stderr or "")
    if "Traceback" in out:
        return None, out
    m = FAILS.search(out)
    if m:
        return int(m.group(1)), out
    m = RECON.search(out)
    if m:
        return int(m.group(2)) - int(m.group(1)), out
    return None, out


def data_spans(src):
    """Character ranges of `NAME = {...}` blocks - where an engine keeps its extracted data."""
    spans = []
    for m in re.finditer(r"^[A-Z_][A-Z_0-9]*\s*=\s*\{", src, re.M):
        depth, i = 0, m.end() - 1
        while i < len(src):
            if src[i] == "{":
                depth += 1
            elif src[i] == "}":
                depth -= 1
                if depth == 0:
                    spans.append((m.start(), i))
                    break
            i += 1
    return spans


def candidates(src):
    spans = data_spans(src)
    if not spans:
        return []
    out = []
    for m in NUMBER.finditer(src):
        a = m.start()
        if any(s <= a <= e for s, e in spans):
            line = src[src.rfind("\n", 0, a) + 1: src.find("\n", a)]
            if line.lstrip().startswith("#"):
                continue
            out.append((a, m.end(), m.group(1)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--sample", type=int, default=0, help="test N random literals (0 = all)")
    ap.add_argument("--delta", type=float, default=0.07)
    ap.add_argument("--floor", type=float, default=1.0)
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    d = ROOT / "Companies" / args.slug
    engine = d / "compute_ratios.py"
    if not engine.exists():
        sys.exit("no compute_ratios.py for %r" % args.slug)
    src = engine.read_text(encoding="utf-8")

    base, out = failures(engine, d)
    if base is None:
        print("=" * 88)
        print("BLACK-BOX COVERAGE - %s" % args.slug)
        print("=" * 88)
        print("  NOT MEASURABLE: the engine prints no reconcile line, so it reports no")
        print("  tie-outs at all. Coverage is not low here - it is undefined, because there")
        print("  is nothing to be covered BY. This engine needs tie-outs before it needs")
        print("  measuring; see Companies/jindal-stainless/compute_ratios.py for the shape.")
        return

    cands = candidates(src)
    if args.sample and len(cands) > args.sample:
        random.seed(args.seed)
        cands = random.sample(cands, args.sample)

    tmp = Path(tempfile.mkdtemp()) / "compute_ratios.py"
    covered = 0
    misses = []
    for a, b, lit in cands:
        val = float(lit)
        bump = abs(val) * args.delta
        if bump < args.floor:
            bump = args.floor
        mutated = src[:a] + repr(round(val + bump, 4)) + src[b:]
        (d / "_mut_tmp.py").write_text(mutated, encoding="utf-8")
        try:
            after, _ = failures(d / "_mut_tmp.py", d)
        finally:
            (d / "_mut_tmp.py").unlink(missing_ok=True)
        if after is not None and after > base:
            covered += 1
        else:
            line_no = src.count("\n", 0, a) + 1
            line = src[src.rfind("\n", 0, a) + 1: src.find("\n", a)].strip()
            misses.append((line_no, lit, line[:70]))

    n = len(cands)
    print("=" * 88)
    print("BLACK-BOX COVERAGE - %s" % args.slug)
    print("=" * 88)
    print("  literals tested   : %d%s" % (n, " (sampled)" if args.sample else " (all)"))
    print("  changed a tie-out : %d" % covered)
    print("  changed NOTHING   : %d" % len(misses))
    print("  coverage          : %.1f%%" % (100.0 * covered / n if n else 0.0))
    if base:
        print("  NOTE: %d tie-out(s) already failing before any mutation" % base)
    if misses:
        print("\n  first unverified literals (line, value, context):")
        for ln, lit, ctx in misses[:12]:
            print("    L%-5d %-12s %s" % (ln, lit, ctx))


if __name__ == "__main__":
    main()
