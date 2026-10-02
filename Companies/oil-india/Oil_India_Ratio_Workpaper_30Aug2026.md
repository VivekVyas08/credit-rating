# Oil India Limited — Ratio Workpaper (CRISIL basis)
*Prepared 30-Aug-2026. Data cutoff: FY2025-26 audited (13-May-2026); Q1 FY2026-27 unaudited results (30-Jun-2026) reviewed for material events. Engagement type: NEW rating.*

## 1. Document Read Log
See the Step 1b gate presented in chat (30-Aug-2026) — reproduced in summary here.

| File | Coverage |
|---|---|
| IntegratedAnnualReport2025-26.md | Standalone + consolidated financial statements, Other Expenses note, KAM/EoM, contingent liabilities, borrowings notes 22/25/31, Form AOC-1, segment note, promoter holding, reserves/production, ESG, credit-rating note |
| AnnualReport202324_3.md | FY24/FY23 standalone + consolidated comparatives, exceptional-item footnote (note 57.13/60.9) |
| OIL_India_Annual_Report_2024_25_0.md | Cross-check on credit-rating note and 5-year exceptional-item summary |
| Q1 FY2026-27 results (30-Jun-2026) | Standalone + consolidated segment tables (clean); P&L tables materially garbled by source conversion — **not used for headline P&L figures**, only for the segment-level PBT trend and the material-events check |
| Q2/Q3 FY26, Q4/FY26 results | Referenced for corroboration only |

**Known gaps handled per Step 1:** no instrument term sheets/sanction letters uploaded — instrument detail extracted from the AR itself (Step 7b) instead; no sector-assumptions document uploaded — projections base case rests on management's own guidance quoted in the AR/MD&A, stated as such throughout.

## 2. Extraction and computation
`Companies/oil-india/compute_ratios.py` — 265/265 tie-outs reconcile; **mutation-measured coverage 100.0%** (`python tieout_mutation.py oil-india`), i.e. every extracted input would be noticed by at least one check if it were wrong. No subtotal is typed by hand; every debt/liquidity aggregate is derived from its balance-sheet components and tied to a row the AR prints in its own right.

### Ratio suite (CRISIL convention — Section IV of `criteria-for-manufacturing-trading-and-corporate-services-sector.md`)

**Consolidated** (Rs crore unless stated)

| Metric | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| Revenue from operations | 41,025.98 | 36,303.62 | 36,163.75 | 37,049.55 |
| PBDIT (incl. recurring other income) | 15,987.42 | 13,847.04 | 12,882.57 | 12,376.66 |
| PBDIT margin % | 38.97 | 38.14 | 35.62 | 33.41 |
| PAT (total, incl. NCI) | 9,854.39 | 6,980.45 | 7,039.63 | 7,550.67 |
| Total debt | 18,831.75 | 24,040.50 | 30,645.24 | 37,477.98 |
| Net debt | 14,932.25 | 17,144.75 | 22,804.17 | 31,432.57 |
| Adjusted net worth (owners) | 38,481.49 | 48,338.99 | 49,767.72 | 57,998.36 |
| Gearing (x) | 0.49 | 0.50 | 0.62 | **0.65** |
| Interest coverage (x) | 17.75 | 14.37 | 12.05 | **10.28** |
| RoCE % | 24.50 | 16.19 | 13.14 | **10.12** |
| Current ratio (x) | 1.69 | 1.17 | 1.23 | 1.09 |
| Debtor days | 21.4 | 33.5 | 33.1 | 44.6 |
| NCATD % | 62.67 | 37.89 | 30.54 | 27.38 |

**Standalone**

| Metric | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| Revenue from operations | 23,259.61 | 22,129.79 | 22,117.22 | 21,345.94 |
| PBDIT | 11,176.09 | 11,643.30 | 10,635.95 | 8,752.74 |
| PBDIT margin % | 48.05 | 52.61 | 48.09 | 41.00 |
| PAT | 6,810.40 | 5,551.85 | 6,114.19 | 4,455.34 |
| Total debt | 11,437.36 | 11,710.14 | 12,885.95 | 14,746.95 |
| Gearing (x) | 0.33 | 0.27 | 0.28 | 0.30 |
| Interest coverage (x) | 15.43 | 15.32 | 12.28 | 9.06 |

