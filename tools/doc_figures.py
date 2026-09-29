#!/usr/bin/env python3
"""Every number that actually appears in a case's source documents, for corroboration checks.

    python doc_figures.py <case-slug>          # build/refresh the index
    python doc_figures.py <case-slug> --report # what is and is not corroborated

WHY
---
An engine's figure is only trustworthy if it came from the documents. Most engines in this
project hold summary figures - revenue, PBT, total assets - with no components to sum, so the
"derive the subtotal and tie it to the printed row" pattern has nothing to work with. There is
still a check available, and it is a real one:

    does this exact figure appear anywhere in the source documents?

A transcription error almost never survives that. 66.55 typed for 6.65, 185.53 copied into the
wrong year, a digit dropped from 240,742 - none of them will be found. It is mechanical, it
works on every engine regardless of shape, and because a mutated value stops being present, it
registers properly on the coverage harness.

WHAT IT DOES NOT PROVE
----------------------
Presence is not correctness. A figure can appear in the documents and still be the WRONG figure
for the line it was put against - the right number from the wrong year, the wrong entity, or the
standalone column instead of the consolidated one. That is failure mode 30, and this check is
blind to it. It is a corroboration floor beneath the labelled tie-outs, never a substitute for
them: only a check that names WHICH printed row a figure came from can catch a right-number-
wrong-place error.

Indian filings state figures in crore or in lakh, with or without thousands separators and with
Indian digit grouping, so each value is searched in every one of those forms.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # this script now lives in tools/,
# one level below the project root - moved here 01-Sep-2026 to declutter the root.
NUM = re.compile(r"\d[\d,]*\.?\d*")


def _variants(v):
    """Every way an Indian filing might print this value - and NO looser than that.

    THE FIRST VERSION OF THIS FUNCTION MADE THE WHOLE CHECK WORTHLESS, and it is worth saying
    exactly how. It generated each value at three scales and rounded to 0, 1 and 2 decimals,
    with western and Indian grouping - dozens of candidate strings per figure. Against an index
    of 8,000-19,000 numeric tokens, something always matched: measured on 29-Aug-2026, **100%
    of randomly generated WRONG values were "corroborated"** for vedanta and jsw-steel. The
    check passed everything, which is the precise failure mode this project keeps rediscovering
    - a test that cannot fail is not a test.

    So the match is now EXACT to two decimals, in crore and in lakh only, with the three ways
    those are printed (plain, western grouping, Indian grouping). A figure that appears in the
    documents rounded - "2,215" for 2,214.64 - is NOT matched, and that is the right trade:
    a missed corroboration is a stated gap, a false one is a lie. The measured false-positive
    rate under this definition is reported by `--selftest`.
    """
    out = set()
    for scale in (1.0, 100.0):                       # crore, and the same figure in lakh
        x = round(v * scale, 2)
        if abs(x) < 1.0:
            continue
        s = "%.2f" % x
        whole, _, frac = s.partition(".")
        out.add(s)
        out.add("{:,}".format(int(whole)) + "." + frac)
        w = whole.lstrip("-")
        indian = None
        if len(w) > 3:                               # Indian grouping: 1,09,333.55
            head, tail = w[:-3], w[-3:]
            parts = []
            while len(head) > 2:
                parts.insert(0, head[-2:])
                head = head[:-2]
            if head:
                parts.insert(0, head)
            indian = ",".join(parts) + "," + tail
            out.add(indian + "." + frac)
        if frac == "00":                             # integers are printed without decimals
            out.add(whole)
            out.add("{:,}".format(int(whole)))
            if indian:
                # The Indian-grouped INTEGER form was missing, and it is the commonest way a
                # lakh-denominated statement prints a round figure. Creative Newtech's FY2026
                # revenue of 2,699.77 crore appears in its documents as "2,69,977" - four
                # times - and was reported as NOT corroborated purely because this one string
                # shape was not generated. A false negative is less dangerous than a false
                # positive, but it still sends you hunting for a problem that is not there.
                out.add(indian)
    return out


def index_path(slug):
    return ROOT / "Companies" / slug / "documents_figures.json"


def build(slug):
    d = ROOT / "Companies" / slug / "documents"
    if not d.is_dir():
        sys.exit("no documents/ folder for %r" % slug)
    seen = set()
    files = 0
    for f in d.rglob("*.md"):
        files += 1
        for tok in NUM.findall(f.read_text(encoding="utf-8", errors="replace")):
            seen.add(tok)
            seen.add(tok.replace(",", ""))
    payload = {"slug": slug, "files": files, "tokens": sorted(seen)}
    index_path(slug).write_text(json.dumps(payload), encoding="utf-8")
    return payload


def load(slug):
    p = index_path(slug)
    if not p.exists():
        return None
    return set(json.loads(p.read_text(encoding="utf-8"))["tokens"])


_NUMERIC_CACHE = {}


def _numeric_index(tokens):
    """The document's numbers as a sorted float list, cached per token set."""
    key = id(tokens)
    hit = _NUMERIC_CACHE.get(key)
    if hit is not None:
        return hit
    vals = []
    for tok in tokens:
        s = tok.replace(",", "")
        if not s or s in (".",):
            continue
        try:
            vals.append(float(s))
        except ValueError:
            continue
    vals.sort()
    _NUMERIC_CACHE[key] = vals
    return vals


