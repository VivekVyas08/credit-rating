"""Calibration statistics over the mined CareEdge corpus.

Answers the questions a prose read of 805 reports cannot: at each grade, what
scale, gearing, margin and coverage does CareEdge actually publish? The Cochin
Minerals error was a calibration error -- a 295 crore single-product
manufacturer assigned A- -- so the corpus is the control.
"""
import json, os, statistics as st, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "Docs", "careedge_corpus.json")
LT_SCALE = ["AAA", "AA+", "AA", "AA-", "A+", "A", "A-", "BBB+", "BBB", "BBB-",
            "BB+", "BB", "BB-", "B+", "B", "B-", "C+", "C", "C-", "D"]


def latest(vals):
    """Brief Financials columns run oldest -> newest; take the newest FY.

    The last column is often an unaudited interim quarter, whose TOI is a
    part-year figure and must never be compared against a full year. Prefer the
    second-to-last when there are three or more columns."""
    vals = [v for v in vals if v is not None]
    if not vals:
        return None
    return vals[-2] if len(vals) >= 3 else vals[-1]


def q(xs):
    xs = sorted(x for x in xs if x is not None)
    if not xs:
        return None
    n = len(xs)
    return (xs[0], xs[n // 4], st.median(xs), xs[(3 * n) // 4], xs[-1], n)


def fmt(t, w=8, p=2):
    if t is None:
        return "        -"
    return " ".join(("%%%d.%df" % (w, p)) % v for v in t[:5]) + "  n=%d" % t[5]


def main():
    recs = [r for r in json.load(open(DATA, encoding="utf-8"))
            if not r.get("error") and r.get("lt") and r.get("bf")
            and not r.get("is_suspended")]
    print("reports with a grade + Brief Financials, not INC/suspended: %d\n" % len(recs))

    metrics = [("toi", "TOI (Rs cr)", 0), ("gearing", "Overall gearing (x)", 2),
               ("pbildt_mgn", "PBILDT margin (%)", 2), ("intcov", "Interest cover (x)", 2),
               ("tdgca", "TD/GCA (x)", 2)]

    for key, name, prec in metrics:
        print("=" * 78)
        print("%s   [min  p25  median  p75  max]" % name)
        print("=" * 78)
        for g in LT_SCALE:
            rows = [r for r in recs if r["lt"] == g]
            vals = [latest(r["bf"][key]) for r in rows if key in r["bf"]]
            t = q(vals)
            if t:
                print("  %-5s %s" % (g, fmt(t, 8, prec)))
        print()


if __name__ == "__main__":
    main()