### Trend, not snapshot (per Step 1b sub-gate)
- **Gearing is rising every year on a consolidated basis** — 0.49x → 0.65x over four years — driven entirely by the NRL refinery-expansion financing (see §4). Standalone gearing is essentially flat (0.33x → 0.30x): the leverage build is concentrated in the subsidiary, not the parent.
- **Consolidated PBDIT margin has compressed every year** — 38.97% → 33.41% — while revenue is roughly flat (₹41,026 cr → ₹37,050 cr, down from a FY23 peak). This is a genuine multi-year direction, not a one-year dip, and is the first driver a reader should see.
- **Interest coverage has nearly halved** — 17.75x → 10.28x — reflecting both the margin compression and the growing debt load; still comfortably above any distress threshold in absolute terms.
- **RoCE has fallen from 24.5% to 10.1%**, consistent with a large capital base (CWIP) not yet generating revenue — the NRL expansion is capital deployed ahead of the associated cash flow.
- **Reserve Replacement Ratio improved: 0.94 (FY25) → 1.02 (FY26)** — reversed the prior year's sub-unity reading. This is the sector-defining metric and its direction (not just the FY26 snapshot) belongs in the drivers.

## 3. Qualitative fact register (traced, with source; corroborated per Step 1b sub-gate)
- **Promoter (Government of India) holding: 56.66%**, unchanged FY25→FY26 (President of India, 921,564,990 shares) — IAR p. shareholding table; corroborated in three separate locations in the same document (credit-rating note, MD&A, promoter shareholding note).
- **Outstanding ratings, per the company's own AR**: CRISIL AAA (Stable) / CRISIL A1+; CARE AAA (Stable)/A1+; Moody's Baa3 (Stable); Fitch BBB- (Stable) — the AR itself states the Moody's/Fitch ratings are "at par with India's sovereign rating." Confirmed present in the reference library (CRISIL *Oil India Limited_29 Oct 2025*) — Step 14 divergence table below.
- **Subsidiaries/JVs (16 entities, all named per Form AOC-1, failure mode 17):**
  - Subsidiaries: Numaligarh Refinery Limited (69.63%, the "material subsidiary" per the AR's own MD&A), OIL Green Energy Limited (100%), Oil India International B.V. (100%), Oil India International Pte. Ltd. (100%), Oil India Sweden AB (100%).
  - Associates/JVs: Beas Rovuma Energy Mozambique Ltd. (40%), Indradhanush Gas Grid Limited (20%), Brahmaputra Cracker and Polymer Limited (10%), Duliajan Numaligarh Pipeline Limited (23%), Assam Petro-Chemicals Limited (48.80%), HPOIL Gas Private Limited (50%), North East Gas Distribution Company Limited (49%), Purba Bharati Gas Private Limited (26%), Assam Valley Fertilizer and Chemical Company Limited (20.24%), APGCL OIL Green Power Limited (49%), Suntera Nigeria 205 Ltd (25%).
- **Contingent liabilities (standalone, FY26): ₹4,150.44 cr** claims not acknowledged as debt (largest single item: ₹2,484.81 cr under the Assam Taxation on Specified Lands Amendment Act, partly bank-guaranteed) **+ ₹4,028.06 cr guarantees** (largely regulatory/operational — MWP commitments, OALP, DSF blocks — not third-party credit support). Combined ~17% of standalone net worth; assessed as manageable given the guarantee book's operational (not financial) nature.
- **ESG:** Net Zero by 2040 target; GHG emissions 1.190 million tCO2e FY26, down 17.93% vs the FY24 baseline; gas flaring down 32% (82→56 MMSCM); +45% captive solar consumption; methane-abatement technology (AUSEA) deployed across 24 installations; S&P Global ESG score more than doubled (22→46).
- **Capex/investment programme:** consolidated CWIP nearly tripled since FY23 (₹11,953 cr → ₹37,644 cr), driven by the Numaligarh Refinery expansion (target 9 MMTPA) plus midstream pipeline builds (crude 18+ MMTPA, gas 6 MMSCMD, product 5.5+ MMTPA targeted capacity).

## 4. The central credit story — Numaligarh Refinery expansion, project-style financing
Subsidiary NRL's SBI-led consortium term loan has been enhanced twice within the review period: ₹18,904 cr (Dec-2021) → revised to ₹15,504 cr after ₹3,400 cr of Oil Industry Development Board (OIDB) funding (May-2025) → **enhanced to ₹21,678 cr with a ₹4,113 cr standby facility** (Sep-2025), following a change in project scope. Repayment is **44 quarterly instalments starting only 30-Sep-2029** — i.e. a multi-year construction moratorium. A further ₹5,482 cr NaBFID facility carries the same structure.

This is the single largest driver of the consolidated leverage build documented in §2, and it is entirely absent from the standalone (parent-only) statements. **Execution risk on this project — cost overrun, schedule slippage, or a further scope-driven enhancement — is the primary monitorable for this rating**, not a generic capex-guidance line.

## 5. Normalisation decisions (failure mode 36 — written, not silent)
- **Forex**: taken from the P&L Other Expenses note ("Exchange Loss-Net," ₹899.18 cr FY26 / ₹198.66 cr FY25), never from the cash-flow reconciliation row (₹914.78 cr FY26 / ₹198.16 cr FY25), which is the unrealised bridge figure only (failure mode 38 guard).
- **FY24 exceptional item (₹2,362.72 cr standalone / ₹2,365.56 cr consolidated)**: the cumulative FY2016–FY2023 catch-up of a disputed GST-on-royalty provision, booked as a one-off under Ind AS materiality grounds — genuinely non-recurring, correctly excluded from FY24 normalised PBT. The *ongoing annual* increment of the *same* dispute (₹865.12 cr FY26, ₹809.32 cr FY25) sits inside Other Expenses every year as a normal recurring cost and is **not** normalised out — royalty/cess-linked provisioning is a structural, recurring feature of E&P economics under the Oilfields (Regulation & Development) Act.
- **Other income / dividend & interest income (₹1,863.15 cr standalone, FY26)**: **retained** in PBDIT under CRISIL's convention (recurring non-operating income is included, unlike ICRA's unconditional strip). This income is genuinely recurring — investment income on a large, growing equity-method book (₹25,014 cr FY26) of JVs and associates, not a one-off gain. Explicitly *not* the ICRA treatment (failure mode 32/33 guard).
- **Capital-structure break**: equity share capital rose ₹1,084.41 cr (FY24) → ₹1,626.61 cr (FY25/26), a bonus issue. EPS is not reported as a comparable trend across that break.

