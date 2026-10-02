# Ratio Workpaper - APTUS VALUE HOUSING FINANCE INDIA LIMITED | CareEdge

*Generated 04 Sep 2026 by `tools/make_workpaper.py` from this case's own `compute_ratios.py`.*

> **What this document is.** The EXTRACTION AND VERIFICATION record for this case: the computed ratio suite, every tie-out with its source, the measured coverage of those tie-outs, and the inputs nothing checks. Every figure below is produced by the engine, not retyped - re-run `python Companies/aptus-value-housing-finance-india-limited/compute_ratios.py` to reproduce it.
>
> **What this document is NOT.** It does not contain the Document Read Log, the qualitative fact register, the materiality sweep or the Methodology Compliance Map. Those require the documents to have been read and are listed by name in section 6 as outstanding. They are not generated here because a fabricated Read Log reads as diligence and stops anyone looking - which is failure mode 20, and the reason failure mode 37 exists.

## 1. Computed ratio suite (Step 6)

Basis: periods as the engine declares them. Values as `compute()` returns them.

| Metric | FY2025 | FY2026 |
|---|---|---|
| Interest income | 1,669.58 | 1,943.80 |
| Fees and commission income | 56.85 | 58.65 |
| Net gain on fair value changes | 7.67 | 17.36 |
| Net gain on derecognition (assignment) | 16.31 | 172.44 |
| Total income | 1,798.40 | 2,245.48 |
| Finance costs | 540.51 | 648.45 |
| Impairment on financial instruments | 28.32 | 61.51 |
| Total expenses | 823.56 | 1,034.33 |
| Profit before tax | 974.84 | 1,211.16 |
| Profit after tax | 751.25 | 942.94 |
| Debt securities | 1,292.29 | 1,350.49 |
| Borrowings (other than debt securities) | 5,554.55 | 6,523.18 |
| TOTAL DEBT | 6,846.84 | 7,873.67 |
| Lease liabilities | 26.24 | 30.10 |
| Loans - on book | 10,630.27 | 11,929.52 |
| Cash and cash equivalents | 302.59 | 563.32 |
| Bank balances other than above | 121.16 | 27.42 |
| Total assets | 11,243.41 | 13,047.66 |
| GNPA % - AR, consolidated | 1.19 | 1.52 |
| NNPA % - AR, consolidated | 0.89 | 1.15 |
| Gross stage 3 % - CareEdge published | 1.18 | 1.45 |
| Tangible net worth | 4,293.58 | 5,058.67 |
| AUM | 10,865.00 | 13,107.00 |
| On-book gearing (x) | 1.59 | 1.56 |
| AUM / tangible net worth (x) | 2.53 | 2.59 |
| Net interest income | 1,129.07 | 1,295.35 |
| PAT margin (%) | 41.77 | 41.99 |
| Cost-to-income (%) | 20.25 | 20.31 |
| Capital adequacy CRAR (%) | 71.00 | 71.00 |
| NIM on average AUM (%) | - | 10.81 |
| Credit cost on avg AUM (%) | - | 0.51 |
| Return on managed assets ROMA (%) | - | 7.87 |
| Return on total assets (%) | - | 7.76 |
| Return on net worth (%) | - | 20.16 |

## 2. Tie-outs (Step 6 gate) - 16/16 reconcile

Each row reconciles a figure this engine DERIVES against one printed somewhere else. A check that compares a value with itself cannot fail and is not a check (failure mode 39).

