# Ratio Workpaper - Jindal Stainless Limited | CareEdge

*Generated 04 Sep 2026 by `tools/make_workpaper.py` from this case's own `compute_ratios.py`.*

> **What this document is.** The EXTRACTION AND VERIFICATION record for this case: the computed ratio suite, every tie-out with its source, the measured coverage of those tie-outs, and the inputs nothing checks. Every figure below is produced by the engine, not retyped - re-run `python Companies/jindal-stainless/compute_ratios.py` to reproduce it.
>
> **What this document is NOT.** It does not contain the Document Read Log, the qualitative fact register, the materiality sweep or the Methodology Compliance Map. Those require the documents to have been read and are listed by name in section 6 as outstanding. They are not generated here because a fabricated Read Log reads as diligence and stops anyone looking - which is failure mode 20, and the reason failure mode 37 exists.

## 1. Computed ratio suite (Step 6)

Basis: periods as the engine declares them. Values as `compute()` returns them.

| Metric | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| Total operating income | 35,697.03 | 38,562.47 | 39,312.21 | 42,954.66 |
| PBILDT | 3,586.09 | 4,704.29 | 4,666.63 | 5,560.43 |
| PBILDT margin % | 10.05 | 12.20 | 11.87 | 12.94 |
| PAT | 2,083.83 | 2,693.48 | 2,499.72 | 3,184.57 |
| PAT margin % | 5.84 | 6.98 | 6.36 | 7.41 |
| Total debt | 3,958.17 | 6,052.26 | 6,401.87 | 7,460.33 |
| Net debt | 2,726.66 | 3,719.90 | 4,127.50 | 4,525.18 |
| Tangible net worth | 11,009.70 | 13,149.16 | 15,001.41 | 17,900.83 |
| Overall gearing (times) | 0.36 | 0.46 | 0.43 | 0.42 |
| Total debt/PBILDT (times) | 1.10 | 1.29 | 1.37 | 1.34 |
| Net debt/PBILDT (times) | 0.76 | 0.79 | 0.88 | 0.81 |
| TOL/TNW (times) | 1.38 | 1.25 | 1.30 | 1.16 |
| Interest coverage (times) | 11.05 | 8.49 | 7.63 | 9.79 |
| Current ratio (times) | 1.38 | 1.47 | 1.27 | 1.25 |
| EPS (Rs) | 25.68 | 32.95 | 30.42 | 38.76 |
| RoCE % (on avg capital employed) | - | 22.39 | 18.28 | 19.25 |

## 2. Tie-outs (Step 6 gate) - 39/39 reconcile

Each row reconciles a figure this engine DERIVES against one printed somewhere else. A check that compares a value with itself cannot fail and is not a check (failure mode 39).

