# JSW Steel Limited — Ratio Workpaper (Jul 2026)

Basis: **Consolidated** (ICRA rates JSL on consolidated basis; Corporate + Iron & Steel methodologies). Rs crore.
Source: JSW Integrated Annual Reports FY2023-24 (FY24+FY23) and FY2025-26 (FY26+FY25); Q1–Q4 FY2026 results; 6 broker notes (forward assumptions only). Computed in `Companies/jsw-steel/compute_ratios.py`.

## 0. Document Read Log (Step 1b — every file read one by one before drafting)

| # | File | What it is | Key facts / material items extracted |
|---|---|---|---|
| 1 | Integrated-Annual-Report-FY-2025-26 | FY26 audited AR (read section-by-section, all credit-material parts) | **Financials:** consol BS + P&L (rev 185,470; OPBDITA 29,821; PAT 25,508). **Exceptional:** Rs 18,051 cr gain (BPSL slump-sale, Note 48; also a KAM). **Instruments:** 6 NCD ISINs + coupons + amounts + maturities (Corp Gov + Note 17/20), NCDs Rs 6,750 cr, **no CP outstanding**. **Rating note:** ICRA/CARE/India Ratings all AA. **Segment note:** 5 segments. **Leverage:** caps 3.75x ND/EBITDA & 1.75x ND/Equity; net debt 53,870 / 1.81x; net debt movement chart. **KAMs (auditor):** BPSL JV gain; **recoverability of ~Rs 10,700 cr goodwill/PPE/CWIP/advances on loss-making/on-hold projects (Note 49)**; related-party disclosure; **taxation/litigation (Note 46)**. **Contingent liabilities (Note 46): Rs 5,008 cr tax/legal + Rs 6,140 cr forest-development-tax = ~Rs 11,148 cr.** **Group:** 46 subs / 19 JVs / 5 associates; financial guarantees for overseas subs (JSW Netherlands, Periama, Acero Junction) + loan-loss allowances on overseas exposures. **MD&A/risk:** capex roadmap, coking-coal/iron-ore integration targets, safeguard duty, forex risk. Auditor S R B C & Co LLP — unmodified opinion. |
| 2 | Integrated-Annual-Report-FY-2024-25 | FY25 AR | (comparatives cross-checked; FY25 trough margin 13.6%) |
| 3 | Integrated-Annual-Report-FY-2023-24 | FY24 AR | Consol BS + P&L FY24/FY23 for 3-yr trend |
| 4 | Q1 FY26 results PPT | Company deck | Q1 rev 43,147; EBITDA 7,576; **BPSL review petition filed 25-Jun-2025 (SC)**; util 87% (maint. shutdown) |
| 5 | Q2 FY26 results PPT | Company deck | **SC on 26-Sep-2025 UPHELD JSW's BPSL resolution plan** (dismissed appeals); CRGO expansion; Illawarra stake→30% |
| 6 | Q3 FY26 results PPT | Company deck | JFE JV for BPSL announced (deleveraging ~Rs 37,000 cr); Utkal Odisha 5mtpa Ph-1 announced; net debt/EBITDA 2.91x |
| 7 | Q4 FY26 results PPT | Company deck | FY26 rev 185,470; EBITDA 29,821; **normalised net profit excl exceptionals Rs 8,698 cr (Q4 3,475)**; net debt 1.81x/0.51x; div Rs 7.1; BPSL transferred to JSSL 27-Mar-26 for Rs 29,475 cr, deconsolidated; POSCO 6mtpa JV (Apr-26); MdR Mozambique done; BMM Ispat approved |
| 8 | Nuvama (REDUCE) | Broker note | Bear case: aggressive expansion; capex Rs 1.26 lakh cr FY27-31; net debt/EBITDA trajectory; conf-call takeaways; capacity roadmap to 78 mtpa |
| 9 | Motilal Oswal (BUY +18%) | Broker note | JFE JV terms: Rs 320bn cash, ~Rs 350bn deleveraging; BPSL FY25 rev 214bn/EBITDA 22bn; JFE Rs 157.5bn for 50% |
| 10 | Anand Rathi (BUY +16%) | Broker note | JV deal mechanics (EV Rs 530bn); ~Rs 30bn annual finance-cost saving; Piombino merger → promoter 46.74% |
| 11 | ICICI Direct (HOLD) | Broker note | Capex roadmap to ~55.5 mtpa by FY31; Utkal Rs 31,600 cr; captive coking coal 25% by FY31; net debt Rs 80,347 cr Q3 |
| 12 | Centrum (NEUTRAL) | Broker note | Q4 detail; normalised PAT ~Rs 35.2bn Q4; leverage discipline noted despite capex |
| 13 | SMIFS/JSW_Steel-May15 (BUY, TP 1,500) | Broker note | POSCO JV (Apr-26); Rs 18,051 cr exceptional confirmed; safeguard duty 12%; capex Rs 22,000-24,000 cr FY27 |
| 14 | Prior ICRA report (12-Dec-2025) | **Anchor — opened ONLY at Step 14** | [ICRA]AA on Rating Watch Positive / A1+; JFE JV material event; expected net debt/OPBDITA 2.1-2.2x; rated structure Rs 94,660 cr |

