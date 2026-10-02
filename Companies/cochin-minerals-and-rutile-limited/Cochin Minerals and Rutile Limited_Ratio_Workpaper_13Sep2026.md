# Ratio Workpaper — Cochin Minerals and Rutile Limited | CareEdge | 13 September 2026

**Basis: STANDALONE** (declared at intake; the Company has no subsidiary).
**Engagement:** new assignment. **Deliverable:** `..._13 Sep 2026_CARE_Rating Rationale.md`.

---

## 1. Step 1a — Pre-flight

`python tools/preflight.py cochin-minerals-and-rutile-limited` — 8 documents, 120,040 words.

| Probe | Result | What it bound |
|---|---|---|
| [0] newest first | newest is 2026 | Q1 FY2027 filing is the newest and had to be read |
| [0b] metrics across docs | no conflicts | — |
| [0c] aggregate-note contaminants | forex gain 34.75; exceptional 505.20; interest & dividend income; investment subsidy 15.00 | each needed a written include/exclude decision — §5 |
| [0d] cash-flow vs note | no conflict | — |
| **[0e] balance-sheet aggregates** | **margin money 523.74, unclaimed dividend 18.57/35.09 sitting inside CASH** | the caption had to be split before any liquidity figure — §4 |
| [1] prior rating action | **hits were NOT this issuer** | see §2 — the most important finding of the pre-flight |
| [2] rating note in AR | **absent, 0 matches** | absence EVIDENCED; safe to state no prior rating |
| [3] subsidiaries | "The Company has no subsidiary" | standalone is forced, not elected; Annexure-6 N/A |
| [4] ESG | 112 matches | ESG may not be called unextractable |

## 2. The pre-flight hit that had to be rejected

Probe [1] reported PRESENT and offered **Cochin Shipyard Limited** (with ₹2,280 crore of rated
facilities) and **Sarda Energy & Minerals Limited**. Neither is this issuer — one is a
shipbuilder, the other a steel and power group; the match scores were 1/3 on name tokens.

The probe's own warning governs: *"A PARENT, SIBLING OR PEER IS NOT THE ISSUER — importing a
peer's rated amount is a WORSE error than leaving it TBC."* A word-boundary check on all three
tokens (`Cochin`, `Minerals`, `Rutile`) returns nothing in any library, and `step14_diff.py`
independently matches zero publications. Combined with probe [2] finding **no rating disclosed
in any of the three annual reports**, the conclusion is that **no CRA has rated this issuer**.

**Consequence:** rated amounts are *to be confirmed by issuer*, there is no rating history, and
Step 14 falls back to peer benchmarking. Cochin Shipyard's ₹2,280 crore does not appear
anywhere in the deliverable.

## 3. Steps 5–6 — Extraction and tie-outs

Engine: `compute_ratios.py`. **30/30 tie-outs reconcile. Mutation coverage 94.3% of 105 inputs.**
Source figures are in **₹ lakh** and converted to ₹ crore **once, in code** (R6).

| Metric (₹ crore) | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Total operating income | 300.44 | 319.21 | **294.92** |
| PBILDT | 37.89 | 30.88 | **23.49** |
| PBILDT margin (%) | 12.61 | 9.67 | **7.96** |
| PAT | 26.69 | 23.56 | **12.51** |
| Gross cash accruals | 27.55 | 24.69 | 14.10 |
| Total debt | 5.72 | 10.78 | **6.21** |
| Unencumbered cash | 0.03 | 22.06 | **38.17** |
| Encumbered bank balances | not split | 5.59 | 5.57 |
| **Net debt / (net cash)** | 5.69 | (11.28) | **(31.95)** |
| Tangible net worth | 148.44 | 165.40 | 172.03 |
| Overall gearing (x) | 0.04 | 0.07 | **0.04** |
| TOL / TNW (x) | 0.62 | 0.59 | 0.44 |
| Interest coverage (x) | 45.14 | 152.20 | 121.75 |
| RoCE (%) | 24.02 | 16.88 | **12.28** |
| Inventory days | 138.57 | 190.35 | 154.93 |
| Receivable days | 42.60 | 18.99 | 30.14 |

**Two findings the arithmetic produced, not the eye:**