| # | Check | Computed | Disclosed | Tol | Source | |
|---|---|---|---|---|---|---|
| 1 | FY2026 TNW reproduces published 5,059 | 5,058.67 | 5,059.00 | 1 | CareEdge published rationale tangible net worth vs the AR equity/intangibles/DTA build-up | OK |
| 2 | FY2026 total income reproduces published 2,245 | 2,245.48 | 2,245.00 | 1 | CareEdge published rationale Brief Financials vs audited P&L | OK |
| 3 | FY2025 total income reproduces published 1,798 | 1,798.40 | 1,798.00 | 1 | CareEdge published rationale Brief Financials vs audited P&L | OK |
| 4 | FY2026 PAT reproduces published 943 | 942.94 | 943.00 | 1 | CareEdge published rationale Brief Financials vs audited P&L | OK |
| 5 | FY2025 PAT reproduces published 751 | 751.25 | 751.00 | 1 | CareEdge published rationale Brief Financials vs audited P&L | OK |
| 6 | FY2026 on-book gearing reproduces published 1.56 | 1.56 | 1.56 | 0.02 | CareEdge published rationale gearing vs audited total debt over derived TNW | OK |
| 7 | FY2025 on-book gearing reproduces published 1.60 | 1.59 | 1.60 | 0.02 | CareEdge published rationale gearing vs audited total debt over derived TNW | OK |
| 8 | FY2025 AUM/TNW reproduces published 2.53 | 2.53 | 2.53 | 0.02 | CareEdge published rationale AUM/TNW row | OK |
| 9 | FY2026 AUM/TNW vs published 2.58 | 2.59 | 2.58 | 0.02 | CareEdge published rationale AUM/TNW row | OK |
| 10 | FY2026 ROMA vs the AR's own RoA of 7.9 | 7.87 | 7.90 | 0.1 | FY2025-26 annual report - the company's own stated return on assets | OK |
| 11 | FY2026 RONW vs the AR's own RoE of 20.1 | 20.16 | 20.10 | 0.1 | FY2025-26 annual report - the company's own stated return on equity | OK |
| 12 | LINE INTEGRITY bank facilities = 2,100.00 | 2,100.00 | 2,100.00 | 0.02 | CareEdge published rationale rated-amount table - component lines vs their printed total (failure mode 12) | OK |
| 13 | LINE INTEGRITY NCDs = 1,145.00 | 1,145.00 | 1,145.00 | 0.02 | CareEdge published rationale rated-amount table - component lines vs their printed total (failure mode 12) | OK |
| 14 | FY2026 total debt = debt securities + other borrowings | 7,873.67 | 7,873.67 | 0.02 | audited balance sheet - printed total-debt row | OK |
| 15 | FY2026 AUM split sums to the AUM | 13,107.00 | 13,107.00 | 1 | AR segment disclosure - HFC and NBFC book split vs consolidated AUM | OK |
| 16 | FY2026 PAT = PBT less tax implied | 942.94 | 942.94 | 0.02 | audited P&L - PBT less the tax charge vs the printed PAT row | OK |

## 3. Tie-out coverage, measured by mutation (Step 6 / failure mode 39)

`python tools/tieout_mutation.py aptus-value-housing-finance-india-limited` -> **27.1% coverage**.

Coverage is MEASURED, not asserted: the harness perturbs every numeric input and reports which ones no tie-out notices. A suite can be 100%% green and still verify nothing, so the count of passing checks is not the question - the question is which inputs would be caught if they were wrong.

Inputs no tie-out is sensitive to (35):

| Table | Input | Period | Value |
|---|---|---|---|
| ASSET_QUALITY | GNPA % - AR, consolidated | FY2025 | 1.19 |
| ASSET_QUALITY | GNPA % - AR, consolidated | FY2026 | 1.52 |
| ASSET_QUALITY | NNPA % - AR, consolidated | FY2025 | 0.89 |
| ASSET_QUALITY | NNPA % - AR, consolidated | FY2026 | 1.15 |
| ASSET_QUALITY | Gross stage 3 % - CareEdge published | FY2025 | 1.18 |
| ASSET_QUALITY | Gross stage 3 % - CareEdge published | FY2026 | 1.45 |
| BS | Debt securities | FY2025 | 1292.29 |
| BS | Borrowings (other than debt securities) | FY2025 | 5554.55 |
| BS | Lease liabilities | FY2025 | 26.24 |
| BS | Lease liabilities | FY2026 | 30.10 |
| BS | Loans - on book | FY2025 | 10630.27 |
| BS | Loans - on book | FY2026 | 11929.52 |
| BS | Cash and cash equivalents | FY2025 | 302.59 |
| BS | Cash and cash equivalents | FY2026 | 563.32 |
| BS | Bank balances other than above | FY2025 | 121.16 |
| BS | Bank balances other than above | FY2026 | 27.42 |
| BS | Total assets | FY2025 | 11243.41 |
| BS | Total assets | FY2026 | 13047.66 |
| NW | less: intangible assets | FY2025 | 1.01 |
| NW | less: deferred tax assets | FY2025 | 22.06 |
| PL | Interest income | FY2025 | 1669.58 |
| PL | Interest income | FY2026 | 1943.80 |
| PL | Fees and commission income | FY2025 | 56.85 |
| PL | Fees and commission income | FY2026 | 58.65 |
| PL | Net gain on fair value changes | FY2025 | 7.67 |
| PL | Net gain on fair value changes | FY2026 | 17.36 |
| PL | Net gain on derecognition (assignment) | FY2025 | 16.31 |
| PL | Net gain on derecognition (assignment) | FY2026 | 172.44 |
| PL | Finance costs | FY2025 | 540.51 |
| PL | Finance costs | FY2026 | 648.45 |
| PL | Impairment on financial instruments | FY2025 | 28.32 |
| PL | Impairment on financial instruments | FY2026 | 61.51 |
| PL | Total expenses | FY2025 | 823.56 |
| PL | Total expenses | FY2026 | 1034.33 |
| PL | Profit before tax | FY2025 | 974.84 |

