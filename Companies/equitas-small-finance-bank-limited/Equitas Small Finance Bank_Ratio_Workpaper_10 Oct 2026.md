# Equitas Small Finance Bank Limited — Ratio Workpaper (CareEdge)

**Prepared:** 10 Oct 2026 · **Agency style:** CareEdge · **Engagement:** new assignment in this
exercise (CareEdge already rates the bank — Step 14 applies) · **Data cutoff:** audited FY2026
(31-Mar-2026); Q1 FY2027 (reviewed, 28-Jul-2026) used only where readable ·
**Engine:** `compute_ratios.py`, 102/102 tie-outs, mutation coverage 92.6% ·
**Spreads:** `Equitas_SFB_Financial_Spreads.xlsx` (102/102 internal; 32/32 against screener.in)

---

## 0. Independence and anchor exposure (declared)

| Exposure | How | What was seen | Mitigation |
|---|---|---|---|
| Step 1a pre-flight [1] | Prints the rated-amount lines of same-issuer actions | CareEdge 06-Oct-2025: issuer rating and Lower Tier II CARE AA-; Stable; CD CARE A1+ | View built bottom-up from the compliance map and peer calibration; the Step 13 view is written before Step 14 opens the report |
| Bank's own AR (Corporate Governance report, credit ratings) | Listed banks disclose ratings | The same CareEdge ratings, plus CRISIL A1+ (CD) and India Ratings IND AA-/Stable | As above; the amounts in the AR are usable company data |
| Step 7b table import | FM29 makes this a Step 7b action | Only the rated-amount table, extracted by anchoring on its own header and stopping at "Details of instruments" (the Ashok Leyland lesson) | Nothing else of the report was read before §13 |

---

## 1. Step 1 — Inventory, engagement, information adequacy

| # | Document | Period | Status | Basis |
|---|---|---|---|---|
| 1 | Equitas-SFB-Integrated-Annual-Report-2025-26.md | FY2026 (comparative FY2025, restated) | Audited — ASA & Associates LLP and Suri & Co. (joint), unmodified | Standalone |
| 2 | Equitas-AR-2024-25.md | FY2025 (comparative FY2024) | Audited, unmodified | Standalone |
| 3 | ESFBL-Annual-Report_2023-24.md | FY2024 (comparative FY2023) | Audited, unmodified | Standalone |
| 4 | OutcomeofBoardmeetQ1FY27-1.md | Q1 FY2027 (to 30-Jun-2026) | Limited review, 28-Jul-2026 | Standalone |
| 5 | OutcomeofBoardmeetQ4FY26.md | Q4 / FY2026 | Audited results | Standalone |
| 6 | OutcomeofBoardMeetingQ3.md | Q3 / 9M FY2026 | Limited review | Standalone |
| 7 | OutcomeofBoardmeeting_Q2.md | Q2 / H1 FY2026 | Limited review | Standalone |
| 8 | OutcomeofBoardMeetingQ1-2.md | Q1 FY2026 | Limited review | Standalone |

**Intake correction (HLE Glascoat lesson).** `case.json` was created as sector "Corporate -
Manufacturing (master criteria)", routing "corporate", while every document and every selected
methodology is for a bank. It was corrected to CareEdge's own intake option, "Bank / SFB / RRB",
routing "bank" (webapp option list), before the pre-flight was run.

**Missing:**
- (a) Term sheets / sanction letters. The rated programme is imported under the amendment (§8),
  and the bond ISINs, coupons and maturities come from the bank's own documents.
- (b) Sector-assumptions note. Not supplied; the base case uses the bank's own trajectory with a
  stress case and a tail case.
- (c) Pillar 3 disclosures. Not supplied; the capital, LCR and NSFR notes in the audited AR cover
  the need.

**Engagement:** new assignment (R15), with a long-term rating plus outlook and a short-term CD
rating. **Information adequacy:** adequate.

---

## 2. Step 1a — Pre-flight (verbatim in Appendix A)

Present:
- the same-issuer prior action (CareEdge 06-Oct-2025);
- the AR ratings note (37 matches);
- entities (111 matches; the bank has none — Q1 FY2027 note 13);
- ESG data (377 matches);
- instrument details (61 matches);
- the auditor's opinion and KAMs (57 matches);
- the sector metrics NIM, GNPA, CRAR and CASA (112 matches).

Absent, with the search recorded: promoter shareholding (0 matches). This is consistent with a
widely held bank whose holding company was amalgamated in FY2023.

Flags acted on:
- **[0b]** branch and city counts differ across ARs — only the FY2026 figure (1,060 branches) is
  quoted.
- **[0c]** "Excess provision reversed / write-off loans" (1,125.02; 937.30) are NPA-movement
  components, not P&L contaminants. Earnings are analysed on the bank's own P&L, where tax sits
  inside "Provisions and contingencies" and is stripped out using note 18.14(f).
- **[0e]** cash includes lien-marked deposits of 6.11 (FY2026). These are excluded from cash
  equivalents by the bank itself, and no liquidity ratio here uses them.
- **[10]** CareEdge's LT-ST mapping table is corrupted. The short-term grade is therefore checked
  against the issuer's own published ratings: the AR shows CARE A1+ for CDs alongside CARE AA-.

---

## 3. Step 1b — Document Read Log

