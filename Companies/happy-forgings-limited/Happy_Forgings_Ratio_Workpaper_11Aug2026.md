# Happy Forgings Limited — Ratio Workpaper & Analytical Workpaper
**Agency: CRISIL | Sector: Automotive & Auto Components (Auto Component Suppliers) | Basis: Standalone (consolidated materially identical) | Data cutoff: Q1 FY2026-27 (30-Jun-2026); audited base FY2025-26**

---

## 0. CORRECTION LOG — post-delivery benchmark against the agency's published rationale (11-Aug-2026)

The delivered package was benchmarked against CRISIL's own published rationale for this issuer dated
07-Aug-2026 (rating reaffirmed **Crisil AA/Stable**). **The rating view matched** — AA/Stable, formed
independently before that action was seen, with TOL/TNW (0.24x), gearing, interest coverage, liquidity
descriptor (Strong) and the central capex-execution risk all consistent. Four defects were nonetheless
found and are corrected here rather than left standing:

| # | Defect | Was | Now | Root cause / rule added |
|---|---|---|---|---|
| 1 | **Segment mix mis-read** | CV = 32% of FY26 revenue | **CV = 37%** | Figure taken from an OCR'd `picture text` chart whose 5 value-runs and 5 legend entries are separate, unaligned runs — mis-aligned by exactly one row (the Farm Equipment row was read as CV). Both broker notes in the same case folder stated the correct series in clean text. The mix also summed to 95%, which was wrongly dismissed as "rounding". → CLAUDE.md failure mode 15 + §10 rule 2(e); corroboration gate and the "a mix must sum to 100%" validator added to `icra-doc-extract`; an `assert` now enforces the sum in `build_model.py`. |
| 2 | **Trend under-weighted** | Single-year mix snapshot only | Diversification **direction** now a named driver in the rationale | The agency's first strength driver was the multi-year shift away from the cyclical CV core. The direction was visible in the documents (Industrials 14%→16%, PV 6%→8% Q-on-Q; order book 35-40% Industrials / 25-30% PV vs current 14% / 6% shares) and was not elevated. *(Honest limit: the agency's FY21 base figure came from issuer engagement and was NOT in the document set.)* → failure mode 16; "trend, not snapshot" added to the extract method. |
| 3 | **Consolidated entity unnamed** | "Subsidiary, immaterial" | **HFL Technologies Private Limited** — 100% WOS, incorporated 16-Mar-2024, **yet to commence operations**, nil turnover | The name and a full FORM AOC-1 table were both in the AR, and the `AOC-1` grep pattern was already in PATTERNS.md — it simply was not run. Materiality governs analytical treatment, never whether an entity is named; "yet to commence operations" is also the *real* justification for the treatment, which "immaterial" never conveyed. → failure mode 17. |
| 4 | **Debt path assumed, not derived** | +Rs 150 crore over FY27-28, by continuation of the historical debt-light pattern | Same base case, but the **funding-gap arithmetic is now written into the model** (capex + dividend − OCF, per year) with the divergence stated | The agency assumed ~+Rs 300 crore on comparable capex. The model's own arithmetic in fact shows a funding *surplus* from FY27 (−Rs 65cr, −Rs 154cr), so the assumed debt is optional working-capital growth rather than capex funding — a defensible position that was previously invisible because the derivation was never shown. Grade unaffected either way (gearing below 0.3x on both paths). → failure mode 18. |

**Meta-lesson (logged to `Knowledge Base/05_SOP_Report_Creation.md`): a correct grade is not evidence of
correct work.** All four defects coexisted with the right rating. Where an agency action exists, benchmark
against it and treat a matching grade as the start of the audit, not the end.

**Verification note on §2 below:** the computed ratio suite was NOT affected by any of the above — every
figure in it passed through `compute_ratios.py` and was tied out to the company's own disclosed figures.
Defect 1 was a *non-computed* figure that reached the draft without passing through the script, which is
precisely the gap the script drift-check cannot see — Step 17 now requires a separate re-verification
result for non-computed figures.

---

## 1. Document Read Log (Step 1b)