| # | Check | Computed | Disclosed | Tol | Source | |
|---|---|---|---|---|---|---|
| 1 | Assets = equity + liabilities, FY2023 | 27,115.48 | 27,115.48 | 0.005 | consolidated balance sheet | OK |
| 2 | Total assets vs AR's printed total, FY2023 | 27,115.48 | 27,115.48 | 0.005 | AR consolidated balance sheet, Total row | OK |
| 3 | Assets = equity + liabilities, FY2024 | 30,817.25 | 30,817.25 | 0.005 | consolidated balance sheet | OK |
| 4 | Total assets vs AR's printed total, FY2024 | 30,817.25 | 30,817.25 | 0.005 | AR consolidated balance sheet, Total row | OK |
| 5 | Assets = equity + liabilities, FY2025 | 36,158.05 | 36,158.05 | 0.005 | consolidated balance sheet | OK |
| 6 | Total assets vs AR's printed total, FY2025 | 36,158.05 | 36,158.05 | 0.005 | AR consolidated balance sheet, Total row | OK |
| 7 | Assets = equity + liabilities, FY2026 | 40,703.62 | 40,703.62 | 0.005 | consolidated balance sheet | OK |
| 8 | Total assets vs AR's printed total, FY2026 | 40,703.62 | 40,703.62 | 0.005 | AR consolidated balance sheet, Total row | OK |
| 9 | PBILDT base vs AR's own EBITDA line, FY2025 | 4,666.63 | 4,666.63 | 0.005 | FY2025-26 AR, consolidated financial highlights, EBITDA row | OK |
| 10 | PBILDT base vs AR's own EBITDA line, FY2026 | 5,560.43 | 5,560.43 | 0.005 | FY2025-26 AR, consolidated financial highlights, EBITDA row | OK |
| 11 | PBILDT base + associate + exceptional vs AR note, FY2023 | 3,696.05 | 3,696.05 | 0.005 | FY2023-24 AR capital-management note, EBITDA row | OK |
| 12 | PBILDT base + associate + exceptional vs AR note, FY2024 | 4,856.57 | 4,856.57 | 0.005 | FY2023-24 AR capital-management note, EBITDA row | OK |
| 13 | Borrowings excl. leases vs AR note, FY2023 | 3,871.43 | 3,871.43 | 0.005 | FY2023-24 AR capital-management note, total borrowings | OK |
| 14 | Borrowings excl. leases vs AR note, FY2024 | 5,948.19 | 5,948.19 | 0.005 | FY2023-24 AR capital-management note, total borrowings | OK |
| 15 | Company's own debt-equity pct, FY2023 | 32.35 | 32.35 | 0.005 | FY2023-24 AR capital-management note, debt-equity ratio | OK |
| 16 | Company's own debt-equity pct, FY2024 | 41.38 | 41.38 | 0.005 | FY2023-24 AR capital-management note, debt-equity ratio | OK |
| 17 | Total income = revenue + other income, FY2023 | 35,823.32 | 35,823.32 | 0.005 | AR consolidated statement of profit and loss, Total income row | OK |
| 18 | PAT attribution: owners + NCI = PAT, FY2023 | 2,083.83 | 2,083.83 | 0.005 | AR consolidated statement of profit and loss, 'Profit attributable to' block - three separately printed figures that must reconcile | OK |
| 19 | Total income = revenue + other income, FY2024 | 38,731.59 | 38,731.59 | 0.005 | AR consolidated statement of profit and loss, Total income row | OK |
| 20 | PAT attribution: owners + NCI = PAT, FY2024 | 2,693.48 | 2,693.48 | 0.005 | AR consolidated statement of profit and loss, 'Profit attributable to' block - three separately printed figures that must reconcile | OK |
| 21 | Total income = revenue + other income, FY2025 | 39,603.06 | 39,603.06 | 0.005 | AR consolidated statement of profit and loss, Total income row | OK |
| 22 | PAT attribution: owners + NCI = PAT, FY2025 | 2,499.72 | 2,499.72 | 0.005 | AR consolidated statement of profit and loss, 'Profit attributable to' block - three separately printed figures that must reconcile | OK |
| 23 | Total income = revenue + other income, FY2026 | 43,306.14 | 43,306.14 | 0.005 | AR consolidated statement of profit and loss, Total income row | OK |
| 24 | PAT attribution: owners + NCI = PAT, FY2026 | 3,184.57 | 3,184.57 | 0.005 | AR consolidated statement of profit and loss, 'Profit attributable to' block - three separately printed figures that must reconcile | OK |
| 25 | PBT base + associate share = PBT before exceptional, FY2023 | 2,773.97 | 2,773.97 | 0.005 | AR consolidated P&L - three separately printed rows | OK |
| 26 | PBT before exceptional + exceptional = PBT, FY2023 | 2,773.97 | 2,773.97 | 0.005 | AR consolidated P&L - three separately printed rows | OK |
| 27 | PBT base + associate share = PBT before exceptional, FY2024 | 3,493.32 | 3,493.32 | 0.005 | AR consolidated P&L - three separately printed rows | OK |
| 28 | PBT before exceptional + exceptional = PBT, FY2024 | 3,592.47 | 3,592.47 | 0.005 | AR consolidated P&L - three separately printed rows | OK |
| 29 | PBT base + associate share = PBT before exceptional, FY2025 | 3,346.02 | 3,346.02 | 0.005 | AR consolidated P&L - three separately printed rows | OK |
| 30 | PBT before exceptional + exceptional = PBT, FY2025 | 3,338.96 | 3,338.96 | 0.005 | AR consolidated P&L - three separately printed rows | OK |
| 31 | PBT base + associate share = PBT before exceptional, FY2026 | 4,300.41 | 4,300.41 | 0.005 | AR consolidated P&L - three separately printed rows | OK |
| 32 | PBT before exceptional + exceptional = PBT, FY2026 | 4,242.07 | 4,242.07 | 0.005 | AR consolidated P&L - three separately printed rows | OK |
| 33 | Other Expenses note components sum to its printed total, FY2025 | 6,924.31 | 6,924.31 | 0.005 | FY2025-26 AR note 34, all 25 line items against the note's Total row | OK |
| 34 | Forex line in the note matches the engine input, FY2025 | -154.37 | -154.37 | 0.005 | note 34 - binds the P&L note figure to the value the engine carries | OK |
| 35 | Other Expenses note components sum to its printed total, FY2026 | 7,894.46 | 7,894.46 | 0.005 | FY2025-26 AR note 34, all 25 line items against the note's Total row | OK |
| 36 | Forex line in the note matches the engine input, FY2026 | -78.41 | -78.41 | 0.005 | note 34 - binds the P&L note figure to the value the engine carries | OK |
| 37 | Forex FY2023 corroborated in a second annual report | 68.48 | 68.48 | 0.005 | FY2022-23 AR and FY2023-24 AR both state (68.48) - two independent documents | OK |
| 38 | CareEdge rated facilities sum to their published total | 17,999.00 | 17,999.00 | 0.005 | CareEdge press release 09-Oct-2025 - line-integrity check only (failure mode 12); not carried into this report as a Total row | OK |
| 39 | Outstanding NCD, 990 debentures of Rs 10 lakh each, FY2026 | 99.00 | 99.00 | 0.005 | FY2025-26 AR Note 18, non-current borrowings | OK |

