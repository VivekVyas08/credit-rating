# Workpaper — Yasho Industries Limited (CRISIL)
**Date:** 14 August 2026 · **Analyst tool run:** local · **Agency:** CRISIL · **Basis:** Consolidated

---

## Step 1a — PRE-FLIGHT (mandatory gate, `python preflight.py yasho-industries`)

```
PRE-FLIGHT  |  Yasho Industries  |  agency CRISIL  |  8 documents, 310,646 words

[1] PRIOR RATING ACTION IN THE REFERENCE LIBRARY  -> PRESENT
      - CRISIL: Yasho Industries Limited_11 Feb 2026_RR_388684.md
      - CareEdge: Yasho Industries limited_07 Jun 2021.md
[2] CREDIT-RATING NOTE in the issuer's own AR      -> PRESENT, 18 matches
[3] SUBSIDIARIES / entities to NAME                -> PRESENT, 295 matches
[4] ESG data                                       -> PRESENT, 405 matches
[5] INSTRUMENT details                             -> PRESENT, 6 matches
[6] CAPEX / investment cycle                       -> PRESENT, 115 matches
[7] SHAREHOLDING / promoter stake                  -> PRESENT, 6 matches
[8] AUDITOR opinion / KAM / Emphasis of Matter     -> PRESENT, 79 matches
[9] SECTOR-DEFINING METRIC                         -> receivable/GCA days (ambiguous flag raised)
```

**Binding effect applied:** every item above marked PRESENT was extracted and used. No section of this report states that any of them is unavailable.

**Pre-flight bug found and fixed during this run.** The first execution returned false positives at probe [1] — it matched the generic token "Industries" and returned Aarti Industries, Britannia Industries, Belrise Industries and five others. Root cause: token selection took the first two words longer than three characters without excluding generic corporate suffixes. Fixed by adding a `GENERIC_TOKENS` exclusion set (industries, limited, corporation, company, group, india, private, enterprises, holdings, international) with fallback if the name contains nothing else. Re-run returned the two genuine matches only. Self-test extended and passing (7 cases).

---

## Step 1b — DOCUMENT READ LOG (8 files, all read)

| # | File | What it is | Key contribution | Material flags |
|---|---|---|---|---|
| 1 | `yasho_industries_annual_report_2025-26.md` | FY26 AR (primary) | Consolidated P&L/BS/CFS; BRSR; KAMs; credit-ratings note; AOC-1 | Two KAMs (LTSA advance accounting; inventory valuation); FY26 Scope 1/2 GHG marked "Under Process" by the company |
| 2 | `yasho_industries_ar25_22.08.25.md` | FY25 AR | FY25/FY24 comparatives; Rs 125 cr preferential allotment | KAMs: preferential allotment; CWIP→PPE capitalisation. Auditor changed to Gokhale & Sathe |
| 3 | `ar_holding_co_2023-24.md` | FY24 AR (NOT a separate holdco) | FY24/FY23 comparatives; 5-year-at-a-glance back to FY20 | Filename misleading — CIN L74110MH1985PLC037900 identical across all three; "Holding Company" is standard consolidated-audit language |
| 4 | `investor_presentation_q1fy27.md` | Q1FY27 deck (**data cutoff**) | Q1FY27 P&L; debt 1.86x; utilisation >65%; WC 143 days; FY28 target >Rs 1,600 cr | **Discloses the CRISIL/ICRA upgrade BBB+ → A-** (line 290) |
| 5 | `investor_presentationq4fy26__1_.md` | Q4FY26 / FY26 full year | FY26 revenue 830.03, EBITDA 144.46, debt 540.9 | FY27 capex then guided Rs 125 cr (later revised to Rs 250 cr) |
| 6 | `investor_presentation_q3fy26.md` | Q3FY26 deck | MNC project Rs 85–90 cr customer-funded; two new lines Rs 25.9 cr | Utilisation "below optimal" on tariffs |
| 7 | `investor_presentation_q1fy26.md` | Q1FY26 deck | Q1FY26 base; utilisation "over 50%" | Q1FY26 EBITDA later restated 33.87 → 32.70 cr |
| 8 | `covering_letter_investor_presentation.md` | Q2FY26 covering letter + deck | H1FY26; 15-yr LTSA first disclosed | Confirms the Q1FY26 EBITDA restatement |

---

## Step 14 — PRIOR RATING ACTION AND DIVERGENCE (the critical step)

**This case would have been rated one notch wrong had the reference library been trusted.**

| Source | Rating | Date | Status |
|---|---|---|---|
| Reference library, CRISIL | Crisil BBB+/Positive · Crisil A2 | 11 Feb 2026 | **SUPERSEDED** |
| Reference library, CareEdge | CARE BBB-/Stable · CARE A3 | 07 Jun 2021 | Withdrawn at issuer request |
| **Issuer's Q1FY27 deck, line 290** | **"upgraded/assigned by CRISIL and ICRA from BBB+ to A-"** | ~Jul 2026 | **CURRENT** |
| Issuer's FY26 AR | IND BBB+/Positive · IND A2+, "Affirmed; Off Rating Watch" | 04 Mar 2026 | India Ratings, superseded by the above |

