"""Find the CareEdge reference reports that are genuine peers of a case.

Peer selection is by INDUSTRY CLASSIFICATION plus SIZE BAND, never by name
similarity -- the Cochin Minerals pre-flight offered Cochin Shipyard on a
one-token name overlap, which is how a shipbuilder nearly supplied the rated
amounts for a synthetic-rutile plant.

    python tools/corpus_peers.py --industry chemical --toi-lo 100 --toi-hi 900
"""
import argparse, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "Docs", "careedge_corpus.json")


def latest(vals):
    vals = [v for v in vals if v is not None]
    if not vals:
        return None
    return vals[-2] if len(vals) >= 3 else vals[-1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--industry", default="", help="regex against the industry block")
    ap.add_argument("--toi-lo", type=float, default=0)
    ap.add_argument("--toi-hi", type=float, default=1e12)
    ap.add_argument("--since", default="", help="only reports whose date contains this year")
    a = ap.parse_args()

    recs = [r for r in json.load(open(DATA, encoding="utf-8"))
            if not r.get("error") and r.get("lt") and not r.get("is_suspended")]
    rx = re.compile(a.industry, re.I) if a.industry else None

    hits = []
    for r in recs:
        blk = (r.get("industry_block") or "") + " " + r["issuer"]
        if rx and not rx.search(blk):
            continue
        toi = latest(r.get("bf", {}).get("toi", []))
        if toi is None or not (a.toi_lo <= toi <= a.toi_hi):
            continue
        if a.since and a.since not in (r.get("date") or ""):
            continue
        hits.append((toi, r))

    hits.sort(key=lambda t: (t[1]["lt_idx"], -t[0]))
    print("%-46s %-6s %-5s %9s %8s %8s %8s  %s"
          % ("issuer", "grade", "ST", "TOI", "PBILDT", "PAT", "gearing", "liquidity"))
    print("-" * 118)
    for toi, r in hits:
        bf = r["bf"]
        g = lambda k: latest(bf.get(k, []))
        val = lambda x, p=2: ("%9.*f" % (p, x)) if x is not None else "        -"
        print("%-46s %-6s %-5s %s %s %s %s  %s"
              % (r["issuer"][:46], r["lt"], r["st"] or "-", val(toi, 2),
                 val(g("pbildt")), val(g("pat")), val(g("gearing")),
                 r.get("liquidity") or "-"))
    print("\n%d peers" % len(hits))


if __name__ == "__main__":
    main()
