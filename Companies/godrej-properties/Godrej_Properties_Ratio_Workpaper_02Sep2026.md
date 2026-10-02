# Godrej Properties Limited — Ratio Workpaper (02-Sep-2026)

Agency: ICRA. Basis: CONSOLIDATED (per the Consolidation methodology — GPL develops substantially through project-level SPVs/JVs, so the consolidated view is the economically relevant one). All figures Rs crore unless stated.

## 1. Document Read Log (Step 1b)

| Document | What it is | Key figures / material items contributed |
|---|---|---|
| `integrated-annual-report-2025-26-...md` | FY2025-26 Integrated Report (audited, newest) | Consolidated BS/P&L/notes for FY2026 & FY2025; Note 31 Other Income decomposition (fair value gain on control Rs 2,093.01 cr); Notes 22/25 borrowings; promoter shareholding 51.66% (31-Mar-2026); ESG/BRSR data; unmodified audit opinion with one Rule 11(g) technical exception (accounting-software backup servers); Booking Value Rs 34,171 cr, Collections Rs 19,965 cr, OCF Rs 7,830 cr |
| `gpl-integrated-report-2024-25-...md` | FY2024-25 Integrated Report (audited) | Consolidated BS/P&L for FY2025 & FY2024 comparative — used to CROSS-CHECK the FY2025 figures taken from the FY2026 AR (Revenue, PAT, Total Equity all matched to the rupee); Booking Value Rs 29,444 cr / Collections Rs 17,047 cr for FY2025, independently corroborating the FY2026 AR's prior-year reference; promoter stake was 46.67% here (superseded — see failure mode 26 note below) |
| `gpl-ir-23-24-...md` | FY2023-24 Integrated Report | Not separately re-extracted this pass beyond what the FY24-25 AR's comparative column already supplied; flagged as a scope limit, not an absence claim |
| `investor-presentation-cmoqxpog...md`, `investor-presentation-cmselyvbn...md`, `s-efinal-ip-...md`, `s-efinal-o04qkGPNw5WXfrYsPKfo.md`, `seip-05022026-...md` | Q1-Q4 FY2026 investor presentations / SE filings | Not individually re-extracted line-by-line in this pass beyond the pre-flight's document-date ranking; the two annual reports already carry the FY2026 full-year audited figures these presentations would corroborate quarterly, so the annual figures were prioritised under the time available |