| # | Document | What it contributes | Material items |
|---|---|---|---|
| 1 | FY2026 integrated AR | Statements and schedules (Rs '000), Schedule 18 regulatory notes, KAMs, governance, BRSR | PAT Rs 103.08 crore; CRAR 20.31%; GNPA 2.60%; slippages 2,125.40; write-offs 919.97; NPA sale to ARCs (principal 565.40, consideration 184.00); IBPC Rs 2,000 crore issued; second Lower Tier II bond (Rs 500 crore, 9.6%, 31-Jul-2030); top-20 depositors 20.61%; LCR 179.64 → 138.45% across the year; NSFR 114.01%; frauds 488 cases / Rs 18.33 crore; no RBI penalty; complaints 29,533 (23,755). **MD&A prose is unreadable** (font converted to missing glyphs; tables legible and used) |
| 2 | FY2025 AR | FY2025/FY2024 statements and notes; microfinance narrative | Microfinance book cut 28% to Rs 4,527 crore (12% of advances); first Lower Tier II bond (Rs 500 crore, 9.6%, 05-Dec-2030); floating provision Rs 180 crore created; CRAR 20.60% |
| 3 | FY2024 AR | FY2024/FY2023 statements; product-mix table; amalgamation | PAT Rs 798.96 crore; ROA 1.96%; Equitas Holdings amalgamated (FY2023 P&L adjustment −878.25); deposits +43%; FY2023 CASA 42.2% |
| 4 | Q1 FY2027 results | Segment results; notes | PBT Rs 244.07 crore (Q1 FY2026: −297.48); total assets Rs 64,282.57 crore; Rs 520.30 crore of loans not in default assigned; SRs Rs 175.22 crore gross; no subsidiary. **The P&L statement and Reg 52(4) table did not convert** — no Q1 FY2027 GNPA or CRAR is used |
| 5 | Q4 FY2026 results | Quarterly P&L, Reg 52(4) ratios | Q4 PAT 212.68, Q3 90.03; net worth excluding DTA and intangibles 5,582.45 (FY2026) and 5,592.58 (FY2025), tied to the engine's TNW; total debt / total assets 9.52% (4.04%) |
| 6 | Q3 FY2026 results | Quarter results | Q3 profit returns (90.03, per the Q4 file); readable notes only |
| 7 | Q2 FY2026 results | Quarter results | Statement table did not convert; Q2 PAT derived as the FY2026 residual: 103.08 + 223.78 − 90.03 − 212.68 = 24.15 |
| 8 | Q1 FY2026 results | Quarter results | Q1 FY2026 net loss (223.78); FY2025 PAT 147.05 |

**Corroboration register:**

| Figure | Source 1 | Source 2 | Result |
|---|---|---|---|
| Tangible net worth FY2025/26 | Engine 5,592.57 / 5,582.45 | Reg 52(4) "net worth excluding DTA, revaluation & intangibles" 5,592.58 / 5,582.45 | Agree (tie-out) |
| NII, operating profit FY2025/26 | Engine | MD&A table 3,251.61 / 3,391.17; 1,334.27 / 1,264.97 | Agree |
| GNPA / NNPA / PCR, all years | Engine (computed from amounts) | Printed ratios | Agree |
| CRAR / Tier I, all years | Engine | Printed | Agree |
| ROA FY2025/26 (bank basis) | AR business ratios 0.30 / 0.18 | Q4 FY2026 results 0.30 / 0.18 | Agree |
| All BS/P&L headlines FY2023-26 | Engine | screener.in (32 comparisons) | Agree within rounding |
| Microfinance share FY2025 | 4,527 / 37,986 = 11.92% | AR text "12%" | Agree |
| Microfinance ~10% (FY2026) | Legible AR fragment | Unsecured advances 3,827.35 = 8.95% of net advances | Consistent; FM15 applied |
| Top-20 depositors FY2025 | Printed 17.60% | 7,105.81 / 43,102.31 = 16.49% | **Diverge** — denominator not disclosed; printed figure quoted |

**Trends:**
- PAT 573.59 → 798.96 → 147.05 → 103.08.
- ROTA (CareEdge basis) 1.99% → 0.30% → 0.18% (FY2024-26).
- NIM 7.67% → 6.63% → 5.98%.
- Slippage ratio 5.75% → 4.47% → 6.64% → 5.93%.
- Write-off ratio 1.56% → n/m → 2.24% → 2.11%.
- GNPA 2.76% → 2.61% → 2.89% → 2.60%.
- CASA 42.23% → 31.98% → 28.78% → 26.21%.
- CRAR 23.80% → 21.70% → 20.60% → 20.31%; Tier I 23.08% → 16.68%; leverage ratio 13.21% → 8.84%.
- Gross advances growth 19.9% / 17.5% / 18.0%; deposits growth 42.5% / 19.3% / 8.0%.
- Credit/deposit 85.7% (FY2024) → 91.9% (FY2026).
- Microfinance share 18.75% → 18.25% → 11.92% → ~10%.

---

## 4. Steps 2-4 — Routing, methodology, peers

**Route:** CareEdge "Rating Methodology – Banks" (March 2025) — scope: "debt instruments of
banks including SFBs and regional rural banks". The other papers applied:
- "Financial Ratios – Financial Sector" (February 2025) — definitions;
- "Criteria for Rating Basel III – Hybrid Capital Instruments issued by Banks" (March 2025) — the
  Lower Tier II bonds;
- "Issuer Rating" (February 2025);
- "Rating of Short-Term Instruments" (February 2025) — CDs;
- "Assigning Outlook or Rating Watch" — outlook;
- "Policy on Default Recognition" (January 2025).

All were read this session (the Banks and Ratios papers in full).

**Factor structure (Banks methodology):** quantitative — A) capital adequacy, B) asset quality,
C) resources, D) liquidity, E) earnings quality. Qualitative — a) industry and operating
environment, b) ownership, c) management, d) risk management (market, operational and digital),
e) regulatory compliance, f) accounting quality, g) size and market presence. The paper has **no
numeric indicative bands**: assessment is descriptive and peer-relative ("A detailed inter-bank
analysis is carried out"). Regulatory floors quoted: SFB minimum CAR 15%, Tier I 7.5% (Basel II),
leverage ratio 4.5%. Seniority: "Infrastructure bonds and FDs are senior to Tier-II instruments"
and the FD rating "may be higher by one notch". Hybrid paper: Basel III Tier II rated "similar or
close to the rating of Lower Tier II instruments under Basel II", with notching down only "for
lower rated banks".

**Peers (CareEdge library, craft and calibration only):**

| Peer | Grade | Total assets (Rs crore) | ROTA | GNPA | CAR | Other | Liquidity |
|---|---|---|---|---|---|---|---|
| Ujjivan SFB (23-Mar-2026) | CARE AA-; Stable | 52,078 | 1.10% (9M FY2026) | 2.38% | 21.62% | CASA 27%; micro-banking 52% | Adequate |
| AU SFB (01-Dec-2025) | CARE AA; Stable | ~1.65 lakh | 1.41% | — | 18.78% | — | Adequate |
| Capital SFB (27-Feb-2026) | CARE A; Stable | 12,091 | — | — | — | — | — |
| ESAF SFB (02-Sep-2025) | CARE A-; Negative | — | negative | — | — | — | — |
| Utkarsh SFB (05-Jan-2026) | CARE A; Negative | — | negative | 12.42% | — | — | Strong |

The format is learnt from these: rating table → rationale and key rating drivers → sensitivities
→ analytical approach → outlook → key strengths and weaknesses → liquidity → ESG → applicable
criteria → about the company and industry → industry classification → brief financials (total
income, PAT, total assets, NIM, ROTA, GNPA, NNPA, CAR) → non-cooperation → other information →
Annexures 1-5.

---

## 5. Step 5 — Extraction, basis, normalisation

**Basis (R12):** standalone. There are no subsidiaries, associates or JVs (Q1 FY2027 note 13),
which matches the case declaration and CareEdge's SFB peers.

**Units:** statements are in Rs '000 as printed (Indian digit grouping), converted once in code;
regulatory notes are in Rs crore.

**Earnings normalisation ([0c]):**
- "Provisions and contingencies" includes tax. Note 18.14(f) splits it, so credit cost = the line
  less tax (current 85.41 + deferred −60.36 = 25.05 in FY2026).
- The FY2025 floating provision (180.00) and FY2026 provision for non-performing investments
  (64.18) are credit costs and are kept.
- Other income includes PSLC fees (the bank sold PSLCs of Rs 1,800 crore in FY2026), recoveries
  from written-off accounts (345.97) and overdue penal charges (88.42). These are recurring for
  this business model and are retained, with the composition named.
- There are no exceptional items in the P&L. The FY2023 amalgamation adjustment went to
  reserves, not to profit.

**Balance-sheet splits ([0e]):**
- Borrowings of Rs 5,772.55 crore include the Lower Tier II bonds (Rs 1,000 crore). The rest of
  the split is not disclosed.
- IBPCs of Rs 2,000 crore were issued against advances (Schedule 9 footnote).
- Deposits are split per Schedule 3, and CASA is computed from it.
- Lien-marked bank deposits of 6.11 are excluded from cash equivalents by the bank.

---

## 6. Step 6 — Ratio suite, tie-outs, coverage (engine)

**A. CareEdge financial-sector ratio suite - standalone (Rs crore / %)**

| Metric | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|---:|
| Total income | 4,831.46 | 6,285.07 | 7,223.21 | 7,867.78 |
| Interest earned | 4,161.88 | 5,486.40 | 6,311.73 | 6,794.24 |
| Net interest income | 2,544.72 | 3,079.76 | 3,251.61 | 3,391.17 |
| Other income | 669.59 | 798.67 | 911.49 | 1,073.55 |
| Operating expenses | 2,038.30 | 2,501.07 | 2,828.83 | 3,199.75 |
| Pre-provision operating profit | 1,176.01 | 1,377.36 | 1,334.27 | 1,264.97 |
| Credit cost (provisions excl. tax) | 407.20 | 314.23 | 1,135.42 | 1,136.84 |
| PBT | 768.81 | 1,063.13 | 198.85 | 128.13 |
| Tax | 195.22 | 264.17 | 51.80 | 25.05 |
| PAT | 573.59 | 798.96 | 147.05 | 103.08 |
| Total assets | 34,958.13 | 45,303.87 | 52,835.63 | 60,610.36 |
| Net worth | 5,157.95 | 5,968.70 | 6,072.52 | 6,124.83 |
| Tangible net worth | 4,796.85 | 5,537.37 | 5,592.57 | 5,582.45 |
| Deposits | 25,348.48 | 36,129.20 | 43,102.31 | 46,533.09 |
| Borrowings | 2,973.76 | 1,787.53 | 2,136.99 | 5,772.55 |
| Advances (net) | 25,798.56 | 30,964.30 | 36,208.89 | 42,751.29 |
| Overall gearing (deposits + borrowings)/TNW (x) | 5.90 | 6.85 | 8.09 | 9.37 |
| Borrowings (incl. Tier II)/TNW (x) | 0.62 | 0.32 | 0.38 | 1.03 |
| CASA ratio (%) | 42.23 | 31.98 | 28.78 | 26.21 |
| Credit/deposit (%) | 101.78 | 85.70 | 84.01 | 91.87 |
| CRAR (%) | 23.80 | 21.70 | 20.60 | 20.31 |
| Tier I (%) | 23.07 | 20.71 | 17.84 | 16.68 |
| GNPA (%) | 2.76 | 2.61 | 2.89 | 2.60 |
| NNPA (%) | 1.21 | 1.17 | 0.98 | 0.72 |
| PCR incl. floating (%) | 56.90 | 56.06 | 66.83 | 73.03 |
| Net NPA/TNW (%) | 6.50 | 6.52 | 6.33 | 5.48 |
| Slippage ratio (%) | 5.75 | 4.47 | 6.64 | 5.93 |
| Write-off ratio (%) | 1.56 | - | 2.24 | 2.11 |
| Cost to income (%) | 63.41 | 64.49 | 67.95 | 71.67 |
| Microfinance share of gross advances (%) | 18.75 | 18.25 | 11.92 | - |
| Growth in gross advances (%) | - | 19.89 | 17.49 | 18.03 |
| Growth in deposits (%) | - | 42.53 | 19.30 | 7.96 |
| Growth in PAT (%) | - | 39.29 | -81.59 | -29.90 |
| NIM (%) | - | 7.67 | 6.63 | 5.98 |
| ROTA (%) | - | 1.99 | 0.30 | 0.18 |
| RONW (%) | - | 15.46 | 2.64 | 1.84 |
| Credit cost / avg total assets (%) | - | 0.78 | 2.31 | 2.00 |
| Opex / avg total assets (%) | - | 6.23 | 5.76 | 5.64 |
| Other income / avg total assets (%) | - | 1.99 | 1.86 | 1.89 |
| Cost of funds (%) | - | 7.27 | 7.36 | 6.98 |
| Net stressed assets/TNW (%) | - | - | 8.65 | 6.85 |
| Yield on advances (%) | - | - | - | 15.12 |

**B. Tie-out register (102/102 reconcile)**

| # | Check | Computed | Disclosed | Tol | Result | Source |
|---|---|---:|---:|---:|---|---|
| 1 | Balance sheet assets sum to printed total, FY2023 | 34,958.13 | 34,958.13 | 0.00 | PASS | balance sheet |
| 2 | Balance sheet liabilities sum to printed total, FY2023 | 34,958.13 | 34,958.13 | 0.00 | PASS | balance sheet |
| 3 | PAT from P&L lines = printed net profit, FY2023 | 573.59 | 573.59 | 0.00 | PASS | profit and loss account |
| 4 | Total income = interest earned + other income, FY2023 | 4,831.46 | 4,831.46 | 0.00 | PASS | profit and loss account |
| 5 | Provisions note components = P&L provisions line, FY2023 | 602.42 | 602.42 | 0.02 | PASS | note 18.14(f) vs P&L |
| 6 | GNPA movement: opening + additions - reductions = closing, FY2023 | 723.96 | 723.96 | 0.02 | PASS | asset-quality note |
| 7 | Gross advances = standard + gross NPA, FY2023 | 26,210.50 | 26,210.50 | 0.02 | PASS | asset-quality note |
| 8 | Net NPA = gross NPA - NPA provisions - floating provisions, FY2023 | 312.01 | 312.01 | 0.02 | PASS | asset-quality note |
| 9 | GNPA ratio computed = printed, FY2023 | 2.76 | 2.76 | 0.01 | PASS | NPA ratio table |
| 10 | NNPA ratio on balance-sheet net advances = printed, FY2023 | 1.21 | 1.21 | 0.01 | PASS | NPA ratio table |
| 11 | PCR incl. floating = printed, FY2023 | 56.90 | 56.90 | 0.02 | PASS | NPA ratio table |
| 12 | Total capital = Tier I + Tier II, FY2023 | 4,727.25 | 4,727.25 | 0.02 | PASS | regulatory capital note |
| 13 | CRAR computed = printed, FY2023 | 23.80 | 23.80 | 0.01 | PASS | regulatory capital note |
| 14 | Tier I computed = printed, FY2023 | 23.07 | 23.08 | 0.01 | PASS | regulatory capital note |
| 15 | PBT = PAT + tax (note 18.14(f)), FY2023 | 768.81 | 768.81 | 0.02 | PASS | MD&A / AR text (FY2023 none printed - identity only) |
| 16 | Balance sheet assets sum to printed total, FY2024 | 45,303.87 | 45,303.87 | 0.00 | PASS | balance sheet |
| 17 | Balance sheet liabilities sum to printed total, FY2024 | 45,303.87 | 45,303.87 | 0.00 | PASS | balance sheet |
| 18 | PAT from P&L lines = printed net profit, FY2024 | 798.96 | 798.96 | 0.00 | PASS | profit and loss account |
| 19 | Total income = interest earned + other income, FY2024 | 6,285.07 | 6,285.07 | 0.00 | PASS | profit and loss account |
| 20 | Provisions note components = P&L provisions line, FY2024 | 578.40 | 578.40 | 0.02 | PASS | note 18.14(f) vs P&L |
| 21 | GNPA movement: opening + additions - reductions = closing, FY2024 | 821.28 | 821.28 | 0.02 | PASS | asset-quality note |
| 22 | Gross advances = standard + gross NPA, FY2024 | 31,424.68 | 31,424.68 | 0.02 | PASS | asset-quality note |
| 23 | Net NPA = gross NPA - NPA provisions - floating provisions, FY2024 | 360.90 | 360.90 | 0.02 | PASS | asset-quality note |
| 24 | GNPA ratio computed = printed, FY2024 | 2.61 | 2.61 | 0.01 | PASS | NPA ratio table |
| 25 | NNPA ratio on balance-sheet net advances = printed, FY2024 | 1.17 | 1.17 | 0.01 | PASS | NPA ratio table |
| 26 | PCR incl. floating = printed, FY2024 | 56.06 | 56.06 | 0.02 | PASS | NPA ratio table |
| 27 | Total capital = Tier I + Tier II, FY2024 | 5,372.71 | 5,372.71 | 0.02 | PASS | regulatory capital note |
| 28 | CRAR computed = printed, FY2024 | 21.70 | 21.70 | 0.01 | PASS | regulatory capital note |
| 29 | Tier I computed = printed, FY2024 | 20.71 | 20.71 | 0.01 | PASS | regulatory capital note |
| 30 | PBT = PAT + tax (note 18.14(f)), FY2024 | 1,063.13 | 1,063.12 | 0.02 | PASS | MD&A / AR text (FY2023 none printed - identity only) |
| 31 | Deposit lines sum to Schedule 3 total, FY2024 | 36,129.20 | 36,129.20 | 0.00 | PASS | Schedule 3 |
| 32 | Balance sheet assets sum to printed total, FY2025 | 52,835.63 | 52,835.63 | 0.00 | PASS | balance sheet |
| 33 | Balance sheet liabilities sum to printed total, FY2025 | 52,835.63 | 52,835.63 | 0.00 | PASS | balance sheet |
| 34 | PAT from P&L lines = printed net profit, FY2025 | 147.05 | 147.05 | 0.00 | PASS | profit and loss account |
| 35 | Total income = interest earned + other income, FY2025 | 7,223.21 | 7,223.21 | 0.00 | PASS | profit and loss account |
| 36 | Provisions note components = P&L provisions line, FY2025 | 1,187.22 | 1,187.22 | 0.02 | PASS | note 18.14(f) vs P&L |
| 37 | GNPA movement: opening + additions - reductions = closing, FY2025 | 1,067.73 | 1,067.73 | 0.02 | PASS | asset-quality note |
| 38 | Gross advances = standard + gross NPA, FY2025 | 36,922.42 | 36,922.42 | 0.02 | PASS | asset-quality note |
| 39 | Net NPA = gross NPA - NPA provisions - floating provisions, FY2025 | 354.20 | 354.20 | 0.02 | PASS | asset-quality note |
| 40 | GNPA ratio computed = printed, FY2025 | 2.89 | 2.89 | 0.01 | PASS | NPA ratio table |
| 41 | NNPA ratio on balance-sheet net advances = printed, FY2025 | 0.98 | 0.98 | 0.01 | PASS | NPA ratio table |
| 42 | PCR incl. floating = printed, FY2025 | 66.83 | 66.83 | 0.02 | PASS | NPA ratio table |
| 43 | Total capital = Tier I + Tier II, FY2025 | 6,088.84 | 6,088.84 | 0.02 | PASS | regulatory capital note |
| 44 | CRAR computed = printed, FY2025 | 20.60 | 20.60 | 0.01 | PASS | regulatory capital note |
| 45 | Tier I computed = printed, FY2025 | 17.84 | 17.84 | 0.01 | PASS | regulatory capital note |
| 46 | PBT = PAT + tax (note 18.14(f)), FY2025 | 198.85 | 198.85 | 0.02 | PASS | MD&A / AR text (FY2023 none printed - identity only) |
| 47 | Deposit lines sum to Schedule 3 total, FY2025 | 43,102.31 | 43,102.31 | 0.00 | PASS | Schedule 3 |
| 48 | Balance sheet assets sum to printed total, FY2026 | 60,610.36 | 60,610.36 | 0.00 | PASS | balance sheet |
| 49 | Balance sheet liabilities sum to printed total, FY2026 | 60,610.36 | 60,610.36 | 0.00 | PASS | balance sheet |
| 50 | PAT from P&L lines = printed net profit, FY2026 | 103.08 | 103.08 | 0.00 | PASS | profit and loss account |
| 51 | Total income = interest earned + other income, FY2026 | 7,867.78 | 7,867.78 | 0.00 | PASS | profit and loss account |
| 52 | Provisions note components = P&L provisions line, FY2026 | 1,161.89 | 1,161.89 | 0.02 | PASS | note 18.14(f) vs P&L |
| 53 | GNPA movement: opening + additions - reductions = closing, FY2026 | 1,134.89 | 1,134.89 | 0.02 | PASS | asset-quality note |
| 54 | Gross advances = standard + gross NPA, FY2026 | 43,580.10 | 43,580.10 | 0.02 | PASS | asset-quality note |
| 55 | Net NPA = gross NPA - NPA provisions - floating provisions, FY2026 | 306.08 | 306.08 | 0.02 | PASS | asset-quality note |
| 56 | GNPA ratio computed = printed, FY2026 | 2.60 | 2.60 | 0.01 | PASS | NPA ratio table |
| 57 | NNPA ratio on balance-sheet net advances = printed, FY2026 | 0.72 | 0.72 | 0.01 | PASS | NPA ratio table |
| 58 | PCR incl. floating = printed, FY2026 | 73.03 | 73.03 | 0.02 | PASS | NPA ratio table |
| 59 | Total capital = Tier I + Tier II, FY2026 | 6,503.56 | 6,503.56 | 0.02 | PASS | regulatory capital note |
| 60 | CRAR computed = printed, FY2026 | 20.31 | 20.31 | 0.01 | PASS | regulatory capital note |
| 61 | Tier I computed = printed, FY2026 | 16.68 | 16.68 | 0.01 | PASS | regulatory capital note |
| 62 | PBT = PAT + tax (note 18.14(f)), FY2026 | 128.13 | 128.13 | 0.02 | PASS | MD&A / AR text (FY2023 none printed - identity only) |
| 63 | Deposit lines sum to Schedule 3 total, FY2026 | 46,533.09 | 46,533.09 | 0.00 | PASS | Schedule 3 |
| 64 | FY2023 deposit split (MD&A) = balance-sheet deposits | 25,348.48 | 25,348.48 | 0.02 | PASS | FY2023-24 AR MD&A deposit table |
| 65 | NII = MD&A net interest income, FY2025 | 3,251.61 | 3,251.61 | 0.02 | PASS | FY2025-26 AR MD&A |
| 66 | Operating profit = MD&A, FY2025 | 1,334.27 | 1,334.27 | 0.02 | PASS | FY2025-26 AR MD&A |
| 67 | Tangible net worth = bank's 'net worth excl. DTA & intangibles', FY2025 | 5,592.57 | 5,592.58 | 0.02 | PASS | Q4 FY2026 results, Reg 52(4) |
| 68 | NII = MD&A net interest income, FY2026 | 3,391.17 | 3,391.17 | 0.02 | PASS | FY2025-26 AR MD&A |
| 69 | Operating profit = MD&A, FY2026 | 1,264.97 | 1,264.97 | 0.02 | PASS | FY2025-26 AR MD&A |
| 70 | Tangible net worth = bank's 'net worth excl. DTA & intangibles', FY2026 | 5,582.45 | 5,582.45 | 0.02 | PASS | Q4 FY2026 results, Reg 52(4) |
| 71 | Net worth = AR highlight (rounded), FY2023 | 5,157.95 | 5,158.00 | 0.60 | PASS | FY2023-24 AR highlights |
| 72 | Net worth = AR highlight (rounded), FY2024 | 5,968.70 | 5,969.00 | 0.60 | PASS | FY2023-24 AR highlights |
| 73 | Opening gross NPA FY2024 = closing FY2023 | 723.96 | 723.96 | 0.02 | PASS | consecutive asset-quality notes |
| 74 | Opening standard advances FY2024 = closing FY2023 | 25,486.54 | 25,486.54 | 0.02 | PASS | consecutive asset-quality notes |
| 75 | Opening gross NPA FY2025 = closing FY2024 | 821.28 | 821.28 | 0.02 | PASS | consecutive asset-quality notes |
| 76 | Opening standard advances FY2025 = closing FY2024 | 30,603.40 | 30,603.40 | 0.02 | PASS | consecutive asset-quality notes |
| 77 | Opening gross NPA FY2026 = closing FY2025 | 1,067.73 | 1,067.73 | 0.02 | PASS | consecutive asset-quality notes |
| 78 | Opening standard advances FY2026 = closing FY2025 | 35,854.69 | 35,854.69 | 0.02 | PASS | consecutive asset-quality notes |
| 79 | GNPA reductions = upgradation + recoveries + write-offs, FY2023 | 1,200.31 | 1,200.31 | 0.02 | PASS | asset-quality note |
| 80 | GNPA reductions = upgradation + recoveries + write-offs, FY2025 | 1,785.17 | 1,785.17 | 0.02 | PASS | asset-quality note |
| 81 | GNPA reductions = upgradation + recoveries + write-offs, FY2026 | 2,058.24 | 2,058.24 | 0.02 | PASS | asset-quality note |
| 82 | FY2024 reductions leave a 62.02 technical write-off residual (row (iii) unprinted) | 62.02 | 62.02 | 0.02 | PASS | FY2024-25 AR - residual named in DISCLOSED_DIFFERENCES |
| 83 | FY2023 opening standard + opening GNPA = printed opening gross advances | 19,731.91 | 19,731.91 | 0.02 | PASS | FY2023-24 AR classification table |
| 84 | Schedule 13 lines = interest earned, FY2025 | 6,311.72 | 6,311.73 | 0.00 | PASS | Schedule 13 |
| 85 | LCR = HQLA / net cash outflows, Q4 FY2025 | 156.52 | 156.52 | 0.01 | PASS | LCR note |
| 86 | Bank-reported ROA: AR business ratios = Q4 results, FY2025 | 0.30 | 0.30 | 0.00 | PASS | two documents |
| 87 | Software: opening + additions - amortisation chain carries forward, FY2025 | 231.75 | 231.75 | 0.00 | PASS | software note, consecutive years |
| 88 | Restructured standard: opening - slipped - paid = closing, FY2025 | 126.80 | 126.80 | 0.02 | PASS | resolution-framework table |
| 89 | Schedule 13 lines = interest earned, FY2026 | 6,794.24 | 6,794.24 | 0.00 | PASS | Schedule 13 |
| 90 | LCR = HQLA / net cash outflows, Q4 FY2026 | 138.45 | 138.45 | 0.01 | PASS | LCR note |
| 91 | Bank-reported ROA: AR business ratios = Q4 results, FY2026 | 0.18 | 0.18 | 0.00 | PASS | two documents |
| 92 | Software: opening + additions - amortisation chain carries forward, FY2026 | 246.18 | 246.18 | 0.00 | PASS | software note, consecutive years |
| 93 | Restructured standard: opening - slipped - paid = closing, FY2026 | 70.05 | 70.05 | 0.02 | PASS | resolution-framework table |
| 94 | Top-20 depositors share = amount / deposits, FY2026 | 20.61 | 20.61 | 0.01 | PASS | concentration note |
| 95 | SRs: opening + additions = closing, FY2026 | 175.22 | 175.22 | 0.02 | PASS | non-performing non-SLR note |
| 96 | SR opening FY2026 = closing FY2025 | 100.61 | 100.61 | 0.00 | PASS | non-performing non-SLR note |
| 97 | SR provisions: opening + additions = closing, FY2026 | 169.12 | 169.12 | 0.02 | PASS | NPI provisions note |
| 98 | SR provision opening FY2026 = closing FY2025 | 97.74 | 97.74 | 0.00 | PASS | NPI provisions note |
| 99 | DTA FY2024: FY2023-24 AR = FY2024-25 AR comparative | 199.58 | 199.58 | 0.00 | PASS | Schedule 11, two documents |
| 100 | MFI share FY2025 = 4,527 / 37,986 vs printed 12% | 11.92 | 12.00 | 0.50 | PASS | FY2024-25 AR |
| 101 | Product mix sums to company gross advances, FY2023 | 27,860.50 | 27,860.50 | 0.02 | PASS | FY2023-24 AR MD&A table |
| 102 | Product mix sums to company gross advances, FY2024 | 34,336.80 | 34,336.80 | 0.02 | PASS | FY2023-24 AR MD&A table |

**External tie-out:** screener.in (read 10-Oct-2026) matches interest earned, interest expended,
PBT, net profit, net worth, deposits, borrowings and total assets for FY2023-26 — 32/32 within
rounding (`ExternalTieOut` tab).

**Mutation coverage:** 296 inputs, 92.6%. The 22 unverified inputs are named in
DISCLOSED_DIFFERENCES: the bank's own regulatory ratios, three single-source operating facts, and
the FY2023 DTA and software.

---

## 7. Step 7 — Fact register

| Fact | Value | Source |
|---|---|---|
| Ownership | No promoter; the holding company (Equitas Holdings) was amalgamated in FY2023 | FY2023-24 AR; pre-flight [7] absent |
| Board | 11 directors: 9 independent (82%), incl. 1 woman; 2 whole-time | FY2025-26 AR |
| MD and CEO | P N Vasudevan | Q1 FY2027 results |
| Auditors | ASA & Associates LLP and Suri & Co. (joint); unmodified | FY2025-26 AR |
| Network / staff | 1,060 branches + 53 other offices; 28,072 employees (11.85% women) | FY2025-26 AR BRSR |
| Advances concentration | Top-20 borrowers 3.93% of advances; top-20 exposures 5.14% | Note 6 |
| Deposit concentration | Top-20 depositors 20.61% (17.60%) | Note 6 |
| Priority sector | 29,698.10 of 43,580.10 gross advances | Sector note |
| CGFMU cover | 71% of the MFI book; 99% of FY2026 MFI disbursements | AR highlights (legible fragment) |
| Securitisation | 4 SPVs, Rs 224.37 crore; credit enhancement (FD) 61.08 | Securitisation note |
| SRs | Gross 175.22, provisions 169.12 (R1/RR1 114.28; RR5 40.33) | Investment notes |
| Restructured standard (COVID) | 70.05 (126.80) | Resolution-framework note |
| Contingent liabilities | Rs 1,024.55 crore (incl. forward contracts 314.14; investment purchases pending 285.87) | Schedule 12 |
| Penalties | No RBI penalty in FY2026; GST/tax penalties of Rs 1.8-8.5 lakh each | Note 12; CG report |
| Dividends | None for FY2025 or FY2026 | Note 1c(vi) |
| ESG | Board ESG oversight; GHG disclosed in BRSR; CSR spend Rs 14.67 crore | FY2025-26 AR BRSR / CSR note |

---

## 8. Step 7b — Instruments

**From the bank's own documents:**

| Instrument | ISIN | Amount | Coupon | Allotted | Maturity | Source |
|---|---|---|---|---|---|---|
| Lower Tier II bond (Basel II), unsecured, subordinated | INE063P08112 | Rs 500 crore | 9.6% p.a. | 05-Dec-2024 | 05-Dec-2030 | FY2024-25 AR |
| Lower Tier II bond (Basel II) | INE063P08120 | Rs 500 crore | 9.6% p.a. | 31-Jul-2025 | 31-Jul-2030 | FY2025-26 AR Directors' Report |

The ISIN-to-bond pairing follows the order of the Q1 FY2027 filing. CD outstanding is not
disclosed: the only CD references in the documents are the ratings lines.

**CRA-published rated amounts — imported under the amendment (FM29).** Source: CareEdge rationale
of **06-Oct-2025**. Conditions: (1) same-issuer primary rationale in the library ✓; (2) verbatim
every line, dated ✓; (3) labelled CRA-published, not issuer-confirmed ✓; (4) line arithmetic —
500.00 + 500.00 + 1,500.00 = 2,500.00 (no total printed) ✓, and every line matches the bank's own
AR ratings table (27-Sep-2025 reaffirmation) ✓; (5) limits vs drawn — below ✓.

| Instrument | Amount (Rs crore) | Rating (06-Oct-2025) |
|---|---:|---|
| Issuer rating | 0.00 | CARE AA-; Stable |
| Lower Tier II | 500.00 | CARE AA-; Stable |
| Lower Tier II | 500.00 | CARE AA-; Stable |
| Certificate of deposit | 1,500.00 | CARE A1+ |

**Limits vs drawn:** the Lower Tier II bonds are fully issued (Rs 1,000 crore, inside borrowings
of Rs 5,772.55 crore). The CD line is a programme limit; the outstanding amount is not disclosed.

---

## 9. Step 8 — Materiality sweep (R13: ≥1% of TNW = Rs 56 crore; ≥5% of PBT = Rs 6.4 crore; or plausibly ≥1 notch; or any governance or regulatory item)

| Finding | Size | Decision |
|---|---|---|
| Profitability collapse (ROTA 0.30% / 0.18%) | ≥1 notch | **Material** — the central weakness |
| Slippages ~6% and write-offs ~2% a year; GNPA held down by write-offs (FM59) | ≥1 notch | **Material** — write-offs stated next to every asset-quality figure |
| CASA erosion to 26.2%; top-20 depositors 20.6%; bank term deposits 18% | ≥1 notch | **Material** — resource profile |
| Negative cumulative ALM gaps within one year (−6,411 at one year, before cash) | Liquidity | **Material** — the liquidity descriptor |
| IBPC Rs 2,000 crore (short-tenor inter-bank funding) | >1% TNW | Material — funding |
| CRAR decline 23.80 → 20.31; leverage ratio 13.21 → 8.84 | Capital trajectory | **Material** |
| NPA sale to ARCs (principal 565.40; SRs 175.22, 97% provided) | >1% TNW | Material — asset quality; SRs largely provided |
| Q1 FY2026 loss (−223.78) and recovery (Q4 FY2026 212.68; Q1 FY2027 PBT 244.07) | ≥1 notch | **Material** — the outlook |
| Restructured standard 70.05 | 1.3% TNW | Material by size; small and declining |
| Frauds Rs 18.33 crore | <1% TNW | Governance type — noted; immaterial in size |
| Tax penalties (lakhs) | Immaterial | Logged |
| Complaints up 24% to 29,533 | Operational | Noted (social risk) |

---

## 10. Step 10 — Methodology Compliance Map (CareEdge Banks, March 2025)

| Factor (as named) | Evidence | Assessment | Weight |
|---|---|---|---|
| A) Capital adequacy | CRAR 20.31% (minimum 15%); Tier I 16.68% (7.5%); leverage 8.84% (4.5%); Tier II raised twice (Rs 500 crore each); Tier I fell 6.4 pp in three years; base case drifts to ~16.5% by FY2031 | **Comfortable today, declining** — growth needs fresh equity in the medium term | High |
| B) Asset quality | GNPA 2.60%, NNPA 0.72%, PCR 73.03% (86.81% with technical write-offs); slippages 5.93% of opening standard advances; write-offs 2.11% of gross advances; net stressed assets / TNW 6.85%; top-20 borrowers 3.93% | **Moderate** — granular and largely secured (~10% MFI, 71% CGFMU-covered), but the loss rate is high and persistent | High |
| C) Resources | Deposits 46,533 (+8%); CASA 26.21% (42.23% FY2023); top-20 depositors 20.61%; term deposits from banks 8,448; borrowings/TNW 1.03x; cost of deposits 7.11% | **Moderate and weakening** | High |
| D) Liquidity | LCR 138.45%; NSFR 114.01%; negative cumulative ALM gaps within one year (§11); access to LAF/MSF | **Adequate** | Medium |
| E) Earnings quality | NIM 5.98% (6.63%); PPOP / ATA ~2.2% vs credit cost 2.00%; cost-to-income 71.67%; ROTA 0.18%; turn visible in Q4 FY2026 and Q1 FY2027 | **Weak, recovering** | High |
| a) Industry / operating environment | SFB sector; microfinance stress FY2025-26 across peers (ESAF and Utkarsh on Negative outlooks) | Moderate | Medium |
| b) Ownership | No promoter; widely held | Neutral — no support uplift | Low |
| c) Management quality | Founder-led; de-risked the MFI book early (MFIN guardrails from January 2025, ahead of the industry — FY2024-25 AR) | Adequate | Medium |
| d) Risk management (market, operational, digital) | AFS reserve −53.22; frauds Rs 18.33 crore; complaints up 24% | Adequate | Medium |
| e) Compliance with statutory requirements | No RBI penalty FY2026; no divergence disclosure required | Clean | Low |
| f) Accounting quality | Unmodified audits; KAM on NPA identification | Clean | Low |
| g) Size and market presence | Total assets Rs 60,610 crore — among the larger SFBs (AU ~1.65 lakh crore; Ujjivan 52,078) | Supports | Medium |
| ESG | Board ESG oversight; financial-inclusion lending (priority sector 68% of gross advances); 82% independent board | Neutral to positive | Low |
| Instrument: Lower Tier II (Basel II) | Hybrid paper: Basel III Tier II rated "similar or close to" Basel II Lower Tier II for higher-rated banks | **Rated at the issuer level** | — |
| Short-term (CD) | Mapping table corrupted (FM49); the issuer's own published action shows CARE A1+ alongside CARE AA- | **A1+** at AA- | — |

