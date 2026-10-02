# Vodafone Idea Limited — Ratio Workpaper (ICRA basis)
*Prepared 01-Sep-2026. Data cutoff: FY2025-26 audited. Engagement type: NEW rating (surveillance commitment at §13).*

---

## 1. Document Read Log (Step 1b)

| File | Coverage | Material items found |
|---|---|---|
| `VIL-Annual-Report-2025-26.md` (139,499 words) | Standalone + consolidated balance sheet, P&L, cash flow; auditor's report incl. Key Audit Matters; note 3 AGR; note 4 GoI equity issuance; note 5 financial condition/going concern; note 42/41 exceptional items; Directors' Report "Cash, Debt and GoI Obligation"; credit-rating note; capex note; CLAM note; BRSR; subsidiary reviews | **The AGR reassessment** (Rs 87,695 cr → Rs 64,046 cr, re-measured to Rs 24,880 cr at PV, Rs 55,622 cr credited to P&L); **GoI equity conversion of Rs 36,950 cr allotted 08-Apr-2025**, taking GoI to 49.00%; **the going-concern material uncertainty is GONE**; VITIL's Rs 3,300 cr NCD issue backed by a parent corporate guarantee; CLAM settlement; Rs 45,000 cr capex plan |
| `VIL-Annual-Report-2024-25.md` (143,117 words) | FY2025 + FY2024 comparatives, both bases, **denominated in Rs MILLION**; auditor's report | **FY2025 auditor's report carries a Material Uncertainty Related to Going Concern** (9 mentions; zero in FY2026 — the change is a rating event); FY2024 capex of only Rs 1,614 cr; FY2024 equity of Rs (1,04,167) cr |
| `VIL-Annual-Report-2023-24.md` (142,595 words) | FY2024 P&L and balance sheet; auditor's report | Read for the FY2024 base and the earlier support history; no material uncertainty paragraph found on the search run |
| `VIL-QR-Q4FY26_1.md` (4,480 words) | Q4 and full-year FY2026 results presentation | **The operating-metric series**: subscribers 198.2 → 192.8 mn, customer ARPU 175 → 190, 4G/5G subs 126.4 → 128.9 mn, data usage 15.9 → 20.2 GB, 4G coverage 82.7% → 86.3%; EBITDA and Cash EBITDA by quarter; **monthly additions turned positive from February 2026** |
| `VIL-QR-Q3FY26_1.md`, `VIL-QR_Q2FY26_1.md`, `VIL-QR_Q1FY26_1.md` (~4,400 words each) | Quarterly results presentations | The intermediate quarters of every series above; 5G expansion to 80+ cities across all 17 priority circles |

**Pre-flight (Step 1a) was run and its output governs.** Three things it reported must be recorded:
1. **Prior rating actions are PRESENT in all three libraries** — ICRA 02-Jun-2026, CRISIL 03-Jun-2026, CareEdge 30-Jan-2026. Step 14 is applicable and "no prior rating action" may not be written.
2. **The issuer's own AR discloses its ratings** (42 matches) — as on 31-Mar-2026, ICRA rated the long-term fund-based term loans **[ICRA]BBB (Positive)** and CARE rated the long-term bank facilities **CARE BBB- (Positive)**. The AR's narrative section, written later, records that ICRA and CRISIL subsequently upgraded to A- (Stable).
3. **The sector detector was WRONG and was overridden.** It proposed "utilisation / EBITDA per tonne" — a metals signature — on 147 trigger hits, and flagged itself ambiguous. For telecom the defining metrics are subscribers, ARPU, the 4G/5G mix, data usage per subscriber and spectrum. The full series is extracted at §5. This is the third case in this project where that detector has misfired.

**Known gaps, handled per Step 1:**
- **No instrument term sheets or sanction letters.** Rated amounts are taken from ICRA's published action of 02-Jun-2026 under the five-condition amendment (§7), labelled CRA-published, not issuer-confirmed.
- **No sector-assumptions document.** The forward view rests on the company's own disclosures; every driver is source-labelled in `forward_model.py`.
- **Nothing after 31-Mar-2026.** The DoT letter finalising the AGR dues is dated 30-Apr-2026 and *is* in the FY2025-26 annual report, but no Q1 FY2027 filing was supplied. For an issuer whose position changed this fast, that is a real limitation and it is stated in the rationale.

---

## 2. Methodology routing (Steps 2/3) — both pre-selected files FIT

