# Ashok Leyland Limited — Ratio Workpaper (ICRA)

**Prepared:** 10 Oct 2026 · **Agency style:** ICRA · **Engagement:** new assignment in this exercise
(fresh independent view; ICRA and CareEdge already rate the issuer — Step 14 applies) ·
**Data cutoff:** audited FY2026 (31-Mar-2026); latest interim in the case folder is H1 FY2026 ·
**Engine:** `compute_ratios.py` (166/166 tie-outs; mutation coverage 97.9%) ·
**Spreads:** `Ashok_Leyland_Financial_Spreads.xlsx` (generated from the engine, render-verified, 0 formula cells)

> Every figure in this workpaper is either copied from the engine's output (sections marked
> "engine") or quoted with its document location. Nothing is typed from memory or from a CRA
> publication (R1, R2, R6).

---

## 0. Independence and anchor exposure (declared)

Declared before any analysis, per R7/R16 and the HLE Glascoat lesson ("company rating
intimations ... may ENCLOSE the CRA rationale (anchor exposure — declare + mitigate)"):

| Exposure | How it happened | What was seen | Mitigation |
|---|---|---|---|
| Step 1a pre-flight probe [1] | Mechanical gate prints rated-amount lines of same-issuer actions | ICRA 02-Jun-2026: [ICRA]AA+ (Stable)/[ICRA]A1+ on the instrument lines; CareEdge 22-Sep-2025: CARE AA+; Stable / CARE A1+ | Rating view built bottom-up from computed metrics vs ICRA's indicative bands (Step 10 map) before any comparison |
| Issuer's own AR (Corporate Governance report §U) | Listed issuers disclose their ratings | The same grades from both agencies, as at the AR date | As above; the AR is a company document, so the *amounts* in §U are usable data |
| Step 7b extraction of ICRA's rated-amount table (FM29 makes this a Step 7b action) | My script cut at the first "Annexure I" string, which also occurs in a footnote near the top of the report, so the block over-ran | ICRA's analytical-approach row ("considered the consolidated financials of ALL"), its key-financial-indicators table, its rating history ([ICRA]AA (Stable) Oct-2023 → AA+ (Stable) from Sep-2024) and its Annexure II list | The analytical basis below was derived from ICRA 934 and coded into the engine **before** this read (engine docstring); the basis difference is argued at Step 14, not adopted. No figure from that report enters this workpaper except the rated-amount table under the 13-Aug-2026 five-condition amendment |

The Credit strengths/challenges, rationale text and sensitivities of the ICRA report were **not** read.

---

## 1. Step 1 — Input inventory, engagement type, information adequacy

| # | Document | Period | Status | Basis |
|---|---|---|---|---|
| 1 | AL_ANNUAL-REPORT-2026_Final.md | FY2025-26 (comparatives FY2024-25) | Audited — Price Waterhouse & Co Chartered Accountants LLP, unmodified, 28-May-2026 | Standalone + consolidated |
| 2 | Annual-Report-FY-2024-25_1.md | FY2024-25 (comparatives FY2023-24, restated) | Audited — PwC, unmodified, 23-May-2025 | Standalone + consolidated |
| 3 | Annual-Report-FY-2023-24-1.md | FY2023-24 (comparatives FY2022-23) | Audited — PwC, unmodified, 24-May-2024 | Standalone + consolidated |
| 4 | ALOutcomeofBMNov122025final.md | Q2 / H1 FY2026 (to 30-Sep-2025) | Limited review, 12-Nov-2025 | Standalone + consolidated |
| 5 | ALResultsjune2025.md | Q1 FY2026 (to 30-Jun-2025) | Limited review, 14-Aug-2025 | Standalone + consolidated |
| 6 | un-audited-financial-results-for-the-quarter-ended-September-30-2024.md | Q2 / H1 FY2025 | Limited review, 08-Nov-2024 | Standalone + consolidated |
| 7 | un-audited-financial-results-for-the-quarter-ended-June-30-2024.md | Q1 FY2025 | Limited review, 25-Jul-2024 | Standalone + consolidated |

**Missing (per the request):** (a) instrument term sheets / sanction letters — handled at Step 7b:
the company's own AR discloses the rated instruments and amounts (§U), the NCD's ISIN, coupon and
maturity, and the same-issuer ICRA rated-amount table (02-Jun-2026) is imported under the
five-condition amendment; lender-wise sanctioned limits remain **to be confirmed by issuer**.
(b) Sector-assumptions note — not provided; the base case uses the company's own MD&A outlook
("FY27 is expected to mark a year of disciplined, consolidation-led growth", FY2026 AR MD&A §C) and
its own history, source-labelled, with a stress case. (c) Any result after 31-Mar-2026 (Q1 FY2027)
— not provided; data cutoff is the FY2026 audit; the latest event in the documents is the
re-appointment of the Executive Chairman on 28-May-2026 (FY2026 AR notice).

**Engagement type:** new assignment in this exercise (R15). **Mandate scope:** the ICRA-rated
programme — long-term (with outlook) and short-term instruments: fund-based and non-fund-based
LT/ST limits, term loans, LT/ST unallocated, commercial paper, NCD and proposed NCD (Step 7b).
**Information adequacy:** adequate — three audited annual reports, four reviewed interims, listed
issuer with full segment and subsidiary disclosure; no INC route.

---

## 2. Step 1a — Pre-flight (verbatim output in `_preflight_output.txt`)

Present: two same-issuer prior actions (ICRA 02-Jun-2026; CareEdge 22-Sep-2025); the AR's own
credit-rating note (65 matches); subsidiaries to name (1,619 matches); ESG data (646); instrument
details (129); capex (87); shareholding (7); auditor opinion/KAM (182).
Flags acted on: **[0c]** aggregate-note contaminants — every component carries a written decision in
§5.2; **[0e]** balance-sheet aggregates — current maturities inside current borrowings, supplier
finance, earmarked bank balances and lease liabilities each split in §5.3; **[1b]** the peer match
(NMDC, Reliance Power) and **[9]** the sector-metric guess ("EBITDA per tonne") are wrong for a CV OEM
— overridden: peers chosen manually at Step 4, sector metrics = volumes, market share, capacity
utilisation (ICRA 1006 "Scale, market position and brand strength"); **[10]** the CareEdge LT-ST
table corruption does not affect an ICRA case.
Absence claims made in this workpaper, each backed by a recorded search: no pledge of promoter
shares disclosed (grep `pledg|encumb` over all three ARs — only the auditor's CARO statement that
no loans were raised on pledged subsidiary securities); no auditor qualification, emphasis of matter
or material uncertainty (the three audit reports are unmodified).

---

## 3. Step 1b — Document Read Log

Method: `icra-doc-extract` section map for the three ARs (statements, notes, segment, borrowings,
investments, contingent liabilities, related parties, KAMs, governance, MD&A, chairman's letter,
subsidiary list/Schedule III); the four quarterly filings read end-to-end.

| # | Document | What it is | Key facts (location) | Material items |
|---|---|---|---|---|
| 1 | FY2026 AR | Audited annual report | Standalone revenue Rs 44,007.03 crore, PAT 3,565.53 (p123); consolidated total income 56,946.90 (p221); segment note 3.8 (p310); vehicles 220,437 (ten-year table p6); M&HCV share 30.3% (MD&A); net cash Rs 5,899 crore (chairman) | Labour Codes exceptional (348.48 standalone, 384.44 consolidated, note 2.8); KAM on Optare-group investment Rs 3,129.83 crore; HLF ECL KAM (gross loans 49,156.66, ECL 1,279.86); Switch UK manufacturing discontinued (Board's report); HLF-NDL merger (RBI NOC, CCI approval, BSE NOC 18-May-2026); ICDs to promoter-group companies, max Rs 670 crore in aggregate (note 3.9.1); guarantees for subsidiaries Rs 785.71 crore (note 3.9.2); ELV/EPR obligation not estimable (note 3.9 note 2) |
| 2 | FY2025 AR | Audited annual report | Standalone revenue 38,752.74, PAT 3,303.29 (p113); FY2024 restated comparatives (p208); M&HCV share 30.7%; net cash Rs 4,242 crore and "net debt of Rs 89 crores the previous year" (chairman) | Rs 200 crore into HLF and Rs 498.76 crore into Optare (Board's report); HEIL fair-value gain 120.53 (exceptional); guarantees 1,021.58; ICDs to promoter-group companies, max 70 each to seven entities |
| 3 | FY2024 AR | Audited annual report | Standalone revenue 38,367.03, PAT 2,617.87 (p117); FY2023 comparatives; M&HCV share 31.1% (31.8% FY2023); bus share 33.8% (28.0%) | Rs 1,200 crore into Optare and Rs 299.99 crore into OHM (Board's report); interim dividend Rs 1,453.48 crore held in a designated account at year-end (note 1.11B); NCD Series 3 ISIN INE208A07406 (CG report) |
| 4 | Q2 FY2026 filing | Board outcome + reviewed results | H1 FY2026 standalone PBT before exceptional 1,880.39 (vs 1,579.89); consolidated ratios "excluding financial services segment": debt-equity 0.64x, ISCR 13.37x | Rs 40 crore litigation provision (exceptional); term loan Rs 345.63 crore for an asset in CWIP (security cover note); RBI NOC for HLF-NDL merger 08-Aug-2025; bonus 1:1 |
| 5 | Q1 FY2026 filing | Reviewed results + press release | Record Q1: 44,238 vehicles, revenue Rs 8,725 crore, EBITDA Rs 970 crore (11.1%), PAT Rs 594 crore, cash positive Rs 821 crore | OCR misread of standalone PBT (191.13 printed; Q2 filing's comparative 797.73 governs) |
| 6 | Q2 FY2025 filing | Reviewed results + press release | PAT Rs 770 crore; EBITDA 11.6%; domestic M&HCV share "over 31%"; interim dividend Rs 2/share | Hinduja Tech to acquire 100% of TECOSIM Group GmbH; HEIL gain 120.53 |
| 7 | Q1 FY2025 filing | Reviewed results + press release | Q1 FY2025 vehicles 43,893 ("highest ever CV volumes of 43893 units"); EBITDA Rs 911 crore (10.6%); domestic M&HCV share 30.7%, bus 33.3%; domestic LCV 15,345 units; security-cover statement for the Rs 200 crore Series 3 NCD | Management target "mid-teen EBITDA in the medium term" |

**Corroboration register (traced ≠ verified):**

| Figure | Source 1 | Source 2 | Result |
|---|---|---|---|
| Standalone OPBDITA FY2024/25/26 | Engine: 4,606.58 / 4,930.56 / 5,732.25 | Chairman's letters: 4,607 / 4,931 / 5,732; screener.in 4,607 / 4,931 / 5,732 | Agree (tie-outs) |
| Standalone net cash FY2025/26 | Engine rebuild: 4,242.93 / 5,901.72 | Chairman: 4,242 / 5,899 | Agree within EIR rounding (tie-out) |
| Total vehicles FY2024/25/26 | Ten-year table | Domestic M&HCV + domestic LCV + exports (MD&A/chairman) | Exact (tie-out) |
| Domestic M&HCV share FY2026 | MD&A 30.3% | Chairman's letter 30.8% | **Diverge 0.5 pp** — MD&A series (31.8/31.1/30.7/30.3) used; gap recorded |
| Consolidated borrowings FY2023-26 | Engine 31,160.93 → 63,935.70 | screener.in 31,161 → 63,936 | Agree |
| FY2024 consolidated other income | FY2024 AR: 140.58 | FY2025 AR comparative: 227.88 | Restatement of Rs 87.30 crore (FS revenue → other income); restated figure used |
| Equity into Optare FY2025-26 | Investment note: cost 2,130.89 → 3,000.23 | Board's report: 498.76 (FY2025 application money) + 370.58 (FY2026) = 869.34 | Exact |

**Trends (multi-year direction, not snapshots):** total vehicles 192,205 → 220,437 (FY2023-FY2026,
+14.7%), within a ten-year series that fell from 197,366 (FY2019) to 100,725 (FY2021) — a 49% peak
-to-trough contraction with a standalone loss of Rs 314 crore in FY2021 (ten-year table);
standalone OPBDITA margin 8.11% → 12.01% → 12.72% → 13.03%; domestic M&HCV share eroding
31.8% → 31.1% → 30.7% → 30.3% (trucks 32.3% FY2023 → 30.0% FY2026) while bus share rose 28.0% →
33.8% → 34.1%; exports 11,853 → 15,255 → 18,082 units; standalone net debt Rs 132 crore (FY2024)
→ net cash Rs 5,856 crore (FY2026, engine); non-financial subsidiaries' borrowings 1,879.89 →
1,607.50 → 2,418.99 → 3,538.63 (engine); HLF's share of group borrowings 83.6% → 92.6% (engine).

---

## 4. Steps 2-4 — Routing, methodology, peers

**Route (ICRA):** `960~Corporate Credit Rating Methodology, Jul 2025` + `1006~Commercial Vehicles,
Rating Methodology, Dec 2025` (scope: "ICRA's approach to assessing the business and financial
risk profiles of CV original equipment manufacturers" — matches); cross-cutting
`934~Rating Approach, Consolidation, Nov 2024` (basis); conventions file `ICRA/ICRA_CONVENTIONS.md`
(operating profit §1, leverage §3, coverage §4, LT-ST §12). All three methodology files and the
conventions file read in full this session.

**Indicative bands extracted (identical in 960 and 1006):**

| Ratio | Strongest | Weakest | Source |
|---|---|---|---|
| RoCE | ≥25% | <10% | 1006 / 960 "Validation of Business Risk through Profitability Metrics" |
| Volatility in RoCE | ≤10% | >55% | same |
| Indebtedness ratio (TOL/TNW) | ≤0.9x | >3.0x | "Assessment of Leverage" (picture-text block in 1006; table in 960) |
| Debt-to-profit (Total debt/OPBDITA) | ≤0.5x | >5.0x | same |
| Interest coverage | ≥18.0x | <2.0x | "Assessment of Coverage" |
| DSCR | ≥4.0x | <1.1x | same |

**Unreadable / absent:** 1006 "Summary of the Salient Business Risk Factors" — no table survives
conversion (no picture text either); no business-risk band is invented. 1006/960 liquidity
"snapshot" is a sources-vs-uses diagram, not a threshold table.

**Peer set (craft and calibration only — R2):** Mahindra & Mahindra (ICRA, 29-Sep-2025) — auto OEM
with a captive NBFC; its analytical approach states ICRA "considered the consolidated financials of
M&M excluding the financial services business ... However, the analysis considers the ordinary
and extraordinary funding support likely to be extended by M&M to MMFSL" — the same structure as
ICRA 934's dissimilar-business rule applied here; SML Mahindra (ICRA, 28-Nov-2025) — CV OEM; Eicher
Motors (ICRA, 11-Dec-2025) — auto OEM with a CV JV. Calibration read: ICRA's AAA peers combine
dominant or diversified franchises with very large liquidity; SML's AA+ rests on its AAA parent.
Format learned: summary table → Rationale (outlook paragraph last) → Key rating drivers (Credit
strengths / Credit challenges, bold headline + dash) → Environmental and Social Risks → Liquidity
position: [descriptor] → Rating sensitivities → Analytical approach table → About the company →
Key financial indicators (Operating income, PAT, OPBDIT/OI, PAT/OI, TOL/TNW, Total debt/OPBDIT,
Interest coverage) → Status of non-cooperation → Rating history → Complexity → Annexure I/II.

---

## 5. Step 5 — Extraction, basis, normalisation

### 5.1 Analytical basis (R12 — methodology-determined)
ICRA 934, "Approach for consolidated analysis when a parent and its subsidiary are in dissimilar
businesses": *"In case the parent is a non-financial sector entity with a subsidiary in the
financial sector (such as the captive finance arm of an automobile manufacturer) ... the parent and
its subsidiary are assessed separately on a standalone basis by applying the rating methodology of
their respective sectors. The standalone analysis, however, does consider the ongoing and future
funding interchange (including the likely extraordinary support) among them."* And for entities
excluded from consolidation, the "Limited Consolidation" approach factors in "the ongoing and future
expected/committed cash outflows from the parent towards the 'excluded' subsidiaries".

Applied: **basis = consolidated excluding the financial-services subsidiaries** (the automotive
business). HLF, a dissimilar business, is assessed separately, with its expected funding needs
factored into AL's cash flows; AL and its CV-related subsidiaries (Optare/Switch, OHM, Hinduja
Tech, Albonair and others) are analysed together. This is the construction of ICRA's own M&M
rationale ("consolidated financials of M&M excluding the financial services business ... the
analysis considers the ordinary and extraordinary funding support"). Because the segment note gives
the CV segment's PBIT but not its depreciation, the automotive view is measured two ways (engine
table B): segment-based metrics at the low OPBDITA bound, and standalone OPBDITA set against
standalone plus non-financial-subsidiary debt (non-financial debt derived exactly from notes
1.20/1.26). **AL standalone** — the rated entity, 91% of automotive revenue (44,007.03 /
48,313.71) — carries the full ratio suite (engine table A) and is reported alongside, as ICRA's
key-financial-indicator tables do. The reported consolidated view, in which HLF carries 92.6% of
group borrowings, is a supplement and never relied on. The company itself reports consolidated
debt-equity and coverage "excluding financial services segment" (Q2 FY2026 filing), which
corroborates the separation. This matches the case file's "consolidated" declaration in
substance; the exclusion of HLF is the methodology's, stated here, not a silent override (R12).

### 5.2 Operating-profit normalisation (pre-flight [0c] — written decision per component)
ICRA OPBDITA = revenue from operations − cost of goods sold − employee cost − other expenses
(ICRA 960 footnote 5; conventions §1). Engine output equals the company's published EBITDA to the
crore (tie-outs), which validates the definition.

| Component (pre-flight [0c]) | Where it sits | Decision |
|---|---|---|
| Interest income 66.92; dividend 6.01 (FY2026) | Other income | **Excluded** — ICRA: "not considered under operating income though they might be recurring" |
| Profit on sale of investments 92.83; FVTPL gain 26.61; profit on sale of PPE 43.15; others 79.65 | Other income | **Excluded** — non-core |
| Exceptional items (note 2.8): FY2026 Labour Codes (308.48) + litigation provision (40.00) = (348.48); FY2025 HEIL fair-value gain 120.53, Ashley Aviation impairment (3.20), CWIP/intangibles write-off (13.60) = 103.73 | Below operating profit | **Excluded** from OPBDITA; reported PAT kept as reported in KFI |
| Forex gain 4.08 (standalone FY2026 cash-flow adjustment) | Within other income/expenses | Immaterial (<1% TNW, <5% PBT); no adjustment |
| Export incentives 70.68-71.89 | Revenue from operations (other operating revenue) | **Retained** — core (ICRA retains duty drawback) |
| Electoral-trust contribution Rs 108 crore (FY2026; Rs 100 crore FY2025) | Other expenses (miscellaneous) | **Retained in costs** — conservative; disclosed |
| Unwinding of discount on warranty provisions 95.69 | Finance costs | Retained in interest (conservative for coverage) |
| Consolidated "impairment relating to financing activities" 1,234.24 | FS segment cost | Consolidated supplement only |

### 5.3 Balance-sheet splits (pre-flight [0e])
Current borrowings FY2026 Rs 633.82 crore = short-term bank loans 150.00 + current maturities of
long-term debt 483.82 (note 1.21; includes the NCD falling due 17-Mar-2027). Supplier-finance
liabilities 87.25 (consolidated note 1.26) are inside consolidated borrowings and therefore inside
debt. Lease liabilities are added to debt (ICRA 960 definition). Earmarked bank balances (unclaimed
dividend 13.35, escrow 32.61 in FY2026; plus the Rs 1,453.48 crore interim-dividend account in
FY2024) are excluded from liquidity. Of the FY2026 Rs 900 crore of 3-12 month deposits, the note
1.11B footnote says it "Includes fixed deposit of Rs. 100 crores (2024-25: Nil) ... towards meeting
Debenture Redemption Fund requirements": that Rs 100 crore is usable only for the NCD due
17-Mar-2027, so it is excluded from free liquidity and set only against that redemption at Step 11
(ICRA_CONVENTIONS §3 fn 2, §8); the other Rs 800 crore is free. Total debt is kept gross
(Rs 1,195.04 crore, tying to the AR and screener.in); netting the DRF deposit per ICRA's formula
would give Rs 1,095.04 crore — 0.76% of TNW, below the R13 threshold (engine
DISCLOSED_DIFFERENCES). FY2024 current investments include Rs 23.90 crore of subsidiary
preference shares — excluded as non-liquid.

---

## 6. Step 6 — Ratio suite, tie-out, coverage (engine)

**A. AL standalone (the rated entity) - ICRA ratio suite (Rs crore)**

| Metric | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|---:|
| Operating income | 36,144.14 | 38,367.03 | 38,752.74 | 44,007.03 |
| Revenue growth (%) | - | 6.15 | 1.01 | 13.56 |
| OPBDITA | 2,930.70 | 4,606.58 | 4,930.56 | 5,732.25 |
| OPBDITA margin (%) | 8.11 | 12.01 | 12.72 | 13.03 |
| PBIT (operating) | 2,198.74 | 3,888.77 | 4,211.22 | 5,017.06 |
| PBIT margin (%) | 6.08 | 10.14 | 10.87 | 11.40 |
| PAT | 1,380.11 | 2,617.87 | 3,303.29 | 3,565.53 |
| PAT margin (%) | 3.82 | 6.82 | 8.52 | 8.10 |
| Total debt | 3,224.83 | 2,299.40 | 1,481.72 | 1,195.04 |
| Tangible net worth | 8,425.80 | 8,810.37 | 11,518.79 | 13,113.42 |
| Total outside liabilities | 14,165.83 | 14,801.38 | 14,007.04 | 15,480.24 |
| Gearing (x) | 0.38 | 0.26 | 0.13 | 0.09 |
| TOL/TNW (x) | 1.68 | 1.68 | 1.22 | 1.18 |
| Total debt/OPBDITA (x) | 1.10 | 0.50 | 0.30 | 0.21 |
| Interest coverage (x) | 10.14 | 18.47 | 22.73 | 33.77 |
| DSCR (x) | 3.61 | 2.65 | 4.68 | 8.10 |
| RoCE (%) | - | 32.85 | 33.90 | 35.96 |
| NCA (PAT + D&A - dividend) | 1,818.52 | 2,572.29 | 1,981.86 | 2,445.30 |
| Free cash and liquid investments | 3,225.53 | 2,167.03 | 5,678.52 | 6,950.80 |
| Net debt (negative = net cash) | -0.70 | 132.37 | -4,196.80 | -5,755.76 |
| Net debt/OPBDITA (x) | -0.00 | 0.03 | -0.85 | -1.00 |
| Current ratio (x) | 1.05 | 0.96 | 1.08 | 1.10 |
| Debtor days | 41.02 | 33.96 | 27.19 | 24.47 |
| Inventory days | 36.36 | 41.72 | 39.08 | 40.50 |
| Payable days | 94.04 | 82.45 | 96.52 | 96.77 |
| CFO | 2,136.01 | 2,503.12 | 7,819.42 | 4,792.10 |
| RCF (CFO - dividend) | 1,842.46 | 1,739.73 | 5,778.65 | 2,956.68 |
| FCF (RCF - capex - repayments) | 964.47 | 139.25 | 4,135.63 | 1,527.55 |
| Capex/OI (%) | 1.39 | 1.29 | 2.46 | 2.38 |
| Support to subsidiaries (equity) | 19.81 | 1,567.02 | 717.06 | 386.28 |

**B. METHODOLOGY BASIS - automotive business = consolidated EXCLUDING financial services (ICRA 934; HLF assessed separately)**

| Metric | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|---:|
| AUTO CV revenue | 38,024.72 | 40,956.35 | 42,333.28 | 48,313.71 |
| AUTO CV PBIT margin (%) | 4.78 | 8.83 | 8.71 | 9.06 |
| AUTO OPBDITA low (CV PBIT + standalone D&A) | 2,551.36 | 4,332.49 | 4,408.31 | 5,094.51 |
| AUTO OPBDITA high (CV PBIT + consolidated D&A) | 2,719.62 | 4,541.97 | 4,775.62 | 5,516.88 |
| AUTO total debt | 5,300.48 | 4,099.87 | 4,115.44 | 4,976.23 |
| AUTO non-FS subsidiary borrowings | 1,879.89 | 1,607.50 | 2,418.99 | 3,538.63 |
| AUTO debt/OPBDITA at low bound (x) | 2.08 | 0.95 | 0.93 | 0.98 |
| AUTO interest coverage at low bound (x) | 6.77 | 10.15 | 11.10 | 11.96 |
| AUTO net assets (CV segment) | 5,286.97 | 4,718.21 | 6,969.29 | 7,892.63 |
| AUTO gearing on CV net assets (x) | 1.00 | 0.87 | 0.59 | 0.63 |
| ADJ standalone debt + non-FS subsidiary debt / standalone OPBDITA (x) | 1.74 | 0.85 | 0.79 | 0.83 |
| ADJ net debt incl. non-FS subsidiary debt (negative = net cash) | 1,879.19 | 1,739.87 | -1,777.81 | -2,217.13 |

**C. Reported consolidated incl. Hinduja Leyland Finance (supplementary only)**

| Metric | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|---:|
| CONS operating income | 41,672.60 | 45,703.34 | 48,535.14 | 56,362.08 |
| CONS PAT | 1,358.82 | 2,696.34 | 3,382.79 | 3,720.98 |
| CONS total debt | 31,160.93 | 40,802.18 | 49,962.11 | 63,935.70 |
| CONS TNW (incl. NCI) | 10,795.81 | 11,814.59 | 15,844.86 | 18,546.24 |
| CONS TOL/TNW (x) | 4.07 | 4.73 | 4.16 | 4.45 |
| CONS total debt/OPBDITA (x) | 6.12 | 5.19 | 5.43 | 5.95 |
| CONS FS share of group borrowings (%) | 83.64 | 90.48 | 92.24 | 92.63 |

**D. Operating and support series**

| Metric | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|---:|
| Total vehicle volume | 192,205.0 | 194,555.0 | 195,097.0 | 220,437.0 |
| M&HCV market share (%) | 31.8 | 31.1 | 30.7 | 30.3 |
| Corporate guarantees for subsidiaries | 892.7 | 762.2 | 1,021.6 | 785.7 |

**E. Tie-out register (186/186 reconcile)**

| # | Check | Computed | Disclosed | Tol | Result | Source |
|---|---|---:|---:|---:|---|---|
| 1 | FY2026 non-current borrowings = term loans NC + sales-tax loans NC | 517.88 | 517.88 | 0.01 | PASS | borrowings repayment schedule vs balance sheet |
| 2 | FY2026 current maturities = term loans + NCD + sales-tax loans (current) | 484.16 | 483.82 | 0.50 | PASS | schedule is at face value; note 1.21 at amortised cost (EIR residual 0.34) |
| 3 | FY2026 current borrowings = short-term bank loans + current maturities | 633.82 | 633.82 | 0.01 | PASS | note 1.21 |
| 4 | FY2026 long-term borrowings (Board's report) = term loans + NCD + sales-tax loans | 1,002.04 | 1,002.04 | 0.01 | PASS | Board's report: 'long term borrowings stood at Rs 1,002.04 crores' |
| 5 | Revenue mix: product lines = sale-of-products subtotal, FY2023 | 35,467.10 | 35,467.10 | 0.01 | PASS | note 2.1 / 3.7.1 |
| 6 | Revenue mix: products + services + other - rebates = contract revenue, FY2023 | 36,096.60 | 36,096.60 | 0.01 | PASS | note 3.7.1 |
| 7 | Revenue mix: India + outside India = contract revenue, FY2023 | 36,096.60 | 36,096.60 | 0.01 | PASS | note 3.7.1 geography |
| 8 | Revenue mix: contract revenue + export incentives/grant = revenue from operations, FY2023 | 36,144.14 | 36,144.14 | 0.01 | PASS | note 2.1 vs P&L |
| 9 | SA total income = revenue + other income, FY2023 | 36,260.28 | 36,260.28 | 0.01 | PASS | standalone P&L, Total Income row |
| 10 | SA cost of goods sold = materials + purchases + inventory change, FY2023 | 27,849.15 | 27,849.15 | 0.01 | PASS | standalone P&L, printed subtotal |
| 11 | SA total expenses (sum of lines), FY2023 | 34,234.49 | 34,234.49 | 0.01 | PASS | standalone P&L, Total Expenses row |
| 12 | SA profit before exceptional & tax, FY2023 | 2,025.79 | 2,025.79 | 0.01 | PASS | standalone P&L |
| 13 | SA profit before tax, FY2023 | 2,110.40 | 2,110.40 | 0.01 | PASS | standalone P&L |
| 14 | SA profit after tax, FY2023 | 1,380.11 | 1,380.11 | 0.01 | PASS | standalone P&L |
| 15 | SA non-current assets (sum of lines), FY2023 | 10,888.01 | 10,888.01 | 0.02 | PASS | standalone balance sheet |
| 16 | SA current assets (sum of lines), FY2023 | 11,631.70 | 11,631.70 | 0.02 | PASS | standalone balance sheet |
| 17 | SA total assets, FY2023 | 22,591.63 | 22,591.63 | 0.02 | PASS | standalone balance sheet |
| 18 | SA total equity = share capital + other equity, FY2023 | 8,425.80 | 8,425.80 | 0.01 | PASS | standalone balance sheet |
| 19 | SA non-current liabilities (sum of lines), FY2023 | 3,093.03 | 3,093.03 | 0.02 | PASS | standalone balance sheet |
| 20 | SA current liabilities (sum of lines), FY2023 | 11,061.93 | 11,061.93 | 0.02 | PASS | standalone balance sheet |
| 21 | SA balance sheet balances: assets = equity + liabilities, FY2023 | 22,591.63 | 22,591.63 | 0.02 | PASS | standalone balance sheet |
| 22 | SA cash in AR net-debt bridge = balance-sheet cash, FY2023 | 454.11 | 454.11 | 0.01 | PASS | standalone net debt reconciliation |
| 23 | SA liquid investments = AR bridge liquid investments, FY2023 | 2,771.42 | 2,771.42 | 0.01 | PASS | standalone net debt reconciliation (FY2024 differs from the balance sheet by Rs 23.90 crore of subsidiary preference shares - removed as non-liquid) |
| 24 | CONS segment results bridge to reported PBT, FY2023 | 2,264.93 | 2,264.93 | 0.02 | PASS | consolidated segment note 3.8 vs consolidated P&L |
| 25 | CONS segment assets sum to total assets, FY2023 | 54,746.01 | 54,746.01 | 0.02 | PASS | segment note vs consolidated balance sheet |
| 26 | CONS segment net assets = total equity, FY2023 | 10,795.81 | 10,795.81 | 0.02 | PASS | segment note vs balance sheet |
| 27 | CONS PBT = pre-JV PBT + JV share + exceptional, FY2023 | 2,264.93 | 2,264.93 | 0.02 | PASS | consolidated P&L |
| 28 | Revenue mix: product lines = sale-of-products subtotal, FY2024 | 37,699.43 | 37,699.43 | 0.01 | PASS | note 2.1 / 3.7.1 |
| 29 | Revenue mix: products + services + other - rebates = contract revenue, FY2024 | 38,323.49 | 38,323.49 | 0.01 | PASS | note 3.7.1 |
| 30 | Revenue mix: India + outside India = contract revenue, FY2024 | 38,323.49 | 38,323.49 | 0.01 | PASS | note 3.7.1 geography |
| 31 | Revenue mix: contract revenue + export incentives/grant = revenue from operations, FY2024 | 38,367.03 | 38,367.03 | 0.01 | PASS | note 2.1 vs P&L |
| 32 | SA total income = revenue + other income, FY2024 | 38,613.60 | 38,613.60 | 0.01 | PASS | standalone P&L, Total Income row |
| 33 | SA cost of goods sold = materials + purchases + inventory change, FY2024 | 27,912.01 | 27,912.01 | 0.01 | PASS | standalone P&L, printed subtotal |
| 34 | SA total expenses (sum of lines), FY2024 | 34,727.70 | 34,727.70 | 0.01 | PASS | standalone P&L, Total Expenses row |
| 35 | SA profit before exceptional & tax, FY2024 | 3,885.90 | 3,885.90 | 0.01 | PASS | standalone P&L |
| 36 | SA profit before tax, FY2024 | 3,792.18 | 3,792.18 | 0.01 | PASS | standalone P&L |
| 37 | SA profit after tax, FY2024 | 2,617.87 | 2,617.87 | 0.01 | PASS | standalone P&L |
| 38 | SA non-current assets (sum of lines), FY2024 | 11,948.66 | 11,948.66 | 0.02 | PASS | standalone balance sheet |
| 39 | SA current assets (sum of lines), FY2024 | 11,597.07 | 11,597.07 | 0.02 | PASS | standalone balance sheet |
| 40 | SA total assets, FY2024 | 23,611.75 | 23,611.75 | 0.02 | PASS | standalone balance sheet |
| 41 | SA total equity = share capital + other equity, FY2024 | 8,810.37 | 8,810.37 | 0.01 | PASS | standalone balance sheet |
| 42 | SA non-current liabilities (sum of lines), FY2024 | 2,746.18 | 2,746.18 | 0.02 | PASS | standalone balance sheet |
| 43 | SA current liabilities (sum of lines), FY2024 | 12,038.37 | 12,038.37 | 0.02 | PASS | standalone balance sheet |
| 44 | SA balance sheet balances: assets = equity + liabilities, FY2024 | 23,611.75 | 23,611.75 | 0.02 | PASS | standalone balance sheet |
| 45 | SA cash in AR net-debt bridge = balance-sheet cash, FY2024 | 1,941.87 | 1,941.87 | 0.01 | PASS | standalone net debt reconciliation |
| 46 | SA liquid investments = AR bridge liquid investments, FY2024 | 225.16 | 225.16 | 0.01 | PASS | standalone net debt reconciliation (FY2024 differs from the balance sheet by Rs 23.90 crore of subsidiary preference shares - removed as non-liquid) |
| 47 | CONS segment results bridge to reported PBT, FY2024 | 4,106.07 | 4,106.07 | 0.02 | PASS | consolidated segment note 3.8 vs consolidated P&L |
| 48 | CONS segment assets sum to total assets, FY2024 | 67,660.46 | 67,660.46 | 0.02 | PASS | segment note vs consolidated balance sheet |
| 49 | CONS segment net assets = total equity, FY2024 | 11,814.59 | 11,814.59 | 0.02 | PASS | segment note vs balance sheet |
| 50 | CONS PBT = pre-JV PBT + JV share + exceptional, FY2024 | 4,106.07 | 4,106.07 | 0.02 | PASS | consolidated P&L |
| 51 | Revenue mix: product lines = sale-of-products subtotal, FY2025 | 38,124.00 | 38,124.00 | 0.01 | PASS | note 2.1 / 3.7.1 |
| 52 | Revenue mix: products + services + other - rebates = contract revenue, FY2025 | 38,702.65 | 38,702.65 | 0.01 | PASS | note 3.7.1 |
| 53 | Revenue mix: India + outside India = contract revenue, FY2025 | 38,702.65 | 38,702.65 | 0.01 | PASS | note 3.7.1 geography |
| 54 | Revenue mix: contract revenue + export incentives/grant = revenue from operations, FY2025 | 38,752.74 | 38,752.74 | 0.01 | PASS | note 2.1 vs P&L |
| 55 | SA total income = revenue + other income, FY2025 | 39,002.99 | 39,002.99 | 0.01 | PASS | standalone P&L, Total Income row |
| 56 | SA cost of goods sold = materials + purchases + inventory change, FY2025 | 27,622.78 | 27,622.78 | 0.01 | PASS | standalone P&L, printed subtotal |
| 57 | SA total expenses (sum of lines), FY2025 | 34,758.43 | 34,758.43 | 0.01 | PASS | standalone P&L, Total Expenses row |
| 58 | SA profit before exceptional & tax, FY2025 | 4,244.56 | 4,244.56 | 0.01 | PASS | standalone P&L |
| 59 | SA profit before tax, FY2025 | 4,348.29 | 4,348.29 | 0.01 | PASS | standalone P&L |
| 60 | SA profit after tax, FY2025 | 3,303.29 | 3,303.29 | 0.01 | PASS | standalone P&L |
| 61 | SA non-current assets (sum of lines), FY2025 | 13,193.53 | 13,193.53 | 0.02 | PASS | standalone balance sheet |
| 62 | SA current assets (sum of lines), FY2025 | 12,308.62 | 12,308.62 | 0.02 | PASS | standalone balance sheet |
| 63 | SA total assets, FY2025 | 25,525.83 | 25,525.83 | 0.02 | PASS | standalone balance sheet |
| 64 | SA total equity = share capital + other equity, FY2025 | 11,518.79 | 11,518.79 | 0.01 | PASS | standalone balance sheet |
| 65 | SA non-current liabilities (sum of lines), FY2025 | 2,576.26 | 2,576.26 | 0.02 | PASS | standalone balance sheet |
| 66 | SA current liabilities (sum of lines), FY2025 | 11,426.13 | 11,426.13 | 0.02 | PASS | standalone balance sheet |
| 67 | SA balance sheet balances: assets = equity + liabilities, FY2025 | 25,525.83 | 25,525.83 | 0.02 | PASS | standalone balance sheet |
| 68 | SA cash in AR net-debt bridge = balance-sheet cash, FY2025 | 2,659.82 | 2,659.82 | 0.01 | PASS | standalone net debt reconciliation |
| 69 | SA liquid investments = AR bridge liquid investments, FY2025 | 3,018.70 | 3,018.70 | 0.01 | PASS | standalone net debt reconciliation (FY2024 differs from the balance sheet by Rs 23.90 crore of subsidiary preference shares - removed as non-liquid) |
| 70 | CONS segment results bridge to reported PBT, FY2025 | 4,596.33 | 4,596.33 | 0.02 | PASS | consolidated segment note 3.8 vs consolidated P&L |
| 71 | CONS segment assets sum to total assets, FY2025 | 81,714.64 | 81,714.64 | 0.02 | PASS | segment note vs consolidated balance sheet |
| 72 | CONS segment net assets = total equity, FY2025 | 15,844.86 | 15,844.86 | 0.02 | PASS | segment note vs balance sheet |
| 73 | CONS PBT = pre-JV PBT + JV share + exceptional, FY2025 | 4,596.33 | 4,596.33 | 0.02 | PASS | consolidated P&L |
| 74 | Revenue mix: product lines = sale-of-products subtotal, FY2026 | 43,309.98 | 43,309.98 | 0.01 | PASS | note 2.1 / 3.7.1 |
| 75 | Revenue mix: products + services + other - rebates = contract revenue, FY2026 | 43,936.35 | 43,936.35 | 0.01 | PASS | note 3.7.1 |
| 76 | Revenue mix: India + outside India = contract revenue, FY2026 | 43,936.35 | 43,936.35 | 0.01 | PASS | note 3.7.1 geography |
| 77 | Revenue mix: contract revenue + export incentives/grant = revenue from operations, FY2026 | 44,007.03 | 44,007.03 | 0.01 | PASS | note 2.1 vs P&L |
| 78 | SA total income = revenue + other income, FY2026 | 44,322.20 | 44,322.20 | 0.01 | PASS | standalone P&L, Total Income row |
| 79 | SA cost of goods sold = materials + purchases + inventory change, FY2026 | 31,417.14 | 31,417.14 | 0.01 | PASS | standalone P&L, printed subtotal |
| 80 | SA total expenses (sum of lines), FY2026 | 39,159.70 | 39,159.70 | 0.01 | PASS | standalone P&L, Total Expenses row |
| 81 | SA profit before exceptional & tax, FY2026 | 5,162.50 | 5,162.50 | 0.01 | PASS | standalone P&L |
| 82 | SA profit before tax, FY2026 | 4,814.02 | 4,814.02 | 0.01 | PASS | standalone P&L |
| 83 | SA profit after tax, FY2026 | 3,565.53 | 3,565.53 | 0.01 | PASS | standalone P&L |
| 84 | SA non-current assets (sum of lines), FY2026 | 13,931.67 | 13,931.67 | 0.02 | PASS | standalone balance sheet |
| 85 | SA current assets (sum of lines), FY2026 | 14,661.99 | 14,661.99 | 0.02 | PASS | standalone balance sheet |
| 86 | SA total assets, FY2026 | 28,593.66 | 28,593.66 | 0.02 | PASS | standalone balance sheet |
| 87 | SA total equity = share capital + other equity, FY2026 | 13,113.42 | 13,113.42 | 0.01 | PASS | standalone balance sheet |
| 88 | SA non-current liabilities (sum of lines), FY2026 | 2,153.60 | 2,153.60 | 0.02 | PASS | standalone balance sheet |
| 89 | SA current liabilities (sum of lines), FY2026 | 13,326.64 | 13,326.64 | 0.02 | PASS | standalone balance sheet |
| 90 | SA balance sheet balances: assets = equity + liabilities, FY2026 | 28,593.66 | 28,593.66 | 0.02 | PASS | standalone balance sheet |
| 91 | SA cash in AR net-debt bridge = balance-sheet cash, FY2026 | 2,031.09 | 2,031.09 | 0.01 | PASS | standalone net debt reconciliation |
| 92 | SA liquid investments = AR bridge liquid investments, FY2026 | 4,119.71 | 4,119.71 | 0.01 | PASS | standalone net debt reconciliation (FY2024 differs from the balance sheet by Rs 23.90 crore of subsidiary preference shares - removed as non-liquid) |
| 93 | CONS segment results bridge to reported PBT, FY2026 | 5,154.79 | 5,154.79 | 0.02 | PASS | consolidated segment note 3.8 vs consolidated P&L |
| 94 | CONS segment assets sum to total assets, FY2026 | 101,040.74 | 101,040.74 | 0.02 | PASS | segment note vs consolidated balance sheet |
| 95 | CONS segment net assets = total equity, FY2026 | 18,546.24 | 18,546.24 | 0.02 | PASS | segment note vs balance sheet |
| 96 | CONS PBT = pre-JV PBT + JV share + exceptional, FY2026 | 5,154.79 | 5,154.79 | 0.02 | PASS | consolidated P&L |
| 97 | SA OPBDITA vs company-published EBITDA, FY2024 | 4,606.58 | 4,607.00 | 0.60 | PASS | chairman's letter, EBITDA (rounded to the crore) |
| 98 | Domestic M&HCV + domestic LCV + exports = total vehicles, FY2024 | 194,555.00 | 194,555.00 | 0.50 | PASS | MD&A / chairman volumes vs ten-year historical table |
| 99 | SA OPBDITA vs company-published EBITDA, FY2025 | 4,930.56 | 4,931.00 | 0.60 | PASS | chairman's letter, EBITDA (rounded to the crore) |
| 100 | Domestic M&HCV + domestic LCV + exports = total vehicles, FY2025 | 195,097.00 | 195,097.00 | 0.50 | PASS | MD&A / chairman volumes vs ten-year historical table |
| 101 | SA OPBDITA vs company-published EBITDA, FY2026 | 5,732.25 | 5,732.00 | 0.60 | PASS | chairman's letter, EBITDA (rounded to the crore) |
| 102 | Domestic M&HCV + domestic LCV + exports = total vehicles, FY2026 | 220,437.00 | 220,437.00 | 0.50 | PASS | MD&A / chairman volumes vs ten-year historical table |
| 103 | Company net cash rebuilt from the balance sheet, FY2025 | 4,242.93 | 4,242.00 | 3.50 | PASS | chairman's letter net cash (rounded; residual = effective-interest accruals) |
| 104 | Company net cash rebuilt from the balance sheet, FY2026 | 5,901.72 | 5,899.00 | 3.50 | PASS | chairman's letter net cash (rounded; residual = effective-interest accruals) |
| 105 | Company net debt FY2024 rebuilt from the balance sheet | -89.54 | -89.00 | 1.00 | PASS | FY2024-25 AR chairman's letter |
| 106 | Net surplus on the AR bridge's definition, FY2023 | 0.70 | 47.39 | 60.00 | PASS | AR net-debt reconciliation; residual = derivative + EIR/accrued interest (bridge carries borrowings gross of EIR) - named in DISCLOSED_DIFFERENCES |
| 107 | Net surplus on the AR bridge's definition, FY2024 | -132.37 | -87.88 | 60.00 | PASS | AR net-debt reconciliation; residual = derivative + EIR/accrued interest (bridge carries borrowings gross of EIR) - named in DISCLOSED_DIFFERENCES |
| 108 | Net surplus on the AR bridge's definition, FY2025 | 4,196.80 | 4,203.99 | 60.00 | PASS | AR net-debt reconciliation; residual = derivative + EIR/accrued interest (bridge carries borrowings gross of EIR) - named in DISCLOSED_DIFFERENCES |
| 109 | Net surplus on the AR bridge's definition, FY2026 | 4,955.76 | 4,936.65 | 60.00 | PASS | AR net-debt reconciliation; residual = derivative + EIR/accrued interest (bridge carries borrowings gross of EIR) - named in DISCLOSED_DIFFERENCES |
| 110 | FS non-current borrowings = its components, FY2023 | 16,960.42 | 16,960.42 | 0.02 | PASS | consolidated note 1.20 note 8 |
| 111 | FS current borrowings = its components, FY2023 | 8,900.03 | 8,900.03 | 0.02 | PASS | consolidated note 1.26 note 2 |
| 112 | CONS non-current borrowings = note 1.20 lines, FY2023 | 19,502.86 | 19,502.86 | 0.02 | PASS | consolidated note 1.20 |
| 113 | CONS lease liabilities = NC + current, FY2023 | 240.49 | 240.49 | 0.02 | PASS | consolidated balance sheet |
| 114 | CONS revenue = CV + FS - inter-segment, FY2023 | 41,672.60 | 41,672.60 | 0.02 | PASS | segment note vs P&L |
| 115 | CONS PAT = PBT - tax, FY2023 | 1,358.82 | 1,358.82 | 0.02 | PASS | consolidated P&L |
| 116 | CONS D&A = cash-flow D&A + ROU depreciation, FY2023 | 900.22 | 900.22 | 0.02 | PASS | consolidated cash flow vs P&L |
| 117 | AR bridge arithmetic: net surplus from its own lines, FY2023 | 47.39 | 47.39 | 0.02 | PASS | standalone net debt reconciliation |
| 118 | SA lease liabilities = AR bridge lease line, FY2023 | 44.73 | 44.73 | 0.02 | PASS | balance sheet vs bridge |
| 119 | SA borrowings vs AR bridge borrowings (gross of EIR), FY2023 | 3,180.10 | 3,230.82 | 55.00 | PASS | bridge carries borrowings gross of effective-interest adjustments |
| 120 | SA other bank balances = earmarked + free deposits, FY2023 | 47.18 | 47.18 | 0.02 | PASS | standalone note 1.11B |
| 121 | SA CFO = cash from operations - tax paid, FY2023 | 2,136.01 | 2,136.01 | 0.02 | PASS | standalone cash flow |
| 122 | FS non-current borrowings = its components, FY2024 | 25,204.93 | 25,204.93 | 0.02 | PASS | consolidated note 1.20 note 8 |
| 123 | FS current borrowings = its components, FY2024 | 11,497.38 | 11,497.38 | 0.02 | PASS | consolidated note 1.26 note 2 |
| 124 | CONS non-current borrowings = note 1.20 lines, FY2024 | 26,695.71 | 26,695.71 | 0.02 | PASS | consolidated note 1.20 |
| 125 | CONS lease liabilities = NC + current, FY2024 | 237.84 | 237.84 | 0.02 | PASS | consolidated balance sheet |
| 126 | CONS revenue = CV + FS - inter-segment, FY2024 | 45,703.34 | 45,703.34 | 0.02 | PASS | segment note vs P&L |
| 127 | CONS PAT = PBT - tax, FY2024 | 2,696.34 | 2,696.34 | 0.02 | PASS | consolidated P&L |
| 128 | CONS D&A = cash-flow D&A + ROU depreciation, FY2024 | 927.29 | 927.29 | 0.02 | PASS | consolidated cash flow vs P&L |
| 129 | AR bridge arithmetic: net surplus from its own lines, FY2024 | -87.88 | -87.88 | 0.02 | PASS | standalone net debt reconciliation |
| 130 | SA lease liabilities = AR bridge lease line, FY2024 | 44.87 | 44.87 | 0.02 | PASS | balance sheet vs bridge |
| 131 | SA borrowings vs AR bridge borrowings (gross of EIR), FY2024 | 2,254.53 | 2,262.03 | 55.00 | PASS | bridge carries borrowings gross of effective-interest adjustments |
| 132 | SA other bank balances = earmarked + free deposits, FY2024 | 1,496.31 | 1,496.31 | 0.02 | PASS | standalone note 1.11B |
| 133 | SA CFO = cash from operations - tax paid, FY2024 | 2,503.12 | 2,503.12 | 0.02 | PASS | standalone cash flow |
| 134 | FS non-current borrowings = its components, FY2025 | 34,006.51 | 34,006.51 | 0.02 | PASS | consolidated note 1.20 note 8 |
| 135 | FS current borrowings = its components, FY2025 | 11,840.16 | 11,840.16 | 0.02 | PASS | consolidated note 1.26 note 2 |
| 136 | CONS non-current borrowings = note 1.20 lines, FY2025 | 36,382.92 | 36,382.92 | 0.02 | PASS | consolidated note 1.20 |
| 137 | CONS lease liabilities = NC + current, FY2025 | 261.01 | 261.01 | 0.02 | PASS | consolidated balance sheet |
| 138 | CONS revenue = CV + FS - inter-segment, FY2025 | 48,535.14 | 48,535.14 | 0.02 | PASS | segment note vs P&L |
| 139 | CONS PAT = PBT - tax, FY2025 | 3,382.79 | 3,382.79 | 0.02 | PASS | consolidated P&L |
| 140 | CONS D&A = cash-flow D&A + ROU depreciation, FY2025 | 1,086.65 | 1,086.65 | 0.02 | PASS | consolidated cash flow vs P&L |
| 141 | AR bridge arithmetic: net surplus from its own lines, FY2025 | 4,203.99 | 4,203.99 | 0.02 | PASS | standalone net debt reconciliation |
| 142 | SA lease liabilities = AR bridge lease line, FY2025 | 46.28 | 46.28 | 0.02 | PASS | balance sheet vs bridge |
| 143 | SA borrowings vs AR bridge borrowings (gross of EIR), FY2025 | 1,435.44 | 1,440.44 | 55.00 | PASS | bridge carries borrowings gross of effective-interest adjustments |
| 144 | SA other bank balances = earmarked + free deposits, FY2025 | 46.13 | 46.13 | 0.02 | PASS | standalone note 1.11B |
| 145 | SA CFO = cash from operations - tax paid, FY2025 | 7,819.42 | 7,819.42 | 0.02 | PASS | standalone cash flow |
| 146 | FS non-current borrowings = its components, FY2026 | 43,119.02 | 43,119.02 | 0.02 | PASS | consolidated note 1.20 note 8 |
| 147 | FS current borrowings = its components, FY2026 | 15,840.45 | 15,840.45 | 0.02 | PASS | consolidated note 1.26 note 2 |
| 148 | CONS non-current borrowings = note 1.20 lines, FY2026 | 46,016.36 | 46,016.36 | 0.02 | PASS | consolidated note 1.20 |
| 149 | CONS lease liabilities = NC + current, FY2026 | 285.90 | 285.90 | 0.02 | PASS | consolidated balance sheet |
| 150 | CONS revenue = CV + FS - inter-segment, FY2026 | 56,362.08 | 56,362.08 | 0.02 | PASS | segment note vs P&L |
| 151 | CONS PAT = PBT - tax, FY2026 | 3,720.98 | 3,720.98 | 0.02 | PASS | consolidated P&L |
| 152 | CONS D&A = cash-flow D&A + ROU depreciation, FY2026 | 1,137.56 | 1,137.56 | 0.02 | PASS | consolidated cash flow vs P&L |
| 153 | AR bridge arithmetic: net surplus from its own lines, FY2026 | 4,936.65 | 4,936.65 | 0.02 | PASS | standalone net debt reconciliation |
| 154 | SA lease liabilities = AR bridge lease line, FY2026 | 43.34 | 43.34 | 0.02 | PASS | balance sheet vs bridge |
| 155 | SA borrowings vs AR bridge borrowings (gross of EIR), FY2026 | 1,151.70 | 1,154.71 | 55.00 | PASS | bridge carries borrowings gross of effective-interest adjustments |
| 156 | SA other bank balances = earmarked + free deposits, FY2026 | 945.96 | 945.96 | 0.02 | PASS | standalone note 1.11B |
| 157 | SA CFO = cash from operations - tax paid, FY2026 | 4,792.10 | 4,792.10 | 0.02 | PASS | standalone cash flow |
| 158 | CONS current borrowings = note 1.26 lines, FY2024 | 13,868.63 | 13,868.63 | 0.02 | PASS | consolidated note 1.26 |
| 159 | CONS finance costs = FS interest + non-FS interest, FY2024 | 2,982.25 | 2,982.25 | 0.02 | PASS | segment note 'material items' vs P&L |
| 160 | Equity into subsidiaries: cash flow vs board report, FY2024 | 1,567.02 | 1,567.71 | 1.00 | PASS | standalone cash flow vs board's report |
| 161 | CONS current borrowings = note 1.26 lines, FY2025 | 13,318.18 | 13,318.18 | 0.02 | PASS | consolidated note 1.26 |
| 162 | CONS finance costs = FS interest + non-FS interest, FY2025 | 3,930.21 | 3,930.21 | 0.02 | PASS | segment note 'material items' vs P&L |
| 163 | Equity into subsidiaries: cash flow vs board report, FY2025 | 717.06 | 717.05 | 1.00 | PASS | standalone cash flow vs board's report |
| 164 | CONS current borrowings = note 1.26 lines, FY2026 | 17,633.44 | 17,633.44 | 0.02 | PASS | consolidated note 1.26 |
| 165 | CONS finance costs = FS interest + non-FS interest, FY2026 | 4,704.65 | 4,704.65 | 0.02 | PASS | segment note 'material items' vs P&L |
| 166 | Equity into subsidiaries: cash flow vs board report, FY2026 | 386.28 | 386.28 | 1.00 | PASS | standalone cash flow vs board's report |
| 167 | Interest paid: cash flow vs AR bridge, FY2023 | 259.79 | 259.79 | 0.02 | PASS | net debt reconciliation |
| 168 | NC borrowings net flow: repayments - proceeds = bridge, FY2023 | 375.94 | 375.94 | 0.02 | PASS | net debt reconciliation |
| 169 | Interest paid: cash flow vs AR bridge, FY2024 | 246.11 | 246.11 | 0.02 | PASS | net debt reconciliation |
| 170 | NC borrowings net flow: repayments - proceeds = bridge, FY2024 | 1,104.98 | 1,104.98 | 0.02 | PASS | net debt reconciliation |
| 171 | Interest paid: cash flow vs AR bridge, FY2025 | 149.06 | 149.06 | 0.02 | PASS | net debt reconciliation |
| 172 | NC borrowings net flow: repayments - proceeds = bridge, FY2025 | 441.73 | 441.73 | 0.02 | PASS | net debt reconciliation |
| 173 | Interest paid: cash flow vs AR bridge, FY2026 | 93.64 | 93.64 | 0.02 | PASS | net debt reconciliation |
| 174 | NC borrowings net flow: repayments - proceeds = bridge, FY2026 | 276.60 | 276.60 | 0.02 | PASS | net debt reconciliation |
| 175 | SA finance costs = note 2.5 lines, FY2025 | 216.91 | 216.91 | 0.02 | PASS | standalone note 2.5 |
| 176 | SA other income = note 2.2 lines, FY2025 | 250.25 | 250.25 | 0.02 | PASS | standalone note 2.2 |
| 177 | SA finance costs = note 2.5 lines, FY2026 | 169.73 | 169.73 | 0.02 | PASS | standalone note 2.5 |
| 178 | SA other income = note 2.2 lines, FY2026 | 315.17 | 315.17 | 0.02 | PASS | standalone note 2.2 |
| 179 | Vehicle volume repeated in FY2024-25 AR table, FY2023 | 192,205.00 | 192,205.00 | 0.50 | PASS | FY2024-25 AR p6 |
| 180 | Vehicle volume repeated in FY2024-25 AR table, FY2024 | 194,555.00 | 194,555.00 | 0.50 | PASS | FY2024-25 AR p6 |
| 181 | Vehicle volume repeated in FY2024-25 AR table, FY2025 | 195,097.00 | 195,097.00 | 0.50 | PASS | FY2024-25 AR p6 |
| 182 | Guarantees repeated as next AR's comparative, FY2024 | 762.16 | 762.16 | 0.02 | PASS | next year's note 3.9.2 |
| 183 | Guarantees repeated as next AR's comparative, FY2025 | 1,021.58 | 1,021.58 | 0.02 | PASS | next year's note 3.9.2 |
| 184 | M&HCV share change vs the change the AR states, FY2024 | -0.70 | -0.70 | 0.15 | PASS | MD&A; FY2025's stated -0.3 vs series -0.4 is the AR's own rounding gap |
| 185 | M&HCV share change vs the change the AR states, FY2025 | -0.40 | -0.30 | 0.15 | PASS | MD&A; FY2025's stated -0.3 vs series -0.4 is the AR's own rounding gap |
| 186 | M&HCV share change vs the change the AR states, FY2026 | -0.40 | -0.40 | 0.15 | PASS | MD&A; FY2025's stated -0.3 vs series -0.4 is the AR's own rounding gap |


**External tie-out (screener.in, read 10-Oct-2026; cross-check only, R1):** standalone sales,
operating profit, borrowings incl. leases, net worth, PAT and CFO agree for FY2023-FY2026 to the
crore; consolidated sales and borrowings agree; consolidated FY2023 PAT differs by Rs 3 crore
(screener uses FY2023 as originally reported) — full table in the spreads' `ExternalTieOut` tab.

**Mutation coverage:** `tools/tieout_mutation.py ashok-leyland` → 611 inputs perturbed, 598 change a
tie-out (97.9%). The 13 that change nothing are named in the engine's DISCLOSED_DIFFERENCES: capex
and dividends paid (single-sourced in the cash-flow statement), FY2023 consolidated current
borrowings and finance cost, FY2023/FY2026 guarantees, FY2023 equity into subsidiaries. None feeds
a leverage or coverage ratio.

---

## 7. Step 7 — Fact register

| Fact | Value | Source |
|---|---|---|
| Promoter | Hinduja Automotive Limited, UK — 50.85% (holding company) | FY2026 AR, list of subsidiaries/holding (Board's report annexure) |
| Pledge of promoter shares | None disclosed | Recorded search (§2) |
| Management | Dheeraj G Hinduja, Executive Chairman (re-appointed 28-May-2026); Shenu Agarwal, MD & CEO; K.M. Balaji, CFO | FY2026 AR |
| Auditor | Price Waterhouse & Co Chartered Accountants LLP — unmodified opinions FY2024-FY2026 | Audit reports |
| KAMs | Standalone: carrying value of investment in Optare group Rs 3,129.83 crore (impairment judgement). Consolidated: HLF ECL on gross loans Rs 49,156.66 crore (ECL 1,279.86 vs 888.22); FVTOCI classification | FY2026 AR audit reports |
| Capacity / plants | Hosur (NCD security), multi-plant; dealer and service touchpoints 2,104 | FY2026 AR chairman; note 3.11 |
| Market position FY2026 | Domestic M&HCV 30.3% (#2); buses 34.1% (#1); LCV VAHAN share 12.7% (0-7.5T) | FY2026 AR MD&A |
| Exports | 18,082 units FY2026 (+19%); "a clear ambition to reach 25,000 export units in the near term" | FY2026 AR chairman |
| Non-CV businesses | Power Solutions revenue > Rs 1,000 crore (second year); Defence +20% | FY2026 AR chairman |
| Subsidiaries (consolidation) | 39 subsidiaries, 6 associates, 4 JVs; full list with holdings in §7.1 | FY2026 AR Board's report |
| Financial-services arm | Hinduja Leyland Finance (61.12%) + Hinduja Housing Finance and Gaadi Mandi (step-down): net assets Rs 10,504.82 crore, FY2026 profit Rs 877.37 crore | Schedule III table (note 3.1.3) |
| Group financing book quality (consolidated note 3.6, financing activity) | Exposure Rs 60,525.09 crore (Rs 48,605.69 crore): vehicles 34,286.56 (+20.8%), loans against property 14,735.00 (+54.3%), housing 11,503.53. Stage 3 Rs 2,125.91 crore = 3.51% (3.52%); Stage 3 ECL 45.26% (42.24%). ECL allowance +415.54 (1,046.87 → 1,462.41; "Write offs" row nil), against a P&L impairment/write-off charge of 1,234.24 → ~Rs 818.70 crore charged off directly (derived; FM59: the flat Stage 3 ratio is not evidence of stable quality) | FY2026 AR consolidated note 3.6 |
| HLF corporate action | Merger by absorption into NDL Ventures Limited (25 NDL shares per 10 HLF shares; NCDs convert); RBI NOC 08-Aug-2025, CCI approved, BSE/NSE no-objection (BSE 18-May-2026); to be filed with NCLT Mumbai | FY2026 AR note 1.3 sub-note 9; Board's report |
| EV business | Switch UK discontinued manufacturing at Sherburn (after-sales continues); Switch Mobility India "achieved net profitability"; Optare group FY2026 loss Rs 148.26 crore, net assets Rs 130.78 crore vs AL's cost Rs 3,000.23 crore | Board's report; chairman; Schedule III; note 1.3 |
| Other loss-making subsidiaries FY2026 | Hinduja Tech (−199.60), OHM Global Mobility (−35.69), Gro Digital (−17.00), Albonair GmbH (−10.61), Ashley Aviation (−2.22) | Schedule III |
| Equity support to subsidiaries | FY2024 1,567.02; FY2025 717.06; FY2026 386.28 (engine; tied to Board's report) | Cash flow + Board's report |
| Guarantees for subsidiaries | Rs 785.71 crore (Switch Mobility UK 633.12, Albonair GmbH 152.59) + open-ended "financial support ... including undertaking provided to customers of certain subsidiaries" | Notes 3.9.1, 3.9.2, 3.10 |
| ICDs to promoter-group companies | Max outstanding FY2026 Rs 670 crore across seven Hinduja-group entities (Hinduja Group, Hinduja Realty Ventures, IndusInd Media & Communications, OneOTT Intertainment, In Entertainment, Hinduja Healthcare — max 70, Hinduja Properties); FY2025 max Rs 490 crore; nil at both year-ends; FY2024 year-end Rs 100 crore | Note 3.9.1 (FY2026, FY2025 ARs) |
| Contingent liabilities | Claims not acknowledged as debts Rs 342.87 crore (FY2026) — sum of the five printed lines: GST/VAT 232.34, excise 8.92, service tax 24.06, customs 0.41, others 77.14 | Note 3.9 |
| Capital commitments | Rs 460.19 crore (FY2026) | Note 3.10 |
| Covenants | "complied with all applicable covenants as at March 31, 2026" | Note 1.16 note 5 |
| Undrawn bank lines | Rs 2,854.34 crore (FY2026); CP option Rs 2,000 crore, none outstanding (standalone) | Liquidity-risk note |
| ESG | Renewable energy 77% (69% FY2025); BRSR Core assured by DNV; carbon-neutrality target 2030 | FY2026 chairman; Board's report; FY2025 chairman |

### 7.1 Entities consolidated (FY2026 AR — every entity named, FM17)
Holding company: Hinduja Automotive Limited, UK (50.85%). Wholly owned: Albonair GmbH (Germany);
Albonair (Taicang) Automotive Technology Co. (China, step-down); Albonair (India) Private Limited;
Ashok Leyland (Nigeria) Limited; Ashok Leyland (Chile) S.A.; Ashok Leyland Foundation; OHM Global
Mobility Private Limited; Ashley Aviation Limited; Ashok Leyland (UAE) LLC; Ashok Leyland Saudi
Company (step-down); Vishwa Buses and Coaches Limited. Subsidiaries: Gulf Ashley Motor Limited
(93.15%); Optare Plc, UK (93.28%) with Optare UK Limited, Switch Mobility Limited UK, Switch
Mobility Automotive Limited and Switch Mobility Europe S.L. (92.91%); HLF Services Limited
(82.05%); Gro Digital Platforms Limited (80.56%); Hinduja Tech Limited (72.93%) with Hinduja Tech
GmbH, Hinduja Tech Inc., Hinduja Tech (Shanghai), Hinduja Tech Canada, Drive System Design
Limited/Inc./s.r.o., Hinduja Tech Limited UK, TECOSIM Group GmbH, TECOSIM GmbH, TECOSIM Engineering
Services Private Limited, TECOSIM Japan, TECOSIM Limited UK, TECOSIM Engineering S.R.L., TECOSIM
Inc.; Global TVS Bus Body Builders Limited (66.67%); Hinduja Leyland Finance Limited (61.12%) with
Hinduja Housing Finance Limited and Gaadi Mandi Digital Platforms Limited. JVs: Ashley Alteams
India Limited (50%); TVS Trucks and Buses Private Limited (49.90%); ZeBeyond Limited UK (20.84%,
JV of subsidiary); Ashok Leyland John Deere Construction Equipment Co. (under liquidation).
Associates: Ashok Leyland Defence Systems Limited (48.49%); Mangalam Retail Services Limited
(37.48%); Lanka Ashok Leyland PLC (27.85%); Rajalakshmi Wind Energy Limited, Prathama Solar
Connect Energy Private Limited, HR Vaigai Private Limited (26% each).

---

## 8. Step 7b — Instrument details

**From the company's documents:** NCD Series 3 — "NCD - Series 3 - 7.30% AL 2027", Rs 200 crore,
ISIN INE208A07406 (FY2024 AR Corporate Governance report); "Bullet repayment at the end of 5 years
from the date of allotment i.e. March 17, 2027" (FY2026 AR borrowings repayment schedule); "The
Company has a call option to redeem the debentures at the end of 3rd year" (FY2024 AR, same
schedule); secured by "First Ranking charge over specific plant and machinery of manufacturing
unit situated at Hosur to the extent of 1.10 times" (borrowings note, security clause (viii));
quarterly security-cover statements filed (Q1 FY2025 filing). "Your Company did not issue any
fresh Non-Convertible Debentures (NCDs), nor were any NCDs redeemed during the year" (FY2026
Board's report). CP: Rs 2,000 crore option, none outstanding at the standalone level
(liquidity-risk note); the consolidated CP of Rs 96.94 crore belongs to the financial-services arm
(note 1.26 note 2). Rated programme per the AR (§U, ICRA lines): fund-based 2,000.00;
non-fund-based 1,500.00; long-term loans 982.50; LT/ST unallocated 750.00; CP 2,000.00; NCD
200.00 — the AR prints no total; the six lines sum to Rs 7,432.50 crore.

**CRA-published rated-amount table — imported under the 13-Aug-2026 amendment (FM29):**
ICRA rationale dated **02-Jun-2026** (reference library). Conditions: (1) same-issuer primary
rationale held in the library ✓; (2) reproduced verbatim, every line, dated ✓; (3) labelled
CRA-published, **not issuer-confirmed** ✓; (4) line integrity — 2,000.00 + 200.00 + 300.00 +
2,000.00 + 1,500.00 + 729.38 + 750.00 = **7,479.38** = printed total ✓, and its "previous" column
(7,432.50) equals the company's own AR §U table line-for-line ✓; (5) rated limits vs drawn debt
stated below ✓.

| Instrument | Previous (Rs crore) | Current (Rs crore) |
|---|---:|---:|
| Commercial Paper | 2,000.00 | 2,000.00 |
| Non-Convertible Debenture | 200.00 | 200.00 |
| Proposed Non-convertible debenture | 0.00 | 300.00 |
| LT/ST: Fund based limits | 2,000.00 | 2,000.00 |
| LT/ST: Non-fund based limits | 1,500.00 | 1,500.00 |
| Long-term – Fund based – Term loans | 982.50 | 729.38 |
| LT/ST: Unallocated | 750.00 | 750.00 |
| **Total** | **7,432.50** | **7,479.38** |

**Rated limits ≠ drawn debt (R4):** rated programme Rs 7,479.38 crore (includes Rs 1,500 crore
non-fund-based, Rs 750 crore unallocated, Rs 2,000 crore CP with nil outstanding, Rs 300 crore
proposed NCD) vs standalone **drawn** borrowings of Rs 1,151.70 crore at 31-Mar-2026 (long-term
517.88 + current 633.82; plus leases 43.34 = total debt 1,195.04, engine), reconciled to screener.in
(1,195). Long-term borrowings "stood at Rs 1,002.04 crores" (FY2026 Board's report) = term loans
735.63 + NCD 200.00 + interest-free sales-tax loans 66.41 (non-current 61.50 + current 4.91) —
all three from the FY2026 AR repayment schedule, which sums exactly. Drawn term loans Rs 735.63
crore at 31-Mar-2026 vs ICRA's rated term loans Rs 729.38 crore at 02-Jun-2026: a Rs 6.25 crore
gap of the size of a scheduled April-May 2026 instalment (TL-15 is "Repayable quarterly");
**to be confirmed by issuer.**

---

## 9. Step 8 — Materiality sweep (R13: material if ≥1% of TNW = Rs 131 crore, or ≥5% of PBT = Rs 241 crore, or ≥1 notch, or any governance/regulatory/default item)

| Finding | Size / nature | Test met | Decision |
|---|---|---|---|
| Equity support to EV and loss-making subsidiaries (Optare/Switch Rs 2,069 crore over FY2024-26; OHM Rs 300 crore) with Optare-group KAM | Rs 2,670 crore of equity in three years (engine) | ≥1% TNW; plausibly ≥1 notch | **Material** — credit challenge; support assessment |
| Non-financial subsidiaries' borrowings Rs 3,538.63 crore (up from 1,607.50) + guarantees 785.71 | Contingent claims on AL | ≥1% TNW | **Material** — adjusted leverage view |
| ICDs to promoter-group companies, max Rs 670 crore (FY2026), Rs 490 crore (FY2025) | Related-party support to group entities | Governance item — regardless of size | **Material** — governance consideration (ICRA 960 "instances of financial support to group entities at the expense of debt holders") |
| HLF credit costs: impairment relating to financing 1,234.24 vs 651.95; ECL 1,279.86 vs 888.22; loan growth ~30% | Possible capital call on AL | Plausibly ≥1 notch over time | **Material** — monitored via capital-requirement lens (ICRA 1006 "assesses capital requirements for the captive finance business") |
| HLF-NDL merger (listing route) | Corporate action pending NCLT | Event | **Material** — reduces HLF's dependence on AL if completed; not yet effective |
| Labour Codes exceptional Rs 308.48 crore; litigation 40.00 | One-time | ≥5% PBT | **Material for PAT, excluded from OPBDITA**; state rules pending (further impact possible) |
| ELV/EPR obligation | Not estimable | Regulatory | **Material by type** — disclosed as unquantified |
| Cyclicality: FY2021 loss (Rs 314 crore), volumes −49% FY2019-21 | Industry | ≥1 notch | **Material** — central to the view |
| M&HCV truck share erosion 32.3% → 30.0% | Business | Plausibly ≥1 notch if sustained | **Material** — weakness, sensitivity |
| Aircraft acquisition funded by Rs 345.63 crore term loan | ~2.6% TNW | ≥1% TNW | Material by size, analytically a capex/use-of-funds item — noted |
| Electoral-trust contributions Rs 108 crore (FY2026) | Legal under s.182 | <1% TNW | Immaterial — logged |
| Contingent liabilities Rs 342.87 crore | Tax disputes | ≥1% TNW | Material by size; low devolvement risk given liquidity — noted |
| Supplier finance Rs 87.25 crore (consolidated) | In borrowings | <1% TNW | Immaterial |
| Debenture Redemption Fund deposit Rs 100 crore inside the FY2026 Rs 900 crore deposits | Encumbered cash | <1% TNW; but FM45 (liquidity must be unencumbered) | Excluded from free liquidity; set against the NCD redemption only (§5.3) |
| Dividend outflow Rs 1,835.42 crore (FY2026), Rs 2,040.77 crore (FY2025) | ~56-58% payout | Financial policy | Material to cash flow — in the model |

---

## 10. Step 10 — Methodology Compliance Map (ICRA 1006 + 960; 934 for basis)

**Indicative-metrics tables, scored with the company's numbers (engine; FY2026 unless stated).**
Two columns per ratio: the automotive view (consolidated excluding financial services — the
methodology basis) and AL standalone (the rated entity).

| Ratio (1006 / 960 band) | Strongest | Weakest | Automotive view | AL standalone | Assessment |
|---|---|---|---|---|---|
| RoCE | ≥25% | <10% | CV segment PBIT 4,379.32 on average CV segment net assets (6,969.29 FY2025, 7,892.63 FY2026) = 58.9% | 32.85% / 33.90% / 35.96% (FY2024-26) | **Strongest band** |
| Volatility in RoCE | ≤10% | >55% | not computable | the 3 computable years (FY2024-26) span 32.85-35.96%, a 3.1 pp range — inside the strongest band; but the FY2021 loss (ten-year table) shows through-cycle volatility is far higher; RoCE for FY2017-22 cannot be computed (no PBIT or debt split in the ten-year table) | **Data-limited; judged moderate through the cycle** |
| Indebtedness — TOL/TNW | ≤0.9x | >3.0x | no automotive balance sheet (segment note gives assets/liabilities, not TNW) | 1.68x / 1.22x / 1.18x | **Strong** (second band; trade payables of Rs 8,329 crore drive it — not debt) |
| Total debt/OPBDITA | ≤0.5x | >5.0x | 0.95x / 0.93x / 0.98x at the low OPBDITA bound | 0.50x / 0.30x / 0.21x | Standalone **strongest**; automotive **strong** |
| Interest coverage | ≥18x | <2x | 10.15x / 11.10x / 11.96x at the low bound | 18.47x / 22.73x / 33.77x | Standalone **strongest**; automotive **strong** |
| DSCR | ≥4.0x | <1.1x | not computable (no subsidiary repayment schedule) | 2.65x / 4.68x / 8.10x | **Strongest** (FY2024's 2.65x reflects Rs 1,104.98 crore of prepayment) |

**Factor-by-factor map.**

| Rating factor (as named in the methodology) | Section | Company's evidence / metric | Assessment vs the methodology | Weight |
|---|---|---|---|---|
| Industry risk — Cyclicality | 1006 "Cyclicality": "the M&HCV segment shows higher cyclicality" | M&HCV = 58% of AL's FY2026 volume (1,28,033 of 2,20,437); AL's volumes −49% FY2019-21, FY2021 loss Rs 314 crore | High cyclicality — the main constraint on the rating | High |
| Industry risk — Competitive intensity; Regulatory/policy | 1006 | Tata Motors leads M&HCV **[web]**; ELV extended-producer-responsibility obligation "not estimable" (note 3.9); Labour Codes (state rules pending); emission norms drive capex | Moderate | Medium |
| Scale, market position and brand strength | 1006: "an assessment is made of the trend in the OEM's scale and positioning" | 2,20,437 vehicles; revenue Rs 44,007 crore; M&HCV 30.3% (31.8% FY2023); trucks 30.0% (32.3%); buses 34.1% (leader); LCV 12.7% VAHAN | Strong scale and position; **the trend in truck share is adverse** | High |
| Product portfolio | 1006 | Trucks, buses, LCVs, defence, engines and gensets (Rs 1,414 crore), spares (Rs 4,450 crore); CVs are 82% of gross revenue | Moderate diversification beyond CVs, improving | Medium |
| Sales, service network and geographic diversification | 1006 | 2,104 touchpoints; exports 18,082 units, 7.0% of revenue | Domestic-concentrated | Medium |
| Technology and product development | 1006 | BEV, hydrogen, LNG/CNG programmes; capex Rs 1,050 crore; EV subsidiaries loss-making (Optare −148.26) | Adequate; the EV build-out costs cash | Medium |
| Profitability (validation through RoCE) | 1006 indicative metrics | Above; OPBDITA margin 8.11% → 13.03% (FY2023-26) | Strongest band at this point in the cycle | High |
| Leverage; Coverage | 1006 indicative metrics | Above | Strongest (standalone) / strong (automotive) | High |
| Liquidity | 1006 "Liquidity"; ICRA 1014 | §11: Superior | Supports the rating | High |
| Cash flows; Capital expenditure and investment plans | 1006 | CFO Rs 4,792 crore; FCF Rs 1,528 crore (FY2026); capex Rs 1,050 crore; equity into subsidiaries Rs 1,567 / 717 / 386 crore (FY2024-26) | Internally funded; subsidiary support is a recurring call | Medium |
| Foreign currency risks | 1006 | No foreign-currency borrowing disclosed at the standalone level; exports 7.0% of revenue | Low | Low |
| Tenure mismatch / refinancing; Financing availability | 1006 | Borrowings Rs 1,151.70 crore against free liquidity Rs 6,950.80 crore; NCD Rs 200 crore due 17-Mar-2027 with Rs 100 crore pre-funded | Negligible refinancing risk | Low |
| Parentage/Group support | 1006: "The rating of the OEM would thus be influenced by the parent's standing and the linkages between them." | Hinduja Automotive Limited, UK — 50.85%; **its credit profile cannot be established from the document set** (no financials; unlisted). The cash flows the other way: AL lends to promoter-group companies (ICDs up to Rs 670 crore) | **No uplift. Downward linkage risk** (FM56) — §13 | High |
| Captive finance | 1006: "for OEMs with captive finance companies, ICRA's analysis assesses capital requirements for the captive finance business" | HLF gross loans Rs 49,156.66 crore (+29.7%); credit cost Rs 1,234.24 crore (Rs 651.95 crore); group financing book Stage 3 steady at 3.5% only because ~Rs 819 crore was charged off directly (§7); loans against property +54%; AL put Rs 200 crore into HLF in FY2025; listing via the NDL merger pending NCLT | Moderate capital-call risk; the merger would widen HLF's own access to capital | Medium |
| Consolidated financial analysis | 1006: ICRA "analyses consolidated/group-level financial indicators"; 934 dissimilar-business rule | §5.1 basis; non-FS subsidiaries' borrowings 1,607.50 → 3,538.63 (FY2024-26) | Automotive leverage is ~1x OPBDITA — still strong | High |
| Financial flexibility | 1006 | Market capitalisation ~Rs 88,390 crore (aggregator price, 01-Oct-2026) = 74x standalone debt; undrawn lines Rs 2,854.34 crore; CP programme | Very strong | Medium |
| Debt-servicing track record | 1006 | Covenants complied (note 1.16); no delay disclosed | Clean | Low |
| Accounting quality | 1006 | PwC, unmodified; KAMs on the Optare carrying value and HLF ECL | Good; the Optare carrying value (Rs 3,129.83 crore vs net assets Rs 130.78 crore) is a watch item | Low |
| Contingent liabilities and off-balance-sheet exposures | 1006 | Contingent liabilities Rs 342.87 crore; guarantees for subsidiaries Rs 785.71 crore + open-ended support undertakings; capital commitments Rs 460.19 crore | Manageable against liquidity | Medium |
| Event risk | 1006 | HLF-NDL merger; Labour Codes state rules; Switch UK restructuring | Monitorable | Medium |
| Management Quality (and governance) | 1006; 960: "related party transactions, instances of financial support to group entities at the expense of debt holders ... are evaluated" | ICDs to seven promoter-group companies (max Rs 670 crore FY2026, Rs 490 crore FY2025, nil at year-ends); electoral-trust contributions Rs 108 crore (FY2026); conservative leverage policy; dividend payout ~56-58% | **Constrains the rating** — it is the main reason the strongest-band financials do not translate into AAA | High |
| ESG | 1006 "Assessment of ESG Risks" | Renewable energy 77% (69%), 85% targeted FY2027; Water Positive; BRSR Core assured by DNV; product transition (BEV, H2) under way; governance above | Environmental transition risk moderate and being addressed; governance is the relevant ESG factor here | Medium |

---

## 11. Step 11 — Liquidity: sources vs claims, FY2027 (model base case, Rs crore)

| Sources | | Uses | |
|---|---:|---|---:|
| Free cash and liquid investments, 31-Mar-2026 | 6,950.80 | Scheduled repayments (note 1.21 current maturities) | 483.82 |
| Debenture Redemption Fund deposit (only for the NCD) | 100.00 | Capex | 1,200.00 |
| Cash flow from operations FY2027E (PAT 4,101.38 + D&A 787.22 + working-capital release 130.18) | 5,018.78 | Dividends (Rs 1,468.46 crore committed 28-May-2026 + Rs 1/share interim) | 2,055.85 |
| Undrawn bank lines (not needed) | 2,854.34 | Equity support to subsidiaries | 500.00 |
| **Total excl. undrawn lines** | **12,069.58** | **Total** | **4,239.67** |

(Interest of Rs 157.00 crore is inside PAT.) Internal cash flow alone (5,018.78) covers all uses
(4,239.67); opening unencumbered liquidity plus the DRF deposit (7,050.80) covers scheduled debt
service (483.82 + 157.00 = 640.82) **11.0 times**. Under stress: the rating-stress case's lowest
free liquidity is Rs 4,878.30 crore (FY2029) and the FY2019-21 tail's is Rs 2,783.94 crore
(FY2028) — **neither draws new debt**. **Descriptor: Superior.** It is the conclusion of the
arithmetic, and it matches how ICRA uses the word for net-cash auto OEMs (Eicher, M&M, Escorts
Kubota — craft only).

---

## 12. Step 12 — Projections (equity-research Tasks 1-4, scaled; `case.json`)

Deliverables: `Ashok Leyland_Research_Note_10Oct2026.md` (Task 1),
`Ashok Leyland_Financial_Model_10Oct2026.xlsx` (Task 2: Revenue Model, Income Statement, Cash
Flow, Balance Sheet, Scenarios, DCF Inputs + Credit Ratios [116 formula cells, cached; the 31
historical cells equal the engine] + Debt Breakup + Valuation), `Ashok Leyland_Valuation_Note_10Oct2026.md`
(Task 3), `Ashok Leyland_Charts_10Oct2026.zip` (Task 4, 8 charts). Every driver and its source is in the
model's Assumptions tab. The debt path is derived from the funding gap (FM18): borrowing only
below a Rs 1,500 crore liquidity floor.

**Assumptions (base / rating stress), FY2027E-FY2031E:**

| Driver | Base | Rating stress (Bear) | Source |
|---|---|---|---|
| Vehicle volume growth (%) | 5, 5, 2, −4, 4 | −8, −25, −10, 15, 10 | MD&A "consolidation-led growth"; stress = a downturn of about three-quarters of the FY2019-21 depth (ten-year table) |
| OPBDITA margin (%) | 13.0, 13.0, 12.5, 11.5, 12.5 | 10.5, 6.0, 7.5, 10.0, 11.0 | FY2026 actual 13.03% |
| Capex (Rs crore) | 1,200 / 1,150 / 1,100 / 1,000 / 1,100 | 1,000 / 800 / 800 / 900 / 1,000 | FY2026 Rs 1,050 crore |
| Support to subsidiaries (Rs crore) | 500 / 500 / 400 / 400 / 400 | 1,000 ×3, then 500 ×2 (HLF capital call + EV losses) | FY2024-26 actuals |
| Dividends | committed Rs 1,468.46 crore + interim; then 55% of prior PAT | committed only; then 30% | FY2026 AR |

A **tail** case repeats the company's own FY2019-21 path (volumes −37%, −20%, then recovery;
margin troughing at 3%).

**Outputs (worst year in each case):**

| Case | OPBDITA margin | Interest coverage | DSCR | Total debt/OPBDITA | Free liquidity | New debt |
|---|---|---|---|---|---|---|
| Base | 11.5% (FY2030) | 38.87x (FY2027) | 7.87x (FY2027) | 0.12x | ≥ Rs 7,830 crore | nil |
| Rating stress | 6.0% (FY2028) | 14.17x | 7.27x | 0.30x | Rs 4,878 crore (FY2029) | nil |
| Tail (FY2019-21 repeat) | 3.0% (FY2028) | 5.46x | 2.86x (FY2027) | 0.77x | Rs 2,784 crore (FY2028) | nil |

Reading: the standalone balance sheet absorbs even a repeat of the worst downturn in the
company's ten-year history without new borrowing. What the stress does show is RoCE falling to
7.33% (stress, FY2028) and −0.38% (tail) — through the weakest band of the indicative table.
That earnings cyclicality, not leverage, is what the rating must price.

---

## 12b. Step 12b — Scorecard (Stage 1 anchor)

`Rating_Scorecard_Ashok Leyland Limited.xlsx`: sector Auto OEM, industry override 3.5 (CVs are
more cyclical than the blended OEM base), business 2, management 3, support 0, liquidity
Superior. Historicals are AL standalone audited actuals; the automotive leverage is cited in the
note on the debt row. **Anchor: [ICRA]AA / [ICRA]A1+** (composite 2.016, index 2; no hard cap;
business-risk gate does **not** fire — business 2.0 vs financial 1.54). Justifications are on
the sheet (Inputs!F39:F43). FY+1/FY+2 drivers were copied from the model, each labelled
"source: forecast model".

---

## 13. Step 13 — Independent rating view (formed before opening ICRA's report)

**Standalone credit profile — what supports a high rating.** Strongest-band financial metrics
on the rated entity: Total debt/OPBDITA 0.21x, interest coverage 33.77x, DSCR 8.10x, RoCE 35.96%,
standalone net cash Rs 5,755.76 crore (FY2026). The automotive view is weaker but still strong
(Total debt/OPBDITA ~1.0x, coverage ~12x at the conservative bound). Liquidity is Superior and
survives a repeat of FY2019-21 without borrowing. Scale and franchise: 2,20,437 vehicles, the
second-largest M&HCV share, bus leadership, and growing aftermarket and Power Solutions revenue.

**What holds it below AAA.**
1. *Single-industry cyclicality.* A five-year upcycle followed a 49% volume collapse and a loss
   (FY2021). ICRA's AAA auto names (M&M, Eicher, in the reference library) combine this with
   dominant or diversified franchises; AL is the number two in M&HCV, with share eroding.
2. *Group claims on cash — downward linkage (FM56).* The cash flows run from AL to the group,
   not the other way: ICDs to promoter-group companies up to Rs 670 crore, Rs 2,670 crore of
   equity into loss-making EV subsidiaries in three years, guarantees of Rs 785.71 crore, and a
   fast-growing captive NBFC whose credit costs nearly doubled. The parent's own credit profile
   cannot be established from the documents. The 960 governance test — "financial support to
   group entities at the expense of debt holders" — applies directly.
3. *Automotive leverage rising.* Non-financial subsidiaries' borrowings more than doubled,
   1,607.50 → 3,538.63 (FY2024-26).

**Why not lower (AA).** Every indicative metric on the rated entity is in the strongest band.
The automotive metrics are in the strong band, and the stress tests show no refinancing
dependence at all. The group claims are real but sized against Rs 6,951 crore of free liquidity:
the largest single year of subsidiary support (Rs 1,567 crore, FY2024) is 23% of it.

**Support notching, both directions.** No uplift: AL is the operating flagship, not a supported
subsidiary. Drag: assessed above as a cap on the rating at the AA+ level rather than a notch
off the standalone profile, because the ICDs were repaid by every year-end and no default or
covenant issue exists.

**Instruments.** All are plain bank facilities, CP, a secured NCD and a proposed NCD — no hybrid,
no structural enhancement; all rated at the issuer level.

**LT/ST mapping.** AA+ maps to A1+ (ICRA's fixed anchor: AAA/AA → A1+; ICRA_CONVENTIONS §8).

**Outlook.** Stable: the strongest-band financials and Superior liquidity give a wide cushion
against a cyclical downturn; and the group-linkage constraint is not expected to resolve within
the outlook horizon.

> **Proposed view: [ICRA]AA+ (Stable) / [ICRA]A1+** on all instruments; the Rs 300 crore
> proposed NCD at [ICRA]AA+ (Stable).
> **Anchor divergence:** +1 notch above the scorecard anchor (AA). The CLAUDE.md overlay
> requires Committee resolution for *any* divergence at AA+/AAA. The scorecard cannot see that
> its financial composite (1.54) sits in the AA+/AAA cohort while business and governance hold
> the grade down — the documented under-rating at AA+/AAA in the 18-Jul-2026 back-test. To be
> recorded at Step 17c as a named Stage 2 notch.

**Sensitivities (to carry into the report):**
- *Positive:* a sustained gain in M&HCV share and scale with diversification beyond domestic
  CVs; an end to lending to promoter-group companies; subsidiaries becoming self-funding.
- *Negative:* sustained loss of M&HCV share or OPBDITA margin below ~9%; automotive Total
  debt/OPBDITA above 1.5x on a sustained basis; support to subsidiaries, HLF or promoter-group
  entities that erodes liquidity materially; any weakening of governance practices.

---

## 14. Step 14 — Comparison with ICRA's own action (opened only after §13 was written)

ICRA rationale dated **02-Jun-2026** (reference library): "Ratings reaffirmed; rated amount
enhanced"; [ICRA]AA+ (Stable)/[ICRA]A1+. `tools/step14_diff.py` output is in §17.

| Item | This analysis | ICRA (02-Jun-2026) | Explanation |
|---|---|---|---|
| Long-term rating / outlook | [ICRA]AA+ (Stable) | [ICRA]AA+ (Stable) | Same grade reached independently (§13 written first; the grade lines seen at pre-flight were declared in §0) |
| Short-term rating | [ICRA]A1+ | [ICRA]A1+ | Same; fixed anchor AA+ → A1+ |
| Analytical basis | Consolidated excluding the financial-services subsidiaries; HLF's funding needs factored in | Approach-table row: "consolidated financials of ALL"; its KFI footnote and rationale body exclude the NBFC, with funding support to HLF factored in | **Same in substance.** ICRA's table row is shorthand; its own footnote describes the HLF exclusion |
| Liquidity descriptor | **Superior** | Strong | **Postdates the anchor.** ICRA used 31-Dec-2025 data (cash and liquid investments of over Rs 3,800 crore, undrawn lines over Rs 2,000 crore, FY2027 repayments over Rs 676 crore). The audited 31-Mar-2026 position is free liquidity Rs 6,950.80 crore and undrawn lines Rs 2,854.34 crore; FY2027 scheduled repayments are Rs 483.82 crore (note 1.21). The FY2027 CFO alone covers all calls on cash (§11). Kept, with the reason stated in the report |
| KFI, standalone FY2025 | OI 38,752.7; PAT 3,303.3; 12.7%; 8.5%; TOL/TNW 1.2; TD/OPBDIT 0.3; ICR 22.7 | Identical | Agree to the decimal |
| KFI, consolidated FY2025 | OI 48,535.1; PAT 3,382.8; 19.0%; 7.0%; TOL/TNW 4.2; TD/OPBDIT 5.4; ICR 2.3 | OI 48,535.1; PAT 3,351.2; 19.0%; 6.9%; TOL/TNW 4.1; TD/OPBDIT 5.4; ICR 2.3 | PAT gap of 31.6 = the share of profit of JVs/associates (31.58), which ICRA excludes; PAT/OI follows. TOL/TNW 4.16 vs 4.1: ICRA's tangible net worth is probably net of goodwill/intangibles — basis difference, not reconciled |
| Market share | M&HCV 30.3% (MD&A, buses + trucks); trucks 30.0% | Trucks 30.0% "excluding defence" | Same truck figure. The MD&A says AL's truck volumes include defence; ICRA's "excluding defence" basis is not visible in the documents |
| LCV share | 12.7% VAHAN, 0-7.5 tonne cargo (FY2026 AR) | 12.3% | Different measurement basis — this report quotes the company's own figure |
| Key drivers | Strengths: position; strongest-band metrics; liquidity. Challenges: cyclicality; subsidiary support; **promoter-group ICDs and HLF capital**; regulatory/contingent | Strengths: position; margins; capitalisation and liquidity. Challenges: EV capex (~Rs 1,800 crore a year incl. investments); investee entities; cyclicality | **This analysis found something more.** The promoter-group ICDs (note 3.9.1) and HLF's credit-cost doubling are elevated to a driver; ICRA names "investments in group companies" only in its negative sensitivity. ICRA's ~Rs 1,800 crore capex-plus-investment figure is not in the company documents; the model uses Rs 1,200 crore capex + Rs 500 crore support (Rs 1,700 crore), close to it |
| Sensitivities | Upgrade: share/scale, diversification, end of promoter-group ICDs. Downgrade: share loss, margin < 9%, automotive TD/OPBDIT > 1.5x, group support, governance | Upgrade: diversification, share, EV scale-up, margins/RoCE. Downgrade: slowdown, share loss, debt-funded capex/group investments/dividends | Consistent direction; this report quantifies the triggers |
| Methodologies | Corporate (Jul 2025); Commercial Vehicles (Dec 2025); Consolidation (Nov 2024); Liquidity (Mar 2026) | Corporate; Commercial Vehicles | This report also names the approaches it actually applied |
| Rated amounts | Rs 7,479.38 crore (ICRA table imported, verified) | Same | Imported under the amendment; issuer confirmation outstanding |
| Entity list | FY2026 AR holdings (Optare 93.28%, Hinduja Tech 72.93%, ZeBeyond 20.84% effective) | FY2025 AR holdings (Optare 92.59%, Hinduja Tech 72.99%, ZeBeyond 36.50%) | **Postdates the anchor** (FY2026 AR) |

**Mandate details found only in the anchor (REQUIRING ISSUER CONFIRMATION):** term-loan issuance
and maturity years (FY2020-FY2025 / FY2027-FY2032); the Rs 300 crore proposed NCD; the
complexity classification of CP as "Simple".

**Verbatim-reuse guard (FM37):** the rationale was written from the workpaper. Its sentences are
my own, apart from mandated scaffolding (section headers, methodology names, the complexity
paragraph). The `check_sections.py` FM37 probe is the mechanical check (§17).

---

## 15. Step 15 — Analytical package (proposed view; the Committee decides at 17c)

Input gaps and handling: term sheets — handled per §8 (AR plus the imported ICRA table; issuer
confirmation outstanding). Sector-assumptions note — not supplied; the base case uses the
company's MD&A outlook, with a stress and a tail case (§12). Proposed view: **[ICRA]AA+
(Stable)/[ICRA]A1+**. Anchor: AA (Stage 1), +1 to be resolved at 17c. Judgment calls:
(1) liquidity Superior vs ICRA's Strong; (2) the group-linkage cap at AA+ rather than a notch
off; (3) basis — automotive metrics measured at the conservative OPBDIT bound.

---

## 17. Step 17 / 17a — Re-verification and delivery gates

**(a) Computed drift check.** A script extracted every number in the rationale and matched each, at
the rationale's own rounding, against the engine, the model and the spreads. **176 match a computed
value.** Nine more are arithmetic on engine or document figures, each recomputed: 342.9 (sum of
the five contingent-liability lines); 415.5 (ECL allowance 1,462.41 - 1,046.87); 818.7
(1,234.24 - 415.54); 2,069.3 (Optare 1,200 + 498.76 + 370.58); 2,670.4 (1,567.02 + 717.06 +
386.28); 3,876.2 (dividends 2,040.77 + 1,835.42); about 4,240 (FY2027 uses 4,239.67); 5,755.8
(engine net debt -5,755.76 shown as net cash); about 88,000 (market cap 88,390, rounded).
**No unexplained figure remains.**

**(b) Non-computed drift check.** **76 numbers match a figure in the case documents.** The
context-sensitive ones were re-read at their source this session; presence alone does not prove
the right year or entity (FM30):
- market shares: M&HCV 30.3% (MD&A); trucks 30.0% (MD&A line 2968) vs 32.3% FY2023 (FY2024 AR
  line 3097); buses 34.1% (chairman line 64; MD&A line 2970, on an industry base of 61,125
  units); LCV VAHAN 12.7% (line 786);
- operations and targets: touchpoints 2,104; export ambition 25,000 "in the near term";
- group and HLF: HLF equity Rs 200 crore (FY2025 AR line 776); HLF-NDL dates (RBI 08-Aug-2025,
  CCI 17-Feb-2026, BSE 18-May-2026 — lines 5712, 7377); Stage 3 and loan-mix tables (note 3.6,
  ~line 14357);
- other: electoral trust Rs 108 crore standalone (line 8382; consolidated Rs 150 crore, line
  13079); employees 9,891 (ten-year table); dividend Rs 1,468.46 crore declared 28-May-2026;
  NCD terms (FY2026 schedule; call option in the FY2024 AR line 9272).

Corroborated by a second source: OPBDITA (chairman's EBITDA), net cash (chairman), volumes
(segment sum) and borrowings (screener.in). **5 numbers** are attributed to ICRA's 02-Jun-2026
rationale: rated amounts, rating-history dates and term-loan years.

**(c) Corrections made during this pass:**
- the FY2025 exceptional items were itemised (not "write-offs 16.80");
- the Rs 100 crore DRF deposit was removed from free liquidity (7,050.80 -> 6,950.80);
- the term-loan reconciliation was corrected (sales-tax loans 66.41, not 61.50);
- an unsupported Q1 FY2025 "net debt/equity 0.1" was dropped;
- "warranty provisions" was reworded to "provisions" (the unwinding line is not warranty-specific);
- a typed CP tenor was removed;
- the valuation note's "listed parent" was removed;
- the basis was relabelled to consolidated excluding financial services (§5.1).

**(d) Gates (Step 17a), final run:**
- `check_sections.py` — PASS, quality probes clean. The first run's three warnings were each
  verified: the NBFC metric was absent, so Stage 3 was added from note 3.6; the basis was not
  stated in the probe's form, so a statement line was added; and the FM37 hit was a false
  positive (my own workpaper matched the CareEdge footer pattern on the phrase "ICRA and
  CareEdge ratings", now reworded).
- `step14_diff.py` — no material divergence.
- `annotate_scorecard.py` — MATCHES. It compared the short-term grade, because the CP row comes
  first; the long-term grade was checked directly on the sheet: `Rating!C36` = [ICRA]AA+ (Stable).
- `delivery_audit.py` — **READY TO SHARE**: 186/186 tie-outs; coverage 98.1%; section gate PASS;
  scorecard matches; workpaper present; Step 14 clean.


---

## Appendix A — Step 1a pre-flight output (verbatim)

```
==============================================================================
PRE-FLIGHT  |  Ashok Leyland  |  agency ICRA  |  7 documents, 478,857 words
==============================================================================

[0] DOCUMENTS BY DATE - READ THE NEWEST FIRST  (failure mode 26)
      ~2026  AL_ANNUAL-REPORT-2026_Final.md
      ~2025  ALResultsjune2025.md
      ~2024  Annual-Report-FY-2024-25_1.md
      ~2024  un-audited-financial-results-for-the-quarter-ended-June-30-2024.md
      ~2024  un-audited-financial-results-for-the-quarter-ended-September-30-20
      ~2023  Annual-Report-FY-2023-24-1.md
       ?    ALOutcomeofBMNov122025final.md
    *** Newest content appears to be 2026. Any figure taken from an older
        document than this must be justified in the workpaper. ***

[0b] OPERATING METRICS ACROSS DOCUMENTS - ATTRIBUTE EACH TO ITS YEAR  (failure mode 30)
    no metric appears with conflicting values across documents

[0c] AGGREGATE-NOTE CONTAMINANTS - DECOMPOSE BEFORE USING A SUBTOTAL  (failure mode 36)
    !! forex loss/gain:
                29.06   Foreign exchange loss/ (gain)- net                   AL_ANNUAL-REPORT-2026_Final.md
                 4.08   Foreign exchange (gain) / loss - net                 AL_ANNUAL-REPORT-2026_Final.md
                 2.76   Foreign exchange loss - net i                        Annual-Report-FY-2023-24-1.md
                 2.70   Foreign exchange (gain) / loss - net                 Annual-Report-FY-2024-25_1.md
    !! exceptional item:
               384.44   Exceptional items   i                                AL_ANNUAL-REPORT-2026_Final.md
               348.48   Exceptional items                                    AL_ANNUAL-REPORT-2026_Final.md
               119.02   Exceptional items                                    un-audited-financial-results-for-t
               103.73   Exceptional items                                    Annual-Report-FY-2024-25_1.md
    !! profit/loss on asset sale:
                92.83   Profit on sale of investments - net                  AL_ANNUAL-REPORT-2026_Final.md
                92.83   Profit on sale of liquid investments (net)           AL_ANNUAL-REPORT-2026_Final.md
                60.61   Profit on sale of investments - net                  Annual-Report-FY-2023-24-1.md
                60.61   Profit on sale of liquid investments (net)           Annual-Report-FY-2023-24-1.md
    !! impairment / write-off:
               164.90   h. Impairment loss allowance I write off relating 10 un-audited-financial-results-for-t
                51.84   Write off/impairment ofgoodwill and intangible asset AL_ANNUAL-REPORT-2026_Final.md
                21.06   (l)    Impairment loss allowance / write off on trad Annual-Report-FY-2024-25_1.md
                15.74   Write off/impairment of Property, plant and equipmen AL_ANNUAL-REPORT-2026_Final.md
    !! interest / dividend income:
             6,931.82   includes interest income from financial services     AL_ANNUAL-REPORT-2026_Final.md
             5,453.69   includes interest income from financial services     Annual-Report-FY-2024-25_1.md
             1,267.57   • Includes interest income from financial services   un-audited-financial-results-for-t
               219.05   Interest income ii                                   AL_ANNUAL-REPORT-2026_Final.md
    !! fair-value change:
                19.11   Netgain on fair value changes/disposal of investment Annual-Report-FY-2023-24-1.md
                19.11   Net gain on fair value changes / disposal of investm Annual-Report-FY-2024-25_1.md
    !! govt grant / incentive:
               145.92   i) Subsidy receivable from Government                Annual-Report-FY-2024-25_1.md
                71.89   - Export incentives                                  AL_ANNUAL-REPORT-2026_Final.md
                70.68   -     Export incentives                              AL_ANNUAL-REPORT-2026_Final.md
                52.64   - Export incentives                                  Annual-Report-FY-2024-25_1.md
    ^^ BINDING: each line above is a COMPONENT of an aggregate note. Before any
       operating-profit measure (OPBDIT/OPBDITA/PBILDT/EBITDA) is published, each
       must carry a WRITTEN include-or-exclude decision in the workpaper's
       normalisation note. A subtotal may NOT be fed into a ratio until its
       components have been read. 'No exceptional item was disclosed' is an
       ABSENCE CLAIM about these documents (failure mode 20) - a forex loss is
       not captioned 'exceptional', so that sentence does not cover it.

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
    !! current maturities inside CURRENT borrowings:
         483.82, 383.21                 Current maturities of long-term debts              AL_ANNUAL-REPORT-2026_Fina
         16,346.52, 11,633.52           c)                                                 AL_ANNUAL-REPORT-2026_Fina
         15,670.19, 11,070.03           -     Current maturities of long-term debt         AL_ANNUAL-REPORT-2026_Fina
         638.58, 1,145.24               Current maturities of long-term debts              Annual-Report-FY-2023-24-1
    !! acceptances / bill discounting inside borrowings or payables:
         151.92                         Proceeds under a supplier finance arrangement      AL_ANNUAL-REPORT-2026_Fina
         64.66                          Repayments under a supplier finance arrangement    AL_ANNUAL-REPORT-2026_Fina
         87.25                          Liabilities under Supplier finance arrangement     AL_ANNUAL-REPORT-2026_Fina
         87.25                          Total supplier finance liabilities                 AL_ANNUAL-REPORT-2026_Fina
    !! earmarked / margin / restricted balances inside CASH:
         0.37                           3                                                  AL_ANNUAL-REPORT-2026_Fina
         13.35, 13.52                   i)                                                 AL_ANNUAL-REPORT-2026_Fina
         32.61, 32.61                   ii)                                                AL_ANNUAL-REPORT-2026_Fina
         13.35, 13.52                   i) Unclaimed                                       AL_ANNUAL-REPORT-2026_Fina
    !! lease liabilities shown apart from borrowings:
         29.60, 31.74                   (ii)<br>Lease liabilities<br>ii                    AL_ANNUAL-REPORT-2026_Fina
         13.74, 14.54                   (ii)<br>Lease liabilities                          AL_ANNUAL-REPORT-2026_Fina
         14.80, 59.33                   Payments of Lease liability                        AL_ANNUAL-REPORT-2026_Fina
         43.34, 46.28                   Lease Liability                                    AL_ANNUAL-REPORT-2026_Fina
    ^^ BINDING: each line above sits INSIDE a balance-sheet caption that a ratio
       will use. Before publishing overall gearing, working-capital dependence,
       long-term debt or a liquidity figure, SPLIT the caption and state the
       split. A caption is not a ratio input until its components have been read
       - the same rule failure mode 36 applies to the P&L, applied to the
       balance sheet, where it had no probe at all.

[0f] PROMOTER / RELATED-PARTY UNSECURED LOANS  (failure mode 48, CRISIL only)
     n/a - CRISIL's four-factor test does not apply to a ICRA case

[1] PRIOR RATING ACTION IN THE REFERENCE LIBRARY  (Step 14 / failure mode 24)
    *** PRESENT - Step 14 IS APPLICABLE. Open these AFTER forming your view, and
        produce a divergence table. You may NOT write 'no prior rating action'. ***
      - CareEdge: Ashok Leyland Limited_22 Sep 2025.md
      - ICRA: Ashok Leyland Limited_02 Jun 2026_143433.md

    >>> RATED AMOUNTS FOUND IN THE LIBRARY <<<
      Failure mode 29: never write 'to be confirmed by issuer' while a
      SAME-ISSUER line exists. Condition (1) is MET - the library counts.
      !! CONFIRM THE ENTITY FIRST. A PARENT, SIBLING OR PEER IS NOT THE
         ISSUER - importing a peer's rated amount is a WORSE error than
         leaving it TBC. [match n/m] = how many of the issuer's name
         tokens the filename carries. Highest score is the candidate;
         it still needs your confirmation that it is the same company.
      from Ashok Leyland Limited_22 Sep 2025.md  [match 2/2]
        |Long-term bank facilities|200.00 (Reduced from 300.00)|CARE AA+; Stable|Reaffirmed|
        |Long-term / Short-term bank facilities|3,700.00|CARE AA+; Stable / CARE A1+|Reaffirmed|
        |Short-term bank facilities|300.00|CARE A1+|Reaffirmed|
        |Non-convertible debentures|200.00|CARE AA+; Stable|Reaffirmed|
        |Commercial paper|2,000.00|CARE A1+|Reaffirmed|
      from Ashok Leyland Limited_02 Jun 2026_143433.md  [match 2/2]
        |**Commercial Paper**|2,000.00|2,000.00|[ICRA]A1+; reaffirmed|
        |**Non-Convertible Debenture**|200.00|200.00|[ICRA]AA+ (Stable); reaffirmed|
        |**Proposed Non-convertible** **debenture**|0.00|300.00|[ICRA]AA+ (Stable): assigned|
        |**Long term/ Short term: Fund** **based limits**|2,000.00|2,000.00|[ICRA]AA+ (Stable)/ [ICRA]A1+; reaff
        |**Long term/ Short term: Non-fund** **based limits**|1,500.00|1,500.00|[ICRA]AA+ (Stable)/ [ICRA]A1+; r
        |**Long-term – Fund based - Term** **loans**|982.50|729.38|[ICRA]AA+ (Stable); reaffirmed|

[1b] PEER REPORTS - ICRA, SAME SECTOR  (failure modes 32/33)
    * NMDC Limited_03 Feb 2023_117762.md   (score 6.2 on corporate+methodology)
    * Reliance Power Limited_25 Nov 2025_139188.md   (score 6.2 on corporate+methodology)
        Brief Financials rows THIS AGENCY USES IN THIS SECTOR:
          - Operating income
          - PAT
          - OPBDIT/OI
          - PAT/OI
          - Total outside liabilities/Tangible net worth (times)
          - Total debt/OPBDIT (times)
          - Interest coverage (times)
    * Rationale-Ascent_Hotels_Private_Limited.md   (score 5.4 on corporate+specific)
        Brief Financials rows THIS AGENCY USES IN THIS SECTOR:
          - Operatng income(Rs. crore)
          - PAT(Rs. crore)
          - OPBDIT/OI(%)
          - PAT/OI(%)
          - Total outside liabilites/Tangible net worth(tmes)
          - Total debt/OPBDIT(tmes)
          - Interest coverage (tmes)
    *** These rows are the REQUIRED set, and the footnotes are the agency's
        RATIO DEFINITIONS. Reproduce them. A metric may be omitted only after
        checking a peer above - never by reasoning from another sector. ***
    !! TOP PEERS DISAGREE ON THE ROW SET - the sector match is
       AMBIGUOUS. Confirm which peer is the same ENTITY TYPE before
       relying on peer_rows.json, and overwrite it if the top hit is
       the wrong kind of company.
    PEER NORM over 20 peers: 0 carry a LONG-TERM rating, 11 a short-term rating.
    -> wrote peer_rows.json (0 rows from NMDC Limited_03 Feb 2023_117762.md; peer norm 0/20 LT). check_sections.py VERIFIES both.

[1c] STEP 12 - THE FORWARD VIEW IS NOT OPTIONAL  (failure mode 35)
    entity_type 'corporate' -> required artefact:
      Full 5-yr 3-statement model (corporate with term debt).
    PLUS Step 12b: fill Rating_Scorecard_<Company>.xlsx from AUDITED ACTUALS.
    If a lighter treatment is right, record WHY in case.json as
    'step12_scaling_decision' - the delivery gate refuses the case without one.

[2] CREDIT-RATING NOTE in the issuer's own AR  (Step 7b)
    *** PRESENT - 65 match(es)
        If PRESENT you already know the outstanding rating - declare the anchor exposure and NEVER write 'no rating disclosed'.
        e.g. ...11 crores on March 31, 2025. Details pertaining to the credit rating of the debt instruments are provided in t...
        e.g. ...ficer|Mr. N Ramanathan, Company Secretary|| ## U. **Credit Ratings** |**Name of the Agency**|**Type of Instrum...

[3] SUBSIDIARIES / entities to NAME  (failure mode 17)
    *** PRESENT - 1619 match(es)
        Every entity must be NAMED in the entities-consolidated annexure regardless of materiality.
        e.g. ...extended our presence in the Gulf region through a new wholly owned subsidiary in Saudi Arabia ? a local assem...
        e.g. ...brought concrete proof of commercial viability. Our EV subsidiary, Switch Mobility India, achieved net profita...

[4] ESG data  (failure modes 19/20)
    *** PRESENT - 646 match(es)
        If PRESENT you may NOT write 'ESG data not extractable'. Extract and quote the numbers.
        e.g. ...roup?s consolidated performance. # **Sustainability, CSR and Our Stakeholders** Our sustainability commitment...
        e.g. ...iness. On the environmental side, we have achieved 77% renewable energy status across our operations, up from ...

[5] INSTRUMENT details  (Step 7b)
    *** PRESENT - 129 match(es)
        Populate Annexure I from these; mark only genuinely undisclosed amounts as TBC.
        e.g. ...## **FINANCE ?** ## **Long term funding** ## (a) **Non-Convertible Debentures (NCDs)** During the year under r...
        e.g. ...ear under review, your Company did not issue any fresh Non-Convertible Debentures (NCDs), nor were any NCDs re...

[6] CAPEX / investment cycle
    *** PRESENT - 87 match(es)
        Capital-intensive sectors: capex must appear in the rationale.
        e.g. ...cipal pillars: (i) decisive acceleration in government capital expenditure (ii) robust agricultural output tra...
        e.g. ...m the stimulus to the consumer specific sectors. The capex spending during FY26 reached ` 10.75 lakh crores ag...

[7] SHAREHOLDING / promoter stake
    *** PRESENT - 7 match(es)
        Quantify the controlling stake - never write 'controlling shareholder' bare.
        e.g. ...witch UK from Dana Ltd., thereby increasing its direct holding in Switch UK to 99.57%. Consequently, Optare Pl...
        e.g. ...NCIAL STATEMENTS** |`**Crores**<br>**% of**<br>**hareholding**|61.12%|66.67%|93.15%<br>93.28%<br>100.00%<br>10...

[8] AUDITOR opinion / KAM / Emphasis of Matter
    *** PRESENT - 182 match(es)
        An EOM or qualification is rating-relevant regardless of quantum (R13).
        e.g. ...tandalone Financial Statements (Pages 113 to 208)** |Independent Auditors? Report to the members ................
        e.g. ...solidated Financial Statements (Pages 209 to 335)** |Independent Auditors? Report to the members ................

[9] SECTOR-DEFINING METRIC  (failure mode 21)
    sector detected (133 trigger hits; next best 'cost of production per tonne' at 82) -> the rationale MUST quote: utilisation / EBITDA per tonne
    *** PRESENT in documents - 1 match(es) -> EXTRACT IT
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
