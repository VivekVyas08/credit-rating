# Tie-out coverage across every engine

Measured 29-Aug-2026. Coverage = the share of an engine's extracted figures that at least one
tie-out would notice if they were wrong. It is **not** the same as "tie-outs pass" — an engine
can report 34/34 reconciling while two thirds of its inputs are checked by nothing.

Two harnesses produce these numbers:

- `tieout_mutation.py <slug>` — white-box, fast, exact. Needs the engine to expose
  `YEARS` / `compute()` / `tieouts()` (see `engine_contract.py`).
- `mutate_blackbox.py <slug> [--sample N]` — works on **any** engine. Edits a numeric literal
  in the source, re-runs the script, and reads the reconcile line the engine already prints.
  Validated against the white-box measure on Jindal Stainless: 97.5% (40-literal sample) vs
  98.2% (exact).

## Where every engine stands

| Engine | Coverage | Tie-outs | Notes |
|---|---|---|---|
| balkrishna-industries-ltd | **98.5%** | 68 | fixed 29-Aug; was 13.4% |
| jindal-stainless | **98.2%** | 39 | built to the contract |
| repco-home-finance-limited | **97.5%** | 65 | fixed 29-Aug; was 20.5% |
| tvs-credit | 66.7% | yes | sampled |
| hdfc-securities | 58.3% | yes | sampled |
| gujarat-energy-limited | 41.7% | yes | sampled |
| nabkisan-finance-limited | 41.7% | yes | sampled |
| sbi | 31.4% | 34 | refactored to the contract 29-Aug; exact measure |
| riba-textiles-limited | 25.0% | yes | sampled |
| aptus-value-housing-finance-india-limited | 16.7% | yes | sampled |
| creative-newtech-limited | **none** | **0** | no tie-outs at all |
| dhampur | **none** | **0** | no tie-outs at all |
| doms-industries | **none** | **0** | no tie-outs at all |
| happy-forgings-limited | **none** | **0** | no tie-outs at all |
| hle-glascoat | **none** | **0** | no tie-outs at all |
| iifl | **none** | **0** | no tie-outs at all |
| indus-towers | **none** | **0** | no tie-outs at all |
| itc | **none** | **0** | no tie-outs at all |
| jsw-steel | **none** | **0** | no tie-outs at all |
| vedanta | **none** | **0** | no tie-outs at all |
| yasho-industries | **none** | **0** | no tie-outs at all |

## The finding that matters

**Eleven of twenty-one engines contain no tie-outs whatsoever.** Their coverage is not low; it
is *undefined*, because there is nothing for a figure to be checked against. Those eleven ran
clean and produced ratings, and every number in them may well be right — but nothing in the
project would have noticed if one were not.

This is the same condition that produced the three worst errors this project has recorded: the
Balkrishna forex add-back (a full rating notch), the Jindal Stainless cash-flow-vs-note mix-up,
and the 143.02 crore FY2023 transcription error found on 29-Aug — each an input that no check
was sensitive to.

## Why the remaining work is not mechanical

Raising coverage requires **independently sourced** disclosed values. Summing an engine's
components and comparing the result to a total derived from those same components is circular
and worth nothing — it is the hollow-check pattern this whole discipline exists to prevent.

A real tie-out needs a figure the source document prints *separately*: a balance-sheet subtotal,
a note's own total, a company-published EBITDA, a regulator-reported ratio. Only 7 of the 18
unfixed engines already carry such figures in their extraction. **The other 11 require going
back to that case's annual reports** to extract printed totals — which is analytical work per
case, not a refactor.

## Recommended order

1. **The 11 with no tie-outs** — highest risk, since nothing is checked. Start with the largest
   exposures: `jsw-steel`, `itc`, `vedanta`, `indus-towers`, `iifl`.
2. **`aptus` (16.7%), `sbi` (31.4%), `riba` (25.0%)** — tie-outs exist but cover little.
3. **`gujarat-energy`, `nabkisan` (41.7%)**, then `hdfc-securities` and `tvs-credit`.

The pattern to apply is in `Companies/jindal-stainless/compute_ratios.py`: keep components only,
derive every subtotal, tie each derived total to the figure the annual report prints, decompose
the aggregate notes and tie them to their own printed totals, then declare in
`UNVERIFIED_INPUTS` whatever still cannot be checked.


