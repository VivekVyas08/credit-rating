"""Positive controls for failure-mode 47/51/52 probes and the LT-ST mapping check, added
13-Sep-2026. Per CLAUDE.md's own rule (FM39's corollary): a check that cannot fail its own
control is not a check. Run directly: python tools/test_fm47_52.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_sections as cs

FAILS, PASSES = 0, 0


def check(name, got_bad, got_clean):
    global FAILS, PASSES
    ok_bad = got_bad is not None and got_bad is not False
    ok_clean = got_clean is None or got_clean is False
    status = "OK" if (ok_bad and ok_clean) else "FAIL"
    (PASSES if status == "OK" else FAILS)
    print(f"[{status}] {name}")
    print(f"       bad   -> {got_bad!r}")
    print(f"       clean -> {got_clean!r}")
    return status == "OK"


results = []

# ---- FM47: total-debt basis unstated (CareEdge, LC facilities disclosed, never connected) ----
bad = """
CARE BBB; Stable / CARE A3+

The company's overall gearing stood at 0.04x as on March 31, 2026, reflecting a comfortable
capital structure. The company also availed a Letter of Credit facility of Rs 80.00 crore
during the year, largely for import of raw materials, along with bank guarantees.
"""
clean = """
CARE BBB; Stable / CARE A3+

Overall gearing (Total debt including acceptances / creditors on LC, per CareEdge convention)
stood at 0.31x as on March 31, 2026. The Letter of Credit facility of Rs 80.00 crore, along with
bank guarantees, is included in Total Debt for this computation.
"""
results.append(check("FM47 total-debt basis unstated",
                     cs._total_debt_basis_unstated(bad),
                     cs._total_debt_basis_unstated(clean)))

clean_no_nfb = """
CARE BBB; Stable

Overall gearing stood at 0.31x as on March 31, 2026, computed on total debt of Rs 6.21 crore
against tangible net worth of Rs 172.03 crore. The company has no non-fund-based facilities.
"""
r = cs._total_debt_basis_unstated(clean_no_nfb)
print(f"[{'OK' if r is False else 'FAIL'}] FM47 no false-positive when no LC/BG disclosed -> {r!r}")
results.append(r is False)

# ---- LT-ST mapping mismatch: ICRA fixed anchor violated ----
bad = "[ICRA]AA (Stable)/[ICRA]A2+; reaffirmed. The rating reflects a strong financial profile."
clean = "[ICRA]AA (Stable)/[ICRA]A1+; reaffirmed. The rating reflects a strong financial profile."
results.append(check("LT-ST mapping: ICRA AA must map to A1+",
                     cs._lt_st_mapping_mismatch(bad),
                     cs._lt_st_mapping_mismatch(clean)))

# ---- LT-ST mapping mismatch: CRISIL bank entity class ----
bad = """
Crisil A-/Stable/Crisil A2+; reaffirmed.

## About the Company
The bank has a network of over 500 branches across India and is a scheduled commercial bank.
"""
clean = """
Crisil A-/Stable/Crisil A1+; reaffirmed.

## About the Company
The bank has a network of over 500 branches across India and is a scheduled commercial bank.
"""
results.append(check("LT-ST mapping: CRISIL bank A- must map to A1+/(A1), not A2+",
                     cs._lt_st_mapping_mismatch(bad),
                     cs._lt_st_mapping_mismatch(clean)))

# ---- LT-ST mapping: CRISIL corporate at same A- grade legitimately maps differently (no false
# positive against the bank rule above) ----
corp = """
Crisil A-/Stable/Crisil A2+; reaffirmed.

## About the Company
The company is a leading manufacturer of auto components with plants across three states.
"""
r = cs._lt_st_mapping_mismatch(corp)
print(f"[{'OK' if r is None else 'FAIL'}] LT-ST mapping: CRISIL CORPORATE A- with A2+ is not "
      f"flagged (entity-class-specific table) -> {r!r}")
results.append(r is None)

# ---- FM51: hybrid cap conflation, ICRA corporate citing CRISIL's 15% ----
bad = """
[ICRA]A+ (Stable); reaffirmed.

## Hybrid Instruments
The Company's perpetual bond is eligible for equity credit up to 15% of adjusted equity, per
ICRA's cap on hybrid instruments issued by non-financial sector entities.
"""
clean = """
[ICRA]A+ (Stable); reaffirmed.

## Hybrid Instruments
The Company's perpetual bond is eligible for equity credit up to 30% of adjusted equity, per
ICRA's cap on hybrid instruments issued by non-financial sector entities.
"""
results.append(check("FM51 hybrid cap: ICRA corporate citing 15% (CRISIL's NBFC rule)",
                     cs._hybrid_cap_conflated(bad),
                     cs._hybrid_cap_conflated(clean)))

# ---- FM51: hybrid cap conflation, CRISIL NBFC citing ICRA's 30% ----
bad = """
Crisil A+/Stable; reaffirmed.

## About the Company
The Company is a non-banking financial company (NBFC) registered with the RBI.

## Hybrid Instruments
The perpetual debt instrument qualifies for Tier I inclusion up to 30% of Tier I capital.
"""
clean = """
Crisil A+/Stable; reaffirmed.

