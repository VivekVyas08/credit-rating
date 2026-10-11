# Reliance Industries Limited — Ratio Workpaper (CRISIL)

**Issuer:** Reliance Industries Limited (RIL) · **Agency:** CRISIL · **Date:** 10 October 2026 ·
**Basis:** Consolidated (full consolidation) · **Engagement type (R15):** new assignment in this
exercise; RIL already carries a CRISIL rating (declared in §0) · **Data cut-off:** audited FY2026
(31-Mar-2026) consolidated financial statements; Q1 FY2027 (30-Jun-2026) unaudited media release
dated 17-Jul-2026.

All amounts Rs crore unless stated. Every computed figure comes from `compute_ratios.py` (208/208
tie-outs; mutation coverage 94.8%, the 35 untested inputs named in its `DISCLOSED_DIFFERENCES`).
Spreads: `RIL_Financial_Spreads.xlsx` (internal 208/208; external 38/38 against screener.in).
Model: `RIL_Financial_Model_10Oct2026.xlsx`. Scorecard: `Rating_Scorecard_Reliance Industries
Limited.xlsx`.

## 0. Independence and anchor exposure (declared)

- **Anchor exposure — present and declared.** RIL's own FY2025-26 annual report (MD&A, credit
  rating table) states "Long-term Debt | CRISIL | AAA (Stable) | Highest rating by CRISIL", and
  the same table shows CARE, ICRA and India Ratings at AAA (Stable), S&P at A- and Moody's at Baa2.
  The Q1 FY2027 release (17-Jul-2026) adds that Moody's upgraded RIL's foreign-currency debt to
  Baa1. The pre-flight found CRISIL's 30-Mar-2026 Credit Bulletin on RIL in the reference library,
  and RIL actions by CareEdge (03-Jul-2026) and ICRA (29-Jan-2026).
- **What was read before §13 was written:** from the CRISIL bulletin, ONLY its "Annexure - Details
  of Bank Lenders & Facilities" (Step 7b, failure mode 29 — reading an amount cannot form a credit
  view). The bulletin's analytical text (lines 7-13 of the file) was opened only at Step 14 (§14).
  The CareEdge and ICRA actions were not opened.
- The agreement of the AR with this analysis is noted and **not counted as evidence**.
- Roles: operator supplied documents only; no grade was set by the operator. The rating is UPSI
  until published.

## 1. Step 1 — Input inventory, engagement type, information adequacy

| # | Document | Period | Audited? | Basis |
|---|---|---|---|---|
| 1 | RIL-Integrated-Annual-Report-2025-26.md | FY2026 (FY2025 comparative) | Audited | Standalone + consolidated |
| 2 | RIL-Integrated-Annual-Report-2024-25.md | FY2025 (FY2024 comparative) | Audited | Standalone + consolidated |
| 3 | RIL-Integrated-Annual-Report-2023-24.md | FY2024 (FY2023 comparative) | Audited | Standalone + consolidated |
| 4 | Media_Release_RIL_Q1_FY2026-27 (17-Jul-2026) | Q1 FY2027 | Limited review | Consolidated + standalone |
| 5 | 24042026_Media_Release_RIL_Q4_FY2025-26 | Q4 / FY2026 | Audited results | Consolidated + standalone + segments |
| 6 | Media_Release_RIL_Q3_FY2025-26 (16-Jan-2026) | Q3 / 9M FY2026 | Limited review | Consolidated + standalone |
| 7 | Media_Release_RIL_Q2_FY2025-26 (17-Oct-2025) | Q2 / H1 FY2026 | Limited review | Consolidated + standalone |
| 8 | MediaRelease-RILQ1FY2025-26 | Q1 FY2026 | Limited review | Consolidated + standalone |
| 9 | 25042025_Media_Release_RIL_Q4_FY2024-25 | Q4 / FY2025 | Audited results | Consolidated + standalone + segments |

**Missing and handling.** (a) Instrument term sheets / sanction letters — not supplied; the
CRISIL-rated bank facilities are imported from CRISIL's 30-Mar-2026 bulletin under the
five-condition amendment (§8); the CRISIL-rated NCD and CP programme sizes are NOT in that
bulletin and are marked "to be confirmed by issuer". (b) Sector-assumptions document — not
supplied; forward drivers come from the company's own segment history, Q1 FY2027 trends and
labelled analyst judgment (§12). **Information adequacy:** adequate — three audited ARs, six
quarterly releases; no INC trigger.

## 2. Step 1a — Pre-flight (verbatim output in `_preflight_output.txt`, Appendix A)

Items reported PRESENT and how each is handled: prior CRISIL action (§0, §14); AR credit-rating
note (§0); subsidiaries — named in §7.1; ESG data — quoted in the rationale's ESG section;
instrument details — §8; capex — §11-§12; shareholding — promoter group 49.11%; auditor opinion /
KAMs — §7; sector metric — the probe classified the sector as distribution (receivable / GCA days)
and flagged its own match as ambiguous: RIL is a diversified conglomerate, so the rationale
carries each segment's own metric (O2C throughput, KG D6 output, Jio subscribers and ARPU, retail
stores and area) AND receivable / GCA days (19.85 / 119.05 days, FY2026). [0c] and [0d] found no
aggregate-note contaminant or cash-flow-vs-note conflict; the one-time item was nonetheless found
by reading (§5.2). [10] flags a CareEdge table — not used in this CRISIL case.

## 3. Step 1b — Document Read Log (newest first)

| Document | What it contributes | Material / one-off items flagged |
|---|---|---|
| Q1 FY2027 release (17-Jul-2026) | Revenue 3,40,257 (+24.5% YoY); EBITDA 54,067 (+10.1% on recurring basis); PAT 23,196; capex 38,682; gross debt 3,69,705; cash 2,46,791; net debt 1,22,914 (ND/EBITDA 0.57x annualised); Jio 533.3 mn subscribers, ARPU Rs 215.6; RRVL revenue 90,408; O2C EBITDA 17,010 (+17.2%); throughput 18.1 MMT; KG D6 59.2 BCFe | Jio Platforms filed its DRHP with SEBI (IPO); Moody's upgrade to Baa1; RCPL (consumer brands) demerged from the retail arm; Q1 FY2026 comparative contained the 8,924 one-time gain; finance cost +18.5% on 5G capitalisation; NCDs outstanding 27,389 (secured 20,000) |
| FY2025-26 AR | All FY2026/FY2025 statements and notes (BS p196, P&L p198, CF p202); notes 16-17 (borrowings, DoT liabilities by auction), 20 (current borrowings, CP 13,186), 22-23 (current DPL, contract liabilities 1,72,201), 26 (other income), 29 (finance cost; capitalised interest 16,091), 30 (other expenses), 34 (contingencies; commitments 66,517), 35 (net gearing 0.14), 44 (supplier finance 76,377); MD&A credit-rating table; segment and KPI narrative; AOC-1 | Rs 10 lakh crore AI data-centre investment plan announced; Rs 75,000 crore clean-energy commitment; battery giga-factory (40 GWh, commissioning from 2026); KG D6 gas-migration demand USD 2.81 bn (RIL share USD 1.87 bn), SLP filed in the Supreme Court; SEBI RPL disgorgement Rs 447.27 crore + 12% interest — Supreme Court reserved judgment 30-Jan-2026; onerous-contract provision (JioStar) 17,742; KAM on Level-3 valuation of Rs 77,852 crore JDFPL preference shares; unmodified opinions; S&P upgrade to A- (Dec-2025) |
| Q4 FY2026 release (24-Apr-2026) | FY2026 headline table, audited segment information (revenue, EBITDA, EBIT, assets, liabilities), KPI tables (Jio, Retail, O2C, O&G) | Note 5: other income includes 8,924 one-time gain; dividend Rs 6/share recommended; New Labour Codes impact not material |
| Q3 FY2026 release (16-Jan-2026) | 9M FY2026 results; NCDs 27,389 | Labour codes notified; 9M other income includes 8,924 |
| Q2 FY2026 release (17-Oct-2025) | H1 FY2026; NCDs 28,389 (secured 21,000) | EPS restated for the Oct-2024 bonus |
| Q1 FY2026 release | Q1 FY2026 results | First disclosure of the 8,924 gain ("proceeds of profit from sale of listed investments"); EBITDA +15% excluding it |
| FY2024-25 AR | FY2025/FY2024 statements; note 35 (net gearing 0.14 / 0.15); finance-cost footnote (capitalised 18,283 / 15,222); next-year comparatives used as second sources | 1:1 bonus issue (Oct-2024); JioStar (Star India) consolidated from 14-Nov-2024; provisions jump to 28,304 (onerous contracts) |
| Q4 FY2025 release (25-Apr-2025) | FY2025/FY2024 headline table (EBITDA 1,83,422 / 1,78,290; capex 1,31,107 / 1,31,769; ND/EBITDA 0.64 / 0.65); FY2024 segment information; KPIs | Store rationalisation (19,340 stores after 2,659 openings) |
| FY2023-24 AR | FY2024/FY2023 statements; FY2023 discontinued operations (Jio Financial Services demerger); note 35 (0.15 / 0.18) | FY2023 profit from discontinued operations 418; cash 6,044 moved out on demerger |

