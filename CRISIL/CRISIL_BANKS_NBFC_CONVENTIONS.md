# CRISIL — financial sector (Banks, NBFCs/HFCs, Securities firms): ratio, capital-instrument and notching conventions

**Source, read 13-Sep-2026:** `criteria-for-banks-and-financial-institutions.md` (Sections I-III: core CRAMEL parameters, Basel III non-equity instruments, Basel II hybrids) and `criteria-for-finance-and-securities-companies.md` (Sections I-III: finance companies, NBFC/HFC hybrids, securities/broking companies), all read in full this session. This is the twin of `ICRA_BANKS_NBFC_CONVENTIONS.md`.

`CareEdge/BROKING_CONVENTIONS.md` already exists for CareEdge's broking definitions — this file is the CRISIL and ICRA-adjacent equivalent, and the three should be read side by side, never substituted for one another (see failure mode 32/33 in `CLAUDE.md`).

---

## 1. Banks and Financial Institutions — the CRAMEL framework

**C**apitalisation, **R**esource profile, **A**sset quality, **M**anagement, **E**arnings, **L**iquidity. Asset quality, capitalisation, earnings and resource profile are the **core** parameters the standalone rating anchors to; market position, management and liquidity are **supplementary** — CRISIL states explicitly that supplementary parameters "have limited ability to uplift the rating based on the core parameters but can constrain the rating in certain situations." Do not weight a strong market-position score as equally capable of lifting the anchor as a core parameter.

### Definitions

```
GNPA%                 = GNPAs / Gross advances        (GNPA = on-book loans overdue ≥90 days)
Restructured advances% = Restructured advances / Gross advances
CET1                  = CET1 capital / Risk-weighted assets
Overall CAR (CRAR)    = (Tier 1 capital + Tier 2 capital) / Risk-weighted assets
Net worth to NNPA     = Net worth / Net NPA           (capital cover over UNPROVIDED weak assets)
RoA                   = PAT / Average total assets
CASA ratio            = CASA deposits / Total deposits
Retail deposits ratio = Retail deposits (savings + retail term) / Total deposits
Market share (assets) = Total reported assets / Total banking-sector assets
Market share (deposits)= Total deposits / Total banking-sector deposits
LCR                   = High-Quality Liquid Assets / (30-day outflows − inflows)
```

**Restructured advances is CRISIL's own defined term** and is broader than a plain "loan modification" reading — it explicitly includes: altered payment period/amount/instalments/interest rate; rollover of credit facilities; additional credit facility sanctioned to a defaulting account to aid curing; enhancement of existing limits to an account already in default; and compromise settlements with a payment window **exceeding three months**. A search for "restructured" alone will miss compromise settlements captured under this definition.

**SFB minimum CAR is 15% of RWA**, materially higher than the universal-bank requirement of **11.5% (incl. 2.5% CCB)** — this is CRISIL's stated compensation for SFBs' inherently riskier target-segment mix, not evidence of superior capitalisation when comparing an SFB to a universal bank at face value.

### Basel III instrument notching — CRISIL's rule is a stated numeric range, unlike ICRA's qualitative-factor approach

