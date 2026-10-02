# Apollo Tyres Limited — Ratio Workpaper (CRISIL basis)
*Prepared 30-Aug-2026. Data cutoff: FY2025-26 audited (14-May-2026); Q1 FY2026-27 unaudited results (30-Jun-2026) reviewed for material events. Engagement type: NEW rating.*

## 1. Document Read Log
| File | Coverage |
|---|---|
| AGM_Notice_and_Annual_Report_FY2026.md (176k words) | Standalone + consolidated statements, exceptional-item note B31/B30, KAM (Enschede impairment + goodwill impairment testing), contingent liabilities note 22, borrowings note 7 (NCD/term loan detail), Form AOC-1 (33 subsidiaries), promoter shareholding, credit-rating note, segment note |
| AGM_Notice_and_Annual_Report_FY2025.md (147k words) | FY25/FY24 standalone + consolidated comparatives (used for the FY2024 column throughout) |
| AGM_Notice_and_Annual_Report_FY2024.md | Referenced for cross-check only; FY24 figures used are the FY25 AR's own comparative column, not retyped from this file, per the newest-first rule |
| Q1/Q2/Q3 FY26, Q4/FY26, Q1 FY27 quarterly results | Q1 FY27 (30-Jun-2026) segment tables reviewed for the material-events bring-down check; the full P&L tables in that file are **not used** — see note below |

**Known gaps handled per Step 1:** no instrument term sheets/sanction letters — instrument detail extracted from the AR (Step 7b); no sector-assumptions document — projections base case rests on management's own capex/guidance statements in the AR, labelled as such.

