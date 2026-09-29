"""Positive control for corpus_mine.py.

Every expectation below was read by eye off the facilities table at the top of
the named report. A parser that cannot reproduce these is not evidence about
anything, and the first version could not: it read Themis Medicare as BBB when
the header says BBB-, having picked up an ASSOCIATE company's rating out of the
Analytical approach paragraph.
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corpus_mine as cm

# file stem -> (long-term, short-term, outlook, lt_amount, st_amount)
EXPECT = {
    "Themis Medicare Limited_12 Aug 2025":
        ("BBB-", "A3", "Negative", 77.39, 48.50),
    "Chemfab Alkalis Limited_04 Apr 2025":
        ("A-", "A2+", "Stable", 0.0, 0.0),          # withdrawn: amounts blank
    "Bhagiradha Chemicals and Industries Limited_10 Jun 2025":
        ("BBB+", "A2", None, None, None),           # amounts not asserted
}


def main():
    fails = 0
    for stem, (lt, st, outlook, lta, sta) in EXPECT.items():
        path = os.path.join(cm.LIB, stem + ".md")
        if not os.path.exists(path):
            print("SKIP (missing) %s" % stem)
            continue
        r = cm.mine(path)
        checks = [("lt", lt, r["lt"]), ("st", st, r["st"])]
        if outlook is not None:
            checks.append(("outlook", outlook, r["outlook"]))
        if lta is not None:
            checks.append(("lt_amt", lta, r["lt_amt"]))
        if sta is not None:
            checks.append(("st_amt", sta, r["st_amt"]))
        for field, want, got in checks:
            ok = (want == got)
            if not ok:
                fails += 1
            print("%-6s %-52s %-8s want=%-10s got=%s"
                  % ("PASS" if ok else "FAIL", stem[:52], field, want, got))
    print("\n%d failure(s)" % fails)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