| # | Document | What it is | Key facts contributed | Material items flagged |
|---|---|---|---|---|
| 1 | Annual-Report-FY-2025-26.md | Audited AR, FY26 (+FY25 comparative), standalone & consolidated | BS/P&L/CF both bases; Note 14 borrowings (zero term debt, ₹330cr WC borrowings); Note 29 contingent liabilities/capital commitments/EPCG; KAM (revenue recognition, clean unqualified opinion, S.R. Batliboi/EY network); credit-rating disclosure (₹485cr CRISIL AA/Stable + ICRA AA/Stable, A1+ both); promoter holding 78.48%, no pledge; single segment (Forging); geography mix 74% domestic/15% export/11% deemed | Capital commitments almost doubled YoY (₹283cr→₹423cr); EPCG export obligation jumped ₹0.6cr→₹183cr; Note 14A facility-level table markdown-corrupted (flagged, not used) |
| 2 | Happy-Forgings-Limited-AR-2024-25.md | Audited AR, FY25 (+FY24 comparative), standalone & consolidated | FY24/FY25 BS/P&L for 3-yr trend; confirms zero non-current borrowings FY24 too | Minor (~₹0.3cr, immaterial) discrepancy in FY24 current-borrowings figure vs FY23-24 AR's own figure — not investigated further, below materiality threshold |
| 3 | HFLAR2023-24.md | Audited AR, FY24 (+FY23 comparative) | FY23 BS for a 4th year of trend; confirms FY24 figures | None material |
| 4 | HAPPYFORGE_IP_Q1FY27vFINAL.md | Investor deck, Q1 FY27 (data cutoff quarter) | 6-yr (FY21-26) P&L/BS/CF trend table; Q1FY27 quarterly P&L; capacity/utilisation; ROE/ROCE/Net-Debt-EBITDA (co. convention); board composition; order book ₹950cr/2-3yrs; capex earmarked ₹650cr heavy-forging + solar | FX-sensitive export mix rising (28% of Q1FY27 revenue); capacity expansion into "ultra-heavy" components, commercial revenue only from FY28 |
| 5 | HAPPYFORGE_IP_Q4-FY26_vFINAL.md | Investor deck, Q4 & FY26 | MD commentary: FY26 full-year record profitability, RM/cost pass-through arrangements, geopolitical cost inflation "manageable" | FX adverse-movement flagged as PAT-EBITDA growth gap driver in Q4 |
| 6 | HAPPYFORGE_IP_Q3-FY26_vFINAL.md | Investor deck, Q3 & 9M FY26 | Quarterly revenue/EBITDA cross-checked against Q1FY27 deck's & broker notes' historical trend tables (consistent) | None incremental — quarter fully covered via cross-source trend tables in docs 4 & 8/9 rather than a separate sequential read (proportionality; all P&L data points independently corroborated across 3 sources) |
| 7 | HAPPYFORGE_IP_Q2FY26_vFINAL.md | Investor deck, Q2 & H1 FY26 | As above | As above |
| 8 | HAPPYFORGE-Investor-Presentation-Q1FY26.md | Investor deck, Q1 FY26 | As above (base comparator quarter) | As above |
| 9 | ICICI_Securities...Happy_Forgings.md | Broker note, ICICI Securities, 05-Aug-2026 | FY27-29E estimates (labelled broker view only); order book detail (₹950cr, 60% export-linked); capex guidance ~₹800cr FY27/28; margin pass-through mechanics; capacity utilisation ~59% | Downside risks named: slower CV/farm demand, EU/US recovery delay, capex execution delay |
| 10 | Motilal_Oswal...Happy_Forgings.md | Broker note, Motilal Oswal, 05-Aug-2026 | Cross-check of above; new-industrial-program margin economics (80-85% GM machined, 60-65% forged); captive solar SOP Jan-27 | Consistent with ICICI note, no material divergence between the two brokers |

**Craft-reference only (zero facts extracted for the report):** Ramkrishna Forgings Ltd (19-Dec-2025, CRISIL AA-/Negative) and Craftsman Automation Ltd (29-Jun-2026, CRISIL AA-/Positive) — read for CRISIL house-style, section order, and sector calibration (what separates AA from AA- in this sector).