---

## 11. Step 11 — Liquidity (ALM, 31-Mar-2026, Rs crore)

| Bucket | Inflows (advances + investments) | Outflows (deposits + borrowings) | Cumulative gap | Cumulative gap / cumulative outflows |
|---|---:|---:|---:|---:|
| Day 1 | 1,716.48 | 763.14 | 953.34 | 124.9% |
| 2-7 days | −328.69 | 669.08 | −44.43 | −3.1% |
| 8-14 days | 384.64 | 834.68 | −494.47 | −21.8% |
| 15-30 days | 759.93 | 1,100.72 | −835.26 | −24.8% |
| 31 days-2 months | 1,098.34 | 1,642.64 | −1,379.56 | −27.5% |
| 2-3 months | 1,743.74 | 1,700.73 | −1,336.55 | −19.9% |
| 3-6 months | 3,281.43 | 3,561.81 | −1,616.93 | −15.7% |
| 6 months-1 year | 7,035.48 | 11,829.78 | −6,411.23 | −29.0% |

Advances inflows are net of the Rs 2,000 crore of IBPC outflows (ALM note). Cash and balances
with RBI and banks (5,666.29) are not in the ALM table; adding them (part is CRR) leaves −744.94
at one year.

Offsets: LCR 138.45% (Q4 FY2026 average; HQLA 10,221.92 against net outflows of 7,383.15); NSFR
114.01%; access to LAF and MSF. **Descriptor: Adequate.** The regulatory ratios are comfortable,
but contractual gaps rely on deposit renewal. That is weaker than Ujjivan, which reports no
negative cumulative mismatch within one year.