## 4. Disclosed differences and unverified inputs (carried from the engine)

- **Asset-quality percentages are not independently reproducible** - GNPA/NNPA and gross stage 3 are taken as printed from the AR and the CareEdge rationale. The engine holds no stage-wise gross carrying amounts or provision balances to rebuild them from, so they are traceable but not reproducible here.
- **CRAR, LCR, cost of borrowings and the liquidity buffer are single-sourced** - CRAR 71%, the standalone LCR/PCR block, COST_OF_BORROWINGS and LIQUIDITY come from one disclosure each with no second source in the folder to reconcile against.
- **The Q1FY2027 block is unchecked** - Q1 income and PAT support the trend narrative only; no audited quarterly statement is in the case folder.
- **The FY2026 tax charge is a single literal** - The PAT waterfall uses a tax charge of 268.22 read from the P&L. It is not carried as a table input, so no mutation can reach it - the check proves the PBT/PAT relationship, not the tax line itself.

## 6. OUTSTANDING - the sections that require the documents to be read

These are **not** in this document and have **not** been done. They are named here so the gap is visible rather than silent.

- [ ] **Document Read Log (Step 1b)** - one row per uploaded file: what it is, the key facts it contributes, the material items it flags. A file not in the log has not been read.
- [ ] **Qualitative fact register (Step 7)** - every non-computed claim traced to a document location, and corroborated against a second source where one exists (response protocol 2(e)).
- [ ] **Materiality sweep (Step 8)** - the untouched sections of every file walked for credit-relevant items, each tagged material/immaterial against the R13 test with a written include/exclude decision.
- [ ] **Methodology Compliance Map (Step 10)** - one row per rating factor as the methodology names it, scored with the company's actual numbers against the indicative band, every notching criterion quoted verbatim.
- [ ] **Liquidity computation (Step 11)** - sources-vs-claims arithmetic over ~12 months; the descriptor is the conclusion of that arithmetic, never an adjective.

## 7. Rating view as delivered (Step 13-15, from this case's own rationale)

Source: `Aptus Value Housing Finance India Limited_21 Aug 2026_CARE_Rating Rationale.md`

> > **This is not an official CRA publication.** It is an independent analytical exercise prepared in CareEdge Ratings' published format, using the issuer's own disclosures and CareEdge's published criteria. It is not a CARE Ratings Limited rating, carries no regulatory standing, and must not be represented as one.

Sections present in the delivered rationale:

- **Aptus Value Housing Finance India Limited**
- **Summary of rating action**
- **Rationale and key rating drivers**
- **Rating sensitivities: Factors likely to lead to rating actions**
- **Positive factors**
- **Negative factors**
- **Analytical approach:** Consolidated
- **Outlook: Stable**
- **Detailed description of key rating drivers:**
- **Key strengths**
- **Key weaknesses**
- **Liquidity: Adequate**
- **Environment, social, and governance (ESG) risks**
- **Applicable criteria**
- **About the company and industry**
- Industry classification
- **Brief Financials (₹ crore)** — Consolidated
- **Annexure I — Details of instruments / facilities**
- **Annexure II — Rating history**
- **Annexure III — Basis and evidence notes**

The rating view itself lives in that document; it is referenced here rather than restated, so the two cannot drift apart.

---

*Reproduce this workpaper: `python tools/make_workpaper.py aptus-value-housing-finance-india-limited --force`. Re-verify the case: `python tools/delivery_audit.py aptus-value-housing-finance-india-limited`.*