| Instrument | Trigger | CRISIL's rating |
|---|---|---|
| Basel III Tier II | PONV only (remote in CRISIL's own assessed probability — "adequately factored in the bank's CCR" already) | **Same, or one notch below, the bank's Composite Credit Rating (CCR)** |
| Basel III AT1 (Tier I) | Coupon: CET1 (incl. CCB) < 8.0%, capital-conservation schedule (100% conservation at 5.50-6.125% CET1, tapering to 0% above 8.0%). Principal: write-down/conversion at CET1 < 6.125% or PONV | **Typically 1-3 notches below CCR**, driven by (a) eligible-reserve adequacy after stress, (b) CET1 cushion and track record of maintaining it above the regulatory minimum. **The floor is NOT fixed at 3** — CRISIL states explicitly the gap "can increase as the bank's CCR goes down," so a weak bank's AT1 can be notched down by more than 3. |
| Basel II Upper Tier II | CRAR breach only | 0-3 notches below CCR, per the pre-Basel-III framework (superseded for banks that have migrated, but the "0-3 notch" language is the anchor CRISIL later extends to NBFC/HFC hybrids — see §2) |

**This differs materially from ICRA's approach** (`ICRA_CONVENTIONS.md`/`ICRA_BANKS_NBFC_CONVENTIONS.md` §1): ICRA gives a qualitative multi-factor notching rationale with no stated numeric range; CRISIL gives an explicit 1-3 (or more) notch range for AT1. **Do not import CRISIL's numeric range onto an ICRA case, or vice versa — quote each agency's own stated rule.**

## 2. Finance companies (NBFCs and HFCs)

Core parameters: **asset quality, capitalisation, earnings.** Supplementary: market position, resource-raising ability, management, liquidity/ALM.

```
GNPA%           = GNPAs / Gross advances   OR   Gross Stage III loans / Gross Loans (Ind AS entities)
AUM             = On-balance-sheet advances + off-book securitisation portfolio
                  + co-lending book + business-correspondent book
Adjusted gearing = Adjusted borrowings / Net worth
ROMA            = PAT / Total average managed assets
```

**Adjusted borrowings** includes all on-balance-sheet debt (bank loans, debentures, deposits) **and assets securitised via the trust route**; direct-assignment securitisation reliance is separately factored as a qualitative risk rather than grossed into the ratio. **Adjusted net worth** is evaluated after deducting the First Loss Default Guarantee (FLDG) exposure on co-lending arrangements — confirmed structurally identical to ICRA's own adjusted-gearing treatment of FLDG (`ICRA_BANKS_NBFC_CONVENTIONS.md` §2), a genuine point of cross-agency convergence.

**AUM formula is confirmed identical in substance to ICRA's** (on-balance-sheet + off-book securitisation + co-lending + business-correspondent) — one of the few places all three agencies converge rather than diverge. Debt-instrument investments that function as credit substitutes (rather than conventional loans) may be folded into AUM case-by-case — check for this before concluding an NBFC's on-book-only figure is its full AUM.

**GNPA is analysed on a lagged/static-pool basis** for growth-distorted portfolios, same caution as ICRA's methodology.

### Hybrid instruments — NBFC/HFC notching now explicitly aligned to the bank framework

CRISIL states plainly that the NBFC/HFC hybrid notch-down framework has been **deliberately realigned to mirror the bank Upper-Tier-II framework** (0-3 notches), because of converging regulation: NBFC/HFC minimum Tier I is now 10% (deposit-taking/systemically-important), **CAR minimum is 15%**, and RBI has demonstrated willingness to approve hybrid servicing for loss-making NBFCs whose CAR still clears 15% — the same regulatory-forbearance pattern seen in banks.

| Instrument | CRISIL's rating |
|---|---|
| Lower Tier II / subordinate debt | **No** loss-absorption restriction tied to CAR/profitability → **equated to the Corporate Credit Rating (CCR)** |
| Other hybrids (perpetual debt, upper Tier II bonds, NCRPS, cumulative NCRPS) | Equated with CCR, or **notched down by up to 3 notches** in exceptional cases, depending on CAR cushion above 15% and financial flexibility (parental support, valuations, RoE, capital-market access track record) |

**The hybrid instrument's rating is CAPPED at the Lower-Tier-II/subordinate-debt rating** — a default on subordinate debt necessarily implicates the hybrid, so the hybrid can never be rated above it.

**NBFC Tier I inclusion cap for perpetual debt instruments: 15% of Tier I capital** (excess treated as Tier II within eligible limits) — a DIFFERENT cap from ICRA's 30%-of-adjusted-equity ceiling on corporate hybrid equity credit (`ICRA_CONVENTIONS.md` §9). These are not the same rule measuring the same thing: CRISIL's is a **regulatory Tier I inclusion limit specific to NBFC capital instruments**; ICRA's is that agency's own **analytical** equity-credit cap for corporate (non-financial) hybrids. Do not conflate the two percentages.

## 3. Securities companies (brokers, primary dealers)

Framework: Business Risk (market position, RMS, resources) → Financial Risk (capitalisation, earnings, liquidity) → Management. CRISIL states explicitly that **balance-sheet ratios alone do not capture a securities firm's risk profile** — market and business risk dominate and are volatile year-to-year, so RMS quality (margin/haircut/debtor policies, trader limits, algo-trading audit status, BCP/DR plans) is a first-order input, not a soft factor layered on top of the numbers.

### Definitions — three distinct capitalisation metrics, not one

```
Gearing            = Adjusted total debt / Net worth
                     (adjusted debt includes on-balance-sheet debt + off-book securitised assets,
                      trust route AND direct assignment)
Networth coverage  = Net worth (adjusted: excl. fixed assets, doubtful debts, illiquid assets,
                      investments in group companies) / Receivable risk (credit-risk exposure)
PD networth coverage = Net worth (adjusted for credit-risk charge)
                        / Loss in portfolio value from a 100bp parallel yield-curve shift
```

**CRISIL states gearing has real limitations for securities firms** and is supplemented — not replaced — by networth coverage, which strips out illiquid/risky assets and group-company investments to show what's actually available to absorb a sudden credit-risk loss. **A broking case citing only gearing, without networth coverage, is incomplete by CRISIL's own stated methodology.**

```
Cost-to-income ratio = Total operating cost / Total income (net of market-related income and adjustments)
Average RoE          = Net income / Shareholders' equity, averaged over a market cycle (single-year RoE
                        is explicitly flagged as too volatile to be meaningful alone)
RoA                   = PAT / Total average assets   (used where the firm is also active in lending —
                        Margin Trade Financing, loan against securities)
```

**PD minimum capital adequacy is 15% of RWA** (credit risk + market risk, VaR-based), with the 100bp-shift networth-coverage test as an CRISIL-specific supplementary check.

**Liquidity for securities firms is explicitly confidence-sensitive** — CRISIL frames disruption risk as reputational/perception-driven, not purely balance-sheet-driven, and names unencumbered pledgeable assets and committed bank lines (with proven operational ability to actually draw them under stress) as the real liquidity backstop, more than any static ratio.

## 4. Consolidation — CRISIL's own three-tier classification, and a distinctive Capital Allocation mechanism

Source: `criteria-for-consolidation.md`, read this session (Section I in full; Section II on homogenous groups not yet read). CRISIL uses **pooling of interests** (assets/liabilities/revenue/cost pairs cancelled, investments netted against equity, intra-group borrowings cancelled — no goodwill or valuation exercise required), and classifies every related entity into exactly one of three tiers:

| Tier | Treatment |
|---|---|
| **Fully integrated** | Full analytical consolidation with the parent |
| **Moderately integrated** | No consolidation — CRISIL factors in the ADDITIONAL investment/support the parent may need to provide, and separately tests the parent's existing investment in the entity for impairment |
| **Financial investment** | No consolidation — analysed as any other equity holding, tested for impairment only; requires low strategic importance, minimal economic incentive to support, AND adequate ring-fencing |

This is structurally different in *naming and mechanics* from both ICRA's Full/Limited Consolidation + separate "Consolidated View" concept (`ICRA_CONVENTIONS.md` §10) and CareEdge's inclusion/exclusion list (`CareEdge` Consolidation criteria) — the three agencies converge on similar underlying judgment factors (economic importance, cash-flow fungibility, documentary support, management posture, ownership, shared name) but structure the OUTPUT categories differently. Do not assume a "moderately integrated" CRISIL classification maps one-to-one onto ICRA's "Limited Consolidation."

**Capital Allocation Approach — a CRISIL-specific mechanism with no ICRA/CareEdge equivalent found in either corpus so far:** for a subsidiary in a genuinely different sector from the parent (a finance arm of a manufacturer, an insurance arm of a bank) that CRISIL still wishes to notch up, CRISIL **deducts a specific, objectively-assessed capital amount from the parent's net worth and allocates it to the unconsolidated subsidiary** — the deduction lowers the parent's own rating inputs, the allocation raises the subsidiary's. This is a real, quantifiable mechanic, not a qualitative uplift — if a CRISIL case involves a cross-sector subsidiary getting notched up, this is the mechanism to look for and reproduce, not a generic "support" adjustment.

## 5. Parent/group/government linkage notching — one genuinely numeric rule ICRA and CareEdge do not state

Source: `criteria-for-factoring-parent-group-government-linkages.md`, read this session (Section II, corporate-parent notch-up framework, in full; Sections I/III/IV — government/GRE, group-company, and weak-parent-drags-strong-subsidiary — not yet read in full).

Framework mirrors ICRA's ability/willingness structure but under different labels: **Economic rationale** (strategic importance, extent of holding, economic incentive) + **Moral obligation** (management control, shared name, domiciliary status — a foreign parent has weaker moral obligation than a domestic one — and stated posture) + **Corporate status of the parent** (listed/capital-market-active parents have a higher obligation, since a subsidiary default threatens the parent's OWN capital-raising plans — a factor neither ICRA's nor CareEdge's framework names explicitly).

