# Ratio Workpaper - BALKRISHNA INDUSTRIES LTD | ICRA

*Generated 04 Sep 2026 by `tools/make_workpaper.py` from this case's own `compute_ratios.py`.*

> **What this document is.** The EXTRACTION AND VERIFICATION record for this case: the computed ratio suite, every tie-out with its source, the measured coverage of those tie-outs, and the inputs nothing checks. Every figure below is produced by the engine, not retyped - re-run `python Companies/balkrishna-industries-ltd/compute_ratios.py` to reproduce it.
>
> **What this document is NOT.** It does not contain the Document Read Log, the qualitative fact register, the materiality sweep or the Methodology Compliance Map. Those require the documents to have been read and are listed by name in section 6 as outstanding. They are not generated here because a fabricated Read Log reads as diligence and stops anyone looking - which is failure mode 20, and the reason failure mode 37 exists.

## 1. Computed ratio suite (Step 6)

Basis: periods as the engine declares them. Values as `compute()` returns them.

| Metric | FY2023 | FY2024 | FY2025 | FY2026 | Q1FY2027 |
|---|---|---|---|---|---|
| Revenue from operations | 9,759.53 | 9,368.87 | 10,446.95 | 10,823.08 | 3,455.27 |
| OPBDITA | 1,707.11 | 2,255.37 | 2,457.60 | 2,590.44 | 744.40 |
| OPBDITA margin % | 17.49 | 24.07 | 23.52 | 23.93 | 21.54 |
| PAT | 1,057.40 | 1,471.49 | 1,654.96 | 1,243.10 | 450.77 |
| PAT margin % | 10.83 | 15.71 | 15.84 | 11.49 | 12.68 |
| Total debt | 3,346.53 | 3,099.44 | 3,267.45 | 4,110.82 | - |
| Net debt | 2,495.60 | 1,670.45 | 1,478.42 | 2,718.83 | - |
| Net worth (TNW) | 7,556.93 | 8,853.82 | 10,387.60 | 10,955.29 | 11,583.84 |
| Gearing (times) | 0.44 | 0.35 | 0.31 | 0.38 | 0.41 |
| Net gearing (times) | 0.33 | 0.19 | 0.14 | 0.25 | - |
| TOL/TNW (times) | 0.63 | 0.55 | 0.51 | 0.62 | - |
| Total debt/OPBDITA (times) | 1.96 | 1.37 | 1.33 | 1.59 | - |
| Net debt/OPBDITA (times) | 1.46 | 0.74 | 0.60 | 1.05 | - |
| Interest coverage (times) | 35.54 | 19.98 | 19.15 | 19.39 | - |
| RoCE % | 10.20 | 13.04 | 12.59 | 11.80 | - |
| Current ratio (times) | 1.17 | 1.27 | 1.32 | 1.01 | - |
| Debtor days | 41.71 | 56.31 | 52.22 | 48.78 | - |
| Inventory days | 123.82 | 108.21 | 128.53 | 126.28 | - |
| Payable days | 36.55 | 65.68 | 54.38 | 63.70 | - |
| Working capital cycle (days) | 128.98 | 98.84 | 126.36 | 111.36 | - |
| EPS (Rs) | 54.70 | 76.12 | 85.61 | 64.30 | - |

## 2. Tie-outs (Step 6 gate) - 68/68 reconcile

Each row reconciles a figure this engine DERIVES against one printed somewhere else. A check that compares a value with itself cannot fail and is not a check (failure mode 39).

