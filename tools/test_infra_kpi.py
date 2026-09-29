"""Positive controls for the infrastructure SECTOR_KPI entries added 06-Sep-2026.

These entries fire on nothing in the current 35-rationale corpus, because the project has no
solar, wind, transmission, toll or annuity/HAM case yet. A check that has never fired is a
check that has never been tested - this project's own rule (failure mode 39's corollary: "a
check that cannot fail its own control is not a check"). Every entry below is therefore
exercised against a deliberately-bad report and a deliberately-good one.

Two traps these controls exist to catch, both of which the earlier sugar entry fell into:
  - the trigger must come from the ABOUT-THE-COMPANY section, so an ESG paragraph mentioning
    "solar" must not fire the renewable rule on a manufacturer;
  - the metric must be QUANTIFIED - a passing mention without a number is still a miss.

Run: python tools/test_infra_kpi.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_sections as cs

results = []


def case(name, text, should_fire, expect_fragment=None):
    got = cs._missing_sector_kpi(text)
    fired = got is not None
    ok = fired == should_fire
    if ok and fired and expect_fragment:
        ok = expect_fragment.lower() in got.lower()
    print(f"[{'OK' if ok else 'FAIL'}] {name}")
    print(f"       fired={fired} (want {should_fire}) -> {(got or '')[:110]}")
    results.append(ok)


def report(about, body=""):
    return (f"Crisil A/Stable; reaffirmed.\n\n## About the Company\n{about}\n\n"
            f"## Detailed Rationale\n{body}\n")


# ---------------- solar / wind: P90 PLF -----------------------------------------------------
case("solar SPV with no PLF basis at all fires",
     report("The company is a solar power project SPV operating a 150 MW plant in Rajasthan.",
            "The project has a debt service coverage ratio of 1.25 times over the loan life."),
     True, "P90")

case("solar SPV mentioning PLF but not quantifying it still fires",
     report("The company is a solar power project SPV operating a 150 MW plant in Rajasthan.",
            "The PLF has been broadly in line with expectations and DSCR is comfortable."),
     True, "not quantified")

case("solar SPV quantifying P90 PLF passes",
     report("The company is a solar power project SPV operating a 150 MW plant in Rajasthan.",
            "DSCR of 1.25 times is computed on a P90 PLF of 19.5%, against a P50 of 21.8%."),
     False)

case("wind SPV quantifying PLF passes",
     report("The company is a wind farm SPV with 90 MW of capacity across two sites.",
            "The P90 PLF is assessed at 20.1%; liquidity covers 4.2 months of maturing debt."),
     False)

# The trap: a manufacturer whose ESG section mentions solar must NOT trigger the renewable rule.
case("manufacturer with a solar mention in ESG does NOT fire the renewable rule",
     report("The company manufactures speciality chemicals at three plants in Gujarat.",
            "ESG: the company commissioned a solar power project of 5 MW for captive use, "
            "reducing grid dependence."),
     False)

# ---------------- transmission: line availability -------------------------------------------
case("transmission SPV with no availability figure fires",
     report("The company is an inter-state transmission project SPV under a 35-year TSA.",
            "Revenue visibility is healthy given the CERC-approved tariff."),
     True, "line availability")

case("transmission SPV quantifying line availability passes",
     report("The company is an inter-state transmission project SPV under a 35-year TSA.",
            "Line availability has been maintained at 99.4% against the normative 98%."),
     False)

# ---------------- toll roads: traffic and toll rate ------------------------------------------
case("toll road SPV with no traffic figure fires",
     report("The company is a toll road SPV operating a 62 km stretch under a BOT concession.",
            "The DSCR is projected at 1.30 times over the loan life."),
     True, "traffic")

case("toll road SPV quantifying traffic passes",
     report("The company is a toll road SPV operating a 62 km stretch under a BOT concession.",
            "Average daily traffic was 18,400 PCU in fiscal 2026, with toll rates revised 5.2%."),
     False)

# ---------------- annuity / HAM: DSCR ---------------------------------------------------------
case("HAM SPV with no DSCR fires",
     report("The company is a hybrid annuity model road SPV awarded by NHAI in 2021.",
            "Annuities have been received without material delay since COD."),
     True, "DSCR")

case("HAM SPV quantifying DSCR passes",
     report("The company is a hybrid annuity model road SPV awarded by NHAI in 2021.",
            "Minimum DSCR is 1.18 times over the loan life, excluding DSRA and sponsor support."),
     False)

print()
n_fail = sum(1 for r in results if not r)
print(f"{len(results) - n_fail}/{len(results)} controls passed"
      + (f" - {n_fail} FAILED" if n_fail else ""))
sys.exit(1 if n_fail else 0)