## 6. Liquidity (Step 11 — sources vs. claims, ~12 months, standalone)
- **Sources**: cash + bank balances + current investments ₹3,693 cr (FY26) + operating cash flow (FY26: ₹7,576 cr net from operations) + undrawn facility headroom (NRL's enhanced consortium facility carries a ₹4,113 cr standby not yet drawn as at the AR date).
- **Claims**: current maturities of long-term debt (~₹474 cr standalone FY26, embedded in current borrowings), working-capital facilities largely undrawn, capex commitments (₹461.24 cr standalone capital commitments; the NRL expansion capex is funded through its own project facility, not through OIL's standalone liquidity).
- **Descriptor: Strong** (standalone) — the parent carries negligible near-term refinancing risk, low gearing (0.30x), and its FY26 operating cash flow alone covers current maturities several times over. This descriptor applies to the standalone entity; the subsidiary's project financing is assessed separately as construction-phase risk, not a liquidity item for the parent.

## 7. Methodology Compliance Map (Step 10)

| Rating factor (Section XII / IV) | Company evidence | Assessment |
|---|---|---|
| Price sensitivity of E&P performance | Revenue driven by crude/gas realisations; Q1 FY27 segment PBT more than tripled y-o-y on a Hormuz-disruption-linked price spike (see §8) | High sensitivity — as the methodology names as the primary E&P risk factor |
| Reserve replacement | RRR 1.02 (FY26) vs 0.94 (FY25), above unity | Positive, improving |
| Diversity of fields / oil-gas mix | Crude 3.450 MMT + gas 3.186 BCM FY26; multiple basins (Assam, Rajasthan, offshore Andaman/KG/Kerala-Konkan) | Diversified within India; concentrated domestically |
| Operator's credentials | Record drilling (74 wells), terminal rate 10,566 MTPD (highest in 14 years) | Strong operational track record |
| Capital structure (E&P-specific weight) | Consolidated gearing rising (0.49x→0.65x), standalone flat (0.33x→0.30x) | Divergent by basis — driver is subsidiary capex, not parent balance sheet |
| Government linkage | GoI 56.66%; Maharatna CPSE status; policy role in energy security; existing standalone rating already AAA | Category assessment pending completion of standalone view — see §9 |

## 8. Q1 FY2026-27 — treated as a data point and a volatility flag, not a structural driver
Segment data (the only reliably parseable part of this quarter's release) shows standalone PBT of ₹3,741.72 cr against ₹1,097.55 cr in the same quarter last year — crude-oil segment PBT alone rose from ₹969.85 cr to ₹2,998.64 cr. Consolidated PBT similarly rose to ₹5,322.17 cr from ₹2,505.08 cr. The AR's own MD&A links the window to a Strait of Hormuz flow disruption pushing global oil supply/prices; IEA/EIA/OPEC forecasts cited in the same document diverge materially on 2026 demand and converge only for 2027. This is genuine operating strength but externally and geopolitically driven — recorded as a positive recent data point and a sensitivity, not folded into an "improving margin trend" claim that the FY23-FY26 audited series does not support.

## 9. Divergence against the prior CRISIL rating action (Step 14 — opened only after the above view was formed)
CRISIL's own prior action (*Oil India Limited_29 Oct 2025*, reference library) rates the issuer **CRISIL AAA/Stable — A1+**, consistent with the company's own AR disclosure. The standalone financial risk profile computed here (gearing 0.30x, interest coverage 9.06x, strong liquidity) and the government-linkage support (56.66% GoI, Maharatna status, sovereign-equivalent Moody's/Fitch ratings per the company's own AR) are both consistent with a AAA outcome. The consolidated leverage build (0.65x, driven by NRL's project financing) is the one factor that could argue for caution, but project debt at a 70%-owned subsidiary with government-linked funding (OIDB, NaBFID) and non-recourse structural features would need to be assessed against CRISIL's consolidation criteria before it could reasonably move the standalone-equivalent view — no divergence from the anchor at this stage.

## 10. Rated-amount table (five-condition amendment applies — CareEdge published rationale IS in the reference library, not CRISIL's)
No CRISIL rated-amount table for Oil India Limited itself was found in `CRISIL/Report for Reference/`. The CareEdge library holds *Oil India Limited_30 Sep 2025* with a rated-amount table (LT bank facilities ₹7,816.09 cr; LT/ST ₹3,859.00 cr; ST ₹2,059.45 cr) — this is a **different agency's action** and is NOT imported into a CRISIL report under any condition of the five-condition amendment (which only ever permits importing a rated table from the SAME agency being rated). **Rated amounts for the CRISIL mandate are therefore "to be confirmed by issuer."**

## 10a. Step 12b — quantitative anchor and its divergence (binding: any AA+/AAA divergence must be explained)
`Rating_Scorecard_Oil_India.xlsx` filled from the audited actuals above (sector: "Oil & Gas / Refining", the closest of the workbook's 22 sectors). **The workbook's formulas were not recalculated by a spreadsheet engine in this environment** (no Excel/LibreOffice available); the chain was replicated by hand in Python against the exact formulas visible in the Scorecard/Rating/Projections sheets and is recorded, with every intermediate figure, on the `Anchor_Computation_Manual` sheet of that file — this should be re-verified by opening the workbook in Excel (it recalculates on open) before any Committee reliance.

**Anchor grade: CRISIL AA+ (Stable) / A1+ — one notch below the company's actual outstanding rating (CRISIL AAA/Stable / A1+, per the company's own AR and the reference-library anchor).**

This is exactly the divergence CLAUDE.md's governance overlay requires be explained (any divergence at AA+/AAA, not just >2 notches): the financial-risk sub-score (2.33/6, roughly mid-scale) is driven almost entirely by the **consolidated** gearing (0.65x) and debt/EBITDA (3.03x) picking up the NRL project financing — the same driver identified as the central credit story in §4. The scorecard has no way to see that this debt sits at a 69.63%-owned subsidiary, is government-linked (OIDB, NaBFID co-funding), carries a multi-year construction moratorium, and is structurally distinct from parent-level leverage. A conservative +1 government-support notch was applied (see the qualitative-score justification in the scorecard); a fuller notch consistent with CRISIL's own Category II/III government-linkage framework (§7) would close some but not all of the one-notch gap.

**This is not treated as a reason to override the anchor mechanically in either direction.** The Step 13 rating view (below) is formed on the standalone financial strength, the government linkage, and the international-agency corroboration — not on the scorecard number — and the anchor's one-notch-low reading is recorded as evidence of the calibration's own documented limitation (`Scorecard_Backtest_Report_18Jul2026.md`: the anchor "under-rates AA+/AAA... unless the support notch and Ref_Qualitative rubric are applied") rather than as a case for downgrading the analytical view to match it.

## 11. Step 12 scaling decision
Recorded in `case.json`: given (a) the entity is an existing, unqualified AAA-rated issuer with no history of financial distress, (b) the single dominant forward-looking driver is one identifiable, well-disclosed project (NRL expansion) rather than a diffuse multi-variable forecast, and (c) time/document constraints (no sector-assumptions note, no term sheets), a **focused sensitivity model on the 2–3 rating-driving variables** (crude realisation, NRL capex drawdown pace and debt build, RRR/production trajectory) is used in place of the full 5-year 3-statement equity-research-plugin workflow. See `Oil_India_Sensitivity_Model_30Aug2026.md` for the model and its assumptions, each source-labelled.

## 12. Unverified inputs / disclosed differences (carried from the engine)
See `UNVERIFIED_INPUTS` and `DISCLOSED_DIFFERENCES` in `compute_ratios.py` — reproduced: the new FY26 ₹2,498.37 cr NCD (consolidated) has no ISIN/coupon/maturity disclosed anywhere in the document set (Annexure I marks it TBC); consolidated forex-in-opex for FY24/FY23 is carried as the printed subtotal only, not individually decomposed (the FY24 exceptional-item note already isolates the one material non-operating item that year).
