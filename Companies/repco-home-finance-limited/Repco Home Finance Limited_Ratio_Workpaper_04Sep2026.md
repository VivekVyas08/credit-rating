# Ratio Workpaper - Repco Home Finance Limited | ICRA

*Generated 04 Sep 2026 by `tools/make_workpaper.py` from this case's own `compute_ratios.py`.*

> **What this document is.** The EXTRACTION AND VERIFICATION record for this case: the computed ratio suite, every tie-out with its source, the measured coverage of those tie-outs, and the inputs nothing checks. Every figure below is produced by the engine, not retyped - re-run `python Companies/repco-home-finance-limited/compute_ratios.py` to reproduce it.
>
> **What this document is NOT.** It does not contain the Document Read Log, the qualitative fact register, the materiality sweep or the Methodology Compliance Map. Those require the documents to have been read and are listed by name in section 6 as outstanding. They are not generated here because a fabricated Read Log reads as diligence and stops anyone looking - which is failure mode 20, and the reason failure mode 37 exists.

## 1. Computed ratio suite (Step 6)

Basis: periods as the engine declares them. Values as `compute()` returns them.

| Metric | FY2023 | FY2024 | FY2025 | Q1FY2027 |
|---|---|---|---|---|
| Total income | 1,299.16 | 1,540.80 | 1,724.55 | 467.90 |
| Net interest income | 582.67 | 678.95 | 719.30 | 216.41 |
| Operating expenses | 145.78 | 171.02 | 208.77 | 59.18 |
| Pre-provision operating profit | 452.31 | 524.21 | 549.92 | 157.43 |
| PAT | 296.08 | 394.70 | 439.44 | 114.15 |
| Total managed assets | 13,042.47 | 14,224.97 | 15,035.63 | 16,245.83 |
| Total debt | 9,924.08 | 10,701.04 | 11,139.09 | 12,087.01 |
| Net worth | 2,516.17 | 2,893.95 | 3,313.55 | 4,018.65 |
| Tangible net worth | 2,508.65 | 2,878.42 | 3,294.52 | 3,995.75 |
| NIM % (on avg total assets) | 4.75 | 5.18 | 5.08 | 5.51 |
| Opex / avg total assets % | 1.19 | 1.30 | 1.47 | 1.51 |
| Cost-to-income % | 24.37 | 24.60 | 27.52 | 27.32 |
| Credit cost % (on avg managed assets) | 0.40 | -0.00 | -0.26 | 0.25 |
| Return on avg managed assets % | 2.32 | 2.90 | 3.00 | 2.91 |
| Return on avg total assets % | 2.41 | 3.01 | 3.10 | 2.91 |
| Return on avg net worth % | 12.46 | 14.59 | 14.16 | 12.17 |
| Gearing (times) | 3.94 | 3.70 | 3.36 | 3.01 |
| Gearing on tangible net worth (times) | 3.96 | 3.72 | 3.38 | 3.02 |
| Managed assets / tangible net worth (times) | 5.20 | 4.94 | 4.56 | 4.07 |
| Equity / total assets % | 20.09 | 21.11 | 22.69 | 24.74 |
| Book value per share (Rs) | 402.19 | 462.58 | 529.65 | 642.35 |
| Basic EPS (Rs) | 47.33 | 63.09 | 70.24 | 72.98 |
| Liquid assets (cash + other bank balances) | 454.43 | 408.40 | 136.29 | 142.12 |

## 2. Tie-outs (Step 6 gate) - 65/65 reconcile

Each row reconciles a figure this engine DERIVES against one printed somewhere else. A check that compares a value with itself cannot fail and is not a check (failure mode 39).