---

# Progress, 29-Aug-2026 (second pass)

Six of the eleven zero-tie-out engines now have tie-outs. Two were done with case-specific
checks against figures their annual reports print; four carry the shared structural checks in
`common_tieouts.py`.

| Engine | Before | Tie-outs now | 7% coverage | 10x coverage |
|---|---|---|---|---|
| yasho-industries | none | 16 | **32.2%** | – |
| happy-forgings-limited | none | 24 | **26.7%** | – |
| creative-newtech-limited | none | 16 | 15.4% | 29.2% |
| doms-industries | none | 18 | 0.0% | 30.0% |
| vedanta | none | 18 | 0.0% | 27.7% |
| indus-towers | none | 6 | 0.0% | 17.6% |
| **still untouched** | | | | |
| dhampur, hle-glascoat, iifl, itc, jsw-steel | none | 0 | – | – |

**Read the two coverage columns together, and do not quote the second alone.** The four engines
carrying only structural checks score 0–15% against a subtle (7%) error and 17–30% against a
decimal slip (10x). Containment checks have enormous slack — a 7% error never makes cash exceed
current assets — so they close the order-of-magnitude failure mode and little else. That is a
real failure mode (Jindal carried provisions of 66.55 against a true 6.65), but an engine
carrying only these is **not** verified in the sense that matters for a subtly wrong figure.

Yasho and Happy Forgings score higher because their checks include figures the annual report
prints in its own right — total assets, total equity, EBITDA against the investor deck. That is
the difference between a floor and actual verification, and it is why the remaining work is
per-case document extraction rather than more shared code.

## Harness fixes made along the way

`tieout_mutation.py` was silently under-measuring, in four separate ways — each of which made
an engine look measured when it was not:

1. **Tuple-wrapped series** `{"CRAR": ([...], "source")}` were invisible; every bank and NBFC
   engine reported "no input tables found".
2. **Bare module-level series** (`rev_consol = [...]`) were invisible; Yasho and similar
   engines reported the same.
3. **A single all-`None` row disqualified its whole table.** Happy Forgings' `norm_pat`
   discarded 57 of its 60 inputs, and the harness then reported 28.6% as though it had looked
   at everything. The honest figure was 26.7%.
4. `mutate_blackbox.py` was added so any engine can be measured without refactoring at all.

The pattern is the same one this project keeps rediscovering: a measurement that quietly
measures less than it claims is more dangerous than no measurement.


---

# Complete, 29-Aug-2026: no engine is left with zero tie-outs

All eleven are done. Every one of the 21 engines in this project now carries checks, runs
clean, and can be measured.

| Engine | Tie-outs | 7% coverage | 10x coverage |
|---|---|---|---|
| iifl | 6 | **33.3%** | 39.4% |
| yasho-industries | 16 | **32.2%** | 39.0% |
| happy-forgings-limited | 24 | **26.7%** | 35.0% |
| creative-newtech-limited | 16 | 15.4% | 29.2% |
| jsw-steel | 15 | 13.0% | 28.3% |
| hle-glascoat | 12 | 11.9% | 19.8% |
| doms-industries | 18 | 0.0% | 30.0% |
| vedanta | 18 | 0.0% | 27.7% |
| itc | 20 | 0.0% | 24.1% |
| dhampur | 12 | 0.0% | 19.0% |
| indus-towers | 6 | 0.0% | 17.6% |

**These are floors, not finished work.** An engine scoring 0% at 7% carries only containment
checks, which have enormous slack and close the decimal-slip failure mode alone. Raising these
into the nineties means what it meant for Balkrishna, Repco and Jindal: opening the annual
report, finding the totals it prints in its own right, and tying components to them. That is
per-case analytical work and it has not been done for these eleven.

## Two real defects the new checks found immediately

**IIFL's loan book was missing a category.** Secured plus unsecured did not sum to gross loans -
short by 88.78 (FY25) and 77.19 (FY26). Schedule III Division III splits a loan book THREE
ways, and the third - "covered by bank/government guarantees" - had not been extracted. The
FY25 residual matches the annual report's own printed 88.78 exactly. FY26 is deliberately left
`None`: a 77.19 residual is implied, but the printed row was not unambiguously identified (the
documents carry 14.05, 48.06 and 88.78 across entities and years), and writing an implied
figure in as though it were extracted is the habit these checks exist to break.