---

## 12. Step 12 — Projections (lending model; `case.json` scaling)

`Equitas_SFB_Lending_Model_10Oct2026.xlsx` contains:
- Assumptions; Lending P&L; Balance Sheet; Capital;
- Credit Ratios — 85 formula cells, cached; the 28 historical cells equal the engine;
- Scenarios; Debt Breakup; Valuation.

Also delivered: `Equitas Small Finance Bank_Research_Note_10Oct2026.md` (Tasks 1 and 3) and
`Equitas_SFB_Charts_10Oct2026.zip` (Task 4, 6 charts).

| Driver (FY2027E-31E) | Base | Stress (MFI-type shock) | Tail |
|---|---|---|---|
| Advances growth (%) | 18, 18, 17, 16, 15 | 10, 8, 12, 15, 15 | 5, 5, 10, 15, 15 |
| NIM / ATA (%) | 6.0 → 6.2 | 5.6, 5.5, 5.8, 6.0, 6.1 | as stress |
| Credit cost / ATA (%) | 1.20, then 1.10 | 3.00, 2.50, 1.60, 1.20, 1.10 | 5.00, 3.50, 2.00, 1.30, 1.10 |
| Opex / ATA (%) | 5.5 → 5.1 | 5.6-5.2 | as stress |
| **FY2027 PAT / ROTA / CRAR** | **544 / 0.82% / 18.65%** | −667 / −1.05% / 16.57% | −1,581 / −2.54% / 14.64% |
| Minimum CRAR over the horizon | 16.50% | 12.77% | 9.91% |