| # | Check | Computed | Disclosed | Tol | Source | |
|---|---|---|---|---|---|---|
| 1 | Asset components sum to the printed Total assets, FY2022 | 11,997.39 | 11,997.39 | 0.02 | balance sheet, printed Total assets row | OK |
| 2 | Liability components sum to the printed Total liabilities, FY2022 | 9,761.79 | 9,761.79 | 0.02 | balance sheet, printed Total liabilities row | OK |
| 3 | Asset components sum to the printed Total assets, FY2023 | 12,523.43 | 12,523.43 | 0.02 | balance sheet, printed Total assets row | OK |
| 4 | Liability components sum to the printed Total liabilities, FY2023 | 10,007.26 | 10,007.26 | 0.02 | balance sheet, printed Total liabilities row | OK |
| 5 | Asset components sum to the printed Total assets, FY2024 | 13,707.11 | 13,707.11 | 0.02 | balance sheet, printed Total assets row | OK |
| 6 | Liability components sum to the printed Total liabilities, FY2024 | 10,813.16 | 10,813.16 | 0.02 | balance sheet, printed Total liabilities row | OK |
| 7 | Asset components sum to the printed Total assets, FY2025 | 14,602.24 | 14,602.24 | 0.02 | balance sheet, printed Total assets row | OK |
| 8 | Liability components sum to the printed Total liabilities, FY2025 | 11,288.69 | 11,288.69 | 0.02 | balance sheet, printed Total liabilities row | OK |
| 9 | Asset components sum to the printed Total assets, 30-Sep-2025 | 15,187.10 | 15,187.10 | 0.02 | balance sheet, printed Total assets row | OK |
| 10 | Liability components sum to the printed Total liabilities, 30-Sep-2025 | 11,699.82 | 11,699.82 | 0.02 | balance sheet, printed Total liabilities row | OK |
| 11 | Asset components sum to the printed Total assets, Q1FY2027 | 16,245.83 | 16,245.83 | 0.02 | balance sheet, printed Total assets row | OK |
| 12 | Liability components sum to the printed Total liabilities, Q1FY2027 | 12,227.18 | 12,227.18 | 0.02 | balance sheet, printed Total liabilities row | OK |
| 13 | Revenue components sum to Revenue from operations, FY2023 | 1,283.74 | 1,283.74 | 0.02 | statement of profit and loss, printed Revenue from operations row | OK |
| 14 | Total income = revenue + other income, FY2023 | 1,299.16 | 1,299.16 | 0.02 | statement of profit and loss, printed Total income row | OK |
| 15 | Expense components sum to Total expenses, FY2023 | 898.40 | 898.40 | 0.02 | statement of profit and loss, printed Total expenses row | OK |
| 16 | PBT = total income - total expenses, FY2023 | 400.76 | 400.76 | 0.02 | statement of profit and loss - three printed rows | OK |
| 17 | PAT = PBT - tax expense, FY2023 | 296.08 | 296.08 | 0.02 | statement of profit and loss - three printed rows | OK |
| 18 | Revenue components sum to Revenue from operations, FY2024 | 1,524.52 | 1,524.52 | 0.02 | statement of profit and loss, printed Revenue from operations row | OK |
| 19 | Total income = revenue + other income, FY2024 | 1,540.80 | 1,540.80 | 0.02 | statement of profit and loss, printed Total income row | OK |
| 20 | Expense components sum to Total expenses, FY2024 | 1,016.08 | 1,016.08 | 0.02 | statement of profit and loss, printed Total expenses row | OK |
| 21 | PBT = total income - total expenses, FY2024 | 524.72 | 524.72 | 0.02 | statement of profit and loss - three printed rows | OK |
| 22 | PAT = PBT - tax expense, FY2024 | 394.70 | 394.70 | 0.02 | statement of profit and loss - three printed rows | OK |
| 23 | Revenue components sum to Revenue from operations, FY2025 | 1,685.16 | 1,685.16 | 0.02 | statement of profit and loss, printed Revenue from operations row | OK |
| 24 | Total income = revenue + other income, FY2025 | 1,724.55 | 1,724.55 | 0.02 | statement of profit and loss, printed Total income row | OK |
| 25 | Expense components sum to Total expenses, FY2025 | 1,137.06 | 1,137.06 | 0.02 | statement of profit and loss, printed Total expenses row | OK |
| 26 | PBT = total income - total expenses, FY2025 | 587.49 | 587.49 | 0.02 | statement of profit and loss - three printed rows | OK |
| 27 | PAT = PBT - tax expense, FY2025 | 439.44 | 439.44 | 0.02 | statement of profit and loss - three printed rows | OK |
| 28 | Revenue components sum to Revenue from operations, FY2026 | 1,795.79 | 1,795.79 | 0.02 | statement of profit and loss, printed Revenue from operations row | OK |
| 29 | Total income = revenue + other income, FY2026 | 1,797.69 | 1,797.69 | 0.02 | statement of profit and loss, printed Total income row | OK |
| 30 | Expense components sum to Total expenses, FY2026 | 1,211.65 | 1,211.65 | 0.02 | statement of profit and loss, printed Total expenses row | OK |
| 31 | PBT = total income - total expenses, FY2026 | 586.04 | 586.04 | 0.02 | statement of profit and loss - three printed rows | OK |
| 32 | PAT = PBT - tax expense, FY2026 | 452.77 | 452.77 | 0.02 | statement of profit and loss - three printed rows | OK |
| 33 | Revenue components sum to Revenue from operations, Q1FY2027 | 467.70 | 467.70 | 0.02 | statement of profit and loss, printed Revenue from operations row | OK |
| 34 | Total income = revenue + other income, Q1FY2027 | 467.90 | 467.90 | 0.02 | statement of profit and loss, printed Total income row | OK |
| 35 | Expense components sum to Total expenses, Q1FY2027 | 320.16 | 320.16 | 0.02 | statement of profit and loss, printed Total expenses row | OK |
| 36 | PBT = total income - total expenses, Q1FY2027 | 147.74 | 147.74 | 0.02 | statement of profit and loss - three printed rows | OK |
| 37 | PAT = PBT - tax expense, Q1FY2027 | 114.15 | 114.15 | 0.02 | statement of profit and loss - three printed rows | OK |
| 38 | Balance sheet ties, FY2022: assets = liabilities + equity | 11,997.39 | 11,997.39 | 0.02 | FY2023/FY2025 AR balance sheets; Q2FY2026 filing; Reg 54(3) security-cover certificate 30-Jun-2026 | OK |
| 39 | Balance sheet ties, FY2023: assets = liabilities + equity | 12,523.43 | 12,523.43 | 0.02 | FY2023/FY2025 AR balance sheets; Q2FY2026 filing; Reg 54(3) security-cover certificate 30-Jun-2026 | OK |
| 40 | Balance sheet ties, FY2024: assets = liabilities + equity | 13,707.11 | 13,707.11 | 0.02 | FY2023/FY2025 AR balance sheets; Q2FY2026 filing; Reg 54(3) security-cover certificate 30-Jun-2026 | OK |
| 41 | Balance sheet ties, FY2025: assets = liabilities + equity | 14,602.24 | 14,602.24 | 0.02 | FY2023/FY2025 AR balance sheets; Q2FY2026 filing; Reg 54(3) security-cover certificate 30-Jun-2026 | OK |
| 42 | Balance sheet ties, 30-Sep-2025: assets = liabilities + equity | 15,187.10 | 15,187.10 | 0.02 | FY2023/FY2025 AR balance sheets; Q2FY2026 filing; Reg 54(3) security-cover certificate 30-Jun-2026 | OK |
| 43 | Balance sheet ties, Q1FY2027: assets = liabilities + equity | 16,245.83 | 16,245.83 | 0.02 | FY2023/FY2025 AR balance sheets; Q2FY2026 filing; Reg 54(3) security-cover certificate 30-Jun-2026 | OK |
| 44 | Security-cover asset components sum to 16,245.83 (30-Jun-2026) | 16,245.83 | 16,245.83 | 0.02 | Reg 54(3) certificate, 30-Jun-2026 | OK |
| 45 | Total debt / total assets, 30-Jun-2026 | 0.74 | 0.74 | 0.005 | Reg 52(4) disclosure, Q1FY2027 filing | OK |
| 46 | Net worth, 30-Jun-2026 | 4,018.65 | 4,018.65 | 0.01 | Reg 52(4) disclosure, Q1FY2027 filing | OK |
| 47 | Net profit margin, Q1FY2027 | 24.40 | 24.40 | 0.02 | Reg 52(4) disclosure, Q1FY2027 filing | OK |
| 48 | Net interest income, FY2023 (revenue from ops less finance costs) | 582.67 | 583.00 | 0.6 | FY2025 AR six-year highlights table | OK |
| 49 | Net interest income, FY2024 (revenue from ops less finance costs) | 678.95 | 679.00 | 0.6 | FY2025 AR six-year highlights table | OK |
| 50 | Net interest income, FY2025 (revenue from ops less finance costs) | 719.30 | 719.00 | 0.6 | FY2025 AR six-year highlights table | OK |
| 51 | Net interest income, FY2022 (opening-year check of the same convention) | 600.26 | 600.00 | 0.6 | FY2023 AR P&L and FY2025 AR highlights table | OK |
| 52 | Basic EPS, FY2023 | 47.33 | 47.33 | 0.02 | AR statement of profit and loss | OK |
| 53 | Basic EPS, FY2024 | 63.09 | 63.09 | 0.02 | AR statement of profit and loss | OK |
| 54 | Basic EPS, FY2025 | 70.24 | 70.24 | 0.02 | AR statement of profit and loss | OK |
| 55 | Gross loan exposure, FY2025 = net loans + impairment allowance | 14,542.57 | 14,542.57 | 0.02 | FY2025 AR sectoral-exposure table (Note on sector-wise NPA) | OK |
| 56 | Sectoral GNPA %, FY2025 = gross NPA / gross exposure | 3.99 | 3.99 | 0.01 | FY2025 AR sector-wise NPA table | OK |
| 57 | Return on average total assets, FY2025 | 3.10 | 3.10 | 0.05 | FY2025 AR management discussion (Return on Assets chart) | OK |
| 58 | Return on average total assets, FY2025 vs CareEdge published ROTA | 3.10 | 3.11 | 0.02 | CareEdge press release 30-Sep-2025 (peer-agency cross-check only) | OK |
| 59 | Gearing, FY2023 vs AR leverage series | 3.94 | 3.94 | 0.02 | computed from AR balance sheet; AR chart states 4.3 on a NET OWNED FUNDS denominator - see DISCLOSED_DIFFERENCES | OK |
| 60 | FY2026 revenue from operations sums from its five components | 1,795.79 | 1,795.79 | 0.01 | Q1FY2027 filing, audited year-ended 31-Mar-2026 column | OK |
| 61 | FY2026 total expenses sum from components | 1,211.65 | 1,211.65 | 0.01 | Q1FY2027 filing, audited FY2026 column | OK |
| 62 | FY2026 PAT = PBT less tax | 452.77 | 452.77 | 0.01 | Q1FY2027 filing, audited FY2026 column | OK |
| 63 | Q1FY2027 PAT = PBT less tax | 114.15 | 114.15 | 0.01 | Q1FY2027 filing | OK |
| 64 | CRAR FY2025 = Tier I + Tier II | 37.09 | 37.09 | 0.01 | FY2025 AR Note 32.1 | OK |
| 65 | Tier I ratio FY2025 = Tier I capital / RWA | 36.41 | 36.41 | 0.02 | FY2025 AR Note 32.1 | OK |