**Failure-mode-26 catch, recorded here explicitly:** promoter shareholding is stated as **51.66%** (25 promoter entities, 31-Mar-2026, FY2025-26 AR's own Corporate Governance table) — NOT the 46.67% figure that appears in the older FY2024-25 AR. The newest document was used, per the binding rule.

## 2. Pre-flight output (Step 1a) — pasted verbatim

Run: `python tools/preflight.py godrej-properties`. Full raw output is reproducible from this command; the material findings acted on in this workpaper and the rationale are:
- Prior ICRA rating action PRESENT for this exact issuer (17-Oct-2025, 21-Jul-2026) — Step 14 is applicable; no "no prior rating" claim was made.
- Rated-amount table PRESENT in the 21-Jul-2026 rationale — imported per the five-condition amendment (see the rationale's Summary of rating action).
- Aggregate-note contaminants flagged inside Other Income/Other Expenses — decomposed component-by-component in `compute_ratios.py` (Note 31, both years available).
- ESG data, instrument details, capex, shareholding, auditor opinion, subsidiaries all flagged PRESENT — none described as unavailable in the rationale.
- Sector-defining-metric probe returned a metals/cement false positive ("utilisation/EBITDA per tonne") under the case's original "Construction" sector mis-tag; overridden with the Real Estate sector's own defining metrics (Booking Value, Collections, inventory/debt) per CLAUDE.md's failure-mode-21 table, after the sector tag was corrected to "Real Estate."

## 3. Computed ratio suite (consolidated), `compute_ratios.py`

| Particulars | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Revenue from Operations | 3,035.62 | 4,922.84 | 5,131.43 |
| Other Income | 1,298.60 | 2,044.21 | 3,279.45 |
| OPBDIT (ICRA convention, ex Other Income) | (129.68) | 44.36 | (416.57) |
| OPBDIT margin (%) | (4.27) | 0.90 | (8.12) |
| PAT (total) | 747.06 | 1,389.23 | 1,840.66 |
| PAT (owners) | 725.27 | 1,399.89 | 1,850.20 |
| Net worth | 10,301.44 | 17,573.73 | 19,354.89 |
| Total debt (incl. lease) | 10,679.29 | 12,641.40 | 15,894.09 |
| Total debt (ex-lease, matches ICRA's own "gross debt") | 10,656.46 | 12,561.16 | 15,614.87 |
| Gearing (x) | 1.04 | 0.72 | 0.82 |
| TOL/TNW (x) | 2.47 | 2.16 | 3.23 |
| Interest coverage (x), accrual OPBDIT basis | (0.85) | 0.26 | (3.04) |
| Cash + liquid investments | 3,108.06 | 5,231.53 | 4,744.97 |
| Booking Value | n/a (not stated cleanly) | 29,444.0 | 34,171.0 |
| Collections | n/a | 17,047.0 | 19,965.0 |
| Operating cash flow | n/a | 7,484.0 | 7,830.0 |
| Memo: OCF / Interest coverage (cash basis) | n/a | 43.1x | 57.2x |

**Trend commentary.** Revenue and PAT both grew steadily across all three years, but the accrual OPBDIT/interest-coverage measures are negative or near-nil throughout — this is NOT a deteriorating trend, it is a persistent, structural feature of project-completion accounting, present in all three years reviewed (not a new FY2026 phenomenon). Net worth nearly doubled (Rs 10,301 cr → Rs 19,355 cr) on retained profit with zero dividend outflow. Gearing improved FY2024→FY2025 (1.04x→0.72x) on a large equity base-year effect, then rose again FY2025→FY2026 (0.72x→0.82x) as debt funded higher construction/land spend — consistent with, and smaller than, the further rise to ~1.1-1.2x-equivalent debt levels the company itself guides for FY2027.

## 4. Tie-out results

`compute_ratios.py` (27/27 reconcile) plus `tools/tieout_mutation.py` (coverage measured at 60.9% by mutation, up from an initial 52.7% after adding the equity-split and KPI cross-source checks below). Every tie-out and every remaining uncovered input is listed in the engine's own `tieouts()`, `DISCLOSED_DIFFERENCES` and `UNVERIFIED_INPUTS` — reproduced in summary:

- P&L waterfall (Revenue+OtherIncome−Expenses=PBT; PBT+JV−Exceptional=PBT; PBT−Tax=PAT; PAT split to owners+NCI) — all three years, all reconcile.
- Other Income decomposition ties to Note 31's own printed total — FY2025 and FY2026 (FY2024 not decomposed, no comparative column exists — disclosed).
- Balance sheet identity (Equity+Liabilities=Assets) — all three years, reconciles.
- Equity split (owners+NCI=Total Equity) — all three years, reconciles (added after `tieout_mutation.py` flagged it as previously uncovered).
- Cross-source: FY2025 Revenue/PAT/Total Equity, and separately Booking Value/Collections/OCF, reproduce identically between the FY2025-26 AR's comparative column and the FY2024-25 AR's own figures for its own year.
- External: computed total debt (ex-lease), March 2026, reconciles to the rupee (Rs 15,614.87 cr) against ICRA's own published "gross debt" of Rs 15,615 cr (21-Jul-2026 rationale, same issuer, reference library).

**Disclosed, uncovered by any tie-out (named per failure mode 39, not silently gapped):** the individual debt-component split for FY2024/FY2025 (no second published source for those two years specifically); the cash-component split (cash vs bank balances vs current investments) in any year (no second published source for the exact split); inventory and trade receivables (transcribed directly, not tied to a current-assets identity because the remaining current-asset lines — Loans, Other Current Financial/Non-Financial Assets — were not separately captured); finance_cost and depreciation individually (used inside OPBDIT but not decomposition-tied to Total Expenses, since the remaining expense lines — Cost of Materials, Purchases, Employee Benefits — were read but not stored as structured inputs).

## 5. Methodology Compliance Map

| Rating factor (Real Estate Methodology, Nov 2024) | Company evidence | Assessment | Weight |
|---|---|---|---|
| Scale and market position | India's #1 developer by Booking Value, 3rd consecutive year; Rs 34,171 cr FY2026, +16% YoY | Strongly positioned | High |
| Project execution track record | 78 msf delivered since FY2018; cash-flow adequacy ratio ~80% for ongoing projects | Strongly positioned | High |
| Financial risk — leverage | Gearing 0.82x, TOL/TNW 3.23x (FY2026); rising per company's own FY2027 guidance | Moderately positioned, monitorable | High |
| Financial risk — coverage | Accrual OPBDIT/interest <1x (structural, project-completion accounting); cash-flow (OCF/interest) ~57x | Requires the cash-flow lens, not the accrual lens, per the methodology's own recognition of real-estate revenue timing | High |
| Liquidity | Cash+liquid investments Rs 4,745 cr; OCF Rs 7,830 cr, 30% 3-yr CAGR | Strong | Medium |
| Parent/Group support | Godrej Industries Group; Rs 12,850 cr equity raised FY2019-25 | One support notch (financial flexibility, not an explicit guarantee) | Medium |
| Corporate governance | Unmodified audit opinion; one technical Rule 11(g) exception (non-financial) | Satisfactory | Medium |

**Applicable rating methodologies read in full this session:** Corporate Credit Rating Methodology (July 2025); Real Estate, Rating Methodology (November 2024).

## 6. Materiality sweep (Step 8) — decisions

| Item found | Include/exclude decision | Reason |
|---|---|---|
| Rs 2,093.01 cr (FY2026) / Rs 930.35 cr (FY2025) fair value gain on control | EXCLUDE from OPBDIT (already excluded by the "less Other Income" convention); INCLUDE, disclosed prominently, in the PAT/rationale narrative | Non-cash, non-recurring, but material enough to distort headline PAT interpretation if left unflagged |
| Rs 23.11 cr exceptional item, FY2026 (Note 59) | Not separately investigated this pass — immaterial (~0.9% of PBT) relative to the fair-value-gain item above | Materiality threshold (R13, ~1% of TNW/5% of PBT) not clearly crossed; flagged as a scope limit |
| Rule 11(g) accounting-software backup-server exception in the audit report | INCLUDE as a governance observation | Technical compliance matter, not a financial-statement qualification or going-concern flag — disclosed as such, not overstated |
| LTIFR 0.06 with 5 contractor fatalities, FY2026 | INCLUDE as a flagged ESG/safety observation | Credit-relevant to a construction-intensive business; no multi-year trend was extracted this pass, so it is disclosed as a single-year data point, not asserted as a trend |
| Godrej Industries Group support | INCLUDE as one scorecard support notch | ICRA's own published rationale explicitly names this as a rating strength |

## 7. Caveats

- FY2024 Other Income is not decomposed to component level (no comparative column in either AR for that note); FY2024 OPBDIT carries this caveat.
- FY2024 Booking Value/Collections/OCF are not stated as clean, non-chart figures and are left blank rather than back-calculated from multiplier statements.
- Investor presentations and the FY2023-24 AR were not individually re-extracted line-by-line in this pass — flagged as a scope limit under the SOP's own proportionality principle, given the two most recent audited annual reports already supply and cross-corroborate the headline figures this rating turns on.
- Annexure II (complete consolidated-entity list) and ISIN-level instrument detail were not extracted from the company's own annual report this pass; both are flagged in the rationale as outstanding for issuer confirmation rather than reconstructed or omitted silently.
