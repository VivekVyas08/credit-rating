# ITC Limited — Ratio Workpaper & Analytical Workpaper
*Prepared under CLAUDE.md SOP (19 steps). Basis: standalone (ICRA convention for ITC; consolidation immaterial to leverage — see §7). Data cut-off: audited FY2026 (year ended 31 Mar 2026), Report & Accounts 2026. All figures Rs crore, ICRA definitions per 927/960/1012. Computation script: `Companies/itc/compute_ratios.py`.*

---

## 1. Input inventory (Step 1)

| Document | Period | Audited? | Basis |
|---|---|---|---|
| Report & Accounts 2026 | FY2026 (+FY2025 comparative) | Audited (S R B C & CO LLP) | Standalone & Consolidated |
| Report & Accounts 2025 | FY2025 (+FY2024) | Audited | Standalone & Consolidated |
| Report & Accounts 2024 | FY2024 (+FY2023) | Audited | Standalone & Consolidated |
| Q4 FY2026 press release + investor presentation | Q4/FY2026 | Company-reported | — |
| Q1–Q3 FY2026 result FAQs | 9M FY2026 | Company-reported | — |
| Broker notes (ICICI Securities, Motilal Oswal, Yes Securities) | — | Third-party | Used only for sector/demand assumptions, never as fact source |

**Missing / handling:** Instrument term sheets / sanction letters — NOT provided. Rated amounts and instrument-level detail (Annexure I) therefore **cannot be populated** and must be supplied by the user or the rating shown at issuer level only. No prior-CRA data. No management projections (base case built from historicals + AR guidance + broker demand view per SOP Step 12).

## 2. Routing (Step 2)

Non-financial corporate, FMCG conglomerate → **Corporate Credit Rating Methodology (July 2025) + Rating Methodology for Entities in the FMCG Industry (February 2026)**. Matches empirical routing map (ITC Limited → "Corporate Credit Rating Methodology; FMCG") and the FY2025-demerged post-Hotels business mix. Cross-cutting applied: Financial Ratio Analysis (Sep 2024), Liquidity Analysis – Non-Financial Sector (Mar 2026), Consolidation (Nov 2024), Outlook & Watch policy. Scope statements verified — both methodologies cover non-financial corporates; neither excludes ITC.

## 3. Computed ratio suite (Steps 5–6) — standalone

| Metric | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| Operating income (Rev from ops) | 70,251.28 | 70,105.29 | 74,238.13 | 81,640.11 |
| OPBDIT | 23,944.47 | 24,478.61 | 24,025.61 | 25,208.22 |
| OPBDIT margin % | 34.1 | 34.9 | 32.4 | 30.9 |
| PAT (continuing) | 18,753.31 | 20,421.97 | 20,093.29 | 20,286.42 |
| PAT/OI % | 26.7 | 29.1 | 27.1 | 24.8 |
| Total debt (borrowings + leases) | — | 311.97 | 156.75 | 2,162.39 |
| TOL/TNW (x) | — | 0.21 | 0.24 | 0.27 |
| Gearing – Total debt/TNW (x) | — | 0.00 | 0.00 | 0.03 |
| Total debt/OPBDIT (x) | — | 0.01 | 0.01 | 0.09 |
| Interest coverage (OPBDIT/Fin cost, x) | 572.7 | 535.3 | 661.0 | 360.4 |
| RoCE % (op PBIT / avg CE) | — | — | 31.6 | 33.1 |
| Cash + current liquid investments | — | 18,134.57 | 18,474.80 | 21,837.06 |
| Net debt (TD − liquid) | — | −17,822.60 | −18,318.05 | −19,674.67 |
| Non-current investments (treasury+strategic) | — | 22,821.94 | 20,692.67 | 19,409.05 |
| Total cash + all investments | — | 40,956.51 | 39,167.47 | 41,246.11 |

Revenue growth: FY24 −0.2%, FY25 +5.9%, FY26 +10.0%. PAT growth (continuing): FY24 +8.9%, FY25 −1.6%, FY26 +1.0%.

**Trend commentary.** Operating income compounded to Rs 81,640 cr in FY2026 on 10% growth, the fastest in the window, led by FMCG-Others (segment revenue Rs 24,209.75 cr, +10.1% — traced, AR2026) and sustained cigarette growth. OPBDIT margin eased ~350 bps over three years (34.9%→30.9%) as input costs (edible oil, wheat, cocoa, wood) stayed elevated and mix shifted toward lower-margin FMCG-Others and Agri; still exceptional for the sector. Leverage is effectively nil throughout: the FY2026 rise in total debt to Rs 2,162 cr is short-term borrowing against a Rs 69,929 cr net worth and Rs 21,837 cr of current liquid investments — the company remains deeply net-cash (net cash Rs 19,675 cr, or Rs 41,246 cr counting non-current investments). Interest cover is not economically meaningful (360x) — ITC is a net lender, not a borrower.

## 4. Methodology Compliance Map (Step 10)