## 4. Steps 2-4 — Routing, methodology, peers

**Routing.** Non-financial corporate, diversified (refining/petrochemicals, E&P, retail, telecom
and digital, media). CRISIL Methodology folder ONLY: *Crisil Ratings criteria for manufacturing,
trading and corporate services sector (March 2026)* — Section I scope: "the broader rating
methodology for entities in the manufacturing and corporate services sectors" (covers RIL's
manufacturing and service businesses); *Criteria for consolidation (February 2025)*; *Basics of
ratings (June 2026)* (scale, LT-ST mapping, outlook, default recognition). Linkage criteria
(*criteria-for-factoring-parent-group-government-linkages*, February 2025) consulted for the
parent-direction check only (§13). No sector-specific CRISIL methodology covers a conglomerate;
the holding-company criteria do not apply (RIL itself operates the O2C and E&P businesses).

**Factors that structure the analysis (Step 3):** business risk — industry risk (median rating),
market position (pricing flexibility, diversity), operating efficiency; financial risk —
accounting quality, adequacy of cash flows, liquidity and financial flexibility; management risk
(risk appetite: "a propensity to undertake projects that are larger than existing operations, is
not viewed favourably"); project risk ("the size of the project compared with the existing
operations"); ESG (materiality test: sector, foreign holding, external borrowings).

**Peer craft (Step 4).** CRISIL's L&T rationale (30-Jun-2026) was read for format only: "Ratings
reaffirmed" header, Rating Action table with regulator, Detailed Rationale, Analytical Approach,
strengths/weaknesses, "Liquidity: Superior", ESG Profile with key highlights, Outlook, downward-only
sensitivities at AAA, About the Company, Key Financial Indicators (operating income, PAT, PAT
margin, adjusted debt/adjusted networth, interest coverage), annexures. Zero facts carried.

## 5. Step 5 — Extraction, basis, normalisation

### 5.1 Analytical basis (R12 — methodology-determined)

CRISIL *Criteria for consolidation*: "All subsidiaries of the rated entity are generally
consolidated through the pooling of interests method for a fair representation of the entity's
operations and liabilities"; exceptions are a subsidiary "in a sector different from that of the
parent" or one "explicitly ring-fenced". RIL's material subsidiaries — Jio Platforms (66.43%),
Reliance Jio Infocomm (100% of JPL), Reliance Retail Ventures (83.56%), Reliance Retail, Reliance
International (FY2025-26 AR Board's report) — are operating businesses under RIL's management
control, sharing the Reliance name and funded through the group's capital framework (note 35:
"Maintain investment grade ratings for all issuing entities"). There is no financial-sector
subsidiary of note after the FY2023 demerger of Jio Financial Services. **Basis: full
consolidation**, matching `case.json` "consolidated". Non-controlling interest (1,81,836) stays in
adjusted networth.

### 5.2 Operating-profit normalisation (written decision per component)

| Item | FY2026 | Treatment | Reason |
|---|---|---|---|
| Interest income (note 26) | 13,302 | Retained in PBDIT | CRISIL PBDIT "includes recurring non-operating income"; recurs every year (11,240 / 10,745 / 12,410 / 13,302) |
| Dividend income | 9,100 | 8,924 removed; 176 retained | Q4 FY2026 release note 5: other income "includes Rs 8,924 crore, being proceeds of profit from sale of listed investments"; the company itself excludes it for comparison; dividend income is otherwise 38 / 89 / 504 |
| Other non-operating income | 3,614 | Retained | recurring (1,758 / 3,302 / 3,507) |
| Gain/(loss) on financial assets | 2,946 | Retained | treasury gains on a 2.5 lakh crore book recur (-1,302 / 1,921 / 1,557) |
| Forex loss classified in finance costs | 2,788 | In interest (added back in PBDIT) | company classifies it as borrowing cost; conservative for coverage |
| Exchange difference in other expenses | (35) gain | Retained | immaterial (463 / 109 / (189) / (35)) |
| Loss on sale/discard of PPE | 116 | Retained | recurring and small |
| New Labour Codes | not quantified | n/a | release: "not material to the results" |

PBDIT = 1,53,896 / 1,78,290 / 1,83,422 / 1,98,987 (FY2023-26). The company's EBITDA (2,07,911
FY2026) is PBDIT + 8,924 — tied in the engine to the releases for FY2024-FY2026.

### 5.3 Balance-sheet splits

Current borrowings 1,03,670 (FY2026) = working-capital and short-term loans 64,519 + CP 13,186 +
current maturities 25,965 (note 20; engine ties each line). DoT liabilities sit in two captions:
non-current 99,552 (note 17) + current 4,962 inside other current financial liabilities (note 22).
Supplier finance 76,377 sits inside trade payables (47,121) and other financial liabilities
(29,256) (note 44). Contract liabilities 1,72,201 sit inside other current liabilities (note 23).

## 6. Step 6 — Ratio suite, tie-out, coverage (engine)

Definitions (CRISIL_CONVENTIONS §1-§5): PBDIT incl. recurring other income, excl. one-time;
interest incl. capitalised; adjusted debt = borrowings + leases + DoT deferred payment liabilities
(+ supplier finance in the wide rows); adjusted networth incl. NCI, DTL excluded; RoCE = PBIT /
average (adjusted debt + adjusted networth + DTL); NCATD = (PAT - dividend + D&A) / adjusted debt;
CDSCR per §4 with debt payable within a year = current maturities + current DoT + current leases
(CP and working-capital lines excluded as rolled over).

