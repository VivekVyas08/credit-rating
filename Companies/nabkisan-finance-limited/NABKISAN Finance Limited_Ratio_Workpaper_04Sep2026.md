# Ratio Workpaper - NABKISAN Finance Limited | CareEdge

*Generated 04 Sep 2026 by `tools/make_workpaper.py` from this case's own `compute_ratios.py`.*

> **What this document is.** The EXTRACTION AND VERIFICATION record for this case: the computed ratio suite, every tie-out with its source, the measured coverage of those tie-outs, and the inputs nothing checks. Every figure below is produced by the engine, not retyped - re-run `python Companies/nabkisan-finance-limited/compute_ratios.py` to reproduce it.
>
> **What this document is NOT.** It does not contain the Document Read Log, the qualitative fact register, the materiality sweep or the Methodology Compliance Map. Those require the documents to have been read and are listed by name in section 6 as outstanding. They are not generated here because a fabricated Read Log reads as diligence and stops anyone looking - which is failure mode 20, and the reason failure mode 37 exists.

## 1. Computed ratio suite (Step 6)

Basis: periods as the engine declares them. Values as `compute()` returns them.

| Metric | FY2025 | FY2026 | Q1FY27 |
|---|---|---|---|
| Total income | 472.00 | 545.00 | 173.00 |
| Profit after tax | 126.00 | 132.00 | 31.00 |
| Assets under management (AUM) | 5,128.00 | 7,066.00 | 6,852.00 |
| Tangible net worth (TNW) | 881.00 | 1,011.00 | 1,042.00 |
| On-book gearing (x) | 4.92 | 6.07 | 5.53 |
| AUM / TNW (x) | 5.82 | 6.99 | 6.57 |
| Gross stage III (%) | 0.86 | 0.85 | 0.94 |
| Net stage III (%) | 0.25 | 0.27 | 0.37 |
| Return on total assets (%) | 2.57 | 2.09 | 1.74 |
| Return on net worth (%) | 15.34 | 13.90 | 11.95 |
| Capital adequacy ratio (%) | 18.11 | 22.26 | 22.80 |
| Opex / avg total assets (%) | 0.52 | 0.45 | - |
| Credit cost (%) | -0.04 | 0.05 | - |
| Interest income | 470.50 | 540.74 | - |
| Finance costs | 288.05 | 333.55 | - |
| Impairment (write-back) | -15.73 | -2.50 | - |
| Profit before tax | 160.69 | 179.81 | - |
| Loans (net) | 4,829.59 | 6,571.24 | - |
| Total assets | 5,330.49 | 7,238.23 | - |
| Borrowings | 4,330.04 | 6,137.15 | - |
| Total equity | 888.09 | 1,016.03 | - |
| Tier I capital | 880.76 | 1,011.42 | - |
| Tier II capital | 25.39 | 517.22 | - |
| Risk weighted assets | 5,000.92 | 6,866.29 | - |
| Net interest income | 182.45 | 207.19 | - |
| PBT normalised (ex write-back) | 144.96 | 177.31 | - |

## 2. Tie-outs (Step 6 gate) - 11/11 reconcile

Each row reconciles a figure this engine DERIVES against one printed somewhere else. A check that compares a value with itself cannot fail and is not a check (failure mode 39).

| # | Check | Computed | Disclosed | Tol | Source | |
|---|---|---|---|---|---|---|
| 1 | FY2025 CRAR from Tier I + Tier II / RWA | 18.12 | 18.11 | 0.06 | FY2026 audited financials capital note vs CareEdge published rationale 19-Aug-2026 | OK |
| 2 | FY2025 AUM / TNW reproduces the published ratio | 5.82 | 5.82 | 0.06 | CareEdge published rationale 19-Aug-2026 - AUM and TNW rows vs the published ratio row | OK |
| 3 | FY2025 gearing = borrowings / TNW | 4.91 | 4.92 | 0.06 | FY2026 audited financials balance sheet borrowings vs CareEdge published rationale 19-Aug-2026 gearing row | OK |
| 4 | FY2026 CRAR from Tier I + Tier II / RWA | 22.26 | 22.26 | 0.06 | FY2026 audited financials capital note vs CareEdge published rationale 19-Aug-2026 | OK |
| 5 | FY2026 AUM / TNW reproduces the published ratio | 6.99 | 6.99 | 0.06 | CareEdge published rationale 19-Aug-2026 - AUM and TNW rows vs the published ratio row | OK |
| 6 | FY2026 gearing = borrowings / TNW | 6.07 | 6.07 | 0.06 | FY2026 audited financials balance sheet borrowings vs CareEdge published rationale 19-Aug-2026 gearing row | OK |
| 7 | FY2026 TNW sits BELOW total equity (DTA/intangibles deducted) | 1.00 | 1.00 | 0.5 | CareEdge published rationale 19-Aug-2026 TNW vs FY2026 audited financials total equity | OK |
| 8 | Tier II movement equals the rated bond size | 491.83 | 500.00 | 10 | FY2026 audited financials Tier II capital movement vs the rated instrument INE165U08016 | OK |
| 9 | FY2026 PBT = total income less total expenses | 179.81 | 179.81 | 0.06 | FY2026 audited financials P&L - printed income and expense totals | OK |
| 10 | FY2026 RoTA = PAT / average total assets | 2.10 | 2.09 | 0.15 | CareEdge published rationale 19-Aug-2026 PAT over FY2026 audited financials balance-sheet total assets, average basis | OK |
| 11 | FY2026 RoNW = PAT / average tangible net worth | 13.95 | 13.90 | 0.15 | CareEdge published rationale 19-Aug-2026 PAT over average TNW - the NBFC convention, not closing equity | OK |