| # | Check | Computed | Disclosed | Tol | Source | |
|---|---|---|---|---|---|---|
| 1 | Other Expenses note components sum to its printed total, FY2025 | 2,374.53 | 2,374.53 | 0.005 | consolidated note 37, all 22 line items vs the note's Total row | OK |
| 2 | Other Expenses note total = the P&L line, FY2025 | 2,374.53 | 2,374.53 | 0.005 | note 37 total against the P&L's Other Expenses row | OK |
| 3 | Forex line in note 37 matches the engine's add-back input, FY2025 | 0.00 | 0.00 | 0.005 | binds the note figure to the value fed into OPBDITA (failure mode 36) | OK |
| 4 | Other Expenses note components sum to its printed total, FY2026 | 2,699.31 | 2,699.31 | 0.005 | consolidated note 37, all 22 line items vs the note's Total row | OK |
| 5 | Other Expenses note total = the P&L line, FY2026 | 2,699.31 | 2,699.31 | 0.005 | note 37 total against the P&L's Other Expenses row | OK |
| 6 | Forex line in note 37 matches the engine's add-back input, FY2026 | 290.01 | 290.01 | 0.005 | binds the note figure to the value fed into OPBDITA (failure mode 36) | OK |
| 7 | Total income = revenue + other income, FY2023 | 10,106.06 | 10,106.06 | 0.02 | consolidated statement of profit and loss, printed Total Income row | OK |
| 8 | Total expenses = sum of the printed expense lines, FY2023 | 8,671.27 | 8,671.27 | 0.02 | consolidated statement of profit and loss, printed Total Expenses row | OK |
| 9 | PBT = total income - total expenses, FY2023 | 1,434.79 | 1,434.79 | 0.02 | consolidated statement of profit and loss - three printed rows | OK |
| 10 | PAT = PBT - tax expense, FY2023 | 1,057.40 | 1,057.40 | 0.02 | consolidated statement of profit and loss - three printed rows | OK |
| 11 | Total income = revenue + other income, FY2024 | 9,818.09 | 9,818.09 | 0.02 | consolidated statement of profit and loss, printed Total Income row | OK |
| 12 | Total expenses = sum of the printed expense lines, FY2024 | 7,877.09 | 7,877.09 | 0.02 | consolidated statement of profit and loss, printed Total Expenses row | OK |
| 13 | PBT = total income - total expenses, FY2024 | 1,941.00 | 1,941.00 | 0.02 | consolidated statement of profit and loss - three printed rows | OK |
| 14 | PAT = PBT - tax expense, FY2024 | 1,471.49 | 1,471.49 | 0.02 | consolidated statement of profit and loss - three printed rows | OK |
| 15 | Total income = revenue + other income, FY2025 | 10,985.74 | 10,985.74 | 0.02 | consolidated statement of profit and loss, printed Total Income row | OK |
| 16 | Total expenses = sum of the printed expense lines, FY2025 | 8,798.35 | 8,798.35 | 0.02 | consolidated statement of profit and loss, printed Total Expenses row | OK |
| 17 | PBT = total income - total expenses, FY2025 | 2,187.39 | 2,187.39 | 0.02 | consolidated statement of profit and loss - three printed rows | OK |
| 18 | PAT = PBT - tax expense, FY2025 | 1,654.96 | 1,654.96 | 0.02 | consolidated statement of profit and loss - three printed rows | OK |
| 19 | Total income = revenue + other income, FY2026 | 11,074.91 | 11,074.91 | 0.02 | consolidated statement of profit and loss, printed Total Income row | OK |
| 20 | Total expenses = sum of the printed expense lines, FY2026 | 9,431.23 | 9,431.23 | 0.02 | consolidated statement of profit and loss, printed Total Expenses row | OK |
| 21 | PBT = total income - total expenses, FY2026 | 1,643.68 | 1,643.68 | 0.02 | consolidated statement of profit and loss - three printed rows | OK |
| 22 | PAT = PBT - tax expense, FY2026 | 1,243.10 | 1,243.10 | 0.02 | consolidated statement of profit and loss - three printed rows | OK |
| 23 | Total income = revenue + other income, Q1FY2027 | 3,554.94 | 3,554.94 | 0.02 | consolidated statement of profit and loss, printed Total Income row | OK |
| 24 | Total expenses = sum of the printed expense lines, Q1FY2027 | 2,953.89 | 2,953.89 | 0.02 | consolidated statement of profit and loss, printed Total Expenses row | OK |
| 25 | PBT = total income - total expenses, Q1FY2027 | 601.05 | 601.05 | 0.02 | consolidated statement of profit and loss - three printed rows | OK |
| 26 | PAT = PBT - tax expense, Q1FY2027 | 450.77 | 450.77 | 0.02 | consolidated statement of profit and loss - three printed rows | OK |
| 27 | Total non-current assets components sum to the AR's printed row, FY2023 | 8,419.71 | 8,419.71 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 28 | Total current assets components sum to the AR's printed row, FY2023 | 3,927.95 | 3,927.95 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 29 | Total NC liabilities components sum to the AR's printed row, FY2023 | 1,441.46 | 1,441.46 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 30 | Total current liabilities components sum to the AR's printed row, FY2023 | 3,349.27 | 3,349.27 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 31 | Total assets components sum to the AR's printed row, FY2023 | 12,347.66 | 12,347.66 | 0.005 | consolidated balance sheet, printed TOTAL ASSETS | OK |
| 32 | Assets = equity + liabilities, FY2023 | 12,347.66 | 12,347.66 | 0.005 | consolidated balance sheet | OK |
| 33 | Total non-current assets components sum to the AR's printed row, FY2024 | 9,040.48 | 9,040.48 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 34 | Total current assets components sum to the AR's printed row, FY2024 | 4,644.06 | 4,644.06 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 35 | Total NC liabilities components sum to the AR's printed row, FY2024 | 1,170.28 | 1,170.28 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 36 | Total current liabilities components sum to the AR's printed row, FY2024 | 3,660.44 | 3,660.44 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 37 | Total assets components sum to the AR's printed row, FY2024 | 13,684.54 | 13,684.54 | 0.005 | consolidated balance sheet, printed TOTAL ASSETS | OK |
| 38 | Assets = equity + liabilities, FY2024 | 13,684.54 | 13,684.54 | 0.005 | consolidated balance sheet | OK |
| 39 | Total non-current assets components sum to the AR's printed row, FY2025 | 10,063.26 | 10,063.26 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 40 | Total current assets components sum to the AR's printed row, FY2025 | 5,571.40 | 5,571.40 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 41 | Total NC liabilities components sum to the AR's printed row, FY2025 | 1,020.41 | 1,020.41 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 42 | Total current liabilities components sum to the AR's printed row, FY2025 | 4,226.65 | 4,226.65 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 43 | Total assets components sum to the AR's printed row, FY2025 | 15,634.66 | 15,634.66 | 0.005 | consolidated balance sheet, printed TOTAL ASSETS | OK |
| 44 | Assets = equity + liabilities, FY2025 | 15,634.66 | 15,634.66 | 0.005 | consolidated balance sheet | OK |
| 45 | Total non-current assets components sum to the AR's printed row, FY2026 | 12,611.87 | 12,611.87 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 46 | Total current assets components sum to the AR's printed row, FY2026 | 5,154.47 | 5,154.47 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 47 | Total NC liabilities components sum to the AR's printed row, FY2026 | 1,722.05 | 1,722.05 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 48 | Total current liabilities components sum to the AR's printed row, FY2026 | 5,089.00 | 5,089.00 | 0.005 | consolidated balance sheet, printed subtotal | OK |
| 49 | Total assets components sum to the AR's printed row, FY2026 | 17,766.34 | 17,766.34 | 0.005 | consolidated balance sheet, printed TOTAL ASSETS | OK |
| 50 | Assets = equity + liabilities, FY2026 | 17,766.34 | 17,766.34 | 0.005 | consolidated balance sheet | OK |
| 51 | FY2024 total assets: lakh-AR conversion vs crore-AR comparative | 13,684.54 | 13,684.54 | 0.02 | FY2023-24 AR (13,68,454 lakh / 100) vs FY2024-25 AR's FY2024 column | OK |
| 52 | FY2024 total equity: lakh-AR conversion vs crore-AR comparative | 8,853.82 | 8,853.82 | 0.02 | FY2023-24 AR (8,85,382 lakh / 100) vs FY2024-25 AR's FY2024 column | OK |
| 53 | FY2024 revenue from operations: lakh-AR vs crore-AR comparative | 9,368.87 | 9,368.87 | 0.02 | FY2023-24 AR (9,36,887 lakh / 100) vs FY2024-25 AR's FY2024 column | OK |
| 54 | FY2024 PAT: lakh-AR conversion vs crore-AR comparative | 1,471.49 | 1,471.49 | 0.02 | FY2023-24 AR (1,47,149 lakh / 100) vs FY2024-25 AR's FY2024 column | OK |
| 55 | Balance sheet ties, FY2023: assets = equity + NC liab + C liab | 12,347.66 | 12,347.66 | 0.05 | FY2023-24 / FY2025-26 AR consolidated balance sheets | OK |
| 56 | Balance sheet ties, FY2024: assets = equity + NC liab + C liab | 13,684.54 | 13,684.54 | 0.05 | FY2023-24 / FY2025-26 AR consolidated balance sheets | OK |
| 57 | Balance sheet ties, FY2025: assets = equity + NC liab + C liab | 15,634.66 | 15,634.66 | 0.05 | FY2023-24 / FY2025-26 AR consolidated balance sheets | OK |
| 58 | Balance sheet ties, FY2026: assets = equity + NC liab + C liab | 17,766.34 | 17,766.34 | 0.05 | FY2023-24 / FY2025-26 AR consolidated balance sheets | OK |
| 59 | EPS, FY2023 | 54.70 | 54.70 | 0.01 | AR consolidated statement of profit and loss | OK |
| 60 | EPS, FY2024 | 76.12 | 76.12 | 0.01 | AR consolidated statement of profit and loss | OK |
| 61 | EPS, FY2025 | 85.61 | 85.61 | 0.01 | AR consolidated statement of profit and loss | OK |
| 62 | EPS, FY2026 | 64.30 | 64.30 | 0.01 | AR consolidated statement of profit and loss | OK |
| 63 | Gearing (Debt-Equity ratio), FY2026 | 0.38 | 0.37 | 0.01 | Q1 FY2026-27 filing, Reg 52(4) disclosure, consolidated, year-ended column | OK |
| 64 | Operating margin (company's own EBIT-based measure, REPORTED base), FY2026 | 14.09 | 14.09 | 0.15 | Q1 FY2026-27 filing Reg 52(4): 'EBIT less other income / revenue' - a DIFFERENT convention from OPBDITA margin (this row excludes depreciation, ICRA's OPBDITA margin above does not); both are reported, neither forced onto the other | OK |
| 65 | Net profit margin (PAT/Total income), FY2026 | 11.22 | 11.22 | 0.05 | Q1 FY2026-27 filing Reg 52(4): PAT / TOTAL INCOME (includes other income), a different denominator from the OPBDITA-margin row's revenue-only base | OK |
| 66 | Current ratio, FY2026 | 1.01 | 1.01 | 0.01 | Q1 FY2026-27 filing, Reg 52(4) disclosure, consolidated | OK |
| 67 | Note 46 contingent liabilities sum to the total quoted in the rationale | 946.09 | 946.09 | 0.01 | FY2025-26 AR, standalone Note 46 | OK |
| 68 | FY2026 capex, cash-flow statement vs MD&A headline figure | 3,003.29 | 2,984.00 | 25 | Consolidated cash flow 'Purchase of Property, Plant and equipment' 3,003.29 vs MD&A 'Capital expenditure for the year was Rs 2,984 Crores' - the MD&A figure likely nets small disposals/capitalised items differently; both disclosed, gap of Rs 19.29 crore (0.6%) is immaterial and stated rather than silently picked | OK |

