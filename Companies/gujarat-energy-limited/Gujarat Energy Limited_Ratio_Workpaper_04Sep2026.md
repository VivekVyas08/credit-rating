# Ratio Workpaper - Gujarat Energy Limited | CareEdge

*Generated 04 Sep 2026 by `tools/make_workpaper.py` from this case's own `compute_ratios.py`.*

> **What this document is.** The EXTRACTION AND VERIFICATION record for this case: the computed ratio suite, every tie-out with its source, the measured coverage of those tie-outs, and the inputs nothing checks. Every figure below is produced by the engine, not retyped - re-run `python Companies/gujarat-energy-limited/compute_ratios.py` to reproduce it.
>
> **What this document is NOT.** It does not contain the Document Read Log, the qualitative fact register, the materiality sweep or the Methodology Compliance Map. Those require the documents to have been read and are listed by name in section 6 as outstanding. They are not generated here because a fabricated Read Log reads as diligence and stops anyone looking - which is failure mode 20, and the reason failure mode 37 exists.

## 1. Computed ratio suite (Step 6)

Basis: periods as the engine declares them. Values as `compute()` returns them.

| Metric | FY2024 (standalone) | FY2025 (standalone) | FY2025 (merged) | FY2026 (merged) |
|---|---|---|---|---|
| Revenue from operations | 16,292.97 | 17,184.97 | 27,718.00 | 24,198.00 |
| Other income | 107.75 | 209.97 | - | - |
| Total income | 16,400.72 | 17,394.94 | - | - |
| Excise duty | 602.78 | 698.02 | - | - |
| Finance costs | 29.31 | 32.49 | - | - |
| Depreciation | 474.30 | 510.64 | - | - |
| Profit before tax | 1,536.21 | 1,546.60 | - | - |
| Profit after tax | 1,142.77 | 1,145.51 | - | 2,299.00 |
| Borrowings - non-current | 0.00 | 0.00 | - | - |
| Borrowings - current | 0.00 | 0.00 | - | - |
| Lease liabilities - NC | 117.77 | 115.16 | - | - |
| Cash & equivalents | 915.98 | 326.86 | - | - |
| Other bank balances | 10.14 | 32.54 | - | - |
| Total equity | 7,689.26 | 8,453.65 | - | - |
| Total assets | 11,658.35 | 12,615.12 | - | - |
| Trade receivables | 1,029.84 | 1,023.97 | - | - |
| Inventories | 58.67 | 61.86 | - | - |
| Deferred tax liability | 910.75 | 958.88 | - | - |
| PBILDT | 1,932.07 | 1,879.76 | - | - |
| PBILDT margin on gross revenue (%) | 11.86 | 10.94 | - | - |
| Revenue NET of excise | 15,690.19 | 16,486.95 | - | - |
| PBILDT margin net of excise (%) | 12.31 | 11.40 | - | - |
| Adjusted debt (leases only) | 117.77 | 115.16 | - | - |
| Overall gearing (x) | 0.02 | 0.01 | - | - |
| Net debt / (net cash) | -808.35 | -244.24 | - | - |
| Interest coverage (x) | 65.92 | 57.86 | - | - |
| TOL / TNW (x) | 0.52 | 0.49 | - | - |
| EBITDA | - | - | 3,677.00 | 3,772.00 |
| Net worth | - | - | - | 18,517.00 |
| EPS (Rs) | - | - | - | 24.50 |
| Dividend per share (Rs) | - | - | - | 8.90 |

## 2. Tie-outs (Step 6 gate) - 11/11 reconcile

Each row reconciles a figure this engine DERIVES against one printed somewhere else. A check that compares a value with itself cannot fail and is not a check (failure mode 39).

| # | Check | Computed | Disclosed | Tol | Source | |
|---|---|---|---|---|---|---|
| 1 | FY2024 total income = revenue + other income | 16,400.72 | 16,400.72 | 0.06 | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) - printed total income row | OK |
| 2 | FY2024 borrowings are NIL | 0.00 | 0.00 | 0.06 | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) - both borrowing lines | OK |
| 3 | FY2024 company is in NET CASH | 1.00 | 1.00 | 0.5 | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) - lease-only debt against cash and bank balances | OK |
| 4 | FY2025 total income = revenue + other income | 17,394.94 | 17,394.94 | 0.06 | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) - printed total income row | OK |
| 5 | FY2025 borrowings are NIL | 0.00 | 0.00 | 0.06 | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) - both borrowing lines | OK |
| 6 | FY2025 company is in NET CASH | 1.00 | 1.00 | 0.5 | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) - lease-only debt against cash and bank balances | OK |
| 7 | FY2025 merged revenue EXCEEDS standalone (bases differ) | 1.00 | 1.00 | 0.5 | Q4 FY2026 press release, 30-May-2026 (merged basis) against FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) - a deliberate cross-basis sanity check | OK |
| 8 | FY2025 basis gap is ~Rs 10,323 cr | 10,323.06 | 10,323.06 | 0.06 | Q4 FY2026 press release, 30-May-2026 (merged basis) revenue less FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) total income | OK |
| 9 | FY26 volumes: CGD + trading = total | 13.63 | 13.63 | 0.06 | Q4 FY2026 press release, 30-May-2026 (merged basis) - segment volume table | OK |
| 10 | Q4 volumes: CGD + trading = total | 13.51 | 13.51 | 0.06 | Q4 FY2026 press release, 30-May-2026 (merged basis) - segment volume table | OK |
| 11 | FY26 CGD sub-segments sum to CGD total | 8.70 | 8.69 | 0.06 | Q4 FY2026 press release, 30-May-2026 (merged basis) - CGD volume breakdown | OK |

