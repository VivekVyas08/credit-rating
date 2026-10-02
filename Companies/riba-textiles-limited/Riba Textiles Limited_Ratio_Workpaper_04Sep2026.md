# Ratio Workpaper - Riba Textiles Limited | CareEdge

*Generated 04 Sep 2026 by `tools/make_workpaper.py` from this case's own `compute_ratios.py`.*

> **What this document is.** The EXTRACTION AND VERIFICATION record for this case: the computed ratio suite, every tie-out with its source, the measured coverage of those tie-outs, and the inputs nothing checks. Every figure below is produced by the engine, not retyped - re-run `python Companies/riba-textiles-limited/compute_ratios.py` to reproduce it.
>
> **What this document is NOT.** It does not contain the Document Read Log, the qualitative fact register, the materiality sweep or the Methodology Compliance Map. Those require the documents to have been read and are listed by name in section 6 as outstanding. They are not generated here because a fabricated Read Log reads as diligence and stops anyone looking - which is failure mode 20, and the reason failure mode 37 exists.

## 1. Computed ratio suite (Step 6)

Basis: periods as the engine declares them. Values as `compute()` returns them.

| Metric | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| PBILDT | 18.70 | 19.73 | 22.25 |
| PBILDT margin (%) | 7.70 | 7.99 | 7.52 |
| PAT margin (%) | 3.05 | 3.21 | 2.87 |
| Total debt | 60.80 | 67.68 | 61.39 |
| Tangible net worth | 81.48 | 89.40 | 97.90 |
| Overall gearing (x) | 0.75 | 0.76 | 0.63 |
| TOL / TNW (x) | 1.02 | 1.00 | 0.85 |
| Interest coverage (x) | 4.16 | 4.24 | 3.78 |
| Total debt / PBILDT (x) | 3.25 | 3.43 | 2.76 |
| RoCE (%) | 10.00 | 9.51 | 10.54 |
| Total income | 242.83 | 247.21 | 296.13 |
| Depreciation | 4.47 | 4.79 | 5.47 |
| Finance cost | 4.49 | 4.65 | 5.89 |
| Profit before tax | 9.74 | 10.60 | 11.16 |
| Profit after tax | 7.40 | 7.92 | 8.50 |
| Borrowings - non-current | 26.12 | 25.38 | 25.74 |
| Borrowings - current | 34.68 | 42.30 | 35.65 |
| Equity share capital | 9.65 | 9.65 | 9.65 |
| Reserves & surplus | 71.83 | 79.74 | 88.24 |
| Total assets | 164.21 | 179.08 | 181.45 |
| Net debt | - | 62.91 | 58.84 |
| Net overall gearing (x) | - | 0.70 | 0.60 |
| Current ratio (x) | - | 1.33 | 1.38 |
| Receivable days | - | 61.48 | 44.68 |
| Inventory days | - | 37.96 | 31.04 |
| Revenue from operations | - | 246.89 | 295.86 |
| Other income | - | 0.31 | 0.27 |
| Total expenses | - | 236.60 | 284.96 |
| Inventories | - | 25.68 | 25.16 |
| Trade receivables | - | 41.59 | 36.22 |
| Cash & cash equivalents | - | 4.70 | 2.47 |
| Other bank balances | - | 0.07 | 0.07 |
| Current assets | - | 82.63 | 75.89 |
| Current liabilities | - | 61.99 | 54.91 |
| Deferred tax liability | - | 2.32 | 2.90 |

## 2. Tie-outs (Step 6 gate) - 8/8 reconcile

Each row reconciles a figure this engine DERIVES against one printed somewhere else. A check that compares a value with itself cannot fail and is not a check (failure mode 39).