**Correction the log surfaced:** company's own normalised FY26 net profit is **Rs 8,698 cr** (Q4 PPT), not the ~Rs 5,000 cr from the Nuvama note — report corrected. **Timeline clarified:** SC UPHELD JSW's BPSL plan (26-Sep-2025); the JFE JV is a strategic value-unlock, not a distress response.

## 1. Computed ratio suite (consolidated)

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Operating income | 175,006 | 168,824 | 185,470 |
| OPBDITA | 28,236 | 22,904 | 29,821 |
| OPBDITA margin | 16.1% | 13.6% | 16.1% |
| Total debt (excl acceptances) | 87,984 | 98,752 | 99,310 |
| Total debt (incl acceptances) | 105,638 | 119,286 | 119,127 |
| Total debt/OPBDITA (excl accept) | 3.1x | 4.3x | 3.3x |
| Net debt/OPBDITA (excl accept) | 2.7x | 3.5x | 1.9x |
| Net debt/OPBDITA (incl accept) | 3.3x | 4.4x | 2.6x |
| Interest coverage (OPBDITA/int) | 3.5x | 2.7x | 3.3x |
| TOL/TNW | 1.86x | 1.95x | 1.56x |
| RoCE (op PBIT/CE) | – | 8.0% | 10.5% |
| PAT to owners (reported) | 8,973 | 3,504 | 22,316 |

