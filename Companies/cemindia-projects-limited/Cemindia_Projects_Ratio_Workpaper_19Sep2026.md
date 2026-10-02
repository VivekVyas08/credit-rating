# Cemindia Projects Limited (formerly ITD Cementation India Limited) — Ratio Workpaper (ICRA basis)
*Prepared 19-Sep-2026. Data cutoff: FY2025-26 audited (Board approval 29-Apr-2026). Engagement type: NEW rating (surveillance commitment at §13).*

---

## 1. Document Read Log (Step 1b)

| File | Coverage | Material items found |
|---|---|---|
| `CemindiaAR_2025_26_290526.md` (FY2026 AR, **Rs crore**) | Standalone + consolidated balance sheet, P&L, cash flow; auditor's report incl. KAM and CARO; note 25 other income; notes 16-19A borrowings/supplier's credit; credit-rating note; order-book chart; supplier-finance note; BRSR | **Name change** ITD Cementation → Cemindia Projects; **RenewExim DMCC (Adani) 67.46%**; **credit-rating upgrade to A+ (Stable) from both ICRA and CARE**; order book Rs 24,545 cr on record inflows Rs 14,821 cr; company's own EBITDA Rs 1,199 cr; supplier's credit Rs 96.32 cr in the company's own total-debt definition; CARO 3(ii)(b) observation on quarterly bank returns |
| `ITDCementationAR_24_25_150725.md` (FY2025 AR, **Rs lakh**) | FY2025 + FY2024 comparatives, both bases, on the OLD ITD consolidation basis; auditor's report | **UNIT SWITCH** — this AR is in lakh, the FY2026 AR in crore; **basis restatement** between the two (FY2025 revenue 9,096.94 cr here vs 9,246.16 cr restated in the FY2026 AR); FY2024 base figures; bill-discounting inside borrowings |
| `ITDCementationAR_23_24_030824.md` (FY2024 AR, **Rs lakh**) | FY2024 P&L and balance sheet; exceptional/bad-debt notes | Read for the FY2024 base and the pre-Adani history; interest income Rs 33.12 cr, bad debts written off, provision write-backs — none exceptional, all recurring |
| `Audited_financial_result_31032026.md` | Audited Q4 + full-year FY2026 consolidated result | Ties to the AR: FY2026 revenue 10,060.58, PBT 817.62, PAT 597.73; Q4FY26 revenue 2,973.49; the "reclassification of certain line items" note (no profit impact) |
| `Unaudited_*` (4 files, Q1-Q3 FY2026 + Q1 FY2027) | Interim consolidated results | Intermediate quarters; the operating series is continuous and reconciles to the audited year |

**Pre-flight (Step 1a) was run and its output governs. Four things it reported must be recorded:**
1. **This is a CONSTRUCTION/EPC company, not a cement maker.** The sector detector fired "utilisation / EBITDA per tonne" on 863 hits of "Cementation" in the name and is WRONG. The peers are all EPC/Projects firms (Kalpataru, Power Mech, PSP, Bajel). The correct sector-defining metric is the ORDER BOOK and book-to-bill (§5). Construction methodology (case.json) is right; the "Cement" case tag is a mislabel.
2. **The rated amounts in the library are all PEERS, not this issuer** — PSP Projects, Power Mech (both [match 1/3]). No same-issuer prior action is in the reference library, so the rated amount is taken from the issuer's own AR credit-rating note (§7), not imported from a peer.
3. **The issuer's own AR discloses its rating** (25 hits): **ICRA A+ (Stable), upgraded 29-Jul-2025 from ICRA A**; CARE A+ (Stable), upgraded from CARE BBB-. Step 14 benchmarks against peers (no same-issuer library file) but the AR-disclosed rating IS the anchor.
4. **Aggregate-note contaminants (probe [0c]) and balance-sheet aggregates (probe [0e]) flagged** — forex, bad debts, provision write-backs, interest income inside other income; current maturities of LT debt inside current borrowings; margin money inside cash; bill discounting/supplier's credit inside borrowings. All decomposed at §4/§6.