| # | Check | Computed | Disclosed | Tol | Source | |
|---|---|---|---|---|---|---|
| 1 | FY2024 total income = revenue + other income | 247.21 | 247.21 | 0.02 | AR statement of profit and loss - printed total income row | OK |
| 2 | FY2024 PBT = total income - total expenses | 10.60 | 10.60 | 0.02 | AR statement of profit and loss - printed PBT row | OK |
| 3 | FY2024 current ratio vs company-disclosed | 1.33 | 1.33 | 0.02 | AR key-financial-ratios note, current ratio row | OK |
| 4 | FY2024 company 'debt-equity' = LT debt / equity | 0.28 | 0.28 | 0.02 | AR key-financial-ratios note, debt-equity row (long-term basis) | OK |
| 5 | FY2025 total income = revenue + other income | 296.13 | 296.13 | 0.02 | AR statement of profit and loss - printed total income row | OK |
| 6 | FY2025 PBT = total income - total expenses | 11.16 | 11.16 | 0.02 | AR statement of profit and loss - printed PBT row | OK |
| 7 | FY2025 current ratio vs company-disclosed | 1.38 | 1.38 | 0.02 | AR key-financial-ratios note, current ratio row | OK |
| 8 | FY2025 company 'debt-equity' = LT debt / equity | 0.26 | 0.26 | 0.02 | AR key-financial-ratios note, debt-equity row (long-term basis) | OK |

## 3. Tie-out coverage, measured by mutation (Step 6 / failure mode 39)

`python tools/tieout_mutation.py riba-textiles-limited` -> **30.0% coverage**.

Coverage is MEASURED, not asserted: the harness perturbs every numeric input and reports which ones no tie-out notices. A suite can be 100%% green and still verify nothing, so the count of passing checks is not the question - the question is which inputs would be caught if they were wrong.

Inputs no tie-out is sensitive to (35):

| Table | Input | Period | Value |
|---|---|---|---|
| BS | Borrowings - non-current | FY2023 | 2611.53 |
| BS | Borrowings - current | FY2023 | 3468.10 |
| BS | Borrowings - current | FY2024 | 4230.22 |
| BS | Borrowings - current | FY2025 | 3564.93 |
| BS | Equity share capital | FY2023 | 965.29 |
| BS | Equity share capital | FY2024 | 965.29 |
| BS | Equity share capital | FY2025 | 965.29 |
| BS | Reserves & surplus | FY2023 | 7182.62 |
| BS | Reserves & surplus | FY2024 | 7974.38 |
| BS | Reserves & surplus | FY2025 | 8824.35 |
| BS | Total assets | FY2023 | 16420.83 |
| BS | Total assets | FY2024 | 17908.18 |
| BS | Total assets | FY2025 | 18144.64 |
| BS | Inventories | FY2024 | 2567.85 |
| BS | Inventories | FY2025 | 2516.15 |
| BS | Trade receivables | FY2024 | 4158.75 |
| BS | Trade receivables | FY2025 | 3621.70 |
| BS | Cash & cash equivalents | FY2024 | 470.29 |
| BS | Cash & cash equivalents | FY2025 | 247.37 |
| BS | Other bank balances | FY2024 | 6.73 |
| BS | Other bank balances | FY2025 | 6.73 |
| BS | Deferred tax liability | FY2024 | 231.68 |
| BS | Deferred tax liability | FY2025 | 289.94 |
| PL | Other income | FY2025 | 26.73 |
| PL | Total income | FY2023 | 24282.97 |
| PL | Depreciation | FY2023 | 446.66 |
| PL | Depreciation | FY2024 | 479.18 |
| PL | Depreciation | FY2025 | 547.38 |
| PL | Finance cost | FY2023 | 449.38 |
| PL | Finance cost | FY2024 | 464.89 |
| PL | Finance cost | FY2025 | 588.57 |
| PL | Profit before tax | FY2023 | 974.08 |
| PL | Profit after tax | FY2023 | 740.25 |
| PL | Profit after tax | FY2024 | 791.77 |
| PL | Profit after tax | FY2025 | 849.96 |

## 4. Disclosed differences and unverified inputs (carried from the engine)

- **FY2023 column is largely unchecked** - The FY2024 AR restates only total income, depreciation, finance cost, PBT, PAT and the balance-sheet headline for FY2023 - it carries no revenue/other-income split, no current assets/liabilities and no working-capital lines. The two arithmetic tie-outs therefore cannot run on FY2023, and its PBILDT margin is struck on TOTAL income rather than revenue. Stated rather than silently blended.
- **Working-capital and cash lines have no independent second source** - Inventories, trade receivables, cash and other bank balances come from the FY2025 AR balance sheet alone. The company discloses no inventory- or receivable-day ratio to reconcile them against, so receivable/inventory days are traceable but not reproducible.
- **No lease add-back is possible, so coverage may be overstated** - No lease liability line and no right-of-use asset appears on the balance sheet in any of FY2023, FY2024 or FY2025, so PBILDT equals PBDIT and no CareEdge lease add-back can be computed. If material operating leases exist off-balance-sheet, the add-back would raise PBILDT and improve coverage - to be confirmed by the issuer. See LEASE_NOTE.