## 3. Tie-out coverage, measured by mutation (Step 6 / failure mode 39)

`python tools/tieout_mutation.py gujarat-energy-limited` -> **36.2% coverage**.

Coverage is MEASURED, not asserted: the harness perturbs every numeric input and reports which ones no tie-out notices. A suite can be 100%% green and still verify nothing, so the count of passing checks is not the question - the question is which inputs would be caught if they were wrong.

Inputs no tie-out is sensitive to (33):

| Table | Input | Period | Value |
|---|---|---|---|
| MERGED | Revenue from operations FY2025 | (standalone) | 24198.00 |
| MERGED | EBITDA FY2024 | (standalone) | 3677.00 |
| MERGED | EBITDA FY2025 | (standalone) | 3772.00 |
| MERGED | Profit after tax FY2025 | (standalone) | 2299.00 |
| MERGED | Net worth FY2025 | (standalone) | 18517.00 |
| MERGED | EPS (Rs) FY2025 | (standalone) | 24.50 |
| MERGED | Dividend per share (Rs) FY2025 | (standalone) | 8.90 |
| STANDALONE | Excise duty FY2024 | (standalone) | 602.78 |
| STANDALONE | Excise duty FY2025 | (standalone) | 698.02 |
| STANDALONE | Finance costs FY2024 | (standalone) | 29.31 |
| STANDALONE | Finance costs FY2025 | (standalone) | 32.49 |
| STANDALONE | Depreciation FY2024 | (standalone) | 474.30 |
| STANDALONE | Depreciation FY2025 | (standalone) | 510.64 |
| STANDALONE | Profit before tax FY2024 | (standalone) | 1536.21 |
| STANDALONE | Profit before tax FY2025 | (standalone) | 1546.60 |
| STANDALONE | Profit after tax FY2024 | (standalone) | 1142.77 |
| STANDALONE | Profit after tax FY2025 | (standalone) | 1145.51 |
| STANDALONE | Lease liabilities - NC FY2024 | (standalone) | 117.77 |
| STANDALONE | Lease liabilities - NC FY2025 | (standalone) | 115.16 |
| STANDALONE | Cash & equivalents FY2024 | (standalone) | 915.98 |
| STANDALONE | Cash & equivalents FY2025 | (standalone) | 326.86 |
| STANDALONE | Other bank balances FY2024 | (standalone) | 10.14 |
| STANDALONE | Other bank balances FY2025 | (standalone) | 32.54 |
| STANDALONE | Total equity FY2024 | (standalone) | 7689.26 |
| STANDALONE | Total equity FY2025 | (standalone) | 8453.65 |
| STANDALONE | Total assets FY2024 | (standalone) | 11658.35 |
| STANDALONE | Total assets FY2025 | (standalone) | 12615.12 |
| STANDALONE | Trade receivables FY2024 | (standalone) | 1029.84 |
| STANDALONE | Trade receivables FY2025 | (standalone) | 1023.97 |
| STANDALONE | Inventories FY2024 | (standalone) | 58.67 |
| STANDALONE | Inventories FY2025 | (standalone) | 61.86 |
| STANDALONE | Deferred tax liability FY2024 | (standalone) | 910.75 |
| STANDALONE | Deferred tax liability FY2025 | (standalone) | 958.88 |

## 4. Disclosed differences and unverified inputs (carried from the engine)

- **The merged basis carries almost no independent checks** - Basis A comes from a single Q4 press release. Only revenue is cross-checked, and then only against the standalone basis as a DIFFERENCE test that proves the two are not comparable. EBITDA, PAT, net worth, EPS and DPS on the merged basis have no second source in the case folder and are traceable but not reproducible.
- **Q4 columns are unchecked** - The Q4 revenue/EBITDA/PAT figures support the quarterly narrative only; no audited quarterly statement exists in the folder to reconcile them against.
- **Working-capital lines are single-sourced** - Trade receivables, inventories and the deferred-tax liability come from the FY2024-25 balance sheet alone, with no disclosed ratio to reproduce them from.