## About the Company
The Company is a non-banking financial company (NBFC) registered with the RBI.

## Hybrid Instruments
The perpetual debt instrument qualifies for Tier I inclusion up to 15% of Tier I capital.
"""
results.append(check("FM51 hybrid cap: CRISIL NBFC citing 30% (ICRA's corporate rule)",
                     cs._hybrid_cap_conflated(bad),
                     cs._hybrid_cap_conflated(clean)))

# ---- FM51 third cap: CRISIL CORPORATE citing 30% (ICRA's) or 15% (CRISIL's own NBFC rule) ----
# Added 06-Sep-2026. The probe shipped knowing only two of the three caps and passed both of
# these. CRISIL's corporate cap is 20% of adjusted net worth (basics-of-ratings.md III.2).
bad30 = """
Crisil A+/Stable; reaffirmed.

## About the Company
The company manufactures speciality chemicals at three plants in Gujarat.

## Hybrid Instruments
The perpetual bond is eligible for equity credit up to 30% of adjusted net worth.
"""
bad15 = bad30.replace("30% of adjusted net worth", "15% of Tier I capital")
clean20 = bad30.replace("30% of adjusted net worth", "20% of adjusted net worth")
results.append(check("FM51 hybrid cap: CRISIL CORPORATE citing 30% (ICRA's rule)",
                     cs._hybrid_cap_conflated(bad30),
                     cs._hybrid_cap_conflated(clean20)))
r = cs._hybrid_cap_conflated(bad15)
print(f"[{'OK' if r is not None else 'FAIL'}] FM51 hybrid cap: CRISIL CORPORATE citing 15% "
      f"(CRISIL's own NBFC rule, wrong entity class) -> {r!r}")
results.append(r is not None)

# ---- FM52: infra SPV notch-up beyond CRISIL's stated 1-2 notch norm ----
bad = """
Crisil AA-/Stable; reaffirmed.

The Company is a special purpose vehicle (SPV) executing a toll road project under a long-term
concession agreement. The rating reflects a 4 notch uplift for parent support given the strong
strategic linkage with the sponsor group.
"""
clean_notched = """
Crisil AA-/Stable; reaffirmed.

The Company is a special purpose vehicle (SPV) executing a toll road project under a long-term
concession agreement. The rating reflects a 1-2 notch uplift for parent support given the
linkage with the sponsor group.
"""
clean_excepted = """
Crisil AA-/Stable; reaffirmed.

The Company is a special purpose vehicle (SPV) executing a toll road project. The rating
reflects a 4 notch uplift for parent support; this is an exception to CRISIL's usual 1-2 notch
norm for infrastructure SPVs, given the exceptional linkage and cross-default with the parent.
"""
results.append(check("FM52 infra SPV notch: 4 notches with no exception language",
                     cs._infra_spv_notch_excessive(bad),
                     cs._infra_spv_notch_excessive(clean_notched)))
r = cs._infra_spv_notch_excessive(clean_excepted)
print(f"[{'OK' if r is None else 'FAIL'}] FM52 no false-positive when an exception is stated "
      f"in writing -> {r!r}")
results.append(r is None)

r = cs._infra_spv_notch_excessive(bad.replace("Crisil", "[ICRA]"))
print(f"[{'OK' if r is None else 'FAIL'}] FM52 is CRISIL-only, does not fire on an ICRA SPV "
      f"-> {r!r}")
results.append(r is None)

# ---- LT-ST entity class: "bank facilities" is a CORPORATE borrowing a bank's money ----
# Found 13-Sep-2026 on the delivered corpus. _section_body reads a fixed span from "About the"
# and overran the section on a short report, landing in the Complexity-level paragraph, which
# says "fund-based and non-fund-based bank facilities" on nearly every corporate rationale.
# Creative Newtech - a DISTRIBUTOR - was mapped against CRISIL's Banks row and reported as a
# mismatch. The SECTOR_KPI comment already recorded this exact trap for its own bank trigger;
# it had never been applied to the LT-ST probe.
distributor = """
Crisil BBB+/Stable/Crisil A2; reaffirmed.

## About the Company
The company is a distributor of technology and lifestyle brands in India.

## Complexity level of the rated instruments
Fund-based and non-fund-based bank facilities are assessed Simple.
"""
r = cs._lt_st_mapping_mismatch(distributor)
print(f"[{'OK' if r is None else 'FAIL'}] LT-ST: 'bank facilities' does not make a "
      f"distributor a bank -> {r!r}")
results.append(r is None)

# ...and a real bank must still be classified as one, or the fix has merely disabled the rule.
real_bank = """
Crisil A-/Stable/Crisil A2+; reaffirmed.

## About the Company
The entity is a scheduled commercial bank with 500 branches across India.
"""
r = cs._lt_st_mapping_mismatch(real_bank)
print(f"[{'OK' if r is not None else 'FAIL'}] LT-ST: a genuine bank is still mapped on the "
      f"Banks row -> {r!r}")
results.append(r is not None)

print()
n_fail = sum(1 for r in results if not r)
print(f"{len(results) - n_fail}/{len(results)} controls passed" +
      (f" - {n_fail} FAILED" if n_fail else ""))
sys.exit(1 if n_fail else 0)