| Metric | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| Operating income (net of GST) | 891,311.00 | 914,472.00 | 980,136.00 | 1,075,675.00 |
| Gross revenue (value of sales and services) | 974,864.00 | 1,000,122.00 | 1,071,174.00 | 1,175,919.00 |
| EBITDA as reported (company) | 153,896.00 | 178,290.00 | 183,422.00 | 207,911.00 |
| PBDIT (CRISIL) | 153,896.00 | 178,290.00 | 183,422.00 | 198,987.00 |
| PBDIT margin (%) | 17.27 | 19.50 | 18.71 | 18.50 |
| OPBDIT excl. all other income | 142,162.00 | 162,233.00 | 165,444.00 | 178,949.00 |
| OPBDIT margin excl. other income (%) | 15.95 | 17.74 | 16.88 | 16.64 |
| Other income share of PBDIT (%) | 7.62 | 9.01 | 9.80 | 10.07 |
| PAT (incl. associates) | 74,088.00 | 79,020.00 | 81,309.00 | 95,754.00 |
| PAT margin (%) | 8.31 | 8.64 | 8.30 | 8.90 |
| PAT excl. one-time gain (pre-tax amount deducted) | 74,088.00 | 79,020.00 | 81,309.00 | 86,830.00 |
| Interest (incl. capitalised) | 28,401.00 | 38,340.00 | 42,552.00 | 43,152.00 |
| Interest capitalised | 8,830.00 | 15,222.00 | 18,283.00 | 16,091.00 |
| Interest coverage (x) | 5.42 | 4.65 | 4.31 | 4.61 |
| Interest coverage on P&L finance cost (x) | 7.86 | 7.71 | 7.56 | 7.35 |
| Borrowings | 313,966.00 | 324,622.00 | 347,530.00 | 374,421.00 |
| Lease liabilities | 20,426.00 | 21,520.00 | 22,045.00 | 23,579.00 |
| Deferred payment liabilities (spectrum) | 117,272.00 | 112,849.00 | 109,148.00 | 104,514.00 |
| Adjusted total debt | 451,664.00 | 458,991.00 | 478,723.00 | 502,514.00 |
| Supplier finance | - | - | 103,716.00 | 76,377.00 |
| Adjusted total debt incl. supplier finance | - | - | 582,439.00 | 578,891.00 |
| Adjusted networth (incl. NCI) | 828,881.00 | 925,788.00 | 1,009,626.00 | 1,085,866.00 |
| Gearing (x) | 0.54 | 0.50 | 0.47 | 0.46 |
| Gearing incl. supplier finance (x) | - | - | 0.58 | 0.53 |
| Company net gearing (x) | 0.18 | 0.15 | 0.14 | 0.14 |
| TOL/ANW (x) | 0.94 | 0.90 | 0.93 | 1.01 |
| Adjusted debt/PBDIT (x) | 2.93 | 2.57 | 2.61 | 2.53 |
| Adjusted debt incl. SF/PBDIT (x) | - | - | 3.18 | 2.91 |
| Cash and marketable securities | 188,159.00 | 208,375.00 | 230,447.00 | 249,704.00 |
| Net adjusted debt | 263,505.00 | 250,616.00 | 248,276.00 | 252,810.00 |
| Net adjusted debt/PBDIT (x) | 1.71 | 1.41 | 1.35 | 1.27 |
| Company net debt | 125,766.00 | 116,281.00 | 117,083.00 | 124,717.00 |
| Company net debt/PBDIT (x) | 0.82 | 0.65 | 0.64 | 0.63 |
| NCATD (x) | 0.24 | 0.27 | 0.27 | 0.29 |
| NCA (PAT - dividend + D&A) | 109,308.00 | 123,763.00 | 127,265.00 | 145,563.00 |
| Current ratio (x) | 1.07 | 1.18 | 1.10 | 1.10 |
| Debtor days | 11.65 | 12.62 | 15.69 | 19.85 |
| Inventory days | 86.84 | 95.26 | 84.67 | 88.48 |
| Payable days | 91.28 | 111.23 | 108.27 | 84.19 |
| Net working capital (inv + debtors - creditors) | 21,284.00 | 6,021.00 | 1,394.00 | 66,590.00 |
| GCA days (CRISIL: operating current assets / operating income) | 97.53 | 106.45 | 102.06 | 119.05 |
| CFO | 115,032.00 | 158,788.00 | 178,703.00 | 192,113.00 |
| Capex (cash flow) | 140,988.00 | 152,883.00 | 139,967.00 | 122,916.00 |
| FCF (CFO - capex - DPL - lease payments) | -27,362.00 | -1,001.00 | 31,206.00 | 57,953.00 |
| FCF after dividends | -32,445.00 | -7,090.00 | 24,026.00 | 50,074.00 |
| CFO/adjusted debt (x) | 0.25 | 0.35 | 0.37 | 0.38 |
| Capex/PBDIT (x) | 0.92 | 0.86 | 0.76 | 0.62 |
| Debt payable within one year | 57,153.00 | 53,950.00 | 38,964.00 | 38,308.00 |
| Commercial paper outstanding | 20,506.00 | 19,595.00 | 29,162.00 | 13,186.00 |
| Liquidity cover: cash & MS / (debt due 1y + CP) (x) | 2.42 | 2.83 | 3.38 | 4.85 |
| Revenue growth (%) | - | 2.60 | 7.18 | 9.75 |
| RoCE (%) | - | 9.11 | 8.60 | 8.67 |
| CDSCR (x) | - | 1.86 | 2.19 | 2.21 |
| Segment EBITDA share - O2C (%) | - | 36.52 | 31.46 | 31.20 |
| Segment EBITDA share - Oil and Gas (%) | - | 11.82 | 12.12 | 9.82 |
| Segment EBITDA share - Retail (%) | - | 13.53 | 14.36 | 13.93 |
| Segment EBITDA share - Digital Services (%) | - | 33.18 | 37.19 | 39.45 |
| Segment EBITDA share - Others (%) | - | 4.96 | 4.88 | 5.60 |
| Consumer businesses (Retail + Digital) EBITDA share (%) | - | 46.70 | 51.54 | 53.39 |
| Energy (O2C + Oil and Gas) EBITDA share (%) | - | 48.34 | 43.58 | 41.02 |
| O2C EBITDA margin on segment revenue (%) | - | 11.05 | 8.77 | 9.14 |
| Digital EBITDA margin on segment revenue (%) | - | 42.63 | 42.18 | 43.46 |
| Retail EBITDA margin on segment revenue (%) | - | 7.53 | 7.58 | 7.29 |
| Jio subscribers (mn) | - | 481.80 | 488.20 | 524.40 |
| Jio ARPU Q4 (Rs/month) | - | 181.70 | 206.20 | 214.00 |
| Jio data traffic (bn GB) | - | 148.50 | 184.50 | 241.40 |
| Retail stores (nos.) | - | - | 19,340.00 | 20,160.00 |
| Retail area (mn sq ft) | - | - | 77.40 | 78.30 |
| Retail registered customers (mn) | - | - | 349.00 | 387.00 |
| O2C throughput (MMT) | - | 78.20 | 80.50 | 80.00 |
| KG D6 production (BCFe) | - | 260.30 | 270.90 | 248.80 |

**Tie-outs:** 208/208 (balance sheets, P&L, cash-flow totals rebuilt line by line, financing
bridge, note decompositions, next-year comparatives, segment reconciliation to PBT, KPI repeats).
**Mutation coverage:** 640 of 675 inputs change a tie-out = 94.8%; the 35 that do not are named
in `DISCLOSED_DIFFERENCES` (single-sourced cash-flow-only or one-release items; FY2023 capitalised
interest is the only one that feeds a coverage ratio — FY2023 only).

**External tie-out (screener.in consolidated, read 10-Oct-2026): 38/38 exact** once three basis
differences are applied: screener's sales net excise duty and sales tax/VAT (19,895 FY2026);
it moves loss on PPE into other income; its "borrowings" = borrowings + leases + the CURRENT DoT
instalment (4,962) for FY2024-26 (402,962 FY2026) but ALL DoT liabilities for FY2023 (4,51,664 =
our adjusted debt exactly). PAT, CFO, reserves, interest and depreciation match in every year.
**AR's own net-debt bridge (note 35):** gross debt 3,74,421 - cash & marketable securities
2,49,704 = net debt 1,24,717; net gearing 0.14 — our borrowings tie to its gross debt every
year; the company's net debt EXCLUDES leases (23,579) and DoT liabilities (1,04,514), which is why
our net adjusted debt (2,52,810) is about twice it.