**Known gaps, handled per Step 1:**
- **No instrument term sheets / sanction letters.** Rated amounts are the issuer's own AR disclosure of the rated facility structure; issuer confirmation of the exact limit remains outstanding.
- **No sector-assumptions document.** The forward view rests on the company's own order book and disclosures; every driver is source-labelled in `forward_model.py`.

---

## 2. Methodology routing (Steps 2/3)

| File | Scope test | Applied? |
|---|---|---|
| `930~Construction, Rating Methodology, Oct 2024.md` | ICRA's construction methodology covers EPC/civil-construction contractors — order book, execution, working-capital intensity, contract profitability. CemIndia is a marine/urban-infra/hydro EPC contractor. Scope fits. | **YES** |
| `960~Corporate Credit Rating Methodology, Jul 2025.md` | Non-financial corporate | **YES** |
| `963~Implicit Parent or Group Support, Rating Methodology, Jul 2025.md` | Cross-cutting; RenewExim DMCC (Adani) holds 67.46% | **YES** — support assessment, §10 |
| `934~Rating Approach, Consolidation, Nov 2024.md` | Cross-cutting | **YES** — basis, §3 |

**Operating-profit convention (per the 13-Sep-2026 correction in CLAUDE.md §12b).** ICRA's OPBDITA RETAINS core-related other income (job-work, scrap, duty drawback) but EXCLUDES interest, dividend and rental income even when recurring. CemIndia's Rs 176.96 crore of FY2026 other income is Rs 94.07 crore of interest income plus Rs 82.89 crore of forex/insurance/PPE-disposal/miscellaneous — **none of it is core-related job-work/scrap/duty-drawback** (a contractor's job-work is inside contract revenue). So stripping all of it from OPBDIT is the correct ICRA treatment here, and is checked rather than assumed.

---

## 3. Basis determination (R12 — methodology-determined)

**CONSOLIDATED** (case.json). The group is the holding company, its joint operations, one subsidiary and one associate. Consolidated and standalone debt are near-identical (borrowings sit at the parent), so the basis choice does not move the leverage story; consolidated is taken because that is the published headline basis on which revenue, order book and profit are reported, and it captures the joint operations that execute a material part of the book.

---

## 4. Ratio suite (ICRA convention, consolidated, Rs crore)

`compute_ratios.py` — **128 of 128 tie-outs reconcile; mutation-measured coverage 100.0%.**

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Operating income | 7,717.87 | 9,246.16 | **10,060.58** |
| OPBDIT (ICRA convention, retains core claim income) | 760.89 | 862.09 | **1,072.02** |
| OPBDIT/OI (%) | 9.86 | 9.32 | **10.66** |
| PAT | 274.18 | 372.78 | **597.73** |
| PAT/OI (%) | 3.55 | 4.03 | **5.94** |
| Total debt | 889.12 | 992.53 | **1,001.23** |
|   — of which long-term | 151.72 | 218.73 | 177.69 |
|   — of which short-term (WC + supplier's credit + current leases) | 737.40 | 773.80 | 823.54 |
| Tangible net worth | 1,498.14 | 1,833.38 | **2,399.59** |
| TOL/TNW (times) | 2.95 | 2.19 | **1.95** |
| Total debt/OPBDIT (times) | 1.17 | 1.15 | **0.93** |
| Interest coverage (times) | 3.49 | 3.65 | **4.99** |
| Gearing (times) | 0.59 | 0.54 | **0.42** |
| Debtor days | 57.3 | 39.1 | **47.0** |
| Unencumbered cash | 895.72 | 509.42 | **634.01** |
| Net debt (of unencumbered cash) | (6.60) | 483.11 | 367.22 |
| Order book (year-end) | 19,918 | 18,300 | **24,545** |
| Order book (current, Jun-30-2026) | – | – | **31,306.8** |
| Order book / OI (current, times) | – | – | **3.11** |

### Trend, not snapshot (failure mode 16)
- **Every leverage and coverage metric improved for two consecutive years**, and materially: gearing 0.59 → 0.42x, TD/OPBDIT 1.17 → 0.93x (now under 1x), interest coverage 3.49 → 4.99x, TOL/TNW 2.95 → 1.95x. Debtor days 47.0 (FY2025 39.1) reconcile to ICRA's published 47/39.
- **Revenue grew each year** — 7,718 → 9,246 → 10,061 — though the FY2024→FY2025 step mixes organic growth with the consolidation-basis change (see the caveat below).
- **PAT grew 60% in FY2026** (373 → 598), on both execution scale and a lower finance cost; margin widened to 5.94%.
- **The order book climbed to Rs 31,306.8 crore as on June 30, 2026** (from Rs 18,300 cr at Mar-2025, +71%; Rs 24,545 cr at FY2026 year-end), on sizeable Adani-group inflow. At **3.1x FY2026 OI** it underwrites medium-term revenue visibility — the sector-defining metric, taken current (Jun-2026) per failure mode 26, not the stale year-end figure.

### Gearing basis note (failure mode 47)
Total debt here follows the **company's own disclosed definition** (non-current + current borrowings + supplier's credit) plus lease liabilities per ICRA. The Rs 96.32 crore supplier's credit is an acceptance-type supplier-finance arrangement. On a strict reading of ICRA's own Corporate methodology, acceptances/LC creditors may sit in Total Outside Liabilities rather than in the Gearing numerator; excluding supplier's credit would give gearing of **0.38x** against the 0.42x reported. Both are very low and support the same rating level; the inclusive figure is used because it matches the issuer's own presentation and TOL/TNW captures it regardless.

### Basis-restatement caveat (disclosed, failure mode 26)
FY2024 sits on the OLD ITD consolidation basis (joint ventures equity-accounted, Rs 4.43 crore non-controlling interest); FY2025-FY2026 sit on the revised Cemindia basis (joint operations proportionately consolidated). The FY2026 AR restates FY2025 revenue to Rs 9,246.16 crore from the Rs 9,096.94 crore the FY2025 AR shows on the old basis. FY2025 is taken from the newer AR; FY2024 is the only figure available and is on the old basis. The direction of every ratio is unaffected; a precise FY2024→FY2025 growth rate carries this caveat.

---

## 5. Sector-defining operating metric (failure mode 21) — the ORDER BOOK

For an EPC contractor the defining metric is the order book and its book-to-bill, not "EBITDA per tonne". Five-year series (FY2025-26 AR, Rs crore):

| | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Order book | 15,548 | 20,044 | 19,918 | 18,300 | **24,545** |
| Book / revenue | — | — | 2.58 | 1.98 | **2.44** |

Sizeable Adani-group inflows took the book to **Rs 31,306.8 crore as on June 30, 2026** (3.1x FY2026 OI; Rs 24,545 cr at FY2026 year-end). On the current (Jun-2026) composition the book is well diversified: **marine 23.2%**, urban infrastructure/MRTS 16.5%, data centres 13.3%, water/sewage 10.9%, buildings 8.8%, transportation 8.4%, industrial 8.1% — top five projects 32%, top three clients 26% (Jun-2026 basis attributed to ICRA's action). Marine remains the recognised niche though its share has fallen from the ~33-35% FY2025/Mar-2026 AR basis as data-centre and urban-infra work has scaled. Quarterly revenue reconciles to the audited year (Q4FY26 Rs 2,973.49 cr against FY2026 Rs 10,060.58 cr).

---

## 6. Normalisation (failure mode 36)

Other income note 25 decomposed (FY2026 / FY2025, Rs crore) and tied to its printed total of **176.96 / 76.90**:

| Component | FY2026 | FY2025 | Treatment |
|---|---|---|---|
| Interest on bank deposits | 34.76 | 31.12 | Stripped (ICRA excludes interest income) |
| Interest on other financial assets | 0.49 | 0.48 | Stripped |
| Interest on income-tax refund | 6.68 | 1.35 | Stripped; non-recurring |
| Interest on sales-tax refund | 0.51 | 5.21 | Stripped; non-recurring |
| Interest on settlement/award | 50.46 | 0.27 | Stripped; non-recurring, large in FY2026 |
| Interest — others | 1.17 | — | Stripped |
| Insurance claim | 2.17 | 0.13 | Stripped; non-operating |
| Net foreign-exchange gain | 55.72 | 1.86 | Stripped; non-operating (reconstructed residual — see below) |
| Profit on disposal of PPE (net) | 12.75 | 14.87 | Stripped; non-operating |
| Miscellaneous income | 12.25 | 21.61 | Stripped |
| **Total (ties to note 25)** | **176.96** | **76.90** | |

**OPBDIT convention (corrected against ICRA's action).** ICRA's OPBDITA retains core-related other income and excludes interest/dividend/rental. For an EPC contractor, income on the settlement of contract claims/awards is core-related, so this workpaper RETAINS the FY2026 "Interest on settlement/award" of **Rs 50.46 crore** (FY2025 Rs 0.27 cr — the very item ICRA cites: margin "aided by ... claim-related income") and strips the rest. ICRA-convention OPBDIT is **Rs 1,072.02 crore (10.66% margin, coverage 4.99x)** — reconciling to ICRA's published 10.7% and 5.0x. The prior version stripped ALL other income (10.15%, 4.75x), which understated profitability and contributed to the delivered rating being one notch low. The company's own "EBITDA Rs 1,199 crore" retains all other income (1,021.56 + 176.96); ICRA's convention sits between.

**Forex reconstruction (disclosed, failure mode 38/39).** The AR prints a net forex gain in note 25 sub-block (c), but the OCR split the line. The Rs 55.72 crore is the residual of the (c) subtotal after the separately-printed insurance, PPE-disposal and miscellaneous lines, so that the note sums to its printed total of Rs 176.96 crore. Probe [0d] flagged the cash-flow forex row (unrealised, Rs 31.22 crore) as distinct from the P&L note figure — the P&L note governs; the cash-flow row is not used. Forex is a GAIN in both years and no forex loss sits in operating costs, so the failure-mode-36 asymmetry does not arise; it is stripped either way, so the reconstruction affects no published ratio.

**No exceptional items** in any year (the FY2024 "profit before exceptional items" line carries a nil exceptional). Bad debts written off and provision write-backs are recurring working-capital items inside operating costs, not exceptionals.

---

## 7. Rated amount (Step 7b)

No same-issuer prior action is in the reference library (the library holds only EPC peers). The rated facility is therefore taken from the **issuer's own AR credit-rating note**: ICRA rates the **Long-term fund-based term loans / working capital, and long/short-term non-fund-based limits at [ICRA]A+ (Stable)**, upgraded 29-Jul-2025 from [ICRA]A. The exact rated LIMIT is not stated as a number in the AR (a rated limit lives in the CRA press release, which was not supplied) — it is marked **to be confirmed by issuer** in the Annexure, not reconstructed. **Drawn debt** used for the ratios is Rs 1,001.23 crore (total, ICRA definition); of which fund-based working-capital borrowings Rs 712.55 crore, term debt Rs 154.25 crore, supplier's credit Rs 96.32 crore, leases Rs 38.11 crore. The company also operates large **non-fund-based** (bank-guarantee) limits inherent to EPC — quantum not separately disclosed as a limit; the margin money of Rs 314.84 crore is held against them.

---

## 8. Materiality sweep (Step 8)

| Finding | Quantum | Decision |
|---|---|---|
| **Change of control** — RenewExim DMCC (Adani) acquired 67.46% from Italian-Thai Development (FY2025) | control | **INCLUDE — the key support and strategic-access factor** |
| **Rating upgrade to A+** by both ICRA and CARE during FY2026 | rating | **INCLUDE — the anchor** |
| **Order-book recovery** to Rs 24,545 cr on record Rs 14,821 cr inflows | book | **INCLUDE — revenue visibility driver** |
| **CARO 3(ii)(b)**: quarterly bank returns not agreeing with books; Mar-2026 returns not filed | process | **INCLUDE (R13)** — governance/process item; opinion unmodified |
| Supplier's-credit finance arrangement (bill discounting / M1 exchange) | Rs 96.32 cr | **INCLUDE — in total debt per the company's own definition** |
| Margin money earmarked against non-fund-based limits | Rs 314.84 cr | **INCLUDE — excluded from liquidity** |
| Large interest-on-settlement/award income in FY2026 | Rs 50.46 cr | **INCLUDE — stripped from OPBDIT as non-recurring** |
| Contract assets (unbilled revenue) | Rs 2,263 cr | **INCLUDE — working-capital intensity** |

---

## 9. Methodology Compliance Map (Step 10)

| Rating factor | Company evidence | Assessment |
|---|---|---|
| **Industry / order-book visibility** | Order book Rs 31,306.8 cr (Jun-30-2026), 3.1x FY2026 OI; up ~71% from Rs 18,300 cr; well diversified (marine 23.2%, urban infra/MRTS 16.5%, data centres 13.3%, water/sewage 10.9%) | **Strong** — medium-term visibility |
| **Scale & market position** | Revenue Rs 10,061 cr (5-yr CAGR ~30%); marine/maritime niche; over-four-decade franchise; Adani-group EPC arm (~65% of ~Rs 25,000 cr inflow over 15 months) | **Strong** for an EPC contractor; the binding qualitative strength |
| **Operating efficiency / margin** | OPBDIT/OI 9.86 → 9.32 → 10.66% (retains core claim income) | Adequate-to-strong; improving on leverage, mix and claim income |
| **Leverage** | Gearing 0.42x; TD/OPBDIT 0.93x; TOL/TNW 1.95x | **Strong** — near-net-cash on term debt |
| **Coverage** | Interest coverage 4.99x; DSCR 3.2x (ICRA basis) | **Strong** and improving |
| **Working-capital intensity** | NWC/OI 4.7% (0.8% FY2025); inventory days 103; debtor days 47; mobilisation advances ~Rs 1,015 cr; contract assets Rs 2,263 cr | Moderate — the sector's structural feature and the main constraint |
| **Liquidity** | Free cash ~Rs 380 cr + ~Rs 209 cr FB WC buffer (Jun-2026); NCA Rs 800-1,000 cr; repayments Rs 61.1/49.4 cr | **Adequate** (§11) |
| **Management & governance** | Unmodified audit opinion; Adani governance; CARO 3(ii)(b) process observation | Adequate |
| **Parent / support** | RenewExim DMCC (Adani) 67.46%; benefit via order inflows, BG terms, bank rates | **Not Applicable** as a support notch — captured in business risk (§10) |

---

## 10. Support assessment (methodology 963) — Parent/Group support: Not Applicable

RenewExim DMCC (Adani group) holds **67.46%**, acquired from Italian-Thai Development in May 2025. The Adani association is a material credit positive, but it operates through **business channels** — sizeable order inflows (~65% of ~Rs 25,000 cr booked over 15 months to Jun 2026), favourable bank-guarantee terms and bank charges, and access to the group's project pipeline — rather than an explicit guarantee or cash-support undertaking. **Parent/Group support is therefore treated as Not Applicable** (matching ICRA's published action), and the benefit is captured inside business risk and financial flexibility. Entering zero support notches at Step 12b keeps the anchor honestly standalone; the group-driven uplift is applied as a named Stage-2 business-strength overlay (§13), where it is visible. No downward drag applies: the parent is far stronger than the standalone, so failure mode 56 does not arise.

---

## 11. Liquidity (Step 11) — Adequate

**Sources (Jun-30-2026 basis, per ICRA's action):** free cash and bank balances of around **Rs 380 crore** plus a buffer of about **Rs 209 crore** in fund-based working-capital limits; net cash accruals of around **Rs 800-1,000 crore** per annum; FY2026 net cash from operations was Rs 499.78 crore (up from Rs 184.28 cr). **Claims:** modest scheduled debt-repayment obligations of Rs 61.1 crore (FY2027) and Rs 49.4 crore (FY2028); annual capex ~Rs 350-400 crore with no material debt-funding plans; the approved QIP of up to Rs 5,000 crore would further limit external-debt reliance. **Descriptor: Adequate** — the operations are working-capital-intensive and funded partly through mobilisation advances (~Rs 1,015 cr) and extended supplier credit whose continuation matters (Adequate not Strong); accruals cover scheduled repayments many times over and there is no debt cliff (Adequate not Stretched).

**Claims:** total debt of Rs 1,001.23 crore is overwhelmingly short-tenor working-capital lines against a self-liquidating contract book; only **Rs 177.69 crore is long-term debt** with scheduled repayment (current maturities Rs 61.69 crore); capex ~Rs 264 crore a year; dividend Rs 34.30 crore.

**Descriptor: Strong.** Unencumbered cash of Rs 634 crore covers the entire long-term debt (Rs 178 crore) 3.6 times and the FY2027 current maturities many times over; operating cash flow of Rs 500 crore covers term-debt service comfortably. Strong rather than Superior because the working-capital cycle is intensive (contract assets Rs 2,263 crore) and part of the cash is margin money against non-fund-based limits. What is EXCLUDED from liquidity, and why (failure mode 34): Rs 314.84 crore of margin money earmarked against bank guarantees — counting it would overstate free liquidity by ~50%.

---

## 12. Forward view (Step 12) — `forward_model.py`

A five-year projection (FY2027-FY2031) with the debt path derived from the working-capital funding gap. Base case — revenue converting the order book at low-teens tapering to 10%, margin edging to 11%, working capital ~13% of revenue:

| | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---|---|---|---|---|
| Revenue | 11,469 | 12,960 | 14,515 | 16,112 | 17,723 |
| OPBDIT | 1,181 | 1,361 | 1,553 | 1,740 | 1,950 |
| Total debt | 1,081 | 1,185 | 1,317 | 1,530 | 1,732 |
| Total debt/OPBDIT (x) | 0.89 | 0.83 | 0.80 | 0.81 | 0.81 |
| Interest coverage (x) | 5.15 | 5.53 | 5.63 | 6.00 | 6.11 |
| Gearing (x) | 0.36 | 0.32 | 0.29 | 0.28 | 0.26 |

Stress case — growth halved, margin giving back the FY2026 gain to 9%, working-capital cycle stretching 4 points (the classic EPC stress of a slow-paying government client ballooning contract assets): TD/OPBDIT peaks at **1.0x** and interest coverage stays **above 4.6x**. **The credit is resilient in both cases** — the near-net-cash start, the absence of a term-debt cliff and the order-book visibility are what make it so. The one variable that matters is the working-capital cycle; a sustained stretch is the named monitorable.

---

## 13. Step 12b anchor and rating view

`Rating_Scorecard_Cemindia Projects Limited.xlsx`, sector **Real Estate / Construction** (nearest of the 22 scorecard sectors to EPC), filled from the engine by `fill_scorecard.py`.

**Stage-1 anchor: AA-** (support notches 0). No hard-cap disapplication (accrual coverage 4.99x, positive net worth). Business-risk gate (failure mode 53): business risk (score 2) is a **strength**, not weaker than financial risk, so the gate does not bind and sets no ceiling.

**Assigned rating: [ICRA]AA (Stable)/[ICRA]A1+.** The committee applies a **+1 Stage-2 business-strength overlay** (Inputs!C61) to bridge AA- → AA, for a reason the financial composite cannot fully see: the demonstrated Adani-group operational synergies (order inflows, favourable BG terms and bank rates, access to the group pipeline) and the strong, well-diversified 3.1x order book materially strengthen the business and financial-flexibility profile. This is entered as a **business-strength** overlay, NOT a parent-support notch (Inputs!C42 = 0; §10) — matching ICRA's treatment of Parent/Group support as Not Applicable. The +1 anchor-to-assigned divergence is within the ±2 screening band and is computed on the scorecard's Stage 2 (Rating!C34 = 1), not typed into prose. LT/ST mapping (ICRA, §8): AA maps to [ICRA]A1+.

**Correction note.** The delivered exercise reached [ICRA]A+ — one notch low. Two errors combined: (a) OPBDIT stripped all other income (margin 10.15%/coverage 4.75x instead of the correct 10.66%/4.99x), and (b) a −1 committee overlay was applied to bridge AA- DOWN to the AR-disclosed Jul-2025 A+, not knowing ICRA had UPGRADED to AA on Sep 03, 2026. Both are corrected here; the assigned grade is now [ICRA]AA (Stable)/[ICRA]A1+.

**Rating view chain:** demonstrated Adani-group synergies and strong 3.1x diversified order book (business strength) → near-net-cash, effectively unlevered balance sheet with coverage 5.0x (financial strength) → working-capital-intensive cycle (NWC/OI 4.7%) and execution risk on an early-stage book (the constraint) → [ICRA]AA (Stable)/[ICRA]A1+.

**Outlook: Stable** — the order book, financial flexibility and demonstrated synergies support the level; a sustained working-capital stretch, margin deterioration or large debt-funded capex would pressure it.

---

## 14. Divergence against prior action (Step 14)

ICRA's published action of **September 03, 2026** was supplied and is the source of truth for this Step-14 comparison:
- **ICRA (Sep 03, 2026):** ratings **upgraded to [ICRA]AA (Stable)/[ICRA]A1+** from [ICRA]A+ (Stable)/[ICRA]A1, rated amount enhanced to Rs 12,067 crore. **This exercise (corrected) reaches [ICRA]AA (Stable)/[ICRA]A1+ — no divergence.**
- **Basis divergence (failure mode 42):** ICRA is on a "Consolidated + 2 JVs" basis (fully consolidating ITD ITD Cem JV and CEC-ITD Cem-TPL JV); this engine is on the company's own consolidated basis. OI 10,130.4 (ICRA) vs 10,060.58 (here) — 0.7%, immaterial; every headline ratio reconciles (see the KI basis note). The 2-JV figures are attributed, not rebuilt (JV standalones not in the document set).
- **Ratio reconciliation:** margin 10.7%/10.66%, coverage 5.0x/4.99x, TD/OPBDIT 0.9x/0.93x, TOL/TNW 1.9x/1.95x, debtor days 47/47.0 — all tie on the company-consolidated basis.
- **AR-disclosed prior rating** (issuer's own FY2025-26 AR): ICRA A+ (Stable), upgraded 29-Jul-2025 from A — the superseded grade; the delivered exercise anchored to it and missed the Sep-2026 upgrade (see §13 correction note).

---

## 15. Surveillance (R15)

Annual review. Event-driven triggers: (1) a sustained stretch in the working-capital cycle / contract assets or a build in government-client receivables; (2) a large debt-funded acquisition or capex step-up that lifts gearing above ~1x; (3) any change in the RenewExim/Adani shareholding or support stance; (4) a material slowdown in order inflows that erodes the book below ~1.5x revenue; (5) escalation of the CARO 3(ii)(b) bank-returns matter; (6) one-day-one-rupee default monitoring on rated term facilities (30-day for cash-credit/non-fund-based per the facility type).
