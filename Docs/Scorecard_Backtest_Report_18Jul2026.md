# Rating Scorecard — Back-test Report
*18-Jul-2026. Open item #1 (SESSION_HANDOFF §5). Data: 396 ICRA-rated issuers (379 corporate + 17 financial-sector) with complete key-financial-indicator (KFI) tables, drawn from the 649 reference reports.*

> **Data-rule note (declared, per CLAUDE.md §10 rule 1).** This is a **calibration-only** use of CRA-published ratings (the label) and CRA-published KFI figures (the features). R2 forbids CRA material *as a source for a rating report*; this is not a report — it is validation of the anchor against agency outcomes, for which the agency's own published numbers are the only coherent ground truth. **No figure extracted here flows into any issuer's rationale.**

---

## 1. Headline result

The scorecard anchor was run against each issuer's actual ICRA long-term grade, holding all **judgmental inputs neutral** (business & management = 3; sector base, weights, liquidity, support-notch = generic) so the test isolates the **quantitative core** (the financial-risk block + the composite→grade map). Result under the current xlsx knobs:

| Metric | Baseline (current knobs) | Target |
|---|---|---|
| Exact notch | 11% | — |
| **Within ±1 notch** | **30%** | ~80% |
| Within ±2 notches | 49% | — |
| **Signed bias** | **+2.13 notches (anchor too LOW)** | 0 |
| MAE | 2.85 notches | — |

The **+2.13-notch downward bias reproduces the JSW (A− vs AA) and IIFL (A+ vs AA) "anchor too low" defects at scale** — it is systematic, not case-specific.

## 2. Where it fails — the diagnostic that matters

| Actual grade band | n | Mean notch error | Within ±1 |
|---|---|---|---|
| AAA to AA− | 186 | **+3.79** (anchor far too low) | 8% |
| A+ to A− | 149 | +1.46 | 54% |
| BBB | 48 | −0.69 | 50% |
| BB & below | 13 | **−3.62** (anchor too high) | 0% |

The anchor **under-rates the strongest names and over-rates the weakest**, and is only well-behaved in the A/BBB middle. This is the signature of a grade that is **majority-qualitative**: AAA/AA ratings rest on franchise, parentage and sovereign/group support; sub-investment-grade ratings rest on governance, default-proximity and event risk. Neither is visible in KFI ratios, so a neutral-judgmental run cannot reach them.

Corroborating statistics:
- **Spearman(financial-core score, actual grade) = 0.32** — the financial core has only modest standalone rank-correlation with the grade.
- **Isotonic ceiling (best-possible monotone financials-only map) = 47% within ±1, 68% within ±2.** No functional form beats this from KFI financials alone.

## 3. Why no knob-tune reaches the target

I tested every lever the open item names (Ref_Bands, Ref_Weights) plus the composite→grade map and the neutral prior:

1. **Financial bands cannot be tuned to the target.** Recalibrating them to the rated-population distribution *raises* thresholds (strong names cluster at 15–36× coverage), pushing most scores down and *worsening* the bias unless the map is also changed. Every band/prior/offset combination plateaus at ~42–45% within-1 / ~65% within-2. **The bands are not the bottleneck** and were left unchanged.
2. **A naïve affine re-fit of the map** removes the bias but its shallow slope (1.6 vs 3.2) is **overfit to the neutral-qualitative back-test** — it compresses the scale so the worst composite reaches only ~BBB, breaking the scorecard for real per-issuer use. Rejected.
3. **A range-preserving power softening of the map — `index = 16·((C−1)/5)^p` — is the correct fix.** It keeps the endpoints (C=1→AAA, C=6→C) but eases the harsh investment-grade zone where the linear map put a strong composite (~2) at AA−/A+ instead of AA. At **p = 1.4** the bias collapses to **+0.13**, within-2 rises to **68%**, and — critically — it is validated on the two real fully-scored cases (below), not just the neutral sample.

**Two-case validation (real analyst qualitative inputs, from the delivered scorecards):**

| Case | Composite | Old-map grade | New-map (p=1.4) grade | Analyst view |
|---|---|---|---|---|
| IIFL Finance (NBFC) | 2.21 | A+ | **AA** | AA / AA− |
| JSW Steel (steel) | 2.99 | A− | **A+** | AA / AA− |

Both move from 2–3 notches low to within ~1 notch of the analyst view, confirming the map — not the bands — was the defect.

**Residual ceiling is qualitative.** Even with the map fixed, within-1 stays ~40% because the composite still depends mostly on the (neutralised) judgmental inputs. Closing that gap needs the *judgmental* layer, not more quant tuning.

## 4. What was applied (and what was not)

**Applied to the master `Rating_Scorecard.xlsx` (18-Jul-2026), kept formula-driven, recompute-verified via the `formulas` engine:**
1. **Composite→grade map → power p=1.4** (`Rating!C7`). Removes the +2.1-notch bias; range-preserving. The pre-filled example issuer now reads `[ICRA]AA` (was AA−).
2. **New `Ref_Qualitative` sheet** — a 1–6 rubric for Industry / Business / Management, anchored in ICRA/CRISIL/CareEdge methodology language (**closes open item #4**).
3. **Support-notch discipline** — README + an `Inputs!C42` comment making it mandatory to apply the parent/group/government notch for support-driven issuers (PSU/sovereign, strong-parent subsidiaries). The neutral scorecard under-rates them 2–3 notches; leaving the notch at 0 was a direct cause of the IIFL/JSW misses.

**Deliberately NOT changed:** the financial bands (`Ref_Bands`, `Ref_Bands_Fin` — proven not the constraint; tuning overfits) and the block weights (`Ref_Weights` — analyst framework inputs). GCA/TD and current-ratio bands remain not-back-tested (no KFI data; low weight).

**Governance implication (open item #1 re-scoped, not "solved by tuning"):** after calibration the anchor is a **zero-biased ±2-notch screening band**, reliable to ~±1 only in the A+…BBB− range; it still structurally under-rates AA+/AAA and over-rates BB-and-below unless the support notch / qualitative rubric are applied per issuer. The anchor **binds as a ±2 cross-check, never as a point rating**: a divergence beyond ±2, or any divergence for AA+/AAA and BB-and-below, must be resolved by the qualitative/support narrative and minuted by the Committee — it is not, by itself, a scorecard failure.

---

## Appendix — method

- **Engine:** faithful Python replica of the xlsx (band-scoring 1–6 → weighted composite → liquidity adj → composite→grade map → hard caps), validated cell-for-cell against the Scorecard/Rating sheet formulas; master recompute confirmed via the `formulas` engine after the edit.
- **Parser:** long-term grade from the Summary-of-rating-action block (`[ICRA]<grade>(<outlook>)`); KFI metrics from the "Key financial indicators" table (latest audited FY). Corporate core = interest coverage, TD/OPBDITA, OPBDITA/OI margin, TOL/TNW; financial-sector core = CRAR, GNPA, NNPA, RoA.
- **Held neutral (not available per-issuer):** business/management qualitative scores, sector base score & weights (generic corporate / bank-nbfc-hfc), liquidity descriptor, support notches.
- **Not back-tested (no KFI data):** GCA/TD and current-ratio bands (corporate); NIM and cost-to-income (financial); financial-sector bands overall (n=17 too small to recalibrate — left provisional).
- Scripts in session scratchpad: `scan_reports.py`, `backtest.py`, `calibrate.py`, `ceiling.py`, `finalize.py`, `results.py`, `powermap.py`, `build_calibration.py`, `verify_master.py`.
