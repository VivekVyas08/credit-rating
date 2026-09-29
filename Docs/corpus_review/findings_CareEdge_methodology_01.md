# CareEdge Methodology Corpus — Full Read (77/77 files), 13-Sep-2026

Every file in CareEdge/Methodology/ read in full via the Read tool by 8 dispatched agents, each covering ~10 files. Merged below in file order.

# CareEdge Methodology Corpus Review — Part 1 (10 files)

## Analytical treatment of restructuring - COVID-Revised (15-7-22).md

- **Scope:** Covers analytical/default-recognition treatment for entities restructuring debt under RBI's Aug-6-2020 "Resolution Framework for Covid-19 related stress" and the related SEBI Aug-31-2020 relaxation (default-recognition relief up to Dec 31, 2020). Applies to rated bank facilities and to capital-market/money-market instruments. A COVID-era, time-boxed policy — not a general methodology; superseded/dated document, low relevance to current ratings unless a legacy OTR case resurfaces.
- **Rating-factor structure:** Not a scorecard document — it is a default-recognition decision tree (bank facilities vs capital-market instruments; before/after due date; application accepted/rejected/pending).
- **Indicative-metrics tables:** None (no numeric thresholds). Only a qualitative/process flowchart (rendered as broken image/OCR placeholders in the .md) and one voting threshold: resolution plan approved when **"75% by value and 60% by number of lenders agree"**; inter-creditor agreement to be signed within **30 days** of approval; plan implementation required within **180 days** of invocation.
- **Notching/support/mapping rules:** No notching. States CARE may take rating action (revision/credit watch/outlook change) even where default is not technically recognized under the OTR relief, if credit quality has structurally weakened.
- **Definitional differences:** None relevant to net-worth/gearing/TOI/PBILDT. Reiterates the general default-recognition principle: "Non-servicing of debt ... in anticipation of a favourable response from banks ... shall be considered as a default. Rescheduling ... prior to the due date ... will not be treated as default, unless the same is done to avoid default or bankruptcy."
- **Bright-line/mechanical-check-worthy thresholds:** The **75% value / 60% number** lender-approval threshold, the **30-day** ICA signing window, and the **180-day** implementation window are precise and could be coded as eligibility checks for legacy OTR treatment — but this is a dated, narrow COVID policy, not a general scorecard input, so low priority for the misweighting bug hunt.

## Assigning Outlook or Rating Watch to Credit Ratings.md