**Trend commentary.** PBDIT grew 29.3% FY2023-26 (1,53,896 to 1,98,987) while adjusted debt grew
11.3% (4,51,664 to 5,02,514): adjusted debt/PBDIT eased 2.93x to 2.53x and net adjusted
debt/PBDIT 1.71x to 1.27x. Interest coverage including capitalised interest fell 5.42x to 4.61x
because capitalised interest rose (8,830 to 16,091) with the 5G and new-energy build. The mix
shifted: consumer businesses (Retail + Digital) went from 46.7% to 53.4% of segment EBITDA
(FY2024-26) while energy fell from 48.3% to 41.0% — O2C EBITDA fell 12% in FY2025 (62,389 to
54,988) and recovered 10% in FY2026 (60,546). Free cash flow after capex, DoT and lease payments
turned from -27,362 (FY2023) to +57,953 (FY2026) as capex/PBDIT fell from 0.92x to 0.62x — but
FY2026 CFO was helped by an 86,609 rise in trade and other payables, inside which contract
liabilities rose by 1,09,196 (§9).

## 7. Step 7 — Fact register

| Claim | Value | Source |
|---|---|---|
| Promoter and promoter group holding | 49.11% (664,54,96,096 of 1353,24,72,634 shares) | FY2025-26 AR, distribution of shareholding; FY2023-24 AR 49.11% (pre-bonus share count x2) |
| Institutions / custodian (DR) holding | 38.51% / 1.78% | same table (foreign-holding test for ESG materiality) |
| Credit ratings disclosed | CRISIL, CARE, ICRA, India Ratings AAA (Stable); S&P A-; Moody's Baa2 (Baa1 per Q1 FY2027 release) | FY2025-26 AR MD&A table; Q1 FY2027 chairman's statement |
| Auditors / opinion | Deloitte Haskins & Sells LLP and Chaturvedi & Shah LLP; unmodified; KAMs: litigation (incl. SEBI matter), Level-3 valuation of JDFPL preference shares (Rs 77,852 crore), RJIL revenue recognition (component auditor), IT systems | FY2025-26 AR auditors' reports |
| Contingent liabilities | claims 5,532; guarantees 7,117; capital commitments 66,517 (31,629 FY2025); investment commitments 4,705 | note 34 |
| KG D6 migration demand | USD 2.81 bn (RIL share USD 1.87 bn); company views as remote, not quantified in note 34 | note 33.4(a) |
| SEBI / RPL | disgorgement Rs 447.27 crore + 12% p.a. from 29-Nov-2007; penalty Rs 25 crore; Supreme Court reserved judgment 30-Jan-2026 | note 34 (III) |
| Hathway / DEN license-fee demands | Rs 3,202 crore / Rs 2,157 crore, contested; TDSAT restrained coercive action (DEN) | note 34 (IV)-(V) |
| Capex | company capex excl. spectrum 1,31,769 / 1,31,107 / 1,44,271 (FY2024-26); Q1 FY2027 38,682 | Q4 FY2025, Q4 FY2026, Q1 FY2027 releases |
| AI data-centre plan | "a plan to invest Rs 10 lakh crore for the development of multi-gigawatt (GW) scale AI-ready data centres" — no phasing or funding plan disclosed | FY2025-26 AR |
| Clean-energy plan | Rs 75,000 crore commitment; 100 GW renewable capacity by 2030; battery giga-factory 40 GWh (scalable to 100 GWh) from 2026; 3 MMTPA green hydrogen by 2032; Net Carbon Zero by 2035 | FY2025-26 AR |
| Jio IPO | Jio Platforms filed its DRHP with SEBI in Q1 FY2027 | Q1 FY2027 release |
| Supplier finance | 76,377; payment due 45-1,083 days after invoice vs 1-624 days for comparable liabilities | note 44 |
| Dividend | Rs 6/share for FY2026 = 8,119 (recommended) | note 45 |
| Operating metrics | Jio 481.8 / 488.2 / 524.4 mn subscribers, Q4 ARPU Rs 181.7 / 206.2 / 214.0 (FY2024-26); Retail 19,340 / 20,160 stores, 77.4 / 78.3 mn sq ft; O2C throughput 78.2 / 80.5 / 80.0 MMT; KG D6 260.3 / 270.9 / 248.8 BCFe | Q4 releases (each repeated in the next release — engine) |
| Board | duly constituted with executive, non-executive (incl. a woman director) and independent directors; Mukesh D. Ambani Chairman and Managing Director | secretarial audit report; signatures to the accounts |

### 7.1 Entities consolidated (FY2026 AR — FM17)

Part A of Form AOC-1 in the FY2025-26 AR lists over 210 subsidiaries (row numbering), plus
associates and joint ventures in Part B. Material subsidiaries named with the group's holding:
Jio Platforms Limited (66.43%); Reliance Jio Infocomm Limited (100.00% within JPL); Reliance
Retail Ventures Limited (83.56%); Jiostar India Private Limited (63.16%); Reliance New Energy
Limited (100.00%); Reliance Consumer Products Limited (83.56%; amalgamated with RRVL per AOC-1
note). All are fully consolidated (§5.1); the rationale's annexure names these and refers to
AOC-1 for the full list.

## 8. Step 7b — Instrument details

**Disclosed in the company's documents (drawn):** NCDs 27,389 outstanding at 31-Mar-2026 and
30-Jun-2026, of which secured 20,000 (Q4 FY2026 and Q1 FY2027 release notes) — the 7.79% secured
NCDs mature 15,000 in 2033-34 and 5,000 in 2032-33; unsecured NCDs 7,389 at 8.65-9.05% mature in
2028-29 (note 16.3). CP outstanding 13,186 (note 20). Foreign-currency bonds 57,274 (non-current)
+ 510 (current) (note 16). No ISIN for any debt instrument appears in the AR (searched
`INE[0-9A-Z]{9,10}` — only the equity ISIN INE002A01018).

**CRISIL-rated bank facilities — imported under the five-condition amendment.** (1) CRISIL's own
publication for this issuer is in the reference library (Credit Bulletin, 30-Mar-2026); (2)
reproduced verbatim in the rationale annexure with the date stamped; (3) labelled CRA-published,
not issuer-confirmed; (4) line integrity verified: 56 lines = ECB 23,424 + fund-based 22,740 +
non-fund-based 50,510 + proposed fund-based 318 + proposed non-fund-based 8 + term loan 3,000 =
**Rs 1,00,000 crore**; (5) limits vs drawn debt stated (below). **Freshness:** the bulletin is 194
days old at the report date; the documents describe no divestment or prepayment in the interval,
but the table is presented as of 30-Mar-2026, not as the current programme.

**NCD and CP programme sizes rated by CRISIL:** not in the bulletin and not in the company's
documents — **to be confirmed by issuer**. (CareEdge's 03-Jul-2026 action lists its own NCD and CP
programmes; another agency's programme is not CRISIL's and is not carried.)

**Limits vs drawn debt.** The 1,00,000 is RIL's sanctioned bank-facility limits (fund-based,
non-fund-based, ECB, term loan); consolidated drawn borrowings are 3,74,421 across all group
entities (note 35). They are different measures and do not reconcile.

## 9. Step 8 — Materiality sweep (R13: material if ≥1% of adjusted networth = Rs 10,859 crore, or ≥5% of PBT = Rs 6,158 crore, or plausibly ≥1 notch, or any governance / regulatory / default item)