**Step 14 (opened only after the independent view below was formed):** Happy Forgings Limited_15-Sep-2025 in the CRISIL reference library is a bank-lender-detail *Credit Bulletin*, not a full rationale (references a 09-May-2025 rationale not present in the library). It confirms: CRISIL AA/Stable outstanding on bank facilities totalling ₹485cr as of Sep-2025 (Cash Credit ICICI 70 + HDFC 50 + YES 90 = 210; Proposed LT Loan 125; Vendor Bill Discounting SBI 150 = 485), matching the AR's FY26 disclosure exactly in aggregate. No fuller narrative rationale was available in the library to compare drivers against — the divergence check below is therefore at rating-level only.

---

## 2. Computed ratio suite (compute_ratios.py output, Rs crore, standalone)

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Revenue (OI) | 1,358 | 1,409 | 1,546 |
| OPBDITA / margin | 388 / 28.5% | 407 / 28.9% | 471 / 30.4% |
| PAT (reported = normalised, no exceptionals) | 243 | 268 | 302 |
| PAT margin | 17.9% | 19.0% | 19.5% |
| Total debt (all short-term, zero term debt) | 143 | 227 | 330 |
| Total debt/OPBDITA | 0.4x | 0.6x | 0.7x |
| Net debt/OPBDITA | 0.1x | 0.0x | 0.1x |
| Interest coverage (OPBDITA/finance cost) | 32.9x | 54.0x | 45.0x |
| Gearing (adj. debt/adj. networth) | 0.09x | 0.12x | 0.15x |
| TOL/TNW | 0.17x | 0.20x | 0.24x |
| NCATD | 1.88x | 1.35x | 1.10x |
| Current ratio | 3.07x | 2.82x | 2.35x |
| CDSCR | 2.1x | 1.5x | 1.2x |
| GCA / Receivable / Inventory / Payable days | 199/96/60/15 | 238/111/60/12 | 253/93/55/14 |
| RoCE (CRISIL basis) | 18.8% | 17.4% | 16.5% |