## 3. Tie-out coverage, measured by mutation (Step 6 / failure mode 39)

`python tools/tieout_mutation.py nabkisan-finance-limited` -> **35.6% coverage**.

Coverage is MEASURED, not asserted: the harness perturbs every numeric input and reports which ones no tie-out notices. A suite can be 100%% green and still verify nothing, so the count of passing checks is not the question - the question is which inputs would be caught if they were wrong.

Inputs no tie-out is sensitive to (38):

| Table | Input | Period | Value |
|---|---|---|---|
| AUDITED | Interest income | FY2025 | 470.50 |
| AUDITED | Interest income | FY2026 | 540.74 |
| AUDITED | Finance costs | FY2025 | 288.05 |
| AUDITED | Finance costs | FY2026 | 333.55 |
| AUDITED | Impairment (write-back) | FY2025 | -15.73 |
| AUDITED | Impairment (write-back) | FY2026 | -2.50 |
| AUDITED | Profit before tax | FY2025 | 160.69 |
| AUDITED | Loans (net) | FY2025 | 4829.59 |
| AUDITED | Loans (net) | FY2026 | 6571.24 |
| AUDITED | Total assets | FY2025 | 5330.49 |
| AUDITED | Total assets | FY2026 | 7238.23 |
| AUDITED | Total equity | FY2025 | 888.09 |
| AUDITED | Total equity | FY2026 | 1016.03 |
| AUDITED | Tier II capital | FY2025 | 25.39 |
| M | Total income | FY2025 | 472.00 |
| M | Total income | FY2026 | 545.00 |
| M | Total income | Q1FY27 | 173.00 |
| M | Profit after tax | FY2025 | 126.00 |
| M | Profit after tax | Q1FY27 | 31.00 |
| M | Assets under management (AUM) | Q1FY27 | 6852.00 |
| M | Tangible net worth (TNW) | Q1FY27 | 1042.00 |
| M | On-book gearing (x) | Q1FY27 | 5.53 |
| M | AUM / TNW (x) | Q1FY27 | 6.57 |
| M | Gross stage III (%) | FY2025 | 0.86 |
| M | Gross stage III (%) | FY2026 | 0.85 |
| M | Gross stage III (%) | Q1FY27 | 0.94 |
| M | Net stage III (%) | FY2025 | 0.25 |
| M | Net stage III (%) | FY2026 | 0.27 |
| M | Net stage III (%) | Q1FY27 | 0.37 |
| M | Return on total assets (%) | FY2025 | 2.57 |
| M | Return on total assets (%) | Q1FY27 | 1.74 |
| M | Return on net worth (%) | FY2025 | 15.34 |
| M | Return on net worth (%) | Q1FY27 | 11.95 |
| M | Capital adequacy ratio (%) | Q1FY27 | 22.80 |
| M | Opex / avg total assets (%) | FY2025 | 0.52 |
| M | Opex / avg total assets (%) | FY2026 | 0.45 |
| M | Credit cost (%) | FY2025 | -0.04 |
| M | Credit cost (%) | FY2026 | 0.05 |

## 4. Disclosed differences and unverified inputs (carried from the engine)

- **Q1FY27 column is unchecked** - The Q1FY27 figures are CareEdge-published only; no audited quarterly statement is in the case folder, so nothing independent exists to reconcile them against. They inform the trend narrative and feed no rated conclusion.
- **Portfolio-mix and asset-quality percentages are single-sourced** - Gross/net stage III, opex/ATA, credit cost and the PORTFOLIO split come from the published rationale alone. The audited financials carry the ECL movement tables behind them but not these ratios as printed, so they are traceable but not independently reproducible here.

## 5. Extraction source register (Step 5)