def corroborated(value, tokens, min_abs=1.0):
    """Does this figure appear in the documents, allowing for rounding?

    STRING matching was the first approach and it produced false NEGATIVES that cost real
    time. Creative Newtech's FY2026 revenue is carried as 2,699.77 crore; its documents print
    the same figure in lakh as "2,69,977.25". Those are the same number - the engine stores two
    decimals - but no string form of one equals the other, so the check reported a figure that
    is plainly in the documents as missing.

    Matching numerically with a half-of-last-decimal tolerance (0.005 crore, or 0.5 when the
    statement is in lakh) fixes that without loosening the test into meaninglessness: the
    false-positive rate is measured by --selftest and must stay near zero, which is the only
    thing that makes this check worth running at all.
    """
    import bisect
    if value is None or not isinstance(value, (int, float)) or isinstance(value, bool):
        return None
    if abs(value) < min_abs:
        return None                      # too small to be distinctive; not testable
    # Threshold lowered from 10.0 to 1.0 on 29-Aug-2026 after measuring, not guessing: the
    # false-positive rate across creative-newtech, dhampur and jsw-steel is 0.0-0.2% at every
    # threshold from 10.0 down to 1.0, so the higher floor was excluding testable figures for
    # no benefit. Below 1.0 the numbers stop being distinctive and it would start passing
    # anything, which is the line this check must never cross.
    vals = _numeric_index(tokens)
    if not vals:
        return False
    # scale 10.0: some filings (Apollo Tyres) state figures in MILLION rather than lakh/crore -
    # a crore value of X appears in the document as X*10 million. Added rather than guessed:
    # verified against Apollo Tyres' own AR, where the corroboration search previously failed
    # on every single input because no scale in this list matched a million-denominated filing.
    for scale, tol in ((1.0, 0.005), (100.0, 0.5), (10.0, 0.05)):
        target = abs(value) * scale
        i = bisect.bisect_left(vals, target - tol)
        while i < len(vals) and vals[i] <= target + tol:
            return True
        # no candidate inside the window
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--selftest", action="store_true",
                    help="measure the false-positive rate on random wrong "
                         "values - run this before trusting any result")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    payload = build(args.slug)
    print("indexed %d distinct numeric tokens from %d document(s)"
          % (len(payload["tokens"]), payload["files"]))

    if args.selftest:
        import random
        random.seed(11)
        toks = set(payload["tokens"])
        hits = n = 0
        for _ in range(600):
            v = round(random.uniform(10.0, 60000.0), 2)
            r = corroborated(v, toks)
            if r is None:
                continue
            n += 1
            hits += 1 if r else 0
        print("false-positive rate           : %d/%d = %.1f%% "
              "(random WRONG values reported as corroborated)"
              % (hits, n, 100.0 * hits / n if n else 0.0))
        print("  a high rate means the check is worthless - it would pass anything")

    if not args.report:
        return
    sys.path.insert(0, str(ROOT))
    import tieout_mutation as tm
    mod = tm.load_engine(args.slug)
    tokens = set(payload["tokens"])
    found = missing = skipped = 0
    misses = []
    for name, (tbl, ix) in tm.input_tables(mod).items():
        for key in tbl:
            for v in tm.series_of(tbl, key, ix):
                r = corroborated(v, tokens)
                if r is None:
                    skipped += 1
                elif r:
                    found += 1
                else:
                    missing += 1
                    misses.append((name, key, v))
    total = found + missing
    print("corroborated in the documents : %d / %d (%.1f%%)"
          % (found, total, 100.0 * found / total if total else 0.0))
    print("too small to test             : %d" % skipped)
    if misses:
        print("\nNOT found in any document (derived, aggregated, or wrong):")
        for n, k, v in misses[:25]:
            print("  %-14s %-30s %s" % (n, k[:30], v))


if __name__ == "__main__":
    main()
