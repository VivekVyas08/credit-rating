# Ratio Workpaper — Dhampur Bio Organics Limited | CareEdge | 13 September 2026

**Basis: STANDALONE.** Engagement: new assignment, operator-directed.
**Supersedes** the workpaper of 04 September 2026, which was consolidated. The duplicate
case folder `Companies/dhampur` - which carried a separate CareEdge rating for this same
issuer, also struck on the wrong (consolidated) basis - was **deleted on 13-Sep-2026** at
the operator's instruction, after confirming no document was lost. This is now the single
CareEdge opinion for this issuer.

---

## 0. What was wrong in v1, and how it was found

v1 was delivered on 04-Sep-2026 reading **READY TO SHARE on all five gates**: 34/34 tie-outs,
**100.0% mutation coverage of 147 inputs**, every mandatory section present, scorecard matching
the rationale. The operator then supplied CareEdge's own published rationale for the same
issuer, dated the same day. Six errors:

| # | v1 said | Correct | Class of error |
|---|---|---|---|
| 1 | Basis **consolidated** | **Standalone** | right number, wrong statement |
| 2 | Rated amount **₹1,134.45 cr** | **₹1,062.05 cr** | stale — Jan-2026 limits |
| 3 | Cash **₹36.16 cr** | **₹4.50 cr** unencumbered | right caption, wrong definition |
| 4 | Meerganj proceeds in FY2026 | **FY2027** event | right number, wrong period |
| 5 | Outlook **Stable** | **Positive** | judgement, downstream of #4 |
| 6 | Capacity (TCD); throughput absent | **41.44 → 34.98 → 32.92 lakh t** | metric never sought |

**Not one was reachable by any gate the project had**, because every gate verified *internal
consistency*, and a wrong-basis extraction is perfectly consistent with itself. The 100%
coverage figure did not merely miss this — v1 quoted it as though it were assurance. That is
now failure mode 41, and `tools/step14_diff.py` is the answer to it.

## 1. Why standalone — the test that settles it

Both bases are internally valid, so the discriminator cannot be arithmetic. It is reproduction
(failure mode 32): the correct basis reproduces the agency's published figures.

| Metric | v1 consolidated | **v2 standalone** | CareEdge published |
|---|---|---|---|
| Cash & equivalents | 8.71 | **4.50** | "low at ₹4.5 crore" |
| Inventories | 1,013.17 | **994.45** | ₹994 crore |
| Tangible net worth | 1,026.64 | **1,029.68** | ₹1,030 crore |
| TOI net of excise FY2026 | 2,109.25 | **2,082.01** | ₹2,082 crore |
| PAT FY2026 | 25.18 | **24.97** | ₹25 crore |
| Overall gearing FY2025 | 1.15 | **1.142** | 1.14 |

Standalone reproduces on every line. The subsidiaries are immaterial and carry no borrowings —
consolidating them moves TNW by ₹3.04 crore and total debt not at all. **CareEdge's action of
13-Jan-2026 states "Analytical approach: Standalone" on its face**: it was in the library,
flagged PRESENT by the pre-flight, and opened at Step 14, where only the grade was compared.

## 2. Computed suite (standalone) — 29/29 tie-outs reconcile

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Cane crushed (lakh tonne) | 41.44 | 34.98 | **32.92** |
| Cane diverted to ethanol (lakh t) | – | 3.37 | **nil** |
| Sugar produced (lakh tonne) | – | 3.10 | **3.54** |
| Gross / net recovery (%) | 11.37 / – | 10.56 / 9.80 | **10.98 / 10.74** |
| TOI (net of excise) | 1,831.18 | 1,882.96 | 2,082.01 |
| PBILDT | 137.88 | 139.93 | 131.04 |
| PBILDT margin (%) | 7.53 | 7.43 | **6.29** |
| PAT | 48.82 | 12.09 | 24.97 |
| Gross cash accruals | 98.28 | 65.94 | 83.73 |
| Total debt (incl leases) | 1,056.95 | 1,162.34 | 1,060.46 |
| — working capital | – | – | **764.51** |
| — long-term incl current maturities | – | – | **289.66** |
| Unencumbered cash | 2.38 | 6.90 | **4.50** |
| Encumbered bank balances | 4.08 | 6.42 | 6.19 |
| Tangible net worth | 1,020.66 | 1,017.61 | 1,029.68 |
| Overall gearing (x) | 1.04 | 1.14 | 1.03 |
| Interest coverage (x) | 3.05 | 2.09 | 2.08 |
| Net debt / PBILDT (x) | 7.65 | 8.26 | 8.06 |
| Total debt / GCA (x) | 10.75 | 17.63 | 12.67 |
| RoCE (%) | 4.26 | 3.95 | 3.46 |
| Inventory days | 215.78 | 203.81 | 174.34 |

**The debt split v1 never made.** Current borrowings of ₹847.19 crore are **not** all working
capital: ₹82.68 crore is current maturities of long-term debt. Working capital is therefore
**₹764.51 crore** (CareEdge: ₹765 crore) and long-term debt **₹289.66 crore** (CareEdge:
₹290 crore). Both reconcile to the rupee — from figures already sitting in v1's own extraction.

**The operating identity, which validates four inputs at once:**
sugar produced = (cane crushed − cane diverted) × net recovery.
FY2026: (32.92 − 0.00) × 10.74% = **3.54** ✓   FY2025: (34.98 − 3.37) × 9.80% = **3.10** ✓