- **An OCR decimal loss.** The FY2025-26 AR prints FY2025 cost of material as `1614195`. The expense build-up reconciles to the printed total of 28,967.05 only at **16,141.95**, which the prior AR confirms.
- **A missing expense line.** The FY2024 build-up was 49.97 short until a separate **CSR Expenses** line was found in the FY2024-25 AR — a line the newer AR folds into other expenses.

**Three restatements between AR vintages, each nil-sum, newer governs (FM26):** CSR ₹81.62 lakh
folded into other expenses; ₹15.16 lakh moved from other income to revenue; and ₹213.92 lakh
removed from other current assets, matched by ₹107.40 + ₹106.52 on the liabilities side. All
three reconcile on both sides of the sheet.

## 4. Liquidity (Step 11) — the caption had to be split first

Pre-flight [0e] surfaced margin money and unclaimed dividend sitting inside the bank-balance
caption. Note 12 decomposes it, and the components tie to the printed total:

| Note 12 (₹ crore) | FY2025 | FY2026 |
|---|---|---|
| Margin money vs BG/LC — **encumbered** | 5.24 | **5.07** |
| Deposits 3–12 months — free | 22.01 | **24.03** |
| Unpaid dividend — **encumbered** | 0.35 | **0.50** |
| **Printed total** | 27.60 | **29.60** ✓ |

**Unencumbered cash = ₹14.14 crore (cash and equivalents) + ₹24.03 crore (deposits) = ₹38.17
crore.** Taking the caption whole would have overstated free liquidity by ₹5.57 crore. Against
total debt of ₹6.21 crore, all short-term, the Company is in **net cash of ₹31.95 crore**.
Descriptor: **Strong** — a genuine surplus, not merely adequate cover.

## 5. Step 8 — Materiality sweep, with decisions

R13 test: ≥1% of TNW (₹1.72 crore), ≥5% of PBT (₹0.95 crore), or any
regulatory/governance item regardless of size.

| Finding | Quantum | Decision |
|---|---|---|
| **Metallisation CWIP impairment** — project abandoned for want of domestic ilmenite | ₹5.05 crore | **INCLUDE** as the central business-risk evidence; **EXCLUDE** from PBILDT (exceptional, non-cash) |
| Forex gain | ₹0.35 crore | EXCLUDE — sits in other income, already stripped; convention is **not** asymmetric here |
| Interest & dividend income | ₹3.00 / ₹1.92 crore | EXCLUDE — within other income |
| Investment subsidy | ₹0.15 crore | EXCLUDE — within other income; recurring, not a one-off gain |
| CSR expense | ₹0.82 crore | RETAIN in PBILDT on both AR bases |
| Margin money / unpaid dividend | ₹5.57 crore | EXCLUDE from liquidity — §4 |

## 6. Step 10 — Methodology Compliance Map

Criteria read this session from `CareEdge/Methodology/`: Manufacturing Companies (March 2025),
Financial Ratios – Non-Financial Sector, Liquidity Analysis, Short-Term Instruments,
Outlook/Watch, Default Recognition. Scope verified: a non-financial manufacturing corporate,
squarely within the manufacturing master criteria.

| Factor (as the criteria name it) | Evidence | vs band | Weight |
|---|---|---|---|
| A — Economy & industry | TiO2 feedstock chain; ilmenite availability and price the driving variables | Moderate, input-constrained | High |
| B — Business: **size, market share, diversification** | ₹294.92 crore revenue, **one product, one site**, 50,000 MT capacity | **Weak** — the criteria treat size and diversification as explicit factors | **High** |
| B — Cost structure / operating efficiency | Conversion spread compressed: rutile prices fell, ilmenite did not follow | Weak and outside the Company's control | High |
| C — Financial: accounting quality | Unqualified audit opinion; no emphasis of matter | Strong | Medium |
| C — Financial: leverage & coverage | Gearing 0.04x, TOL/TNW 0.44x, **net cash** | **Very strong** | High |
| C — Financial: liquidity | Unencumbered ₹38.17 crore, current ratio 2.93x, no LT repayment | **Strong** | High |
| D — Management | Long-established listed company; but the metallisation project absorbed capital for years before write-off | Adequate | Medium |
| E — Project risk | None — no announced project; the only one was abandoned | Not applicable | Low |