## 3. Tie-out coverage, measured by mutation (Step 6 / failure mode 39)

`python tools/tieout_mutation.py jindal-stainless` -> **98.2% coverage**.

Coverage is MEASURED, not asserted: the harness perturbs every numeric input and reports which ones no tie-out notices. A suite can be 100%% green and still verify nothing, so the count of passing checks is not the question - the question is which inputs would be caught if they were wrong.

Inputs no tie-out is sensitive to (5):

| Table | Input | Period | Value |
|---|---|---|---|
| PL | EPS basic (Rs) | FY2023 | 25.68 |
| PL | EPS basic (Rs) | FY2024 | 32.95 |
| PL | EPS basic (Rs) | FY2025 | 30.42 |
| PL | EPS basic (Rs) | FY2026 | 38.76 |
| PL | Forex gain in Other Expenses | FY2024 | -190.04 |

## 4. Disclosed differences and unverified inputs (carried from the engine)

- **PL** - EPS basic (Rs)
- **PL** - EPS basic (Rs)
- **PL** - EPS basic (Rs)
- **PL** - EPS basic (Rs)
- **PL** - Forex gain in Other Expenses
- **Five inputs are verified by no tie-out, and here they are** - Measured by mutation, not asserted: perturbing each of this engine's 278 inputs and re-running the suite shows 273 of them change at least one tie-out - 98.2% coverage. The five that change NOTHING are (a) basic EPS in all four years, which cannot be checked without a weighted average share count that the extracted data does not carry, and (b) the FY2024 foreign-currency line, because the FY2023-24 annual report's Other Expenses note was not decomposed to its line items the way FY2025 and FY2026 were. EPS is display-only and feeds no ratio. The FY2024 forex figure feeds no ratio either - it is quoted in the rationale's narrative and nowhere else. Run `python tieout_mutation.py jindal-stainless` to reproduce. This entry exists because an unverified input that nobody has NAMED is the condition under which the forex error survived three rounds of checking.
- **PBILDT equals the company's own published EBITDA - no residual to explain** - Because neither CareEdge adjustment bites on this issuer, PBILDT here IS the base, and the base reproduces the annual report's own EBITDA line to the paisa in both years the company discloses one (FY2025 4,666.63; FY2026 5,560.43). For FY2023 and FY2024 the older annual report's capital-management note computes EBITDA off FULL profit before tax, so it carries the associate share and the exceptional item; bridging both back reproduces it exactly (FY2023 3,696.05; FY2024 4,856.57). There is no unexplained difference anywhere in the series.
- **Loss on disposal of fixed assets is left unadjusted, and that is a choice** - CareEdge's criteria treat profit or loss on sale of assets as non-operating. Profit on sale of current investments (FY2026 3.75, FY2025 4.85) sits in Other Income and is already excluded by the base. Loss on disposal of property, plant and equipment is NOT isolated as a line in the Other Expenses note; the cash-flow reconciliation implies about 11.61 crore in FY2026, or 0.2% of PBILDT. It is left unadjusted and stated here rather than adjusted off the cash-flow reconciliation - which had already been misread once in this case, when its unrealised-forex row was mistaken for the P&L forex line.
- **Adjusted leverage cannot be computed - two CareEdge inputs are not separately disclosed** - CareEdge's corporate criteria compute an ADJUSTED gearing that adds acceptances / LC creditors to total debt and adds back corporate guarantees issued to group entities. The trade-payables ageing note (note 55) confirms in a footnote that amounts pertaining to letters of credit ARE included within 'Others' trade payables, but does not quantify them; searches for 'acceptance', "buyer's credit" and 'letter of credit' return no separate figure in the consolidated accounts, and guarantees to subsidiaries are not separately quantified either. Gearing and net debt/PBILDT here are therefore the UNADJUSTED measures. This matters more than a footnote suggests: CareEdge's own published sensitivities for this issuer are framed on net debt INCLUDING acceptances, so the adjusted figures would be higher than those stated here. Both inputs should be obtained from the issuer.
- **Sales volume for FY2025 is derived, not disclosed** - The FY2025-26 annual report states finished-goods sales volume of approximately 2.57 MT in FY2026, up 8.1%. The FY2025 figure of 2.377 MT is BACK-SOLVED from that growth rate and is not separately published, so PBILDT per tonne for FY2025 (19,633) inherits that derivation. Both per-tonne figures also rest on a volume the company itself reports as approximate, so they are indicative to roughly the nearest hundred rupees rather than precise to the rupee.