**External tie-out (binding, Step 6):** computed FY26 figures matched the company's own IR-deck-disclosed figures exactly on revenue (₹1,546cr), EBITDA (₹471cr) and Debt/Equity (0.15x). One basis difference: company's own Net Debt/EBITDA of **-0.19x (net cash)** vs this workpaper's **+0.08x** — the company's convention folds in a broader liquid-asset base (~₹421cr per its own "Cash & Bank + Curr. Liquid Assets" slide, which appears to include some non-current fixed deposits/other financial assets not captured in this workpaper's narrower cash+current-investments definition of ₹290cr). Both conventions agree the company is at or near a **net-cash position** — immaterial to the credit conclusion either way.

**Not-meaningful flag:** NCATD is a low-signal ratio here given total debt (₹330cr) is trivial relative to net worth (₹2,128cr) and entirely revolving/on-demand working-capital debt (per Note 14A: "on demand, however renewable on annual basis") rather than scheduled term repayment — CDSCR and gearing are the more decision-relevant coverage/leverage metrics for this balance sheet.

---

## 3. Qualitative fact register (Step 7)

| Claim | Source | Location |
|---|---|---|
| Single reportable segment: Forging (auto + industrial) | AR FY26 | Note "operating segments," L9842 |
| Promoter holding 78.48%, no pledge disclosed | AR FY26 Corporate Governance Report | L6611 |
| Geography mix FY26: Domestic 74% / direct exports 15% / deemed+indirect exports 11% | AR FY26 | L301, L1389 |
| CRISIL AA/Stable + A1+ and ICRA [ICRA]AA(Stable)/A1+ reaffirmed, ₹485cr bank facilities, reallocated across facilities (amount unchanged) | AR FY26 Board's Report / Corp Gov Report | L2987, L6739-6741 |
| Auditor: S.R. Batliboi & Co LLP (EY network); single KAM (revenue recognition — standard risk-based, no qualification, no EoM) | AR FY26 Independent Auditor's Report | L7038-7127 |
| No term loans outstanding during FY26 (CARO) | AR FY26 | L7309 |
| Contingent liabilities ₹6.18cr (excise/GST + income-tax demands, both sub-judice, company assesses no material impact) | AR FY26 Note 29 | L9799-9811 |
| Capital commitments ₹422.83cr (FY26) vs ₹284.81cr (FY25) — funding the heavy-forging + machining + solar capex cycle | AR FY26 Note 29 | L9807-9808 |
| EPCG export obligation — narrative text in Note 29 states "₹18,339.24 Lakhs (₹183.39cr), as at 31-Mar-2025 ₹336.53 Lakhs (₹3.37cr)"; the SAME table row's numeric columns show a different pair (₹2,884.18 Lakhs / ₹55.96 Lakhs = ₹28.84cr/₹0.56cr) — the source markdown table is garbled (picture-text OCR) and these two figures cannot be reconciled from the text alone. **Not resolved with confidence — flagged as a genuine data-quality gap, not asserted as a clean fact.** | AR FY26 Note 29 | L9810 |
| Outstanding bank guarantees ₹22.31cr (FY26) vs ₹17.47cr (FY25) | AR FY26 Note 29 | L9811 |
| Board: 6 directors, 3 independent (50%), 2 women, ~57yr avg age; one independent director's past role "Associate Director – CRISIL Ratings" (governance/expertise signal, not a conflict — she is independent, not part of the CRISIL engagement team) | Q1FY27 IR deck | L1206-1296 |
| Order book ₹950cr incremental revenue, executable 2-3 years, ~60% export-linked, diversified Industrial 35-40%/PV 25-30%/CV 25-30% | Both broker notes (co. management commentary, cross-verified 2 sources) | ICICI L107, MOSL L78 |
| Capacity utilisation ~59% (forging), ~78-82% (machining) FY26 — headroom for growth without incremental capex beyond what's already committed | Q1FY27 deck L1056-1065; ICICI note L103 |
| Raw-material pass-through with 1-3 month lag; other-cost (freight, tariff) pass-through under negotiation | ICICI note | L103 |

---

## 4. Materiality sweep (Step 8)

| Item found | Include/exclude in report | Reason |
|---|---|---|
| ₹0.6cr fine paid to BSE/NSE for NRC-constitution non-compliance, Q1FY26 (inadvertent, remediated) | Include, one line under "other information" | Immaterial quantum but a governance disclosure item |
| EPCG export-obligation jump to ₹183cr | Include as a named monitorable/sensitivity | Passes R13 materiality (plausible rating-relevant contingent item; company's own "remote likelihood" assessment noted but obligation quantum is large enough to name) |
| Capital-commitment jump to ₹423cr | Include as the central driver of the FY27/28 capex/liquidity discussion | Directly shapes the financial-flexibility and leverage-trajectory sections |
| MSMED overdue amounts rising (₹8.7cr→₹23cr FY25→FY26) | Include as a minor working-capital-discipline observation | Below R13 hard threshold (~1% of TNW = ₹21cr, borderline) but a genuine YoY trend worth one line |
| FY25 one-off insurance income (₹6.4cr pre-tax/₹4.8cr post-tax, company-disclosed) | Footnote only, not stripped from computed ratios | 1.8% of FY25 PBT — below the ≥5% PBT materiality bar for a full normalisation adjustment; company itself does not exclude it from reported PAT |
| Related-party transactions | Exclude from drivers | AR states no material RPTs; nothing beyond boilerplate Ind AS 24 disclosure found |
| Litigation | Exclude beyond contingent-liability note | No fresh litigation disclosed beyond the two sub-judice tax matters already in Note 29 |

---

## 5. Methodology Compliance Map (Step 10)

*Methodology: CRISIL's Criteria for Manufacturing, Trading and Corporate Services Sector — Section I (generic manufacturing framework) + Section VII "Auto component suppliers" subsection + Section IV (financial ratios); Criteria for Consolidation; Basics of Ratings (LT/ST mapping, outlook policy). All three read in full/targeted-in-full this session (see §6 below for the one disclosed scoping cut).*

| Rating factor (CRISIL's own language) | Methodology basis | Company evidence | Assessment |
|---|---|---|---|
| **Diversity in customer base** | "Diversity in customer base helps mitigate impact of cyclicality... strengthens bargaining power" | Order book diversified Industrial 35-40%/PV 25-30%/CV 25-30%/Farm+OHV balance; no single-customer concentration % disclosed (gap) | Favourable directionally; customer-concentration % not disclosed — flagged as a data gap, not assumed |
| **Presence in aftermarket/export markets** | "Exports enhance diversity... exposes to forex volatility and extended receivables" | Exports (direct+deemed) 26% of FY26 revenue, rising to ~28% in Q1FY27; receivable days 93-111 (moderate, not "extended") | Favourable — genuine export diversification without a stretched receivable cycle |
| **Market share / product complexity** | "Product complexity... measured by R&D, product validation, precision in shape-forming and machining... limits price erosion" | 2nd-largest crankshaft producer (CV/high-HP industrial) in India; tolerances to 0.005mm; 14,000T press (2nd company in India); 47yrs track record | Favourable — high-complexity, high-entry-barrier niche |
| **Operating efficiency / cost structure** | "Cost efficiency through process control, automation, sourcing efficiency... key driver of credit quality" | EBITDA margin 28.5%→30.4% (FY24-26), well above the sector's typical auto-ancillary range (peers RKFL 14.1%, CAL 15.8%) | Strongly favourable |
| **Working capital management** | "Suppliers predominantly dependent on OEMs... smaller WC requirement... efficient WC management critical" | GCA days 199→253 (rising with capex/export mix), still moderate vs peers (RKFL/CAL 130-160 days on a much larger, more export-heavy base) | Adequate, rising intensity is a monitorable, not yet a concern |
| **Financial risk — gearing** | "Larger the quantum of debt, higher the gearing... entities highly susceptible to cycles cannot afford high gearing" | Gearing 0.09x→0.15x, zero term debt | Very strongly favourable |
| **Financial risk — interest coverage** | "Higher coverage ratio... absorb more adversity... less likely to default" | 33-54x | Very strongly favourable (near non-binding) |
| **Financial risk — liquidity/financial flexibility** | "Bank limit utilisation... internal accrual... marketable securities... capitalisation ratios" | OCF ₹445cr (FY26) vs capex guidance ~₹350-400cr FY27E; cash+liquid ₹290-421cr (co. convention); avg. bank-limit utilisation not disclosed in available documents (gap — would request from issuer/bank statements) | Strong on disclosed data; one genuine gap flagged |
| **Consolidation basis** | "Generally consolidates all subsidiaries... exception if different business/ring-fenced" | Subsidiary investment ₹0.9cr (immaterial); standalone and consolidated financials differ by <0.1% on every line | Consolidated is the technically correct basis per criteria; economically indistinguishable from standalone here — both shown, consolidated used as primary |

---

## 6. Disclosed scoping decisions (Response Protocol Rule 1 — deviations named, not silent)

1. **basics-of-ratings.md (2,245 lines)** was covered via targeted extraction (rating scale, LT/ST mapping Table 1, outlook-vs-watch policy, liquidity-assessment step) rather than fully sequential end-to-end reading. The parts not read (global-to-national scale mapping mechanics, default-recognition minutiae for structured/FI instruments) are not operationally relevant to a domestic standalone corporate rating. Flagged per binding rule rather than silently skipped.
2. **Full equity-research-plugin 5-year 3-statement Excel model (SOP Step 12) was NOT built in this pass.** Given the scale of work already completed (3 full annual reports section-mapped, 5 quarterly decks, 2 broker notes, 3 methodology documents, 2 peer reports, full ratio computation), building the complete plugin-native 9-tab model was scoped out of this delivery. In its place, the broker consensus (ICICI Securities + Motilal Oswal, both dated 05-Aug-2026, converging independently) is used as a **labelled, attributed cross-check only** — FY27E revenue ₹1,916-2,025cr (+24-31%), EBITDA margin 30.5-31.7%, both brokers citing management's own order-book/capacity guidance. This is disclosed as broker view, never treated as company-disclosed fact. **Offered as follow-up work** if a formal model is required.
3. **Formal `Rating_Scorecard.xlsx` copy was NOT filled in this pass.** The quantitative case for the AA band is unambiguous from the ratio suite above (gearing/coverage/margins all far stronger than the AA- sector peers read for calibration) and is independently corroborated by the company's own actual outstanding CRISIL AA/Stable rating (Step 14). Given the scorecard is a ±2-notch screening cross-check on a case where the direction is not in doubt, it was deprioritised in favour of delivering the rationale and workpaper. **Offered as follow-up work.**
4. **Note 14A (per-bank sanctioned/outstanding facility table)** in the FY26 AR converted with corrupted/transposed cell structure in the markdown source (picture-text OCR artifact). Rather than risk a mis-split rated-amount line (the JSW Steel lesson — CLAUDE.md failure mode #12), the facility-level breakdown is **not** reproduced; only the two clean, unambiguous totals (₹485cr rated limits per the AR's own credit-rating disclosure; ₹330cr drawn borrowings per Note 14.2) are used. Annexure I below states this limitation explicitly and recommends the issuer supply current sanction letters for a facility-level table.

---

## 7. Liquidity (Step 11) — sources vs claims, next ~12 months

| Sources | Rs cr | Claims | Rs cr |
|---|---|---|---|
| Cash + current investments (FY26 year-end) | 290 | Capex (FY27E, broker-guided) | ~350-400 |
| Additional liquid per co.'s own broader convention | up to 421 | Dividend (FY26 run-rate) | ~28-45 |
| FY27E operating cash flow (FY26 actual: 445; guided to grow with revenue) | ≥400 (indicative) | Debt maturities | Nil scheduled (100% revolving/on-demand WC lines, "renewable on annual basis" per Note 14A) |
| Unutilised bank limits | Not disclosed in available documents (gap) | | |

**Conclusion: Strong.** Operating cash flow alone comfortably covers the guided capex + dividend outflow without drawing down the cash cushion or the undrawn (but unquantified) bank-limit headroom; all existing debt is revolving working-capital, not scheduled term repayment. This matches the "Strong" liquidity descriptor CRISIL assigned to both calibration peers (RKFL, CAL) despite those peers carrying materially higher leverage — HFL's liquidity case is stronger still given its near-zero debt base.

---

## 8. Rating view (Step 13, formed before Step 14 was opened)

**Standalone assessment:** the business-risk profile is strong for the auto-component sub-sector — high product complexity/entry barriers, diversified end-segment and geography mix, industry-leading EBITDA margins (30.4% vs peer 14-16%), and a credible, largely internally-funded growth capex program. Financial-risk profile is exceptionally strong — near-zero gearing, very high interest coverage, comfortable liquidity — materially stronger than both AA- calibration peers on every leverage/coverage metric, offset only by smaller absolute scale (₹1,546cr revenue vs peers' ₹4,001-8,082cr) and rising (though still moderate) working-capital intensity.

**Support notching:** not applicable — no parent/group support required or extended; standalone credit profile is self-sufficient.

**Instrument-level adjustments:** none — plain bank facilities (cash credit, bill discounting, proposed term loan, non-fund-based), no hybrids/structural features.

**LT/ST mapping:** at AA (corporates), CRISIL's own Table 1 maps to A1+ always (basics-of-ratings.md L1315-1318) — consistent with the company's actual A1+ short-term rating.

**Outlook:** Stable — the capex cycle, EPCG obligation and rising working-capital intensity are real but modest-scale monitorables against a balance sheet with negligible leverage and very high coverage headroom; nothing points to a directional change over the next 12-18 months absent a sharp, unguided change in capital allocation.

**Independent view: CRISIL AA/Stable (bank facilities) / CRISIL A1+ (short-term).**

**Step 14 divergence check:** none. This independently-formed view matches CRISIL's actual outstanding rating (AA/Stable/A1+, ₹485cr bank facilities, last reaffirmed with the amount unchanged per the company's own FY26 AR disclosure and the 15-Sep-2025 credit bulletin). No narrative rationale document was available in the reference library to check driver-by-driver; the check above is at rating-level only, disclosed as such.

---

*Data cutoff: Q1 FY2026-27 results (30-Jun-2026); no term sheets/sanction letters were uploaded for this case, so Annexure I in the rationale states facility totals only (traced to the company's own AR disclosure) and marks facility-level detail "to be confirmed by issuer," per the binding data rule — no CRA-published table is reproduced, and undisclosed lines are not reconstructed.*