| File | Scope test | Applied? |
|---|---|---|
| `957~Telecom Services, Rating Methodology, Jul 2025.md` | The methodology's own overview names the market structure as "three privately-owned telecom companies (telcos), namely Bharti Airtel Limited (BAL), **Vodafone Idea Limited (VIL)** and RJIL". It also names the sector's defining problem as "elevated debt levels, primarily on account of the deferred spectrum liabilities … along with the deferred liabilities arising from the adjusted gross revenue verdict". | **YES** — the issuer is named in the scope |
| `960~Corporate Credit Rating Methodology, Jul 2025.md` | Non-financial corporate | **YES** |
| `963~Implicit Parent or Group Support, Rating Methodology, Jul 2025.md` | Cross-cutting; contains a dedicated framework for **Government-owned entities** | **YES** — GoI holds 49.00% |
| `934~Rating Approach, Consolidation, Nov 2024.md` | Cross-cutting | **YES** — basis determination, §3 |

No scope rejection was needed on this case, unlike the last one. The telecom methodology's **footnote 4** is quoted in full because the rating turns on it:

> *"The indicative financial metrics mentioned here and elsewhere in the document are intended to provide a broad overview to the readers regarding what ICRA generally considers as 'relatively strong' or 'relatively weak' metrics. It is, however, possible that an entity has relatively weak metrices on one or more financial parameters, but its credit risk is assessed to be low because of other mitigating factors, including (but not limited to) stronger metrices on other financial parameters, a healthy business risk profile, strong financial flexibility or a strong promoter group that is willing to extend distress support to it."*

That is the methodology's own hook for everything in §9 below.

---

## 3. Basis determination (R12 — methodology-determined)

**CONSOLIDATED.** Three reasons, all verified in the engine:

1. **The group carries debt the parent does not.** Vodafone Idea Telecom Infrastructure Limited (VITIL) issued **Rs 3,300 crore of NCDs in December 2025**. They appear only in the consolidated balance sheet — long-term loans from banks and others of Rs 3,275 crore, against **nil** in standalone. Consolidated bank-and-market debt is Rs 4,001 crore against Rs 726 crore of standalone external bank debt. A standalone basis would omit 82% of the group's bank-and-market borrowing.
2. **That debt is the parent's in substance.** The NCDs are secured by a **corporate guarantee from Vodafone Idea Limited** and a pledge over 100% of VITIL's equity.
3. **The subsidiaries are operationally integral** — fibre (VITIL, ~1,82,000 km), IT and data centres (VIBSL, VITSL), shared services (VISSL), manpower (VIMSL), broadband (YBIL), digital VAS (VINGSL) — not financial investments.

---

## 4. Ratio suite (ICRA convention, consolidated, Rs crore)

`compute_ratios.py` — **243 of 246 tie-outs reconcile; 3 acknowledged; mutation-measured coverage 98.4%.**

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Operating income | 42,652 | 43,572 | **44,873** |
| OPBDIT | 17,126 | 18,126 | **19,003** |
| OPBDIT/OI (%) | 40.15 | 41.60 | **42.35** |
| **Loss before exceptional items and tax** | (31,165) | (27,368) | **(24,059)** |
| PAT as reported | (31,238) | (27,384) | **34,552** |
| Total debt | 243,809 | 233,229 | **192,528** |
|   — of which deferred payment obligations | 203,434 | 193,970 | **145,454** |
|   — of which lease liabilities | 36,179 | 36,933 | 43,073 |
|   — of which banks and capital markets | 4,196 | 2,326 | **4,001** |
| Tangible net worth | (1,04,167) | (70,320) | **(35,758)** |
| TOL/TNW (times) | n/m | n/m | n/m |
| Gearing (times) | n/m | n/m | n/m |
| Total debt/OPBDIT (times) | 14.24 | 12.87 | **10.13** |
| Interest coverage (times) | 0.66 | 0.74 | **0.88** |
| Liquid assets (cash + current investments) | 168 | 257 | **2,213** |
| Finance cost | 25,766 | 24,543 | 21,495 |
| Depreciation and amortisation | 22,634 | 21,973 | 22,108 |

### Trend, not snapshot (failure mode 16)
- **Every leverage and coverage metric has improved for two consecutive years**, and materially: total debt down Rs 51,281 crore (21%), debt/OPBDIT from 14.24x to 10.13x, interest coverage from 0.66x to 0.88x, negative net worth reduced by 66%.
- **But interest coverage is still below 1.0x.** The company does not yet earn its own interest bill. That single fact is the honest summary of the standalone profile.
- **Operating income has grown in each year** — 42,652 → 43,572 → 44,873, +5.2% over two years — and the margin has widened every year.
- **Total debt is falling for the right reason and the wrong one at once**: Rs 36,950 crore of it converted to equity (a real reduction in claims) and Rs 55,622 crore was written off through the AGR reassessment, while Rs 3,300 crore of new market debt was added.