**Breakeven:** a FY2027 credit cost of **3.99% of average total assets** takes CRAR to the 15%
minimum, about twice the FY2026 actual of 2.00% and 1.7 times the FY2025 peak of 2.31%.

Reading:
- The bank can absorb roughly one more year of FY2025-type credit cost without breaching the
  minimum.
- A repeat lasting two years (the stress case) takes CRAR below 15% in FY2028, so it would need
  equity.
- Even in the base case, growth of 15-18% at ROTA below 1.2% consumes capital, implying an equity
  raise or slower growth within the horizon.

---

## 12b. Step 12b — Scorecard (Stage 1)

`Rating_Scorecard_Equitas Small Finance Bank Limited.xlsx`: sector "Bank / SFB", using the
financial-sector block.

| Input | Latest | FY+1 (copied from the model) |
|---|---|---|
| CRAR | 20.31% | 18.65% |
| GNPA | 2.60% | held |
| NNPA | 0.72% | held |
| ROTA | 0.18% | 0.82% |
| NIM | 5.98% | 6.00% |
| Cost-to-income | 71.67% | — |
| Total assets | Rs 60,610.36 crore | — |

Qualitative scores: industry 3 (override from 2 — SFB customer segments), business 3,
management 2, support 0, liquidity Adequate. **Anchor: CARE A+ / CARE A1** (composite 2.877;
index 4). The business-risk gate does not fire (3.0 vs 3.06).