Where the engine annotates an input with its origin, that annotation is reproduced verbatim. This is a provenance record, not a corroboration record - traced is not verified (response protocol 2(e)).

| Table | Line item | Source as the engine records it |
|---|---|---|
| AUDITED | Interest income | FY2026 audited financials P&L L~638 |
| AUDITED | Finance costs | FY2026 audited financials P&L L644 |
| AUDITED | Impairment (write-back) | FY2026 audited financials P&L L645 - a CREDIT, not a charge |
| AUDITED | Profit before tax | FY2026 audited financials P&L L~651 |
| AUDITED | Loans (net) | FY2026 audited financials BS L476 |
| AUDITED | Total assets | FY2026 audited financials BS L~489 |
| AUDITED | Borrowings | FY2026 audited financials BS L~493 |
| AUDITED | Total equity | FY2026 audited financials share capital + other equity |
| AUDITED | Tier I capital | FY2026 audited financials L~2665 |
| AUDITED | Tier II capital | FY2026 audited financials L~2666 - the Rs 492cr jump = the bond |
| AUDITED | Risk weighted assets | FY2026 audited financials L~2668 |
| M | Total income | CareEdge published rationale 19-Aug-2026 Brief Financials |
| M | Profit after tax | CareEdge published rationale 19-Aug-2026 |
| M | Assets under management (AUM) | CareEdge published rationale 19-Aug-2026 - THE NBFC scale metric |
| M | Tangible net worth (TNW) | CareEdge published rationale 19-Aug-2026 - equity less intangibles & DTA |
| M | On-book gearing (x) | CareEdge published rationale 19-Aug-2026 |
| M | AUM / TNW (x) | CareEdge published rationale 19-Aug-2026 |
| M | Gross stage III (%) | CareEdge published rationale 19-Aug-2026 - v1 wrongly said 'not located' |
| M | Net stage III (%) | CareEdge published rationale 19-Aug-2026 |
| M | Return on total assets (%) | CareEdge published rationale 19-Aug-2026 - Q1FY27 annualised |
| M | Return on net worth (%) | CareEdge published rationale 19-Aug-2026 |
| M | Capital adequacy ratio (%) | CareEdge published rationale 19-Aug-2026 |
| M | Opex / avg total assets (%) | CareEdge published rationale 19-Aug-2026 - NBFC metric, NOT cost-to-income |
| M | Credit cost (%) | CareEdge published rationale 19-Aug-2026 - negative = ECL write-back |

## 6. OUTSTANDING - the sections that require the documents to be read

These are **not** in this document and have **not** been done. They are named here so the gap is visible rather than silent.

- [ ] **Document Read Log (Step 1b)** - one row per uploaded file: what it is, the key facts it contributes, the material items it flags. A file not in the log has not been read.
- [ ] **Qualitative fact register (Step 7)** - every non-computed claim traced to a document location, and corroborated against a second source where one exists (response protocol 2(e)).
- [ ] **Materiality sweep (Step 8)** - the untouched sections of every file walked for credit-relevant items, each tagged material/immaterial against the R13 test with a written include/exclude decision.
- [ ] **Methodology Compliance Map (Step 10)** - one row per rating factor as the methodology names it, scored with the company's actual numbers against the indicative band, every notching criterion quoted verbatim.
- [ ] **Liquidity computation (Step 11)** - sources-vs-claims arithmetic over ~12 months; the descriptor is the conclusion of that arithmetic, never an adjective.

## 7. Rating view as delivered (Step 13-15, from this case's own rationale)

Source: `NABKISAN Finance Limited_19 Aug 2026_CareEdge_Rating Rationale_v2.md`

> > **This is not an official CareEdge Ratings publication.** It is an internal analytical exercise

Sections present in the delivered rationale:

- **NABKISAN Finance Limited**
- **Rationale and key rating drivers**
- **Rating sensitivities: Factors likely to lead to rating actions**
- **Positive factors**
- **Negative factors**
- **Analytical approach:** Standalone
- **Outlook: Stable**
- **Detailed description of key rating drivers**
- **Key strengths**
- **Key weaknesses**
- **Liquidity: Strong**
- **Environment, social, and governance (ESG) risks**
- **Applicable criteria**
- **About the company and industry**
- **Brief Financials (₹ crore)**
- **Annexure I — Details of instruments/facilities**
- **Annexure II — Rating history for last three years**
- **Annexure III — Basis and evidence notes**

The rating view itself lives in that document; it is referenced here rather than restated, so the two cannot drift apart.

---

*Reproduce this workpaper: `python tools/make_workpaper.py nabkisan-finance-limited --force`. Re-verify the case: `python tools/delivery_audit.py nabkisan-finance-limited`.*