## 3. Tie-out coverage, measured by mutation (Step 6 / failure mode 39)

`python tools/tieout_mutation.py repco-home-finance-limited` -> **97.5% coverage**.

Coverage is MEASURED, not asserted: the harness perturbs every numeric input and reports which ones no tie-out notices. A suite can be 100%% green and still verify nothing, so the count of passing checks is not the question - the question is which inputs would be caught if they were wrong.

Inputs no tie-out is sensitive to (6):

| Table | Input | Period | Value |
|---|---|---|---|
| BS | Impairment allowance | FY2023 | 471.63 |
| BS | Impairment allowance | FY2024 | 519.04 |
| BS | Impairment allowance | FY2025 | 517.86 |
| BS | Impairment allowance | Q1FY2027 | 0.00 |
| BS | Impairment allowance | col5 | 0.00 |
| PL | PAT | FY2026 | 452.77 |

## 4. Disclosed differences and unverified inputs (carried from the engine)

- **BS** - Impairment allowance
- **BS** - Impairment allowance
- **PL** - PAT
- **BS** - Impairment allowance
- **BS** - Impairment allowance
- **BS** - Impairment allowance
- **THERE IS NO 31-MARCH-2026 BALANCE SHEET IN THE DOCUMENT SET** - This matters more than a footnote. The documents supplied run to the FY2024-25 annual report plus quarterly filings; no FY2025-26 annual report is present, so no audited balance sheet exists for 31-Mar-2026. FY2026 therefore has a profit-and-loss column but NO balance sheet, and compute() omits the year entirely rather than publish leverage, gearing or asset-quality ratios against a balance sheet borrowed from another date. Note the asymmetry this creates: YEARS lists FY2026 while BS_INDEX has no entry for it. Any tool that trusts YEARS and indexes the balance sheet will fail on that period - which is exactly how build_rationale.py crashed on 29-Aug-2026 with KeyError 'FY2026'. The FY2026 balance sheet should be obtained before the next surveillance review.
- **Six inputs are verified by no tie-out, and here they are** - Measured by mutation, not asserted: perturbing each of this engine's 242 inputs shows 236 break at least one tie-out - 97.5% coverage, up from 20.5% before the totals were derived from their components instead of typed. The six that change nothing are the impairment-allowance (ECL) balance in five periods, which is a memo line sitting outside both the asset and liability blocks and has no published figure to tie against without the gross loan book, and FY2026 PAT, which no ratio consumes because that period has no balance sheet (see the entry above). Reproduce with `python tieout_mutation.py repco-home-finance-limited`.
- **AR six-year 'Networth' row vs the balance sheet** - The FY2025 AR highlights table states net worth of 2,061 / 2,321 / 2,677 / 3,314 for FY2022-FY2025, but the audited balance sheets state total equity of 2,235.60 / 2,516.17 / 2,893.95 / 3,313.55. The FY2025 column matches book equity exactly; the three earlier columns are lower by 174.6 / 195.2 / 216.95, i.e. the series changes basis part way through and is most likely net owned funds in the earlier years. This engine uses the AUDITED BALANCE SHEET throughout, so the gearing and return series here are internally consistent and the AR's own leverage chart (4.7 / 4.3 / 4.0 / 3.6) is NOT reproduced in FY2025, where 11,139.09 / 3,313.55 = 3.36x against the chart's 3.6x. Disclosed, not forced - failure mode 32 says a definition that will not reproduce is the wrong definition, and here the published SERIES is the inconsistent one.
- **AR return on equity** - The AR's RoE reproduces on OPENING equity, not average: FY2025 439.44 / 2,893.95 = 15.18% vs published 15.2%; FY2024 394.70 / 2,516.17 = 15.69% vs published 15.8%. ICRA's convention is an average denominator, so this engine publishes return on AVERAGE net worth and the difference is stated rather than reconciled away.
- **Net interest margin** - NIM on average total assets reproduces the AR's figure in FY2023 (4.75% vs 4.8%) and FY2024 (5.18% vs 5.2%) but not FY2025, where this engine computes 5.08% against the AR's 5.2%. No denominator tested - average total assets, average loans, average interest-earning assets - reproduces 5.2% in FY2025 while also reproducing the earlier years, so the AR's FY2025 figure is on an undisclosed basis. Reported at 5.08% with the gap disclosed.
- **Gross NPA has two published bases** - 3.26% (Rs 472.91 crore) EXCLUDING interest accrued and EIR adjustments, and 3.99% (Rs 580.38 crore) on the RBI sectoral-exposure format INCLUDING them, both for FY2025 and both in the same annual report. At 30-Jun-2026 the same split appears as 2.67% against 3.33%. Both are reported here with the basis named; neither is a correction of the other (failure mode 34 - establish what a number measures before publishing it).