## 5. Extraction source register (Step 5)

Where the engine annotates an input with its origin, that annotation is reproduced verbatim. This is a provenance record, not a corroboration record - traced is not verified (response protocol 2(e)).

| Table | Line item | Source as the engine records it |
|---|---|---|
| MERGED | Revenue from operations | Q4 FY2026 press release, 30-May-2026 (merged basis) |
| MERGED | EBITDA | Q4 FY2026 press release, 30-May-2026 (merged basis) |
| MERGED | Profit after tax | Q4 FY2026 press release, 30-May-2026 (merged basis) - FY2025 PAT not given on merged basis |
| MERGED | Net worth | Q4 FY2026 press release, 30-May-2026 (merged basis) - as on 31-03-2026 |
| MERGED | EPS (Rs) | Q4 FY2026 press release, 30-May-2026 (merged basis) |
| MERGED | Dividend per share (Rs) | Q4 FY2026 press release, 30-May-2026 (merged basis) - 445% of Rs 2 face value; highest ever |
| STANDALONE | Revenue from operations | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) P&L L~5859 |
| STANDALONE | Other income | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) P&L L~5860 |
| STANDALONE | Total income | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) P&L L5858 |
| STANDALONE | Excise duty | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) P&L - shown as an EXPENSE |
| STANDALONE | Finance costs | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) P&L L~5866 |
| STANDALONE | Depreciation | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) P&L L~5867 |
| STANDALONE | Profit before tax | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) P&L L~5872 |
| STANDALONE | Profit after tax | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) P&L L~5878 |
| STANDALONE | Borrowings - non-current | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) BS L~5815 - NIL |
| STANDALONE | Borrowings - current | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) BS L~5823 - NIL |
| STANDALONE | Lease liabilities - NC | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) BS L~5816 |
| STANDALONE | Cash & equivalents | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) BS L~5803 |
| STANDALONE | Other bank balances | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) BS L~5804 |
| STANDALONE | Total equity | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) BS L~5813 |
| STANDALONE | Total assets | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) BS L~5810 |
| STANDALONE | Trade receivables | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) BS L~5802 |
| STANDALONE | Inventories | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) BS L~5799 |
| STANDALONE | Deferred tax liability | FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme) BS L~5818 |

## 6. OUTSTANDING - the sections that require the documents to be read

These are **not** in this document and have **not** been done. They are named here so the gap is visible rather than silent.

- [ ] **Document Read Log (Step 1b)** - one row per uploaded file: what it is, the key facts it contributes, the material items it flags. A file not in the log has not been read.
- [ ] **Qualitative fact register (Step 7)** - every non-computed claim traced to a document location, and corroborated against a second source where one exists (response protocol 2(e)).
- [ ] **Materiality sweep (Step 8)** - the untouched sections of every file walked for credit-relevant items, each tagged material/immaterial against the R13 test with a written include/exclude decision.
- [ ] **Methodology Compliance Map (Step 10)** - one row per rating factor as the methodology names it, scored with the company's actual numbers against the indicative band, every notching criterion quoted verbatim.
- [ ] **Liquidity computation (Step 11)** - sources-vs-claims arithmetic over ~12 months; the descriptor is the conclusion of that arithmetic, never an adjective.

## 7. Rating view as delivered (Step 13-15, from this case's own rationale)

Source: `Gujarat Energy Limited_20 Aug 2026_CareEdge_Rating Rationale.md`

> reviewed. Financial information is as on 31 March 2026 (merged basis) and 31 March 2025

Sections present in the delivered rationale:

- **Gujarat Energy Limited**
- **Rationale and key rating drivers**
- **Rating sensitivities: Factors likely to lead to rating actions**
- **Positive factors**
- **Negative factors**
- **Analytical approach:** Standalone, with group and government linkage
- **Outlook:** Stable
- **Detailed description of key rating drivers:**
- **Key strengths**
- **Key weaknesses**
- **Liquidity: Strong**
- **Environment, social, and governance (ESG) risks**
- **Applicable criteria**
- **About the company and industry**
- **Brief Financials (₹ crore)**
- **Annexure I — Details of instruments / facilities**
- **Annexure II — Ratings of the company by other credit rating agencies (as disclosed by the issuer)**
- **Annexure III — Basis and evidence notes**

The rating view itself lives in that document; it is referenced here rather than restated, so the two cannot drift apart.

---

*Reproduce this workpaper: `python tools/make_workpaper.py gujarat-energy-limited --force`. Re-verify the case: `python tools/delivery_audit.py gujarat-energy-limited`.*