- **Scope:** Governs when CARE assigns a rating "Outlook" (Positive/Stable/Negative) vs a "Rating Watch" (Positive/Negative/Developing). Outlook applies to all long-term instrument-level ratings except CARE C and CARE D (CARE C may get one selectively). Outlook explicitly does NOT apply to: short-term ratings, securitisation ratings, ratings already on Rating Watch, Issuer-Not-Cooperating ratings (where none was assigned earlier), mutual-fund credit-quality ratings reviewed monthly, and non-debt products.
- **Rating-factor structure:** Not a scorecard — a policy defining two forward-looking qualifiers layered on top of a rating.
- **Indicative-metrics tables:** None — purely qualitative/definitional, no numeric thresholds.
- **Notching/support/mapping rules:** Key distinguishing rules (relevant to a ratings tool's post-processing logic):
  - Outlook horizon: "typically about six months to two years."
  - Rating Watch horizon: shorter, event-driven, expected to resolve quickly.
  - "The extent of a rating change under a 'Rating Watch' situation may be severe/substantial i.e., more than one notch. However, outlooks are expected to lead to rating changes of a much lesser degree" — i.e., Watch implies bigger potential notch moves than Outlook.
  - A Positive/Negative outlook does not guarantee an eventual upgrade/downgrade; CARE can also move ratings directly without a prior outlook/watch change.
- **Definitional differences:** None relevant to financial-statement definitions (no TOI/PBILDT/TNW/gearing content) — this is a pure ratings-process/communication document.
- **Bright-line thresholds worth a mechanical check:** The ">1 notch under Watch vs lesser degree under Outlook" statement is qualitative, not a bright-line number — no numeric cutoff to hardcode. The applicability exclusion list (short-term, securitisation, INC, mutual-fund) is the only mechanically checkable rule here (i.e., "does this rating category ever carry an Outlook?").

## CARE Ratings' Criteria for Rating Cement Companies September 2024.md

- **Scope:** Sector-specific overlay on top of CARE's general Manufacturing Sector methodology, applicable specifically to cement companies (covers industry risk, business/operations risk, project risk, financial risk, ESG). Explicitly says financial-ratio analysis follows CARE's standard "Financial Ratios – Nonfinancial Sector" criteria — this file adds cement-specific qualitative overlays only, not new ratio definitions.
- **Rating-factor structure:** 1. Industry Risk (regional demand-supply, cyclicality, government policy) → 2. Business & Operations Risk (A. Market/competitive position — size, brand/trade-mix; B. Operating efficiency/cost competitiveness — locational advantage, freight, power & fuel, plant vintage/utilization, product mix) → 3. Project Risk (timing vs demand-supply, land/clearances) → 4. Financial Risk (leverage/coverage, liquidity) → 5. ESG Risk (environmental, social, governance).
- **Indicative-metrics tables:** No formal banded table (no "AAA vs BBB" cutoffs), but several quantified industry benchmarks are stated as prose:
  - Freight cost: **"accounting for about 24%-27% of the operating cost"**.
  - Power & fuel cost: **"accounting for about 25%-35% of the operating cost"**.
  - PBILDT/tonne of cement observed **"for 3-5 years"** to capture cyclicality.
  - Six geographic demand-supply regions named: North, South, East, West, Central, North East.
- **Notching/support/mapping rules:** None (no parent-support/hybrid/LT-ST content in this document — cross-refers to other CARE criteria for those).
- **Definitional differences:** Key ratios named for leverage/coverage: "overall gearing (gross and even net of cash and cash equivalents), debt to PBILDT (gross and net) and interest and debt service coverage indicators PBILDT/interest and DSCR." No explicit statement here on TNW basis, LC/acceptances treatment, or P&L-note decomposition — this document explicitly defers to the separate Financial Ratios – Nonfinancial Sector criteria (not one of the 10 files reviewed in this pass) for those definitions. **Flag: the underlying "Financial Ratios – Nonfinancial Sector" doc (present in the folder but not part of this batch) is where the net-worth/gearing/TOI definitions actually live and should be reviewed for the specific bug (wrong net-worth basis, LC/acceptances in gearing).**
- **Bright-line/mechanical-check-worthy:** The 24-27% freight-cost-of-total-cost and 25-35% power-fuel-cost-of-total-cost bands are precise enough for a plausibility/sanity check in a tool (flag if a cement company's freight or power-fuel % of total cost falls far outside these ranges as an input-quality red flag), but they are industry-typical ranges, not rating-notch cutoffs.

## CARE_Ratings_criteria_for_Iron_&_Steel_Feb_2025.md

- **Scope:** Sector-specific overlay for the Iron & Steel industry, layered on CARE's general Manufacturing Sector methodology (per the routing logic — Corporate + sector methodology). Covers Management Risk, Business & Operational Risk, Project Risk, Financial Risk, ESG Risk for primary and secondary steel producers.
- **Rating-factor structure:** A. Management Risk → B. Business & Operational Risk (1. Cyclicality, 2. Size of operations, 3. Control over raw-material supply & cost [backward linkages, cost control, freight, power], 4. Technology & plant ageing, 5. Geographical & product diversification, 6. Regulatory risks) → C. Project Risk (timing of expansion vs demand-supply, land/clearances) → D. Financial Risk (large working-capital requirements, access to financial markets) → E. ESG Risk.
- **Indicative-metrics tables — "Key Ratios" list (verbatim):**
  ```
  - Total cost per tonne of steel manufactured
  - Power & fuel cost per tonne of steel manufactured
  - PBILDT per tonne of steel sold across the cycles
  - Total debt/Installed capacity
  - Debt/PBILDT
  ```
  No numeric bands/cutoffs given for any of these — only the metric names, no thresholds attached.
  - Other quantified prose points: raw material constitutes **"~70%-75% of cost of sales of steel"**; steel plant technology size cutoff: blast-furnace route mainstay for large plants **"(> 1 mtpa)"**, DRI route preferred for smaller plants **"(< 1 mtpa)"**; gestation period for a new steel plant **"3-5 years"**; illustrative raw-material transport ratio: "1 MT of steel requires 1.5 MT of iron ore, and 1 MT of Coking coal ... almost 2.5 MT of raw material" transported per MT of steel.
- **Notching/support/mapping rules:** None in this document.
- **Definitional differences:** No explicit net-worth/gearing/TOI/PBILDT definitional deviation stated here — again defers implicitly to the general Financial Ratio criteria. The "Debt/PBILDT" and "Total debt/Installed capacity" are sector-specific ratio *constructs* (not in the generic corporate list) worth flagging for a rating tool: "Installed capacity" as a denominator is unusual and must be sourced/defined (units: tonnes) precisely to avoid misapplication.
- **Bright-line/mechanical-check-worthy:** The ">1 mtpa = blast furnace; <1 mtpa = DRI" plant-size cutoff and the ~70-75% raw-material-cost-of-sales range are concrete enough for input-plausibility checks, though not rating-band cutoffs.

## CARE_Ratings_criteria_for_rating_of_Market_Linked_Debentures_Feb_2025.md

- **Scope:** Applies only to Principal-Protected Market Linked Debentures (PP-MLDs) — MLDs whose principal is protected per SEBI mandate but whose coupon is linked to a market benchmark (equity index, G-Sec, commodity). CARE explicitly rates PP-MLDs only ("CARE Ratings provides credit ratings only for PP-MLDs"); non-principal-protected MLDs, self-referencing products (returns linked to issuer's own equity), and inflation-linked notes (unless carrying extra embedded market risk) are excluded or treated differently (rated without the PP-MLD prefix). Floating-rate instruments (MIBOR/T-Bill/MCLR-linked) are also excluded from the PP-MLD prefix.
- **Rating-factor structure:** Not a scorecard — states that the MLD's rating IS the issuer's underlying credit rating methodology (routed by sector/entity type as normal); this document only governs the PP-MLD *prefix* mechanics and rating-scale treatment, not a separate factor framework.
- **Indicative-metrics tables:** None (no numeric thresholds) — contains only two illustrative worked examples of coupon structures (Nifty 10-yr G-Sec index-linked; Nifty 50-linked) showing how coupon payout scales with underlying index performance (e.g., "if the final level is over 40% of the initial level, then 'Y' coupon is paid, and if the final level is less than 40%, then coupon will be nil" — illustrative example numbers, not a rating criterion).
- **Notching/support/mapping rules:** The rating of the MLD = the issuer's senior/issuer credit rating with a "PP-MLD" prefix appended — e.g. issuer at "CARE A+; Stable" → ELD rated "CARE PP-MLD A+; Stable." No notching down/up for the market-linked feature itself — market risk is explicitly NOT reflected in the credit rating ("does not account for potential fluctuations in returns due to adverse movements in underlying variables").
- **Definitional differences:** None relevant to financial statement metrics — this is an instrument/rating-scale document, not a financial-ratio document.
- **Bright-line/mechanical-check-worthy:** None load-bearing for the misweighting/net-worth bug hunt. Only a structural rule worth encoding if the tool ever rates MLDs: "PP-MLD" prefix = issuer's own rating; never a separate scorecard.

## Consolidation-and-Combined-Approach-March-2025.md

- **Scope:** Governs when CARE rates an entity standalone vs consolidated vs "combined" (group-as-single-entity). Covers three parent archetypes: (1) corporate parent with substantial operations, (2) holding company of subsidiaries in similar line of business, (3) pure investment holding company (cross-refers to separate Investment Holding Companies methodology). Also covers Core Investment Companies (CICs) in the financial sector. Combined approach explicitly excluded for any group containing a listed entity (unless cross-guarantees exist).
- **Rating-factor structure:** Not a scorecard; a decision framework with enumerated trigger criteria for consolidation:
  - Consolidate when: subsidiary strategically important to parent (e.g., marketing arm); parent controls management/operations; legal obligations (corporate guarantees/cross-guarantees) exist between parent and subsidiary; parent has demonstrated past financial support; moral obligation (shared name/brand/common board); actual or expected inter-corporate fund movement (ICDs, advances, loans, equity infusions).
  - Do NOT consolidate when: subsidiary is a different business segment, or is a ring-fenced SPV — in these cases CARE assesses parent standalone but factors in cash-flow impact of likely support/investment.
  - Non-controlling stakes / strategic JVs: even without control/majority ownership, CARE makes "suitable adjustments" to reported consolidated financials to factor in debt/support if there's a corporate guarantee, shortfall undertaking, cross-default clause, or expected unhindered support to an associate/JV.
  - Combined Approach criteria (ALL must hold): closely-held, common promoter/family control; cash-flow fungibility across entities; similar or related (incl. forward/backward-integrated) lines of business; common management controls treasury. Combined approach is barred if any group entity is listed (exception: cross-guarantees by the listed entity), or if inter-se fund movement is restricted by financing docs, or if fungibility has NOT been demonstrated historically (e.g., one entity stressed while another with surplus funds did not support it).
  - Notching within combined approach: **"CARE Ratings may differentiate between the rating of individual entities by up to two notches, based on their constitution, relative size, contribution to the group's present and future cash flow, strategic importance to the group, project risk and the standalone financial risk profile relative to the overall group."**
- **Indicative-metrics tables:** None — this is a qualitative decision-tree document, no numeric thresholds.
- **Notching/support/mapping rules:** The **"up to two notches"** differentiation cap under combined approach is the key concrete rule (bright-line, see below). Disclosure requirement: CARE must disclose "extent of consolidation" as **Full / Proportionate / Moderate** (Full/Proportionate = line-by-line consolidation depending on control/ownership; Moderate = equity-method consolidation or support-factored-into-parent-standalone cases).
- **Definitional differences:** This document is directly load-bearing for the ICRA-tool's traced bug of **wrong basis choice** (the SOP's R12 rule references exactly this kind of criteria). It does NOT define net-worth/gearing/TOI itself, but it DOES establish that: (a) basis (standalone/consolidated/combined) is a **methodology-driven determination** based on the enumerated trigger list above, not an analyst/operator default choice; (b) even where consolidation isn't done, "suitable adjustments" must be made to standalone financials to reflect guarantee/support-linked debt of unconsolidated entities — i.e., an entity's true debt exposure can be understated if these adjustments (which could include guaranteed subsidiary debt) are skipped.
- **Bright-line/mechanical-check-worthy:** The **"up to two notches"** cap for intra-group differentiation under the combined approach is a precise, codeable rule. The consolidation/combined-approach trigger checklist (listed vs unlisted; demonstrated fungibility vs not; SPV ring-fencing vs not) is also a good candidate for a mechanical eligibility gate in a ratings tool, to catch cases where the wrong basis (standalone vs consolidated) was silently assumed.

## Criteria Paper Fertilizer May 2024.md

- **Scope:** Sector overlay for fertilizer manufacturers (urea/nitrogenous, phosphatic/potassic "complex" fertilizers), layered on the general Manufacturing Sector methodology. Explains urea's New Pricing Scheme (NPS, effective Apr 1 2003) and New Urea Policy (NUP, May 2015) subsidy/energy-norm framework, and the Nutrient Based Subsidy (NBS, effective Apr 1 2010) scheme for complex fertilizers.
- **Rating-factor structure:** Named factor list (from the document's own diagram): Regulatory Framework, Energy Efficiency, Feedstock, Forex, Product Profile, Modernisation Plans, Market Position, Agro-Climatic Risk, Working Capital Intensity, Event Risk, ESG Risk. Plus a "Sector-specific analysis" section on Adjusted Collection Period and Working-Capital Intensity Level.
- **Indicative-metrics tables:** No numeric banded table. One concrete numeric range given: lending institutions "have been funding subsidy receivables up to **240 to 360 days** due to their sovereign nature" — a working-capital/DP (drawing power) financing norm, not a rating cutoff. Direct Benefit Transfer (DBT) for subsidy began **February 2018** (subsidy now tied to point of retail sale rather than point of dispatch, per the doc — increasing working-capital intensity).
- **Notching/support/mapping rules:** None (no parent-support/hybrid/LT-ST content here).
- **Definitional differences — HIGH RELEVANCE to the traced bug:**
  - **"Adjusted collection period"**: "Many of the companies might not report subsidy receivables in trade receivables. **The collection period is calculated including the subsidy receivables** to evaluate the working capital intensity of operations." This is a sector-specific redefinition of a standard ratio (collection/receivable days) — a generic tool that computes collection days from trade receivables ALONE (excluding subsidy receivable, which fertilizer companies may book as a separate "other receivable"/non-trade line) would materially understate working-capital intensity for a fertilizer company. This is directly analogous in kind to the traced ICRA-tool bug pattern (P&L/BS aggregates not decomposed correctly) — here the risk is the opposite direction: an aggregate that SHOULD be combined (trade + subsidy receivable) being left split.
  - **"Working-capital intensity level"**: defined as utilisation of working-capital limits against sanctioned limits (not a balance-sheet ratio at all, but a limit-utilization metric) — another sector-specific metric a generic engine might not compute correctly if it assumes "intensity" means a receivable/inventory-days ratio.
- **Bright-line/mechanical-check-worthy:** The 240–360 day subsidy-receivable funding-tenor norm is a plausibility-check candidate. The "adjusted collection period" definitional rule (include subsidy receivable in receivable/collection-days calc even if separately captioned) is the most actionable finding in this file for a mechanical/code check — a rating tool computing this sector's receivable days must explicitly search for and add back subsidy-receivable line items.

## Criteria-Methodology-Infrastructure-Sector-Ratings-Mar-2025.md

- **Scope:** Cross-cutting methodology for Infrastructure Sector Ratings (ISR) — power (gen/transmission/distribution), roads (toll/annuity/HAM), telecom, airports, ports, and similar infra debt programmes, including SPV debt with access to pooled InvIT cashflows. Explicitly a distinct methodology from corporate-sector debt ratings, since infra revenue is largely tariff/regulator/contract-driven with low demand risk (vs. corporate methodology's demand-growth focus). Cross-refers to separate sub-sector methodologies (roads, airports, ports, power sub-types, InvITs) for detail — this doc gives the broad cross-cutting framework covering both project (construction) phase and operational phase.
- **Rating-factor structure:**
  - **Project/implementation phase:** I. Sponsor's evaluation (ownership structure, track record, rationale for setting up project, sponsor's current financial position, technical strength) → II. Approval & completion risk (geography, resource/land/water/manpower availability, permits/clearances, time/cost overrun risk, third-party [lender's engineer] assessment, financial closure/funding mix, contractor track record, physical implementation status) → III. Contractual risk assessment (concession agreement / EPC / O&M contract terms) → IV. Revenue risk (demand & price risk; availability-based vs merchant) → V. Debt maturity & structural features (tenor, ballooning structures, DSRA, escrow/TRA) → VI. Financial risk (cash-flow stability, profitability, leverage incl. top-up loans, liquidity, DSCR under base/stress, IRR/payback, refinancing/tail period, financial flexibility).
  - **Operational phase:** I. Contractual arrangement/risk allocation → II. Business risk (pricing risk, demand risk, counterparty risk, raw-material/fuel supply, O&M arrangements) → III. Financial risk (cash flow adequacy, refinance risk, DSCR/cash coverage ratio, waterfall, financial/operational covenants, forex/interest-rate risk) → IV. Management risk.
  - Plus: Force Majeure Risk (explicitly NOT factored into credit assessment due to unpredictability — "credit ratings principally follow probability of default approach") and ESG Risk (Environmental/Social/Governance).
- **Indicative-metrics tables:** No numeric banded thresholds anywhere in this document — entirely qualitative framework; DSCR/cash-coverage-ratio are named as key metrics but no specific cutoff values (e.g., no "DSCR > 1.2x = strong" table) are given here.
- **Notching/support/mapping rules:** No explicit notching rules. Comparative statement only: "Between two regulated assets having similar DSCRs, the asset having a materially longer tail period will have a relatively superior financial flexibility" (qualitative comparison, not a numeric rule).
- **Definitional differences:** No net-worth/gearing/TOI/PBILDT definitions in this document — it is a risk-factor framework, not a ratio-definition document. No cash-flow-vs-P&L definitional conflict content either, though DSCR (a cash-flow-statement-style measure by nature) is central here — this reinforces that for infra/project-finance entities, cash-flow-based ratios ARE the correct/expected basis (unlike the traced ICRA-tool bug of wrongly substituting cash-flow figures for P&L figures in a corporate context) — i.e., this document is evidence that the P&L-vs-cash-flow-basis question is *entity-type dependent*, and a tool must not apply one universal rule.
- **Bright-line/mechanical-check-worthy:** None — this document contains no numeric bright-line cutoffs at all. Purely qualitative/factor-list framework.

## Criteria-Methodology-Power-Distribution-Companies-March-2025.md

- **Scope:** Covers Distribution Licensees (DLs, mostly state-owned DISCOMs) and Distribution Franchisees (DFs, private entities operating on DL's behalf under franchise agreements) within the power-distribution segment. Cross-refers to the general Infrastructure Sector Ratings methodology for management-risk detail and to "Liquidity Analysis of Non-Financial Sector Entities" for liquidity assessment.
- **Rating-factor structure:** Consumer category mix → Operational performance (AT&C loss = billing efficiency × collection efficiency) → Cost structure analysis (power purchase cost, O&M/employee cost) → Regulatory risk (ARR/tariff-petition process, MYT regime, regulatory assets) → Extent of Government Support → Financial risk (revenue gap = ACS−ARR, leverage, creditor/debtor days, capex funding mix, coverage) → Quality/adequacy of accounting compliance & disclosures → Structural risk (DF-specific: agreement tenor, annualised input rate, capex commitment) → Management evaluation → ESG Risk.
- **Indicative-metrics tables:** No formal banded numeric table, but one precise prose figure: **"power purchase cost typically accounts for over 70% total cost of a DISCOM."** ARR components explicitly listed: power purchase cost, employee cost, O&M expenses, G&A expenses, interest on term/working-capital loans, depreciation, post-tax return on equity. Tariff-petition timeline norms stated: DISCOM "files petition for true-up of past audited accounts and tariff for the projected year by **November 30**"; SERC "sets tariff for the next financial year by **March 30**."
- **Notching/support/mapping rules:** None explicit (no notch-count rules) — qualitative "viewed favourably/negatively" language throughout (e.g., regular tariff hikes, budgetary subsidy allocation, FPPPAC mechanism presence = positive; revenue gap growth, high subsidy dependence, non-filing of tariff petitions, disallowed cost recovery = negative).
- **Definitional differences — sector-specific metric definitions distinct from generic corporate ratios:**
  - **AT&C loss** = billing efficiency × collection efficiency (billing efficiency = fraction of energy purchased that is billed; collection efficiency = fraction of billed revenue collected, including subsidy).
  - **Revenue gap** = ACS (Average Cost of Supply) − ARR (Average Revenue Realised) — a DISCOM-specific profitability-substitute metric; a corporate-style "operating margin" ratio would not apply.
  - Contingent liabilities/off-balance-sheet commitments assessed "as a percentage of total net worth" — an explicit net-worth-denominator ratio, though no % threshold given.
  - No explicit statement here on TNW basis (revaluation/intangibles) or gearing inclusions (LC-backed creditors, acceptances) — this document doesn't override those; it is purely about DISCOM-specific operating/regulatory metrics layered on top of the standard financial-ratio criteria.
- **Bright-line/mechanical-check-worthy:** The **">70% of total cost = power purchase"** benchmark is a plausibility-check candidate. The **Nov 30 / Mar 30** tariff-petition/order filing deadlines are precise, codeable compliance-timeline checks (useful for a "regulatory risk" flag: has DISCOM filed on time / has SERC ruled on time).

## Criteria-Pools-Backed-by-Wholesale-Assets-March-2023.md

- **Scope:** Covers rating of transaction structures (e.g., AIFs, CDOs) where a pool of wholesale-credit receivables backs a rated obligation; ratings carry the **"(SO)"** (structured obligation) suffix. Explicitly EXCLUDES obligor/co-obligor structures where underlying wholesale credits belong to the same group ("This criteria paper shall not be applied to obligor and co-obligor structures, where pools of underlying wholesale credits belong to same groups").
- **Rating-factor structure:** 1. Originator/Sponsor/Promoter analysis (track record, investment strategy, underwriting capability for actively-managed pools) → 2. Assessment of credit quality of underlying pool credits (individual ratings/default-likelihood of each wholesale exposure) → 3. Analysis of transaction structure (tranches — senior/mezzanine/junior; waterfall mechanism; credit enhancement — over-collateralisation/subordination [implicit] or cash collateral/third-party guarantee [explicit]; interest-rate/basis risk; legal structure/bankruptcy-remoteness) → 4. Monte Carlo Simulation to generate a shortfall-distribution table against the rated structure.
- **Indicative-metrics tables:** No numeric banded thresholds — the "simulation" methodology (Monte Carlo) is described procedurally (steps a-e: simulate scenarios → determine default/no-default per underlying credit per its own PD → apply asset correlation → aggregate portfolio defaults → generate shortfall distribution vs rated claims) but no specific correlation, LGD %, or PD numbers are disclosed in this document (those are internal model parameters, not published thresholds).
- **Notching/support/mapping rules:** No entity-level notching rules; ratings are output of the simulation/waterfall model, not a scorecard-notch process. Correlation-assumption logic stated qualitatively: same-sector credits assumed more correlated than cross-sector; same-group borrowers get a higher correlation assumption "to factor interdependence and linkage." LGD/recovery-timing assumptions are based on "experience of banking sector NPAs, IBC, and other similar forums," varying by security seniority/value/liquidity and servicer track record. Recoveries expected after maturity of investor claims are explicitly ignored in cash-flow modelling.
- **Definitional differences:** Not applicable — this document contains no TOI/PBILDT/TNW/gearing definitions; it is a structured-finance/pool methodology, conceptually distant from the corporate scorecard definitional bugs traced in the ICRA tool.
- **Bright-line/mechanical-check-worthy:** None numeric in this document — no cutoffs to hardcode. The one crisp scope-boundary rule worth encoding as an eligibility check: this criteria explicitly does NOT apply to obligor/co-obligor structures of same-group wholesale credits (a routing/scope check, not a ratio threshold).

---

## Cross-cutting observations relevant to the traced ICRA-tool bug

1. **The bug's root documents are likely NOT in this batch.** None of these 10 files define TNW, gearing, TOI, or PBILDT from first principles — they all defer to CareEdge's separate "Financial Ratios – Nonfinancial Sector" (and, for financial-sector entities, the financial-sector ratios criteria) documents, which exist in the same Methodology folder but were **not** part of this 10-file assignment. **Recommend Part 2 prioritize `Financial_Ratios_Non_Financial_Sector_March_2025.md` and `Criteria_Rating_Methodology_Financial_Ratios_Financial_Sector_February_2025.md`** — those are where net-worth basis, gearing inclusions (LC/acceptances), and TOI/PBILDT definitions are actually specified, and are the probable source of the definitional-error class described in the audit brief.
2. **Sector-specific ratio redefinitions found in this batch that a generic engine could get wrong:**
   - Fertilizer: "adjusted collection period" must **include subsidy receivables** even when booked outside trade receivables — a decomposition/aggregation issue in the same family as the traced "aggregate P&L notes not decomposed" bug, but in reverse (here, a note should be *combined into* a ratio, not split out).
   - Power Distribution: AT&C loss and Revenue Gap (ACS−ARR) are DISCOM-specific substitutes for margin/profitability ratios — applying generic corporate margin definitions here would be a methodology mismatch (Failure Mode 28-style: "using another sector's metric set").
3. **Consolidation criteria (basis choice) is fully addressed** in the Consolidation-and-Combined-Approach file and is directly relevant to the "wrong net-worth/gearing basis" bug class if the ICRA tool ever chose consolidated vs standalone incorrectly — but that file governs *which entity's financials to use*, not how to define net worth/gearing once the basis is chosen.
4. **No file in this batch discusses treating LC-backed creditors/acceptances/buyers' credit as debt**, nor cash-flow-statement-vs-P&L-figure substitution rules — confirms these definitions sit in the Financial Ratios methodology documents outside this batch.

# CareEdge Methodology Corpus Review — Part 2 (10 files)

All 10 files were read in full via the Read tool (no truncation encountered — each file was 148–363 lines and returned complete in a single Read call).

---

## Criteria_Asset-Mortgage-Backed-Securitisation-Transactions-March-2025.md

- **Scope**: Covers CareEdge's rating methodology for securitisation transactions — Asset Backed Securities (ABS) and Mortgage Backed Securities (MBS) — including direct assignment of retail loan pools where CareEdge provides lifetime principal loss estimation. Applies to originators such as banks, NBFCs and HFCs selling pools via an SPV/trust issuing PTCs/SNs. Does not cover corporate/entity ratings — this is transaction/structured-finance only.
- **Rating-factor structure**: Not a scorecard of named weighted factors (unlike corporate/NBFC methodologies). Organized around five key risk categories: (1) Credit Risk, (2) Prepayment Risk, (3) Basis Risk, (4) Counterparty Risk (servicer, commingling, trustee/assignee, credit-enhancement provider, other counterparties), (5) Legal Risk. Then a separate analytical framework: Originator business-process analysis; Portfolio Data Analysis (disbursements, collection efficiency, dynamic delinquency/DPD bucketing, prepayments, static pool analysis, past pool performance); Collateral/Pool Analysis (pool selection criteria, pool characteristics, portfolio-vs-actual-pool comparison); Transaction structure analysis (legal soundness, par/premium, credit/liquidity enhancement, payment structures, waterfall/cashflow modelling); Forms of Credit Enhancement (internal: subordination/OC/equity tranche, EIS; external: cash collateral, corporate/bank guarantee).
- **Indicative-metrics tables** (verbatim):
  - Pool characteristics table (qualitative, not numeric-threshold) — Asset type, Asset Classification, Borrower Profile, Geographical Distribution, Obligor Distribution, Seasoning & Amortisation, LTV, Installment-to-Income ratio, Original Tenure, Credit Bureau Score, Property Occupancy, Property Type, Payment Status.
  - Delinquency bucket definitions cited: 30+ DPD, 90+ DPD, 180+ DPD.
  - Example static pool: "The peak 90+ DPD is 5.41% in Q1, while the average 90+ DPD is 4.80%."
  - Geography/Portfolio vs Actual Pool comparison table (worked numeric example):
    | Geography | Proportion of Portfolio as on 31st March, 20XX | Portfolio 90+ DPD as on 31st March, 20XX | Proportion of actual Pool |
    |---|---|---|---|
    | State 1 | 20.0% | 1.8% | 20.00% |
    | State 2 | 15.0% | 2.5% | 5.00% |
    | State 3 | 15.0% | 1.5% | 40.00% |
    | State 4 | 20.0% | 1.3% | 15.00% |
    | State 5 | 25.0% | 1.3% | 15.00% |
    | Others | 5.0% | 3.0% | 5.00% |
    | Total | 100.0% | 1.7% | 100.0% |
    | Weighted Average 90+ DPD in Actual pool (assuming Actual pool behaves like Originator's Portfolio) | | | 1.6% |
    | Extent of Negative Deviation | | | 1.60%/1.70% = 0.96 |
- **Notching/support/mapping rules**: Documents submission timeline of "90 days" post-transaction placement (SEBI-mandated), extendable by "an additional 90 days" case-to-case, else appropriate rating action per CareEdge's Policy on Provisional Ratings. No numeric notching table for credit enhancement sizing (sizing is via proprietary cashflow model, base/stress case shortfall approach) — no LT-ST mapping or outlook-trigger table (not applicable to this instrument type).
- **Definitions differing from generic/ICRA usage**: This is structured-finance methodology, so TOI/PBILDT/TNW/gearing concepts (corporate) are not used. Notably defines AUM-like concept differently for securitisation context (not applicable here — AUM formula appears in the NBFC file, not this one). Key CareEdge-specific definitions: "Excess Interest Spread (EIS)" = difference between pool interest and PTC investor interest, not a P&L margin concept; "Over Collateral" = excess of pool principal over PTC principal (a structural concept, not a P&L or balance-sheet ratio in the corporate sense). No net-worth or gearing definition present — not relevant to this instrument type.
- **Mechanically-checkable thresholds**: (a) 30+/90+/180+ DPD delinquency bucket definitions — exact bright lines usable in code; (b) SEBI-mandated 90-day document submission window with a defined 90-day extension; (c) the worked "Extent of Negative Deviation" ratio formula (Weighted Average Actual-Pool DPD ÷ Portfolio DPD) is a precise, codeable computation, though the underlying threshold for "acceptable" deviation is not stated numerically in this document.

---

## Criteria_Auto-Dealership-Criteria-Dec-2025.md

- **Scope**: Covers auto dealerships (OEM franchise dealers across PV, 2W, MHCV, LCV, tractors) under CareEdge's broader Services Sector methodology; this document only supplements the generic services-sector framework with dealership-specific factors (business/operational risk, financial risk, ESG). Explicitly trading-activity classification ("Although strictly falling under trading activity...").
- **Rating-factor structure**: Standard CareEdge services-sector skeleton — Industry risk, Business/operational risk, Financial risk, Management, Project risk (if any), ESG risk. Dealership-specific sub-factors under business/operational risk: OEM market share & dealer share of OEM sales; catchment-area characteristics; revenue diversification (TOI stability via spares/service/repair mix boosting PBILDT margin, insurance/finance tie-ups, used-vehicle buyback); cost structure and break-even sales level; working capital management (inventory days vs OEM credit period, channel financing); EV transition risk. Financial risk explicitly deferred to CareEdge's separate "Financial Ratios – Non Financial Sector" criteria.
- **Indicative-metrics tables**: No numeric threshold table present. Only a qualitative statement: "dealerships that are favourably placed... can breakeven in less than a year, whereas those dealerships entailing higher investment and higher cost structure... could take significantly more time." No quantified inventory-turnover, leverage, or margin bands given.
- **Notching/support/mapping rules**: None specific to instruments/hybrids/parent support in this document — general financial-risk assessment references CareEdge's generic non-financial-sector methodology for leverage. No LT-ST mapping table, no outlook-trigger table.
- **Definitions differing from generic/ICRA definitions**: Explicitly states leverage treatment for LEASED PREMISES: "CareEdge Ratings considers adjusted debt factoring in the present value of payments in the lease period and considers lease payments as part of interest costs (in line with IND-AS 116)." This is a definitional rule that affects gearing (adjusted debt includes discounted lease liabilities) and interest coverage (lease payments treated as interest cost) — directly relevant to the ICRA project's known "wrong gearing inclusions" error class since a lease/IND-AS 116 adjustment could be conflated with or omitted alongside LC/acceptances treatment. Notes debt "normally comprises working capital borrowings" — channel financing loans are typically <1 month tenor.
- **Mechanically-checkable thresholds**: No hard numeric cutoffs (e.g., no specific gearing ratio, no specific breakeven period in months/years is quantified — "less than a year" vs "significantly more" is qualitative). Channel financing loan tenor described as "normally less than a month" — soft guidance, not a bright-line rule enforceable in code.

---

## Criteria_CARE_NBFC_Criteria_February_2025.md

- **Scope**: Applies to companies registered as NBFCs with the RBI — standalone assessment methodology; final rating also incorporates notching for parent/promoter/group linkages per CareEdge's separate "Factoring Linkages Parent Sub JV Group" methodology. Covers subordinated debt and perpetual debt instrument criteria for NBFCs as well.
- **Rating-factor structure** (8 named parameters, explicitly diagrammed): (1) Business Mix and Growth Trend, (2) Capital & Leverage, (3) Asset Quality, (4) Profitability, (5) Liquidity, (6) Resource Profile, (7) Management and Systems, (8) Size, Vintage and Market Presence. Plus "Additional considerations": Peer group analysis, Market-based indicators, Regulatory Inspection/due-diligence, Accounting Quality, ESG (Environmental/Social/Governance).
- **Indicative-metrics tables**: No numeric indicative-band table (e.g., no explicit "CAR X% = AAA, Y% = AA" grid) — qualitative/relative framework throughout. One structured table for Perpetual Debt Instrument features:
  | Maturity Period | Perpetual maturity |
  |---|---|
  | Options | May have embedded 'Call' option subject to the instrument having run for at least 10 years from date of issue. Call option shall be exercised only with prior approval of RBI... |
  | Lock-in clause | NBFCs may defer payment of interest if: the NBFC's CRAR is below the minimum regulatory requirement prescribed by RBI; or the impact of such payment results in NBFC's CRAR falling below or remaining below the minimum regulatory requirement. |
  | Interest payment | Interest payment requires prior approval of RBI when the impact... may result in net loss or increase the net loss, provided the CRAR remains above the regulatory norm. |
  | Claim seniority | Claims of the PDI investors shall be superior to the claims of equity shareholders and subordinated to the claims of all other creditors. |
  | Capital treatment | PDI shall be eligible to be treated as Tier-I capital up to 15% of the total Tier-I capital. The amount of PDI in excess of amount admissible as Tier-I shall qualify as Tier-II capital. |
- **Notching/support/mapping rules**: (a) Perpetual Debt Instruments (PDI): "such instruments are generally notched down by at least one notch than the rating of senior debt" due to lock-in-clause sensitivity to CAR/capital-raising/profitability; delayed interest/principal after lock-in invocation constitutes an event of default per CareEdge's definition, and these instruments "might exhibit a somewhat sharper migration" than conventional debt. (b) Subordinated debt: CareEdge "generally does not differentiate" between senior and subordinated debt rating for NBFCs — PD is treated as identical, only LGD differs on liquidation; case-to-case differentiation possible on issuer-specific circumstances. (c) 15% Tier-I cap for PDI, excess treated as Tier-II. (d) Parent/promoter notching deferred to a separate linkage methodology (not detailed here).
- **DEFINITIONS differing from generic — HIGH RELEVANCE to known error classes**:
  - **Gearing/leverage definition**: "CARE Ratings also monitors debt-equity ratio of an NBFC... CareEdge Ratings also factors in assets under management (AUM)-to-net worth ratio." **AUM is explicitly defined**: "AUM = On-balance sheet advances (and lending in form of investments) + Off-book Securitisation portfolio + Co-lending + Business Correspondent." This is a sector-specific numerator broader than plain balance-sheet advances — an ICRA-project analyst mechanically computing "gearing" using only on-balance-sheet debt/net worth without adding back off-book securitised/co-lent exposure would misstate NBFC leverage per this methodology.
  - **Group-exposure-adjusted net worth**: "In case of significant exposure to the group entities, adjusted standalone leverage is calculated by reducing the amount of such exposure from the entity's tangible net worth." This is a specific TNW adjustment rule (deduct group exposure from TNW before computing adjusted leverage) — directly analogous to net-worth-basis errors flagged in the audit brief.
  - **Consolidated approach caveat**: "CARE Ratings considers capital adequacy of the holding company at standalone level per regulatory requirements" even when following a consolidated approach for group lending entities; "Overall gearing and net non-performing assets (NNPA)/net worth ratios are analysed" at consolidated level — a basis distinction (standalone CAR vs consolidated gearing/NNPA-to-net-worth) that could be a source of net-worth-basis mismatch if not tracked carefully.
  - **Liquidity ratio definition**: "For NBFCs running a cumulative negative ALM mismatch in up to one-year bucket, such cover will be below 100%" — cover = scheduled inflows from credit assets (adjusted for collection efficiency) in next 12 months ÷ 12-month debt obligations. Rating-linked acceleration clauses explicitly EXCLUDED from liquidity assessment ("CareEdge Ratings does not consider such rating-linked acceleration clauses") despite noting real-world severe impact if triggered — a definitional exclusion an analyst must not silently reverse.
  - **Off-balance-sheet treatment for asset quality**: "For NBFCs resorting to securitisation of their assets and/or involved in co-lending, CareEdge Ratings assesses leverage, asset quality and profitability based on AUM by treating such off-balance sheet assets as on-balance sheet." This is a specific instruction to gross up off-book assets into leverage/asset-quality ratios — a common point of ICRA-project error type (aggregate/decomposition treatment).
  - **Profitability/income decomposition**: "CARE Ratings analyses the composition of the company's income by segregating it into fee-based and fund-based activities. Core earnings are also identified by excluding non-recurring income from the total income." This explicit instruction to decompose income by segment/nature (not simply take P&L aggregate) is directly relevant to the "aggregate P&L notes not decomposed" error class flagged in the brief.
- **Mechanically-checkable thresholds**: (a) AUM formula (exact, codeable); (b) PDI Tier-I cap = 15% of total Tier-I capital, excess to Tier-II (bright-line, codeable); (c) PDI call option minimum 10-year running period before exercise (bright-line); (d) ALM/liquidity cover <100% threshold for negative mismatch flag (bright-line, though inputs require judgment); (e) at least one-notch-down rule for PDI vs senior debt (codeable as a notching rule, though "at least" leaves room for more).

---

## Criteria_CARE_Ratings_criteria_for_rating_of_Capital_Protection_Oriented_Mutual_Fund_Schemes_March_2025.md

- **Scope**: Covers CareEdge's CPOS (Capital Protection Oriented Scheme) ratings under SEBI's August 2006 CPOS guidelines — close-ended mutual fund schemes rated for the "degree of certainty" the portfolio structure achieves capital protection at maturity (NAV ≥ face value). Not an entity/corporate credit rating; explicitly states CPOS ratings are "not an opinion on the fund's management practices... financial performance and management quality of an AMC" and do not factor in business practices/reputation/compliance. No overlap with corporate/NBFC/bank credit-rating scope.
- **Rating-factor structure**: Not a scorecard — a risk-factor checklist for the debt/equity portfolio structure: Credit Risk (of debt component), Reinvestment Risk, Market Risk, Liquidity/Marketability Risk, Gap Risk/Crash Risk (relevant to CPPI structures), Float Risk. Plus "Structured Obligation" conditions: Asset allocation, Screening rules, Structure covenants, Maturity profile of debt instruments.
- **Indicative-metrics tables**: None with numeric thresholds. Key qualitative/bright-line rule: SEBI does not allow CPOS to invest in debt instruments rated below 'AAA'; CareEdge obtains Representations & Warranties requiring debt investment in "government securities or securities rated as 'CARE AAA' or equivalent," with mandatory sale/replacement on downgrade.
- **Notching/support/mapping rules**: Suffix "(SO)" (Structured Obligation) attached to CPOS rating symbols. Downgrade-of-debt-security trigger: "In case of any debt security being downgraded, it shall be sold and replaced with government security or security rated as 'CARE AAA' or equivalent. In case this is not possible, CareEdge Ratings shall re-evaluate the entire portfolio... to review the rating." Quarterly mandatory review (SEBI-mandated). No LT/ST mapping or parent-support notching applicable (structured obligation, not entity rating).
- **Definitions differing from generic/ICRA definitions**: Not applicable — this document contains no TOI/PBILDT/TNW/gearing definitions since it is a fund/structured-product rating methodology, not a corporate-entity methodology. "Capital protection" is specifically defined as NAV ≥ face value of the scheme at maturity (not at any interim point) — a definitional nuance ("These ratings do not comment on the volatility of NAV... or the level of NAV compared to the face value... at any time before maturity").
- **Mechanically-checkable thresholds**: (a) Minimum debt-instrument credit rating = 'AAA' (or equivalent/government securities) — hard bright line, codeable; (b) mandatory quarterly review cadence — codeable; (c) CPPI gearing/multiplier factor sizing rule is qualitative ("needs to be determined only after thoroughly projecting the gap risk factors") — not a numeric formula given in this document.

---

## Criteria_Hospital_Criteria_Paper.md

- **Scope**: Supplements CareEdge's generic services-sector methodology for hospital/healthcare-provider entities (primary/secondary/tertiary care segments). No numeric thresholds or exclusions stated; broad sector coverage of single- and multi-specialty hospital corporates.
- **Rating-factor structure**: Business Risk (Brand & Competitive Position; Scale & diversification — geographic, specialty-wise, domestic/international patient mix; Location analysis; Quality of cashflow — cash/TPA/institutional/CGHS payer mix; Operating performance — ARPOB, ALOS, occupancy ratio; Adequacy & Quality of Medical Team — doctor-per-bed ratio, payroll vs visiting doctor mix), Promoters/Management Analysis, Financial Risk (deferred to generic non-financial-sector ratio methodology), Project Risk, Regulatory Risk, ESG risk.
- **Indicative-metrics tables**: None with numeric thresholds — entirely qualitative/directional guidance (e.g., "hospitals in metro cities will have higher ARPOB compared to non-metro," "lower ALOS helps faster turnaround," no specific ARPOB/ALOS/occupancy percentage bands given).
- **Notching/support/mapping rules**: None present — no parent support, hybrid instrument, or LT-ST mapping content in this document (financial risk entirely deferred to the generic non-financial-sector methodology reference).
- **Definitions differing from generic/ICRA definitions**: None stated explicitly — no TOI/PBILDT/TNW/gearing sector-specific redefinition appears in this document. Defines sector-specific operating metrics only: ARPOB (average revenue realised per occupied bed), ALOS (average length of stay), "Doctor per bed" ratio — these are operational KPIs, not accounting/financial-statement definitions.
- **Mechanically-checkable thresholds**: None — the document contains no bright-line numeric cutoffs (all guidance is directional/qualitative, e.g., "an optimum level of doctor per bed is needed" without stating the number).

---

## Criteria_Manmade_Yarn_Manufacturing.md

- **Scope**: Supplements CareEdge's generic manufacturing-sector methodology for manmade (synthetic/cellulosic) yarn spinning companies — PSF/ASF/NSF/VSF fibre-to-yarn manufacturers. No explicit exclusions stated.
- **Rating-factor structure**: Business/Operational Risk (Operational Efficiency — raw material/power/labour cost; Inventory Management; Scale and Flexibility; Level of Integration — backward/forward; Geographical & Customer Diversification; Fiscal Incentives & Regulatory Risks), Financial Risk (Liquidity requirements; Capital structure and debt coverage indicators; Forex exchange risk analysis), ESG risk (Environmental, Social, Governance).
- **Indicative-metrics tables**: No numeric threshold table. Named ratios (list only, no bands): "long-term debt/tangible net worth; total-debt/tangible net worth; total debt/PBILDT; total outside liabilities/tangible net worth; PBILDT/Interest cost; Debt Service Coverage Ratio" — explicitly deferred in detail to CareEdge's "Financial Ratios—Non Financial sector" criteria document (not itself included in this batch).
- **Notching/support/mapping rules**: None present in this document.
- **Definitions differing from generic/ICRA definitions**: Confirms use of "tangible net worth" (not total net worth) as the denominator for leverage ratios (long-term debt/TNW, total debt/TNW, TOL/TNW) — consistent with generic ICRA/CareEdge convention of excluding intangibles, but this document does not itself detail revaluation-reserve treatment (deferred to the separate Financial Ratios criteria, not in this batch). No explicit gearing-inclusions (LC/acceptances) rule stated here — flagged as a gap: this sector document is silent on whether trade-related LC-backed creditors/acceptances/buyers' credit (common in a raw-material-import-heavy sector using PTA/MEG/wood pulp imports) are treated as debt for gearing purposes; ICRA-project analysts must rely on the separate Financial Ratios doc (not reviewed in this batch) for that definition.
- **Mechanically-checkable thresholds**: None — entirely a list of ratio names without numeric bands; "Companies... spend nearly 6%-7%..." (this appears in the pharma file, not here — see below). No bright-line cutoffs present in this document.

---

## Criteria_Rating Methodology - Organized Retail Companies January 2025.md

- **Scope**: Supplements CareEdge's generic services-sector methodology for organised retail companies (value retailing vs lifestyle retailing; specialty stores, department stores, supermarkets/hypermarkets, e-retail/omni-channel). No explicit numeric exclusions.
- **Rating-factor structure**: Promoter & Management evaluation, Industry analysis, Business risk (Market positioning — value vs lifestyle retailing; Diversification & competitive position; Store-level analysis — same-store sales growth, sales/sq ft, footfalls/conversion, average selling price/transaction size, shrinkage; Access to real estate/store ownership model; Supply chain infrastructure; Forex risk; Presence in e-retailing), Financial risk (Capital structure & financial flexibility; Inventory & working capital management; Operating cash flows & debt protection measures), ESG risk.
- **Indicative-metrics tables**: No numeric threshold table. Named ratios only (list, no bands): "Cash accruals against debt levels and other debt protection measures including interest coverage ratio, Debt/PBILDT, Debt service coverage and total debt/cash flow from operations."
- **Notching/support/mapping rules**: None present.
- **Definitions differing from generic/ICRA definitions — RELEVANT**: Explicitly names a debt-protection ratio "total debt/cash flow from operations" as a standard metric alongside PBILDT-based ratios (Debt/PBILDT, interest coverage) — confirming CareEdge DOES use a cash-flow-statement-based ratio (CFO) as a distinct, legitimate leverage/coverage metric for retail entities, separate from the P&L-based PBILDT ratios. This is directly relevant to the audit's "cash-flow figures substituted for P&L figures" error class: CareEdge's own methodology explicitly contemplates BOTH a PBILDT-based ratio and a CFO-based ratio as separate, named metrics — an ICRA-project error would arise if an analyst conflated the two (e.g., using CFO where PBILDT was called for, or vice versa) rather than computing both distinctly as this document requires. Also notes: "CareEdge Ratings also makes necessary adjustments to factor impact of IND AS-116 on 'leases'" (lease-liability adjustment to debt, consistent with the Auto Dealership file) and "CareEdge Ratings also analyses off-balance sheet exposures of the company and adjustments are made to the accounts, wherever necessary" (an explicit off-balance-sheet decomposition instruction).
- **Mechanically-checkable thresholds**: None numeric — no bright-line cutoffs stated (e.g., no specific leverage ratio band, no specific same-store-sales-growth threshold).

---

## Criteria_Rating Methodology Pharmaceutical Sector January 2025.md

- **Scope**: Supplements CareEdge's generic manufacturing-sector methodology for Indian pharmaceutical companies (bulk drug/API manufacturers, formulation manufacturers, integrated operations, CRAMS players). No explicit numeric exclusions.
- **Rating-factor structure**: (1) Business/Operational Risk — Business Segment & Product Portfolio (therapeutic segmentation: acute vs chronic; product portfolio depth/pipeline; formulation company classification: patented/branded-generic/generic; bulk drug/API cost efficiency and supplier concentration), Geographical Diversification (regulated vs semi-regulated export markets, ANDA filings), R&D Focus (R&D-to-sales trend), Manufacturing facilities & regulatory/legal compliance (GMP/GCP/GLP, DPCO/NLEM price control, Para-IV litigation risk); (2) Financial Position (deferred to generic non-financial-sector ratio methodology); (3) Project-specific Risk; (4) ESG risk.
- **Indicative-metrics tables**: No formal indicative-band table. One specific quantitative benchmark embedded in prose: "Generally, mid-to-large sized pharmaceutical companies in India spend nearly 6%-7% of their annual sales on R&D activities, thus companies having relatively higher R&D spend are generally expected to provide greater sustainability to business operations." Also a factual/context statistic (not a rating threshold): "From FY18-FY24, import of KSM and API from China accounts for nearly 66-68% of total imports of KSM/ API."
- **Notching/support/mapping rules**: None present in this document (no hybrid/parent-support/LT-ST mapping content specific to pharma).
- **Definitions differing from generic/ICRA definitions**: None explicit for TOI/PBILDT/TNW/gearing — financial risk entirely deferred to CareEdge's "Financial Ratio - Non-Financial Sector" methodology (not in this batch). No sector-specific redefinition of net worth or gearing appears here.
- **Mechanically-checkable thresholds**: The "6%-7% of annual sales on R&D" figure is a soft industry-average benchmark (not a rating cutoff, described as "generally"/"nearly") — usable as a comparison flag in code but not a strict pass/fail threshold. The "66-68% of imports from China" is a historical industry statistic, not a rating rule.

---

## Criteria_Rating_Methodology_Banks_March_2025.md

- **Scope**: Covers CareEdge's rating methodology for banks including scheduled commercial banks, Small Finance Banks (SFBs), and Regional Rural Banks (RRBs) — debt instruments of banks (FDs, CDs, infrastructure bonds, subordinated/Tier-II/AT-I bonds). Distinguishes RBI Basel III capital rules (SCBs excl. SFBs/RRBs) from separate SFB and RRB minimums.
- **Rating-factor structure**: Quantitative factors — (A) Capital adequacy, (B) Asset quality, (C) Resources, (D) Liquidity, (E) Earnings quality. Qualitative factors — (a) Industry profile/economic environment, (b) Ownership, (c) Management quality, (d) Risk management (incl. market risk, operational risk & digital capability), (e) Compliance with statutory requirements, (f) Accounting quality, (g) Size and market presence. Plus Seniority of rated facilities (FD/CD/infra bonds vs Tier-II) and ESG risk analysis.
- **Indicative-metrics tables** (verbatim):
  - Basel III capital regulations table:
    | With effect from | March 31, 2016 | March 31, 2017 | March 31, 2018 | March 31, 2019 | October 01, 2021 |
    |---|---|---|---|---|---|
    | Common equity Tier(CET)I ratio | 5.50% | 5.50% | 5.50% | 5.50% | 5.50% |
    | Tier-I capital adequacy ratio(CAR) | 7.00% | 7.00% | 7.00% | 7.00% | 7.00% |
    | Total CAR | 9.00% | 9.00% | 9.00% | 9.00% | 9.00% |
    | Capital conservation buffer(CCB) | 0.625% | 1.25% | 1.875% | 1.875% | 2.50% |
    | CET I Ratio(including CCB) | 6.125% | 6.75% | 7.375% | 7.375% | 8.00% |
    | Tier-I CAR(including CCB) | 7.625% | 8.25% | 8.875% | 8.875% | 9.50% |
    | CAR(including CCB) | 9.625% | 10.25% | 10.875% | 10.875% | 11.50% |
  - "The minimum CAR prescribed for SFBs by RBI is 15% with Tier-I CAR of 7.5% (under Basel II), while the minimum CAR prescribed for RRBs by RBI is 9% (under Basel I) and CCB and counter-cyclical buffer is not applicable for them."
  - Leverage ratio: "Leverage ratio is defined as Tier-I capital / total exposure (including on-balance sheet and off-balance sheet exposures adjusted for credit conversion factors). The guidelines prescribe minimum leverage ratio of 4.0% for domestic systemically important banks (D-SIBs), 3.5% for other banks, and 4.5% for SFBs."
  - SMA buckets: "SMA 0 - accounts overdue up to 30 days, SMA 1 – accounts overdue more than 30 days and up to 60 days, and SMA 2 – accounts overdue more than 60 and up to 90 days."
  - LCR: "banks need to maintain minimum LCR of 100% from April 01, 2021."
  - NSFR: "The NSFR should be equal to or at least 100% on an ongoing basis." NSFR = Available Stable Funding (ASF) / Required Stable Funding (RSF).
- **Notching/support/mapping rules**: "Infrastructure bonds and FDs are senior to Tier-II instruments. FDs are also protected up to a certain limit per depositor by Deposit Insurance and Credit Guarantee Corporation (DICGC)... Thus, the rating of FD programme may be higher by one notch compared to the Tier-II instruments of the bank." Cross-references a separate "Criteria for Rating Basel III – Hybrid Capital Instruments issued by Banks" for AT-I/Tier-II detail (not in this batch). Regulatory divergence disclosure rule: "banks are subject to supervision by RBI and are required to disclose divergence in asset classification and provisioning if the incremental provision required... exceeds the prescribed proportion of published net profit... and/or additional gross NPA assessed by RBI exceed prescribed proportion... High amount of divergences and its impact on the bank's financials is considered."
- **DEFINITIONS differing from generic/ICRA — HIGH RELEVANCE**:
  - Explicit rule that CareEdge does NOT factor rating-linked acceleration clauses into liquidity, mirroring the NBFC document.
  - Net worth cover concept for NPA: "The net worth cover that it has to absorb losses from the NPA which are unprovided for, is also examined" — i.e., unprovided NPA is compared against net worth (a specific, codeable ratio: (GNPA − provisions)/net worth).
  - Advances decomposition requirement: "The break-up of the advances book into wholesale/corporate advances and non-corporate advances, which in turn are divided into retail loans, agriculture loans and MSME loans, is also analysed" — an explicit decomposition-by-segment instruction (relevant to the "aggregate P&L/exposure not decomposed" error class, applied here to the loan book rather than P&L, but the same principle).
  - Earnings-quality decomposition: "CareEdge Ratings analyses the composition of a bank's income by segregating it into those generated from fund-based activities and fee-based activities... Core earnings are also identified by excluding non-recurring income from the total income" — same non-recurring-income exclusion principle as the NBFC document.
  - Accounting quality note: "The rating relies on the audited data... Suitable adjustments to reported figures are made for consistency of evaluation and meaningful interpretation" — general instruction, not a specific rule.
  - No specific TNW/gearing/net-worth-basis redefinition for banks (capital ratios use regulatory CET1/Tier1/CAR definitions per RBI, not a corporate TNW/gearing framework) — banks are NOT assessed on the corporate gearing/TOL-TNW framework at all; this is a structural difference from the corporate-sector methodologies that an ICRA-project analyst must not blur (i.e., never apply "gearing"/"TNW" logic to a bank rating — capital adequacy and leverage ratio, as defined by RBI, are the correct framework).
- **Mechanically-checkable thresholds**: Extensive and highly codeable — (a) full Basel III CAR/CET1/CCB glide path table by date; (b) SFB minimum CAR 15%, Tier-I 7.5%; (c) RRB minimum CAR 9%; (d) leverage ratio minima 4.0%/3.5%/4.5% (D-SIB/other/SFB); (e) SMA 0/1/2 day-bucket definitions (0-30/31-60/61-90 days overdue); (f) LCR minimum 100% from 1-Apr-2021; (g) NSFR minimum 100%; (h) FD/infra-bond-vs-Tier-II seniority = "may be higher by one notch" (a soft rule — "may," not "shall").

---

## Criteria_Rating_Methodology_City_Gas_Distribution_Companies_March_2025.md

- **Scope**: Covers CareEdge's rating methodology for City Gas Distribution (CGD) debt issuers, regulated by PNGRB — CNG (transport) and PNG-D/C/I (domestic/commercial/industrial) segments. No explicit numeric exclusions.
- **Rating-factor structure**: Business Risk (Demand analysis of GAs — geographic-area demand drivers by segment; Supply analysis of natural gas/APM allocation; Consumer mix), Industry Risk (Pricing/cost competitiveness vs alternative fuels; Competition from third parties post-exclusivity; Regulatory risk), Financial Risk (deferred to generic non-financial-sector ratio methodology — solvency/debt coverage), Project Risk (Approval & execution risk; Financial closure; Infrastructure development/Minimum Work Programme), Promoter/Management Risk, ESG risk.
- **Indicative-metrics tables**: No numeric indicative-band table. Named benchmark ratios (list only, no bands): "The profit before interest, lease rentals, depreciation and taxation (PBILDT) margin, spreads/standard cubic metre (SCM) and PBILDT/SCM are used as standard benchmarks to evaluate the margins of a CGD company against its peers." Debt-coverage metrics named: "total debt position against level of gross cash accruals (GCA) and PBILDT."
- **Notching/support/mapping rules**: Regulatory/structural rules (not rating notching per se): "CGD entities have a 5-year marketing exclusivity and 25-year infrastructure exclusivity from the date of authorisation... from the 9th CGD bidding round, the market exclusivity is increased from five years to eight years, which is further extendable up to two years based on physical performance." No parent-support/hybrid/LT-ST content in this document.
- **Definitions differing from generic/ICRA definitions**: PBILDT explicitly defined as "profit before interest, lease rentals, depreciation and taxation" — note the inclusion of "lease rentals" being added back alongside interest, consistent with IND-AS 116 lease-capitalization treatment seen in the Auto Dealership and Retail documents (a CareEdge-wide convention, not unique to CGD). No explicit TNW/gearing redefinition in this document — deferred to the generic Financial Ratios criteria (not in this batch). Net-worth reference for project sizing only: "the magnitude of the project against the net worth/asset size of the entity" (qualitative, no ratio defined).
- **Mechanically-checkable thresholds**: (a) Marketing exclusivity = 5 years (or 8 years from 9th CGD bidding round, extendable up to 2 more years based on physical performance) — bright-line, codeable; (b) infrastructure exclusivity = 25 years from authorisation date — bright-line, codeable. No numeric financial-ratio thresholds are given in this document (PBILDT/SCM, Debt/GCA are named metrics without stated bands).

---

## Summary of Cross-Cutting Findings Relevant to the ICRA-Project Audit

1. **PBILDT/EBITDA "add back lease rentals" convention** appears consistently across Auto Dealership, Organized Retail, and City Gas Distribution documents — all reference IND-AS 116 lease capitalization, treating lease payments as part of interest cost and lease liabilities as part of adjusted debt. This is a CareEdge-wide, cross-sector convention, not sector-specific, and any ICRA-project ratio engine handling CareEdge-referenced companies must apply it consistently.
2. **Explicit CFO-based ratio alongside PBILDT-based ratio** is named in the Organized Retail document ("total debt/cash flow from operations" as a distinct metric from "Debt/PBILDT") — confirms CareEdge legitimately uses both P&L-based and cash-flow-based leverage/coverage ratios as SEPARATE named metrics; the known ICRA-project error of "cash-flow figures substituted for P&L figures" would arise from conflating these two distinct, correctly-named ratios rather than computing each as its own line item.
3. **Explicit decomposition instructions** recur in the NBFC document (income by fee-based/fund-based; core earnings by excluding non-recurring income; advances book by segment) and the Banks document (advances by wholesale/retail/agri/MSME; income by fund-based/fee-based) — these are the CareEdge-side counterpart to the ICRA-project's "aggregate P&L notes not decomposed" error class, confirming the agency's own methodology mandates segment-level decomposition that a mechanical/aggregate extraction would violate.
4. **AUM-based leverage/asset-quality gross-up for NBFCs** (explicit formula: AUM = on-balance sheet advances + off-book securitisation + co-lending + business correspondent) is a specific, codeable rule that a purely balance-sheet-debt-based gearing calculation would miss for NBFCs with securitisation/co-lending books.
5. **Group-exposure-adjusted TNW** for NBFCs (deduct significant group exposure from tangible net worth before computing adjusted leverage) is a specific net-worth-basis adjustment rule directly analogous to the "wrong net-worth basis" error class flagged in the audit brief.
6. **No document in this batch explicitly addresses LC-backed creditors/acceptances/buyers' credit treatment in gearing** — this specific definitional question is deferred in every sector document to the separate "Financial Ratios – Non-Financial Sector" (or "Financial Sector") criteria documents, neither of which was in this 10-file batch. This is a gap worth flagging: the acceptances/LC-treatment question central to the audit's error thesis is NOT answered by any of these 10 files and must be sourced from the Financial Ratios criteria documents specifically.
7. **Banks are NOT assessed on corporate TNW/gearing framework at all** — capital adequacy (CET1/Tier1/CAR per RBI/Basel III) is the sole leverage-type framework; applying corporate gearing logic to a bank would be a methodology-scope violation (paralleling the ICRA-project's known "scope-mismatched methodology citation" failure mode).

# CareEdge Methodology Corpus Review — Part 3

Source directory: `CareEdge/Methodology/`. All 10 files read in full via Read tool (each fit within a single read; no truncation encountered).

---

## Criteria_Rating_Methodology_Construction_Sector_March_2025.md

- **Scope:** Applies to entities in the engineering, procurement and construction (EPC) space (civil infrastructure, industrial infrastructure, real estate construction contractors). Explicitly layered "over and above the broad corporate rating methodology" — i.e., supplements, does not replace, the general corporate/manufacturing methodology. Cross-refers to CareEdge's Manufacturing Companies methodology for management evaluation detail.
- **Rating-factor structure:** A. Management evaluation; B. Business/Operation risk (1. Evaluation of past projects executed, 2. Order book analysis [a. Diversity/credit quality of counterparty, b. Revenue visibility, c. Resource availability/execution capacity], 3. Scale of operations, 4. Profitability trend, 5. Working capital management); C. Financial risk (1. Capital structure and coverage indicators [a. Debt profile, b. Debt coverage indicators], 2. Off-balance sheet exposures, 3. Liquidity assessment and financial flexibility, 4. Exposure to PPP-model projects); D. Industry risk; ESG (Environmental/Social/Governance).
- **Indicative-metrics tables:** None — this document contains no numeric threshold table (no scorecard/band table with cutoffs). All guidance is qualitative/directional (e.g., "high order book to sales ratio may be a constraint," no numeric bands given).
- **Notching/support/mapping rules:** No LT-ST mapping or outlook table. Parent/SPV support: for PPP/BOT/hybrid-annuity exposures, "CareEdge Ratings may undertake moderate consolidation based on the financial linkages" and makes "suitable adjustments... in the leverage and coverage ratios considering the execution risk... guarantees extended, sponsor commitment... and cash inflow/outflow estimations." Contingent liabilities in the form of corporate guarantees "are treated as debt of the entity being rated depending upon whether the guaranteed entity is in a position to repay its debt."
- **Definitions differing from generic:**
  - **Gearing/debt inclusions (directly relevant to the audit's LC/acceptance question):** "CareEdge Ratings considers advances backed by financial guarantee as a part of working capital debt for its analysis" — i.e., interest-free/interest-bearing mobilisation advances backed by a bank guarantee are added into working-capital debt, not excluded as trade-type liability.
  - Beyond debt-equity and overall gearing, CareEdge additionally uses **TOL/TNW** (total outside liabilities to tangible net worth) as a leverage metric specific to construction (because a large part of funding runs through creditors/sub-contractor back-to-back arrangements).
  - **Working capital / GCA days definition:** Collection period computation deliberately includes **retention money (including retention money not due) and unbilled revenue/contract asset** as part of debtors "so that a realistic operating cycle is arrived at" — i.e., broader than a simple trade-receivables definition. GCA days also gets "advance income/unearned income forming part of contract liability" adjusted against it.
  - **DSCR definition:** "adjusted for internal accruals commited [sic] for capex and investment commitments/support to be extended to SPVs sponsored by the entity" — a company-specific adjustment layer on top of the standard DSCR.
  - Fixed asset turnover (FAT) defined specifically as TOI / average gross block.
- **Mechanically-checkable bright-line rules:** None with hard numeric cutoffs; this document is qualitative throughout (no "gearing < Xx" or "coverage > Yx" bands are given for construction specifically — those live in the cross-referenced Financial Ratios methodology, not reproduced here).

---

## Criteria_Rating_Methodology_Debt_Backed_by_Lease_Rentals_Discounting_Feb_2025.md

- **Scope:** LRD (lease rental discounting) loans — debt secured against future rental cash flows from leased commercial/retail/warehouse real estate. Applies "over and above" the Real Estate projects methodology where a developer does both sale and lease projects. Also covers REITs by cross-reference to CareEdge's separate REIT methodology, used "in conjunction with this methodology."
- **Rating-factor structure:** A. Management evaluation (promoter experience, past leasing track record, entity constitution, org structure/group support); B. Business risk evaluation (execution risk in project-stage entities, location/construction quality, market standing & demand-supply outlook, occupancy levels, tenant profile assessment, lease agreement/renewal risk); C. Financial risk evaluation (debt financing & sanction terms, refinancing risk, leverage & financial flexibility, cash flow analysis, availability of liquid balances); plus REIT-specific note; ESG.
- **Indicative-metrics tables:** No numeric threshold/band table. Only qualitative/rule-of-thumb figures embedded in prose:
  - DSRA "equivalent to **one to three months** of instalments is maintained by the companies in accordance with sanction terms" (a range, not a hard cutoff, and stated as typical market practice rather than a CareEdge pass/fail band).
- **Notching/support/mapping rules:** No explicit LT-ST/outlook table in this doc. Group/parent linkage handled via cross-reference to "CARE Ratings' criteria on notching by factoring linkages." No hybrid-instrument notching here (not applicable to LRD structures).
- **Definitions differing from generic:**
  - **Debt to rental** ratio = years to repay entire debt at average annuity income (debt / rental income) — sector-specific leverage metric distinct from standard TD/TNW gearing.
  - **Cash coverage ratio (CCR):** entire cash inflows (debt drawdown + lease rentals + parking charges + other property income) plotted against operational expenses, refundable-security-deposit outflow on vacancy, and projected capex, to arrive at available cash for debt repayment; CCR is also computed "with inclusion of opening cash balance/accumulated surplus." This is explicitly a cash-flow-statement-style ratio (not a P&L-based ratio), by design, appropriate to this asset-backed structure — but flags the general principle in the audit brief that CareEdge sometimes deliberately builds ratios off projected cash inflows rather than P&L, which must not be confused with an operating-company's OPBDIT/PBILDT based ratios.
  - **WALE (weighted average lease expiry)** compared against average maturity of residual debt — a structural coverage-style metric unique to lease-backed debt.
  - No net-worth/TNW redefinition specific to this doc (net worth of SPV noted as "normally low" given SPV structure, driving higher gearing, but no numeric net-worth adjustment rule given here).
- **Mechanically-checkable bright-line rules:** DSRA "one to three months" range; none of these are strict pass/fail cutoffs (all descriptive of typical structuring, not rating bands) — nothing here rises to a hard numeric threshold worth coding as a gate.

---

## Criteria_Rating_Methodology_Financial_Ratios_Financial_Sector_February_2025.md

- **Scope:** Applies to banks, financial institutions, NBFCs and HFCs — the financial-sector counterpart to the (separate, non-financial) Financial Ratios methodology. Purely a ratio-definitions reference document (no business/industry-risk narrative) — this is the document Steps 5/6/32 of the ICRA agent's SOP point to for financial-sector conventions.
- **Rating-factor structure:** Five ratio categories: A. Growth Ratios; B. Capital Adequacy and Leverage; C. Asset Quality Ratios; D. Earnings Ratios; E. Liquidity Ratios. Not a scored-factor framework — a ratio glossary with formulas.
- **Indicative-metrics tables (verbatim, this is the highest-value document in this batch for exact formulas):**

  **A. Growth Ratios**
  | Ratio | Formula |
  |---|---|
  | Growth in Interest Income | [Interest Income(t) − Interest Income(t-1)] / Interest Income(t-1) × 100 |
  | Growth in PAT | [PAT(t) − PAT(t-1)] / PAT(t-1) × 100 |
  | Growth in Loan Portfolio/AUM | [AUM(t) − AUM(t-1)] / AUM(t-1) × 100 |
  | Growth in Deposits | [Deposits(t) − Deposits(t-1)] / Deposits(t-1) × 100 |
  | Growth in CASA Deposits | [CASA(t) − CASA(t-1)] / CASA(t-1) × 100 |

  **B. Capital Adequacy and Leverage**
  | Ratio | Formula |
  |---|---|
  | Overall CAR | [Tier-I + Tier-II Capital] / Risk Weighted Assets (as reported to RBI/NHB) |
  | Tier-I CAR | Tier-I Capital / RWA |
  | CET-1^ | CET-1 Capital / RWA |
  | Overall Gearing Ratio | Total Debt / **Tangible Net Worth** |
  | CASA Ratio^^ | (Demand deposits + Savings deposits) / Total deposits |
  | CASA to Liabilities^^ | (Demand + Savings deposits) / (Total deposits + Borrowings) |
  | Credit/Deposit^^ | Total advances / Total deposits |
  | Interest Coverage* | PBILDT / (Total interest & finance charges − Amortisation of premium on Debentures − Interest capitalised) |
  | AUM/Net worth | AUM / Tangible Net worth |

  (*specific to non-lending financial institutions; ^Basel III banks; ^^banks only)

  **C. Asset Quality Ratios**
  | Ratio | Formula |
  |---|---|
  | Gross NPA Ratio | Gross NPA / Gross Advances (per RBI/NHB classification) |
  | Net NPA Ratio | Net NPA / Net Advances |
  | Net NPA/Net worth | Net NPA / Tangible Net worth |
  | Provision Coverage Ratio | Provisions for NPA / Gross NPA |
  | Net Stressed Asset Ratio | (Net NPA + Net Restructured Assets + Net SRs) / Net worth |
  | Write-off ratio | Net write-off (P&L) / Gross Advances or Loan Portfolio |
  | Slippages ratio | Addition to NPAs / Opening standard advances/portfolio |

  (Footnote: under Ind AS, Gross/Net Stage 3 may be substituted for Gross/Net NPA.)

  **D. Earnings Ratios**
  | Ratio | Formula |
  |---|---|
  | ROTA | PAT / Average Total Assets |
  | ROMA | PAT / (Avg Total Assets + Avg Off-book Portfolio) |
  | RONW | PAT / **Avg. Tangible Net worth** |
  | Interest Spread | (Interest Income/Avg Interest Earning Assets) − (Interest Expense/Avg Interest Bearing Liabilities) |
  | Net Interest Margin | Net Interest Income / Avg Total Assets; NII = Interest Income − Interest Expense |
  | Cost to Income | Operating Expenses / (Total Income − Interest Expense) |
  | Operating Cost/Avg Total Assets | Operating Expenses / Avg Total Assets |
  | Other Income/Avg Total Assets | Other Income / Avg Total Assets |
  | Credit Cost | Provisions & Write-offs (P&L) / Avg Total Assets |
  | Yield on Advances | Interest Income / Avg Advances |
  | Cost of Borrowing | Interest Expenses / Avg Borrowings |

  **E. Liquidity Ratios**
  | Ratio | Formula |
  |---|---|
  | LCR (per RBI) | High Quality Liquid Assets / Net cash outflows for next 30 days |
  | Immediate coverage (NBFC/HFC, months) | Liquid assets / Debt obligations for next 12 months per ALM statement |
  | Cash flow debt coverage | (Highly liquid assets + scheduled inflows from credit assets next 12m) / Scheduled cash outflows next 12m |

  **Regulatory single-issuer investment caps** (quoted under a related methodology but the exact SEBI-defined single-issuer thresholds — 10%/8%/6% — are reproduced in the Fund CQR document below, not here.)

- **Notching/support/mapping rules:** Not applicable (pure ratio glossary) — no LT-ST or outlook table here.
- **Definitions differing from generic (CENTRAL to the audit's stated failure modes):**
  - **Total Debt (financial sector):** includes all ST and LT debt, **redeemable preference share capital**, optionally convertible debentures, FCY loans, fixed deposits, unsecured loans, CP, inter-corporate borrowings, promoter/associate/group borrowings, **and guarantees extended by the entity (including corporate guarantees for securitisations)** — guarantees are explicitly added to total debt for financial-sector entities.
  - **Hybrid instrument treatment (exact rules, verbatim table):**
    - Redeemable Preference Shares → treated as **debt** (fixed tenure + fixed dividend).
    - Compulsorily Convertible Instruments → treated as **quasi-equity/net worth**, UNLESS the terms give an investor exit option or conditional conversion, in which case treated as **debt**.
    - Optionally Convertible Instruments (OCPS/OCDs) → treated as **debt** (redemption not ruled out until actually converted).
    - Tier II Bonds (banks/HFC/NBFC) → treated as **debt** for gearing (despite Basel III capital-treatment as Tier II), including PONV write-down feature, treated at par with old Lower Tier II.
    - Basel III AT1 Bonds → treated as **debt** despite loss-absorption/coupon-discretion/perpetual features.
    - Upper Tier II / Innovative Perpetual Debt (Basel II banks) → treated as **debt** for leverage despite capital-adequacy treatment.
    - Perpetual Debt Instruments (NBFC/HFC) → treated as **debt** despite subordination to all other creditors.
  - **Tangible Net Worth (financial sector) — exact composition, differs materially from a naive "shareholders' equity" figure:**
    - INCLUDES: equity share capital, all reserves & surplus **excluding revaluation reserve and reserve for bad and doubtful debt**, equity share warrants, share application money, ESOPs outstanding, minority interest (consolidated), and **compulsorily convertible instruments** (per the quasi-equity rule above).
    - DEDUCTS: miscellaneous expenditure not written off, accumulated losses, **revaluation reserves** (explicitly excluded), and **Deferred Tax Assets net of DTL** ("CARE Ratings subtracts DTA (net of DTL) from the company's net worth").
    - Intangibles treatment: stated to be "similar to what CARE Ratings follows for the non-financial sector" (i.e., cross-referenced, not restated numerically here — this is the ICRA project's own CLAUDE.md failure-mode-32 point: financial-sector TNW deducts DTA, the corporate TNW convention does not).
  - This is the single most load-bearing document in this batch for the audit's stated wrong-net-worth-basis / wrong-gearing-inclusion failure class, because it gives EXACT, auditable rules (revaluation reserve exclusion, DTA netting, guarantee-as-debt, hybrid-instrument debt/equity split) that a mechanical check could directly enforce.
- **Mechanically-checkable bright-line rules:**
  - TNW = equity + reserves (ex-revaluation, ex-bad-debt-reserve) + warrants + share-app-money + ESOP + minority interest + compulsorily-convertible instruments − misc. exp. not written off − accumulated losses − DTA(net of DTL). This is a fully codeable formula.
  - Total Debt = all ST/LT debt + redeemable pref shares + all hybrid instruments EXCEPT compulsorily convertible ones + guarantees extended (incl. securitisation corporate guarantees).
  - Gross/Net NPA ratio denominators are "per RBI/NHB Classification" — a codeable rule (use regulatory classification, not company's own stage bucketing, unless Ind AS Stage 3 substitution note applies).

---

## Criteria_Rating_Methodology_Fund_Credit_Quality_Rating_March_2025.md

- **Scope:** CareEdge's Fund Credit Quality Rating (CQR) — an opinion on a debt mutual fund/ETF scheme's overall portfolio credit quality (default risk), NOT a recommendation to buy/sell/hold, NOT an opinion on AMC management practices, NAV volatility/yield, or liquidity/market/sectoral risk. Applies to debt mutual fund schemes and debt ETFs only.
- **Rating-factor structure:** Not a multi-factor scorecard; based on (1) a proprietary Credit Scoring Matrix applied per-security (credit score = f(credit rating, residual maturity, put-option-adjusted where applicable)), (2) portfolio-level weighted-average credit score (weighted by exposure %), (3) concentration-factor overlay, (4) ongoing monitoring/curing-period mechanics.
- **Indicative-metrics tables:** No published numeric score table (the credit scoring matrix itself, mapping rating+maturity to a score, is proprietary and not reproduced with numbers in this document — it is described only conceptually: "credit score is lower for higher ratings and vice versa").
- **Notching/support/mapping rules:**
  - Short-term CQR scale eligibility conditions (bright-line, quotable): (1) **all** holdings must have **residual maturity of less than one year**; (2) fund's mandate is to invest predominantly in short-term debt securities.
  - Rating basis: "latest three months' portfolio" analysed to arrive at the credit score.
  - Securities rated by other CRAs but not CareEdge: **lowest rating assigned by other CRAs** used as a guide (unless CareEdge forms an internal deviating view).
  - Negative watch/outlook securities: portfolio score is stressed by "appropriately notched down rating" — the notch-down quantum is not specified numerically.
  - **SEBI single-issuer concentration limits reproduced verbatim: 10% of fund's NAV for AAA-rated securities, 8% for AA-rated, 6% for A-and-below-rated.** Breach of these limits triggers use of a notched-down rating's score, or a higher credit score for the excess exposure.
  - **Curing period: one month** to realign the fund score to the benchmark once breached (may be waived if realignment is judged unlikely).
  - **Write-off/default treatment:** a write-off is NOT treated as portfolio realignment; the downgraded/defaulted rating continues to be applied to the entire par value "for at least **six months** from the date of complete write-down... or till full redemption/sale, whichever is earlier."
  - Post-downgrade of the scheme's own rating: CareEdge monitors for at least **three months** before reassessing based on the revised portfolio.
- **Definitions differing from generic:** N/A (no TOI/PBILDT/TNW/gearing definitions here — different rating object entirely, portfolio credit-quality not issuer credit-quality).
- **Mechanically-checkable bright-line rules (multiple, exact numeric cutoffs — high value for a code check, though NOT relevant to the corporate/manufacturer rating-tool failure the audit is investigating, since this methodology applies only to debt mutual fund schemes):**
  - Short-term scale eligibility: 100% of holdings residual maturity < 1 year.
  - SEBI concentration thresholds: 10% (AAA) / 8% (AA) / 6% (A & below) of NAV per single issuer.
  - Curing period: 1 month.
  - Write-off score-carry period: minimum 6 months (or full redemption/sale if earlier).
  - Post-downgrade monitoring period before relook: 3 months.

---

## Criteria_Rating_Methodology_Hotel_Industry_Feb_2025.md

- **Scope:** Entities in the hotel/hospitality sector, layered "over and above" the broader Services Sector methodology. Covers owned/leased/franchised/managed business models, greenfield/brownfield hotel projects.
- **Rating-factor structure:** A. Promoters/Management Analysis (incl. parent/group linkage per Notching methodology); B. Industry Risk Analysis (i. Regional demand-supply & cyclicality [demand, supply, cyclicality], ii. Competition); C. Business Risk Analysis (i. business model evaluation [owned/leased/franchised/managed], ii. location analysis, iii. brand strength & competitive position, iv. scale, v. revenue diversification [mixed-use properties, geographical, segmental — luxury/mid-scale/economy], vi. operational performance [ARR, OR, RevPAR]); D. Project Risk (i. timing vs industry cycle & project viability, ii. funding risk); E. Financial Risk Analysis (i. Leverage and Debt Servicing); F. ESG.
- **Indicative-metrics tables:** None — entirely qualitative/narrative, no numeric bands for ARR/OR/RevPAR/leverage. Cross-refers to the (non-financial) Financial Ratios methodology for ratio detail rather than restating numbers.
- **Notching/support/mapping rules:** No LT-ST/outlook table in this document. Parent/group linkage handled by cross-reference to the Notching-by-linkages methodology only.
- **Definitions differing from generic:**
  - **Leverage/total debt inclusion:** "While computing the leverage, CareEdge Ratings also factors in the **lease liabilities as part of total debt**" — explicit inclusion of lease liabilities in gearing for hotel entities (relevant given many hotels operate leased-model properties).
  - Sector-defining operating metrics named explicitly: **ARR (average room rate), OR (occupancy rate), RevPAR (revenue per available room)** — RevPAR is described as "a derivation of ARR and occupancy levels."
  - No numeric net-worth/TNW redefinition specific to hotels (defers to general Financial Ratios methodology).
- **Mechanically-checkable bright-line rules:** None with a hard numeric cutoff. The lease-liabilities-in-debt inclusion rule is a qualitative but structurally important, auditable rule (a code check could flag if lease liabilities were omitted from a hotel-sector debt figure) — this is the sector's single most consequential definitional rule for the audit's stated "wrong gearing inclusions" failure class, though it concerns leases rather than LC-backed acceptances specifically.

---

## Criteria_Rating_Methodology_Housing_Finance_Companies_March_2025.md

- **Scope:** Applies to companies registered as Housing Finance Companies (HFCs) with NHB/RBI. Covers standalone assessment; parent/promoter linkage handled via separate Notching methodology. Also covers subordinated debt and perpetual debt instruments issued by HFCs.
- **Rating-factor structure (named, matches an 8-box chart in the source):** 1. Business Mix (retail vs wholesale, housing vs non-housing); 2. Capital and Leverage; 3. Asset Quality; 4. Profitability; 5. Liquidity; 6. Resource Profile; 7. Management and Systems; 8. Size, Vintage and Market Presence. Plus Additional Considerations (Peer group analysis, Market-based indicators) and separate criteria sections for Subordinated Debt and Perpetual Debt Instruments, plus ESG and Accounting Quality sections.
- **Indicative-metrics tables:** No numeric threshold table for the 8 factors (all qualitative/directional — e.g. "relatively higher leverage is acceptable for granular... prime retail home loans" vs "lower leverage may be warranted" for concentrated/wholesale books — no numeric gearing cutoffs given). One structured non-financial table for PDI features (see below).

  **Perpetual Debt Instruments (PDI) of NBFC/HFC — feature table (verbatim):**
  | Feature | Rule |
  |---|---|
  | Maturity Period | Perpetual maturity |
  | Options | Embedded 'Call' option only after instrument has run ≥ 10 years from issue; call requires prior RBI approval |
  | Lock-in clause | HFC may defer interest if CRAR is below regulatory minimum, or if payment would push CRAR below/keep it below the minimum |
  | Interest payment | Requires prior RBI approval if payment would cause/increase net loss, provided CRAR stays above the norm |
  | Claim seniority | Superior to equity shareholders; subordinate to all other creditors |
  | Capital treatment | PDI eligible as Tier-I capital up to **15% of total Tier-I capital**; excess over 15% qualifies as Tier-II |

- **Notching/support/mapping rules:**
  - **PDI notching rule (bright-line, quotable): "such instruments are generally notched down by at least one notch than the rating of senior debt"** given the lock-in clause's sensitivity to CAR/capital-raising ability/profitability over the instrument's long tenure.
  - **Subordinated debt of HFCs:** CareEdge "generally does not differentiate between the rating of senior and subordinated debt" of an HFC (unlike PDI) — reasoning: servicing is purely cash-flow driven in a going concern, no regulatory restriction on servicing, and subordination only matters in liquidation (affects LGD, not PD) — "the long-term probability of default for Senior and Subordinated Debt... are similar and the same should reflect in their long-term ratings." However, CareEdge "may choose to differentiate... on a case-to-case basis."
  - PDI lock-in triggering an interest/principal delay is explicitly defined as "an event of default per CareEdge Ratings' definition of default."
  - No numeric LT-ST mapping table in this document (defers to general/cross-cutting policy elsewhere).
- **Definitions differing from generic:**
  - **Capital adequacy adjustment:** "CareEdge Ratings adjusts the net worth for **investments in subsidiaries and other non-core activities** while assessing the adequacy of an HFC's risk capital" — a deduction not present in the plain corporate TNW definition.
  - **AUM treatment:** For HFCs doing direct assignment/securitisation, CareEdge assesses leverage/asset quality/profitability on an **AUM basis by treating off-balance-sheet assets as on-balance-sheet** — i.e., securitised/assigned exposures are added back for ratio purposes rather than excluded because they left the balance sheet.
  - **Core earnings / profitability:** profitability analysis explicitly "excludes non-recurring income from total income" to identify core earnings — a normalisation rule directly relevant to the audit's "aggregate P&L notes not decomposed" concern (this methodology explicitly REQUIRES the decomposition CareEdge expects, of fee-based vs fund-based, recurring vs non-recurring income).
  - **NPA seasoning adjustment:** for HFCs with short track record / aggressive loan growth, CareEdge "analyses the NPA levels on a **lagged basis**, which adjusts the growth of the loan book" — i.e., a growth-adjusted delinquency metric rather than a raw point-in-time GNPA%.
  - **Liquidity:** contractual short-term liabilities (CP, ST loans) are explicitly "not assumed to be rolled over" when assessing the ALM/liquidity cover — a conservative assumption rule.
  - **Rating-linked acceleration clauses:** CareEdge's liquidity assessment explicitly "does not consider the presence of such rating-linked acceleration clauses" even though it acknowledges these can cause severe real-world liquidity stress upon a downgrade trigger — an explicit methodological choice to exclude a real risk factor from the base liquidity assessment (flagged as a caveat within the document itself).
- **Mechanically-checkable bright-line rules:**
  - PDI Tier-I capital cap: 15% of total Tier-I capital (excess → Tier-II).
  - PDI call option: only exercisable after ≥10 years from issuance, and only with prior RBI approval.
  - PDI notching: minimum one notch below senior debt.
  - Net worth for capital-adequacy purposes = reported net worth − investments in subsidiaries/non-core activities (a codeable deduction, distinct from the generic TNW formula in the Financial Ratios – Financial Sector document).

---

## Criteria_Rating_Methodology_Infrastructure_Investment_Trusts_(InvITs)_March_2025.md

- **Scope:** Rating of **consolidated debt** of an InvIT (Infrastructure Investment Trust) — an opinion on the InvIT's capacity to repay debt timely. Explicitly NOT a rating of InvIT units, NOT an opinion on returns/yield/NAV performance, NOT an assessment of individual underlying asset credit quality, and does not cover fundamental law/regulatory change, disruptive-technology demand shifts, or extreme/force-majeure events (terrorism, long-term climate effects, etc. — explicitly excluded from scope).
- **Rating-factor structure:** (a) Business risk — cash flows of underlying assets (assessed via the relevant SEBI-registered sector-specific CareEdge methodology per asset class: toll roads, power transmission, solar/wind, seaports, airports); (b) Financial risk; (c) Management risk; (d) Regulatory risk.
- **Indicative-metrics tables (regulatory/structural parameters, verbatim — SEBI-sourced, reproduced by CareEdge as a reference table):**
  | Particular | Threshold |
  |---|---|
  | Public InvIT minimum investment in revenue-generating infra assets | ≥80% of InvIT asset value |
  | Minimum distribution to unit holders | ≥90% of net distributable cash flows |
  | Aggregate consolidated borrowings + deferred payments (net of cash) | Capped at **49%** of asset valuation generally; capped at **70%** for AAA-rated entities with track record of **six continuous distributions** |
  | Frequency of distribution | Minimum once every half-year (public InvITs) / once a year (private InvITs) |
  | Mandatory credit rating trigger | Required once consolidated borrowings + deferred payments (net of cash) **exceed 25%** of asset value |
  | Sponsor lock-in | 3 years for minimum 15% stake; 1 year for holding in excess of 15%; 1-year lock-in for strategic investor |
  | Minimum sponsor unitholding | 15% collectively, for not less than 3 years post-issue |
  | Subordinate unit → ordinary unit minimum gap | Minimum 3 years between issuance and "entitlement date" |
  | InvIT/holdco minimum SPV equity/interest | InvIT must hold ≥51% controlling interest in SPVs (or ≥26% ultimate interest via a two-level holdco structure holding ≥51% of the SPV) |
  | Valuation frequency | Full valuation at least once/year (within 2 months of FY-end); half-yearly valuation for period ending Sept 30, completed within 1 month |

- **Notching/support/mapping rules:**
  - Homogeneous assets under one InvIT are assessed on a **pooled cash-flow basis** using the applicable sector-specific methodology (unless SPV cash-flow fungibility restrictions apply, in which case excluded from pooling); heterogeneous assets are assessed **SPV-by-SPV** using the respective sector methodology.
  - No explicit LT-ST mapping table or notch quantum given for sponsor support (only qualitative — "strong sponsor will have higher financial flexibility").
- **Definitions differing from generic:**
  - **Leverage treatment differs by asset class**: "Lower overall gearing is seen positively for **toll roads**, whereas for **annuity and transmission projects** with stable and predictable cash flow... tend to mitigate the high gearing to an extent, provided the counterparty making annuity payments is strong" — i.e., an explicit sector-conditional relaxation of the leverage penalty, contingent on counterparty credit strength.
  - **DSCR is computed at both SPV level and InvIT (consolidated) level** where debt sits at the SPV; CareEdge also separately evaluates the "extent of distress/need-based support to weaker SPVs."
  - No TOI/PBILDT/TNW-specific redefinition in this document (defers entirely to the underlying sector methodology for each asset class).
- **Mechanically-checkable bright-line rules:**
  - Leverage cap 49% of asset value (general) / 70% (AAA-rated + 6 continuous distributions) — hard SEBI-sourced numeric cutoffs, directly codeable.
  - Mandatory-rating trigger at >25% leverage (net of cash) of asset value.
  - Distribution minimum 90% of net distributable cash flow, at least half-yearly (public) / yearly (private).
  - Sponsor minimum holding 15% for ≥3 years; SPV minimum controlling stake ≥51% (or ≥26% ultimate via holdco).

---

## Criteria_Rating_Methodology_Manufacturing_Companies_March_2025.md

**This is the methodology closest to the failed synthetic-rutile manufacturer case.**

- **Scope:** General manufacturing entities. Explicitly stated as the base/generic methodology: "This methodology covers factors considered while assessing credit risk of a general manufacturing entity. For sector-specific methodologies, please refer to CareEdge Ratings' website" — i.e., it is meant to be supplemented by a sector-specific overlay (e.g., Paper, per the last file in this batch) where one exists, but stands alone for entities with no dedicated sector methodology (as would be the case for a synthetic-rutile / mineral-processing manufacturer, absent a dedicated CareEdge mining/minerals-processing methodology).
- **Rating-factor structure (top-level, from the source's own risk-framework chart plus body text):**
  - Industry Risk (Industry Characteristics, Industry Financials, External Risk)
  - Business Risk (Market Position, Track Record, Operating Efficiency, Strategic Initiatives, Crisis Management) — sub-factors in body text: Diversification; Seasonality and Cyclicality; Size, Market Share and Competition; Earnings Capacity; Cost Structure and Operating Efficiency; Force Majeure events.
  - Financial Risk (Existing Financial Position, Cash-flow Adequacy, Financial Flexibility, Accounting Quality) — sub-factors: Accounting Quality; Financial Ratios (Growth, Profitability, Leverage & Coverage, Turnover & Liquidity — cross-referenced to the separate non-financial Financial Ratios methodology, not restated numerically here); Cash Flows; Liquidity; Financial Flexibility; Validation of Projections and Sensitivity Analysis; Working Capital Analysis (Debtors, Inventory, Creditors); Contingent Liabilities; Foreign Exchange Risk Analysis.
  - Management Evaluation (Track Record, Corporate Strategy, Legal Constitution & Ownership Pattern, Performance of Group Concerns, Organisational Structure, Control Systems, Personnel Policies, Corporate Governance).
  - Project Risk Analysis (for entities with planned capex).
  - ESG (Environmental, Social, Governance).
  - **No numeric factor-weighting or scoring table is given anywhere in this document** — despite the graphical framework chart depicting Industry/Business/Financial/Management/Internal Risk as boxes, there are no percentage weights, point allocations, or a scorecard assigning relative importance across scale/profitability vs leverage/coverage. The methodology is entirely qualitative/narrative in its description of how factors are weighed — it states only that "credit rating is an overall assessment of all aspects of the issuer" and that "rating determination is a matter of experience and holistic judgement of the Rating Committee." **This absence is itself a key finding for the audit**: CareEdge's own published manufacturing methodology gives NO explicit numeric weighting scheme for scale/profitability vs leverage/coverage — any such fixed weighting used inside the ICRA-agent's scorecard tool for a CareEdge-style rating would be the tool's own invention, not something traceable to this document, and is exactly the kind of "misweighted scorecard factor" the audit is investigating. A tool that assigns hard numeric weights to these factors when rating a CareEdge-scope entity cannot cite this methodology as its source.
- **Indicative-metrics tables:** None (no numeric thresholds anywhere in the document; entirely qualitative).
- **Notching/support/mapping rules:** No LT-ST mapping/outlook table. Parent/group/government support handled entirely by cross-reference to CareEdge's separate Notching Criteria document (not detailed here). No hybrid-instrument rules (out of scope for this generic document — covered in the Financial Sector Ratios doc and presumably a dedicated Hybrid Instruments methodology not in this batch).
- **Definitions differing from generic — the key items bearing directly on the audit's stated failure modes:**
  - **Cash flow analysis is explicitly built from the CASH FLOW STATEMENT, not the P&L, and this is a deliberate, named step**: "Cash flow analysis includes evaluating the operating cash flows of an entity. Working capital changes are then adjusted to arrive at cash flow from operations... Cash flow from investing activities is calculated to assess the entity's investing needs... Assessment of cash flow from financing activities is undertaken to evaluate the entity's financing avenues (debt/equity), its repayment obligations, lease liabilities..." — the document explicitly separates OCF/ICF/FCF and cross-checks "adequacy of cash flow from operations to meet an entity's investing and financing needs," warning specifically against an entity "continuously using cash flow from financing activities, especially debt funds, to meet cash flow from operating activities." This is the general corporate-methodology's own boundary line between cash-flow-statement figures and P&L figures — it explicitly wants BOTH computed and cross-checked against each other, never one substituted for the other. This directly supports the audit's concern about "cash-flow figures substituted for P&L figures" as an error class: per this methodology, cash flow measures (OCF, FCF) are a SEPARATE, ADDITIONAL analytical layer alongside — never a replacement for — P&L-based ratios (which live in the cross-referenced Financial Ratios methodology).
  - **Accounting Quality section explicitly requires decomposition/adjustment for one-offs**: "Impact of auditors' qualifications and comments are quantified to the extent possible and analytical adjustments are made to accounts, if material... Change of accounting policy in a particular year, which results in improved reported performance is analysed more closely" — this is the general-methodology-level statement (mirrored, more specifically, in the ICRA project's own failure-mode-36 finding about undecomposed Other Income/Expenses aggregates) that P&L composites must be interrogated for one-off/non-recurring content before being used in ratios, though this document does not itself name "Other Income"/"Other Expenses" line items or give an OPBDIT/PBILDT formula (that resides in the cross-referenced Financial Ratios methodology, not included in this file batch).
  - **Financial Flexibility definition:** "alternative sources of liquidity available to the entity as and when required," including unencumbered liquid investments, group support, timely monetisation of non-core assets, flexibility to defer capex, undrawn sanctioned bank lines — and explicitly: **"CareEdge Ratings does not assume equity fund raising and debt refinancing while analysing ability to repay debt unless funds have already been arranged."** This is a bright-line qualitative rule: prospective/unarranged refinancing or equity raises may NOT be credited in the liquidity/repayment analysis.
  - **Net worth / TNW is NOT separately redefined in this document** — it is deferred entirely to the (non-financial-sector) Financial Ratios methodology, which is referenced repeatedly but not included in this 10-file batch. This is itself a finding: this manufacturing methodology gives no independent net-worth or gearing definition of its own; any misapplication of the financial-sector TNW definition (DTA-netting, revaluation-reserve exclusion) to a manufacturing entity, or vice versa, cannot be diagnosed from this document alone — the corporate Financial Ratios / Non-Financial Sector methodology (not in this batch) is the necessary companion document.
  - **Contingent liabilities:** "CareEdge Ratings takes note of contingent liabilities reported by an entity and carries out an impact analysis of possible liabilities devolving on the entity" — a general instruction to analyse (not a specific rule on LC/acceptance/buyers'-credit treatment as debt; that granular treatment, if it exists in CareEdge's corpus, would live in the Financial Ratios – Non-Financial Sector document, not in this generic manufacturing methodology).
- **Mechanically-checkable bright-line rules:** Essentially none with hard numeric cutoffs in this document — it is the most purely narrative/qualitative of the ten files. The only quasi-bright-line rule is the "no equity/refinancing credit unless already arranged" liquidity rule, which is codeable as a boolean gate (exclude any liquidity source not evidenced as contractually committed) but carries no numeric threshold.

---

## Criteria_Rating_Methodology_Mobile_Service_Providers_March_2025.md

- **Scope:** Mobile/telecom service providers (mobility/wireless operators), including their diversification into enterprise/cloud/WiFi-LAN/DTH/broadband non-mobile revenue streams.
- **Rating-factor structure:** Operating Environment (Structure of the industry, Regulatory Framework); Company-specific/Business Parameters (Market Position, Technology Risk, Geographical Diversification/Consumer Mix, Business diversification, Brand Image/Network Coverage & Quality); Financial Profile (EBITDA profitability, Leverage/Debt Profile); Promoter/Management Evaluation; ESG.
- **Indicative-metrics tables:** None — no numeric threshold table for ARPU, market share, leverage, etc. All qualitative/directional (e.g., "low Average Revenue Per User (ARPU) and Average Revenue Per Minute (ARPM)" characterised as a sector feature, not a rating threshold).
- **Notching/support/mapping rules:** None in this document (no LT-ST/outlook table, no explicit parent-support notching rule beyond the general promoter financial-flexibility narrative).
- **Definitions differing from generic (directly relevant to audit's net-worth-basis concern):**
  - **Net worth / intangibles treatment — explicit sector-specific carve-out:** "CareEdge Ratings **generally excludes intangible assets while computing net worth**, however, in case of mobile service providers, their **spectrum holding, which is an intangible asset is inherent to their ability to offer their services, and hence, is NOT excluded** while calculating the net worth." This is a named, explicit deviation from CareEdge's own generic net-worth convention (which otherwise excludes intangibles) — spectrum licences are retained in net worth for telecom operators specifically because they are operationally essential, unlike goodwill/trademarks etc. This is exactly the kind of sector-specific net-worth-basis rule the audit is looking for as a template of what "wrong net-worth basis" errors look like when a generic rule is misapplied to a sector carve-out (or vice versa).
  - **Debt profile:** explicitly includes "deferred payment liabilities arising out of spectrum purchase and dues pertaining to adjusted gross revenue (AGR)" as part of the leverage/capital-structure analysis — i.e., deferred spectrum payment obligations and AGR dues are treated as debt-like liabilities requiring inclusion in leverage assessment, not merely disclosed as contingent items.
- **Mechanically-checkable bright-line rules:** None with hard numeric cutoffs. The spectrum-intangible-inclusion rule and the AGR/deferred-spectrum-liability-as-debt rule are both qualitative but structurally precise enough to be coded as boolean inclusion/exclusion flags specific to the telecom sector (i.e., a mechanical check could flag "spectrum intangible excluded from net worth" or "deferred spectrum/AGR liabilities excluded from total debt" as sector-methodology violations for a telecom entity).

---

## Criteria_Rating_Methodology_Paper_and_Paper_Products_March_2025.md

- **Scope:** Paper and paper-products manufacturing companies (writing & printing paper, packaging paper, newsprint segments); layered on top of the general manufacturing-sector methodology.
- **Rating-factor structure:** 1. Industry risk analysis (segment classification, cyclicality, entry barriers); 2. Business risk analysis (Market position, Level of integration in operations [backward/forward], Sourcing arrangement of raw materials, Cost structure and operational efficiency, Marketing network and geographical diversification, Capital expenditure for capacity expansion/modernisation); 3. ESG (Environmental, Social, Governance); 4. Financial risk analysis.
- **Indicative-metrics tables:** No numeric threshold/band table — entirely qualitative/directional. Sector-defining operating metrics are named but not benchmarked with numbers: **Net Sales Realisation (NSR), gross margins, PBILDT per tonne, Raw Material Cost per Tonne, Power Cost per Tonne, Return on Capital Employed (ROCE)**. One approximate quantitative statement embedded in prose (not a rating threshold, an industry fact): "Newsprint prices... account for **more than 50% of the total production cost**."
- **Notching/support/mapping rules:** None (no LT-ST/outlook table, no parent-support notching specifics — defers to general/cross-cutting policies).
- **Definitions differing from generic:**
  - **Sector-specific efficiency metrics required to be decomposed and per-tonne normalised**: "Ratios such as Raw Material Cost per Tonne and Power Cost per Tonne are analysed and compared with other industry players" — this requires the aggregate cost-of-goods P&L line to be broken into per-unit components (raw material cost per tonne vs power cost per tonne), which cannot be done without decomposing the P&L note into its constituent cost categories — directly relevant to the audit's "aggregate P&L notes not decomposed" concern; this methodology explicitly mandates that decomposition for paper companies.
  - **PBILDT per tonne** explicitly named as an operating-efficiency benchmark metric (i.e., PBILDT itself must be divided by production volume, requiring both the correctly-computed PBILDT figure and accurate production-volume data — an error in either directly propagates).
  - Trend analysis window specified as **5-year** for financial risk analysis ("Trend of the financial analysis over the last 5-year period is analysed and compared with the average industry trend") — longer than some other sector methodologies in this batch (Mobile Service Providers used "3-5 years").
  - No net-worth/TNW/gearing redefinition specific to paper (defers to the general Financial Ratios methodology, not included in this batch).
- **Mechanically-checkable bright-line rules:** None with hard numeric cutoffs (the ">50% of production cost" newsprint-price statement is descriptive of industry structure, not a rating gate). The requirement to compute cost-per-tonne metrics (raw material, power) is a codeable normalisation step but has no associated pass/fail threshold in this document.

---

## Cross-cutting observations relevant to the audit

1. **No document in this batch contains a numeric factor-weighting/scoring table** for combining Industry/Business/Financial/Management risk into a composite score or notch outcome — including the Manufacturing Companies methodology, the one closest to the failed case. Any hard-coded factor weights in the ICRA-agent's CareEdge scorecard tool are therefore NOT traceable to these methodology texts; they must come from elsewhere (the tri-agency `Rating_Scorecard.xlsx` template mentioned in the project's CLAUDE.md) and should be checked against actual CareEdge published rationales rather than assumed to mirror this prose.
2. **The one document with fully exact, codeable net-worth/gearing/hybrid-instrument rules is the Financial Ratios – Financial Sector methodology** (banks/NBFC/HFC). Its TNW formula (ex-revaluation-reserve, ex-bad-debt-reserve, minus DTA-net-of-DTL) and its Total-Debt-includes-guarantees rule are the most load-bearing definitions in this batch for diagnosing a wrong-net-worth-basis or wrong-gearing-inclusion error — but they apply to financial-sector entities, not a manufacturing/mineral-processing company like the synthetic-rutile case.
3. **Three sector methodologies (Construction, Hotel, Mobile Service Providers) each carry their own explicit, sector-specific gearing/net-worth inclusion rule that deviates from a generic default**: Construction includes guarantee-backed mobilisation advances in working-capital debt; Hotels include lease liabilities in total debt; Mobile Service Providers retain spectrum intangibles in net worth (deviating from CareEdge's own stated general exclusion of intangibles) and include deferred spectrum/AGR liabilities in debt. None of these three specifically discuss LC-backed creditors/acceptances/buyers' credit — that granular trade-finance-instrument treatment is not addressed in any of these ten documents and most likely resides in the (non-financial-sector) Financial Ratios methodology or a dedicated document not included in this batch.
4. **Cash-flow-vs-P&L figure substitution:** the Manufacturing Companies methodology explicitly requires BOTH a cash-flow-statement-based analysis (OCF/ICF/FCF, cross-checked for "financing activities being used to fund operating activities") AND a separate P&L-based ratio suite — it treats these as complementary, not substitutable. The LRD methodology, by contrast, deliberately builds its core coverage metric (CCR) directly from cash inflows/outflows because the underlying loan structure is genuinely cash-flow-based (rent escrow waterfall) — this is a case where cash-flow-based ratios are methodologically CORRECT, not an error, and should not be treated identically to a manufacturing company's P&L-vs-cashflow situation.
5. **Aggregate P&L note decomposition is explicitly required, not optional, in at least two of these documents**: HFCs (fee-based vs fund-based income, recurring vs non-recurring, for "core earnings") and Paper & Paper Products (raw material cost per tonne, power cost per tonne decomposed out of aggregate cost of goods). This directly corroborates the audit's concern about undecomposed aggregate notes as a source of error — CareEdge's own methodologies assume analysts will decompose these aggregates, and a tool that does not will diverge from the CareEdge-intended analysis.

All 10 files were read in full via the Read tool; none required a follow-up offset read (each file's full content returned in a single Read call, confirmed by the trailing disclaimer/footer boilerplate appearing at the end of each output).

# Part 4 — CareEdge Methodology Corpus Review

## Criteria_Rating_Methodology_Pesticides_Agrochemicals.md

- **Scope:** Additive/supplementary criteria for pesticides & agrochemicals manufacturers, layered on top of CARE's generic "manufacturing sector" methodology (available separately on careratings.com). Does not stand alone — the base manufacturing methodology (industry/company business risk → financial/project risk → management quality) governs; this doc only adds sector-specific factors. No explicit exclusions stated. Issued Feb 2025 (supersedes Dec 2022 version).
- **Rating-factor structure:** Business/Operational risks (9 named factors): (1) Product portfolio & diversification across segments (technical vs formulations vs integrated), (2) Market position & distribution network, (3) R&D capabilities, (4) Product registrations/acquisitions (incl. CSM — Custom Synthesis Manufacturing), (5) Regulatory risk management (Insecticides Act 1968/Rules 1971; toxicity label colour-coding), (6) Brand building/product awareness, (7) Presence in export markets, (8) Raw material linkages (import dependence, esp. on China), (9) Working capital management. Then Financial Analysis (deferred entirely to CARE's generic "Financial Ratios – Non-Financial Sector" criteria — no sector-specific ratios given here) and ESG (Environment/Social/Governance qualitative risks).
- **Indicative-metrics tables:** None. This document is entirely qualitative/narrative — no numeric thresholds anywhere (no revenue bands, no margin bands, no leverage cutoffs). The only numeric figures are background stats (crop losses ~20-25% of food produced; China supplies ~90% of world's technical raw material) — not rating thresholds.
- **Notching/support/mapping rules:** None present in this document.
- **Definitions differing from generic/ICRA:** None — the document explicitly defers all financial-ratio definitions to CARE's "Financial Ratios – Non-Financial Sector" criteria; no TOI/PBILDT/TNW/gearing definition is given here.
- **Mechanically-checkable thresholds:** None. Toxicity label categories (red=extremely toxic, yellow=highly toxic, blue=moderately toxic, green=less toxic) are categorical/regulatory facts that could be flagged in a checklist (e.g., "% of revenue from red/yellow-label products") but carry no numeric rating cutoff.

---

## Criteria_Rating_Methodology_Real_Estate_Sector_Feb_2025.md

- **Scope:** Covers real estate entities whose primary business model is construction-and-sale of residential/commercial space. Explicitly EXCLUDES developers whose primary model is leasing commercial space for rent — those are assessed under the separate criteria "Debt backed by lease rentals." Notes real estate financial statements are not directly comparable to manufacturing concerns because (a) revenue-recognition policies vary, (b) profit ≠ cash flow for a given period, (c) revenue booking fluctuates with project execution stage.
- **Rating-factor structure:** Four risk heads — (A) Industry risk evaluation (demand-supply outlook, cyclicality, corporate governance/transparency); (B) Management evaluation (promoter experience, past projects developed, legal constitution, organisational structure/group support — parent notching per CARE's "Notching by Factoring Linkages in Ratings"); (C) Operational risk assessment (execution risk, marketing risk, diversification, land bank availability); (D) Financial risk assessment (cash flow analysis, adequacy of committed receivables, liquidity analysis, project funding pattern, leverage).
- **Indicative-metrics tables:** No numeric threshold table exists (no bands like ">2x strong" etc.). Named ratios/metrics without published cutoffs:
  - Booking ratio = % area/units booked out of launched area/units.
  - Months-to-sell unsold inventory (lower = better sales velocity) — no numeric band given.
  - Cash coverage ratio (CCR) — cushion for debt obligations; sensitised for delays/lower collections/cost increases — no numeric band given.
  - Committed-receivables ratio = committed customer advances (confirmed sales) ÷ (balance project cost + outstanding debt) — lower ratio = higher dependence on fresh sales/promoter funds; no numeric band given.
  - Total-receivables ratio (adds unsold-unit value, esp. recently completed units) to same denominator — no numeric band.
  - Liquidity coverage ratio (buffer vs next-year debt obligations) — cross-refers to CARE's "Liquidity Analysis of Non-financial sector entities" methodology; no band given here.
  - Funding pattern = Promoter Funds : Debt : Customer Advances — no numeric band.
  - Leverage: overall gearing (compared to peers with similar asset portfolios), gross debt/collections, debt per square foot — no numeric bands given for any.
  - Stage-of-construction ratio = % cost incurred ÷ total estimated project cost — no numeric band.
- **Notching/support/mapping rules:** Group/SPV support — "ratings of an entity may be notched up/down based on credit standing of the parent and strength of the linkage between the issuer and the parent company," per CARE's "Notching by Factoring Linkages in Ratings" criteria (cross-referenced, not reproduced). Subordinated debt from promoters is "adjusted appropriately" when assessing leverage (i.e., can be treated akin to equity — not spelled out numerically). LRD (lease rental discounting) loans are "discerned" (segregated) from construction finance/other debt when assessing debt position, since LRD-backed portfolios carry lower average cost of debt and lower cash-flow volatility.
- **Definitions differing from generic/ICRA:** No explicit TOI/PBILDT/TNW/gearing formula is given — the doc references "overall gearing" generically without stating numerator/denominator composition. JDA (Joint Development Agreement) liabilities recorded on balance sheet are explicitly considered part of the developer's financial position/leverage evaluation — i.e., JDA liabilities are debt-like items to be factored in, which is a real-estate-specific inclusion not found in generic corporate methodology. No cash-flow-vs-P&L substitution issue flagged; rather the document explicitly WARNS that profit for a period may differ significantly from cash flow — i.e., it flags the P&L/cash-flow divergence as an analytical hazard rather than defining a ratio that conflates them.
- **Mechanically-checkable thresholds:** None with actual numbers (no bright-line cutoffs published in this document) — every ratio named is described directionally ("lower is better") without a published band, unlike ICRA's typical indicative tables. This absence itself is a checkable fact for a tool: no numeric real-estate gearing/leverage cutoff exists in this CareEdge document to hard-code.

---

## Criteria_Rating_Methodology_Services_Sector_March_2025.md

- **Scope:** Primarily covers personnel-based/professional services: accounting firms, law firms, management consultancy/advisory, security services, support services, IT and facility maintenance services, logistics services, among others. No explicit sector exclusions stated beyond implying capital-intensive/asset-heavy service businesses are covered elsewhere by relevant sector-specific criteria (e.g., shipping, wholesale trading have their own methodology docs referenced elsewhere in this corpus). Issued March 2025, supersedes "Service Sector Companies" (Dec 2022).
- **Rating-factor structure:** A. Industry Risk; B. Management Evaluation (track record, business strategy, profile/association of management team, org structure, succession planning, personnel policies, control systems, corporate governance, legal constitution); C. Business Risk (nature/complexity of services, nature of service contracts, service proposition/market position — incl. per-unit metrics like billing rate/employee and cost/employee for IT, yield/kg for logistics —, seasonality/cyclicality, scale of operations, diversification (services/clients/end-market/geography), exposure to overseas markets, cost structure, force majeure); D. Financial Risk (growth ratios, profitability ratios, leverage & coverage ratios, liquidity ratios, working capital cycle & financial flexibility, validation of projections/sensitivity, contingent liabilities, forex risk); ESG (environment/social/governance).
- **Indicative-metrics tables:** None — entirely qualitative narrative; no table with numeric thresholds anywhere in the document.
  - Named ratio categories (no bands given): Growth — PBILDT growth, PAT growth; Profitability — PBILDT margin, operating margin, PAT margin, ROCE, RONW; Leverage/Coverage — overall gearing, interest coverage, debt/cash accruals, DSCR; Liquidity — current ratio.
  - Full ratio definitions deferred to CARE's "Financial Ratios – Non-Financial Sector Entities" methodology (cross-reference, not reproduced here).
- **Notching/support/mapping rules:** Parent/group/government support notching is mentioned generically — "Support from the parent company, group, or government (if applicable) is thoroughly examined and factored into the overall rating assessment, in accordance with CareEdge Ratings' Criteria on Notching" — cross-referenced, not detailed in this document.
- **Definitions differing from generic/ICRA:** Notably states: "In the services industry, debt mainly consists of working capital borrowings and/or non-fund-based limits such as performance bank guarantees ... overall gearing ratio and interest coverage are major ratios analysed." This flags that non-fund-based limits (performance bank guarantees specifically) are treated as part of the debt/leverage picture for services entities — a sector-specific gearing-inclusion point relevant to the ICRA tool's LC/acceptances-in-gearing issue, though it does not spell out the exact treatment of LC-backed creditors/acceptances the way the Wholesale Trading document does. PBILDT is named (profit before interest, lease rentals, depreciation, and taxation) consistent with CARE's standard PBILDT definition but not further decomposed in this doc.
- **Mechanically-checkable thresholds:** None — no numeric cutoffs anywhere in this document.

---

## Criteria_Rating_Methodology_State_Governments_March_2025.md

- **Scope:** Covers CARE's assessment of state government credit quality SPECIFICALLY as an input to rating debt instruments of State Public Sector Enterprises (SPSEs) that carry explicit state support (guarantees, letters of comfort) or implicit support as strategically important SPSEs — e.g., state power distribution companies, irrigation corporations, road development corporations, state finance corporations, infrastructure development corporations. Not a standalone state-government rating product; it is a support/linkage input methodology. No entity types are explicitly excluded, but scope is narrowly tied to guaranteed/state-backed SPSE debt.
- **Rating-factor structure:** Three broad factors — (1) Economic risk (GSDP growth/sectoral composition, demographics, social infrastructure, economic infrastructure: power/irrigation/transport/manpower/agriculture/natural resources); (2) Financial risk (state government finances: revenue performance, expenditure management, deficit management, debt profile); (3) Economic management (industrialisation/investment policy, economic policies, political risk, liquidity support [RBI's SDF/WMA/overdraft facilities], management of guarantees [CSF/GRF reserves], debt servicing track record, performance of state PSUs).
- **Indicative-metrics tables (verbatim ratio definitions, no numeric bands given):**
  - Revenue performance table: Size of revenue receipts = RR/GSDP; Self-reliance = SOR/RR; Revenue mobilisation = SOR/GSDP.
  - Expenditure management table: Size of expenditure = RD/RR; Quality of expenditure = Committed expenditure/RR, Capital outlay/GSDP, Capital outlay/GFD.
  - Deficit management table: Fiscal prudence = RD/GSDP, GFD/GSDP.
  - Debt profile table: Size of debt and guarantees = (Debt+Guarantees)/GSDP, (Debt+Guarantees)/RR; Debt sustainability = Interest/RR, [(Revenue receipts − (Revenue expenditure − Interest)] / Interest, and [(Revenue receipts − (Revenue expenditure − Interest)] / (Interest + Debt servicing).
  - No numeric strongly/weakly-positioned bands are published for any of these ratios in this document — only the ratio formulas themselves.
- **Notching/support/mapping rules:** Debt+Guarantees is explicitly the numerator convention for state indebtedness — off-budget borrowings are included "subject to availability of information." This is the closest analogue in the corpus to a broad "guarantees count as debt" statement, applied here to sovereign/state-level guarantees rather than corporate LC/acceptances.
- **Definitions differing from generic/ICRA:** RR (Revenue Receipts), SOR (presumably State's Own Revenue = SOTR+SONTR), GSDP, RD (Revenue Deficit), GFD (Gross Fiscal Deficit) are sovereign/public-finance-specific definitions with no corporate analogue — not comparable to TOI/PBILDT/TNW. Debt sustainability ratio nets out interest from revenue expenditure in a specific waterfall ((Revenue receipts − (Revenue expenditure − Interest)) — this is a public-finance-specific "primary balance ÷ interest" construction, not a corporate DSCR.
- **Mechanically-checkable thresholds:** None — every ratio is a formula without a published numeric band.

---

## Criteria_Rating_Methodology_Urban_Infrastructure_March_2025.md

- **Scope:** Covers Urban Local Bodies (ULBs)/municipal bodies and their debt instruments (municipal bonds — General Obligation Bonds and Revenue Bonds) financing water supply, sanitation, solid waste management, bridges/roads, urban transport, bus terminals, public housing, shopping complexes, and similar public facilities. Cross-references the separate State Governments methodology when assessing municipal bodies' dependence on state budgetary support.
- **Rating-factor structure:** A. Economic Base (local economy nature, employment/income, development indicators); B. Legal Factors (borrowing powers/limits, taxation/user-fee powers, litigation, collection enforcement); C. Administrative Factors (org structure, project-implementation track record, MIS, tax billing/collection/enforcement); D. Leverage and Debt Coverage (total debt/RR, DSCR; structured payment mechanisms — escrow, DSRA, waterfall — can notch up specific debt securities from the issuer rating level); E. Financial Factors (revenue receipts & expenditure — tax/non-tax/assigned revenue/grants/other income; capital receipts & expenditure; accounting/auditing practices; financial indicators); F. Project Viability (for project-specific/revenue-bond financings — sources/uses of funds, revenue/expenditure projections, sensitivity to user-charge hikes/cost of borrowing, credit enhancement evaluation).
- **Indicative-metrics tables:** None with numeric bands — only named ratios: total debt/Revenue Receipts (RR), Debt Service Coverage Ratio (DSCR), tax collection efficiency ratio, % share of own revenue (tax+non-tax) to total revenue receipts. No thresholds published.
- **Notching/support/mapping rules:** Structured payment mechanisms (escrow of identified revenue sources, DSRA, waterfall mechanism, restricted payment conditions) can result in "ratings notched up from issuer rating level" for specific debt securities — direction stated, no specific notch count given.
- **Definitions differing from generic/ICRA:** RR (Revenue Receipts) is a municipal-finance-specific concept combining tax revenue, non-tax revenue, assigned revenue (e.g., share of stamp duty), and government grants — not a corporate TOI/PBILDT analogue. No corporate net-worth/gearing/TNW definitions appear in this document at all — entirely public-body/municipal finance vocabulary.
- **Mechanically-checkable thresholds:** None numeric.

---

## Criteria_Rating_Methodology_Wholesale_Trading_Mar_2025.md

- **Scope:** Additive criteria for wholesale/commodity trading companies (large-volume bulk trading, minimal value addition, thin operating margins, high working-capital intensity), layered on CARE's standard Services Sector methodology. Covers entities with logistical assets (silos, warehouses, storage tanks, port facilities) used for holding inventory/last-mile connectivity.
- **Rating-factor structure:** A. Management evaluation (board composition, risk-management policy, parent/group support per Notching criteria); B. Industry risk analysis (regulatory risk on essential-commodity trade, import-duty changes); C. Business risk analysis — commodity & geographic diversification, size & market position (TOI and tangible-net-worth base as competitive-position indicators), relationship with suppliers/customers & diversity (supplier/customer concentration risk), supply chain infrastructure (asset-light vs asset-heavy integration), profitability (RoCE as the KEY measure, plus gross margins), commodity price fluctuation risk, inventory risk, counterparty credit risk, forex risk; D. Financial risk analysis — capital structure & debt protection measures, liquidity & working capital management; E. ESG.
- **Indicative-metrics tables:** No numeric-band table exists — only named ratio formulas:
  - Leverage: "total debt (long + short-term debt + acceptances / non-fund-based facilities) to TNW", total debt/PBILDT, TOL/TNW, total debt/cash flow from operations.
  - Coverage: interest coverage, term debt/GCA, total debt/GCA, DSCR (where long-term debt repayment exists).
  - Liquidity: current ratio; also cash-generating capacity vs 12-month fixed obligations, unencumbered cash/investment balance, unutilised bank lines.
  - Working capital: operating cycle trend, gross current asset (GCA) days, debtor ageing.
  - Profitability: RoCE (key measure) and gross margins.
  - No numeric thresholds/bands given for any ratio in this document.
- **Notching/support/mapping rules:** Parent/group/conglomerate support notching cross-referenced to CARE's "Criteria on Notching by Factoring Linkages in Ratings (Parent-Subsidiary linkages, Group linkages, Joint Ventures, and Private Equity)" — not detailed here.
- **DEFINITION DIFFERING FROM GENERIC/ICRA — DIRECTLY RELEVANT TO THE AUDIT'S FOCUS:** This is the one document in this batch that EXPLICITLY states the gearing-inclusion rule the ICRA tool has reportedly gotten wrong: *"CareEdge Ratings analyses the ratios such as total debt (long + short-term debt + acceptances / non-fund-based facilities) to TNW ... CareEdge Ratings considers the creditors on Letter of credit / Acceptances as part of the total debt while calculating total debt for deriving leverage indicators."* This is a verbatim, unambiguous rule: LC-backed creditors/acceptances/non-fund-based facilities used for trade purchases MUST be included in "total debt" for gearing/leverage ratios in wholesale trading entities specifically (and, by implication of the parallel Services Sector document's mention of "non-fund-based limits such as performance bank guarantees" being part of the debt/leverage picture, this convention likely extends more broadly across CareEdge's working-capital-intensive sector methodologies). Any rating tool that excludes LC/acceptances from gearing for a trading company would misstate leverage upward-favorably (understate gearing), which is exactly the class of definitional error named in the audit brief.
- **Mechanically-checkable thresholds:** None numeric, but the acceptances-in-debt rule above is itself a bright-line INCLUSION rule (not a numeric cutoff, but a binary definitional rule) that is precisely actionable as a mechanical check: "does the tool's gearing/leverage computation for a wholesale-trading entity add LC-backed creditors/acceptances/non-fund-based facilities utilised to total debt? If not, flag as a definitional error."

---

## Criteria_Rating_Methodoloy_Shipping_companies_March_2025.md

- **Scope:** Covers Indian shipping companies across the four industry segments — Dry Bulk, Wet Bulk (tankers), Containership, Offshore Shipping. No explicit entity-type exclusions.
- **Rating-factor structure:** A. Business Risk (economies of scale/fleet size; diversification — operating segment, geographical reach across 7 named trade lanes, customer base; deployment strategy — bareboat/voyage/time charter mix; operating efficiency — fleet age, owned vs leased vessels, fleet type incl. IMO double-hull requirements, fleet utilisation); B. Financial Risk (financial strategy & capital mix — ROCE, overall gearing ratio, Total Debt/PBILDT [document explicitly labels this "Profit before interest Lease Deprecation and Tax" — note the shipping-specific PBILDT formulation naming "Lease" rather than the more standard "Interest, Lease rentals, Depreciation, Tax"]; other ratios per CARE's generic Financial Ratios – Non-Financial Sector methodology; liquidity — free cash reserves for lean-period debt servicing); C. Management Evaluation (per CARE's manufacturing-companies management-risk criteria); D. Industry Risk (IMO/flag-state regulation; India's cabotage law and Right of Refusal for Indian-flagged vessels vs foreign-flagged competitors); ESG (environment — IMO's 2050 GHG-halving target vs 2008 baseline; social — health/safety, Maritime Labour Convention; governance — group structure complexity, related-party transactions).
- **Indicative-metrics tables:** None with numeric bands. Named ratios only: ROCE, overall gearing ratio, Total Debt/PBILDT. No thresholds published.
- **Notching/support/mapping rules:** None explicit in this document (no parent-support notching table, no LT-ST mapping, no outlook-trigger table).
- **Definitions differing from generic/ICRA:** The document's PBILDT expansion reads "profit before interest Lease Deprecation and Tax" (note: no "rentals" term as in the standard formula, and "Deprecation" appears to be a typo for "Depreciation" in the source document) — worth flagging as a potential source of definitional drift if literally implemented, though it is likely simply an OCR/typo artifact of the standard PBILDT (Profit Before Interest, Lease rentals, Depreciation, and Tax) formula used elsewhere in the corpus (e.g., Services Sector doc). No TNW/net-worth or gearing numerator/denominator composition is spelled out (unlike Wholesale Trading's explicit acceptances-in-debt rule) — this document is silent on whether LC/acceptances or off-balance-sheet lease commitments are included in "overall gearing ratio" for shipping companies, which is itself a gap worth flagging for a tool implementer (no explicit guidance = risk of inconsistent treatment for a debt-heavy, asset-intensive sector where leased-vessel treatment matters).
- **Mechanically-checkable thresholds:** None numeric. One directional/categorical fact of note: vessels constitute ~90% of gross block (background stat, not a rating threshold).

---

## Criteria_on_rating_credit_enhanced_debt_march_2025.md

- **Scope:** Covers all credit-enhanced (CE-suffix) ratings across both financial and non-financial sectors — bank facilities, CPs, FDs, NCDs/bonds/other capital market instruments — where an issuer's debt carries external, explicit third-party credit support (guarantee, LOC, shortfall undertaking, SBLC, DSRA guarantee, pledge of shares, covered bonds, guaranteed PBI). Distinguishes CE ratings (external support) from SO-suffix ratings (internal, bankruptcy-remote structural enhancement, e.g., cash-flow ring-fencing) — SO is explicitly out of scope of the CE analysis proper and covered only briefly at the end. Obligor/co-obligor and cross-default guarantee structures are explicitly EXCLUDED from CE rating treatment — CareEdge instead analyses combined financials/cash flows of all co-obligors per its "Consolidation & Combined Approach" criteria and does NOT assign a CE-suffix rating for these structures.
- **Rating-factor structure:** This is a notching/support methodology, not a business/financial-factor scorecard. Core structure: (1) validity tests for any support mechanism — unconditional, irrevocable, legally enforceable till full repayment, independent assessment of guarantor's financial strength, guarantor must have lower PD than issuer on a continuous basis; (2) instrument-specific eligible support types (tabulated separately for Bank Facilities/CP/FD vs NCDs/Bonds/capital-market instruments); (3) full guarantee → equate rating to guarantor's rating (direct credit substitution), including a "Shadow Rating" mechanism if the guarantor itself is unrated; (4) partial credit enhancement (PCE) → three named approaches — Probability of Default (PD) Approach, Cash Flow Specific Stress Approach (for infrastructure, using FLDG), Expected Loss Approach (for NBFC/HFC retail-pool-backed debt, using PD×LGD×EAD-style estimation over pool tenor, generally up to 3 years); (5) Limited-period guarantee (extinguished on defined operational/financial triggers, e.g., DSCR build-up) → rating not equated to guarantor, and post-extinguishment rating must independently "hold good" without the CE suffix; (6) DSRA guarantee from a third party; (7) LOC (only Central/State Government LOCs valid for bank facilities/CP/FD; broader LOC-provider set valid for NCDs/bonds) → rating falls "somewhere between" standalone and LOC-provider rating depending on strength of wording/moral obligation; (8) Shortfall undertaking (legally enforceable/irrevocable/unconditional) → treated akin to guarantee; (9) SBLC (bank/FI-issued) → rating equated to the bank's/FI's rating; (10) pledge-of-shares LAS structures (NCDs/bonds only).
- **Indicative-metrics tables (verbatim):** One structural comparison table listing valid support mechanisms by instrument type:

  | Bank Facilities / CPs / FDs | NCDs, Bonds and Other Capital Market Instruments |
  |---|---|
  | Guarantees meeting all RBI guidance-note principles (full or partial) | Unconditional, irrevocable, legally enforceable guarantees (full/partial)/shortfall undertakings/other third-party credit enhancements |
  | Letter of comfort (LOC) issued by Central/State Governments | Covered bonds (primary recourse to issuer, secondary to pool cash flows in trust) |
  | Shortfall undertaking (legally enforceable, irrevocable, unconditional) | Guaranteed pooled bond issuance (PBI), not through a trust |
  | Standby letter of credit (SBLC) | LOC |
  | Guarantee towards maintaining DSRA from a third party | Commercial mortgage-backed securities (CMBS)-like structures |
  | | SBLC |
  | | Obligor/co-obligor or cross-default guarantee structures* |
  | | Payment waterfall/escrow/DSRA etc. with full guarantee or DSRA-replenishment guarantee from a third party |
  | | Debt backed by pledge of shares or other assets |

  (*co-obligor/cross-default structures are NOT assigned CE ratings — analysed via Consolidation & Combined Approach instead.)
  No numeric thresholds (percentages, coverage multiples, notch counts) are given anywhere in this document — the PCE approaches, PD/LGD/EAD framework, and idealised-default-curve mapping are described conceptually only, without published numeric parameters.
- **Notching/support/mapping rules (the core content of this document):**
  - Full guarantee → issuer's CE rating = guarantor's rating (or a "Shadow Rating" of the guarantor if unrated by CareEdge), with continuous surveillance of the guarantor for the life of the rating.
  - Partial guarantee → final rating lies "somewhere in between" standalone issuer rating and guarantor rating; higher guarantor rating → greater notch-up; three named quantitative approaches (PD approach; cash-flow stress approach for infra PPP/FLDG structures — requires long-term revenue arrangement, concession agreement, and track record for stress-testing; Expected Loss approach for NBFC/HFC pool-backed debt, generally ≤3-year tenor).
  - Amortising vs non-amortising guarantee distinction: non-amortising guarantee's relative coverage strengthens over time as covered debt amortises.
  - Limited-period guarantee → rating NOT equated to guarantor; must independently assess post-extinguishment credit quality; principle stated: "the rating of the debt should, at any point in time, be stable" — i.e., no rating should be set up to cliff-edge-downgrade purely because a guarantee term feature disappears.
  - LOC-based ratings: rating "lies somewhere in between" standalone and LOC-provider rating, moving "significantly closer" to LOC-provider's rating only if the LOC wording is guarantee-like in strength; generally NOT equated even then.
  - SBLC → equated directly to bank/FI rating (unlike LOC, which is never fully equated).
  - Overseas (foreign parent) guarantors: requires a legal opinion covering repatriation/fund-transfer feasibility and legal enforceability in the guarantor's home jurisdiction — transfer restrictions "may have a larger bearing than the credit quality of the guarantor."
- **Definitions differing from generic/ICRA:** LGD is explicitly defined as "1 – Recovery Rate" and the expected-loss approach for NBFC/HFC partial-guarantee structures is framed as PD × LGD × EAD (an EL-style framework overlapping conceptually with the separate Expected Loss Ratings for Infrastructure Projects document below, but applied here to partial-guarantee-covered retail-asset-backed debt rather than infrastructure project debt directly). No TOI/PBILDT/TNW/gearing definitions appear in this document — it is purely a support/enhancement notching methodology, not a financial-ratio methodology.
- **Mechanically-checkable thresholds:** No numeric cutoffs, but several binary/categorical rules are mechanically checkable in a rating tool: (a) is the guarantee unconditional AND irrevocable AND legally enforceable AND covers the facility "in its entirety" (else it's a PCE, not a full credit substitution)? (b) is the support-provider's PD lower than the issuer's PD on a continuous basis (else it does not qualify as valid CE support at all)? (c) for co-obligor/cross-default structures — CE suffix must NEVER be applied (rule is absolute, not a threshold, but is a hard yes/no gate a tool should enforce). (d) LOC validity for bank facilities/CP/FD is restricted ONLY to Central/State Government LOC providers — any other LOC provider is invalid for that instrument class (a bright-line eligibility rule).

---

## Expected_Loss_Ratings_for_Infrastructure_Projects_Nov_2025.md

- **Scope:** Covers Expected Loss (EL) ratings for ALL infrastructure project SPVs, including under-construction and operational projects, and all debt instruments in the infrastructure sector — roads (annuity, toll-based, hybrid annuity model/HAM), power (thermal, hydro, wind, solar), airports, ports, and other infrastructure project entities; also extendable to Municipal Bonds financing infrastructure assets. This is an ALTERNATIVE rating scale (EL 1–EL 7) run alongside/instead of the conventional PD-only 'CARE AAA'–'CARE D' scale, specifically for infrastructure SPVs with concession-driven, long-dated, ring-fenced cash flows. Issued Nov 2025, supersedes March 2025 version.
- **Rating-factor structure:** Two-parameter composite: (a) Probability of Default (PD) — derived from the conventional CARE AAA–D rating (per the applicable sector-specific infrastructure methodology: roads/power/airports/ports etc.) mapped to CareEdge's own periodically-updated long-run/short-run historical default rates by rating category; (b) Loss Given Default (LGD) — derived from a scenario-based recovery-prospects analysis: present value (PV) of the project's future free cash flows under multiple STRESS-CASE default scenarios, assessed against the coverage they provide to outstanding debt over the loan repayment period, factoring in termination payments and insurance claims (especially relevant during the construction phase). Underlying qualifying project features considered for strong recovery prospects: long-term revenue-assurance arrangement (e.g., PPA with pass-through), concession agreement with government/quasi-government body, escrow structure with defined cash-flow waterfall, PPP-specific protections (non-compete clauses, termination-payment clauses), step-in/substitution rights for lenders, insurance cover.
- **Indicative-metrics tables (verbatim, WITH numeric thresholds — the clearest bright-line table in this batch):**

  | Rating Symbol | EL Range | Definition |
  |---|---|---|
  | CARE EL 1 | <1.25% | Lowest expected loss over the life of the instrument |
  | CARE EL 2 | 1.25% < X < 3.5% | Very low expected loss |
  | CARE EL 3 | 3.5% < X < 7.5% | Low expected loss |
  | CARE EL 4 | 7.5% < X < 15% | Moderate expected loss |
  | CARE EL 5 | 15% < X < 25% | High expected loss |
  | CARE EL 6 | 25% < X < 35% | Very high expected loss |
  | CARE EL 7 | (>35%, implied — upper bound not stated in source) | Highest expected loss |

  Formulas given verbatim: **EL = PD × LGD**; **ECL (absolute) = PD × LGD × EAD**; **LGD = 1 − Recovery Ratio**. EAD = exposure at default (outstanding project debt at time of default).
- **Notching/support/mapping rules:** PD is mapped from the conventional AAA-to-D letter rating via CareEdge's own (proprietary, periodically-recalculated) long-run default-rate table — i.e., this is a rating-to-PD lookup mapping rather than a notching rule per se. No LT-ST mapping table is given in this document (that lives in the corporate/cross-cutting criteria, not here). Default recognition follows CareEdge's standard "single day, single rupee" default trigger (stated explicitly in the Conclusion) — any missed payment, however small or brief, triggers 'CARE D' classification, with a "curing period" required before any upgrade out of D.
- **Definitions differing from generic/ICRA:** This is CareEdge's OWN alternative/supplementary scale (EL1–EL7) mapped from a PD×LGD framework — not present in ICRA's standard toolkit in this form (ICRA does have its own Expected Loss rating scale for infra, but the exact EL band cutoffs and their alignment with this CareEdge table should NOT be assumed identical — a tool that conflates ICRA's EL bands with CareEdge's 1.25%/3.5%/7.5%/15%/25%/35% cutoffs above would be importing the wrong agency's numeric convention, precisely the cross-agency-contamination failure mode flagged in the project's own CLAUDE.md failure-mode list (FM32/FM40).
- **Mechanically-checkable thresholds (the most actionable table in this entire batch of 10 files):** The EL% breakpoints above (1.25, 3.5, 7.5, 15, 25, 35) are exact, bright-line, numeric cutoffs suitable for direct mechanical/code implementation of an EL-rating lookup function — provided the tool is scoped ONLY to CareEdge-labelled EL ratings and never silently reused for an ICRA EL computation.

---

## Financial-Ratios–Insurance-Sector.md

- **Content:** This file is a stub/redirect notice, not a substantive methodology document. Full text (excluding boilerplate About/Disclaimer): "Financial Ratios – Insurance Sector [Issued in August 2022, discontinued in March 2025]. This criteria paper has been superseded by two separate criteria papers viz. 'Rating Methodology & Financial Ratios - Life Insurance Sector' and 'Rating Methodology & Financial Ratios - Non-Life Insurance Sector' which are available on CARE Ratings' website." No scope statement, no rating-factor structure, no indicative-metrics tables, no notching rules, and no ratio definitions are present in this file at all — it is purely a discontinuation/redirect notice plus standard company-boilerplate (About CareEdge, Disclaimer, contact/locations).
- **Implication for the audit / for the ICRA tool corpus:** If the ICRA Credit Rating tool's Knowledge Base or routing map cites "Financial Ratios – Insurance Sector" as an active methodology for scoring an insurance-sector rating, that citation is STALE/WRONG per this document's own text — the correct current documents are the separate Life Insurance and Non-Life Insurance methodology-and-ratio papers (which do not appear among the 10 files reviewed in this batch and should be sourced separately if an insurance-sector rating is ever attempted with CareEdge methodology). This is itself a scope-mismatched-methodology risk (the project's own failure mode 4) worth flagging: citing this discontinued document for any live insurance rating would be citing an archived/superseded methodology, which the project's CLAUDE.md explicitly lists as a named failure mode.


# Part 5 — CareEdge Methodology Corpus Review (10 files)

---

## Financial_Ratios_Non_Financial_Sector_March_2025.md

**CRITICAL / load-bearing file — CareEdge's master ratio-definitions document for manufacturing, trading and service sector entities.**

- **Scope:** Applies to manufacturing, trading and service sector entities (past financials and projections). Explicitly notes other sector-specific ratios/adjustments apply for real estate, construction, infrastructure, etc. (covered in their own methodologies). Supersedes the August 2022 version.

- **Structure:** Four ratio categories — (A) Growth ratios, (B) Profitability and return ratios, (C) Leverage and coverage ratios, (D) Turnover and liquidity ratios. Not a "rating factor scorecard" document — it is purely definitional/formula reference, feeding into the broader Corporate/sector methodology's factor analysis.

- **Verbatim definitions (the load-bearing content):**

  - **TOI (Total Operating Income):** "the entire operating income of the entity." Core sales = gross sales **net of indirect taxes** (GST, excise duty, sales tax, service tax etc.). Also **includes** other income related to core operations: job-work income, royalty/technical knowhow/commission received re: core operations, refund of indirect taxes, sale of scrap, cash discount received, duty drawback and other export incentives, and **exchange rate gain (not related to debt)**. Non-core income items excluded. **Interest income, dividend income, rental income are treated as NON-operating income "even though these items may be recurring in nature."**

  - **PBILDT:** TOI minus all operating expenses (raw material, traded goods cost, stores & spares, power & fuel, employee costs, S&D, admin/general expenses, royalty/technical knowhow/commission incurred, insurance, directors' fees, **exchange rate loss (not related to debt)**, bad debts, etc.)

  - **PAT:** From PBILDT, deduct: (-) Interest and finance charges **net of capitalised interest** — includes term loan interest, WC interest, **interest on unsecured loans from promoters/group entities**, interest on lease liability, premium on redemption of bonds/preference shares, gains/losses on exchange rate fluctuation **on debt**; (-) depreciation/amortisation incl. depreciation on right-of-use assets; (+/-) non-operating income/expense (incl. non-core items, profit/loss on sale of assets/investments); (+/-) prior period items (incl. income tax); (-) tax expense (current + deferred).

  - **GCA (Gross Cash Accruals):** PAT + all inherently non-cash expenditure (depreciation/amortisation **excluding depreciation on ROU assets created under Ind AS 116**, provision for deferred tax, write-offs, etc.). Note: **provisions that are not inherently non-cash from an accrual-accounting perspective — e.g., provision for bad debts, doubtful debts, warranties — are usually NOT added back.**

  - **ROCE formula (verbatim):** `[(PBIT +/- Non-Operating Income/Expenses +/- Extraordinary Income/Expenses +/- Other Comprehensive Income) × (12/No. of Months)] / [Avg.(TCEt, TCEt-1)] × 100`. TCE = Tangible Networth + Total Debt + Net Deferred Tax Liabilities/(Assets) **(OR)** Net Fixed Assets + Net Working Capital.

  - **RONW formula:** `[(PAT +/- Other Comprehensive Income) × (12/No. of Months)] / [Avg.(Tangible Networth_t, Tangible Networth_t-1)] × 100`.

  - **TANGIBLE NETWORTH — full definition (most critical passage in the batch):** Includes equity share capital, all reserves and surplus **(excluding revaluation reserve)**, unsecured loans from promoters/group entities **which are subordinated to outside loans**, equity share warrants, share application money, ESOPs outstanding, and **minority interest (in consolidated financials)**.
    - Miscellaneous expenditure not written off AND accumulated losses are **deducted**.
    - **Revaluation reserves are NOT part of tangible networth** (explicit exclusion, verbatim: "Revaluation reserves arising out of revaluation of fixed assets are not treated as a part of the tangible networth of the entity").
    - **Intangible assets are generally EXCLUDED** from tangible networth (software, internally generated goodwill, goodwill on consolidation) — **UNLESS the intangible is critical to core operations**, in which case it IS included. Named examples of includable intangibles: telecom license fees, mining surface rights, media rights (movie/audio/video/broadcasting/TV/theatrical/satellite/music/digital/overseas rights, copyrights), IPRs (patents, copyrights, trademarks, designs — common in IT/pharma).

  - **Leverage ratios — verbatim formulas:**
    - Long-term Debt-Equity = Total Long-term Debt (**including current portion of LT debt**) / Tangible Networth.
    - **Overall Gearing (Including Acceptances/Creditors on LC)** = Total Debt (**Including Acceptances/Creditors on LC**) / Tangible Networth.
    - Total Outside Liabilities to Networth = Total Outside Liabilities / Tangible Networth. TOL includes total debt, other long-term liabilities and provisions, **net of deferred tax liabilities/assets**.
    - Note: "Both debt equity and overall gearing ratios are **adjusted for the exposure to group entities**"; "CareEdge Ratings also considers the impact of **non-fund-based limits** (availed by the entity) on the leverage of the entity."
    - Interest Coverage = PBILDT / (Total Interest and Finance Charges − Amortisation of Premium on Debentures (if any) − Interest Capitalised).
    - Term Debt/GCA = Total LT Debt (incl. current portion) / GCA. Total Debt/GCA = Total Debt (**incl. Acceptances/Creditors on LC**) / GCA.
    - Term Debt/PBILDT and Total Debt/PBILDT (same debt definitions) / PBILDT.
    - Total Debt/CFO = Total Debt (incl. Acceptances/Creditors on LC) / CFO, where **CFO = cash generated from operations after adjusting for working-capital changes**.
    - **DSCR** = (GCA + Interest and Finance Charges − Internal Accruals Committed for Capex/Investment) / (Gross LT Debt Repayable in the Year + Standalone CP + ST Debt Repayment + Interest and Finance Charges).
    - **Cash DSCR** = same numerator minus **25% of the increase in Working Capital** (margin money assumption; balance 75% assumed funded by WC borrowings), over the same denominator.
    - Cumulative/Average DSCR — running average of DSCR across projection years.

  - **TOTAL DEBT — full definition (critical for gearing calc):** Includes all ST and LT debt: redeemable preference share capital, optionally convertible debentures, interest-free loans, foreign currency loans, vehicle loans, fixed deposits, unsecured loans, CP, inter-corporate borrowings, borrowings from promoters/associates/other group entities, bills discounted. **PLUS: acceptances/creditors on LC (including capex LCs), lease liability, and mobilisation advances backed by financial bank guarantees** (typically construction entities). **Any corporate guarantee given to lenders of subsidiaries/group entities is ADDED to debt** for adjusted leverage ratios.
    - **Carve-out:** If part of promoter/related-party borrowings is **subordinated to outside loans, it is treated as part of tangible networth instead of debt** (though interest expense on it is still treated as normal interest expense).
    - **Carve-out:** If debt is **fully backed by dedicated/lien-marked fixed deposits/cash margin**, it is **excluded from total debt**.

  - **Hybrid instruments treatment:**
    - **Redeemable preference shares:** generally treated as debt (fixed tenure + fixed dividend). **EXCEPTION:** if issued to promoters and redeemable only after repayment of outstanding term debt, treated as **quasi-equity**.
    - **Compulsorily convertible instruments:** treated as **quasi-equity / part of tangible networth** — UNLESS investors have an exit option or conversion is conditional, in which case treated as **debt**.
    - **Optionally convertible instruments (OCPS/OCDs):** generally treated as **debt** until actual conversion (debt-like characteristics until conversion).

  - **Turnover/liquidity ratio formulas (verbatim):**
    - Avg. Inventory Period = [Avg.(INV_t, INV_t-1) × 30 × No. of Months] / [Cost of Sales − Selling Expenses].
    - Avg. Collection Period = [Avg.(REC_t, REC_t-1) × 30 × No. of Months] / [Gross Sales + Traded Goods Sales + Job Work Income + Scrap Sales].
    - Avg. Creditors Period = [Avg.(CRED_t, CRED_t-1) × 30 × No. of Months] / [Cost of Sales − Misc. Expenditure Written Off].
    - Working Capital Cycle = Avg. Inventory Period + Avg. Collection Period − Avg. Creditors Period.
    - Fixed Assets Turnover = [(TOI) × (12/No. of Months)] / [Avg.(Gross Block_t, Gross Block_t-1)]; Gross Block is **net of intangible assets such as goodwill**.
    - Working Capital Turnover = [(TOI) × (12/No. of Months)] / [Avg.(NWC_t, NWC_t-1)]; NWC = Total Current Assets − [Total Current Liabilities Related to Operations − Creditors for Capital Goods].
    - Current Ratio = Total Current Assets / [Total Short-term Debt (Including Current Portion of LT Debt/Fixed Deposits and Bills Discounted) + Total Current Liabilities and Provisions].
    - Quick Ratio = [Total Current Assets − Total Inventories] / [same ST-debt + current-liabilities denominator as Current Ratio].

- **DEFINITIONAL DIVERGENCES most relevant to the ICRA tool's known errors:**
  1. **Gearing/Total Debt EXPLICITLY includes acceptances/creditors on LC and capex LCs** — this is a named, verbatim line item ("Overall Gearing (Including Acceptances/Creditors on LC)"). Any workpaper that excludes LC-backed creditors/acceptances from gearing is using the wrong CareEdge definition.
  2. **Tangible Networth explicitly excludes revaluation reserves** and (generally) excludes non-core intangibles — a workpaper including revaluation reserves in net worth, or excluding a core-operations intangible, diverges from this definition.
  3. **CFO used in Total Debt/CFO is "cash generated from operations after adjusting for working capital changes"** — i.e., a cash-flow-statement-derived figure — but this is explicitly labelled as CFO, distinct from PBILDT/GCA which are P&L/accrual-derived. Substituting CFO for GCA or PBILDT (or vice versa) in the wrong ratio is a definitional error this document would catch.
  4. **Subordinated promoter loans move from debt to equity** — a common source of gearing/net-worth misclassification if the analyst doesn't check subordination terms.
  5. Corporate guarantees to subsidiaries/group entities are added to debt for "adjusted leverage ratios" — an easily missed off-balance-sheet leverage item.

- **Mechanical/bright-line checks worth coding:**
  - Gearing = (Total Debt incl. acceptances/LC creditors/lease liability/mobilisation advances backed by bank guarantees) / Tangible Networth (excl. revaluation reserve).
  - Interest Coverage = PBILDT / (Interest & Finance Charges − Amortisation of Premium on Debentures − Interest Capitalised).
  - Cash DSCR margin-money haircut = exactly 25% of incremental working capital.
  - TOI must be gross sales net of indirect taxes (GST/excise/sales tax/service tax) PLUS specified core-adjacent other income; interest/dividend/rental income must NEVER be included in TOI even if recurring — a coded check flagging any non-zero "interest income" or "dividend income" line inside a TOI calculation would catch this specific, previously-identified failure mode.
  - GCA add-back should EXCLUDE depreciation on ROU assets (Ind AS 116) — a check that ROU depreciation isn't double-added.

---

## Hybrid-Annuity-Road-Projects-March-2025.md

- **Scope:** Rating methodology for Hybrid Annuity Model (HAM) road projects (NHAI/MoRTH and state-awarded), covering SPVs formed for such projects. Not applicable to conventional toll/DBFOT BOT projects (only contrasted against them) or to non-road infrastructure.
- **Rating-factor structure (8 named risk factors):** (1) Funding Risk, (2) Sponsor Evaluation, (3) Project Implementation Risk, (4) Cashflow Risk, (5) O&M Risk, (6) Interest Rate Risk, (7) Liquidity, (8) Debt structure. Plus a separate note (9) on GST impact.
- **Indicative-metrics tables:** None with numeric bands/thresholds in the ICRA-style sense; instead contains several bright-line **structural/contractual parameters**:
  - Cash support for construction = **40% of BPC** payable by authority (NHAI/MoRTH projects; may vary for state HAM); balance **60%** funded by developer via debt+equity.
  - Equity commitment typically **12%–15% of BPC**.
  - PIM = weighted average of WPI:CPI in **70:30** ratio.
  - Interest annuity rate: **Bank rate + 3%** for projects awarded before Nov 2020; **average MCLR of top 5 scheduled banks + 1.25%** for projects awarded after Nov 2020.
  - Concession period = construction period (project-specific) + fixed **15-year** operations period.
  - Land availability threshold: **80% length of RoW** required before appointed date (3G basis).
  - Deemed-termination/provisional-COD trigger: completion of 100% work on available land within **180 days** of appointed date; if authority fails to provide balance RoW within **180 days**, portion removed from scope.
  - First annuity received **180 days** post PCOD/COD — hence 6 months' interest + routine maintenance funding recommended as part of project cost.
  - Roughness index range cited: **2000mm/km to 2500mm/km** (lower = better) affecting O&M cost.
  - Accelerated repayment structure preferred: **>50% of repayment in first half of tenor**.
- **Notching/support rules:** No formal notching-up/down scale given; qualitative — sponsor credit strength, explicit corporate guarantee till first annuity, DSRA/MMRA presence, waterfall/cash-trap/cash-sweep structural features, cross-default clauses all assessed qualitatively as rating strengths/weaknesses. No LT-ST mapping content.
- **Definitional divergences:** No TOI/PBILDT/TNW/gearing redefinition here — this is a project-finance/qualitative overlay methodology, not a ratio-definitions document. Does NOT modify the Financial Ratios document's definitions; it layers project-specific structural risk factors on top.
- **Bright-line checks worth coding:** 40%/60% BPC funding split; 12–15% equity-commitment band; 70:30 WPI:CPI weighting; interest rate formula (Bank rate+3% pre-Nov2020 / MCLR+1.25% post-Nov2020); 15-year fixed O&M period; 180-day annuity lag; 80% RoW threshold; >50% first-half repayment threshold — all are numeric, mechanically checkable if a HAM SPV is in scope, though none of the batch's ICRA errors (net worth, gearing, P&L decomposition) apply to this document.

---

## Independent-Credit-Evaluation-of-Residual-Debt-March-2025.md

- **Scope:** Independent Credit Evaluation (ICE) of **residual debt under RBI-mandated resolution plans** for stressed assets with exposure >Rs 100 crore (two CRAs mandatory if >Rs 500 crore). This is a distinct rating product from normal instrument/issuer credit ratings — not applicable to normal-course entities.
- **Rating scale:** RP1–RP7 (not CARE AAA–D). Verbatim definitions given for each of RP1 (highest safety, lowest credit risk) through RP7 (very high risk of default) — see table reproduced in source.
- **Rating-factor structure:** No numbered "factors" like other methodologies but 5 named analytical steps: (1) why the stress occurred & whether the RP addresses it, (2) capability of existing management to turn around (if not culpable), (3) competence of new management/promoters (if changed), (4) stress-testing of RP cash flows, (5) liquidity backup (DSRA funded/BG/promoter support).
- **Key definitional/threshold points:**
  - "Residual debt" = **aggregate debt (fund-based AND non-fund-based)** envisaged to be held by all lenders per the RP.
  - "Outstanding principal debt" includes **all credit facilities including debt/debt-like instruments** — NCDs, OCDs, optionally convertible preference shares, non-convertible preference shares. **Only equity and instruments compulsorily convertible into equity (without embedded optionality) are EXEMPT.** This is a stricter/broader "debt" definition than the general Financial Ratios document — relevant if the ICRA tool ever handles resolution-plan cases: OCDs/OCPS are debt here regardless of subordination nuance.
  - RP approval threshold: **75% of lenders by value AND 60% by number**. Inter-creditor agreement signing: within **30 days** of approval. Plan implementation: within **180 days** of invocation date.
  - "Specified period" = from RP implementation date until **at least 20% of outstanding principal debt (per RP) + capitalised interest sanctioned** is repaid; a default during this period (even with a different, non-defaulting lender) triggers a fresh RP requirement.
  - ICE is a **one-time exercise** — not subject to continuous surveillance (unlike normal ratings).
- **No LT-ST mapping, no notching/support rules of the parent/govt type** — irrelevant to this document's scope.
- **Bright-line checks worth coding:** Rs 100 crore / Rs 500 crore exposure thresholds (single vs dual CRA); 75%/60% RP approval thresholds; 30-day ICA signing window; 180-day implementation window; 20% principal-repayment threshold defining end of "specified period." These are only relevant if the ICRA tool is ever asked to process a resolution-plan/ICE case — not applicable to standard corporate/bank ratings, so low priority for the current audit's root-cause focus (misweighted scorecards / net-worth / gearing errors), but worth flagging that OCDs/OCPS are debt without exception here.

---

## Information_Adequacy_Risk-and-INC_Nov-2025.md

- **Scope:** Governs when/how CareEdge places an issuer in "ISSUER NOT COOPERATING" (INC) status, applicable across all sectors/rating types. Not a credit-risk-factor methodology.
- **No rating-factor structure, no financial-ratio tables, no notching/support rules** — purely a process/compliance policy document (SEBI circular-driven).
- **Bright-line thresholds (verbatim, all worth coding as compliance checks though not financial-ratio checks):**
  - Rating review cadence: NCD-instrument issuers reviewed **at least once a year** (SEBI); RBI requires review **at least once every 15 months**.
  - NDS (No-Default Statement) non-submission: **3 consecutive months** → migration to INC within **5 working days**.
  - Rating-fee non-payment: **60 days** from invoice/surveillance-due/anniversary date (whichever later) → INC.
  - Investment-grade INC rating downgraded to non-investment-grade with INC tag if **all outstanding ratings non-cooperative for more than 6 months**.
  - Cross-CRA INC rule: if an issuer's ratings from ALL other CRAs have been INC for **≥12 months**, CareEdge will not take up a new/initial rating assignment until cooperation resumes or ratings are withdrawn; if **<12 months** have passed, CareEdge may take up the assignment but must issue its own PR before the 12-month mark from the other CRA's INC PR.
  - Minimum information requirement annexures given per sector: Corporate (9 items), Infrastructure (11 items), BFSI (10 items) — includes NDS, latest AR, latest quarterly results, liquidity position, debt/repayment schedule, capex plans, lender/auditor/DT details, management interaction; BFSI additionally requires CAR, ALM statement, portfolio/AUM/GNPA data.
- **No definitional divergence relevant to TOI/PBILDT/TNW/gearing** — out of scope for the audit's core concern but useful for completeness (e.g., if the target company was ever near INC status, this sets the compliance triggers).

---

## Issuer_Ratings_Feb_2025.md

- **Scope:** CARE Ratings' "Issuer Rating" (IR) product — an issuer-specific (not instrument-specific) credit opinion over a ~3-year horizon, applicable to Manufacturing/Trading/Services/Infrastructure/Public Finance entities AND Banks/NBFCs/HFCs/FIs.
- **Rating-factor structure:** None of its own — the document explicitly delegates to the underlying sector methodologies: Rating Methodology – Manufacturing Companies, Wholesale Trading, Service Sector Companies, Infrastructure Sector Ratings, State Governments, Urban Infrastructure Projects (for corporates), and the Banks/NBFC/HFC/Insurance methodologies (for financial-sector issuers). No independent metrics/tables in this document itself.
- **No indicative-metrics tables, no notching rules, no LT-ST mapping.** Pure "scope and routing" document — essentially a two-page pointer stating IR uses the *same* methodology as instrument ratings, just issuer-level and non-instrument-specific, reviewed periodically, withdrawable on issuer's written request.
- **No definitional divergence** from generic/other CareEdge definitions — this file is boilerplate/routing, with essentially nothing analytically load-bearing beyond confirming that IR methodology = whichever sector methodology otherwise applies. State plainly: **largely a scope/routing document with no independent ratio definitions, factor tables, or thresholds of its own.**

---

## Liquidity Analysis of Non-Financial Sector Entities - Sept 2024.md

- **Scope:** Liquidity-risk-analysis approach for **non-financial sector** entities (also feeds short-term rating assessment). Cross-references the Financial Ratios – Non-Financial Sector document for turnover/liquidity ratios, and the "Rating Credit Enhanced Debt" criteria for parent/group guarantee support.
- **Rating-factor structure:** Not a scored-factor grid; a qualitative checklist of liquidity-analysis inputs: (1) Cash flows (near-term, generally next 4 quarters, but longer horizon for seasonal/lumpy-debt industries), (2) Availability of unencumbered cash & cash equivalents, (3) Investment in / loans to group entities (generally NOT considered liquid regardless of tenor classification), (4) Unutilised lines of credit (WC limits + undrawn term loans), (5) Liquidity support from parent/group, (6) Financial ratios (turnover + liquidity ratios, per the Financial Ratios document).
- **Key definitional content (highly relevant to the audit's "cash-flow figures substituted for P&L figures" concern):**
  - **Unencumbered cash and cash equivalents** definition given explicitly: cash balance, bank balance in current account, funds in liquid mutual funds, listed equity shares of large-cap/index entities (non-strategic), listed corporate bonds of highly-rated entities, government securities, unencumbered FDs.
  - **Encumbered cash and cash equivalents EXPLICITLY EXCLUDED from liquidity assessment:** funds in DSRA, margin money, and FDs earmarked against a loan/facility. Verbatim: "CARE Ratings generally does not factor the availability of such funds while assessing the available liquidity."
  - Unutilised WC limit quantum = comparison of monthly max/average utilisation against the **lower of** (a) sanctioned WC limits and (b) available drawing power, **typically over the preceding 12 months**. Consistently high utilisation flagged as a weak-liquidity signal.
  - CP is noted as "carved out of the working capital limits," implicitly creating a back-up liquidity facility whose adequacy depends on drawing power/lender willingness.
- **Liquidity descriptor scale:** Superior/Strong, Adequate, Stretched, Poor (4-level, non-numeric) — disclosed in press releases.
- **No numeric bright-line thresholds** beyond the "preceding 12 months" utilisation-review window — this is a qualitative/sources-vs-uses arithmetic exercise, consistent with the ICRA project's own Liquidity methodology approach (sources-vs-claims over ~12 months). No formulas with hard cutoffs to code mechanically, but the **unencumbered-vs-encumbered cash distinction is exactly the kind of definitional rule the audit should mechanically enforce** — i.e., a rule engine should flag any liquidity-section cash figure that isn't explicitly qualified as unencumbered (this mirrors failure mode 34/45 already logged in the ICRA project's own CLAUDE.md, confirming the underlying CareEdge source rule those failure modes are based on).

---

## Non-Life-Insurance-Sector-March-2025.md

- **Scope:** Rating Methodology & Financial Ratios for **Non-Life (General) Insurance sector** issuer ratings (business/financial strength assessment of policyholder-obligation-servicing ability); explicitly does NOT address policy-specific terms, deductibles, surrender/cancellation penalties, fraud defenses, or exchange-control restrictions on foreign claims. Distinct ratio set and factor structure from the non-financial-sector document — confirms sector-specific ratio sets exist and must not be cross-applied (directly relevant to the audit's "misweighted scorecard factors" root cause, since applying generic corporate ratios to an insurer would be a category error).
- **Rating-factor structure — "RAMELS" framework:** Risk Underwritten, Asset quality, Management, Earnings, Liquidity, Solvency (6 factors).
- **Indicative-metrics tables (verbatim formulas, no numeric bands given except regulatory minima):**
  - Growth: GDP(Gross Direct Premium) growth = (Current GDP − Prior GDP)/Prior GDP; NPE (Net Premium Earned) growth = (Current GDP − Prior GDP)/Prior NPE [note: formula as printed literally uses "GDP" in numerator for both rows — likely a document typo/OCR artifact for "Gross premium" vs "NPE," reproduce verbatim as printed].
  - Business: Risk retention = NPW/GPW; Market share = company premium/industry premium.
  - Profitability: Loss ratio = Net claims incurred/Net premium earned; Expense ratio = (Operating expenses + Commission expenses)/Net premium earned; **Combined ratio = Loss ratio + Expense ratio + Commission ratio**; Investment yield = Total investment income/Average total investments; Conservation ratio = Renewal premium collected/Total premium; Net earnings ratio = PAT/NPW; **Return on net worth = PAT/Average net worth**; Return on assets = PAT/Average assets.
  - Liquidity: Liquidity Coverage = Cash & cash equivalent/Technical Reserves; Liquidity Coverage incl. sub-debt = (Liquid Investments + Cash & cash equivalent)/(Technical Reserves + Sub-debt maturing in next year incl. interest). **Technical Reserves for General Insurance = Reserves for Unexpired Risk + Outstanding Claims Reserves** (footnote in doc also gives Life Insurance technical reserves formula, likely inherited from a combined template — flag as possible cross-document artifact).
  - Solvency: Solvency ratio = Available Solvency Margin/Required Solvency Margin — **regulatory minimum = 1.5x (150%)**, explicitly stated bright-line. Operating Leverage = NPW/Net worth. Financial Leverage = Subordinate debt/Net worth.
- **Hybrid capital (subordinated debt/preference shares) rules — bright-line, IRDAI-sourced, verbatim table:**
  - Quantum cap: **<25% of paid-up capital and <50% of net worth**.
  - Tenure: **≥10 years** (life/general/reinsurance) or **≥7 years** (health insurers).
  - Call option: earliest trigger **5 years** post-issuance; no put option permitted.
  - Solvency-margin inclusion haircut schedule by years-to-maturity: **5+ years = 100%; 4–<5 years = 80%; 3–<4 years = 60%; 2–<3 years = 40%; 1–<2 years = 20%; <1 year = 0%.**
  - Debenture redemption reserve: **25% of outstanding debentures** considered adequate; DRR itself excluded from solvency-margin liability computation.
  - Hybrid capital of insurers is generally **notched down** from the issuer rating (subordination to policyholders/creditors).
- **Definitional divergence relevant to audit:** This document confirms **"Net worth" here is NOT the "Tangible Networth" defined in the Financial Ratios – Non-Financial Sector document** — no revaluation-reserve exclusion or intangible-treatment language appears here; Operating Leverage and Financial Leverage use plain "Net worth," and RONW here = PAT/Average net worth (not "Tangible" net worth as in the generic document). This is a live risk if a workpaper imported the non-financial-sector TNW definition into an insurance-sector rating (or vice versa) — the two are NOT interchangeable per this corpus, paralleling the ICRA project's already-logged failure mode 32 (mixing sector conventions).
- **Bright-line/mechanical checks worth coding:** Solvency ratio ≥ 1.5x regulatory floor; hybrid-capital quantum cap (25% paid-up capital / 50% net worth); hybrid tenure floor (10y/7y); call-option floor (5y); solvency-inclusion haircut schedule (100/80/60/40/20/0% by year bucket); DRR adequacy threshold (25% of outstanding debentures).

---

## Notching by Factoring Linkages with Govt_Jan 2025.md

- **Scope:** Government (central/state) linkage notching for Public Sector Entities (PSEs) — applies as a building block ON TOP OF standalone credit assessment; not a standalone rating methodology.
- **Rating-factor structure:** 3 named linkage-strength factors: (a) Economic and strategic importance to centre/state (ownership/control extent, policy function served), (b) Demonstrated track record of government support (timely past support instances), (c) Legal or moral obligation to support (guarantees/LoCs/undertakings; probable sectoral impact of default).
- **No numeric indicative-metrics tables** — entirely qualitative. Notching outcomes described only in bands: "very strong" linkage → multiple-notch uplift, **potentially equated to sovereign rating (CARE AAA)** for centrally-critical entities; "moderate" linkage → rating falls "somewhere between" standalone and government rating; commercial PSEs with no dedicated policy function → assessed largely on standalone basis with **no significant notch-up**.
- **Notching/support rule (qualitative, no formula):** Explicit CE (Credit Enhancement) suffix and rating equated to guarantor (government) when an unconditional/irrevocable guarantee with structured payment mechanism exists (credit substitution principle) — cross-references the separate "Rating Credit Enhanced Debt" criteria (not in this batch).
- **No definitional divergence on TOI/PBILDT/TNW/gearing** — out of scope; this is a pure notching-overlay document. **No bright-line numeric thresholds present** worth a mechanical check (unlike the parent-linkage document, this one gives zero quantitative notch counts or ownership-percentage cutoffs — it is entirely qualitative judgment, "very strong"/"moderate"/standalone bands only).

---

## Notching_by_Factoring_Linkages_with_Parent_Jan_2025.md

- **Scope:** Non-government linkage notching — parent-subsidiary, group, JV, and PE-fund-portfolio-company relationships. Explicitly excludes government-linked entities (routed to the separate Govt-linkages document instead). Notes that a parent is "generally rated on a consolidated basis" UNLESS the subsidiary operates in a wholly different segment or is a ring-fenced SPV — directly relevant to the audit's "wrong net-worth basis" / consolidation-basis concern, since misapplying consolidated vs standalone basis is a definitional error class this document governs.
- **Rating-factor structure:** 4 covered scenarios: (1) Subsidiary rating (parent-subsidiary linkage strength factors: economic/strategic importance, shareholding extent, demonstrated support track record, cash-flow fungibility, legal/moral obligation — brand-sharing, common management/board, cross-default clauses), (2) JV rating linkages, (3) PE-fund-portfolio entities, (4) Group assessment (non-parent-subsidiary organized-group linkages).
- **No numeric indicative-metrics tables or bright-line thresholds** — entirely qualitative, "very strong"/"moderate" notch-band language identical in structure to the government-linkages document (multiple-notch uplift up to equating with parent rating; moderate linkage → falls between standalone and parent rating). One semi-quantitative anchor: notch-up is **capped at the extent of a parent's explicitly committed support amount** where such commitment is documented in writing/discussion — but no percentage or notch-count given.
- **Notch-DOWN rule for subsidiaries of weak parents:** rating may be capped to the parent's rating if the parent has significant control and a track record of extracting support from the subsidiary (elongated credit terms, differentiated pricing, additional debt burden, high dividend upstreaming) — UNLESS subsidiary cash flows are ring-fenced by loan covenants, in which case standalone assessment applies (rating can exceed parent's, no cap).
- **Banking/Financial Services sector carve-out:** parent and subsidiary/group entity ratings tend to be equalized or closely aligned due to high integration, common brand, shared treasury, and reputational-contagion risk from regulatory group structures (RBI/NHB/IRDAI-driven multi-entity structures).
- **Definitional divergence relevant to audit:** This document is the CareEdge authority on **consolidation basis** determination (parent rated consolidated unless subsidiary is a different-segment business or ring-fenced SPV) — a rating tool computing net worth/gearing on the wrong basis (standalone vs consolidated) for a parent with integrated subsidiaries would violate this document's default rule. No formula-level definitions of TOI/PBILDT/TNW/gearing appear here (out of scope for this document — those live in the Financial Ratios document).
- **No bright-line numeric thresholds** worth mechanical coding — purely qualitative linkage-strength judgment, same as the government-linkages document.

---

## Policy on Curing Period_Dec 2024.md

- **Scope:** CareEdge's policy on the "curing period" — the minimum time before a rating can be upgraded from Default grade ('CARE D') following payment regularisation. Cross-references the separate "Policy on Default Recognition" document (not in this batch) for default-recognition rules (one-day-one-rupee delay for scheduled-repayment instruments; 30-day grace for non-scheduled facilities).
- **No rating-factor structure or indicative-metrics tables** — a pure default-recognition/curing-period compliance policy, not a credit-analysis methodology.
- **Bright-line thresholds (verbatim, exact numbers):**
  - **Curing period: generally 90 days** for upgrade from Default to Non-Investment Grade.
  - **Curing period: generally 365 days** for upgrade from Default to Investment Grade.
  - Upgrade before expiry of the curing period is permitted only if defaulted payments are regularised AND CareEdge's analytical judgment supports low recurrence likelihood; enumerated qualifying "credit reasons" (ownership/management change, sizeable long-term fund inflow, favourable regulatory change improving liquidity, additional funding/refinancing) and "non-credit reasons" (force majeure, payment-mechanism/systems failure not linked to liquidity, incorrect/dormant investor account details, or escrowed payment already made).
  - Rule: default-grade rating for an instrument/facility "shall not be upgraded unless **all instruments/facilities of similar seniority** are cured of their defaults"; for subordinate/structured instruments, curing period applies at the instrument/facility level (not issuer-wide).
- **No definitional divergence on TOI/PBILDT/TNW/gearing** — out of scope; purely a default/curing-period compliance rule.
- **Bright-line checks worth coding:** 90-day (non-investment-grade) and 365-day (investment-grade) curing-period counters from date of default-payment regularisation; same-seniority "all facilities must cure together" rule as a validation gate before any upgrade-from-D action.

---

# Summary note for the audit

The single most consequential file in this batch for explaining the ICRA-tool's traced errors is **Financial_Ratios_Non_Financial_Sector_March_2025.md**. It establishes, in exact and testable form:
1. Gearing/Total Debt **must include** acceptances/creditors on LC, capex LCs, lease liabilities, and BG-backed mobilisation advances — omitting these understates leverage and could produce an inflated rating (consistent with the reported A− vs BBB miss).
2. Tangible Networth **excludes revaluation reserves** and generally excludes non-core intangibles — including them overstates net worth and understates gearing/overstates RONW.
3. TOI/PBILDT are strictly operating-income/operating-expense constructs; interest/dividend/rental income must never enter TOI even if recurring — a common source of margin/coverage-ratio inflation if miscoded.
4. Distinct CFO-based ratios (Total Debt/CFO) exist alongside GCA/PBILDT-based ratios — substituting cash-flow-statement figures into GCA- or PBILDT-denominated ratios (or vice versa) is a definitional error this document's explicit ratio-by-ratio formula structure would catch.
5. The **Non-Life Insurance** document confirms sector-specific ratio sets (RAMELS, plain "Net worth" not "Tangible Networth") are NOT interchangeable with the non-financial-sector definitions — reinforcing that a scorecard must select the correct sector convention set, not a generic one.

# Part 6 — CareEdge Methodology Corpus Review

## Policy on Default Recognition_Jan 2025.md

- **Scope:** Applies to all CARE Ratings-rated debt: (A) listed/proposed-to-be-listed debt securities (per SEBI master circular) and (B) all other facilities/instruments (bank loans, CP, CDs/FDs, packing credit, buyer's credit, bill discounting, cash credit/OD, LCs, BGs). Excludes nothing explicitly, but the default-recognition rules differ materially between the two categories.
- **Rating-factor structure:** Not a scorecard — this is a default-definition and treatment-of-default policy, not a rating-factor methodology. Structure: (1) Definition of default for listed debt; (2) Definition of default for other facilities/instruments; (3) Criteria for treatment of default in initial ratings; (4) Treatment in review of outstanding ratings; (5) Default on unrated facilities of similar seniority; (6) Treatment for hybrid instruments.
- **Indicative-metrics tables (verbatim):**
  - Table A (listed securities):
    | Financial Instrument | Rating Scale | Definition of Default |
    |---|---|---|
    | Debentures/Bonds | Long-Term | A delay of 1 day even of 1 rupee (of principal or interest) from the scheduled repayment date |
    | Commercial Paper | Short Term | (same) |
    | Rescheduled instrument | — | Non-servicing per existing terms in anticipation of favourable restructuring response = default; lender-initiated reschedule before due date is NOT default unless done to avoid default/bankruptcy |
    | Curing Period | — | Generally 90 Days for upgrade Default→Non-Investment Grade; generally 365 Days for upgrade Default→Investment Grade |
  - Table B (other facilities):
    | Facility | Rating Scale | Definition of Default |
    |---|---|---|
    | Term Loan / WC Term Loan / WC Demand Loan / Debentures/Bonds | LT | 1 day/1 rupee delay from scheduled repayment date |
    | CD/FD | ST/LT | same |
    | Commercial Paper | ST | same |
    | Packing Credit (Pre-shipment) | ST | Overdue/unpaid > 30 days |
    | Buyer's Credit | ST | Continuously overdrawn > 30 days |
    | Bill Purchase/Discounting/FBD/Negotiation | ST | Overdue/unpaid > 30 days |
    | Cash Credit | LT | Continuously overdrawn > 30 days |
    | Overdraft | ST | Continuously overdrawn > 30 days |
    | Letter of Credit | ST | Overdue > 30 days from day of devolvement |
    | Bank Guarantee (Perf/Financial) | ST | Unpaid > 30 days from invocation |
    | Curing Period | — | 90 Days (Default→Speculative Grade); generally 365 Days (Default→Investment Grade) |
  - Grace-period footnote: if sanctioned terms allow a grace period, the due date used is after the grace period.
  - Guarantee-backed facility with SPM structured payment mechanism: "T-" structure = due date T, missed payment on T triggers default; "T+x" structure = default recognized if not paid by T+x day (x close to T).
- **Notching/support/mapping rules:** Curing-period rules described above are the core "notching-adjacent" rule (grade migration timing after default). Hybrid instruments: any delay in interest/principal following invocation of a lock-in/deferment clause is an event of default, and "these instruments may exhibit a somewhat sharper migration of the rating compared with conventional subordinated debt instruments" — i.e., faster/sharper downward notching for hybrids on default-adjacent events. Cross-default treatment: default on one facility/instrument generally moves ALL facilities of similar seniority (and the issuer rating) to "near default" or CARE D, unless strong instrument-specific mitigants exist. Default-free track record required: generally 90 days for non-investment-grade/speculative-grade rating (other than D), 365 days for investment-grade rating, before assigning initial rating or moving rating up from D.
- **Definitions differing from generic/ICRA usage:** This document is entirely about default definition, not financial-statement definitions — no TOI/PBILDT/TNW/gearing definitions appear here. Nothing on net-worth basis, gearing inclusions, or P&L/cash-flow substitution is addressed in this file.
- **Mechanically checkable thresholds:**
  - "1 day, 1 rupee" delay = default for LT/ST instruments with scheduled repayment (listed debt and facilities with pre-defined repayment schedule).
  - ">30 days" overdue/overdrawn/unpaid threshold for facilities with no pre-defined repayment schedule (cash credit, OD, LC, BG, packing credit, buyer's credit, bill discounting).
  - Curing period: 90 days (default→non-investment/speculative grade) vs 365 days (default→investment grade) — both for initial-rating assignment and outstanding-rating upgrades. These are hard, codeable cutoffs directly relevant to any automated "can this entity be upgraded out of default" check.

## Policy-on-Assignment-of-Provisional-Ratings_Dec-2025.md

- **Scope:** Governs when/how CareEdge assigns "Provisional" ratings — pending execution of critical documents (LOC, corporate guarantee, DTD/DTA, legal agreements, term sheet, loan-pool assignment/escrow, DSRA, escrow account) or, for REITs/InvITs, pending trust formation post SEBI registration. Explicitly excludes: provisional ratings are NOT assigned for an issuer merely evaluating strategic decisions (funding mix for a project, acquisition, debt restructuring, refinancing scenario-analysis).
- **Rating-factor structure:** Not a credit-factor scorecard; it is a process/validity policy. Structure: (1) When provisional ratings are assigned; (2) Validity period (unplaced instruments — 12 months + 6-month extension = up to 18 months, with case-by-case extension beyond); (3) Validity for placed instruments (180 days to submit documents post-issuance); (4) Material-change-in-terms handling; (5) Validity for REIT/InvIT/AIF issuer ratings (90 days + up to 90-day extension); (6) Press-release disclosures; (7) Unaccepted-rating disclosures.
- **Indicative-metrics tables:** None — no numeric scorecard tables. Only process timelines (see thresholds below).
- **Notching/support/mapping rules:** None directly (no notching framework); however it does specify that on conversion to final rating, "the rating that would have been assigned in absence of the pending steps" must be disclosed — implying a counterfactual/comparator rating must be stated in every provisional press release.
- **Definitions differing from generic/ICRA usage:** No financial-statement definitions in this document (no TOI/PBILDT/TNW/gearing).
- **Mechanically checkable thresholds:**
  - Funds not raised within 12 months + no fundraising plan in next 6 months → rating withdrawn.
  - Funds not raised within 18 months total (12+6) → reviewed for withdrawal; extension beyond 18 months only case-by-case/exceptional.
  - Funds raised → maximum 180 days from issuance date to submit final documents, else reviewed for withdrawal (with simultaneous fresh rating based on record).
  - REIT/InvIT/AIF issuer ratings: 90-day base validity + up to 90-day extension (i.e., max 180 days), computed from completion of fund-raising/issuance of units.

## Policy-on-Withdrawal-of-Ratings_Oct-2025.md

- **Scope:** Governs conditions for withdrawing an outstanding CareEdge rating across instrument types: capital-market securities (bonds/NCDs), bank facilities, perpetual debt (AT1), open-ended mutual fund schemes, issuer ratings, CP/CDs, security receipts, and fixed deposits. Covers full redemption, unplaced proposed debt, merger/amalgamation/liquidation, transfer of rated instrument, provisional-rating withdrawal (cross-refers to the provisional policy), and CE-rating withdrawal.
- **Rating-factor structure:** Process/eligibility policy, not a credit scorecard.
- **Indicative-metrics tables (verbatim):** FD withdrawal scenarios table (a/b/c) reproduced in the source with procedural conditions (NOC, auditor/trustee certificates, escrow) rather than numeric thresholds, apart from the timing rules below.
- **Notching/support/mapping rules:** CE (credit-enhanced) rating withdrawal: if credit enhancement ceases/terms change, the CE rating is reviewed for withdrawal and a new standalone rating is simultaneously assigned; if the CE mechanism fails to work as anticipated (rather than ceasing to exist) — rating is instead revised downward per the Default Recognition policy, not withdrawn/reassigned.
- **Definitions differing from generic/ICRA usage:** None — no financial ratio/statement definitions in this document.
- **Mechanically checkable thresholds (bright-line, codeable):**
  - Single rating on a capital-market instrument: withdrawal only if rated continuously for 5 years OR 50% of tenure (whichever longer) + NOC/undertaking conditions.
  - Multiple ratings on same instrument: withdrawal earlier allowed if rated continuously for 3 years OR 50% of tenure (whichever longer) + NOCs from ≥75% of bondholders by value + undertakings.
  - Perpetual debt (AT1) listed/proposed-listed: withdrawal only after continuous rating for 5 years + undertakings.
  - Open-ended MF schemes: placed on "Notice of Withdrawal" for 30 days before withdrawal.
  - FD rated 'CARE D' continuously for 3 years → withdrawn.
  - FD Notice-of-Withdrawal period (if NOC unavailable but other conditions met): 1 year before withdrawal.

## Project_Stage_Entities_Feb_2025.md

- **Scope:** Covers CARE Ratings' criteria for rating project-stage entities in the MANUFACTURING sector specifically (not infrastructure sub-sectors like road/power/port, which have their own separate methodologies, and not urban-infra projects — both explicitly excluded/referred elsewhere). For operational entities, sector-specific methodologies apply instead; this document is only for the pre-operational/construction phase of manufacturing projects.
- **Rating-factor structure:** Six named risk categories: I. Promoter and management risk; II. Construction risk; III. Financial risk; IV. Industry risk; V. Business risk; VI. Environmental, Social and Governance (ESG) risk. Within Financial risk: project cost reasonableness, financial closure extent, timely equity infusion, project leverage/funding mix, and Project DSCR (sensitised).
- **Indicative-metrics tables:** None — this document is entirely qualitative/narrative; no numeric bands or thresholds are given for DSCR, leverage, or any other ratio. It states CARE Ratings looks at "sensitised DSCRs" and debt-equity mix comparisons to similar projects but publishes no benchmark numbers.
- **Notching/support/mapping rules:** States ratings for project-stage entities "are generally not placed at the higher end of the rating scale, unless an entity is a part of a very strong parent/group" with strong economic incentive and moral obligation to support — a qualitative support-notching principle, not a quantified one. No LT-ST mapping or hybrid rules here.
- **Definitions differing from generic/ICRA usage:** None given — no TOI/PBILDT/TNW/gearing definitions in this document.
- **Mechanically checkable thresholds:** None — purely qualitative/judgmental document ("Rating determination is a matter of experience and holistic judgement of the Rating Committee"). Not suitable for mechanical scorecard checks as written.

## REIT Methodology January 2025.md

- **Scope:** Rating of consolidated debt at the REIT level only. Explicitly states: the rating does NOT signify unitholder returns, does NOT predict NAV performance, is NOT a rating of REIT units, and is NOT an indicator of individual asset credit quality within the REIT's portfolio. Covers listed REITs and references SM (small-and-medium) REITs briefly.
- **Rating-factor structure:** Three main pillars per the methodology diagram: (1) Management Evaluation (experience/track record of REIT managers, asset acquisition/diversification strategy, overall REIT structure); (2) Operational Risk Assessment (location/asset type/construction quality, market standing & demand-supply outlook, occupancy level, tenants' profile, lease-agreement evaluation); (3) Financial Risk Assessment (liquidity, debt financing & sanction terms, leverage & capital structure, cash flow analysis). Plus ESG (Environmental/Social/Governance).
- **Indicative-metrics tables (verbatim, regulatory limits reproduced from SEBI guidelines, used as rating inputs):**
  | Regulatory feature | Threshold |
  |---|---|
  | Sponsor minimum holding | ≥15% of total REIT units, post-issue, for 3 years from listing |
  | Asset mix | ≥80% of REIT asset value in completed, rent-generating properties; ≤20% in under-construction assets |
  | Diversification | REIT must invest in ≥2 projects, with no single project >60% of REIT asset value |
  | Leverage cap | Aggregate consolidated debt + deferred payments, net of cash & cash equivalents, ≤49% of REIT asset value (consolidated basis) |
  | External rating trigger | Mandatory external rating once consolidated debt + deferred payments (net of cash) exceeds 25% of asset value |
  | Holdco structure | REIT must hold ≥50% equity in Holdco; REIT's ultimate holding in underlying SPV ≥26%; REIT/Holdco must hold ≥50% controlling stake in SPVs |
  | Distribution | SPVs must distribute ≥90% of net distributable cash flows to REIT/Holdco; Holdco must distribute 100% of cash flows realised from SPVs + ≥90% of remaining cash flows |
  | Manager tenure | Auditor appointed for max 5 consecutive years; no valuer for the same project for >4 consecutive years |
  | Valuation frequency | Full valuation ≥once/year, within 3 months of FY-end; half-yearly valuation (Sept 30 year-end) within 45 days |
  | NAV disclosure | Declared within 15 days of valuation; done ≥once every 6 months |
- **Notching/support/mapping rules:** No explicit notching table; but WALE (weighted average lease expiry) vs. average maturity of outstanding debt is used to assess lease-renewal risk — a structural matching test rather than a numeric notch. Escrow/waterfall mechanisms, DSRA presence, and cross-default clauses are all treated as qualitative credit-positive structural features.
- **Definitions differing from generic/ICRA usage:** Coverage ratios specific to REITs: "debt/rental", "debt/PBILDT" (Profit Before Interest, Lease Rentals, Depreciation and Taxation — note PBILDT here explicitly includes "Lease Rentals" in its definition, a REIT-specific variant vs. the standard PBILDT used elsewhere in the corpus), and "cash coverage ratio." Consolidated approach is explicitly mandated for cash-flow adequacy assessment (pooling benefit via SPV mandatory distribution, common management control, cross-default clauses) — i.e., REIT financial risk is assessed on a CONSOLIDATED basis by design, unlike some corporate methodologies where standalone/consolidated is a judgment call.
- **Mechanically checkable thresholds:** The SEBI regulatory limits above (49% leverage cap, 25% external-rating trigger, 80/20 asset mix, 60% single-project cap, 15% sponsor holding, 90%/100% distribution rules, 5-year auditor tenure, 4-year valuer tenure) are all precise, bright-line, and directly codeable as compliance checks against REIT financial disclosures — much more so than in most other files in this batch.

## Rating Methodology  Thermal Power Producers - December 2024.md

- **Scope:** Rating methodology for debt issues of THERMAL power projects (coal/lignite/gas/diesel) specifically — explicitly distinguished from nuclear and renewable (solar/wind/hydro/biomass) generation, which are covered elsewhere. Covers both project (under-construction) and operational thermal power entities.
- **Rating-factor structure:** Six named factors: (1) Promoter group and management team; (2) Project implementation risk (land/permitting, construction risk, evacuation infrastructure, financial closure); (3) Project operations/Business risk (demand-supply, revenue risk/PPA type, fuel supply risk, plant efficiency/cost competitiveness, off-taker risk, force majeure, other operational risks); (4) Regulatory risk; (5) Financial risk (future cash flows, leverage, DSCR, liquidity back-ups); (6) ESG risk.
- **Indicative-metrics tables:** No numeric scorecard/threshold table is given (unlike REIT methodology's SEBI limits). Only a table of the six top-level rating factors (Promoter/management, Project implementation, Operation/Business, Regulatory, Financial, ESG) with no associated numeric bands.
- **Notching/support/mapping rules:** Qualitative PPA-type ranking used as an implicit notching driver: long-term cost-plus PPA covering full loan tenor is viewed most positively → long-term competitively-bid PPA next → medium-term PPA next → short-term/merchant sales least favourably (highest risk). Weightage to promoter/parent support is explicitly stated to shift over the project lifecycle: "for an under-construction project... higher weightage [to promoter]... once operational, weightage to promoter group is relatively on lower side... higher weightage is given to quality of the asset" — i.e., support weighting itself is a function of project stage, a nuance any scorecard should capture.
- **Definitions differing from generic/ICRA usage:** Explicitly defines a sector-specific leverage ratio: **"Total debt to profit before interest, lease, depreciation, and taxation (TD/PBILDT)"** — used specifically "to nullify the effect of depreciation on leverage indicators" for power projects (capital-intensive, front-loaded depreciation). This PBILDT explicitly includes "lease" in its own name (Profit Before Interest, LEASE, Depreciation and Taxation) — consistent with REIT methodology's variant, and different from a plain OPBDIT/EBITDA that a rating tool might otherwise assume. Debt-equity funding norm for thermal projects stated as typically 70:30 (used as a comparator/benchmark, not a binding threshold). Liquidity back-up explicitly quantified: DSRA sized to cover "1-2 quarters of debt repayment obligations." References its own standard financial-ratio methodology ("Financial ratios – Non-Financial Sector") and Liquidity Analysis methodology for the rest of the ratio suite — meaning the general corporate ratio definitions (and any errors therein, e.g., wrong TNW basis or wrong gearing inclusions) would flow directly into thermal-power ratings too.
- **Mechanically checkable thresholds:**
  - DSRA coverage: 1-2 quarters of debt repayment.
  - Debt:equity funding norm ~70:30 (soft benchmark, not hard cutoff).
  - Off-taker payment track record review window: 6-12 months of monthly billing/payment data (case-to-case).
  - No hard numeric rating-notch cutoffs are given; the file is qualitative apart from the above operational benchmarks.

## Rating Methodology - Auto Components & Equipments 2025.md

- **Scope:** Covers auto ancillary/component manufacturers (Tier-I/II/III suppliers to OEMs), across product complexity levels — from technology-intensive engine/fuel-system parts to simple sheet-metal parts — including both domestic OEM-focused and export-oriented players. No explicit exclusions stated beyond noting this supplements (does not replace) the general manufacturing-sector methodology.
- **Rating-factor structure:** (1) Promoters/Management Risk; (2) Business/Operations Risk — market share & vendor tier (Tier-I/II/III), product complexity/technology intensity, quality certifications (Six Sigma/Kaizen/TQM/ISO), obsolescence risk (EV transition, ADAS), diversification (clientele, product mix, geography, OEM vs. replacement-market revenue mix), plant location/logistics, raw-material sourcing & cost control, nature of OEM contracts (revenue visibility, cost pass-through clauses, credit terms), regulatory conformity (BS-VI etc.); (3) Financial risk (defers fully to the general "Financial Ratios – Non-Financial Sector" criteria — cash-flow analysis and free-cash-flow generation emphasized); (4) ESG.
- **Indicative-metrics tables (verbatim, industry-structure stats, not rating bands):**
  - Organised sector: ~75-80% of domestic sales.
  - OEM segment: 65-70% of industry turnover; exports 22-25%; replacement market 11-12% (note: these three numbers as stated sum to ~98-107%, an internal inconsistency in the source document itself, reproduced verbatim).
  - India's auto component exports: <2% of global trade in auto components.
  - No rating-scorecard numeric thresholds (no leverage/coverage bands) are given in this file — financial risk is entirely delegated to the generic Financial Ratios methodology.
- **Notching/support/mapping rules:** Vendor-tier hierarchy is used as an implicit positioning factor: Tier-I (direct OEM relationship, higher profitability, viewed as "superior") > Tier-II > Tier-III. No explicit numeric notch adjustment given.
- **Definitions differing from generic/ICRA usage:** None defined in this document itself — it explicitly refers financial-ratio definitions out to "CARE Ratings' criteria 'Financial Ratios – Non-Financial Sector'" rather than restating them. No sector-specific TOI/PBILDT/TNW/gearing variant is introduced here (unlike REIT/Thermal Power files, which do modify PBILDT).
- **Mechanically checkable thresholds:** None of true bright-line rating-relevant nature — the only numeric figures are macro/industry-structure statistics (75-80%, 65-70%, 22-25%, 11-12%, <2%), useful only as sector-context checks, not as company-level scoring cutoffs.

## Rating Methodology - Cotton Textile Manufacturing - December 2024.md

- **Scope:** Covers the full cotton textile value chain — cotton spinning, fabric manufacturing (weaving/knitting/processing), and garment manufacturing — for entities operating in one or multiple segments. No explicit sector exclusions; supplements the general manufacturing-sector methodology. (Note: page headers in the source document erroneously repeat "Rating Methodology – Non-Banking Finance Companies," an artefact of the source PDF/markdown conversion, reproduced faithfully — not an actual scope statement for NBFCs.)
- **Rating-factor structure:** A. Business and Operational Risks — Operational Efficiency (raw-material cost per segment: spinners/fabric/garment differ in exposure), Inventory Management (seasonal cotton procurement cycle, Oct-Feb harvesting), Scale and Flexibility, Level of Integration (backward/forward), Geographical and Customer Diversification, Fiscal Incentives and Regulatory Risks (ATUFS, SITP, RoSCTL, MSP); B. Financial Risk — Liquidity management, Capital structure and debt coverage indicators, Foreign exchange risk; plus ESG.
- **Indicative-metrics tables:** No numeric threshold table with rating bands. The ratios named (see below) are listed without associated strongly/weakly-positioned numeric cutoffs — purely a list of ratios "analysed," referring the reader to the separate Financial Ratios – Non-Financial Sector criteria for detail.
- **Notching/support/mapping rules:** None explicit — no parent-support or hybrid-instrument notching discussion in this sector document.
- **Definitions differing from generic/ICRA usage:** Named ratio list (verbatim): "long-term debt/tangible net worth; total-debt/tangible networth; total debt/profit before interest, lease, depreciation, and taxation (PBILDT); total outside liabilities/tangible networth; PBILDT/Interest cost; debt service coverage ratio." Notably: (a) explicitly uses TANGIBLE net worth as the gearing/TOL denominator (consistent with generic ICRA/CARE convention of excluding intangibles), and (b) again defines PBILDT to explicitly include "lease" ("profit before interest, LEASE, depreciation, and taxation") — the third file in this batch (after REIT and Thermal Power) to embed "lease" inside the PBILDT acronym itself, which is a detail a mechanical ratio engine must get right per methodology rather than assuming a plain EBITDA. No cash-flow-statement-vs-P&L substitution issue is raised in this document.
- **Mechanically checkable thresholds:** None — entirely qualitative on rating factors; the ratio LIST itself (not thresholds) is the only concretely codeable element (i.e., "must compute LT-debt/TNW, TD/TNW, TD/PBILDT, TOL/TNW, PBILDT/interest, DSCR for this sector").

## Rating Methodology - Education Sector December 2024.md

- **Scope:** Covers formal education (K-12, graduation/post-graduation), and touches vocational/informal (pre-school, coaching) segments and "for-profit" entities managing education infrastructure on behalf of owners. Entities are typically registered as Trusts/Societies (not standard corporates) — this affects accounting-basis analysis (see below). No explicit exclusions stated.
- **Rating-factor structure:** A. Management Risk (promoter experience/resourcefulness); B. Business Risk (track record/reputation, enrolment ratio & trend, course diversity, entity size/geographic diversification, placement track record, faculty/infrastructure quality, revenue stability/trend, surplus margin trend); C. Regulatory Risk (UGC/AICTE/other regulator oversight, institute autonomy status — Affiliated/Autonomous/Private University/Deemed University, seat-sharing & fee-fixation rules, risk of course/seat non-renewal, Right to Education Act 25% reservation, Trust/Society accounting-basis quirks); D. Financial Risk (cash-flow seasonality, need for continuous capex); E. ESG.
- **Indicative-metrics tables:** No numeric threshold table — enrolment ratio is named as a key metric ("ratio of actual intake to sanctioned intake") but no specific strongly/weakly-positioned band is given.
- **Notching/support/mapping rules:** None explicit (no parent-support/hybrid rules); institute "status" (Affiliated < Autonomous/Private University/Deemed University in terms of pricing/curriculum flexibility) functions as a qualitative positioning factor, not a numeric notch.
- **Definitions differing from generic/ICRA usage:** Two important sector-specific accounting/definitional notes: (1) Trusts/Societies "may follow cash-basis for accounting income and accrual-basis for expenses" — a MIXED-BASIS accounting practice explicitly flagged as requiring "suitable adjustments... in the analysis" — i.e., the methodology itself warns that P&L figures for education-sector Trusts may not be prepared on a consistent accrual basis, and analysts must adjust rather than take reported income/expense at face value. (2) 85% utilisation rule for tax exemption: trusts/societies/Section 8 companies must use 85% of gross receipts toward the trust's objectives, and this "permitted use" includes regular opex AND interest/principal repayment — meaning continuous capex is often funded by cash that would otherwise reduce leverage, a structural driver of persistently high capex/leverage in this sector that the methodology explicitly calls out. (3) Explicitly states "traditional liquidity ratios are not meaningful while analysing most educational institutes" because fees are collected in advance and receivables are negligible — a sector-specific override of standard liquidity-ratio analysis.
- **Mechanically checkable thresholds:** Right to Education Act: 25% of seats must be reserved (with government fee reimbursement) — a precise, codeable statutory percentage relevant to revenue/receivable analysis (reimbursement delay risk). No other bright-line numeric cutoffs.

## Rating Methodology - Non - Ferrous Metals September 2024.md

- **Scope:** Covers PRIMARY non-ferrous metal (NFM) manufacturers — specifically aluminium, copper, zinc, and lead (the "four widely used base metals"); rare/precious metals (gold, silver, cobalt, mercury, tungsten) are mentioned as part of the broader NFM universe but the methodology's detailed treatment is limited to the four base metals and to PRIMARY (ore-based) manufacturing route, as distinct from secondary/scrap-based recycling route.
- **Rating-factor structure:** A. Industry risk (trade activity/economic cycle, demand-supply, raw-material/finished-goods price trend, inventory position, regulatory changes, substitution risk); B. Business risk — (i) Market position (size/market share, geographical diversity, downstream product diversity — value-added flat products/extrusions/foils/wires/rods vs. commoditised ingots), (ii) Operating efficiencies (raw-material criticality, energy cost, technology/plant quality, plant location/logistics); C. Promoter and management risk; D. Financial risk (per generic Financial Ratios – Non-Financial Sector criteria); E. Key ratios (sector-specific, listed below); F. Foreign exchange fluctuation risk; G. ESG.
- **Indicative-metrics tables (verbatim):**
  - Section E, "Key ratios" (a plain bullet list, no numeric bands given): Total cost/metric tonne (MT); Power cost/MT; Kwh/MT (power consumption); PBILDT/MT; Total Debt/Installed Capacity (per MT); Total Debt/PBILDT.
  - Industry-context statistics (not rating thresholds, but operational benchmarks reproduced verbatim): Energy cost "as high as 35% for aluminium" of total cost of production; aluminium production requires "~14,000-15,000 kWh of power to produce a tonne metal"; zinc manufacturing "~3,500 kWh of power"; logistics cost "accounts for ~5-15% of NFM manufacturing companies' total cost of production"; "~7-8 tonnes of raw material" (incl. "six tonnes of bauxite") required to manufacture one tonne of aluminium.
- **Notching/support/mapping rules:** None explicit — no parent-support/hybrid notching discussion. Qualitative positioning: companies with captive raw-material supply (mines/long-term contracts), captive power plants (CPP), and downstream/value-added product mix are viewed favourably vs. commodity ingot producers with market-sourced inputs.
- **Definitions differing from generic/ICRA usage:** Introduces PER-TONNE (per-MT) denominators not used in most other files in this batch: Total cost/MT, Power cost/MT, PBILDT/MT, Total Debt/Installed Capacity (per MT) — i.e., leverage here is scaled to installed CAPACITY (per MT) as well as to PBILDT, a sector-specific normalisation. Total Debt/PBILDT (not TD/PBILDT with "lease" spelled out, unlike REIT/Thermal Power/Cotton Textile files — here it is plain "PBILDT" without the explicit lease-inclusion language, though presumably the same underlying agency-wide PBILDT definition applies from the cross-referenced generic criteria). No explicit statement here on TNW basis, gearing inclusions (LC-backed creditors/acceptances), or cash-flow vs P&L substitution — this file defers entirely to the generic Financial Ratios methodology for those definitions.
- **Mechanically checkable thresholds:** The per-MT cost/energy benchmarks (35% aluminium energy-cost share, 14,000-15,000 kWh/MT aluminium, 3,500 kWh/MT zinc, 5-15% logistics-cost share, 7-8 tonnes raw material per tonne aluminium output) are precise enough to be used as sector sanity-check ranges (e.g., flagging an extracted "power cost per MT" or "raw material consumption ratio" that falls wildly outside these bands as a probable extraction/decomposition error) even though they are not themselves rating-grade cutoffs.

---

## Cross-cutting notes relevant to the audit's root-cause hypothesis

1. **PBILDT variant with "lease" embedded:** Three of the ten files (REIT, Thermal Power, Cotton Textile) explicitly spell out PBILDT as "Profit Before Interest, **Lease** Rentals, Depreciation and Taxation" — i.e., the CareEdge PBILDT convention bakes in lease rentals as part of the metric's own definition in these sectors. A rating tool using a plain OPBDIT/EBITDA (excluding lease treatment, or treating leases inconsistently) for these three sectors would misstate PBILDT and every ratio downstream of it (PBILDT margin, TD/PBILDT, DSCR-adjacent measures) — directly relevant to the "misweighted scorecard factors" and "wrong gearing inclusions" failure modes named in the audit brief.
2. **Consolidation basis is sector-mandated, not a free choice, for REITs:** The REIT methodology explicitly REQUIRES a consolidated approach to cash-flow adequacy (SPV pooling, common management, cross-default clauses) — using a standalone REIT-level P&L/BS instead of the consolidated REIT+SPV structure would be a direct methodology violation, structurally similar to the "wrong net-worth/consolidation basis" error class named in the audit.
3. **Education-sector accounting-basis warning:** The Education Sector file is the only one in this batch to explicitly flag that source entities (Trusts/Societies) may present P&L on a MIXED cash/accrual basis, and that suitable adjustments are required before ratio computation — directly relevant to the "aggregate P&L notes not decomposed" / "cash-flow figures substituted for P&L figures" failure class, since a naive extraction here risks conflating cash received with accrued income.
4. **Tangible net worth is the explicit denominator in Cotton Textile:** This file is explicit that gearing/leverage ratios use TANGIBLE net worth (not total net worth including intangibles/revaluation reserves) — consistent with the general ICRA/CARE convention flagged elsewhere in the corpus review, and worth cross-checking against whatever TNW basis the rating tool is actually using for textile-sector companies.
5. **No file in this batch explicitly discusses LC-backed creditors/acceptances/buyers' credit treatment as debt**, nor does any of the ten files define TOI or restate the generic TNW/gearing definition in full — these definitions are consistently delegated to the (not-yet-reviewed-in-this-batch) generic "Financial Ratios – Non-Financial Sector" and "Liquidity Analysis of Non-Financial Sector Entities" criteria documents, which several of these sector files (Thermal Power, Auto Components, Cotton Textile, Non-Ferrous Metals) explicitly cross-reference by name. Those generic documents — not the ten reviewed here — are where the audit's specific concerns about net-worth basis, gearing inclusions, and cash-flow-vs-P&L substitution should be checked directly.
6. **Purely qualitative/legal files:** Policy on Default Recognition, Policy on Provisional Ratings, Policy on Withdrawal of Ratings, and Project Stage Entities carry no scorecard/financial-ratio content of their own (Project Stage Entities is fully qualitative; the three Policy documents are procedural/legal). Their load-bearing content for a rating-tool audit is the precise day/percentage/time-period thresholds documented above (1-day/1-rupee default, 30-day overdue, 90/365-day curing periods, 5-year/3-year/50%-of-tenure withdrawal eligibility, 12/18-month and 180-day provisional-rating validity windows) — all directly codeable as mechanical gates, none involving financial-statement definitions.

# Part 7 — CareEdge Methodology Corpus Review (10 files)

## Rating Methodology - Power Generation Projects_Sept2020.md

- **Status: DISCONTINUED.** Document itself states "[This criteria paper has been discontinued from March 31, 2023.]" (last reviewed March 2021). Not to be cited for any current rating — routing to it is a scope violation (any live power-generation-project rating must use a current criteria paper instead, e.g. thermal/solar/wind specific docs in this same folder).
- **Scope:** Debt issues of Power Generation Projects (hydel, thermal, nuclear, non-conventional); covers project overview, PPA evaluation, fuel supply risk, capital structure, management, project implementation risk, credit assessment of power purchaser (discoms), operating risk, financial analysis of projected operations, force majeure, structural risk (DSRA/escrow/TRA).
- **Rating-factor structure:** 11 numbered areas — (1) Overview of project, (2) PPA evaluation, (3) Fuel supply risk, (4) Capital structure, (5) Management evaluation, (6) Project implementation risk, (7) Credit assessment of power purchaser, (8) Operating risk, (9) Financial analysis of projected operations, (10) Force majeure risk, (11) Structural risk.
- **Indicative-metrics tables:** None — entirely qualitative/narrative. No numeric thresholds anywhere in the document.
- **Notching/support/mapping rules:** None specified — no parent-support notching, no hybrid rules, no LT-ST mapping table. Generic reference only to "mitigation of credit risk due to any credit enhancement."
- **Definitions:** No TOI/PBILDT/TNW/gearing definitions given at all. Financial analysis factors named only qualitatively: "Financial Structure and Leverage," "Earning Capacity," "Cash Flow Adequacy," "Debt Service Coverage," "Collection efficiency," "Financial Flexibility" — none defined numerically or by formula.
- **Mechanical-check-worthy thresholds:** None — no bright-line cutoffs present. (Only actionable fact: this methodology is superseded/discontinued — a mechanical check should flag any report citing this file by name/date as non-current.)

## Rating Methodology - Wind Power Projects - December 2024.md

- **Scope:** Wind power SPVs (under-construction and operational), infrastructure-project-financed (non-recourse), useful life ~25 years. Excludes non-SPV/non-project-finance wind entities (would fall under generic corporate/manufacturing methodology instead).
- **Rating-factor structure:** Four broad parameters — Business risk (permitting, construction, funding, PPA terms, tariff competitiveness, counterparty credit risk, operating/climatic risk), Industry & regulatory risk, Financial risk (cash flow stability/adequacy, leverage & coverage, working capital/liquidity, refinancing & forex risk), Management and parentage. Plus ESG (E/S/G) as a named risk category.
- **Indicative-metrics tables:** None with numeric thresholds. Only numeric data points embedded in prose: land requirement 3–5 acre/MW; typical debt:equity ratio "70:30"; PPA land-securing timeline "six months"; resource-assessment confidence levels P-50/P-75/P-90 (P-90 = most conservative, used for projections); payment security mechanism "generally one-month letters of credit (LCs)."
- **Notching/support/mapping rules:** Parent/group notching described qualitatively — "CARE Ratings first assesses the standalone credit profile of an asset and the same is notched up based on its parentage," referring out to the separate "Rating Methodology – Factoring Linkages Parent Sub JV Group" criteria (no notch quantum given in this document). No hybrid-instrument or LT-ST mapping rules in this doc.
- **Definitions:** Leverage/coverage indicators named but not formularised in this doc: "debt/PBILDT," cumulative DSCR, minimum DSCR, Project Life Coverage Ratio (PLCR) — referred to conceptually, no formula or threshold given. No net-worth or gearing formula stated. Notably, financial risk discussion explicitly separates "past financials" review from "projected free cash flow" for DSCR — a P&L-vs-cashflow distinction implicit in methodology but no numeric convention spelled out here.
- **Mechanical-check-worthy thresholds:** Land requirement 3–5 acre/MW (rough sanity-check ratio); typical D:E 70:30 (a benchmark, not a hard rule); PPA land-acquisition window of six months — usable as a soft flag in a project-finance workpaper, not a scored threshold.

## Rating Methodology Cut and Polished Diamond Industry - December 2024.md

- **Scope:** Cut and polished diamond (CPD) manufacturers/processors in India (largely Surat/Navsari-based); applies the generic CARE manufacturing-sector methodology plus CPD-specific overlay factors. Does not cover upstream mining or downstream jewellery retail/manufacturing as separate segments (though value-chain context given).
- **Rating-factor structure:** Four pillars — Management evaluation, Business risk (raw-material access, scale/operating efficiency incl. TOI, revenue diversification — geographic/customer/product, technology adoption/certification, related-party transactions), Financial risk (working capital intensity, forex risk), Industry risk (fragmentation, LGD competition, inventory valuation). Plus ESG section.
- **Indicative-metrics tables:** None with numeric thresholds — no scorecard/table anywhere. Only narrative statistics on India's global CPD market share (60% value / 85% volume / 92% pieces — industry-context stats, not rating thresholds).
- **Notching/support/mapping rules:** None present.
- **Definitions:** TOI referenced as the metric for "scale of operations" but not formula-defined. PBILDT referenced ("superior profit before interest, lease rentals, depreciation and taxation margin than the industry") — spelled out as including lease rentals explicitly ("PBILDT" = profit before interest, LEASE rentals, depreciation, and taxation) — this is a CareEdge-specific naming convention (lease-inclusive) worth noting for cross-document consistency checks against the generic Financial Ratios methodology. No net-worth or gearing definition. Explicit call-out: related-party transactions are industry-wide/structural in CPD (most sale/purchase routed through related/group entities) — methodology flags that "lack of adequate information on key group and associate concerns is viewed negatively," implying P&L/receivables from related parties need decomposition/scrutiny, though no mechanical decomposition rule is given.
- **Mechanical-check-worthy thresholds:** None numeric. Qualitative flag only: net working capital as % of current assets, receivable ageing/movement — used as inputs but no cutoff stated.

## Rating-Methodology-Commercial-Vehicle-Industry-Feb-2025.md

- **Scope:** Commercial Vehicle (CV) OEMs/manufacturers (LCV, M&HCV, goods and passenger carriers) in India; overlay on top of the generic manufacturing-sector methodology. Explicitly defers Financial risk assessment entirely to "CARE Ratings criteria 'Financial Ratios – Non Financial Sector'" — this document adds no CV-specific financial ratio definitions.
- **Rating-factor structure:** Business/Operational risk (market position/share, presence across segments & product range, operating efficiency/PBILDT margin, servicing & distribution network, technology/R&D, regulatory risk — BS-VI/axle load/scrappage policy, geographical diversification/exports, level of ancillarisation, vehicle financing availability) + Financial risk (per generic non-financial-sector ratio methodology) + Foreign exchange risk + ESG.
- **Indicative-metrics tables:** None with numeric thresholds. Only industry-context statistics in prose: goods carriers ~85–90% of CV volume; M&HCV 35–40% of domestic CV sales; buses <15% of industry volume; exports historically 8–13% of total CV sales volume (FY16–FY22); vehicles >16.2 tonnes used for highway transport, ≤3.5 tonnes for intra-city.
- **Notching/support/mapping rules:** None.
- **Definitions:** PBILDT referenced as the profitability metric tied to operating efficiency, but not formula-defined in this document (defers to Financial Ratios – Non-Financial Sector criteria). No gearing/TNW/TOI definitions given directly — this document is entirely dependent on the cross-referenced generic ratio methodology for any numeric convention.
- **Mechanical-check-worthy thresholds:** Export-share range 8–13% of CV sales volumes (FY16–FY22) is a historical benchmark, not a scored cutoff. M&HCV share 35–40%, goods-carrier share 85–90% — industry descriptive stats usable for sanity-checking a company's disclosed segment mix against industry norms, not codified rating thresholds.

## Rating-Methodology-Financial-Ratios-Life-Insurance-Sector-March-2025.md

- **Scope:** CARE Ratings' issuer rating methodology and financial-ratio suite specifically for Life Insurance companies (regulated by IRDAI). Explicitly states the issuer rating is NOT specific to any individual policy/contract, does not address deductibles/surrender/cancellation penalties, does not consider fraud-based claim denial, and does not factor in India sovereign FX-control restrictions on foreign claim settlement. Does not cover general/health insurers directly (footnote gives General Insurance technical-reserves formula for comparison only).
- **Rating-factor structure:** "RAMELS" framework — **R**isk Underwritten, **A**sset Quality, **M**anagement, **E**arnings, **L**iquidity, **S**olvency Margin — plus External support (parent/group linkages, government linkage) and ESG (E/S/G).
- **Indicative-metrics tables — VERBATIM:**

  **Earnings ratios table:**
  | Ratio | Formula | Significance |
  |---|---|---|
  | Gross Direct Premium (GDP) growth | (Current year GDP − Previous year GDP)/Previous year GDP | Growth in business undertaken |
  | Net Premium Earned (NPE) growth | (Current year GDP − Previous year GDP)/Previous year NPE [sic — document literally uses "GDP" in numerator here, likely a typo for NPE] | Growth after ceding/accepting reinsurance |
  | New Business Premium (NBP) growth | (Current year NBP − Previous year NBP)/Previous year NBP | New business growth excl. renewal premium |
  | Annual Premium Equivalent (APE) growth | (Current year APE − Previous year APE)/Previous year APE | APE = annualised first-year premiums on regular-premium policies + 10% of single premiums underwritten during the period (individual + group) |
  | Risk retention | Net Premium Written (NPW) / Gross Premium Written (GPW) | Risk retained vs ceded to reinsurers |
  | Conservation Ratio | Renewal Premium collected / (PY first year premium + PY renewal premium) | Business generated via renewals |
  | Market Share | Premium of company / Total industry premium | Position vs peers |
  | Expense ratio / Expense of Management ratio | Management expenses (opex + commission) / GDP [Gross Direct Premium] | Operating cost efficiency |
  | Value for New Business (VNB) Margin | VNB / APE | Future profits of new business written |
  | Investment yield | Total investment income / Average total investments | Average return on invested assets |
  | Persistency Ratio | Clients paying premium (in X months) / Net Active Clients × 100 | Renewal retention across cohorts |
  | Net earnings ratio | PAT / Net Premium Written (NPW) | Overall profitability vs NPW |
  | Return on net worth | PAT / Average net worth | Post-tax return on net worth |
  | Return on assets | PAT / Average assets | Post-tax return on average total assets |

  **Liquidity ratios table:**
  | Ratio | Formula | Significance |
  |---|---|---|
  | Liquidity Coverage | Cash & cash equivalent / Technical Reserves | Liquid funds vs estimated claims payable |
  | Liquidity Coverage including sub-debt | (Liquid Investments + cash & cash equivalent) / (Technical Reserves + Sub-debt maturing in next 1 year incl. interest) | Liquid funds vs claims + debt obligations |

  Footnote: **Technical Reserves for Life Insurance = Policy Liabilities + Funds for discontinued policies + Provisions.** (General Insurance Technical Reserves = Reserves for Unexpired Risk + Outstanding Claims Reserves — given for contrast only.)

  **Solvency ratios table:**
  | Ratio | Formula | Significance |
  |---|---|---|
  | Solvency ratio | Available Solvency Margin / Required Solvency Margin | Compliance with min. **1.5x (150%)** regulatory requirement; cushion above minimum examined |
  | Operating leverage | NPW / Net-worth | Risk-underwriting appetite per unit of net worth |
  | Financial Leverage | Subordinate Debt / Net-worth | Debt leverage over net worth |

  **Hybrid capital (2015 IRDAI guidelines) table — VERBATIM key terms:**
  | Particular | Condition |
  |---|---|
  | Quantum to be raised | **Less than 25% of paid-up capital and 50% of net worth** |
  | Interest/Dividend rate | Fixed/floating; floating tied to market rupee interest benchmark |
  | Claim priority | Senior to shareholders, subordinate to policyholders/other creditors; sub-debt senior to preference shares |
  | Tenure | **Not less than 10 years** (life/general/reinsurance); **not less than 7 years** (health insurers) |
  | Security | Unsecured; no enhancement of seniority vs policyholders/creditors permitted |
  | Servicing | Interest on sub-debt charged to P&L; preference dividend from distributable profit; subject to solvency compliance; if payment would cause/increase net loss, prior IRDAI approval required |
  | Option | No put option; call option only after **≥5 years** from issuance, subject to IRDAI approval + solvency compliance; no early-redemption incentive |
  | Cumulative/Non-cumulative | Missed interest may be carried forward (with/without compounding) subject to IRDAI approval; preference dividend is non-cumulative |
  | Inclusion in solvency margin (haircut schedule by years-to-maturity) | **≥5 years: 100%; 4–<5 years: 80%; 3–<4 years: 60%; 2–<3 years: 40%; 1–<2 years: 20%; <1 year: 0%** |
  | Debenture redemption reserve | **25% of outstanding debentures** considered adequate; DRR excluded from solvency-margin liability computation |

- **Notching/support/mapping rules:** Hybrid capital of insurance companies is "generally notched down from its issuer rating" (no fixed notch count given) due to subordination to policyholders and sharper migration risk (any coupon/principal delay, even due to regulatory restriction, = default per CARE's definition). Parent/group support and government-linkage notching are referred out to separate "Consolidation & Combined Approach" and "Notching by Factoring Linkages in Ratings" criteria — not detailed here.
- **Definitions — SECTOR-SPECIFIC, differ from generic corporate conventions:**
  - **Net worth** used directly (not "tangible net worth") in Return on Net Worth, Operating Leverage, Financial Leverage — no explicit exclusion of revaluation reserves or intangibles stated in this document (unlike the generic corporate TNW convention flagged elsewhere in this project's corpus). **This is a definitional gap/risk**: a rating-tool computation using generic TNW (excl. revaluation reserves) vs this document's unqualified "net worth" could diverge.
  - **Technical Reserves** is a life-insurance-specific liability aggregate (Policy Liabilities + Funds for discontinued policies + Provisions) — NOT a generic balance-sheet caption; must be assembled from the insurer's actuarial/policy-liability notes, not picked up as a single line item.
  - **Financial Leverage** here = Subordinate Debt / Net-worth — a much narrower "gearing" definition than the standard corporate Total-Debt/TNW; using ordinary corporate gearing (total borrowings/TNW) for a life insurer would be a methodology mismatch (parallel to Failure Mode 28 in the ICRA SOP — using another sector's metric set).
  - **Solvency ratio** denominator (Required Solvency Margin) is an IRDAI-regulatory actuarial calculation, not derivable from the P&L/balance sheet alone.
- **Mechanical-check-worthy thresholds:**
  - **Solvency ratio must be ≥1.5x (150%)** — a hard regulatory bright line; any life insurer's solvency ratio computed below 1.5x is a mechanical breach flag.
  - **Hybrid capital solvency-inclusion haircut schedule** (100/80/60/40/20/0% by years-to-maturity band, cutoffs at exactly 5/4/3/2/1 year) — precisely codeable step function.
  - **Hybrid quantum cap: <25% of paid-up capital AND <50% of net worth** — two simultaneous bright-line ceilings, mechanically checkable against a company's disclosed hybrid issuance and paid-up capital/net worth.
  - **Tenure floors: ≥10 years (life) / ≥7 years (health) for hybrid instruments; call option only after ≥5 years.**
  - **DRR ≥25% of outstanding debentures** considered adequate — a bright-line coverage check.

## Rating-Methodology-Port-and-Port-Services-March-2025.md

- **Scope:** Debt raised by maritime ports across India — both major ports (Major Port Trusts Act 1963 framework) and non-major/minor ports (Indian Ports Act 1908, state-administered); applies to whole port enterprises, single/multi-terminal facilities, and multi-location/under-implementation port entities. Cross-references the generic Infrastructure Sector Ratings criteria and the Financial Ratios – Non-Financial Sector criteria for detailed ratio methodology (this document does not itself define ratio formulas).
- **Rating-factor structure:** (1) Operational/Business risk — split into (A) Operational ports (type/capacity, cargo evacuation/multimodal connectivity, cargo & revenue mix, customer diversification, productivity — average turnaround time/pre-berthing time/output per ship-berth-day, tariff regime, long-term agreements/MGT) and (B) Greenfield/expansion projects (statutory clearances, capital structure & funding risk, EPC contract); (2) Financial risk (cash-flow-based model; leverage & coverage — net debt/PBILDT, DSCR; forex risk; refinancing risk; liquidity/DSRA); (3) Regulatory risk (tariff-setting authority — TAMP historically, now port boards per 2021 policy); (4) Promoter and management risk; plus ESG.
- **Indicative-metrics tables:** None with numeric thresholds/scorecard bands. Only contextual stats: India coastline 7,517 km; ~95% of India's merchandise trade (by volume) via seaports; 12 named major ports listed in footnote (Mumbai, Kandla, Mangalore, JNPT, Mormugao, Cochin, Chennai, Tuticorin, Vishakhapatnam, Paradip, Kolkata, Kamarajar).
- **Notching/support/mapping rules:** None specific to ports in this document (refers to generic Infrastructure Sector Ratings criteria for any support/notching framework).
- **Definitions:** Financial risk metric explicitly named as **"net debt/PBILDT"** (not gross debt/PBILDT) — a port-sector-specific convention worth flagging since other CareEdge docs in this corpus use gross debt/PBILDT or Total debt/OPBDIT language; using gross debt here instead of net debt would be a definitional mismatch. DSCR is referenced without formula (deferred to generic ratio methodology). No TNW/gearing/TOI definitions given directly in this document — fully dependent on the cross-referenced Financial Ratios – Non-Financial Sector criteria. Note the explicit statement: "In case of a group consisting of multiple entities with strong operational and financial linkages, cash flows are assessed at the consolidated/group level" — i.e., basis (standalone vs consolidated/group cash flow) is condition-dependent, not automatically standalone.
- **Mechanical-check-worthy thresholds:** None numeric/bright-line in this document (all thresholds are qualitative — "favourable," "credit positive" — with productivity/coverage benchmarks assessed against unspecified peer/industry norms rather than fixed cutoffs).

## Rating-Methodology-Solar-Power-Projects-December-2024.md

- **Scope:** Solar power project SPVs (under-construction and operational), infrastructure/project-finance structure, non-recourse debt, ~25-year asset life. Same four-pillar structure as the Wind methodology (near-identical document, solar-specific substitutions).
- **Rating-factor structure:** Business risk (permitting — incl. solar-park vs standalone distinction, construction, funding, PPA terms, tariff competitiveness, counterparty credit risk, operating/climatic risk incl. P-50/P-75/P-90 generation estimates with annual degradation adjustment), Industry & regulatory risk, Financial risk (cash flow stability/adequacy, leverage & coverage — debt/PBILDT, cumulative & minimum DSCR, PLCR, working capital/liquidity, refinancing/forex risk), Management and parentage, ESG.
- **Indicative-metrics tables:** None with numeric thresholds. Numeric data points in prose: land requirement for ground-mounted solar 4–5 acre/MW (vs wind's 3–5 acre/MW); PPA land-securing window "generally six months"; resource-assessment confidence levels P-50/P-75/P-90 (P-90 most conservative, "then adjusted for annual degradation" — an explicit methodological nuance not present verbatim in the Wind doc).
- **Notching/support/mapping rules:** Same as Wind doc — parentage notch-up referenced qualitatively, refers to separate Parent-Sub-JV-Group linkage criteria; no notch quantum given.
- **Definitions:** Same gaps as Wind methodology — debt/PBILDT, cumulative/minimum DSCR, PLCR named but not formula-defined in this document. No TNW/gearing/TOI definitions. No explicit net-worth-basis or P&L-vs-cash-flow-figure distinction stated (relies on generic ratio methodology).
- **Mechanical-check-worthy thresholds:** Land ratio 4–5 acre/MW (solar) vs 3–5 acre/MW (wind) — usable as a sanity-check band, not a scored cutoff.

## Rating-Methodology–Power-Transmission-March-2025.md

- **Scope:** Inter-state (ISTS, under CERC/PGCIL/CTUIL point-of-connection [PoC] mechanism) and intra-state transmission projects/utilities (under SERC), including projects awarded via tariff-based competitive bidding (TBCB) or nomination (PGCIL) and cost-plus regulated tariff mechanism (RTM) projects.
- **Rating-factor structure:** Project risk (pre-commissioning: permitting/RoW, funding, construction), Industry & regulatory risk (CERC/SERC tariff determination timeliness, cost-plus vs TBCB), Management risk, Operational risk (demand/supply risk via Transmission Service Arrangement [TSA], O&M risk, natural-calamity/contingency risk, counterparty credit risk — PoC-mechanism projects vs standalone intra-state lines), Financial risk (financial structure/leverage, AFC recovery & cash-flow adequacy, DSCR, PLCR, DSRA/TRA-escrow, O&M/interest-rate risk, tail period), ESG.
- **Indicative-metrics tables — VERBATIM numeric thresholds (all embedded in prose, not in a table format, but precise and bright-line):**
  - **Normative annual transmission line availability: 98.00%.** Full Annual Fixed Charge (AFC) recoverable at/above this level.
  - **Incentive threshold: line availability ≥98.50%** → eligible for incentive.
  - **Incentive cap: no additional incentive payable for availability beyond 99.75%.**
  - Typical debt:equity funding **70:30** (capital-intensive, high leverage by design).
  - PoC-mechanism ISTS pool collection efficiency **"over 98%"**; low receivable days **"~60 days."**
  - Payment security for intra-state lines: revolving LC equivalent to **one month of billing** from Long Term Transmission Customer (LTTC).
  - Tariff regulation block period for cost-plus (CERC) projects: **five years** (SERC block periods vary by state).
  - Transmission asset life: **30–35 years**, exceeding typical loan tenor.
- **Notching/support/mapping rules:** No explicit notch quantum for government/parent linkage; document states that for economically/strategically significant ISTS/intra-state projects with central/state government support, linkage is "analysed" per the SPV-government relationship (no formula). PLCR formula given: **PLCR = NPV of cash flow available for debt servicing over remaining project life ÷ current debt levels** (a rare case where this document DOES spell out the formula, unlike the Wind/Solar docs which merely name PLCR).
- **Definitions — sector-specific nuance:** Explicitly states DSCR can be LOWER for transmission projects than for manufacturing/other project types and still support the same or better credit profile, because of revenue certainty via TSA (a sector-specific relaxation of a generic DSCR threshold — i.e., a "good" DSCR number is NOT comparable across sectors; a manufacturing-methodology DSCR cutoff should not be mechanically applied to transmission). No TNW/gearing/TOI/PBILDT formula given in this document (defers to generic infra/ratio criteria) but explicitly flags "quantum of capital creditors pending for settlement for a long time" and "large contingent liabilities and disputes" as leverage-adjacent items to be factored — i.e., trade-creditor overhang and contingent liabilities are explicitly named as credit-risk items alongside leverage, though not mechanically added into a gearing/debt figure in this text.
- **Mechanical-check-worthy thresholds:**
  - **98.00% line availability = full AFC recovery threshold** — hard bright line.
  - **98.50% = incentive-eligibility threshold; 99.75% = incentive cap** — two more precise bright lines forming a three-tier step function (below 98.00% / 98.00–98.49% / 98.50–99.75% / above 99.75%) — highly codeable for a transmission-SPV revenue model.
  - **PoC pool collection efficiency >98%, receivable days ~60 days** — usable as sector benchmarks.
  - **LC = 1 month billing** payment-security convention — codeable minimum for a standalone intra-state transmission credit assessment.
  - Debt:equity 70:30 — typical/benchmark ratio, not a hard cap.

## Rating-Methodology–Road–Assets-Annuity–March–2025.md

- **Scope:** BOT-annuity road projects specifically (both project/under-implementation phase and operational phase); explicitly EXCLUDES hybrid annuity model (HAM) roads — document states "Please refer to CareEdge Ratings' separate criteria published for road projects under hybrid annuity revenue model" — so HAM roads must be rated under a different (not-in-this-corpus) methodology, not this one. Also excludes toll-based/BOT-toll roads (different revenue-risk profile, not annuity).
- **Rating-factor structure — Project phase:** Sponsor evaluation (track record, financial position, ownership structure, commitment track record, corporate guarantee), Implementation/construction risk (resource availability, statutory clearances, time/cost overrun risk, financial closure), Contractual risk assessment (concession agreement terms/counterparty — NHAI/state authority), Projected financials & sensitivity (DSCR sensitivity to O&M cost and borrowing-rate variation). **Operational phase:** Management risk, O&M risk, Cash flow risk (waterfall/escrow/ring-fencing, DSRA, MMRA), Contractual arrangement/risk allocation.
- **Indicative-metrics tables:** None with scored numeric thresholds. Only a stated technical benchmark range: **road roughness index "ranges between 1,800 mm/km and 3,000 mm/km; lower the better"** — a construction-quality metric, not a financial threshold.
- **Notching/support/mapping rules:** None specific — refers to generic Infrastructure Sector methodology and, for sponsor corporate guarantees, to the separate "Credit Enhanced Debt" criteria (no notch quantum given here).
- **Definitions:** No TNW/gearing/PBILDT/TOI formulas in this document — annuity-road revenue is fixed/contracted (bi-annual annuity payouts from concessioning authority), so this methodology is DSCR/cash-flow-centric rather than P&L-ratio-centric; explicit statement that in the ABSENCE of demand risk, "credit profile of the annuity provider/counterparty…assumes paramount importance" — i.e., counterparty (NHAI/state authority) credit quality substitutes for demand-risk analysis. Notably states that force-majeure/liquidated-damages financial implications "cannot be ascertained upfront, and are therefore, not factored in credit ratings" — an explicit scope exclusion.
- **Mechanical-check-worthy thresholds:** Roughness index band 1,800–3,000 mm/km (lower=better) — a technical/engineering threshold usable in an O&M-quality check, not a financial-statement metric. No debt/coverage bright lines given (DSCR sensitivity is described qualitatively as "stressed" against O&M and interest-rate scenarios, no numeric cutoff for pass/fail).

## Rating-of-Investment-Holding-Companies-Debt-March-2025.md

- **Scope:** Debt raised by investment holding companies (majority assets = equity/debt investments and loans & advances to group/investee entities, typically non-controlling stakes, no independent operations, income = dividend/interest/capital gains) — WITH or WITHOUT pledge of shares (loans against shares/LAS). Explicitly covers Core Investment Companies (CICs, RBI-registered NBFCs) as a sub-case. Explicitly EXCLUDES: LAS criteria does not apply if pledged shares are of UNLISTED companies ("This criteria does not apply if the shares of unlisted companies are pledged").
- **Rating-factor structure:** (1) Non-pledge-backed debt: quality/credit-risk of investment portfolio, debt-to-market-value of investments, financial flexibility, refinancing ability, cash-flow adequacy, off-balance-sheet exposures (corporate guarantees) factored into leverage, cushion of UNENCUMBERED investments' market value vs aggregate debt (incl. off-balance-sheet), shareholding-pattern/promoter-support analysis, standalone (not consolidated) approach with explicit factoring of expected financial support extended TO group entities. (2) CICs: additionally, credit/asset quality of underlying investments, ALM statement across time buckets, **Outside Liabilities/Adjusted Net Worth (RBI-specified metric)** for leverage, diversification (number/sector/product/customer/geography), disclosure quality. (3) Pledge-backed (LAS) debt: Collateral risk analysis (security cover, tenure, promoter holding, beta, liquidation avenues, underlying credit rating), Liquidity risk (liquidation horizon), Valuation/market risk (beta vs SENSEX, PE vs industry PE), Credit rating of underlying pledged company, Legal risk analysis (enforceability of pledge).
- **Indicative-metrics tables:** No formal scored table, but several PRECISE structural/definitional rules stated in prose:
  - LAS shares must be **Group 1 (NSE) or Group A (BSE)** classification only.
  - Underlying pledged shares must have **traded on all trading days for the past 12 months** (exception: technical non-trading days).
  - PE-multiple comparison: underlying company's PE (based on **consolidated financial results for the four trailing quarters**) vs industry PE — lower variation viewed positively.
  - "T minus" payment mechanism: borrower must fund the full repayment obligation (incl. interest) into a lender/trustee-operated account a stipulated number of days before due date (mechanism named, exact "T minus X days" not numerically specified in this document).
- **Notching/support/mapping rules — the CENTRAL, most actionable rule in this document:** **"The rating of loans of investment holding companies by pledging shares of investee/operating companies held by them is generally capped at the rating of the investee/operating company whose shares are pledged, or the LOWEST rating among the investee/operating companies in case shares of multiple companies are pledged."** This is a hard rating-cap/notching rule directly analogous in mechanical-checkability to a bright-line threshold: **LAS rating ≤ min(standalone rating of each pledged-share issuer).**
- **Definitions — differ materially from generic corporate conventions (directly relevant to the audit's stated concern about gearing/net-worth misdefinition):**
  - **Leverage for a non-CIC investment holding company is NOT computed as a conventional Total-Debt/TNW ratio against book net worth.** Instead, the operative metric is **"debt-to-market value of investments"** (i.e., debt against MARKET value of the equity/debt investment portfolio, not book net worth), and specifically the **"cushion of the market value of the UNENCUMBERED investments vis-à-vis aggregate debt level (INCLUDING off-balance sheet exposures such as corporate guarantees)."** A rating tool that computes gearing for a holding company using book TNW instead of market-value-of-investments-based leverage, or that excludes off-balance-sheet corporate guarantees from the debt aggregate, would be using the wrong definition per this methodology.
  - **CIC leverage metric is explicitly the RBI-specified "Outside Liabilities to Adjusted Net Worth"** — NOT the generic corporate TD/TNW ratio. "Adjusted Net Worth" is an RBI regulatory construct (distinct from plain net worth or TNW) — using unadjusted net worth here is a definitional error.
  - **Consolidation basis is explicitly STANDALONE for investment holding companies** — "a consolidated approach may not be appropriate as the business risk profile of the investee/operating entities of the group may vary significantly. CARE Ratings thus evaluates the investment holding companies on a standalone basis." This is a clear, sector-specific basis rule (directly relevant to the audit's "wrong net-worth basis"/consolidation-basis concern) — a holding-company rating built on consolidated financials instead of standalone would violate this document's explicit methodology.
  - Debt aggregate for leverage purposes explicitly includes **off-balance-sheet exposures (corporate guarantees)** — i.e., gearing/leverage for a holding company must add back guarantees given on behalf of group entities, not just on-balance-sheet borrowings. This is directly analogous to (though distinct from) the ICRA-side "LC-backed creditors/acceptances" issue flagged in the audit brief — here it is guarantees, not acceptances, but the same principle (off-balance-sheet credit support must be added into the debt/leverage figure) applies.
- **Mechanical-check-worthy thresholds:**
  - **LAS rating cap = min(rating of each pledged underlying company)** — directly codeable notching rule.
  - Share eligibility: **Group 1 (NSE) / Group A (BSE) classification only**, and **traded on all trading days in the past 12 months** — both mechanically verifiable eligibility gates.
  - PE-comparison convention: **consolidated financials, four trailing quarters** — a precise basis specification (period + consolidation level) that a workpaper could mechanically verify was followed.
  - Leverage metric substitution rule (market-value-of-investments basis, off-balance-sheet guarantees included, standalone basis mandatory) — while not a single numeric cutoff, this is a precise, binary, mechanically-checkable DEFINITIONAL rule: "was leverage computed against market value of unencumbered investments (correct) or against book TNW (incorrect)?" and "was the off-balance-sheet guarantee included in the debt aggregate (correct) or omitted (incorrect)?"

# Part 8 — CareEdge Methodology Corpus Review

## Rating_Methodology_Recovery_Ratings_March_2025.md

- **Scope:** Covers Security Receipts (SRs) issued by Securitisation Companies (SCs) / Asset Reconstruction Companies (ARCs) under the SARFAESI Act, 2002, rated on a defined "Recovery Rating" (RR) scale used to determine Net Asset Value (NAV) per RBI guidelines. Explicitly distinguishes recovery risk (probability of recovery) from default risk (probability of default) — NOT a credit rating in the conventional sense. Excludes standard corporate/bank credit ratings.
- **Rating-factor structure:** Qualitative/quantitative parameters, not a scored-factor grid: (1) Reason for delinquency, (2) Resolution strategy (sale of assets / one-time settlement / sale of business-management restructuring), (3) Nature/composition/valuation/possession status of underlying assets, (4) Seniority of payments to SR holders, (5) Extent of debt acquired and lender composition, (6) Time elapsed from loan assignment, (7) Legal hurdles.
- **Indicative-metrics table (verbatim):**

| Recovery Rating (RR) | Definitions |
|---|---|
| RR 1+ | Present value of expected recoveries is more than 150% of the face value of outstanding SRs. |
| RR 1 | Range of the present value of expected recoveries is more than 100% and up to 150% of the face value of outstanding SRs. |
| RR 2 | Range of present value of expected recoveries is more than 75% and up to 100% of the face value of outstanding SRs. |
| RR 3 | Range of present value of expected recoveries is more than 50% and up to 75% of the face value of outstanding SRs. |
| RR 4 | Range of present value of expected recoveries is more than 25% and up to 50% of the face value of outstanding SRs. |
| RR 5 | Range of present value of expected recoveries is up to 25% of the face value of outstanding SRs. |

- **Notching/support/mapping rules:** No parent-support/hybrid/LT-ST rules (not applicable to this instrument type). Key rule: recovery ratings reviewed bi-annually; resolution period is five years, extendable by three years with SC/ARC Board approval; ratings withdrawn on full redemption or expiry of resolution period upon request. For pooled-asset SRs, an assessment must cover individual assets or at minimum the top assets forming **75–80% of the expected recovery by value**.
- **Definitional differences:** Not applicable — no TOI/PBILDT/TNW/gearing definitions here; NAV/NPV of expected cash flows stated as % of face value is the core metric. NPV discount rate = an "indicative yield" based on prevailing interest rate scenario + risk premium (no fixed formula given).
- **Bright-line thresholds worth a mechanical check:** (1) The six RR bands' exact percentage cutoffs (150%, 100–150%, 75–100%, 50–75%, 25–50%, ≤25%) — directly codeable. (2) The ">60% of total debt aggregated by SC/ARC" threshold for reduced procedural/approval delay (stated as "if the concerned SC/ARC holds over 60% of the total debt of the distressed asset"). (3) The 75–80% expected-recovery-by-value coverage threshold for pooled-asset assessments. (4) Five-year resolution period / three-year extension cap.

## Rating_Methodology_Sugar_Sector_March_2025.md

- **Scope:** Covers Indian sugar manufacturing companies (sugarcane-based); a sector-specific overlay on CareEdge's general manufacturing-sector methodology (not standalone). Explicitly says it applies "over and above" the broad manufacturing methodology.
- **Rating-factor structure:** A. Industry Overview (climatic risk, demand-supply cycle, regulatory risk) → B. Business and Operating Risk (market position/size, forward integration, cane availability/operating efficiency, geographical diversification, revenue/profitability, working capital management) → C. Financial Risk and Key Ratios → D. ESG.
- **Indicative-metrics table:** No numeric threshold table provided. Only narrative ranges given in prose: by-product revenue "ranges from 15% to 25% of total revenues for large sugar mills"; inventory holding "four to six months as on March-end"; industry cyclicality is "a three to five-year cycle."
- **Notching/support/mapping rules:** None present (no parent-support, hybrid, or LT-ST mapping content — this is a sector overlay, not a general corporate methodology).
- **Definitional differences:** States CareEdge "follows its standard ratio analysis methodology for manufacturing companies per CareEdge Ratings' criteria on Financial Ratios—Non-Financial Sector" (i.e., generic corporate ratio definitions apply, no sugar-specific redefinition of TOI/PBILDT/TNW/gearing). Sector-specific overlay ratios named: Total debt/Gross Cash Accruals (GCA), and Total Outside Liabilities/Tangible Net Worth (TOL/TNW) — flagged as "key indicator" for this sector, but no numeric bands given.
- **Bright-line thresholds worth a mechanical check:** None precise enough — all ranges are narrative ("15% to 25%", "four to six months", "three to five-year cycle") rather than rating-determinative cutoffs. Not separately actionable beyond noting them as descriptive context.

## Rating_of_Short_Term_Instruments_Feb_2025.md

- **Scope:** Governs rating of short-term instruments/facilities with original maturity up to one year (CP, short-term bank facilities), across financial and non-financial sector entities. Cross-cutting methodology applicable regardless of sector.
- **Rating-factor structure:** Not a scored factor grid; two pillars — (1) Liquidity (cash flows, working capital, unencumbered liquid investments, unutilised committed credit lines, ALM profile for financial entities), (2) Financial flexibility (parent/group credit line, group support, back-up credit lines/CP backed by WC limits, project-implementation flexibility).
- **Indicative-metrics table:** The LT-ST mapping grid is present but rendered as an EMPTY matrix (all cells blank/unreadable in the source markdown — described only via "teal" vs "grey" shading legend, which did not survive OCR/markdown conversion). Verbatim structure:

| Long-term ratings | A1+ | A1 | A2+ | A2 | A3+ | A3 | A4+ | A4 | D |
|---|---|---|---|---|---|---|---|---|---|
| AAA / AA+ / AA / AA- / A+ / A / A- / BBB+ / BBB / BBB- / BB+ / BB / BB- / B+ / B / B- / C / D | *(all cells blank in source — mapping colours not extractable)* | | | | | | | | |

  **This table is UNREADABLE — the actual LT↔ST mapping (which cell is shaded per long-term grade) is lost in this document.** ICRA's own master prompt states its own house LT-ST mapping rule as the operative fallback (AAA/AA→A1+; A+→A1+/A1; A→A2+/A1; A-→A2+; BBB+→A2; BBB→A3+; BBB-→A3; BB+→A4+; below→A4) — that is an ICRA convention, NOT extractable from this CareEdge document, and should not be silently substituted for CareEdge ratings without a genuine CareEdge source.
- **Notching/support/mapping rules:** Mapping is described as "indicative," not strictly one-to-one — CareEdge "may differ from its general mapping framework" where liquidity is judged superior or inferior to the norm. No numeric override thresholds given (purely qualitative discretion).
- **Definitional differences:** None specific to short-term ratings beyond referencing the generic Liquidity Analysis and Financial Ratios criteria documents. No TOI/PBILDT/TNW/gearing redefinition here.
- **Bright-line thresholds worth a mechanical check:** None extractable — the one numeric table in this document is unreadable in the source. **Flag: per the master CLAUDE.md rule ("If a threshold table is unreadable... say so — never invent thresholds"), any code in the rating tool that hard-codes an LT-ST mapping table sourced to "CareEdge" methodology should be checked against this — the actual CareEdge table could not be recovered from this markdown and may have been fabricated/borrowed from ICRA's convention.**

## Rating–Methodology-Airport–Companies–March-2025.md

- **Scope:** Covers airport companies operating/managing/developing greenfield and brownfield airports under PPP (concession/SPV structures), assessed over the life of the rated debt instrument. Cross-references CareEdge's Infrastructure Sector Ratings (ISR) methodology for detailed management-risk and project-implementation-risk evaluation, and Financial Ratios—Non-Financial Sector for ratio definitions.
- **Rating-factor structure:** 1. Business risk assessment (contractual structures; revenue risk — aeronautical vs non-aeronautical vs real estate; regulatory environment/tariff-order risk; rate-revision flexibility; revenue-sharing with Authority; operating risk) → 2. Market position and passenger base (passenger mix, location, region's economic base, service area, traffic pattern/volatility, competition) → 3. Promoters/sponsors and management track record (experience, financial strength/commitment) → 4. Financial risk analysis → 5. Project risk analysis (for greenfield/expansion) → 6. ESG.
- **Indicative-metrics table:** No numeric threshold table provided. Named financial ratios (no bands): Debt/PBILDT (Profit Before Interest, Lease rentals, Depreciation and Taxation — note the added "L" for lease rentals, sector-specific variant of EBITDA), interest coverage, debt service coverage, and **Project Life Coverage Ratio (PLCR)** = NPV of cash flow available for debt servicing over the remaining life of the project ÷ current debt levels.
- **Notching/support/mapping rules:** No explicit notching formula; qualitative treatment of sponsor support ("articulation of promoters' intent to extend need-based support beyond committed risk capital" viewed favourably), refinancing risk (bank debt tenor 3–10 years) treated case-by-case rather than mechanically.
- **Definitional differences:** **PBILDT here explicitly = Profit Before Interest, Lease rentals, Depreciation and Taxation** — differs from a plain PBIDT/EBITDA by including lease rentals as an add-back component, a sector-specific definitional variant relevant to airport concession accounting (lease payments to AAI/Authority). PLCR is a cash-flow-statement-derived metric (NPV of CFADS) — explicitly cash-flow based, not a P&L ratio, and is stated as intentional/appropriate for a project-finance credit ("CareEdge Ratings analyses airport companies based on cash flow approach") — i.e., this is a case where cash-flow-basis IS the correct/prescribed convention, not a substitution error, but it flags that PBILDT vs standard PBILDT/OPBDIT terminology must be tracked precisely per sector.
- **Bright-line thresholds worth a mechanical check:** Revenue-sharing regulatory note: shared-till framework applies **30% of non-aeronautical revenues** into the aeronautical tariff-setting base (National Civil Aviation Policy, June 15, 2016) — a genuine bright-line percentage worth encoding if modeling airport tariff resets. Tariff control period = **5 years** (fixed cadence for AERA reviews). No other numeric cutoffs (all other factors are qualitative/comparative).

## Toll-Road-Projects-March 2025.md

- **Scope:** Covers debt of toll road projects in India (operational and under-construction; TOT — Toll-Operate-Transfer — projects assessed similarly to operational toll projects). Project-finance/SPV-level rating methodology.
- **Rating-factor structure:** 1. Revenue risk (demand analysis, competition, toll pricing; track record of toll collection; traffic mix; toll-rate revision mechanism) → 2. O&M risk → 3. Financial Analysis (leverage via Debt/CFAD, DSCR, interest coverage, Concession Life Coverage Ratio [CLCR], debt amortisation, DSRA adequacy, cash sweep, restricted payment covenants, FX exposure) → 4. Project Implementation Risk → 5. Sponsor Evaluation → 6. Regulatory Risk (toll exemptions) → 7. Evaluation of Concession Agreement (CA).
- **Indicative-metrics table:** No numeric threshold table. Named ratios only, no bands: Debt/CFAD (Cash Flow Available for Debt servicing), DSCR, interest coverage ratio, **Concession Life Coverage Ratio (CLCR)** = NPV of cash flow available for debt servicing over remaining concession life ÷ current debt levels (structurally identical formula to the airport methodology's PLCR, renamed for concession tenor rather than project/asset life), Debt/toll-collection vs balance loan tenor.
- **Notching/support/mapping rules:** No mechanical notching; DSRA form (cash vs bank guarantee) treated qualitatively — a BG-form DSRA's rollover risk depends on sponsor credit strength (stronger sponsor mitigates BG-renewal/rollover risk). Force majeure and termination events are explicitly EXCLUDED from the rating assessment methodology (an explicit scope carve-out, not a numeric rule).
- **Definitional differences:** CFAD (Cash Flow Available for Debt servicing) is a cash-flow-statement-basis metric used for leverage (Debt/CFAD) — again, explicitly the prescribed/correct convention for project-finance/SPV toll-road analysis, not a substitution error, but confirms cash-flow-basis ratios are sector-appropriate here specifically (in contrast to a standard corporate entity where P&L-basis PBILDT/gearing on TNW is the norm). CLCR formula = NPV(CFADS over remaining concession life) / current debt — a project-life-coverage metric distinct from ordinary DSCR.
- **Bright-line thresholds worth a mechanical check:** No numeric bright-line thresholds present in this document — all factors (traffic mix balance, tail-period length, DSRA adequacy, EOT approval status) are qualitative/comparative with no stated cutoff values.

## criteria-broking-criteria-december-2025.md

- **Scope:** Covers rating of debt instruments and bank facilities of stockbroking companies (standalone brokers, bank-led brokers, discount brokers) in India — financial-sector entity type. Explicitly cross-references CareEdge's "notching by factoring linkages in ratings" criteria for parent/promoter-group support.
- **Rating-factor structure:** 1. Industry risk (stock market scenario, regulatory risk, competition risk) → 2. Business risk (market position; revenue diversification incl. MTF book; client-base diversification; risk management systems; operation/IT systems incl. mandatory VAPT; credit risk) → 3. Financial risk (capitalisation & resource profile; earnings profile; liquidity risk) → 4. Management risk → ESG.
- **Indicative-metrics table (asset/liability nature table, verbatim):**

| Liabilities | Description | Assets | Description |
|---|---|---|---|
| Total borrowings | Fund-based borrowings used for providing funding to clients and working capital requirements of the company. | Cash and bank balances | In addition to the company's cash and bank balances, some portions consist of the client's fund, which is generally in the form of FDs lien marked to exchanges and/or clearing corporations. |
| Trade payables | Margins/payables to be paid back to the clients or exchanges. | Trade receivables, loan book and other assets | Margin funding done by the broker and trade balances receivable from clients or stock exchanges. |

  No numeric ratio-band table is given (no explicit gearing-multiple or coverage cutoffs stated).
- **Notching/support/mapping rules:** Parent/promoter-group linkage notching applied per CareEdge's separate "notching by factoring linkages in ratings" criteria (cross-referenced, not detailed here).
- **DEFINITIONS DIFFERING FROM GENERIC — this is the most directly load-bearing file for the audit's stated concern:**
  - **Gearing ratio is explicitly defined to INCLUDE non-fund-based debt**: "Calculation of leverage considers fund-based **and non-fund-based** borrowings of the firm" and "A gearing ratio is calculated by considering fund-based **and non-fund-based borrowings** against tangible net worth available." Non-fund-based borrowings specifically = **bank guarantees (BGs)** used to fulfil exchange margin requirements. Gearing is then ADJUSTED by netting the bank balance marked as lien against borrowings (since that cash is pledged collateral, not free cash), and by factoring in surplus/unutilised margins available with exchanges.
  - This is a DIRECT and explicit counter-example to a "gearing = fund-based debt only" convention — for broking firms, CareEdge's own criteria REQUIRE including non-fund-based facilities (BGs, and by extension LC-type instruments used similarly) in the gearing numerator. A rating tool that excludes non-fund-based/LC-backed exposures from gearing for a broking entity would be directly contradicting this document.
  - **Tangible Net Worth (TNW)** is explicitly stated to be "per the CareEdge Ratings' criteria on financial ratios for **financial sector**" — i.e., NOT the corporate/non-financial-sector TNW definition; the two are explicitly different bases per the master CLAUDE.md's own failure-mode-32 note ("The two TNW definitions DIFFER").
  - **Liquidity/cash treatment:** the balance sheet's cash and bank balances are explicitly flagged as NOT free cash — "these balances are majorly lien marked against borrowing facilities and to exchanges for margin requirements." Liquidity coverage ratio is explicitly defined using **unencumbered** cash/bank balance and liquid investments only, against 1-year debt maturities — directly matches CLAUDE.md failure mode 34's requirement that broking liquidity must use unencumbered, not gross, cash.
  - **Earnings ratios named:** cost-to-income (CTI) ratio, PBIT margin, PAT margin — no numeric bands given, but these are the specific ratio names expected in a CareEdge broking report (matches CLAUDE.md failure mode 33's note that CareEdge's broking template reports cost-to-income and ROTA as standard rows).
- **Bright-line thresholds worth a mechanical check:** No explicit numeric cutoffs stated in this document (no specific gearing multiple ceiling, no specific LCR minimum). However, the STRUCTURAL rule (gearing numerator = fund-based + non-fund-based debt, net of lien-marked cash; TNW = financial-sector basis; liquidity = unencumbered cash only) is itself a mechanically checkable definitional rule, and is exactly the kind of rule the audit is looking for — a rating tool must be coded to (a) add BG/non-fund-based exposure into the gearing numerator for broking entities, (b) use the financial-sector TNW definition, and (c) exclude lien-marked/client-fund cash from any liquidity numerator.

## hybrid-Instruments-issued-by-Banks-March-2025.md

- **Scope:** Covers Basel III regulatory capital instruments issued by banks — Additional Tier I (AT1) and Tier II bonds — plus comparison to legacy Basel II instruments (IPDI, Upper/Lower Tier II). Explicitly a bank-only methodology; not applicable to non-bank corporate hybrids (consistent with the master CLAUDE.md routing rule that bank hybrids must never be rated under a corporate hybrid-instruments methodology).
- **Rating-factor structure:** Not a scored grid — a features/triggers-based notching methodology: loss-absorption capacity, severity of loss, probability of default, each instrument type (AT1 vs Tier II) assessed against its specific regulatory trigger mechanics, cross-checked against PSU-vs-private ownership (government support likelihood) and the issuing bank's own senior/conventional debt rating.
- **Indicative-metrics tables (verbatim):**

  **Capital Conservation Buffer framework (coupon restriction by CET1 level):**

  | Common Equity Tier I Ratio (inclusive of current period's retained earnings) | Minimum Capital Conservation Ratios (as a percentage of earnings) |
  |---|---|
  | Between 5.5% and 6.125% | 100% |
  | Between 6.125% and 6.75% | 80% |
  | Between 6.75% and 7.375% | 60% |
  | Between 7.375 and 8% | 40% |
  | over 8.00% | 0% |

  Plus narrative bright-line triggers: AT1 write-down/write-off trigger = CET1 ratio breaching **6.125%** (effective from October 1, 2021) or Point of Non-Viability (PONV) as determined by RBI; minimum CET1 regulatory requirement referenced = **8.00%** (inclusive of capital conservation buffer) below which coupon-payment restrictions kick in; AT1 call option exercisable only after a minimum of **five years**, subject to RBI approval; under Basel II, IPDI coupon lock-in triggered at overall CAR below **9%**.

  Also includes two structured comparison tables: (1) Tier I instruments Basel II (IPDI) vs Basel III (AT1) — lock-in clause, loss-absorption features, coupon discretion, severity of loss; (2) Tier II bonds Basel II (Upper/Lower Tier II) vs Basel III Tier II — lock-in clause, severity of loss; (3) Appendix — Tier I vs Tier II bonds under Basel III compared on coupon discretion, lock-in, severity of loss.
- **Notching/support/mapping rules:** AT1 instruments notched down "one to several notches" below the bank's Tier II bond rating, magnitude depending on (a) adequacy of eligible reserves after the capital conservation buffer, (b) cushion over minimum regulatory capital, (c) other bank-specific credit risk factors. Notching also correlates inversely with the bank's own senior/conventional-debt rating: stronger/higher-rated banks get LOWER notching (less punitive), weaker/lower-rated banks get HIGHER (more) notching down. AT1 may also be rated lower than legacy Basel II IPDI. Tier II bonds under Basel III are rated similar to/close to Lower Tier II bonds under Basel II (since PONV-related risk parameters largely mirror Basel II Tier II assessment), again with more notching-down for lower-rated banks. **Public Sector Bank (PSB) government-support uplift**: rating factors in GoI capital-support likelihood — GoI has historically supported PSBs' coupon payments and bond call-backs, and is expected to infuse capital ahead of PONV/CCB triggers being breached. **Private sector banks (PVBs)**: notching driven by the bank's own intrinsic/conventional-debt rating strength, with no government-support overlay.
- **Definitional differences:** Coupon-eligible reserves for AT1 explicitly EXCLUDE revaluation reserve, share premium, foreign currency translation reserve, investment reserve, and reserves created on amalgamation — coupon can only be paid from current-year profits or (if insufficient) from reserves representing appropriation of net profits including statutory reserves, but excluding those named items. This is a bank-regulatory-capital-specific definition of "distributable reserves," distinct from a generic net-worth/reserves definition, and directly relevant to a "net-worth basis" audit theme (this document explicitly EXCLUDES revaluation reserves from the coupon-paying reserve base, paralleling the general TNW convention of excluding revaluation reserves — but here scoped narrowly to AT1 coupon-payment capacity, not net worth itself).
- **Bright-line thresholds worth a mechanical check:** (1) CET1 = 6.125% AT1 write-down/PONV trigger (effective Oct 1, 2021). (2) CET1 = 8.00% minimum threshold below which capital conservation buffer restricts AT1 coupon payments. (3) The five-tier CCB percentage-of-earnings restriction table (5.5–6.125% → 100% restriction; 6.125–6.75% → 80%; 6.75–7.375% → 60%; 7.375–8% → 40%; >8% → 0%). (4) AT1 call option minimum tenor = 5 years. (5) Basel II CAR trigger = 9%. All five are precise, numeric, and directly codeable into any bank-hybrid-instrument scorecard logic.

---

**Summary note relevant to the stated audit purpose:** The most directly load-bearing finding across this batch is in **criteria-broking-criteria-december-2025.md**, which explicitly REQUIRES including non-fund-based borrowings (bank guarantees) in the gearing numerator for broking entities and mandates a financial-sector-specific TNW basis and an unencumbered-cash-only liquidity definition — precisely the class of definitional error (wrong net-worth basis, wrong gearing inclusions) the audit is investigating, but documented here as the CORRECT CareEdge convention rather than an error. The airport and toll-road methodology files show that CASH-FLOW-BASIS ratios (PLCR, CLCR, Debt/CFAD) are the CORRECT/prescribed convention for project-finance/SPV entities — so "cash-flow figures substituted for P&L figures" is only an error for standard corporates, not for these infrastructure-SPV sectors; any rating tool must switch conventions by entity type. The short-term-instruments file's LT-ST mapping table is UNREADABLE in this markdown source and should not be treated as a verified CareEdge convention until re-sourced from a readable original.