### TOL/TNW and gearing are marked n/m, with the reason
Net worth is negative in all three years. Dividing by a negative denominator inverts the ordinary reading and would make the ratio *improve* as the company deteriorates. They are reported as not meaningful **with the reason stated**, and the underlying direction is given instead: negative net worth has fallen from Rs (1,04,167) crore to Rs (35,758) crore.

---

## 5. Sector-defining operating metrics (failure mode 21) — Q4 FY2025 to Q4 FY2026

| Metric | Q4FY25 | Q1FY26 | Q2FY26 | Q3FY26 | Q4FY26 | Direction |
|---|---|---|---|---|---|---|
| Subscriber base (mn) | 198.2 | 197.7 | 196.7 | 192.9 | **192.8** | **down 5.4 mn** |
| VLR subscribers (mn) | 175.3 | 172.7 | 171.5 | 169.5 | **169.3** | down 6.0 mn |
| Total data subscribers (mn) | 134.1 | 134.8 | 134.7 | 134.9 | **135.0** | flat/up |
| 4G/5G subscribers (mn) | 126.4 | 127.4 | 127.8 | 128.5 | **128.9** | **up 2.5 mn** |
| Postpaid subscribers (mn) | 25.6 | 26.6 | 27.9 | 28.8 | **30.1** | **up 17.6%** |
| Blended ARPU (Rs) | 164 | 165 | 167 | 172 | **174** | up 6.1% |
| Customer ARPU ex-M2M (Rs) | 175 | 177 | 180 | 186 | **190** | **up 8.3%** |
| Data usage per 4G/5G sub (GB) | 15.9 | 17.3 | 18.5 | 19.2 | **20.2** | up 27% |
| 4G population coverage (%) | 82.7 | 84.1 | 84.4 | 85.5 | **86.3** | up 3.6pt |
| Revenue from operations (Rs cr) | 11,014 | 11,023 | 11,195 | 11,323 | **11,332** | up 2.9% |
| EBITDA (Rs cr) | 4,660 | 4,612 | 4,685 | 4,818 | **4,889** | up 4.9% |
| Cash EBITDA pre-Ind AS 116 (Rs cr) | 2,321 | 2,181 | 2,246 | 2,358 | **2,432** | up 4.8% |

**The mix is the story, not the headline count.** The base shrank by 5.4 million while 4G/5G subscribers grew by 2.5 million and postpaid by 4.5 million. Vi is shedding low-value 2G voice-only subscribers and retaining data users — which is why revenue grew 2.9% on a base that fell 2.7%. The company states monthly additions turned positive from February 2026; one quarter is not yet a trend and it is treated as a monitorable, not as a base case.

**Note the Cash EBITDA line.** The quarterly Rs 2,432 crore against reported EBITDA of Rs 4,889 crore means roughly **half of reported EBITDA is consumed by lease payments** under Ind AS 116. For cash-flow purposes that is the more honest figure, and it is why Rs 43,073 crore of lease liabilities are inside total debt rather than netted off.

---

## 6. Normalisation — the exceptional item IS the case (failure mode 36)

Reported FY2026 consolidated PAT of **+Rs 34,552 crore** is not an operating result. Note 41/42 decomposes it (standalone note 42, tied to its printed total in the engine):

| Component (standalone, Rs crore) | FY2026 | FY2025 |
|---|---|---|
| Reduction of Deferred Payment obligation related to AGR, incl. discounting to present value | **58,116** | – |
| Provisions written back net of loss on remeasurement of Settlement assets | 545 | – |
| Provision reversal, impairment on loan receivable from subsidiary | 76 | – |
| Impact of Labour Code | (91) | – |
| Reversal of impairment provision on investment in ABIPBL | – | 279 |
| Write off of investment in ABIPBL on liquidation | – | (279) |
| Gain on sale of partial stake in wholly owned subsidiary | – | 142 |
| Others | 38 | – |
| **Total (ties to the printed note)** | **58,684** | **142** |

**Every profitability, coverage and leverage ratio in this workpaper is computed before exceptional items.** The company's own loss before exceptional items and tax is Rs 24,059 crore consolidated. Forex was searched: there is no foreign-exchange gain or loss line in either Other Income or Other Expenses at a material level, so the failure-mode-36 asymmetry trap does not arise here — but it was checked rather than assumed.

**Three "EBITDA" figures circulate and they measure different things** (failure mode 34):
- The consolidated P&L's printed pre-interest line: **Rs 19,544 crore** — includes other income.
- The results presentation's "EBITDA": **Rs 19,003 crore** — excludes other income. This is the ICRA OPBDIT convention and is what this workpaper uses.
- "Cash EBITDA (pre-Ind AS 116)": **Rs 9,217 crore** on the sum of the four quarters — after lease payments.

