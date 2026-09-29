"""Which published metrics actually discriminate a CareEdge grade?

Spearman rank correlation of each Brief Financials metric against the grade
index (0 = AAA ... 17 = D). A metric with |rho| near zero carries no rating
information in CareEdge's own revealed book, however good the number looks.

This exists because the Cochin Minerals anchor was driven to AA- by gearing of
0.04x and interest coverage of 122x, and the assigned rating was BBB.
"""
import json, os, math

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "Docs", "careedge_corpus.json")


def latest(vals):
    vals = [v for v in vals if v is not None]
    if not vals:
        return None
    return vals[-2] if len(vals) >= 3 else vals[-1]


def ranks(xs):
    """Average ranks, ties shared."""
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def spearman(a, b):
    if len(a) < 8:
        return None
    ra, rb = ranks(a), ranks(b)
    n = len(a)
    ma, mb = sum(ra) / n, sum(rb) / n
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    da = math.sqrt(sum((x - ma) ** 2 for x in ra))
    db = math.sqrt(sum((y - mb) ** 2 for y in rb))
    return num / (da * db) if da and db else None


def main():
    recs = [r for r in json.load(open(DATA, encoding="utf-8"))
            if not r.get("error") and r.get("lt_idx") is not None
            and r.get("bf") and not r.get("is_suspended")]

    # derived metrics
    for r in recs:
        bf = r["bf"]
        toi, pbildt = latest(bf.get("toi", [])), latest(bf.get("pbildt", []))
        r["m_toi"] = toi
        r["m_logtoi"] = math.log10(toi) if toi and toi > 0 else None
        r["m_gearing"] = latest(bf.get("gearing", []))
        r["m_intcov"] = latest(bf.get("intcov", []))
        r["m_pat"] = latest(bf.get("pat", []))
        r["m_margin"] = (100.0 * pbildt / toi) if (toi and pbildt and toi > 0) else None

    print("Spearman rho vs grade index (0=AAA .. 17=D).")
    print("Negative rho = a BIGGER value goes with a BETTER (lower-index) grade.\n")
    print("  %-22s %8s %8s   %s" % ("metric", "rho", "n", "reading"))
    print("  " + "-" * 74)

    for key, name in [("m_toi", "Total operating income"),
                      ("m_logtoi", "log10(TOI)"),
                      ("m_pat", "Profit after tax"),
                      ("m_margin", "PBILDT margin"),
                      ("m_intcov", "Interest coverage"),
                      ("m_gearing", "Overall gearing")]:
        pairs = [(r[key], r["lt_idx"]) for r in recs if r.get(key) is not None]
        rho = spearman([p[0] for p in pairs], [p[1] for p in pairs])
        if rho is None:
            continue
        a = abs(rho)
        reading = ("STRONG discriminator" if a >= 0.45 else
                   "moderate" if a >= 0.25 else
                   "WEAK - carries little rating information" if a >= 0.12 else
                   "NONE - no rating information")
        print("  %-22s %8.3f %8d   %s" % (name, rho, len(pairs), reading))

    # Where does a 295 crore issuer with these metrics actually sit?
    print("\n" + "=" * 78)
    print("CMRL's own numbers placed in the corpus distribution")
    print("=" * 78)
    cmrl = {"m_toi": 294.92, "m_gearing": 0.31, "m_intcov": 121.70, "m_margin": 7.96}
    for key, name in [("m_toi", "TOI 294.92"), ("m_gearing", "gearing 0.31x"),
                      ("m_intcov", "int cover 121.70x"), ("m_margin", "PBILDT margin 7.96%")]:
        vals = sorted(r[key] for r in recs if r.get(key) is not None)
        v = cmrl[key]
        pct = 100.0 * sum(1 for x in vals if x <= v) / len(vals)
        # which grade buckets have a median on the other side?
        print("  %-22s percentile %5.1f  of %d rated issuers" % (name, pct, len(vals)))

    # The decisive cut: grade distribution of issuers with TOI in CMRL's band.
    print("\n" + "=" * 78)
    print("Grades actually assigned to issuers with TOI between 150 and 500 Rs cr")
    print("=" * 78)
    band = [r for r in recs if r.get("m_toi") and 150 <= r["m_toi"] <= 500]
    from collections import Counter
    c = Counter(r["lt"] for r in band)
    LT = ["AAA", "AA+", "AA", "AA-", "A+", "A", "A-", "BBB+", "BBB", "BBB-",
          "BB+", "BB", "BB-", "B+", "B", "B-", "C+", "C", "C-", "D"]
    tot = sum(c.values())
    for g in LT:
        if c[g]:
            print("  %-5s %3d  %5.1f%%  %s" % (g, c[g], 100.0 * c[g] / tot, "#" * c[g]))
    print("  total %d" % tot)
    better = sum(v for g, v in c.items() if LT.index(g) < LT.index("BBB+"))
    print("\n  rated A- or better in this size band: %d of %d (%.1f%%)"
          % (better, tot, 100.0 * better / tot))


if __name__ == "__main__":
    main()