## 6. OUTSTANDING - the sections that require the documents to be read

These are **not** in this document and have **not** been done. They are named here so the gap is visible rather than silent.

- [ ] **Document Read Log (Step 1b)** - one row per uploaded file: what it is, the key facts it contributes, the material items it flags. A file not in the log has not been read.
- [ ] **Qualitative fact register (Step 7)** - every non-computed claim traced to a document location, and corroborated against a second source where one exists (response protocol 2(e)).
- [ ] **Materiality sweep (Step 8)** - the untouched sections of every file walked for credit-relevant items, each tagged material/immaterial against the R13 test with a written include/exclude decision.
- [ ] **Methodology Compliance Map (Step 10)** - one row per rating factor as the methodology names it, scored with the company's actual numbers against the indicative band, every notching criterion quoted verbatim.
- [ ] **Liquidity computation (Step 11)** - sources-vs-claims arithmetic over ~12 months; the descriptor is the conclusion of that arithmetic, never an adjective.

## 7. Rating view as delivered (Step 13-15, from this case's own rationale)

Source: `Jindal Stainless Limited_26 Aug 2026_CARE_Rating Rationale.md`

> Press Release

Sections present in the delivered rationale:

- **Jindal Stainless Limited**
- **Rationale and key rating drivers**
- **Rating sensitivities: Factors likely to lead to rating actions**
- **Positive factors**
- **Negative factors**
- **Analytical approach:** Consolidated
- **Outlook:** Stable
- **Key strengths**
- **Key weaknesses**
- **Liquidity: Strong**
- **Assumptions/Covenants**
- **Environment, social, and governance (ESG) risks**
- **Applicable criteria**
- **About the company and industry**
- **Brief Financials (Consolidated)**
- **Status of non-cooperation with previous CRA:** Not applicable
- **Any other information**
- **Rating history for last three years**
- **Covenants of rated instruments:** Detailed explanation of covenants of the rated instruments is given in Annexure-4.
- **Complexity level of the various instruments rated:** Annexure-5.
- **Annexure-1: Details of instruments/facilities**
- **Annexure-2: List of entities consolidated**
- **Annexure-3: Rating history for last three years**
- **Annexure-4: Covenants of rated instruments**

The rating view itself lives in that document; it is referenced here rather than restated, so the two cannot drift apart.

---

*Reproduce this workpaper: `python tools/make_workpaper.py jindal-stainless --force`. Re-verify the case: `python tools/delivery_audit.py jindal-stainless`.*