| Rating factor (methodology) | Section | ITC evidence | Assessment vs indicative band | Weight |
|---|---|---|---|---|
| Industry position / growth (FMCG) | Industry Risk | Diversified FMCG; low per-capita penetration; stable demand | Favourable industry | Med |
| Scale & market position | Business Risk | OI Rs 81,640 cr; #1 in cigarettes (~77%+ organised share), top-tier FMCG-Others, leader in value-added paperboard | **Strong** | High |
| Diversification (segment/geographic) | Business Risk | 4 segments — Cigarettes, FMCG-Others, Agri, Paperboards/Packaging; pan-India | **Strong** | High |
| Profitability / RoCE (Indicative: ≥25% strongest) | Financial Risk | RoCE 33.1% (FY26), 31.6% (FY25); OPBDIT margin 30.9% | **Strongest band** (≥25%) | High |
| Leverage — Indebtedness (≤0.9x strongest) | Financial Risk | TOL/TNW 0.27x | **Strongest band** (≤0.9x) | High |
| Leverage — Debt/Profit (≤0.5x strongest) | Financial Risk | Total debt/OPBDIT 0.09x | **Strongest band** (≤0.5x) | High |
| Coverage — Interest cover (≥18x strongest) | Financial Risk | 360x | **Strongest band** (≥18x) | Med |
| Coverage — DSCR (≥4x strongest) | Financial Risk | n/m — negligible repayments vs OPBDIT Rs 25,208 cr | **Strongest** (n/m favourable) | Low |
| Liquidity | Financial Risk | Rs 21,837 cr current liquid + Rs 19,409 cr non-current inv; no meaningful repayments | **Superior** | High |
| Working capital | Financial Risk | Modest cycle; agri-inventory build funded internally | Comfortable | Low |
| Parent/Group support | Other elements | BAT group ~23% (TMI 20.31%, traced) but ITC professionally managed, no promoter; standalone AAA — no support notching needed | Neutral (not support-driven) | — |
| Management & governance | Mgmt Quality | Professional board; clean audit; high disclosure | Comfortable | Med |
| ESG | ESG | FMCG low E risk; tobacco = social/regulatory risk (S); governance sound | Low–moderate, asymmetric | Med |

Notching: none. No parent/group support factored (standalone profile already at the top of the scale); no instrument-level adjustments possible without term sheets.

## 5. Liquidity (Step 11) — descriptor: **Superior**

Sources (as on 31 Mar 2026, standalone): cash & current liquid investments Rs 21,837 cr; non-current investments Rs 19,409 cr; annual CFO comfortably >Rs 15,000 cr (OPBDIT Rs 25,208 cr less tax/WC). Claims: total debt only Rs 2,162 cr (largely short-term, self-liquidating); leases Rs 136 cr; routine capex (CWIP Rs 1,473 cr); dividends (high pay-out ~Rs 15,000–16,000 cr p.a.). Even after full dividend and capex, internal accruals and the cash pile leave an enormous surplus; no refinancing dependence. Arithmetic conclusion = **Superior**.

## 6. Independent rating view (Step 13) — formed BEFORE opening ITC's prior ICRA report

- **Standalone assessment:** Every applicable FMCG indicative metric sits in the *strongest* band; deeply net-cash; dominant, diversified franchise; superior liquidity. This is an unambiguous **[ICRA]AAA** financial and business profile.
- **Support notching:** none required (standalone already AAA). BAT's ~23% is a shareholding, not a support anchor; ITC is not rated on parent support.
- **Instrument-level:** plain long-term facilities / CP would be Simple complexity. Rated amounts pending term sheets.
- **LT/ST mapping (per mapping.md / KB04):** AAA → **A1+** invariably.
- **Outlook:** **Stable** — profitability and net-cash position are structural; no downgrade trigger visible over 2 years.

**My independent conclusion: [ICRA]AAA (Stable) / [ICRA]A1+.**

## 7. Consolidation note

Consolidated FY2026: revenue Rs 89,913 cr, PAT to owners Rs 20,689 cr, finance cost Rs 85 cr, OPBDIT margin ~30.4% — subsidiaries (Agri, others) add scale but no leverage. Consolidated leverage is as negligible as standalone. ICRA rates ITC on a standalone basis; consolidation does not change the assessment. Annexure II (consolidated-entity list) to be populated from the AR at drafting.

## 8. Materiality sweep (Step 8)