## 3. Liquidity (Step 11) — on unencumbered cash only

| Sources, 12 months | ₹ cr | Claims, 12 months | ₹ cr |
|---|---|---|---|
| Gross cash accruals (FY2026) | 83.73 | Scheduled LT repayment | ~26.00 |
| **Unencumbered cash** | **4.50** | Maintenance capex | ~45.00 |
| Meerganj proceeds (Q1 FY2027) | 305.00 | Dividend | ~5.00 |

₹6.19 crore of "bank balances other than cash and cash equivalents" is **excluded**: the
Company's own notes show it is deposits held as security or margin against guarantees, plus
deposits earmarked for the Molasses Storage Fund. Pre-flight probe `[0e]` surfaces both by
name. Descriptor **Adequate** — accruals cover scheduled claims, but the free-cash base is very
small and the buffer depends on inventory liquidating at carrying value.

## 4. Step 12 forward view (`DBOL_5yr_Model.xlsx`)

Debt path derived from the funding gap, not extrapolated (FM18). Base case reaches interest
coverage **3.37x** and debt ₹950 crore by FY2031. Stress — flexing recovery and administered
ethanol realisation, the two variables the sugar methodology names — troughs at **ICR 1.45x**
and TD/PBILDT 11.58x in FY2028: below the 1.50x negative trigger, above 1.0x. A downgrade
case, not a default case.

## 5. Step 12b anchor and its divergence

Stage 1 anchor **A+** (index 4) → Stage 2 overlay **−3** → Stage 3 **CARE BBB+; Positive**.
Beyond the ±2 screening band, so resolved on the sheet: **−1** for scale and single-state
concentration (throughput −20.6% in two years; two plants in one command area), **−2** for
calibration (the composite is carried by gearing 1.03x and a stable ₹1,029.68 crore TNW and
under-weights coverage 2.08x, TD/GCA 12.67x and net leverage 8.06x on a 6.29% margin). Hard
caps left live — a sugar miller's earnings are accrual-realised, so accrual coverage is the
right test.

## 6. Step 14 — mechanical diff against the agency's own action

`python tools/step14_diff.py dhampur-bio-organics-limited`

| Item | CareEdge | This exercise | Explanation |
|---|---|---|---|
| Basis | Standalone | **Standalone** | corrected; v1 diverged and did not say so |
| Rated amount | 1,062.05 | **1,062.05** | five-condition amendment, date-stamped |
| Outlook | Positive | **Positive** | re-derived once Meerganj was placed in FY2027 |
| TOI FY2026 | 2,082 | 2,082.01 | reproduces |
| PAT FY2026 | 25 | 24.97 | reproduces |
| Gearing FY2026 | 1.03 | 1.03 | reproduces |
| **PBILDT FY2026** | **134** | **131.04** | **DIVERGES 2.96 — disclosed, not forced** |
| Interest coverage FY2026 | 2.13 | 2.08 | follows from the PBILDT gap |
| Inventory days FY2026 | 193 | 174.34 | different denominator (theirs implies cost of goods) |

**On the PBILDT gap (failure mode 32).** On the stated convention — PBT before exceptional,
plus finance and depreciation, less other income in full — PBILDT is 137.88 / 139.93 / 131.04.
CareEdge publishes 143 / 140 / 134. FY2025 reproduces almost exactly; FY2024 and FY2026 fall
5.12 and 2.96 short, most likely because CareEdge adds back the loss on asset sale and small
non-operating items inside other expenses. **The inputs are not adjusted to close it** — a
definition that will not reproduce is a definition to disclose.

**On the outlook, stated plainly.** I did not simply adopt CareEdge's Positive. v1's Stable
rested on a timing error: once the Meerganj sale is correctly placed in FY2027 — ₹305.00 crore
of proceeds against ₹289.66 crore of long-term debt, **none of it in the 31-Mar-2026 balance
sheet** — the deleveraging becomes a forward catalyst rather than a completed fact, which is
precisely what an outlook is for. **Disclosure: I had already seen CareEdge's Positive before
re-deriving this, so it is not independent confirmation.** What is checkable is the arithmetic:
long-term debt more than halves on the proceeds alone.

## 7. Disclosed differences

- PBILDT diverges from CareEdge in FY2024 and FY2026 and is **not forced** (§6).
- Inventory and operating-cycle days use net TOI; CareEdge's denominator implies cost of goods. Both move the same way and by a similar magnitude.
- FY2024 and FY2025 current maturities of long-term debt are **not separately extracted**, so only the FY2026 working-capital split is stated.
- Q1 FY2026-27 is narrative, not a computed column; its reported PAT is dominated by the one-time divestment gain.
- Mutation coverage is **70.6%**, below v1's 100%, because the operating metrics and rated limits are now carried as inputs and only some are arithmetically checkable. **A higher number would not mean a better report — v1 is the proof.**

## 8. Deliverables

`Dhampur Bio Organics Limited_13 Sep 2026_CARE_Rating Rationale.md` · this workpaper ·
`compute_ratios.py` (v2, standalone, 29/29) · `DBOL_Financial_Spreads.xlsx` ·
`DBOL_5yr_Model.xlsx` · `Rating_Scorecard_Dhampur Bio Organics Limited.xlsx` ·
`Committee_Minutes_13Sep2026.md`.

The 04-Sep rationale is retained as `..._SUPERSEDED.md`. It is not clutter: it is the positive
control that five of the new probes fire on, and it should not be deleted.
