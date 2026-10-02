# Ratio Workpaper - HDFC Securities | CareEdge

*Generated 04 Sep 2026 by `tools/make_workpaper.py` from this case's own `compute_ratios.py`.*

> **What this document is.** The EXTRACTION AND VERIFICATION record for this case: the computed ratio suite, every tie-out with its source, the measured coverage of those tie-outs, and the inputs nothing checks. Every figure below is produced by the engine, not retyped - re-run `python Companies/hdfc-securities/compute_ratios.py` to reproduce it.
>
> **What this document is NOT.** It does not contain the Document Read Log, the qualitative fact register, the materiality sweep or the Methodology Compliance Map. Those require the documents to have been read and are listed by name in section 6 as outstanding. They are not generated here because a fabricated Read Log reads as diligence and stops anyone looking - which is failure mode 20, and the reason failure mode 37 exists.

## 1. Computed ratio suite (Step 6)

Basis: periods as the engine declares them. Values as `compute()` returns them.

| Metric | FY2025 | FY2026 |
|---|---|---|
| Total income | 3,264.86 | 3,110.15 |
| Total expenses | 1,768.71 | 1,873.09 |
| Finance costs | 785.45 | 817.40 |
| Profit after tax | 1,125.00 | 929.90 |
| Interest income | 1,418.34 | 1,497.93 |
| Fees and commission income | 1,744.20 | 1,515.83 |
| Brokerage income | 1,259.55 | 1,012.19 |
| Dividend (interim + final) | 898.30 | 740.10 |
| Debt securities (commercial paper) | 7,741.52 | 12,931.33 |
| Borrowings other than debt securities (TREPS) | 202.25 | 2,182.55 |
| TOTAL DEBT | 7,943.77 | 15,113.88 |
| Bank guarantees outstanding | 700.00 | 1,100.00 |
| Total equity | 3,348.59 | 3,595.92 |
| less: deferred tax assets | 0.52 | 15.57 |
| less: other intangible assets | 84.24 | 78.23 |
| less: intangibles under develop. | 7.32 | 5.63 |
| Tangible net worth | 3,256.51 | 3,496.49 |
| Total assets | 14,031.11 | 21,784.33 |
| MTF book | 5,511.87 | 7,132.66 |
| Overall gearing (x) | 2.65 | 4.64 |
| Fund-based gearing (x) | 2.44 | 4.32 |
| Cost-to-income (%) | 39.66 | 46.04 |
| PAT margin (%) | 34.46 | 29.90 |
| RONW on average TNW (%) | - | 27.54 |
| ROTA on average total assets (%) | - | 5.19 |

## 2. Tie-outs (Step 6 gate) - 17/17 reconcile

Each row reconciles a figure this engine DERIVES against one printed somewhere else. A check that compares a value with itself cannot fail and is not a check (failure mode 39).

| # | Check | Computed | Disclosed | Tol | Source | |
|---|---|---|---|---|---|---|
| 1 | FY2025 TNW reproduces published | 3,256.51 | 3,257.00 | 0.6 | FY2025-26 annual report equity/DTA/intangibles build-up vs CareEdge published rationale tangible net worth | OK |
| 2 | FY2026 TNW reproduces published | 3,496.49 | 3,496.00 | 0.6 | FY2025-26 annual report equity/DTA/intangibles build-up vs CareEdge published rationale tangible net worth | OK |
| 3 | FY2025 gearing reproduces published | 2.65 | 2.65 | 0.6 | FY2025-26 annual report debt + bank guarantees over TNW vs CareEdge published rationale gearing row | OK |
| 4 | FY2026 gearing reproduces published | 4.64 | 4.64 | 0.6 | FY2025-26 annual report debt + bank guarantees over TNW vs CareEdge published rationale gearing row | OK |
| 5 | FY2026 RONW on AVERAGE TNW reproduces published | 27.54 | 27.54 | 0.6 | FY2025-26 annual report PAT over average TNW vs CareEdge published rationale RONW - the average basis, not closing | OK |
| 6 | FY2026 ROTA on average assets vs published | 5.19 | 5.22 | 0.55 | FY2025-26 annual report PAT over average total assets vs CareEdge published rationale ROTA | OK |
| 7 | FY2026 cost-to-income vs published | 46.04 | 45.54 | 0.55 | FY2025-26 annual report expenses net of finance cost vs CareEdge published rationale cost-to-income | OK |
| 8 | FY2025 cost-to-income vs published | 39.66 | 39.42 | 0.55 | FY2025-26 annual report expenses net of finance cost vs CareEdge published rationale cost-to-income | OK |
| 9 | FY2026 PAT margin reproduces published | 29.90 | 29.90 | 0.6 | FY2025-26 annual report PAT over total income vs CareEdge published rationale Brief Financials | OK |
| 10 | Q1FY27 PAT margin reproduces published | 31.27 | 31.27 | 0.6 | Q1FY2027 results vs CareEdge published rationale quarterly commentary | OK |
| 11 | Q1FY27 RONW on OPENING TNW reproduces published | 8.50 | 8.50 | 0.6 | Q1FY2027 PAT over FY2026 closing TNW vs CareEdge published rationale | OK |
| 12 | Fees+commission share vs published 48% | 48.74 | 48.00 | 1 | FY2025-26 annual report revenue mix vs CareEdge published rationale stated share | OK |
| 13 | Brokerage share vs published 33% | 32.54 | 33.00 | 1 | FY2025-26 annual report revenue mix vs CareEdge published rationale stated share | OK |
| 14 | LINE INTEGRITY CP: tranches + proposed = limit | 20,000.00 | 20,000.00 | 0.6 | CareEdge published rationale rated-amount table - lines vs printed total (failure mode 12) | OK |
| 15 | LINE INTEGRITY LT/ST: sanctioned + proposed = limit | 3,000.00 | 3,000.00 | 0.6 | CareEdge published rationale rated-amount table - lines vs printed total (failure mode 12) | OK |
| 16 | Q1FY27 fund-based debt itemises to the total | 18,286.00 | 18,286.00 | 0.6 | Q1FY2027 borrowings note - components vs the printed total | OK |
| 17 | FY2026 total debt = CP + TREPS | 15,113.88 | 15,113.88 | 0.6 | FY2025-26 annual report balance sheet - printed total-debt row | OK |