The library's CRISIL file is additionally **not a full rationale** — it is a Credit Bulletin published only to update bank-wise facility details, whose own text directs the reader to a Rating Rationale of 31 August 2025 that is **not in the library**. So the library holds neither the current rating nor the reasoning behind the previous one.

**Independent view formed before opening the anchor:** the FY26 evidence alone (gearing 1.97→1.26x, adjusted debt/EBITDA 5.43→3.86x, first positive FCF since the greenfield, absolute debt reduction) supports a one-notch upgrade from BBB+. The Q1FY27 step-change (48% annualised revenue uplift, margin 17.4%→24.2%, WC 190→143 days) confirms it. **Divergence against the current action: none — both arrive at A-.** Divergence against the superseded library file: one notch, and the library is wrong, not the analysis.

**This is CLAUDE.md failure mode 24 recurring.** Identical shape to the Indus Towers error of 13-Aug: a superseded rating in the reference library, the current one disclosed in the issuer's own documents. The difference is that the Step-1a pre-flight forced the search this time, and probe [2] (18 hits on the AR credit-rating note) is what led to the corroborating check of the quarterly decks that surfaced line 290.

---

## Step 4 — RATIO SUITE (`compute_ratios.py`; workbook `..._Financial_Spreads.xlsx`)

| Ratio (Rs crore, consolidated) | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Revenue | 595.70 | 675.64 | 830.03 |
| EBITDA | 106.67 | 119.40 | 144.46 |
| EBITDA margin % | 17.9 | 17.7 | 17.4 |
| PAT | 57.12 | 6.02 | 25.26 |
| CRISIL adjusted debt | 579.05 | 582.56 | 557.93 |
| Adjusted networth | 293.36 | 420.60 | 441.31 |
| **Gearing (x)** | 1.97 | 1.39 | **1.26** |
| TOL/TNW (x) | 2.38 | 1.60 | 1.63 |
| **Adj debt / EBITDA (x)** | 5.43 | 4.88 | **3.86** |
| Interest coverage, PBDIT/int (x) | 7.25 | 2.03 | 2.60 |
| EBIT/interest (x) — MD&A basis | 6.19 | 1.18 | 1.61 |
| RoCE % | 10.4 | 6.9 | 9.0 |
| Receivable days | 76 | 80 | **90** |
| Net working capital days | 124 | 179 | 149 |
| FCF | −247.00 | 33.87 | **77.24** |

**Conventions.** Adjusted debt = borrowings + Ind AS 116 lease liabilities. Director/KMP unsecured loans of Rs 47.00 crore treated as **debt**, not equity, under CRISIL Box 1 — no evidence of subordination and interest of Rs 4.53 crore was paid in FY26.

**Tie-outs — five independent checks, all reconciled exactly:**

| Check | Computed | Disclosed | Source |
|---|---|---|---|
| FY26 gearing | 1.26 | 1.26 | Company MD&A ratio table |
| FY26 EBIT/interest | 1.61 | 1.61 | Company MD&A ratio table |
| FY26 borrowings | 540.94 | 540.9 | Q4FY26 deck bar chart (LT 305.2 + ST 235.7) |
| FY26 revenue | 830.03 | 830.03 | Q4FY26 deck |
| FY26 EBITDA | 144.46 | 144.46 | Q4FY26 deck (derived PBT+D+I gives 144.29, 0.1% variance) |

**Second, non-Python computation (Step 17):** the Excel workbook's formulas were evaluated independently by the `formulas` engine, returning gearing 1.2643, coverage 2.6001, TOL/TNW 1.6288 — matching the Python suite to four decimals.

---

## Step 15 — MATERIALITY SWEEP

| Item | Amount | Treatment |
|---|---|---|
| GST dispute | Rs 38.54 cr | Static across four fiscals, no provision, pending before authorities. Not adjusted; disclosed as contingent. Would consume ~9% of networth if crystallised |
| Customs duty dispute | Rs 1.75 cr | Immaterial |
| Capital commitments | Rs 27.51 cr | Rising from Rs 6.96 cr — consistent with the FY27 capex step-up |
| Director/KMP loans | Rs 47.00 cr | Treated as debt (see conventions) |
| LTSA customer advances | Rs 98.12 cr received | Contract liability, not permanent capital — explicitly reflected in the "Adequate" not "Strong" liquidity call |
| Exceptional items | Nil, all three fiscals | None |
| Emphasis of Matter | None, all three fiscals | Unmodified opinions throughout |

---

## CORROBORATION GATE (failure mode 15 — picture-text)

Chart-derived figures were **not** accepted on a single read:

| Chart figure | Corroborated by | Result |
|---|---|---|
| FY26 debt Rs 540.9 cr (deck bar chart) | Balance sheet Note 15 + Note 20 = Rs 540.94 cr | **Confirmed** |
| FY26 EBITDA Rs 144.46 cr (deck) | Derived PBT + depreciation + finance cost = Rs 144.29 cr | Confirmed, 0.1% |
| Domestic/international split 38%/62% (FY26 infographic) | **Conflicts** with the same AR's narrative text saying 32% domestic | **Unresolved — 6pp gap.** Report uses "about 62% exports", the figure common to both readings, and avoids the domestic number entirely |
| Q1FY26 EBITDA 33.87 cr (Q1FY26 deck) | Restated to 32.70 cr in three later decks | Later figure adopted |
| Promoter stake 67.91% (chart) | Shareholding table, FY26 AR | Confirmed |

---

## Step 12b — SCORECARD ANCHOR

| Factor | Weight | Score | Basis |
|---|---|---|---|
| Industry / operating environment | 20% | 3 | Speciality chemicals favoured over bulk by CRISIL criteria; offset by crude-linked inputs and demonstrated tariff impact on FY26 utilisation |
| Market position | 20% | 3 | Rs 830 cr revenue, 140+ products, ~62% exports, customer-funded 15-yr LTSA; concentration undisclosed |
| Financial risk profile | 45% | 4 | The binding constraint — leverage still elevated, coverage thin, WC heavy, though improving fast |
| Management & governance | 15% | 3 | Clean audits; watch items on KMP loans, CSR underspend, GHG disclosure gap |

**Weighted composite 3.45 → upper-BBB/A- boundary.** Analyst view **Crisil A-/Stable · Crisil A2+**, placed at the upper end of the anchor band on the strength of the Q1FY27 inflection and the deleveraging trajectory. Divergence from anchor: within one notch, no override required.

Short-term rating: A- maps to "(A1) A2+" per the corporates column of the LT↔ST mapping table in `basics-of-ratings.md` (June 2026). **A2+** selected — the conservative end — given high working capital limit utilisation.

---

## METHODOLOGY COMPLIANCE MAP

| CRISIL criteria section | Applied where |
|---|---|
| Section I — manufacturing framework | Business/financial/management risk structure of the drivers |
| Section IV — financial ratios | Gearing, TOL/TNW, interest coverage, NCATD, RoCE, current ratio, GCA days; Box 1 on promoter loans |
| Section V — chemical industry | Speciality-vs-bulk product profile, export mix as a quality signal, cost of production, in-house technology, multi-product capacity flexibility |
| `criteria-for-consolidation.md` (Feb 2025) | Full consolidation of both wholly owned subsidiaries — same business, not ring-fenced |
| `basics-of-ratings.md` (June 2026) | Rating scale, outlook definition, LT↔ST mapping |

**No numeric threshold table was fabricated.** CRISIL's own text states it "does not adopt an arithmetic approach in using these ratios; instead, it makes a subjective assessment" — no rating-category bands are published, and none were invented.

---

## HOUSE-STYLE NOTE (deviation from the generic template, deliberate)

Three CRISIL chemicals-sector peer reports (Privi Speciality, Galaxy Surfactants, Neogen Chemicals) were read for format. **None carries a standalone ESG section** — CRISIL weaves environmental and social risk into the drivers narrative. An explicit "ESG Profile" section is nonetheless included here because it is a standing requirement of this project (failure mode 19, after ESG was dropped from four consecutive reports) and because the user specifically asked for it. Recorded as a known, intentional divergence from CRISIL house style rather than an error.

Other house-style points adopted from the peers: "Rs 830 crore" with no full stop after Rs; ratios stated as "times"; "fiscal 2026" not "FY26"; Analytical approach written as prose, not a table.

---

## Step 17a — DELIVERY GATE

```
python check_sections.py "Companies/yasho-industries/Yasho Industries Limited_14 Aug 2026_CRISIL_Rating Rationale.md"
[PASS] all mandatory sections present; quality probes clean
1 passed, 0 failed on mandatory sections.   EXIT=0
```

Two warnings were raised on the first run and both fixed rather than waived: an unevidenced absence claim (now carries patterns, hit counts and the verbatim aggregate formulation found) and a missing disclaimer phrasing.

---

## OPEN ITEMS FOR THE ISSUER

1. Lender-wise split of the Rs 217.01 crore of non-HDFC facilities — searched, genuinely undisclosed.
2. Customer concentration — no metric disclosed in any of the eight documents.
3. FY26 Scope 1/Scope 2 GHG emissions — the company's own BRSR marks these "Under Process".
4. The 6pp conflict between the FY26 revenue-split infographic (38% domestic) and the AR narrative (32% domestic).
5. Whether the director/KMP unsecured loans are formally subordinated — would change the Box 1 treatment and improve gearing.
6. The full CRISIL Rating Rationale of 31 August 2025, referenced by the February 2026 bulletin but absent from the reference library.