---

## 13. Step 13 — Independent rating view (written before Step 14)

**Standalone profile.** Four things support a rating in the AA category:
- **Capital:** CRAR 20.31% and Tier I 16.68%, 5.3 pp above the 15% minimum. The breakeven
  credit cost of 3.99% is about twice the FY2026 cost.
- **Franchise:** total assets Rs 60,610 crore and 1,060 branches.
- **A de-risked book:** microfinance cut from 18.8% to about 10% of advances, 71% of it
  CGFMU-covered, with top-20 borrowers at 3.93%.
- **Visible earnings recovery:** Q4 FY2026 PAT Rs 212.68 crore and Q1 FY2027 PBT Rs 244.07 crore,
  after a Q1 FY2026 loss.

**What holds it at AA-, and below AA:**
- **Two years of very weak earnings:** ROTA 0.30% and 0.18%; PPOP/ATA ~2.2% against credit cost
  of 2.0%.
- **A persistently high loss rate:** slippages near 6% and write-offs near 2% a year.
- **A weakening resource profile:** CASA 26%, deposit concentration 20.6%, reliance on inter-bank
  term deposits and IBPC.
- **Steadily declining capital ratios:** CRAR down 3.5 pp in three years.

The peer calibration supports AA-:
- Ujjivan, at CARE AA-, has similar capital (21.6%) and CASA (27%) with higher profitability, but
  a far riskier mix (52% micro-banking).
- AU, at AA, is about 2.7 times the size with steadier ROTA (~1.4-1.5%).

**Anchor divergence (+1).** The scorecard reads the FY2026 trough ROTA (0.18%) as structural. The
capital buffer and the quarterly recovery are what it cannot see. To be resolved at Step 17c.

**Support:** none, either direction — the bank is widely held with no promoter (FM56: no
parent or group exists).

**Instruments:**
- Lower Tier II bonds (Basel II) at the issuer level, per the hybrid paper for higher-rated
  banks.
- CDs: CARE A1+, checked against the issuer's own published pairing because the mapping table is
  corrupted (FM49).

**Outlook — Stable, not Negative.** The negative indicators (two years of sub-0.5% ROTA,
declining CRAR) are real. But the evidence of recovery is already in the numbers: Q4 FY2026 and
Q1 FY2027, a microfinance book now ~10% and mostly guaranteed, and a capital buffer large enough
to absorb one more stress year. A Negative outlook would signal an expected downgrade that the
current trajectory does not support. The risk is carried in quantified sensitivities instead.

> **Proposed view:**
> - Issuer rating: CARE AA-; Stable.
> - Lower Tier II bonds (Rs 500 crore + Rs 500 crore): CARE AA-; Stable.
> - Certificates of deposit (Rs 1,500 crore): CARE A1+.
>
> **Sensitivities:**
> - *Positive:* ROTA sustained above 1.5%; CASA above 35%; Tier I above 18% after a capital raise.
> - *Negative:* ROTA below 0.8% in FY2027 or below 1% thereafter on a sustained basis; GNPA
>   above 3.5%; CRAR below 17% without a capital plan; material deterioration in deposit
>   concentration or liquidity.

---

## 14. Step 14 — Comparison with CareEdge's own action (opened only after §13 was written)

CareEdge rationale of **06-Oct-2025** (reference library): all ratings reaffirmed — issuer and
Lower Tier II CARE AA-; Stable, CD CARE A1+. Its data runs to Q1 FY2026 (30-Jun-2025).
`tools/step14_diff.py` output is in §17.

| Item | This analysis (data to 31-Mar-2026) | CareEdge (data to 30-Jun-2025) | Explanation |
|---|---|---|---|
| Ratings / outlook | CARE AA-; Stable / CARE A1+ | Same | Reached independently (§13 written first; the exposure is declared in §0) |
| Basis | Standalone | Standalone | Same |
| Liquidity descriptor | Adequate | Adequate | Same descriptor. **Postdates the anchor:** CareEdge saw no negative cumulative mismatch up to three months (June 2025). The March 2026 ALM shows negative gaps from the 2-7 day bucket, with Rs 2,000 crore of IBPC within two months. This analysis names that as a weakness |
| Regional concentration | **Not disclosed in the document set** — recorded searches (state-wise / Tamil Nadu % / geographic concentration) returned 0 hits. The BRSR gives only "16 States & 2 UTs" | A key weakness: Tamil Nadu 46% of gross advances, top three states 74% (June 2025) | **This analysis lacked a driver** that rests on issuer-supplied data outside the documents. It is not imported (R1). The report names the gap and lists state-wise advances as an information request. *Lesson logged* |
| Profitability | ROTA 0.30% (FY2025), 0.18% (FY2026) — engine | ROTA 2.00% (FY2024), 0.30% (FY2025), −1.78% (Q1 FY2026) | Agree on FY2025. The FY2026 figure and the H2 recovery postdate CareEdge, which "expects ... improve in H2FY26" — that has since happened (Q3 PAT 90.03, Q4 212.68) |
| Ratio definitions | NIM FY2025 6.63%, FY2024 7.67%; opex/ATA 5.76% / 6.23%; credit cost 2.31% / 0.78% | 6.64% / 7.69%; 5.78% / 6.26%; 2.32% / 0.78% | Within 0.03 pp — averaging/rounding. The engine follows the published formula (average of the opening and closing balance sheets) |
| GNPA / NNPA FY2024 | 2.61% / 1.17% (bank-printed, reproduced) | 2.52% / 1.12% | CareEdge's own calculation differs from the bank's printed ratios; this report uses the printed RBI-basis ratios, as its definitions paper prescribes |
| Slippage ratio FY2025 | 6.64% (additions ÷ opening standard advances — the definitions-paper formula) | 5.94% | Different denominator: CareEdge's published figure is consistent with opening gross advances on the company basis (2,031.62 / 34,336.80 = 5.92%). The paper's formula is used and the difference disclosed |
| Net stressed assets / net worth FY2025 | 8.65% (restructured taken gross; TNW) | 6.01% | Basis: provisions against restructured exposure are not disclosed, so it is taken gross (conservative); CareEdge likely nets it and may use net worth |
| Negative sensitivities | ROTA <0.8% in FY2027 or <1% thereafter; GNPA >3.5%; CRAR <17% without a capital plan; liquidity | GNPA >4%; CAR <18%; ROTA <1% (all "on a sustained basis") | Same direction. This analysis is tighter on GNPA and looser on CAR: the base-case model shows growth taking CRAR to ~16.5% even with no stress, so an 18% floor would be breached by planned growth alone |
| Positive sensitivity | ROTA >1.5%, CASA >35%, Tier I >18% after a capital raise | Scale and geographic diversification, with a sharp fall in single-state concentration | This analysis cannot quantify geography (not disclosed). Its positive triggers target the measured weaknesses |
| Brief-financials rows | Total income, PAT, total assets, NIM, ROTA, GNPA, NNPA, CAR — the CareEdge SFB peer set (AU, Ujjivan, Capital; pre-flight [1b]) | Total operating income, PAT, interest coverage (NA), total assets, NNPA, ROTA | CareEdge's own Equitas table is narrower; the fuller peer set is used, per pre-flight [1b] |
| Instruments | Lower Tier II ISINs, coupons and maturities from the bank's AR — **identical** to CareEdge's Annexure-1 | — | Agree. CareEdge's CD ISINs (October 2025; maturities March/June 2026) are not imported — stale, and outside the amendment |