**Extraction-quality note:** the Q1 FY2026-27 standalone P&L table in `Unaudited_Financial_Results_-_June_30_2026.md` converted with badly scrambled column alignment (multiple total-income figures appearing under ambiguous headers). Rather than risk a right-number-wrong-column error, only the **segment-wise revenue and results table** in the same file was used — it is internally consistent (segment totals tie to the P&L's own Revenue and PBT lines) and corroborates cleanly against the audited FY26 full-year figures.

## 2. Extraction and computation
`Companies/apollo-tyres-limited/compute_ratios.py` — 189/190 tie-outs reconcile; **mutation-measured coverage 100.0%**. The one non-reconciling check is a documented, explained divergence (§5), not an extraction error. All figures are stated in the AR as Rs **million**; converted once, in code, to Rs crore (÷10).

### Ratio suite (CRISIL convention)

**Consolidated** (Rs crore)

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Revenue from operations | 25,377.72 | 26,123.42 | 28,470.60 |
| PBDIT (incl. recurring other income) | 4,601.28 | 3,660.30 | 4,277.23 |
| PBDIT margin % | 18.13 | 14.01 | 15.02 |
| PAT | 1,721.87 | 1,121.32 | 1,372.42 |
| Total debt | 4,905.10 | 4,410.43 | 3,675.23 |
| Net debt | 3,489.52 | 3,512.93 | 2,631.20 |
| Adjusted net worth | 13,902.18 | 14,765.70 | 16,715.17 |
| Gearing (x) | 0.35 | 0.30 | **0.22** |
| Interest coverage (x) | 9.09 | 8.20 | **10.93** |
| RoCE % | 16.61 | 11.27 | 13.41 |
| Current ratio (x) | 1.28 | 1.33 | 1.32 |
| Debtor days | 38.3 | 42.8 | 40.9 |
| Net debt/EBITDA (x) | 0.76 | 0.96 | 0.62 |

**Standalone**

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Revenue from operations | 17,539.33 | 18,173.61 | 19,816.23 |
| PBDIT | 3,232.41 | 2,306.25 | 3,188.66 |
| PBDIT margin % | 18.43 | 12.69 | 16.09 |
| PAT | 1,154.03 | 629.43 | 1,851.77 |
| Gearing (x) | 0.35 | 0.32 | 0.23 |
| Interest coverage (x) | 8.01 | 6.31 | 9.70 |

### Trend, not snapshot
- **FY2025 was a genuine trough year, and FY2026 a sharp recovery** — this is the shape of the whole story, not a single-year print. Consolidated PBDIT margin fell 18.13% (FY24) → 14.01% (FY25) before recovering to 15.02% (FY26); standalone shows the same V-shape more sharply (18.43% → 12.69% → 16.09%). Both bases delevered through the period despite the FY25 dip — gearing fell every single year (consolidated 0.35x → 0.30x → 0.22x).
- **Interest coverage compressed then rebuilt**: 9.09x → 8.20x → 10.93x (consolidated) — the FY25 dip was real, not an artefact, and the FY26 recovery is broad-based (both bases, both revenue and margin contributing).
- **Net debt/EBITDA improved every year**: 0.76x → 0.96x → 0.62x — the FY25 uptick and FY26 recovery below the FY24 starting level is a genuinely improving multi-year direction.

## 3. The FY2026 exceptional item — decomposed and normalised (failure mode 36)
Consolidated exceptional items of **Rs 1,033.51 crore** (FY2026, up from Rs 168.67 crore in FY2025) are dominated by a single item: **Rs 1,000.12 crore provision for impairment of PPE/CWIP/intangibles at Apollo Tyres (NL) B.V. (ATNL)**, following the Board's decision to **discontinue tyre manufacturing at ATNL's Enschede (Netherlands) plant**. This is a genuine Key Audit Matter in the FY2026 auditor's report — not a routine provision — and the audit opinion carries no qualification. Full decomposition (note B31):

| Component | Rs crore |
|---|---|
| Voluntary retirement scheme (VRS) | 7.46 |
| Provision for impairment (ATNL, Enschede closure) | 1,000.12 |
| Labour code impact | 25.93 |
| **Total (ties to printed note B31 total)** | **1,033.51** |

Standalone exceptional items are small throughout (Rs 33–76 crore) — **the Enschede closure and its impairment sit entirely at the consolidated/subsidiary level**, which is why standalone PBT nearly doubled (Rs 961.03 crore → Rs 1,884.11 crore, FY25→FY26) while consolidated PAT actually *fell* (Rs 1,121.32 crore → Rs 1,372.42 crore is a rise, but well below the underlying operating improvement, because the one-off absorbed a large share of the consolidated operating gain).

**Normalisation decision:** the impairment is excluded from PBDIT/PBT throughout this workpaper (it sits below the PBDIT line by construction, in `pbt_bef_exc` vs `exceptional`). It is treated as a genuine one-off restructuring event — a European manufacturing-footprint rationalisation — and is elevated to a Key Rating Driver (§7) rather than buried as a normalisation footnote, because plant-closure decisions of this kind speak to ongoing European segment strategy, not just one year's earnings.

## 4. Normalisation decisions, remaining items (failure mode 36)
- **Other income / dividend & interest income**: retained in PBDIT under CRISIL's convention (recurring non-operating income is included). No large one-off gain sits inside other income in any year of the review period.
- **Government grants** (Rs 3,197.02 million FY26 / Rs 3,086.30 million FY25, flagged by pre-flight as an aggregate-note contaminant): these are **capital-expenditure-linked incentive grants** (state investment-promotion schemes), amortised into the P&L over the life of the related assets — a recurring, structural feature of Apollo's Indian manufacturing footprint, not a one-off, and correctly *not* excluded from PBDIT.
- **FY2026 standalone implied tax rate of 1.72%** (tax expense Rs 32.34 crore on PBT of Rs 1,884.11 crore) is disclosed and explained, not silently absorbed: current tax of Rs 331.25 crore was almost fully offset by a **deferred tax credit of Rs 298.91 crore**. This is a genuine, one-off tax-line movement, not a sustainable low-tax structure, and is not projected forward.

## 5. Qualitative fact register (traced, with source; corroborated per Step 1b)
- **Promoter (Kanwar family / Promoter Group) holding: 36.93%** (23,45,67,487 shares) — AR shareholding pattern table, corroborated against the "no transaction with any 10%+ promoter-group entity" related-party disclosure in the same document.
- **Outstanding ratings, per the company's own AR**: **CRISIL AA+/Stable** for long-term facilities (includes term loans, NCDs, fund-based bank facilities), reaffirmed 24-Dec-2025; **CRISIL A1+** for short-term (commercial paper), reaffirmed. India Ratings carries the same: **IND AA+/Stable, IND A1+**. Confirmed present in the reference library (CRISIL *Apollo Tyres Limited_24 Dec 2025*) — Step 14 divergence table below.
- **Subsidiaries (33 entities, all named per Form AOC-1, 100%-owned throughout, failure mode 17):** the group is heavily Europe-weighted — Apollo Tyres (NL) B.V. (the Enschede entity), (Hungary), (Germany), (France), (Belux), (Austria), (Schweiz), (UK, two entities), (Nordic), Iberica, plus Reifencom GmbH (Hannover) and Reifencom Tyre (Qingdao) — alongside US, South African, Thai, Middle Eastern, Singapore and Brazilian entities. Full list in the engine's `SUBSIDIARIES` dict and Annexure II below.
- **Contingent liabilities (standalone, FY26): ~Rs 440.55 crore** (excise/customs/GST Rs 220.83 crore, income tax Rs 183.16 crore, sales tax Rs 10.29 crore, employee/other claims Rs 26.26 crore) — **down sharply from ~Rs 1,164.02 crore in FY25**, driven almost entirely by the excise/customs/GST line falling from Rs 957.32 crore to Rs 220.83 crore. Management states it does not expect any outflows.
- **Debt instruments (note 7, standalone):** three outstanding NCD series (8.75% due Apr-2030, Rs 499.25 crore; 7.53% due Sep-2027, Rs 249.91 crore; 8.65% Rs 115.00 crore bullet, maturing Apr-2026) plus two rupee term loans (Rs 731.54 crore and Rs 333.59 crore total incl. current maturities), all secured by pari-passu charge on movable fixed assets. **No ISIN found anywhere in the document set for any of the three NCD series** — searched and confirmed absent (`INE[0-9A-Z]{9,10}` returns zero hits across all documents); the equity ISIN (INE438A01022) is disclosed but is not a debt instrument. Marked TBC in Annexure I. Shareholders separately approved (16-Jan-2026) headroom to raise up to Rs 1,000 crore via further NCD private placement — not yet issued as at the AR date. Commercial paper raised during FY26 was fully repaid within tenure; nil outstanding at year-end.
- **ESG headline figures:** Top Employer status across India, Hungary, Netherlands and the UK; HSE engagement index 4,500 per million hours; recordable-injury rate improved to 0.74 from 0.78; ~15 million CSR beneficiaries; 97% of natural-rubber suppliers signed the Apollo Sustainable Natural Rubber Policy; 78% of upstream suppliers signed the Apollo Tyres Sustainable Procurement Policy.

## 6. Sector-defining metrics (auto components/tyre — not the "EBITDA/tonne" the pre-flight detector flagged, which is a metals-sector signature)
- **Total production: 732,097 MT (FY26)**, sold in 100+ countries.
- **Radialisation** in the Indian commercial-vehicle segment continuing to rise, supported by brand strength in the Truck Bus Radial (TBR) category — a genuine multi-year industry direction named in the MD&A, not a snapshot.
- **Segment structure**: APMEA (Asia Pacific, Middle East & Africa — includes Indian manufacturing), Europe, Others — replacement and OEM channels within each. Europe is the segment carrying the Enschede closure; APMEA (anchored by India) is the larger and structurally stronger segment.
- Capacity-utilisation and per-tyre realisation figures were **searched and not found as a standalone disclosed percentage/rate** in the document set (`capacity utilisation`, `installed capacity` — zero hits); the AR discusses capacity in narrative/investment terms (capex outflow, new plant commissioning) rather than a quoted utilisation rate. Recorded as an evidenced gap, not silently omitted.

## 7. Liquidity (Step 11 — sources vs. claims, ~12 months, standalone)
- **Sources**: cash + bank balances Rs 448.15 crore (FY26, standalone) + net cash from operations (strong given FY26 PAT recovery to Rs 1,851.77 crore) + Rs 1,000 crore of newly-approved but unissued NCD headroom.
- **Claims**: current maturities of long-term debt (NCD Rs 115.00 crore + term loan current maturities Rs 213.50 crore = Rs 328.50 crore, note 7) plus ongoing working-capital requirements; capex commitments tied to the Group's stated capex outflow of Rs 1,403.00 crore (consolidated, FY26).
- **Descriptor: Strong** — standalone gearing at 0.23x and interest coverage at 9.70x (FY26) give ample headroom; the improving multi-year gearing trend (0.35x→0.32x→0.23x) reflects sustained deleveraging even through the FY25 margin trough, not a one-year snapshot.

## 8. Methodology Compliance Map (Step 10)
| Rating factor (Section VII does not name tyre manufacturers explicitly — Section I/IV apply) | Company evidence | Assessment |
|---|---|---|
| Market position / scale | 732,097 MT FY26 production, 100+ countries served, established global brand (Apollo, Vredestein) | Strong, established multi-decade position |
| Operating efficiency / cost structure | Consolidated PBDIT margin trough-to-recovery 18.13%→14.01%→15.02%; European footprint rationalisation (Enschede closure) directly addresses a cost-structure weakness | Improving, actively managed |
| Capital structure | Gearing improving every year (0.35x→0.30x→0.22x consolidated) | Strong and improving |
| Coverage | Interest coverage 9.09x→8.20x→10.93x | Strong, recovered from the FY25 dip |
| Management/governance | No qualified audit opinion in any of three years reviewed; KAM on the Enschede impairment reflects appropriate, not deficient, disclosure; promoter (Kanwar family) holding stable at 36.93% | Sound |
| Parent/group | Not applicable — Apollo Tyres is itself the ultimate listed parent; no upstream support notching required |

## 9. Divergence against the prior CRISIL rating action (Step 14 — opened only after the above view was formed)
CRISIL's own prior action (*Apollo Tyres Limited_24 Dec 2025*, reference library) and the company's own AR both disclose the outstanding rating as **CRISIL AA+/Stable — A1+**. The standalone and consolidated financial risk profiles computed here (improving gearing and coverage across the review period, a well-explained one-off behind the FY26 exceptional item, no qualified audit opinion) are consistent with a AA+ outcome — no divergence identified at this stage. The Enschede plant closure, while a real European-footprint weakness, is treated by this analysis as a decisive, disclosed corrective action (ceasing loss-making capacity) rather than an open-ended risk, consistent with the group's continued deleveraging through the same period.

## 9a. Step 12b — quantitative anchor and its divergence (binding: any AA+/AAA divergence must be explained)
`Rating_Scorecard_Apollo_Tyres.xlsx` filled from the audited actuals above (sector: "Auto components", the closest of the workbook's 22 sectors — no dedicated tyre-manufacturer row exists). **The workbook's formulas were not recalculated by a spreadsheet engine in this environment**; the chain was replicated by hand against the exact formulas in the Scorecard/Rating/Projections sheets and is recorded on the `Anchor_Computation_Manual` sheet — this should be re-verified by opening the workbook in Excel before any Committee reliance.

**Anchor grade: CRISIL AA (Stable) / A1+ — one notch below the company's actual outstanding rating (CRISIL AA+/Stable / A1+).**

This is the same pattern found on the Oil India case, and the same documented calibration limitation applies (`Scorecard_Backtest_Report_18Jul2026.md`: the anchor under-reads issuers near the AA+/AAA boundary absent a fuller support-notch and qualitative assessment than a screening tool can apply). Two specific mechanisms here: the financial-risk sub-score (1.46/6, near the strongest end of the scale already) only averages FY2026 actual against a FY+1 projection — it does not credit the **three-year improving direction** (gearing falling every year, 0.35x→0.30x→0.22x) that is the actual strength of this credit; and the scorecard has no mechanism to credit the Enschede plant closure as a **completed, disclosed corrective action** rather than an open risk. Both are exactly the kind of context a screening tool cannot see and a qualitative rating view can.

This is not treated as a reason to move the Step 13 rating view. The view below is formed on the standalone/consolidated trend, the completed European corrective action, and the reference-library corroboration — not on the scorecard number.

## 10. Rated-amount table
No CRISIL rated-amount table for Apollo Tyres Limited itself was found in `CRISIL/Report for Reference/` (only for unrelated peer-named entities — APL Apollo Tubes, Apollo Hospitals — excluded per Step 1a's own name-token-match warning: neither is the same issuer). **Rated amounts are therefore "to be confirmed by issuer."**

## 11. Step 12 scaling decision
Recorded in `case.json`: given (a) Apollo Tyres is an established AA+-rated issuer with three years of consistent, improving financials and no distress history, (b) the single most consequential forward-looking event (the Enschede closure) is a completed, disclosed action rather than an open uncertainty requiring multi-year modelling, and (c) no sector-assumptions document was supplied, a **focused sensitivity model on 2–3 rating-driving variables** (raw-material cost pass-through, European segment margin post-Enschede, capex/deleveraging pace) is used in place of the full 5-year equity-research-plugin workflow. See `Apollo_Tyres_Sensitivity_Model_30Aug2026.md`.

## 12. Unverified inputs / disclosed differences
See `UNVERIFIED_INPUTS` and `DISCLOSED_DIFFERENCES` in `compute_ratios.py`: no ISIN found for the outstanding NCDs (terms disclosed, ISIN not); consolidated PAT carries no explicit NCI line (basic EPS reconciles closely to PAT/shares, implying minimal NCI, but this is inferred); the FY2026 exceptional item and standalone tax-rate movements, both explained above.