**⚑ THE ONE NUMERIC RULE: infrastructure SPVs are typically NOT notched up for parent support, or only by a LIMITED 1-2 NOTCHES**, because they are structured as ring-fenced entities raising debt with no explicit parental recourse by design. Quoted directly: *"Usually, infrastructure SPVs are not notched-up / notched-up only to a limited extent of 1-2 notches for parent support."* **Neither ICRA's Implicit Parent Support methodology nor CareEdge's Notching-by-Parent criteria state a numeric ceiling anywhere** (`ICRA_CONVENTIONS.md` §11 confirms ICRA's illustration is purely qualitative — Low/Moderate/High/Very High likelihood mapped to "close to standalone" through "close to parent" with no notch count). **BINDING: for a CRISIL-rated infrastructure SPV, a support-notch count above 1-2 requires an explicit, written justification for why this SPV is the exception to CRISIL's own stated norm — it is not a default assumption the way it might be argued to be under ICRA's more open-ended framework.**

**Financial-sector parents carry higher moral-obligation weighting** than non-financial parents in CRISIL's framework — "money is the raw material for these entities," so a subsidiary default threatens the parent's trust-based franchise more directly. This mirrors ICRA's own note that reputational sensitivity "has been observed to wield relatively greater influence in financial sector ratings" (`ICRA_BANKS_NBFC_CONVENTIONS.md` §1) — a genuine point of convergence.

**JV notching:** CRISIL defaults to a **weakest-link-style caution** for equal-stake JVs (support attributed to whichever sponsor articulates distress support and has the strongest criticality/linkage case), with the same-strength-to-both-sponsors exception ICRA also allows (`ICRA_CONVENTIONS.md` §11) only where both sponsors are strong, both find the JV equally critical, and their interests are aligned.

**PE/Sovereign/Pension/Insurance funds** are treated as NOT parents for support purposes by default (limited investment horizon, exit-for-profit motive) — matching both ICRA's and CareEdge's explicit exclusion of private equity/financial investors from the "parent" definition.

---

# PART B — linkage and consolidation, read in full 06-Sep-2026

*Closes the caveats in §4 and §5 above. `criteria-for-factoring-parent-group-government-linkages.md` is now read in **all four** sections (I government/GRE · II parent notch-up · III group notch-up · IV weak-parent notch-DOWN), and `criteria-for-consolidation.md` in **both** (I consolidation · II homogenous groups).*

## 6. Government-related entities — a 2×2 that ends in "equate to Crisil AAA"

CRISIL scores a GRE on two axes — **policy role** (criticality of the sector to GoI; strategic importance, proxied by how limited private-sector participation is) and **implications of default / moral obligation** (domino effect; political and social implications; public perception of sovereign backing; GoI's stated posture, e.g. letters of comfort, guarantees, or permission to issue tax-free bonds). The four quadrants carry **different notch-up outcomes, one of them absolute**:

| | Low implications of default | High implications of default |
|---|---|---|
| **Low policy role** | **I — no notch-up.** Rating is the standalone. | **II — notch-up may be "much higher"**, driven by the severity of default's impact and the gap between standalone and GoI ratings. |
| **High policy role** | **III — limited notch-up.** Past government support was given to ensure *solvency*, not *timely debt servicing*, so it earns less than it appears to. | **IV — equate to GoI's rating, `Crisil AAA`.** Regulatory agencies and statutory SPVs channelling capital-market funds to strategic sectors sit here. |

The quadrant-III distinction is the subtle one and worth quoting in any PSU workpaper: **equity infusions and loans in the past evidence support for solvency, not for punctuality**, and CRISIL prices that difference. Note also that GoI's February 2021 strategic-disinvestment policy makes this **case-specific** for any PSU in a sector slated for privatisation, merger or closure — the notch-up cannot be carried forward mechanically from a prior review.

The framework extends to entities not held directly by GoI but majority-owned by PSUs.

## 7. Group support is CAPPED in a way parent support is not

This asymmetry is stated explicitly and this project did not carry it:

> *"In case of subsidiaries, it is possible to identify a single-parent entity that will provide distress support. However, if support is expected from a group of companies, it may not be possible to identify a single entity as the source of distress support, resulting in uncertainty regarding the extent and timeliness of support. Therefore, the extent of notch-up for group support is typically limited. This is in contrast to the notch-up of subsidiaries for support from a clearly identifiable parent, where no such restrictions apply."*

So: **parent support — no stated ceiling. Group support — "typically limited."** A workpaper that notches up for "group support" as generously as it would for parent support has misapplied the criteria. (This sits alongside the infrastructure-SPV 1-2 notch cap already recorded as failure mode 52 — CRISIL has two distinct brakes on notching, and neither has an ICRA or CareEdge equivalent.)

Group notch-up is assessed on **economic rationale** (relevance of the company to the group by turnover/profit contribution and strategic criticality; extent of promoter/group shareholding, current and prospective; economic incentive, forward-looking on profitability) and **moral obligation** (extent of management control, including a common treasury; shared name or common logo; commonality of resources such as common bankers or locations; management's stated posture).

**A track-record gate applies:** *"Crisil Ratings may not notch up companies in a group if the track record of supporting group companies is unsatisfactory."* Past behaviour can zero the uplift regardless of how the other parameters score.

## 8. ⚠ The notch-DOWN framework — a whole direction of travel this project never had

`Inputs!C42` in the scorecard is labelled "Parent/group support notches (+ = uplift, − = drag)" and the SOP's Step 13 says only "support notching". Neither says what a **drag** is or how to size it. CRISIL devotes a full section to it, and it applies whenever **the parent is weaker than the subsidiary** — or, equally, whenever a company's standalone rating is above its group's.

The mechanism is that a weak parent, as economic owner, legitimately accesses a strong subsidiary's cash flows. CRISIL names the routes: **purchase/sale of goods on terms structured to hand the parent the margin**; **lenient credit terms to the parent, receivables left unmanaged and eventually written off**; **inter-corporate deposits to the parent at concessional rates**, or ICDs *from* the parent at inflated rates; **fresh debt raised on the subsidiary's books and channelled to the parent**; **the subsidiary guaranteeing the parent's debt**; and **special dividends**, typically large and "coincidentally close to the date when the parent is required to make payment on its maturing debt".

Sizing runs on two axes:

| A. Management control | B. Ease of transfer of funds |
|---|---|
| Extent of parent's shareholding | Common country of domicile |
| Ability to wield control (common board / CEO / CFO; whether a strong minority shareholder or independent directors sit on the subsidiary's board) | Common treasury operations or bankers |
| Corporate status of the subsidiary | **Past instances of not-at-arm's-length transactions / parent's stated posture** |
| | Regulatory or legal restrictions on upstreaming |

**CRISIL weights B.3 — past not-at-arm's-length transactions — above every other parameter**, because such transactions "can potentially wipe out the entire networth or significantly impair financial flexibility of the subsidiary". Listing matters sharply in the other direction: for a **listed** subsidiary the chance of diversion is "very remote" on disclosure norms; for a proprietorship, partnership or closely held company it is "very high".

**Outcomes are bounded at both ends:** very low ability *and* inclination → **no notch-down**; very strong ability *and* inclination → the subsidiary's rating is **equated with the parent's**; moderate → somewhere between the two. When assessing the parent, CRISIL takes a **consolidated** view of the parent and all its subsidiaries, *including the one being rated*.

**Practical consequence for this flow:** at Step 13, establishing the parent's credit profile is not optional even when the subsidiary looks strong — because the parent being *weaker* is precisely the trigger condition for a drag, and a standalone-looking-strong subsidiary is the case most likely to have the drag missed.

## 9. Homogenous groups — the one place CRISIL gives a numeric contribution threshold

For family-owned groups operating one sector through several entities with **no identifiable parent**, CRISIL combines rather than notches. Preconditions for inclusion, all three required: entities **unlisted and fully held by common promoters** with only marginal external shareholding; **business linkages** (similar or related lines, common manufacturing/procurement/marketing, vertical integration); and **financial linkages** (common management control over treasury, seamless fund flow — CRISIL usually takes a promoter undertaking to this effect).

Entities are excluded where there is substantial external shareholding, limited business linkage, independent management, or a different business line — those revert to the **group notch-up** framework instead. CRISIL also tests for **family-faction risk**: where shareholding and board composition cluster by faction and roles are segregated **by company rather than by function** (procurement, marketing, finance), the probability of a split is treated as high and entities across factions are combined only on a strongly articulated commitment against splitting.

Individual entity ratings then sit at or below the group rating, **by up to three notches**, on a rule that is actually arithmetic:

| Condition | Notch-down from group rating |
|---|---|
| Entity contributes substantially to the group | **Equate** to group |
| **Entity EBITDA < 10% of group EBITDA** and it significantly deviates from other group entities → "low contribution" | up to **2 notches** |
| — low contribution, EBITDA not growing in line with group **and** weak financial risk profile vs group | up to **2 notches** |
| — low contribution, but **either** a healthy financial risk profile **or** EBITDA growing in line or better | restricted to **1 notch** |
| — low contribution, but **both** of those hold | **equate** to group |
| Small entity performing a **critical function** (e.g. supplying critical components) | may be **equated** regardless of size |
| **Project entity yet to commence operations** | up to **3 notches**, on project risk relative to the group |

The two-notch ceiling for low-contribution entities is explicitly justified: CRISIL believes "the group has high moral obligations to extend business, financial, and managerial support", so the differentiation cannot run wider.

The same combination approach governs **REITs and InvITs** (trust plus SPV cash flows consolidated; the SPV rating is usually equated to the consolidated group, differentiated only where cash-flow subordination or prioritisation within the group warrants it) and **bundled infrastructure SPVs** under common promoters with fungible cash flows and an intent to support each other.