**JSW Steel and ITC held every figure only as keyword arguments.** Nothing could reach them -
no check, no measurement, no tooling. The values are unchanged and now live in DATA tables that
the printing code reads from, so the table and the output cannot drift apart.

## Also worth recording

`creative-newtech-limited` shows an implied tax rate of 13.7% (FY25) and 14.0% (FY26) against
India's 25.17% statutory rate. That may be legitimate - overseas subsidiaries, deferred-tax
credits, MAT-credit utilisation - but it is unexplained in the rationale and should be checked.
The plausibility band was widened to 8-45% rather than failed, and the measured rate now prints
on every run.

---

# All eleven raised into the nineties, 29-Aug-2026

Every one of the eleven engines that had no tie-outs three passes ago is now measured at 92% or
better, with no check failing at baseline.

| Engine | Was | Now | Tie-outs |
|---|---|---|---|
| jsw-steel | 13.0% | **100.0%** | 58 |
| happy-forgings-limited | 26.7% | **100.0%** | 106 |
| dhampur | 0.0% | **100.0%** | 90 |
| doms-industries | 0.0% | **100.0%** | 116 |
| creative-newtech-limited | 15.4% | **100.0%** | 96 |
| itc | 0.0% | **98.9%** | 106 |
| vedanta | 0.0% | **96.9%** | 62 |
| hle-glascoat | 11.9% | **96.5%** | 121 |
| indus-towers | 0.0% | **94.1%** | 40 |
| iifl | 33.3% | **93.9%** | 39 |
| yasho-industries | 32.2% | **92.3%** | 47 |

## The one pattern behind almost all of it

Nine of the eleven were held down by the same thing: **an aggregate typed as a single figure**.
`debt` written as `117.45 + 1.76 + 37.54`; `cash` typed as the sum of three balance-sheet notes;
`capex_cash` as PPE plus intangibles; trade payables as MSME plus non-MSME. Python folds the
expression at import, so what reaches the engine is one opaque number — and it is a number the
company never printed, which is why the document search failed on it while the components it is
made of were checked by nothing at all.

The fix is always the same and it is the SOP's own rule (failure mode 36) applied to extraction
rather than to the rationale: **name the components, derive the total, check the derivation.**
That converts one unverifiable input into three or four verifiable ones and adds a check that
fails if either side moves.

## Two real errors this pass found

**Dhampur's FY23 and FY24 lease liabilities were term-loan instalments.** Carried as 2.00 and
2.50 — both figures genuinely in the annual report, in the borrowings schedule, against the 8.70%
Grain/Distillery-Asmoli line and the 8.75% HDFC line. The actual lease liability is disclosed as
two rows: 4.76 + 2.26 = 7.02 (FY23) and 6.61 + 3.53 = 10.14 (FY24). The FY2025-26 report's own
lease movement table opens at 10.14, corroborating it independently. Total debt rises 5.02 and
8.14 crore; gearing moves 0.809x → 0.814x and 1.028x → 1.036x. Immaterial to the grade, which is
exactly why four years of data passed every check — and why the check now exists.

**DOMS held nine balance-sheet lines rounded to crore** while the annual reports state them in
lakh to two decimals, discarding two significant figures on every one. Now carried at full
printed precision.

## A hollow check I wrote and had to remove

The first version of the nil-assertion check appended `(0.0, 0.0)` — both sides a literal — so
it could never fail. The second version fired only `if v == 0`, so mutating a nil made the check
*disappear* rather than fail, and a vanishing check registers as nothing on a harness that
compares failure counts. Nil claims are now **declared** by the engine (`nil_claims=`), never
inferred from the live value. This is failure mode 39 reproduced by the person documenting it,
one pass later, and it is recorded here because the pattern is evidently easy to write.

Related: comparing a value against a snapshot of itself would score 100% coverage and verify
nothing. That option was available and was deliberately not taken.

## What these numbers still do not mean

Coverage says every input would be *noticed* if it changed. It does not say every input is
right. The strongest checks here are PRINTED anchors and sum-to-printed-total identities; the
weakest are CORROBORATED presence checks, which prove a figure exists somewhere in the documents
and are blind to right-number-wrong-place (failure mode 30). Where a figure was anchored by a
second read of the annual report during this pass, the source string says which row.