**Mandate details requiring issuer confirmation:** the current CD programme and outstanding
amount; any change to the rated amounts since 06-Oct-2025; state-wise advances.

---

## 15. Step 15 — Analytical package (proposed view; the Committee decides at 17c)

Proposed: **CARE AA-; Stable** (issuer; Lower Tier II Rs 500 crore + Rs 500 crore) and **CARE
A1+** (CD Rs 1,500 crore). The Stage 1 anchor is A+ / A1; the +1 notch is to be resolved at 17c.

Judgment calls:
1. Stable rather than Negative despite two years of ROTA below 0.5%.
2. The liquidity descriptor stays Adequate despite negative ALM gaps.
3. The definitions paper's slippage formula is used over CareEdge's published figure.

Input gaps:
- State-wise advances.
- The CD outstanding amount.
- Q1 FY2027 asset-quality and capital figures (the Q1 file's statement table did not convert).

---

---

## 17. Step 17 / 17a — Re-verification and delivery gates

**(a) Computed drift check.** A script extracted every number in the rationale and matched each,
at the rationale's own rounding, against the engine, the lending model and the spreads. **187
match a computed value.** Five more are arithmetic or unit conversion:
- 8.95% — unsecured advances / net advances, 3,827.35 / 42,751.29;
- 826 — FY2025 write-offs, 670.88 + 155.47;
- 4,247 — guaranteed advances, Schedule 9, Rs '000 to crore = 4,246.92;
- 6,411 — §11 ALM cumulative gap;
- 9,260 — government securities, Schedule 8 = 9,259.86.
**No unexplained figure.**

**(b) Non-computed drift check.** **36 numbers match a figure in the case documents.** The
context-sensitive ones were re-read at source this session:
- branches 1,060 and "16 States & 2 UTs" (BRSR);
- employees 28,072;
- CGFMU 71% / 99% (AR highlights);
- microfinance book 4,527 / 6,265.45 (FY2025 and FY2024 ARs);
- bond terms (FY2025 AR line 5308; FY2026 AR Directors' Report);
- LCR 179.64 → 138.45 (LCR note);
- NSFR 114.01;
- top-20 depositors 20.61%;
- NPA sale 565.40 / 184.00;
- frauds 488 / 18.33;
- complaints 29,533;
- CSR 14.67;
- the Q1 FY2027 segment PBT of 244.07.

Corroborated by a second source: TNW (Reg 52(4)), NII and operating profit (MD&A), ROA (Q4
results), and every headline against screener.in.

**(c) Corrections made during the pass:**
- the intake sector and routing (corporate → bank);
- the research note's "ESOP-linked" equity claim, removed as unsupported;
- the AU size comparison (2.7 times, not three);
- the pre-flight output, re-saved as UTF-8 (a Windows-1252 byte);
- absence claims in the rationale, now carrying their searches.

**(d) Gates (17a):**
- `check_sections.py` — PASS, probes clean. The first run's five findings were each verified and
  fixed: the KFI header; absence-claim evidence; the unencumbered-cash statement; Stage 2 of the
  scorecard; FM37 on CareEdge's boilerplate complexity note, now paraphrased.
- `step14_diff.py` — no material divergence.
- `annotate_scorecard.py` and `delivery_audit.py` — §17 verdict below.

**Final run:** `annotate_scorecard.py` — assigned AA-/A1+ vs rationale AA-/A1+, MATCHES (anchor A+, 1-notch bridge, scoped to CareEdge). `delivery_audit.py` — **READY TO SHARE** (102/102 tie-outs; coverage 92.6%; section gate PASS; scorecard matches; workpaper present; Step 14 clean).


---

## Appendix A — Step 1a pre-flight output (verbatim)

```
==============================================================================
PRE-FLIGHT  |  Equitas Small Finance Bank Limited  |  agency CareEdge  |  8 documents, 302,662 words
==============================================================================

[0] DOCUMENTS BY DATE - READ THE NEWEST FIRST  (failure mode 26)
      ~2025  Equitas-SFB-Integrated-Annual-Report-2025-26.md
      ~2024  Equitas-AR-2024-25.md
      ~2023  ESFBL-Annual-Report_2023-24.md
       ?    OutcomeofBoardmeeting_Q2.md
       ?    OutcomeofBoardMeetingQ1-2.md
       ?    OutcomeofBoardMeetingQ3.md
       ?    OutcomeofBoardmeetQ1FY27-1.md
       ?    OutcomeofBoardmeetQ4FY26.md
    *** Newest content appears to be 2025. Any figure taken from an older
        document than this must be justified in the workpaper. ***

[0b] OPERATING METRICS ACROSS DOCUMENTS - ATTRIBUTE EACH TO ITS YEAR  (failure mode 30)
    !! branches:
         ~2025  1,060, 31                                Equitas-SFB-Integrated-Annual-Report-2025-26
         ~2024  36                                       Equitas-AR-2024-25.md
         ~2023  25, 32                                   ESFBL-Annual-Report_2023-24.md
         ^^ SAME METRIC, DIFFERENT VALUES across documents. Quote the value from the
            NEWEST document, and state the SERIES if it moves - the direction is the finding.
    !! cities/towns:
         ~2024  3                                        Equitas-AR-2024-25.md
         ~2023  3, 6                                     ESFBL-Annual-Report_2023-24.md
         ^^ SAME METRIC, DIFFERENT VALUES across documents. Quote the value from the
            NEWEST document, and state the SERIES if it moves - the direction is the finding.
    !! clients/customers:
         ~2023  1                                        ESFBL-Annual-Report_2023-24.md
         ^^ FOUND ONLY IN AN OLDER DOCUMENT (newest content is ~2025). Nothing
            contradicts it, so it reads as current - it is NOT. Either date it explicitly
            in the rationale or re-search the newest document for its own figure.

[0c] AGGREGATE-NOTE CONTAMINANTS - DECOMPOSE BEFORE USING A SUBTOTAL  (failure mode 36)
    !! impairment / write-off:
                 3.17   c) Less: Write off / write back of excessprovisions  ESFBL-Annual-Report_2023-24.md
                 1.61   Utilisation / Write back ofprovision for rewardpoint Equitas-SFB-Integrated-Annual-Repo
                 0.85   Utilisation/Write back ofprovision for rewardpoints  Equitas-AR-2024-25.md
                 0.85   Utilisation / Write back ofprovision for rewardpoint ESFBL-Annual-Report_2023-24.md
    !! provision written back:
             1,125.02   Less: Excess provision reversed/Write-off loans      Equitas-SFB-Integrated-Annual-Repo
               937.30   Less: Excess provision reversed/ write-off loans     Equitas-AR-2024-25.md
               937.30   Less: Excess provision reversed/Write-off loans      Equitas-SFB-Integrated-Annual-Repo
               627.17   Less: Excess provision reversed/ write-off loans     ESFBL-Annual-Report_2023-24.md
    !! interest / dividend income:
             3,079.76   Net Interest Income                                  Equitas-AR-2024-25.md
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
    !! earmarked / margin / restricted balances inside CASH:
         0.02                           Unclaimed Securities Account                       Equitas-AR-2024-25.md
         4,596.11, 4,485.63, 27,010.71  19                                                 Equitas-SFB-Integrated-Ann
         4,191.80, 3,824.00             19                                                 Equitas-SFB-Integrated-Ann
    ^^ BINDING: each line above sits INSIDE a balance-sheet caption that a ratio
       will use. Before publishing overall gearing, working-capital dependence,
       long-term debt or a liquidity figure, SPLIT the caption and state the
       split. A caption is not a ratio input until its components have been read
       - the same rule failure mode 36 applies to the P&L, applied to the
       balance sheet, where it had no probe at all.

[0f] PROMOTER / RELATED-PARTY UNSECURED LOANS  (failure mode 48, CRISIL only)
     n/a - CRISIL's four-factor test does not apply to a CareEdge case

[1] PRIOR RATING ACTION IN THE REFERENCE LIBRARY  (Step 14 / failure mode 24)
    (searching on ['Equitas', 'Small', 'ESFBL'] - includes former name / aliases)
    *** PRESENT - Step 14 IS APPLICABLE. Open these AFTER forming your view, and
        produce a divergence table. You may NOT write 'no prior rating action'. ***
      - CareEdge: Equitas Small Finance Bank Limited_06 Oct 2025.md
      - CRISIL: AU Small Finance Bank Limited_02 Apr 2026_RR_392195.md
      - CareEdge: Au Small Finance Bank Limited_01 Dec 2025.md
      - CareEdge: Capital Small Finance Bank Limited_27 Feb 2026.md
      - CareEdge: ESAF Small Finance Bank Limited_02 Sep 2025.md
      - CareEdge: Jana Small Finance Bank Limited_09 Jul 2026.md
      - CareEdge: Suryoday Small Finance Bank Limited_06 Feb 2019.md
      - CareEdge: Ujjivan Small Finance Bank Limited_23 Mar 2026.md

    >>> RATED AMOUNTS FOUND IN THE LIBRARY <<<
      Failure mode 29: never write 'to be confirmed by issuer' while a
      SAME-ISSUER line exists. Condition (1) is MET - the library counts.
      !! CONFIRM THE ENTITY FIRST. A PARENT, SIBLING OR PEER IS NOT THE
         ISSUER - importing a peer's rated amount is a WORSE error than
         leaving it TBC. [match n/m] = how many of the issuer's name
         tokens the filename carries. Highest score is the candidate;
         it still needs your confirmation that it is the same company.
      from Equitas Small Finance Bank Limited_06 Oct 2025.md  [match 2/3]
        |Issuer rating|0.00|CARE AA-; Stable|Reaffirmed|
        |Lower tier II|500.00|CARE AA-; Stable|Reaffirmed|
        |Lower tier II|500.00|CARE AA-; Stable|Reaffirmed|
        |Certificate of deposit|1,500.00|CARE A1+|Reaffirmed|
      from Au Small Finance Bank Limited_01 Dec 2025.md  [match 1/3]
        |Infrastructure bonds|1,000.00|CARE AA; Stable|Assigned|
        |Tier-II bonds|770.00 (Reduced from 2,000.00)|CARE AA; Stable|Reaffirmed|
        |Tier-II bonds|200.00|CARE AA; Stable|Reaffirmed|
        |Tier-II bonds|300.00|CARE AA; Stable|Reaffirmed|
        |Tier-II bonds|125.00 (Reduced from 150.00)|CARE AA; Stable|Reaffirmed|
        |Certificate of deposit|3,900.00|CARE A1+|Reaffirmed|
      from ESAF Small Finance Bank Limited_02 Sep 2025.md  [match 1/3]
        |Certificate Of Deposit|500.00|CARE A1|Downgraded from CARE A1+|
      from Ujjivan Small Finance Bank Limited_23 Mar 2026.md  [match 1/3]
        |Long-term bank facilities|500.00|CARE AA-; Stable|Reaffirmed|
        |Non-convertible debentures|500.00|CARE AA-; Stable|Reaffirmed|
        |Fixed Deposit|10,000.00|CARE AA-; Stable|Reaffirmed|

[1b] PEER REPORTS - CAREEDGE, SAME SECTOR  (failure modes 32/33)
    ignoring generic sector tokens ['bank'] - they identify no sector
    * Au Small Finance Bank Limited_01 Dec 2025.md   (score 13.8 on sfb)
        Brief Financials rows THIS AGENCY USES IN THIS SECTOR:
          - Total income
          - Profit after tax (PAT)
          - Total assets
          - Net interest margin (NIM) (%)
          - ROTA (%)
          - Gross non-performing assets (NPA) (%)
          - Net non-performing assets (NPA) (%)
          - Capital adequacy ratio (CAR) (%)
    * Capital Small Finance Bank Limited_27 Feb 2026.md   (score 13.8 on sfb)
        Brief Financials rows THIS AGENCY USES IN THIS SECTOR:
          - Total income
          - Profit after tax (PAT)
          - Total assets
          - Net interest margin (NIM) (%)
          - ROTA (%)
          - Gross non-performing assets (NPA) (%)
          - Net non-performing assets (NPA) (%)
          - Capital adequacy ratio (CAR) (%)
    * ESAF Small Finance Bank Limited_02 Sep 2025.md   (score 13.8 on sfb)
        Brief Financials rows THIS AGENCY USES IN THIS SECTOR:
          - Total income
          - PAT
          - Total assets
          - Net NPA (%)
          - ROTA (%)
    *** These rows are the REQUIRED set, and the footnotes are the agency's
        RATIO DEFINITIONS. Reproduce them. A metric may be omitted only after
        checking a peer above - never by reasoning from another sector. ***
    !! TOP PEERS DISAGREE ON THE ROW SET - the sector match is
       AMBIGUOUS. Confirm which peer is the same ENTITY TYPE before
       relying on peer_rows.json, and overwrite it if the top hit is
       the wrong kind of company.
    PEER NORM over 9 peers: 7 carry a LONG-TERM rating, 3 a short-term rating.
        -> A long-term rating is NORMAL in this sector. If your report assigns none,
           that is a DEVIATION and must be justified in writing - never inferred
           from the absence of long-term DRAWN debt (failure mode 31).
    -> wrote peer_rows.json (8 rows from Au Small Finance Bank Limited_01 Dec 202; peer norm 7/9 LT). check_sections.py VERIFIES both.

[1c] STEP 12 - THE FORWARD VIEW IS NOT OPTIONAL  (failure mode 35)
    entity_type 'bank' -> required artefact:
      LENDING model - book/AUM growth -> NII -> credit cost -> PAT, plus balance sheet, Cred
      it-Ratios and Debt-Breakup tabs. The corporate 3-statement template does NOT fit a len
      der.
    PLUS Step 12b: fill Rating_Scorecard_<Company>.xlsx from AUDITED ACTUALS.
    If a lighter treatment is right, record WHY in case.json as
    'step12_scaling_decision' - the delivery gate refuses the case without one.

[2] CREDIT-RATING NOTE in the issuer's own AR  (Step 7b)
    *** PRESENT - 37 match(es)
        If PRESENT you already know the outstanding rating - declare the anchor exposure and NEVER write 'no rating disclosed'.
        e.g. ...s been denied access to the Audit Committee. # **20. Credit Ratings** The details of the credit ratings are di...
        e.g. ...ittee. # **20. Credit Ratings** The details of the credit ratings are disclosed in the Corporate Governance Re...

[3] SUBSIDIARIES / entities to NAME  (failure mode 17)
    *** PRESENT - 111 match(es)
        Every entity must be NAMED in the entities-consolidated annexure regardless of materiality.
        e.g. ...rmanent workers|-|-|-|-|-|-|-|-|-| - **V. HOLDING, SUBSIDIARY AND ASSOCIATE COMPANIES (INCLUDING JOINT VENTURE...
        e.g. ...s|-|-|-|-|-|-|-|-|-| - **V. HOLDING, SUBSIDIARY AND ASSOCIATE COMPANIES (INCLUDING JOINT VENTURES)** **23.** (...

[4] ESG data  (failure modes 19/20)
    *** PRESENT - 377 match(es)
        If PRESENT you may NOT write 'ESG data not extractable'. Extract and quote the numbers.
        e.g. ...oversight, with a clear focus on six key areas such as Emissions, Green Financing, Operations, Inclusion, Deve...
        e.g. ...hies that drive our purpose and performance. # **Our CSR Philosophy** Equitas transcends traditional banking...

[5] INSTRUMENT details  (Step 7b)
    *** PRESENT - 61 match(es)
        Populate Annexure I from these; mark only genuinely undisclosed amounts as TBC.
        e.g. ...E Code|543243| |NSE Symbol|EQUITASBNK| |Bloomberg Code|INE063P01018| |AGM Date|September 10, 2025| |AGM Venue|...
        e.g. ...cted by a team of CISAqualified professionals and CERT-Inempanelled external firms. Additionally, the departme...

[6] CAPEX / investment cycle
    *** PRESENT - 32 match(es)
        Capital-intensive sectors: capex must appear in the rationale.
        e.g. ...lexibility to cater to the diverse working capital and capex needs of small businesses. 1,689 746 Gross Advanc...
        e.g. ...sation, digital payment adoption, government-led infra capex, and unmet MSME credit demand position us to grow...

[7] SHAREHOLDING / promoter stake
        absent - 0 match(es)
        absence is now EVIDENCED - safe to state, cite this run

[8] AUDITOR opinion / KAM / Emphasis of Matter
    *** PRESENT - 57 match(es)
        An EOM or qualification is rating-relevant regardless of quantum (R13).
        e.g. ...025 Place: Chennai 202 ANNUAL REPORT 2024-25 # **Independent Auditor?s Report** ## **To the Members of Equitas...
        e.g. ...our audit opinion on the financial statements. ## **Key Audit Matters** Key audit matters are those matters th...

[9] SECTOR-DEFINING METRIC  (failure mode 21)
    sector detected (2377 trigger hits; next best 'utilisation / EBITDA per tonne' at 136) -> the rationale MUST quote: NIM / GNPA / CRAR / CASA
    *** PRESENT in documents - 112 match(es) -> EXTRACT IT

[10] METHODOLOGY TABLE INTEGRITY  (failure mode 49)
    !! CORRUPTED  Rating_of_Short_Term_Instruments_Feb_2025.md
       section 'CARE Ratings’ indicative mapping of short-term ratings to long-term ratings', 18 labelled row(s) with every data cell blank
       -> do NOT quote a threshold from this table; re-extract from a clean PDF

==============================================================================
Paste this into the workpaper Read Log. Anything marked PRESENT may NEVER be described
as 'not available' later without a second recorded search contradicting this one.
==============================================================================
```