## 6. OUTSTANDING - the sections that require the documents to be read

These are **not** in this document and have **not** been done. They are named here so the gap is visible rather than silent.

- [ ] **Document Read Log (Step 1b)** - one row per uploaded file: what it is, the key facts it contributes, the material items it flags. A file not in the log has not been read.
- [ ] **Qualitative fact register (Step 7)** - every non-computed claim traced to a document location, and corroborated against a second source where one exists (response protocol 2(e)).
- [ ] **Materiality sweep (Step 8)** - the untouched sections of every file walked for credit-relevant items, each tagged material/immaterial against the R13 test with a written include/exclude decision.
- [ ] **Methodology Compliance Map (Step 10)** - one row per rating factor as the methodology names it, scored with the company's actual numbers against the indicative band, every notching criterion quoted verbatim.
- [ ] **Liquidity computation (Step 11)** - sources-vs-claims arithmetic over ~12 months; the descriptor is the conclusion of that arithmetic, never an adjective.

## 7. Rating view as delivered (Step 13-15, from this case's own rationale)

Source: `Repco Home Finance Limited_24 Aug 2026_Rating Rationale.md`

> August 24, 2026

Sections present in the delivered rationale:

- Summary of rating action
- Rationale
- Key rating drivers and their description
- Credit strengths
- Credit challenges
- Environmental and social risks
- Liquidity position: Adequate
- Rating sensitivities
- Analytical approach
- About the company
- Key financial indicators (audited; standalone)
- Status of non-cooperation with previous CRA: Not applicable
- Any other information
- Rating history for past three years
- Complexity level of the rated instruments
- Annexure I: Instrument details
- Annexure II: List of entities considered for consolidated analysis

The rating view itself lives in that document; it is referenced here rather than restated, so the two cannot drift apart.

---

*Reproduce this workpaper: `python tools/make_workpaper.py repco-home-finance-limited --force`. Re-verify the case: `python tools/delivery_audit.py repco-home-finance-limited`.*