## 7. Step 12 — Forward view (`CMRL_5yr_Model.xlsx`)

**FY2027 is anchored on Q1 FY2027 ACTUALS, not extrapolated from FY2026.** Q1 revenue of
₹131.26 crore annualises to ₹525 crore; the base case is deliberately set **below** that at
₹420 crore because one unaudited quarter is not a run-rate. Base case: PBILDT margin 10.5%
recovering toward but not to the FY2024 level, PAT ₹31.34 crore, net cash building to ₹45.13
crore. The funding gap is **negative throughout** — this issuer funds capex from accruals.

**Stress** flexes the two variables the criteria and the Company both name — volume/ilmenite
availability and the rutile-ilmenite price relationship — back to the FY2026 trough and below:
revenue ₹285 crore and margin 5.5% in FY2028, PAT ₹10.02 crore, and the Company **still holds
₹28.60 crore of net cash**. That is the point: even in the stress case there is no refinancing
or servicing question. The rating is constrained by business risk, not by financial risk.

## 8. Step 12b — Anchor, and a 3-notch divergence resolved

Stage 1 anchor **AA−** (index 3, composite 2.335) → Stage 2 overlay **−3** → Stage 3
**CARE A−; Stable**.

The divergence exceeds the ±2 screening band and is resolved on the sheet:

- **−2 scale and concentration.** ₹294.92 crore of revenue, one product, one site. The composite reads gearing of 0.04x and net cash and cannot see that the manufacturing criteria treat size, market share and diversification as explicit business-risk factors, on all of which this issuer is weak.
- **−1 raw-material access.** The constraint the Company discloses itself, and which already cost it the metallisation project.

**Why the anchor is so high here is instructive:** the scorecard is fed audited actuals and this
issuer's financial inputs are close to ideal — negligible debt, net cash, 122x coverage, 2.93x
current ratio. The anchor is doing exactly what it was built to do and is still wrong by three
notches, because *the entire risk in this credit sits outside the financial statements*. Hard
caps left live; accrual metrics are meaningful for a manufacturer.

## 9. Step 14 — no same-issuer action; peer benchmarking instead

`python tools/step14_diff.py cochin-minerals-and-rutile-limited` → **no same-issuer agency
publication in the reference libraries** (see §2). Step 14 therefore falls back to peers, as
the SOP provides. Benchmarked against the CareEdge manufacturing peer set the pre-flight
returned, the row set used here (total operating income, PBILDT, PAT, overall gearing, interest
coverage) is the agency's own for this sector.

**Honest limit:** peer benchmarking is a weaker check than a same-issuer diff. There is no
published figure for this issuer against which any number here can be reproduced, so the
extraction rests entirely on internal reconciliation to the printed statements — 30 tie-outs —
and not on external validation. That is a real difference in assurance from a case like Dhampur
and is stated rather than glossed.

## 10. Disclosed differences

- **No prior rating action** — the pre-flight's hits were different companies; Cochin Shipyard's rated amounts are not imported.
- **FY2024 bank balances are not split** between free and encumbered (the older AR gives only the total), so FY2024 unencumbered cash is stated on cash and equivalents alone and is conservative.
- **Production volume and realisation per tonne are not disclosed** — capacity (50,000 MT) is, but tonnage and realisation are not, so capacity utilisation cannot be computed. The operating constraint is therefore described from the Company's own statements rather than quantified. A real limit on the analysis.
- **Interest coverage of ~122x is not a discriminator** — it measures the absence of debt, not the capacity to service it.
- **Q1 FY2027 is a dated data point, not a computed column** — no tie-out reaches it, but it is the newest evidence and it changes the forward view.

## 11. Deliverables

`Cochin Minerals and Rutile Limited_13 Sep 2026_CARE_Rating Rationale.md` · this workpaper ·
`compute_ratios.py` (30/30) · `CMRL_Financial_Spreads.xlsx` · `CMRL_5yr_Model.xlsx` ·
`Rating_Scorecard_Cochin Minerals and Rutile Limited.xlsx` · `Committee_Minutes_13Sep2026.md`
