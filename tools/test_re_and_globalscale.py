"""Controls for failure mode 60 (real-estate CFO ratio set) and failure mode 61
(global-to-national scale mapping), both added 13-Sep-2026.

FM61 fires on nothing in the 35-rationale corpus because the project has no foreign-parent
case yet - which is exactly why it is controlled synthetically here. A probe that has never
been exercised is a probe nobody knows the behaviour of.

    python tools/test_re_and_globalscale.py
"""
import importlib.util
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "cs", str(Path(__file__).resolve().parent / "check_sections.py"))
cs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cs)


def _doc(about, body):
    return ("## about the company\n" + about + "\n\n## rationale\n" + body).lower()


_DEV = "the company is a real-estate developer with residential projects in mmr and ncr"
_MFR = "the company is an integrated steel producer with 18 mtpa of capacity"

# ---------------------------------------------------------------- FM60
RE_CASES = [
    # FIRES: a developer assessed on accrual coverage / gearing, with no CFO ratio anywhere.
    ("developer on gearing alone", _DEV,
     "total debt of rs 4,200 crore against a tangible net worth of rs 3,100 crore gives a "
     "gearing of 1.35 times; interest coverage was 1.9 times in fy26", True),
    ("developer on interest coverage alone", _DEV,
     "interest coverage stood at 2.1 times, down from 2.6 times", True),

    # DOES NOT FIRE: the CRISIL developer framework was actually used. Each alternative on its
    # own must clear the probe, since a report may use any one of them.
    ("developer with debt/CFO", _DEV,
     "debt to cfo (adjusted) stood at 2.8 times against 3.4 times a year earlier", False),
    ("developer with cash buffer ratio", _DEV,
     "the cash buffer ratio was 1.4 times over the next twelve months", False),
    ("developer with committed receivables", _DEV,
     "committed receivables from ongoing projects of rs 9,800 crore cover the balance "
     "construction cost and debt servicing 1.6 times", False),
    ("developer with collections", _DEV,
     "collections rose 22% to rs 6,400 crore and bookings to rs 8,100 crore", False),

    # DOES NOT FIRE: commercial-for-LEASE and LRD are assessed on DSCR, a legitimate
    # alternative track CRISIL states separately. Flagging it would be a false positive.
    ("lease/LRD track on DSCR", _DEV,
     "the lease rental discounting facility carries an average dscr of 1.32 times over the "
     "debt tenure; gearing stood at 1.1 times", False),

    # DOES NOT FIRE: not a developer at all. Guards against the probe leaking into every
    # report that mentions gearing.
    ("manufacturer on gearing is fine", _MFR,
     "gearing stood at 0.8 times and interest coverage at 6.4 times", False),
]

# ---------------------------------------------------------------- FM61
GS_CASES = [
    # FIRES: a foreign CRA's grade cited in a parent/support context, no mapping statement.
    ("S&P parent rating used unmapped", _MFR,
     "the rating factors in support from the ultimate parent, which is rated bbb+ by s&p", True),
    ("Moody's guarantor unmapped", _MFR,
     "the guarantor is rated baa2 by moody's, which underpins the credit enhancement", True),
    ("Fitch sponsor unmapped", _MFR,
     "the sponsor carries a bb+ rating from fitch", True),

    # DOES NOT FIRE: the scale difference is addressed. Any of the accepted formulations
    # clears it - the probe asks that the difference be acknowledged, not phrased one way.
    ("mapping stated explicitly", _MFR,
     "the parent is rated bbb+ by s&p on the global scale, which maps to the crisil national "
     "scale roughly 6 to 7 notches higher", False),
    ("scales named as different", _MFR,
     "the parent's s&p rating is on the global scale and is not comparable with the national "
     "scale used here", False),

    # DOES NOT FIRE: a foreign CRA named with no parent/support context - e.g. a passing
    # reference to sector research. Flagging that would train the reader to ignore the probe.
    ("foreign CRA with no support context", _MFR,
     "global steel demand is expected to grow 2% in cy2026 according to moody's sector "
     "research on the industry outlook", False),

    # DOES NOT FIRE: a DOMESTIC agency's rating in a parent context. The whole point is that
    # national-scale ratings need no mapping; matching them would fire on almost every report.
    ("domestic CRA in parent context", _MFR,
     "the parent is rated crisil aa+/stable and support from it is factored into the rating",
     False),
]


def _run(name, cases, fn):
    fails = []
    for label, about, body, expect in cases:
        got = fn(_doc(about, body))
        ok = bool(got) == expect
        print(("  ok   " if ok else "  FAIL ") + f"[{name}] " + label
              + ("" if ok else f"\n         expected fire={expect}, got={got!r}"))
        if not ok:
            fails.append(label)
    return fails


def main():
    f = _run("FM60", RE_CASES, cs._real_estate_wrong_ratio_set)
    f += _run("FM61", GS_CASES, cs._global_scale_unmapped)
    total = len(RE_CASES) + len(GS_CASES)
    print()
    if f:
        print(f"{len(f)} FAILED of {total}")
        return 1
    print(f"ALL PASS - {total}/{total} controls")
    return 0


if __name__ == "__main__":
    sys.exit(main())