## 5. Extraction source register (Step 5)

Where the engine annotates an input with its origin, that annotation is reproduced verbatim. This is a provenance record, not a corroboration record - traced is not verified (response protocol 2(e)).

| Table | Line item | Source as the engine records it |
|---|---|---|
| BS | Borrowings - non-current | 973 L3120; 998 L3060 |
| BS | Borrowings - current | 973 L3124; 998 L3064 |
| BS | Equity share capital | 973 L3113; 998 L~3053 |
| BS | Reserves & surplus | 973 L3115; 998 L~3054 |
| BS | Total assets | 973 L3110; 998 L3067 |
| BS | Inventories | 998 L3042 |
| BS | Trade receivables | 998 L3044 |
| BS | Cash & cash equivalents | 998 L~3046 |
| BS | Other bank balances | 998 L~3047 |
| BS | Current assets | 998 L~3050 |
| BS | Current liabilities | 998 L3068 |
| BS | Deferred tax liability | 998 L~3061 |
| PL | Revenue from operations | 998 L~3095; FY23 not separately extracted |
| PL | Other income | 998 L~3096 |
| PL | Total income | 973 L3164; 998 L~3097 |
| PL | Depreciation | 973 L3170; 998 L~3109 |
| PL | Finance cost | 973 L3171; 998 L~3110 |
| PL | Total expenses | 998 L~3117 |
| PL | Profit before tax | 973 L3177; 998 L~3120 |
| PL | Profit after tax | 973 L3182; 998 L3121 |

## 6. OUTSTANDING - the sections that require the documents to be read

These are **not** in this document and have **not** been done. They are named here so the gap is visible rather than silent.

- [ ] **Document Read Log (Step 1b)** - one row per uploaded file: what it is, the key facts it contributes, the material items it flags. A file not in the log has not been read.
- [ ] **Qualitative fact register (Step 7)** - every non-computed claim traced to a document location, and corroborated against a second source where one exists (response protocol 2(e)).
- [ ] **Materiality sweep (Step 8)** - the untouched sections of every file walked for credit-relevant items, each tagged material/immaterial against the R13 test with a written include/exclude decision.
- [ ] **Methodology Compliance Map (Step 10)** - one row per rating factor as the methodology names it, scored with the company's actual numbers against the indicative band, every notching criterion quoted verbatim.
- [ ] **Liquidity computation (Step 11)** - sources-vs-claims arithmetic over ~12 months; the descriptor is the conclusion of that arithmetic, never an adjective.

## 7. Rating view as delivered (Step 13-15, from this case's own rationale)

Source: `Riba Textiles Limited_19 Aug 2026_CareEdge_Rating Rationale.md`

> > **This is not an official CareEdge Ratings publication.** It is an internal analytical exercise

Sections present in the delivered rationale:

- **Riba Textiles Limited**
- **Rationale and key rating drivers**
- **Rating sensitivities: Factors likely to lead to rating actions**
- **Positive factors**
- **Negative factors**
- **Analytical approach:** Standalone
- **Outlook:** Stable
- **Detailed description of key rating drivers:**
- **Key strengths**
- **Key weaknesses**
- **Liquidity: Adequate**
- **Environment, social, and governance (ESG) risks**
- **Applicable criteria**
- **About the company and industry**
- **Brief Financials (₹ crore)**
- **Annexure I — Details of instruments / facilities**
- **Annexure II — Ratings of the company by other credit rating agencies (as disclosed by the issuer)**
- **Annexure III — The company's own disclosed ratios, and why they differ**
- **Correction note — 19 August 2026**
- Where this assessment's arithmetic differed, and why

The rating view itself lives in that document; it is referenced here rather than restated, so the two cannot drift apart.

---

*Reproduce this workpaper: `python tools/make_workpaper.py riba-textiles-limited --force`. Re-verify the case: `python tools/delivery_audit.py riba-textiles-limited`.*