## 3. Tie-out coverage, measured by mutation (Step 6 / failure mode 39)

`python tools/tieout_mutation.py balkrishna-industries-ltd` -> **98.5% coverage**.

Coverage is MEASURED, not asserted: the harness perturbs every numeric input and reports which ones no tie-out notices. A suite can be 100%% green and still verify nothing, so the count of passing checks is not the question - the question is which inputs would be caught if they were wrong.

Inputs no tie-out is sensitive to (4):

| Table | Input | Period | Value |
|---|---|---|---|
| PL | Non-op. in other expenses | FY2023 | 0.00 |
| PL | Non-op. in other expenses | FY2024 | 0.00 |
| PL | Non-op. in other expenses | Q1FY2027 | 0.00 |
| PL | EPS (Rs) | Q1FY2027 | 23.32 |

## 4. Disclosed differences and unverified inputs (carried from the engine)

- **PL** - Non-op. in other expenses
- **PL** - Non-op. in other expenses
- **PL** - Non-op. in other expenses
- **PL** - EPS (Rs)
- **Four inputs are verified by no tie-out, and here they are** - Measured by mutation rather than asserted: perturbing each of this engine's 268 inputs and re-running the suite shows 264 of them break at least one tie-out - 98.5% coverage, up from 13.4% before the balance-sheet totals were derived instead of typed. The four that change nothing are the non-operating add-back for FY2023, FY2024 and Q1FY2027 (all nil - the Other Expenses note is decomposed and tied only for FY2025 and FY2026, the two years the FY2025-26 annual report prints in full) and Q1FY2027 basic EPS, which cannot be checked without a weighted average share count the extraction does not carry. None feeds a published ratio for those periods. Reproduce with `python tieout_mutation.py balkrishna-industries-ltd`.
- **Residual gap to ICRA's published OPBDIT/OI after the failure-mode-36 correction** - ICRA's own published rationale (25-Aug-2026) states OPBDIT/OI of 23.9% (FY2025) and 24.3% (FY2026). This engine computes 23.52% and 23.93% after adding back the Rs 290.01 crore forex loss buried in Other Expenses. The add-back closes 2.68 of the original 3.05-point gap and, decisively, corrects the DIRECTION - the uncorrected series showed margin FALLING 2.27pt when it actually ROSE 0.41pt, against ICRA's +0.4pt. A residual of ~0.38pt (~Rs 40 crore) persists in BOTH years, which is itself the useful signal: a constant offset means a further standing normalisation, not an error in any one year. The closest single candidate is CSR expenditure (Rs 34.04 crore FY2026, Rs 32.94 crore FY2025, a statutory appropriation ICRA may add back), which would close most of it - but that cannot be confirmed from ICRA's published summary, so it is DISCLOSED here rather than assumed and forced into the build (failure mode 32: never adjust inputs to force a tie).
- **Interest coverage differs from ICRA's published figure - denominator basis** - ICRA publishes interest coverage of 22.3x (FY2025) and 23.7x (FY2026); this engine computes 19.15x and 19.39x. Solving back, ICRA's denominator is ~Rs 110 crore (FY2025) and ~Rs 109 crore (FY2026) against reported finance costs of Rs 128.34 crore and Rs 133.62 crore - i.e. ICRA nets roughly Rs 18-24 crore out of the finance-cost line. That is consistent with excluding interest on lease liabilities, interest to others and discount unwinding (the company's own Reg 52(4) ISCR likewise uses 'Interest on Term Loan & Debentures' only). The exact composition is not recoverable from the published summary, so the full reported finance cost is used and the difference is stated.
- **Two distinct 'margin' conventions in the company's own disclosures** - The Reg 52(4) filing's 'Operating Margin' is EBIT (i.e. after depreciation) less other income, over revenue - 14.09% for FY2026. ICRA's OPBDITA margin (before depreciation) is a different, larger number - 22.30% for FY2026 (see RatioSuite). Both are reported under their own label; the OPBDITA figure is ICRA's headline convention and the Reg 52(4) figure is reproduced only as a tie-out check, per CLAUDE.md failure mode 32's logic that a convention that will not reproduce a published figure is the wrong one to STATE as if it were that figure - here neither is wrong, they simply measure different things.
- **FY2024 trade payables / other financial liabilities reclassified between annual reports** - The FY2023-24 AR states FY2024 trade payables of Rs 910.23 crore and other financial liabilities of Rs 156.26 crore; the FY2024-25 AR's restated FY2024 comparative states Rs 808.19 crore and Rs 258.30 crore respectively - a Rs 102.04 crore reclassification between the two lines. Both totals (current liabilities Rs 3,660.44 crore; total assets Rs 13,684.54 crore) are identical in both annual reports and tie exactly either way - only the line-item split changed. This engine uses the NEWER document's split throughout, per CLAUDE.md failure mode 26.

## 6. OUTSTANDING - the sections that require the documents to be read

These are **not** in this document and have **not** been done. They are named here so the gap is visible rather than silent.

- [ ] **Document Read Log (Step 1b)** - one row per uploaded file: what it is, the key facts it contributes, the material items it flags. A file not in the log has not been read.
- [ ] **Qualitative fact register (Step 7)** - every non-computed claim traced to a document location, and corroborated against a second source where one exists (response protocol 2(e)).
- [ ] **Materiality sweep (Step 8)** - the untouched sections of every file walked for credit-relevant items, each tagged material/immaterial against the R13 test with a written include/exclude decision.
- [ ] **Methodology Compliance Map (Step 10)** - one row per rating factor as the methodology names it, scored with the company's actual numbers against the indicative band, every notching criterion quoted verbatim.
- [ ] **Liquidity computation (Step 11)** - sources-vs-claims arithmetic over ~12 months; the descriptor is the conclusion of that arithmetic, never an adjective.

## 7. Rating view as delivered (Step 13-15, from this case's own rationale)

Source: `Balkrishna Industries Limited_25 Aug 2026_Rating Rationale.md`

> August 25, 2026

Sections present in the delivered rationale:

- Summary of rating action
- Rationale
- Key rating drivers and their description
- Credit strengths
- Credit challenges
- Environmental and social risks
- Liquidity position: Strong
- Rating sensitivities
- Analytical approach
- About the company
- Key financial indicators (audited; consolidated)
- Status of non-cooperation with previous CRA: Not applicable
- Any other information
- Rating history for past three years
- Complexity level of the rated instruments
- Annexure I: Instrument details
- Annexure II: List of entities considered for consolidated analysis

The rating view itself lives in that document; it is referenced here rather than restated, so the two cannot drift apart.

---

*Reproduce this workpaper: `python tools/make_workpaper.py balkrishna-industries-ltd --force`. Re-verify the case: `python tools/delivery_audit.py balkrishna-industries-ltd`.*