**Acceptances** (buyer's credit: Rs 19,817 cr FY26) — ICRA typically treats as debt for steel; shown both ways. Company-reported net debt Rs 53,900 cr (Mar-26) vs my Rs 57,803 cr (excl accept) — diff is treatment of non-current financial assets; both give net debt/OPBDITA ~1.8–1.9x.

## 2. Methodology Compliance Map (Iron & Steel, Jun 2025 — indicative bands)

| Factor | Band (strongest / weakest) | JSL FY2026 | Assessment |
|---|---|---|---|
| Scale & market position | rev >Rs 4,000 cr / production >1 mt | Rev 185,470 cr; ~30.1 mt; India's largest | **Strongest** |
| RoCE | ≥25% / <10% | 10.5% | Just above weakest — modest (cyclical + capital-heavy) |
| TOL/TNW | ≤0.9x / >3.0x | 1.56x | Mid-range (adequate), improving |
| Total debt/OPBDITA | ≤0.5x / >5.0x | 3.3x (4.0x incl accept) | Weaker half — leverage the key constraint |
| Interest coverage | ≥18x / <2x | 3.3x | Weak-modest |
| DSCR | ≥4x / <1.1x | n/a (not computed — no repayment schedule provided) | data-unavailable |
| Backward integration | captive mines ≥50% / external | ~33% iron ore captive; coking coal mostly imported | Moderate |
| Product/geographic diversity | flats+longs+downstream, >25% exports | flats+longs+VAP; ~10% exports | Comfortable (product), domestic-tilted |

**Interplay:** dominant scale + improving leverage offset modest coverage/RoCE. Net leverage improvement (3.5x→1.9x) via BPSL–JFE monetisation is the swing positive. Maps to **AA** category.

## 3. Materiality sweep (all documents, incl. broker notes — per ITC lesson)

| Item | Decision | Reason |
|---|---|---|
| **Rs 18,051 cr exceptional GAIN (FY26)** = gain on BPSL steel slump-sale into 50:50 JSW–JFE JV (deconsolidated end-FY26). NON-CASH. | **Include — central event** | Inflates headline PAT to Rs 22,316 cr (owners); normalised ~Rs 5,000 cr. Excluded from operating/normalised assessment. Traced to AR Note 48 + all 6 broker notes + anchor. |
| **BPSL–JFE JV: ~Rs 37,000 cr deleveraging**; JFE equity Rs 15,750 cr (Rs 7,875 cr tranche 1 recd Mar-26); net debt 80,300→53,900 cr; net debt/OPBDITA 2.9x→1.81x | **Include** | The reason ICRA placed LT rating on Positive watch (Dec-25); now completed → watch resolved. |
| **~Rs 1.26 lakh cr approved capex FY27–31** (India 31.9→48.8 mtpa by FY30, ~78 mtpa incl JVs by FY32; Odisha greenfield, Vijayanagar/Dolvi brownfield, BMM Ispat, POSCO JV) | **Include — key constraint** | Largely debt-funded; principal negative sensitivity. |
| Management leverage cap cut 3.5x→3.0x net debt/OPBDITA | **Include** | Financial-discipline positive. |
| Safeguard duty 12% (Dec-25), 11.5% FY27, 11% FY28 | **Include** | Supports domestic realisations near-term. |
| Coking coal import dependence; captive target ~50% only by FY31; forex loss Rs 1,080 cr Q4 | **Include** | Cost/cyclicality/forex risk. |
| Promoter pledge (~11.8% of promoter holding) | **Note** | Financial-flexibility watch-item. |
| POSCO 6 mtpa greenfield JV (Apr-26, Odisha) | **Include** | Further expansion/capex commitment. |
| **Contingent liabilities ~Rs 11,148 cr** (Rs 5,008 cr tax/legal disputes + Rs 6,140 cr forest-development-tax/fee) — auditor KAM, Note 46 | **Include** | Manageable vs scale/net worth but a monitorable; now in report "Any other information" + challenges. |
| **Impairment/recoverability KAM (Note 49): ~Rs 10,700 cr** goodwill/PPE/CWIP/advances on loss-making or on-hold projects | **Include** | Asset-quality monitorable; added to challenges. |
| **Related-party transactions + complex group** (46 subs/19 JVs/5 associates); corporate guarantees for overseas subs (JSW Netherlands, Periama, Acero Junction); loan-loss allowances on overseas exposures | **Include** | Governance/consolidation monitorable; added to challenges + Any other information. Surfaced only by the full section-by-section read (KAMs, RPT note, related-party balances). |

## 4. Independent rating view (formed BEFORE opening anchor)

**[ICRA]AA (Stable)/[ICRA]A1+.** Anchored on dominant scale + materially improved leverage (net debt/OPBDITA 1.9x) + financial discipline; constrained by aggressive debt-funded capex, cyclicality, coking-coal import dependence, modest coverage/RoCE. LT→ST: AA → A1+ (invariable mapping). ✓

## 5. Step-14 divergence vs anchor (ICRA, 12 Dec 2025)

| Item | Anchor | My view / resolution |
|---|---|---|
| Rating | [ICRA]AA **on Rating Watch, Positive** / [ICRA]A1+ (watch triggered by JV *announcement*, pending completion; ICRA expected net debt/OPBDITA 2.1–2.2x FY27-28) | **Matches at AA.** Transaction now COMPLETE; net leverage 1.81–1.9x (better than expected) → **watch resolved to Stable**. Judgment call: completed deleveraging is positive but ~Rs 1.26 lakh cr capex + cyclicality temper a full **AA+** upgrade. ICRA's Positive watch signals they may lean AA+ — flagged to user. |
| Basis | Consolidated; proportionate JV (JKSL) share prospectively; Corporate + Iron & Steel methodologies | Adopted identically. |
| Rated amounts | Total Rs 94,660 cr (term loans, ST fund/non-fund, NCD Rs 7,875 cr, CP Rs 5,000 cr, etc.) | **Anchor-sourced → require confirmation** (no term sheets). Used as the rated structure, attributed. |
| Deleveraging quantum | ~Rs 37,000 cr; net debt/OPBDITA 3.4x (FY25) → 2.1–2.2x expected | Confirmed from company/broker data (achieved 1.81x, ahead of expectation). |

**Conclusion:** No material divergence in credit quality (AA). Key independent judgment = resolving the Positive watch to **Stable** (not AA+), on capex/cyclicality grounds.

## 6. Caveats
- **Instrument details CORRECTED (post-review, v2 — full ICRA-format Annexure I):** NCD ISINs/coupons/amounts/security/redemption from the AR (Corp Gov + Notes 17, 20/20B); issuance dates from ICRA's public Dec-2025 record. 6 listed NCDs, **Rs 6,750 cr outstanding**: 8.79% Rs 2,000 (Oct-19 → Oct-29, amortising), 8.90% Rs 1,000 (Jan-20 → Jan-30, amortising), 8.39% Rs 500 (Mar-24 → May-27), 8.35% Rs 1,750 (Aug-24 → Aug-29), 8.43% Rs 500 (Aug-24 → Aug-31, verified: bullet 29-Aug-2031, call 25-Mar-2031, Dolvi Ph-II security), 8.76% Rs 1,000 (placed post Dec-25 → May-31). **FY26 NCD movement reconciled exactly:** Dec-25 placed 6,625 − 875 repaid (8.25% INE019A08033, "Repaid in FY 25-26") + 1,000 placed (8.76% INE019A07449) = 6,750 ✓ Note 17; unplaced headroom 7,875 − 6,750 = 1,125. AR confirms **no CP outstanding** at Mar-26 (programme undrawn). Annexure I now in standard ICRA columns (ISIN | name | issuance | coupon | maturity | amount | rating) covering ALL rated instruments incl. bank facilities (those amounts from ICRA record, attributed). First draft wrongly wrote "not available"; second draft had a non-standard table — both superseded.
- Leverage caps per AR: 3.75x ND/EBITDA, 1.75x ND/Equity (FY26 actuals 1.81x, 0.51x); broker-reported 3.0x is management's tightening guidance. Company net debt Rs 53,870 cr (ex-leases) reconciles to my Rs 57,803 cr (incl Rs 3,778 cr leases).
- All three CRAs rate JSL AA (ICRA on Positive watch, CARE Stable, India Ratings on Positive watch) per AR rating note — corroborates AA.
- DSCR, Annexure II entity list, standalone split not computed (repayment schedule / detailed subsidiary financials not extracted).
- Forward assumptions (capex, volumes, net-debt trajectory) sourced from company guidance + 6 broker notes, attributed; not ICRA projections.
- Data cut-off 31 Mar 2026 (audited).


## 9. Step 12b — Scorecard anchor & Step 12 forecast model (CRISIL run, 13-Jul-2026)

**Files:** `Companies/jsw-steel/JSW_Steel_Financial_Model_2026-07-13.xlsx` (7 tabs; FY27E-31E base: revenue 178,051->249,028; EBITDA 29,378->43,580 at 16.5%->17.5%; ND/EBITDA 1.92x->1.59x; stress FY28E coverage 2.75x / ND 2.5x) and `Companies/jsw-steel/Rating_Scorecard_JSW Steel.xlsx` (CRISIL / Iron & Steel).

**Anchor grade: Crisil A-/Stable / Crisil A2+** (financial-risk 2.97; industry 4.0 sector base; business 2; management 3; composite 2.99 after Strong-liquidity adj).

**Qualitative-score reasoning:** business 2 — India's largest steelmaker (~30 mt sold FY26), dominant scale, value-added mix, distribution (CRISIL market-position factors), tempered by commodity price-taking; management 3 — delivered deleveraging (net 1.81x FY26) and tightened leverage cap 3.0x, but Rs1.26-lakh-cr capex programme (> existing ops in CRISIL risk-appetite terms) and ~11.8% promoter pledge; liquidity Strong not Superior — Rs41,507 cr cash vs large capex claims.

**Divergence: anchor A- vs rating view AA = 4 notches — explained:** (1) generic Ref_Bands under-credit a commodity major: coverage 3.3x scores 4/6 and TD/EBITDA 3.3x scores 3/6 against mid-corporate benchmarks, where the Iron & Steel methodology reads them against scale/integration/cyclical position; (2) industry base 4.0 (sector median) drags 25% of the composite - JSL is the sector's #1, which a linear anchor cannot see; (3) GCA uses normalised PAT 8,698, blind to the completed Rs26,400-cr Q4 deleveraging and JFE tranche-2. Corroboration: ICRA, CARE and India Ratings all rate JSL at AA (AR ratings note). The anchor is retained as the uncalibrated screening floor; the judgment view stands. This divergence is logged as calibration-backtest evidence (bands need steel-sector calibration).