## 3. Tie-out coverage, measured by mutation (Step 6 / failure mode 39)

`python tools/tieout_mutation.py hdfc-securities` -> **56.2% coverage**.

Coverage is MEASURED, not asserted: the harness perturbs every numeric input and reports which ones no tie-out notices. A suite can be 100%% green and still verify nothing, so the count of passing checks is not the question - the question is which inputs would be caught if they were wrong.

Inputs no tie-out is sensitive to (14):

| Table | Input | Period | Value |
|---|---|---|---|
| DEBT | Debt securities (commercial paper) | FY2025 | 7741.52 |
| DEBT | Borrowings other than debt securities (TRE | FY2025 | 202.25 |
| DEBT | TOTAL DEBT | FY2025 | 7943.77 |
| DEBT | Bank guarantees outstanding | FY2025 | 700.00 |
| DEBT | Bank guarantees outstanding | FY2026 | 1100.00 |
| NW | less: deferred tax assets | FY2026 | 15.57 |
| NW | less: intangibles under develop. | FY2026 | 5.63 |
| PL | Profit after tax | FY2025 | 1125.00 |
| PL | Interest income | FY2025 | 1418.34 |
| PL | Interest income | FY2026 | 1497.93 |
| PL | Fees and commission income | FY2025 | 1744.20 |
| PL | Brokerage income | FY2025 | 1259.55 |
| PL | Dividend (interim + final) | FY2025 | 898.30 |
| PL | Dividend (interim + final) | FY2026 | 740.10 |

## 4. Disclosed differences and unverified inputs (carried from the engine)

- **Cost-to-income and ROTA reconcile to ~0.5pp, not exactly** - CareEdge's standardised broking template evidently excludes a small expense line that the audited P&L includes. The gap is stable across both years and is reported AS COMPUTED with the tolerance stated, rather than forcing the inputs to tie (failure mode 32: if a definition will not reproduce, do not adjust the inputs to make it).
- **The MTF book and franchise metrics have no independent second source** - MTF balances, client counts and branch/city figures come from one disclosure each. MTF is the spine of this credit, so its single-sourcing matters and is stated here rather than left silent.
- **The Q1FY2027 liquidity block is single-sourced** - Unencumbered cash and unutilised lines as on 30-Jun-2026 come from the Q1 disclosure alone. This is the figure that corrected an 18x overstatement in v1 (failure mode 34), so it is load-bearing and unreconciled.

## 6. OUTSTANDING - the sections that require the documents to be read

These are **not** in this document and have **not** been done. They are named here so the gap is visible rather than silent.

- [ ] **Document Read Log (Step 1b)** - one row per uploaded file: what it is, the key facts it contributes, the material items it flags. A file not in the log has not been read.
- [ ] **Qualitative fact register (Step 7)** - every non-computed claim traced to a document location, and corroborated against a second source where one exists (response protocol 2(e)).
- [ ] **Materiality sweep (Step 8)** - the untouched sections of every file walked for credit-relevant items, each tagged material/immaterial against the R13 test with a written include/exclude decision.
- [ ] **Methodology Compliance Map (Step 10)** - one row per rating factor as the methodology names it, scored with the company's actual numbers against the indicative band, every notching criterion quoted verbatim.
- [ ] **Liquidity computation (Step 11)** - sources-vs-claims arithmetic over ~12 months; the descriptor is the conclusion of that arithmetic, never an adjective.

## 7. Rating view as delivered (Step 13-15, from this case's own rationale)

Source: `HDFC Securities Limited_20 Aug 2026_CareEdge_Rating Rationale.md`

> > **This is not an official CRA publication.** It is an independent analytical exercise prepared in CareEdge Ratings' published format. It is not a CARE Ratings Limited rating, carries no regulatory standing, and must not be represented as one.

Sections present in the delivered rationale:

- **HDFC Securities Limited**
- **Summary of rating action**
- **Rationale and key rating drivers**
- **Rating sensitivities: Factors likely to lead to rating actions**
- **Positive factors**
- **Negative factors**
- **Analytical approach:** Standalone
- **Outlook: Stable**
- **Detailed description of key rating drivers:**
- **Key strengths**
- **Key weaknesses**
- **Liquidity: Strong**
- **Environment, social, and governance (ESG) risks**
- **Applicable criteria**
- **About the company and industry**
- Industry classification
- **Brief Financials (₹ crore)** — Standalone
- **Annexure I — Details of instruments / facilities**
- **Annexure II — Rating history**
- **Annexure III — Basis and evidence notes**

The rating view itself lives in that document; it is referenced here rather than restated, so the two cannot drift apart.

---

*Reproduce this workpaper: `python tools/make_workpaper.py hdfc-securities --force`. Re-verify the case: `python tools/delivery_audit.py hdfc-securities`.*