| Item | Size | Decision |
|---|---|---|
| One-time gain on sale of listed investments | 8,924 (4.3% of company EBITDA) | INCLUDE: removed from PBDIT (§5.2) |
| Contract liabilities +1,09,196 (to 1,72,201); payables-driven CFO | 10.1% of networth | INCLUDE: flagged in liquidity and as an issuer question; stress case unwinds 1,00,000 |
| Supplier finance 76,377 (1,03,716 FY2025) | 7.0% of networth | INCLUDE: wide adjusted-debt measure (gearing 0.53x, debt/PBDIT 2.91x) |
| AI data-centre plan Rs 10 lakh crore | ~5x FY2026 PBDIT | INCLUDE: key project-risk monitorable and downward sensitivity; each Rs 1 lakh crore of debt-funded spend adds ~0.46x to FY2027 adjusted debt/PBDIT (1,00,000 / 2,16,177) |
| KG D6 migration demand USD 1.87 bn (RIL share) | ~1.6% of networth | INCLUDE: event risk; company views as remote; SLP pending |
| SEBI RPL disgorgement Rs 447.27 crore + interest | below threshold, but regulatory | INCLUDE (governance item regardless of size) |
| Onerous-contract provision (JioStar) 17,742 | 1.6% of networth | INCLUDE in narrative (media rights cost); provision already booked |
| Capital commitments doubled to 66,517 | 6.1% of networth | INCLUDE: capex intensity |
| Level-3 valuation of JDFPL preference shares Rs 77,852 crore (standalone) | standalone item; eliminated on consolidation | NOTE only — affects standalone networth, not the consolidated basis |
| Jio IPO (DRHP filed) | event | INCLUDE as positive financial-flexibility monitorable; no proceeds assumed |
| Moody's Baa1 / S&P A- upgrades | — | INCLUDE in financial flexibility (global-scale; NOT mapped to the national scale as evidence of a grade — FM61) |
| Hathway / DEN demands 3,202 / 2,157 | below threshold | EXCLUDE from text beyond a mention in contingent liabilities |
| New Labour Codes | "not material" | EXCLUDE |

## 10. Step 10 — Methodology Compliance Map (CRISIL corporate criteria March 2026; consolidation February 2025)

CRISIL's corporate criteria publish no numeric indicative bands for these factors (business risk
is descriptive; industry risk "largely indicates the median rating"); the assessment column is
therefore descriptive, and the scorecard's numeric bands are this project's own screening tool.