| Finding | Include/exclude | Reason |
|---|---|---|
| **GST 2.0 cigarette taxation reset, w.e.f. 1 Feb 2026** — GST raised from 28% of transaction value to 40% of retail sale price + higher excise on phasing-out of Compensation Cess; tax incidence up ~60–65%; ~35% MRP hike needed for EBIT-neutrality. Cigarettes = ~84% of FY26 segment PBIT. FY27 cigarette earnings at risk (external estimates: flat to −19% EBIT). Traced to **ITC's own Q4 FY2026 press release** + broker notes (Motilal/ICICI/Yes). Also explains the near-doubling of standalone excise (FY26 9,656 vs FY25 4,912) and why gross revenue/excise are "not strictly comparable" YoY. | **Include — CENTRAL near-term credit development** | Missed in the first draft (broker notes not read; anchor's obsolete "stable tax regime" line copied). Rating (A1+) holds — net-cash balance sheet absorbs it — but rationale/challenges/E&S rewritten around it. |
| **ITC Hotels demerger (effective FY2025)** — Rs 15,104 cr discontinued-ops profit in FY2025; net worth stepped down FY2024 (72,233) → FY2025 (67,894) as hotel net assets distributed | **Include** | Explains the FY2024→FY2025 discontinuity; FY2024 revenue (70,105, incl. hotels) not like-for-like with FY2025 continuing (74,238). Disclose in report. |
| FY2026 rise in short-term borrowings to Rs 2,026 cr | Include (context) | Immaterial to leverage; note it is short-term against huge liquidity, not a credit concern |
| BAT group ~23% shareholding / ITC an associate of BAT | Include | Ownership/ governance disclosure; related-party balances present (AR notes) |
| Tobacco = regulatory/social risk (GST/excise on cigarettes) | Include | Core sector risk; a credit challenge and ESG-social point |

## 9. Caveats

1. **Rated amounts/instrument details unavailable** — no term sheets provided; Annexure I cannot be completed and the Summary-of-rating-action amounts are unknown. The rating opinion is at issuer level.
2. FY2023/FY2024 P&L as-reported still included the Hotels business; FY2025/FY2026 are continuing-operations (post-demerger). Growth across that boundary is not strictly like-for-like — flagged.
3. Broker notes used only for forward sector/demand colour, never as a fact source.
4. Segment-level and shareholding figures traced to AR2026 (FMCG segment Rs 24,209.75 cr; TMI 20.31%); remaining Annexure/About-the-company detail to be pinned from the AR at drafting.
5. Data cut-off: 31 Mar 2026 audited; no post-cut-off events incorporated beyond Q4 FY2026 disclosures.

---

## 10. REVISION after Step 14 (divergence vs ITC's prior ICRA report, 27 Nov 2025)

Opening the anchor (only AFTER the independent view was formed) surfaced four items; my independent view is unchanged in substance but the presentation basis is corrected:

| # | Divergence | Resolution |
|---|---|---|
| 1 | **ICRA's Operating Income is net of excise duty.** My first pass used gross Revenue from Operations, overstating OI and understating margins (30.9% vs the correct ~35%). | **Corrected.** OI = Revenue − Excise duty. Recomputed suite reconciles to the anchor closely (standalone FY2025 OI 69,326 vs 69,324; consolidated FY2025 OI 75,323 vs 75,323 exact). NOTE: consolidated FY2025 PAT is computed independently as **19,731** (continuing profit 20,036.42 − NCI 305.85), NOT the anchor's 19,926 — the anchor figure was on a slightly different basis and must not be inherited. |
| 2 | **Rating basis is consolidated,** not standalone (anchor: "ICRA has considered the consolidated financials"). | **Adopted consolidated as primary;** standalone shown alongside (KI table below). Leverage negligible on both. |
| 3 | **Non-current investments ~Rs 13,000 cr = market securities only** (consolidated Rs 13,721 cr FY2025); my standalone Rs 20,693 cr also embeds strategic stakes (ITC Hotels ~40%, subsidiaries). | Liquidity argument relies on **current** liquid investments (Rs 23,759 cr consolidated FY2026), not on all investments. |
| 4 | **Only ICRA-rated instrument = Rs 500 cr Commercial Paper → [ICRA]A1+.** No long-term ICRA rating outstanding. | Report is a **short-term A1+ CP** reaffirmation (no outlook). Underlying long-term profile assessed AAA-equivalent, which supports A1+. **Rs 500 cr amount is anchor-sourced → REQUIRES USER CONFIRMATION** (no term sheet provided). |

Also anchor-sourced, flagged for confirmation: cigarette organised-market share ~75%; Rs 20,000 cr medium-term capex plan; Century Pulp & Paper acquisition ~Rs 3,500 cr (internal-accrual funded); ITC ~40% in ITC Hotels (associate).

### Corrected KI table (ICRA basis — net-of-excise OI)

| ITC | Standalone FY2025 | Standalone FY2026 | Consolidated FY2025 | Consolidated FY2026 |
|---|---|---|---|---|
| Operating income | 69,326 | 71,984 | 75,323 | 78,868 |
| PAT | 20,093 | 20,286 | 19,731 | 20,689 |
| OPBDIT/OI % | 34.7 | 35.0 | 34.5 | 34.6 |
| PAT/OI % | 29.0 | 28.2 | 26.2 | 26.2 |
| TOL/TNW (x) | 0.2 | 0.3 | 0.3 | 0.3 |
| Total debt/OPBDIT (x) | 0.0 | 0.1 | 0.0 | 0.1 |
| Interest coverage (x) | 661.0 | 360.4 | 576.5 | 320.7 |
| RoCE % (op PBIT/CE) | 32.5 | 32.2 | 33.7 | 33.3 |

**Credit-quality conclusion unchanged:** every FMCG indicative metric remains in the *strongest* band; A1+ reaffirmed. No change to my independent view — only the OI basis and rating scope were corrected via the anchor, both disclosed here.