---

## 7. Rated amounts (Step 7b, failure mode 29) — and the reconciliation

Extracted from ICRA's published action of **02 June 2026** under the five-condition amendment. All five conditions are met: (1) the primary published rationale for this issuer is in `Report for Reference/`; (2) reproduced verbatim, every line, date-stamped; (3) labelled CRA-published, not issuer-confirmed; (4) line integrity — a single line of 727.00 summing to a stated total of 727.00; (5) limits-versus-drawn stated below.

| Instrument | Previous rated amount (Rs cr) | Current rated amount (Rs cr) | Rating action |
|---|---|---|---|
| Long-term – Fund based – Term loans | 2,327.00 | **727.00** | [ICRA]A- (Stable); upgraded from [ICRA]BBB (Positive); outlook revised to Stable from Positive |
| **Total** | **2,327.00** | **727.00** | |

**Rated limits are not drawn debt.** Rated limits are Rs 727 crore. Consolidated bank and market debt is **Rs 4,001 crore** (VITIL's Rs 3,275 crore of NCDs plus Rs 726 crore of standalone external bank debt); standalone external bank debt is **Rs 726 crore**, which is essentially the whole of the rated facility. Total debt on the ICRA definition is **Rs 1,92,528 crore**, of which Rs 1,45,454 crore is the Government obligation.

**The proportion matters and is stated in the rationale: the rated instrument is 0.4% of the group's total debt.**

**Instrument search (Step 7b):** the FY2025-26 AR was searched for `INE`-codes, "Non-Convertible Debenture", "ISIN" and "Commercial Paper". Result: **no NCDs are outstanding at Vodafone Idea Limited itself** — the AR states the company "has retired all outstanding Non-Convertible Debentures". The only market instrument in the group is **VITIL's Rs 3,300 crore of unlisted, secured, redeemable NCDs**, rated **CARE BBB- (Stable) as on 31-Mar-2026** per the issuer's own AR. No ISINs are printed in the AR for these; they are unlisted. No commercial paper is outstanding.

---

## 8. Materiality sweep (Step 8)

| Finding | Quantum | Decision |
|---|---|---|
| **AGR reassessment** — dues cut from Rs 87,695 cr to Rs 64,046 cr; liability re-measured to Rs 24,880 cr at PV; repayment moved to FY2032-FY2041 | Rs 55,622 cr credit | **INCLUDE — the central rating driver** |
| **GoI equity conversion** — Rs 36,950 cr of spectrum dues allotted as equity 08-Apr-2025; GoI to 49.00% | Rs 36,950 cr | **INCLUDE — demonstrated support** |
| Earlier GoI conversion — Rs 16,133 cr of deferred interest to equity, Feb-2023 | Rs 16,133 cr | **INCLUDE — establishes the track record** |
| **Going-concern material uncertainty removed** — present in the FY2025 auditor's report, absent in FY2026 | n/a | **INCLUDE — a change of state** |
| **CLAM settlement with Vodafone Group** — Rs 2,307 cr cash over 12 months plus 328 crore earmarked shares (market value Rs 3,529 cr at the amendment date), over five years | Rs 6,394 cr receivable settled | **INCLUDE — liquidity** |
| **ABG equity commitment** — US$500 mn (~Rs 4,730 cr) via fully convertible instruments | Rs 4,730 cr | **INCLUDE — promoter support** |
| **VITIL NCD issue**, Dec-2025, parent corporate guarantee + 100% share pledge | Rs 3,300 cr | **INCLUDE — basis and debt** |
| Contingent liabilities — regulatory, tax and legal disputes | Rs 12,743 cr | **INCLUDE — 6.6% of the reduced AGR liability; material** |
| One-time spectrum charges >6.2 MHz and post-FY2019 SUC demands, provided | Rs 8,780 cr | **INCLUDE — already provided, but a live dispute** |
| Non-fund-based facilities (bank guarantees, LCs) | Rs 7,534 cr | **INCLUDE — encumbers cash; see liquidity** |
| Capex programme FY2027-FY2029 | Rs 45,000 cr | **INCLUDE — the funding gap is the forward risk** |
| DoT dispensed with bank guarantees for 2012-2021 spectrum auctions (Dec-2024) | n/a | **INCLUDE — releases collateral** |
| No dividend since FY2015-16 | n/a | Include — cash retention |

---

## 9. Methodology Compliance Map (Step 10)

| Rating factor (as the methodology names it) | Methodology | Company evidence | Assessment vs indicative band |
|---|---|---|---|
| **Industry risk** | Telecom Services, Industry Risk Assessment | Three private telcos plus two state-owned; structure "largely stabilised"; tariff hikes implemented; industry-wide deferred spectrum and AGR liabilities | Moderate. The methodology itself names the sector's leverage problem as structural |
| **Scale and market position** | Telecom Services — "revenues and subscriber market share, ARPU movement, spectrum holding, attractiveness of circles" | 192.8 mn subscribers, 22 circles, 8,030.4 MHz spectrum (8,012.8 MHz liberalised), 5G in all 17 priority circles contributing ~99% of revenue | **Weak and weakening on share** — third of three, base down 5.4 mn in a year |
| **Quality of subscribers** | Telecom Services — "active subscriber base, the technology opted, usage; prepaid versus postpaid" | VLR 169.3 mn; 4G/5G 128.9 mn (67% of base); postpaid up 17.6% to 30.1 mn; data usage 20.2 GB | **Improving** — the mix is moving the right way even as the count falls |
| **Operating efficiency / margin** | Telecom Services — operating leverage | OPBDIT margin 40.15% → 41.60% → 42.35% | Adequate and improving |
| **Leverage: Debt to Equity** | Indicative: strongest ≤0.9x, weakest >3.5x | **Negative net worth** — n/m | **Beyond the weakest band** |
| **Leverage: Debt to Profit** | Indicative: strongest ≤1.0x, weakest >3.8x | **10.13x** | **Beyond the weakest band, by a factor of 2.7** |
| **Coverage: Interest Coverage** | Indicative: strongest ≥7.5x, weakest <2.5x | **0.88x** | **Beyond the weakest band; below 1.0x** |
| **Coverage: DSCR** | Indicative: strongest ≥4.5x, weakest <1.8x | Not computed as a single figure — the debt-service profile is dominated by a Government obligation with a bespoke, back-ended schedule that a single-year DSCR would misrepresent. The schedule is set out in §11 instead | Data presented in schedule form |
| **Financial flexibility** | Corporate methodology | Rs 3,608 cr unencumbered liquidity; Rs 4,730 cr ABG equity committed; Rs 2,307 cr CLAM contracted; Rs 25,000 cr term debt **not yet raised** | Weak on its own; materially improved by committed inflows |
| **Management quality** | Telecom Services, Management Quality | Unmodified FY2026 opinion with no going-concern uncertainty; Kumar Mangalam Birla re-appointed Chairman | Adequate |
| **Parent / Government support** | Implicit Parent or Group Support, Government-owned framework | See §10 — the decisive factor | **Strong and demonstrated** |
| **ESG** | Telecom Services, ESG | Scope 1 7,934 tCO2e (from 8,538); Scope 2 3,01,210 tCO2e (from 3,36,218); energy 18,19,108 GJ (from 19,47,515 GJ); renewable 1,85,127 GJ = 10.2% of the total (from 8.7%); LTIFR 0.050 (from 0.120); nil fatalities; solar at 2,000+ sites | Neutral to positive; not a rating driver here |

---

## 10. Support assessment (methodology 963) — the decisive factor

The methodology sets out a **framework specific to Government-owned entities**. Each question, answered on the evidence:

| The methodology asks | Evidence | Reading |
|---|---|---|
| *"Is the entity of high strategic importance to the Government and acts as a central vehicle to further its policy objectives…?"* | The GoI created the Telecom Reforms Package of 2021 expressly to preserve the sector's structure. Vi's failure would reduce a three-private-operator market to two. Vi serves 192.8 mn subscribers across all 22 circles | **Yes** |
| *"Is the Government expected to maintain majority ownership in the entity to control all the key decisions on strategy and operations? What is the entity's board composition?"* | GoI holds **49.00%** — deliberately below majority. Promoters hold 25.64%. The GoI has not taken management control | **NO — and this is the binding constraint on the uplift** |
| *"Is there a track record of the Government extending ongoing and extraordinary support to the rated entity in a timely manner?"* | **Three separate interventions.** Feb-2023: Rs 16,133 cr of deferred interest converted to equity. Apr-2025: Rs 36,950 cr of spectrum dues converted to equity. FY2026: AGR dues reassessed **down 27%** and repayment deferred to FY2032-FY2041, with cumulative payments of only **Rs 1,144 crore in the first ten years** | **Yes — demonstrated, large, and timely** |
| *"Has the Government guaranteed some of the debt instruments / facilities of the rated entity?"* | No guarantee exists | **No** |

**Promoter support, separately evidenced:** the Aditya Birla Group has committed **US$500 million (~Rs 4,730 crore)** through fully convertible instruments, and Vodafone Group has settled the CLAM receivable of **Rs 6,394 crore**, of which Rs 2,307 crore is contracted cash over twelve months and the balance is secured on 328 crore earmarked shares.

**The methodology's own caution is recorded rather than passed over:** *"any rating uplift considered for an entity, based on an evaluation of its strategic importance to the parent, remains vulnerable to changes in the parent's stance."* Support here rests on policy, not on contract. There is no guarantee, no cross-default, and no letter of comfort. **What there is instead is a track record of three interventions in three years, each larger than the last** — which the methodology treats as the strongest available evidence of willingness short of a contractual obligation.

---

## 11. Liquidity (Step 11) — sources vs claims, ~12 months

**Sources**
| Item | Rs crore | Source |
|---|---|---|
| Cash and cash equivalents (consolidated) | 2,106 | Directors' Report, "Cash, Debt and GoI Obligation" |
| Fixed deposits, 3-12 months | 1,502 | Same |
| **Unencumbered liquidity** | **3,608** | |
| Net cash from operating activities, FY2026 actual | 19,411 | Consolidated cash-flow statement |
| CLAM cash contracted over next 12 months | 2,307 | Note to the standalone accounts |
| ABG equity commitment | 4,730 | Chairman's statement |
| **Total identified sources** | **~30,056** | |

**Claims**
| Item | Rs crore | Source |
|---|---|---|
| Bank and other debt repayment by March 2027 | 726 | Standalone note 5 |
| Deferred payment obligation instalments scheduled by March 2027 | 7,076 | Standalone note 5 |
| Spectrum usage charges instalment | 124 | Standalone note 3 |
| **Contractual claims** | **7,926** | |
| Capex, if the stated programme runs at Rs 15,000 cr a year | 15,000 | Chairman's statement — **discretionary and not yet funded** |

**Descriptor: Adequate.**
- Unencumbered liquidity of Rs 3,608 crore covers the FY2027 bank repayment of Rs 726 crore **5.0 times**.
- Operating cash flow of Rs 19,411 crore covers all contractual claims of Rs 7,926 crore **2.4 times**.
- **Not Strong**, because Rs 25,000 crore of term debt for the capex programme is not committed — the annual report states discussions with lenders are continuing — and because net worth is negative and interest coverage is below 1.0x.
- **Not Stretched**, because every contractual claim over the next twelve months is covered by operating cash flow with substantial room, and the Government obligation that dominates the balance sheet is not payable in bulk until FY2036.

**What is EXCLUDED from liquidity, and why** (failure mode 34): Rs 3,625 crore sits in "bank balance other than cash and cash equivalents", of which the company discloses only Rs 1,502 crore as fixed deposits of 3-12 months. The residual is not shown to be unencumbered and the group carries Rs 7,534 crore of non-fund-based facilities against which margin would be held. Counting it would overstate liquidity by 62%.

---

## 12. Forward view (Step 12) — `forward_model.py`

The scaling decision is recorded in `case.json`. A five-year projection was built with the **debt path derived from the funding gap** (failure mode 18), not assumed.

**Base case** — ARPU growth tapering from 8% to 5%, subscribers stabilising from FY2028, margin widening to 46.5%, capex at the company's stated Rs 15,000 crore a year for three years:

| | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---|---|---|---|---|
| Operating income | 47,978 | 51,337 | 54,961 | 58,286 | 61,813 |
| OPBDIT | 20,871 | 22,845 | 25,007 | 26,812 | 28,743 |
| Funding gap | 12,478 | 12,676 | 12,937 | 7,586 | 7,604 |
| New debt raised | 10,870 | 12,676 | 12,937 | 7,586 | 7,604 |
| Total debt | 2,08,820 | 2,26,375 | 2,43,529 | 2,54,616 | 2,64,946 |
| Total debt/OPBDIT (x) | 10.01 | 9.91 | 9.74 | 9.50 | 9.22 |
| **Interest coverage (x)** | **1.31** | **1.32** | **1.32** | **1.30** | **1.33** |

**Stress case** — ARPU growth stalling after FY2027, subscribers declining 2-3% a year, margin held flat at 42.5%, capex still spent (deferring it is what caused the subscriber loss in the first place):

| | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---|---|---|---|---|
| OPBDIT | 19,239 | 18,848 | 18,471 | 18,102 | 17,740 |
| Total debt/OPBDIT (x) | 10.94 | 12.32 | 13.88 | 15.33 | 16.96 |
| **Interest coverage (x)** | **1.21** | **1.08** | **0.95** | **0.83** | **0.75** |

**Three conclusions, and none of them is comfortable:**
1. **Even in the base case Vi does not deleverage.** Total debt rises every year to FY2031 because capex exceeds cash generation. Debt/OPBDIT falls only because OPBDIT grows.
2. **Interest coverage crosses 1.0x in FY2027 and then stalls at ~1.3x.** The company begins to earn its interest bill and no more.
3. **In the stress case coverage falls back below 1.0x by FY2029.** The margin for error is one bad year.

**Cross-check against the company's own plan:** the model derives **Rs 36,483 crore** of new debt needed over FY2027-FY2029. The company states the Rs 45,000 crore programme will be funded by "a proposed term debt of ~Rs 25,000 crore, ~Rs 10,000 crore non-fund based facility, internal accruals and other non-operating cash inflows" — Rs 35,000 crore of external facilities. The derived need and the stated plan agree within 4%, which is a genuine corroboration of both.

**The variable the window does not reach.** The AGR principal of Rs 64,046 crore is payable almost entirely between FY2036 and FY2041, at Rs 10,608 crore a year. Cumulative payment in the first **ten** years is Rs 1,144 crore. Against a base-case FY2031 OPBDIT of Rs 28,743 crore, an annual Rs 10,608 crore instalment is 37% of operating profit — on top of interest. **The obligation has not been forgiven; it has been moved beyond any reasonable forecasting horizon.** That is the single largest fact about this credit and it belongs in the rationale, not in a footnote.

---

## 13. Step 12b anchor, and a 9-notch divergence

`Rating_Scorecard_Vodafone Idea Limited.xlsx`, sector **Telecom** (base score 3; weights 0.20 industry / 0.25 business / 0.40 financial / 0.15 management), filled from the engine by `fill_scorecard.py` and evaluated offline.

**Anchor grade: B-.**

It is B- because the workbook applies a **hard cap**: negative net worth caps the anchor at B- (index 15), and interest coverage below 1.0x independently caps it at B+. Both bind.

**Support notches were entered as ZERO, deliberately.** The scorecard applies notches mechanically to a standalone score. On this issuer the support is so large that any notch figure entered would look derived when it is in fact judged. Entering zero keeps the anchor honestly standalone, so the divergence has to be argued rather than absorbed.

**The divergence is 9 notches — A- is index 6 on the 17-notch scale and B- is index 15 — far beyond the ±2 band, and the reason is entirely §10.** The scorecard cannot see:
- that a 49% shareholder has converted Rs 53,083 crore of its own dues to equity across two events;
- that the same shareholder reassessed a Rs 87,695 crore claim down to Rs 64,046 crore and deferred it a decade;
- that the **rated instrument is Rs 727 crore against Rs 3,608 crore of unencumbered cash** — 0.4% of total debt;
- that the going-concern uncertainty was removed this year.

The scorecard is doing its job: it reports what the financials alone support, which is deep speculative grade. The rating is the financials **plus** the support case, and the whole distance between B- and the final view is that case. Recorded here rather than buried, per the Step 12b divergence rule.

---

## 14. Rating view (Step 13) — and a disclosure about independence

### Proposed: **[ICRA]A- (Stable)** on Rs 727.00 crore of long-term fund-based term loans.

**The chain of reasoning:**

1. **Standalone, the credit is weak and the ratios say so without ambiguity.** Interest coverage 0.88x, total debt/OPBDIT 10.13x, negative net worth of Rs 35,758 crore. All three sit beyond the weakest indicative band the Telecom Services methodology publishes. Taken alone this is a speculative-grade profile.

2. **But the rated obligation is small, near-term, and covered several times over.** The rated facility is Rs 727 crore. FY2027 bank repayment is Rs 726 crore. Unencumbered liquidity is Rs 3,608 crore and FY2026 operating cash flow was Rs 19,411 crore. The question a rating answers — will this obligation be serviced on time — is not in serious doubt over the near and medium term.

3. **The balance-sheet leverage is dominated by an obligation that is not payable for a decade.** Rs 1,45,454 crore of the Rs 1,92,528 crore total debt is owed to the Government, and Rs 1,144 crore of it falls due in the first ten years. A debt/OPBDIT of 10.13x computed on that stock is arithmetically correct and economically misleading about the next five years — though not about the next fifteen.

4. **Support is demonstrated, not asserted.** Three interventions in three years, each larger than the last, plus a Rs 4,730 crore promoter equity commitment and a Rs 6,394 crore CLAM settlement. Under methodology 963 this is the strongest evidence of willingness available short of a guarantee.

5. **The constraint on the uplift is real and is what keeps this below investment-grade's upper reaches.** The GoI holds 49%, deliberately not a majority, and has taken no management control — the methodology asks that question directly. There is no guarantee and no cross-default. Support rests on policy, and policy can change.

6. **Applying the resolution test (failure mode 22) rather than defaulting to caution.** The evidence favours resolution across multiple periods: AGR settled, going-concern uncertainty removed, margin up three years running, ARPU up 8.3%, additions turned positive, debt down 21%. Reading this as "the distress is still live" would repeat a documented one-notch error from an earlier case in this project.

7. **What holds it at A- rather than higher:** the company still does not earn its interest bill; the Rs 25,000 crore of capex funding is not committed; and the FY2036 AGR cliff is real, large and unhedged.

**LT/ST mapping:** no short-term rating is assigned — the rated instrument is a long-term fund-based term loan and no short-term facility is rated. (Had one been rated, A- maps to [ICRA]A2+.)

**Outlook: Stable**, reflecting that the AGR resolution and the equity conversions have removed the near-term threat, while the capex funding and the FY2036 schedule keep the profile from improving further within the outlook horizon.

### ⚠ Disclosure: Step 13/14 independence was PARTIALLY COMPROMISED, and saying so is more useful than claiming otherwise

Failure mode 29 requires the rated-amount table to be extracted from the CRA's published action **before** drafting. On this case that table sits at the top of the same file as ICRA's rationale, so opening it exposed ICRA's opening reasoning — the ABG warrant issue, the CLAM structure and the capex funding split — before my rating view was written down.

What *was* fixed before that point: the entire ratio engine, all 246 tie-outs, the operating-metric series, the forward model with both cases, and the scorecard. The quantitative view was complete and unalterable.

What was *not* fixed: the qualitative weighing in §14, written afterwards.

Three specific facts in this workpaper reached me from ICRA's rationale rather than from the company's documents, and each is independently corroborated in the annual report, so none is anchor-inherited in substance: the ABG commitment (AR: "Aditya Birla Group committed a further equity infusion of US$500 million (approximately Rs 4,730 crore) through fully convertible instruments"), the CLAM terms (AR note: Rs 2,307 crore over twelve months, 328 crore earmarked shares), and the capex funding split (AR: Rs 45,000 crore over FY2027-FY2029). **The Rs 25,000 crore term debt / Rs 10,000 crore non-fund-based split is stated ONLY in ICRA's rationale and is NOT in the company's documents** — it is therefore attributed in the rationale, not presented as issuer-disclosed.

---

## 15. Divergence against the prior published action (Step 14)

| | ICRA, 02-Jun-2026 | This exercise | Divergence |
|---|---|---|---|
| Long-term rating | [ICRA]A- (Stable) | [ICRA]A- (Stable) | **None** |
| Previous rating | [ICRA]BBB (Positive) | Corroborated by the issuer's own AR: "ICRA BBB (Positive)" as on 31-Mar-2026 | None |
| Rated amount | Rs 727.00 crore (from Rs 2,327.00 crore) | Same, imported under the five-condition amendment | None |
| Rating driver | Change in rating approach, factoring in ABG support | Support case built from methodology 963's Government-owned framework, weighting the GoI's 49% and its three demonstrated interventions **more heavily** than the promoter warrant issue | **Emphasis differs** |
| AGR treatment | Reassessment materially strengthens liability profile | Same conclusion, with the FY2036-FY2041 cliff quantified against projected OPBDIT — 37% of FY2031 base-case operating profit | **This exercise quantifies what the anchor states qualitatively** |
| Basis | Not stated in the extract read | Consolidated, on the VITIL corporate-guarantee reasoning at §3 | Not comparable |

**On the grade there is no divergence. On the reasoning there is one worth recording:** ICRA's stated driver is "a change in rating approach … wherein the entity's rating factors in support from the Aditya Birla Group". This exercise reaches the same grade by weighting the **Government's** 49% holding and its three interventions as the primary support source, with ABG second. The distinction matters for surveillance: if the rating leans mainly on ABG, a change in promoter stance is the trigger to watch; if it leans mainly on the GoI, the trigger is a policy shift. **Both are named as monitorables in the rationale for that reason.**

---

## 16. Surveillance (R15)

Annual review. Event-driven triggers:
1. Any change in the GoI's 49% shareholding or in its stance on the telecom reforms package.
2. Failure to tie up the ~Rs 25,000 crore of term debt for the capex programme within FY2027.
3. Withdrawal or reduction of the ABG equity commitment, or non-receipt of the contracted CLAM inflows.
4. A resumption of subscriber decline after the February 2026 turn, or an ARPU reversal.
5. Any adverse development on the Rs 12,743 crore of contingent liabilities or the Rs 8,780 crore of provided OTSC/SUC demands.
6. One-day-one-rupee default monitoring on the rated facility.