| Rating factor (CRISIL's name) | Section | RIL evidence / metric | Assessment | Weight |
|---|---|---|---|---|
| Industry risk | Business risk | O2C cyclical (O2C EBITDA 62,389 -> 54,988 -> 60,546); telecom and retail are domestic-demand businesses with high entry barriers | Moderate overall; diversification lowers the blended median | Medium |
| Market position | Business risk | Jio 524.4 mn subscribers; Retail 20,160 stores, 387 mn registered customers; O2C throughput 80.0 MMT; KG D6 ~30% of India's gas production (AR); no segment above 39.5% of EBITDA | Very strong; pricing flexibility in Digital (ARPU 181.7 -> 214.0) | High |
| Operating efficiency | Business risk | Digital EBITDA margin 43.5%; Retail 7.3%; O2C 9.1%; integrated refining-petrochemicals | Strong | Medium |
| Accounting quality | Financial risk | Unmodified opinions; Level-3 KAM; one-time gain disclosed by the company; contract-liability swing unexplained | Adequate; adjustments made (§5.2) | Medium |
| Adequacy of cash flows | Financial risk | PBDIT 1,98,987; adjusted debt/PBDIT 2.53x (2.91x with supplier finance); NCATD 0.29; interest coverage 4.61x incl. capitalised; CDSCR 2.21x; FCF 57,953 | Strong for the category, with leverage held up by capex | High |
| Liquidity and financial flexibility | Financial risk | Cash & marketable securities 2,49,704; debt due within a year 38,308 + CP 13,186 (cover 4.85x); market cap ~Rs 15.8 lakh crore (screener.in); S&P A-, Moody's Baa1 | Superior | High |
| Management risk (risk appetite) | Management | capex 1.31-1.44 lakh crore a year; Rs 10 lakh crore AI plan; stated investment-grade capital framework (note 35); promoter 49.11% | High risk appetite tempered by a record of funding within the framework | Medium |
| Project risk | Project | new-energy giga-factories, AI data centres; size vs operations large in absolute terms but staged | Key monitorable | Medium |
| ESG | ESG | O2C emissions-intensive; Net Carbon Zero 2035 target; LTIFR 0.06 (O2C and E&P); FII/custodian holding and USD bonds make ESG material on CRISIL's test | Neutral-to-moderate | Low |
| Consolidation basis | Consolidation criteria | §5.1 | Full consolidation | — |
| Parent / group linkage | Linkage criteria | RIL is the flagship; promoter holding via LLPs; no weaker parent dependent on RIL's cash identified in the documents | No adjustment in either direction | — |

## 11. Step 11 — Liquidity: sources vs claims, FY2027 (model base case, Rs crore)

| Sources | | Claims | |
|---|---|---|---|
| Cash and marketable securities 31-Mar-2026 | 2,49,704 | Debt payable within FY2027 (current maturities 25,965 + DoT 4,962 + leases 7,381) | 38,308 |
| Base-case FY2027 CFO (model) | 1,71,022 | Capex (model base) | 1,50,000 |
| | | Dividend (Rs 6/share + NCI) | 8,569 |
| | | Capitalised interest (cash) | 15,247 |
| | | CP outstanding (rolled; shown for cover) | 13,186 |

Cash & marketable securities alone cover debt payable within a year plus CP 4.85x; Q1 FY2027 cash
was 2,46,791 against gross debt 3,69,705. The base case needs no new borrowing in any year; even
the stress case's 2,29,418 of new borrowing over five years is drawn only to hold a 2 lakh crore
cash floor. **Descriptor: Superior** (conclusion of the arithmetic).

## 12. Step 12 — Projections (equity-research Tasks 1-4)

Artefacts: research note `RIL_Research_Note_10Oct2026.md` (Task 1), model
`RIL_Financial_Model_10Oct2026.xlsx` (Task 2: Assumptions, Revenue Model, Income Statement, Cash
Flow, Balance Sheet, Scenarios, DCF Inputs, Valuation, **Credit Ratios** by formula, **Debt
Breakup**), valuation note `RIL_Valuation_Note_10Oct2026.md` (Task 3), charts
`RIL_Charts_10Oct2026.zip` (Task 4, 6 charts). Task 5 not run. Model historicals reproduce the
engine (asserted in code); balance sheet balances in every projected year.

| Scenario (FY2027E-FY2031E) | PBDIT FY2027 | Adj. debt/PBDIT (peak) | Net adj. debt/PBDIT (peak) | Interest coverage (trough) | Gearing (peak) | New borrowing (5 yrs) |
|---|---|---|---|---|---|---|
| Base | 2,16,177 | 2.30x (FY2027) -> 1.60x FY2031 | 1.21x -> 0.11x | 5.39x (FY2027) -> 7.75x | 0.42x | nil |
| Bull | 2,30,728 | 2.16x -> 1.42x | 1.08x -> net cash | 5.75x | 0.42x | nil |
| Bear / rating stress | 1,75,025 | 3.79x (FY2028) | 2.67x (FY2028) | 3.43x (FY2028) | 0.56x | 2,29,418 |
| Tail | 1,51,120 | 5.41x (FY2028) | 4.11x (FY2029) | 2.45x (FY2029) | 0.76x | 4,67,857 |

Base drivers (Assumptions tab, each with source): segment growth O2C 5%/3%, Oil & Gas -5%, Retail
12-10%, Digital 13-10%, Others 10%; margins near FY2026 (O2C 9.0%, Digital 44-45%, Retail
7.3-7.5%); cash capex 1,50,000 falling to 1,25,000; 40% -> 20% of gross interest capitalised;
dividend Rs 6/share then ~10% payout; debt DERIVED from the funding gap with a 2,00,000 cash floor
(FM18) — the base case draws nothing. **Limit of the base case:** it carries the 1.3-1.5 lakh
crore capex run-rate, not the Rs 10 lakh crore AI plan, whose phasing and funding are undisclosed;
each Rs 1 lakh crore of debt-funded spend adds ~0.46x to FY2027 adjusted debt/PBDIT.

**Stress variables (CRISIL's own: price volatility / cyclicality, cash-flow adequacy, project
risk).** Bear: O2C revenue -10% and margin 6.5% for two years, O&G -10% a year, Retail and Digital
growth halved with lower margins, capex +15%, and a 1,00,000 working-capital unwind in FY2027.
Tail: deeper O2C trough (5.0%), capex 1.75 lakh crore, 1,80,000 working-capital unwind.

## 12b. Step 12b — Scorecard (Stage 1 anchor)

Sector "Generic corporate" (closest of the template's 22 to a conglomerate). Inputs from the
engine (FY2024-26) and the model base case (FY+1/FY+2, copied with source notes). Qualitative:
business 1, management 2, support 0, liquidity Superior, outlook Stable (justifications in
`Inputs!F40:F43`). **Anchor: Crisil AA+ / Crisil A1+** (composite 1.732, index 1). The
business-risk gate does not fire (business 1 vs financial 1.96). The anchor is known to under-rate
AA+/AAA (back-test 18-Jul-2026); the one-notch gap to the view in §13 is resolved at 17c.

## 13. Step 13 — Independent rating view (written before opening CRISIL's text)

**Standalone (consolidated) assessment.** Business risk is at the top of the scale: leadership in
four large, unrelated businesses, none above 39.5% of FY2026 segment EBITDA (Digital 76,560; O2C
60,546; Retail 27,034; Oil & Gas 19,050), with the consumer businesses now 53.4% of the total and
growing at double digits (Digital revenue +15.1% CAGR FY2024-26). Diversity cushioned the FY2025
O2C downturn: O2C EBITDA fell 7,401 while Digital and Retail added 10,312. Financial risk is
strong for the category but not pristine on CRISIL's wide debt definition: adjusted debt 5,02,514
(2.53x PBDIT; 2.91x with supplier finance) against a networth of 10,85,866 (gearing 0.46x) and
cash of 2,49,704 (net adjusted debt 1.27x PBDIT). Coverage including capitalised interest is
4.61x. Cash flows now fund capex (FCF 57,953 FY2026, after 1,22,916 of capex).

**Support / linkage, both directions (FM56).** RIL is the group flagship; its promoter holds 49.11%
through LLPs (Srichakra, Devarshi, Karuna, Tattvam Commercials — 10.93%, 8.06%, 8.06%, 8.06%).
No weaker parent drawing on RIL's cash is evidenced in the documents; no notch-down. No support
uplift (RIL is not a supported entity). Global-scale ratings (S&P A-, Moody's Baa1) are used only
as financial-flexibility evidence, never mapped into the grade (FM61).

**Instrument level.** Senior unsecured / secured debt and bank facilities rated at the issuer
level; no hybrid instruments.

**LT/ST.** CRISIL corporate table (basics-of-ratings Table 1): AAA -> A1+.

**Proposed view: Crisil AAA/Stable (long-term) and Crisil A1+ (short-term).** The case for the
top of the scale rests on (i) diversified leadership with a rising share of stable consumer
earnings, (ii) superior liquidity (2.50 lakh crore of cash and marketable securities, 4.85x debt
falling due plus CP) and exceptional financial flexibility (market capitalisation about 3.2x
adjusted debt), and (iii) moderating leverage in the base case (adjusted debt/PBDIT 2.30x in
FY2027 falling to 1.60x by FY2031 with no new borrowing).

**Why not lower.** The stress case (O2C trough, slower consumer growth, capex overrun and a
1,00,000 working-capital unwind) takes adjusted debt/PBDIT to 3.79x and coverage to 3.43x at the
trough — weaker than AAA metrics, but driven by a deliberately severe combination; the cash floor
holds without any refinancing stress, and the base case improves every year.

**Outlook: Stable.** CRISIL's horizon is six months to two years with a one-in-three test. The
base case does not point to a downgrade; the main downside is a debt-funded acceleration of the
AI data-centre and new-energy programmes, which is a sensitivity, not a base case.

**Downward sensitivities (AAA: downward only).** Adjusted debt/PBDIT (incl. DoT liabilities and
leases) above 3.5x on a sustained basis, or net adjusted debt/PBDIT above 2.0x; debt-funded capex
or acquisitions (including the Rs 10 lakh crore AI plan) materially beyond the 1.3-1.5 lakh crore
annual run-rate; a sustained O2C downturn cutting group PBDIT below about 1.75 lakh crore; an
adverse crystallisation of the KG D6 demand.

## 14. Step 14 — Comparison with CRISIL's own publication (opened only after §13 was written)

The only CRISIL publication on RIL in the library is a **Credit Bulletin dated 30-Mar-2026**,
published "solely to update the bank-wise facility details"; it carries no analysis and refers
to a previous Rating Rationale of 30-Oct-2025, which is not in the library (searched
`ls "CRISIL/Report for Reference" | grep -i reliance` — two hits: this bulletin and none other
for RIL). The company's FY2025-26 AR states CRISIL AAA (Stable).

| Item | This analysis (§13) | CRISIL (bulletin 30-Mar-2026 / AR) | Divergence |
|---|---|---|---|
| Long-term rating | Crisil AAA/Stable | Crisil AAA/Stable | none |
| Short-term rating | Crisil A1+ | Crisil A1+ | none |
| Outlook | Stable | Stable | none |
| Basis | Consolidated | not stated in the bulletin | not testable |
| Drivers / figures | §13 | none published in the bulletin | not testable |
| Bank facilities | imported (Rs 1,00,000 crore, 56 lines, verified line by line against the bulletin) | same | — |

**Mandate details found only in the CRISIL publication — REQUIRING ISSUER CONFIRMATION:** the
bank-facility schedule (dated 30-Mar-2026). The NCD and CP programme sizes CRISIL rates are not
published in any document available here. The agreement on the grade is noted and not counted
as evidence (§0).

## 15. Step 15 — Analytical package (proposed view; the Committee decides at 17c)

- Input gaps: term sheets / sanction letters (bank limits imported from CRISIL's dated bulletin;
  NCD/CP programme sizes TBC); no sector-assumptions note (drivers labelled analyst judgment).
- Assumptions and stress: §12 (base 2.30x -> 1.60x; stress peak 3.79x, coverage 3.43x; tail
  5.41x / 2.45x).
- Proposed view: **Crisil AAA/Stable / Crisil A1+**; anchor Crisil AA+ (one notch below —
  committee-resolved, §12b).
- Judgment calls: one-time 8,924 removed; supplier finance shown as a wide measure, not in core
  adjusted debt; AI plan treated as a sensitivity, not in the base case; contract-liability
  swing flagged, not adjusted.

## 17. Step 17 / 17a — Re-verification and delivery gates

**Drift check — computed figures:** every number in the draft was matched against the engine and
model (`ril_drift.py`, scratchpad): 187 matched to computed output, 81 to the case documents, 5 to
the CRISIL bulletin (facility lines), 95 trivial (years, small integers); 7 unmatched, each a
derived sum or difference re-done by hand: 40.29% (38.51% institutions + 1.78% custodian); 7,401
(62,389 - 54,988); 10,312 (8,326 Digital + 1,986 Retail); 27,362 (FY2023 FCF deficit, engine
-27,362); 1,09,196 (1,72,201 - 63,005); 23,424 and 50,510 (bank-facility sub-totals, summed in
code from the 56 lines).

**ERROR FOUND AND FIXED BY THE DRIFT CHECK:** the first draft stated the CRISIL bank-facility
total as Rs 1,04,060 crore (fund-based 26,750; non-fund-based 50,560) — hand arithmetic. Summed in
code, the 56 lines (identical to the bulletin, line by line) total **Rs 1,00,000 crore** (ECB
23,424 + fund-based 22,740 + non-fund-based 50,510 + proposed 326 + term loan 3,000). Corrected in
the rationale, this workpaper and the model's Debt Breakup. The delivery gate's line-integrity
probe did NOT catch it: it parses only two-decimal amounts, and CRISIL's lender tables print
integers (positive control with the wrong total also passed) — flagged as a tooling fix.

**Drift check — non-computed figures (source + corroborating source):** Jio 524.4 mn (Q4 FY2026
release; repeated in Q1 FY2027 release); 20,160 stores / 78.3 mn sq ft (Q4 FY2026 release; FY2025-26
AR MD&A); promoter 49.11% (FY2025-26 AR; FY2023-24 AR); subsidiary holdings 66.43% / 83.56% /
63.16% (AOC-1 only — single source, statutory form); NCD 7.79% Rs 20,000 crore (note 16.3; FY2023-24 AR MD&A
"Rs 20,000 crore 10-year NCD"); NCDs 27,389 / secured 20,000 (Q4 FY2026 and Q1 FY2027 release
notes); DoT 1,04,514 (notes 17 + 22; auction footnote sums to it); capex 1,31,769 / 1,31,107 /
1,44,271 (Q4 FY2025, Q4 FY2026 releases; FY2026 also in AR MD&A); USD 2.81 bn / 1.87 bn and Rs
447.27 crore (consolidated note 33.4 / 34; repeated in the auditors' KAM); LTIFR, 10 million GJ,
Net Carbon Zero 2035, Rs 75,000 crore, Rs 10 lakh crore (FY2025-26 AR only — single source,
company's own report); CSR 2,248 / 2,156 (consolidated cash-flow footnote).

**Gates:** check_sections, step14_diff, annotate_scorecard and delivery_audit results are
recorded in §17c of `Committee_Minutes_10Oct2026.md` and below.

## Appendix A — Step 1a pre-flight output (verbatim)

```
==============================================================================
PRE-FLIGHT  |  Reliance Industries Limited  |  agency CRISIL  |  9 documents, 435,980 words
==============================================================================

[0] DOCUMENTS BY DATE - READ THE NEWEST FIRST  (failure mode 26)
      ~2026  Media_Release_RIL_Q1_FY2026-27_Financial_and_Operational_Performan
      ~2025  RIL-Integrated-Annual-Report-2025-26.md
      ~2025  24042026_Media_Release_RIL_Q4_FY2025-26_Financial_and_Operational_
      ~2025  Media_Release_RIL_Q2_FY2025-26_Financial_and_Operational_Performan
      ~2025  Media_Release_RIL_Q3_FY2025-26_Financial_and_Operational_Performan
      ~2025  MediaRelease-RILQ1FY2025-26FinancialandOperationalPerformance.md
      ~2024  RIL-Integrated-Annual-Report-2024-25.md
      ~2024  25042025_Media_Release_RIL_Q4_FY2024_25_Financial_and_Operational_
    *** Newest content appears to be 2026. Any figure taken from an older
        document than this must be justified in the workpaper. ***

[0b] OPERATING METRICS ACROSS DOCUMENTS - ATTRIBUTE EACH TO ITS YEAR  (failure mode 30)
    !! cities/towns:
         ~2025  1,500                                    RIL-Integrated-Annual-Report-2025-26.md
         ~2025  1,000, 10, 6                             Media_Release_RIL_Q2_FY2025-26_Financial_and
         ~2025  1,300, 10, 26                            Media_Release_RIL_Q3_FY2025-26_Financial_and
         ~2025  26, 6                                    MediaRelease-RILQ1FY2025-26FinancialandOpera
         ~2024  1,000                                    RIL-Integrated-Annual-Report-2024-25.md
         ~2024  26, 300                                  25042025_Media_Release_RIL_Q4_FY2024_25_Fina
         ~2023  4, 5,900                                 RIL-Integrated-Annual-Report-2023-24.md
         ^^ SAME METRIC, DIFFERENT VALUES across documents. Quote the value from the
            NEWEST document, and state the SERIES if it moves - the direction is the finding.
    !! clients/customers:
         ~2026  396                                      Media_Release_RIL_Q1_FY2026-27_Financial_and
         ~2025  524                                      RIL-Integrated-Annual-Report-2025-26.md
         ~2025  387, 5.8                                 24042026_Media_Release_RIL_Q4_FY2025-26_Fina
         ~2025  5.8                                      Media_Release_RIL_Q2_FY2025-26_Financial_and
         ~2025  5.9                                      Media_Release_RIL_Q3_FY2025-26_Financial_and
         ~2024  349                                      RIL-Integrated-Annual-Report-2024-25.md
         ~2024  1.9, 6                                   25042025_Media_Release_RIL_Q4_FY2024_25_Fina
         ~2023  300                                      RIL-Integrated-Annual-Report-2023-24.md
         ^^ SAME METRIC, DIFFERENT VALUES across documents. Quote the value from the
            NEWEST document, and state the SERIES if it moves - the direction is the finding.

[0c] AGGREGATE-NOTE CONTAMINANTS - DECOMPOSE BEFORE USING A SUBTOTAL  (failure mode 36)
    none found - absence is EVIDENCED by this run, safe to state

[0d] SAME ITEM IN TWO STATEMENTS - CASH-FLOW ROW vs P&L NOTE  (failure mode 38)
    no cash-flow-vs-note conflict detected in the parsed tables

[0e] BALANCE-SHEET AGGREGATES - DECOMPOSE BEFORE USING A CAPTION
     Probe [0c] decomposes P&L notes. Nothing decomposed the BALANCE SHEET, and
     that is how Dhampur Bio Organics reported current borrowings of Rs 847.19
     crore as if it were all working capital, when Rs 82.68 crore of it was
     CURRENT MATURITIES OF LONG-TERM DEBT. Both numbers were in the extraction;
     neither was split. Long-term debt was understated by the same Rs 82.68 crore
     (206.98 reported against the agency's 290), and the working-capital number
     was overstated by it. Two different credit stories, one undecomposed caption.
    no decomposable balance-sheet caption detected in the parsed tables

[0f] PROMOTER / RELATED-PARTY UNSECURED LOANS  (failure mode 48, CRISIL only)
     no promoter/related-party unsecured loan line found in the parsed tables

[1] PRIOR RATING ACTION IN THE REFERENCE LIBRARY  (Step 14 / failure mode 24)
    *** PRESENT - Step 14 IS APPLICABLE. Open these AFTER forming your view, and
        produce a divergence table. You may NOT write 'no prior rating action'. ***
      - CRISIL: Reliance Industries Limited_30 Mar 2026_RR_392495.md
      - CareEdge: Reliance Communications Limited_02 Feb 2026.md
      - CareEdge: Reliance Industries Limited_03 Jul 2026.md
      - CareEdge: Reliance Infrastructure Limited_01 Apr 2025.md
      - ICRA: Reliance Communications Limited_17 Jul 2025_136393.md
      - ICRA: Reliance Industries Limited_29 Jan 2026_140636.md
      - ICRA: Reliance Power Limited_25 Nov 2025_139188.md

    >>> RATED AMOUNTS FOUND IN THE LIBRARY <<<
      Failure mode 29: never write 'to be confirmed by issuer' while a
      SAME-ISSUER line exists. Condition (1) is MET - the library counts.
      !! CONFIRM THE ENTITY FIRST. A PARENT, SIBLING OR PEER IS NOT THE
         ISSUER - importing a peer's rated amount is a WORSE error than
         leaving it TBC. [match n/m] = how many of the issuer's name
         tokens the filename carries. Highest score is the candidate;
         it still needs your confirmation that it is the same company.
      from Reliance Communications Limited_02 Feb 2026.md  [match 1/2]
        |Long-term bank facilities|9,322.00|CARE D; ISSUER NOT COOPERATING*|Rating continues to remain under ISS
        |Non-convertible debentures|750.00|CARE D; ISSUER NOT COOPERATING*|Rating continues to remain under ISSU
        |Short-term – Short-term instruments|2,880.00|CARE D; ISSUER NOT COOPERATING*|Rating continues to remain
      from Reliance Industries Limited_03 Jul 2026.md  [match 1/2]
        |Non-convertible debentures|6,500.00|CARE AAA; Stable|Reaffirmed|
        |Non-convertible debentures|5,500.00|CARE AAA; Stable|Reaffirmed|
        |Non-convertible debentures|20,000.00|CARE AAA; Stable|Reaffirmed|
        |Commercial Paper|34,500.00|CARE A1+|Reaffirmed|
      from Reliance Communications Limited_17 Jul 2025_136393.md  [match 1/2]
        |**Short Term-Fund Based-Cash Credit**|3365.00|3365.00|[ICRA]D ISSUER NOT COOPERATING*; Rating continues
        |**Non-convertible Debenture (NCD)** **Programme**|5000.00|5000.00|[ICRA]D ISSUER NOT COOPERATING*; Rati
        |**Long Term-Fund Based-Term Loan**|8658.00|8658.00|[ICRA]D ISSUER NOT COOPERATING*; Rating continues to
        |**Long Term-Non-Fund Based-Others**|6582.00|6582.00|[ICRA]D ISSUER NOT COOPERATING*; Rating continues t
        |**Short Term-Unallocated**|3949.00|3949.00|[ICRA]D ISSUER NOT COOPERATING*; Rating continues to remain 
        |**Long Term-Unallocated**|12876.00|12876.00|[ICRA]D ISSUER NOT COOPERATING*; Rating continues to remain
      from Reliance Industries Limited_29 Jan 2026_140636.md  [match 1/2]
        |**Non-convertible debentures**|3000|0.00|[ICRA]AAA (Stable); reaffirmed and withdrawn|
      from Reliance Power Limited_25 Nov 2025_139188.md  [match 1/2]
        |**Non-convertible debentures** **(NCD)**|250.00|250.00|[ICRA]D; reaffirmed|
        |**Long term/Short term non-fund-** **based limits**|146.00|145.00|[ICRA]D/[ICRA]D; reaffirmed|

[1b] PEER REPORTS - CRISIL, SAME SECTOR  (failure modes 32/33)
    * Minda Corporation Limited_09 Jun 2026_RR_398006.md   (score 12.0 on corporate+manufacturing+master)
        ratio footnote: *Includes securitisation transactions involving assignee payout, acquir
    * Orient Bell Limited_21 Apr 2026_RR_393300.md   (score 12.0 on corporate+manufacturing+master)
        ratio footnote: *Includes securitisation transactions involving assignee payout, acquir
    * Solex Energy Limited_12 May 2026_RR_395483.md   (score 12.0 on corporate+manufacturing+master)
        ratio footnote: *Includes securitisation transactions involving assignee payout, acquir
    *** These rows are the REQUIRED set, and the footnotes are the agency's
        RATIO DEFINITIONS. Reproduce them. A metric may be omitted only after
        checking a peer above - never by reasoning from another sector. ***
    PEER NORM over 20 peers: 0 carry a LONG-TERM rating, 12 a short-term rating.
    -> wrote peer_rows.json (0 rows from Minda Corporation Limited_09 Jun 2026_RR; peer norm 0/20 LT). check_sections.py VERIFIES both.

[1c] STEP 12 - THE FORWARD VIEW IS NOT OPTIONAL  (failure mode 35)
    entity_type 'corporate' -> required artefact:
      Full 5-yr 3-statement model (corporate with term debt).
    PLUS Step 12b: fill Rating_Scorecard_<Company>.xlsx from AUDITED ACTUALS.
    If a lighter treatment is right, record WHY in case.json as
    'step12_scaling_decision' - the delivery gate refuses the case without one.

[2] CREDIT-RATING NOTE in the issuer's own AR  (Step 7b)
    *** PRESENT - 39 match(es)
        If PRESENT you already know the outstanding rating - declare the anchor exposure and NEVER write 'no rating disclosed'.
        e.g. ...the Indian Rupee in the short to medium term. ### **Credit Rating** RIL continues to be rated two notches abov...
        e.g. ...OnenotchaboveIndia?s sovereign rating| |Long-Term Debt|CRISIL|AAA(Stable)|Highestrating by CRISIL| |Long-Term ...

[3] SUBSIDIARIES / entities to NAME  (failure mode 17)
    *** PRESENT - 1262 match(es)
        Every entity must be NAMED in the entities-consolidated annexure regardless of materiality.
        e.g. ...Company, world?s leading media company, for creating a joint venture which combines the businesses of Viacom 1...
        e.g. ...oss debt was at `C` 2,11,790 crore with balance in key subsidiaries including Reliance Retail ( `C` 41,317 cro...

[4] ESG data  (failure modes 19/20)
    *** PRESENT - 665 match(es)
        If PRESENT you may NOT write 'ESG data not extractable'. Extract and quote the numbers.
        e.g. ...**>1.7 Lakh** **New Hires** # **?1,592 Crore** **CSR Contribution** ### **Proud champion of Make In India...
        e.g. ...& Sustainability Responsibility Report (BRSR) Report (CSR)** <u>Click here Click here</u> **Reliance at a Glan...

[5] INSTRUMENT details  (Step 7b)
    *** PRESENT - 225 match(es)
        Populate Annexure I from these; mark only genuinely undisclosed amounts as TBC.
        e.g. ...on equivalent)** RIL issued `C` 20,000 crore 10-year nonconvertible debentures (NCD), marking the largest sing...
        e.g. ...The NCDs were issued at rates which were RIL?s lowest coupon ever and at the tightest spread over sovereign cr...

[6] CAPEX / investment cycle
    *** PRESENT - 103 match(es)
        Capital-intensive sectors: capex must appear in the rationale.
        e.g. ...olidated its balance sheet after the previous round of capex and is ready for the next level of growth. Our co...
        e.g. ...k-up in investment.** ### **Global Economy** ### **Capex** The Company achieved a consolidated revenue of `C`...

[7] SHAREHOLDING / promoter stake
    *** PRESENT - 92 match(es)
        Quantify the controlling stake - never write 'controlling shareholder' bare.
        e.g. ...LC *|United Arab<br>Emirates|53.68%|26|Columbus Centre Holding Company<br>LLC *|USA|100.00%| |4|Accops Systems...
        e.g. ...Distribution Services Limited|India|73.15%| |130|IPCO Holdings LLP *|United|51.33%|171 Meerut Cable Network Pr...

[8] AUDITOR opinion / KAM / Emphasis of Matter
    *** PRESENT - 149 match(es)
        An EOM or qualification is rating-relevant regardless of quantum (R13).
        e.g. ...e previous assurance practitioner who had expressed an unmodified opinion/conclusion on August 4, 2023. Our op...
        e.g. ...udit Qualification** The Company is in the regime of unmodified opinions on financial statements. ## **Reporti...

[9] SECTOR-DEFINING METRIC  (failure mode 21)
    sector detected (180 trigger hits; next best 'utilisation / EBITDA per tonne' at 111) -> the rationale MUST quote: receivable / GCA days
        ABSENT in documents - 0 match(es) -> confirm genuinely undisclosed
    !! ambiguous - verify the sector manually before relying on this

[10] METHODOLOGY TABLE INTEGRITY  (failure mode 49)
    !! CORRUPTED  Rating_of_Short_Term_Instruments_Feb_2025.md
       section 'CARE Ratings’ indicative mapping of short-term ratings to long-term ratings', 18 labelled row(s) with every data cell blank
       -> do NOT quote a threshold from this table; re-extract from a clean PDF

==============================================================================
Paste this into the workpaper Read Log. Anything marked PRESENT may NEVER be described
as 'not available' later without a second recorded search contradicting this one.
==============================================================================
```
