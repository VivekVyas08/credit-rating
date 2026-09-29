# CRISIL — corporate (manufacturing/trading/services) sector: ratio and mapping conventions

**Source, read 13-Sep-2026:** `CRISIL/Methodology/criteria-for-manufacturing-trading-and-corporate-services-sector.md` (Section IV, "Crisil Ratings methodology for financial ratios") and `CRISIL/Methodology/basics-of-ratings.md` (LT-ST mapping section), read in full this session as the cross-cutting priority pass after the Cochin Minerals two-notch miss. **Partial corpus** — `criteria-for-consolidation.md`, `criteria-for-factoring-parent-group-government-linkages.md`, `criteria-for-banks-and-financial-institutions.md`, `criteria-for-finance-and-securities-companies.md`, `criteria-for-real-estate-developers-lrd-and-cmbs.md`, `criteria-for-infrastructure-sectors.md` and `criteria-for-securitisation-transactions.md` have NOT been read this session. Treat any gap here as "not yet extracted."

This is the CRISIL twin of `CareEdge/CORPORATE_CONVENTIONS.md` and `ICRA_CONVENTIONS.md`. CRISIL is the **most permissive of the three** on what counts as core income, and the **widest** of the three on what counts as debt.

> Failure mode 32 in one line: *if a definition will not reproduce the agency's published figure, the definition is wrong.* CRISIL's PBDIT is not ICRA's OPBDITA and is not CareEdge's PBILDT — the three are close but not interchangeable, and the differences bite hardest exactly where a small-scale, low-leverage issuer sits (the Cochin Minerals pattern).

---

## 1. PBDIT — the widest "operating profit" of the three agencies

```
Interest coverage ratio = Profit Before Depreciation, Interest and Tax (PBDIT) / Interest and finance charges
```

**CRISIL's own footnote, verbatim:** *"Crisil Ratings, in its computation of PBDIT, includes recurring non-operating income, but excludes one-time, extraordinary income or expense."*

This is a **materially wider inclusion rule than either ICRA or CareEdge.** ICRA's OPBDITA and CareEdge's PBILDT both exclude interest and dividend income even when recurring (see `ICRA_CONVENTIONS.md` §1, `CareEdge/CORPORATE_CONVENTIONS.md` §2) — CRISIL explicitly retains it, as long as it recurs and isn't extraordinary. **Do not carry a CareEdge/ICRA "strip all interest/dividend income" habit into a CRISIL PBDIT calculation** — it will understate the CRISIL figure and any leverage/coverage ratio computed on it.

**Interest and finance charges** include the interest component of lease liabilities, non-funded capitalised interest, and preference dividend.

## 2. PAT margin, RoCE

```
PAT margin = Profit after tax / Operating income
RoCE       = Profit before interest and tax (PBIT) / [Total debt + Adjusted networth + Deferred tax liability]
```

DTL is **added into** the RoCE denominator despite being **excluded from** adjusted networth for gearing purposes (§3) — the same split CareEdge applies (see `CareEdge/CORPORATE_CONVENTIONS.md` §7).

## 3. Gearing — the widest debt definition of the three agencies

```
Gearing                  = Adjusted total debt / Adjusted networth
Total indebtedness ratio = Adjusted total outside liability / Adjusted networth
```

**Adjusted total debt includes:** short- and long-term borrowings, off-balance-sheet liabilities, preference shares, subordinated debt, optionally convertible debentures, deferred payment credit, bills discounted, **AND** — beyond what CareEdge or ICRA name explicitly — **guarantees, factored receivables, pension liabilities, derivatives, and contingent liabilities**, each assessed for likelihood of devolvement and recoverability, including management intent.

**Adjusted networth** excludes revaluation reserves, unwritten-off miscellaneous expenditure, and — stated more explicitly than either other agency — **deferred tax liability**, on the reasoning that DTL "represents the taxman's funds and not the shareholders." Intangibles/goodwill are assessed case-specifically: arm's-length-transaction goodwill amortised over its useful life or 5 years (whichever shorter); acquired intangibles (patents, trademarks, licences) amortised over useful life or 10 years (whichever shorter).

### Box 1: promoter unsecured loans — a codeable three-way test not present anywhere else in this project

CRISIL classifies promoter/family unsecured loans into ONE of three treatments, not a single default rule:

1. **Full debt.**
2. **Fully excluded from debt** (equity-like).
3. **Partial equity treatment — around 75% treated as equity, the remaining 25% as debt** (CRISIL's own stated split, not a generic 50/50).

The classification turns on four named factors, all extractable from a promoter-loan note and the AR's related-party disclosures:

| Factor | Debt-like signal | Equity-like signal |
|---|---|---|
| Subordination to external borrowings | Not subordinated | Subordinated |
| Track record of retention | Frequent withdrawals | Long track record of retention, expected to continue |
| Interest rate charged | Materially above market borrowing rate (suggests promoter arbitraging an external loan into the entity) | At or below market, or nil |
| Deferability / plough-back | Interest always paid on schedule | Demonstrated deferral in distress, or interest ploughed back as fresh unsecured loans |

**BINDING for any promoter-owned, unlisted CRISIL case with a material unsecured-loan balance:** run this four-factor test explicitly in the workpaper before defaulting to "unsecured loans = debt." No equivalent test currently exists in this project's tooling for ICRA or CareEdge cases — check whether either agency's own methodology carries something similar before assuming its absence.

**Indicative note on Total Indebtedness Ratio:** CRISIL calls this out as *especially* relevant for entities financing working capital heavily through non-fund-based facilities (LC) or stretched payables — i.e. exactly the issuers where the CareEdge-style "LC creditors are debt" question matters most.

## 4. Coverage and cash-generation ratios

```
NCATD  = (PAT − dividend + depreciation) / Adjusted total debt (short + long term, incl. off-balance-sheet debt)
Debt/PBDIT = Adjusted total debt / PBDIT      (case-to-case, not universal)
CDSCR  = [PAT + depreciation + interest charges − 25% of incremental net working capital]
         / [debt payable within one year + interest and finance charges]
```

CDSCR's 25%-of-incremental-NWC deduction is structurally the same mechanism as CareEdge's Cash DSCR (`CareEdge/CORPORATE_CONVENTIONS.md` §9: 25% assumed funded from GCA, 75% from working-capital borrowings) — a genuine point of convergence across two of the three agencies, unlike PBDIT/PBILDT/OPBDITA which diverge.

"Debt payable within one year" **excludes** debt normally rolled over (working-capital borrowings, commercial paper) even though it is short-term by tenor — only the current portion of long-term debt and genuinely maturing short-term obligations count.

## 5. Current ratio, GCA days

```
Current ratio = Current assets (incl. marketable securities) / Current liabilities (incl. CPLTD)
GCAs          = Total current assets related to operations / Operating income
```

## 6. LT↔ST mapping — varies BY ENTITY TYPE within CRISIL itself, not just by agency

Source: `basics-of-ratings.md` Table 1 ("Mapping between short-term and long-term ratings"). **This table is agency-specific to CRISIL and further splits by entity type** — a dimension neither ICRA's nor CareEdge's mapping notes carry explicitly for CRISIL to be assumed identical to.

| LT rating | Corporates | Other fin-sector (ex banks/PDs) | PDs | Banks |
|---|---|---|---|---|
| AAA .. AA− | A1+ | A1+ | A1+ | A1+ |
| A+ | (A1+) A1 | A1+ (A1) | A1+ | A1+ |
| A | A1 (A2+) | (A1+) A1 (A2+) | A1+ (A1) | A1+ |
| A− | (A1) A2+ | A1 (A2+) | A1 | **A1+ (A1)** |
| BBB+ | (A2+) A2 | A2+, A2 | (A1) A2+ | A1 (A2+, A2) |
| BBB | (A2) A3+ (A3) | (A2) A3+ (A3) | (A2+) A2 | (A1) A2+, A2 |
| BBB− | (A2, A3+) A3 | (A2, A3+) A3 | (A2) A3+, A3 | A3+, A3 |
| BB+ .. BB | A4+ | A4+ | A4+ | A4+ |
| BB− | A4+ (A4) | A4+ (A4) | A4+ (A4) | A4+ (A4) |
| B, C | A4 | A4 | A4 | A4 |

*(brackets = exceptional-case mapping only, per CRISIL's own table caption)*

**The gap this closes:** at the SAME long-term grade of A−, a CRISIL-rated corporate maps to (A1)/A2+ while a CRISIL-rated bank maps to A1+/(A1) — a full notch better. Applying ICRA's single AAA/AA→A1+-always, B/C→A4-always logic (which happens to agree at the extremes but not in the A/BBB band) or a generic "same table for every agency" assumption to a CRISIL bank or NBFC report will misstate its short-term rating in the A+ through BBB− band. **This table must be looked up by entity type, not just by agency, before any CRISIL LT-ST mapping is asserted.**

CRISIL's mapping process is explicitly a 5-step sequence, not a table lookup alone: (1) assess long-term credit quality, (2) assess liquidity — average monthly bank-limit utilisation over 12 months for non-financial entities, ALM mismatch coverage for financial entities, (3) apply the table above, informed by step 2's liquidity read, (4) evaluate liquidity backup for confidence-sensitive instruments (CP, short-term NCDs), (5) evaluate credit enhancement options if applicable.

---

# PART B — read 06-Sep-2026, the full-corpus pass

*Source: `basics-of-ratings.md` Sections I-V, VII and XII, and `criteria-for-manufacturing-trading-and-corporate-services-sector.md` Section I, all read in full. This closes the "partial corpus" caveat at the top of this file for those files. **Still unread:** `basics-of-ratings.md` Sections VI (global-scale mapping), IX (fixed deposits), X (partial guarantees) and XI (guarantee detail beyond the 12-point framework); the manufacturing file's Sections II (trading), III (education) and V onward (materials and other sector chapters); and, entirely, `criteria-for-infrastructure-sectors.md`, `criteria-for-securitisation-transactions.md`, `criteria-for-real-estate-developers-lrd-and-cmbs.md`, `criteria-for-public-finance.md`, `criteria-for-insurance-companies.md`, `criteria-for-future-flow-transactions.md`, the expected-loss, REIT/InvIT, bond-fund, capital-protection-fund, ICE, holding-company, intraday-MF and security-receipt criteria. Treat any gap here as "not yet extracted."*

## 7. Hybrid instruments — CRISIL's corporate cap is 20%, and it is the THIRD of three similar caps

**"Crisil Ratings limits the total equity content for hybrids for an issuer to 20% of its adjusted net worth."** (basics-of-ratings.md III.2, non-financial corporates.)

This project had recorded two hybrid caps and built a conflation check on them. There are **three**, all within ten percentage points of each other, and the one that was missing is the one covering this project's commonest case type:

| Agency | Entity class | Cap | Base | Nature |
|---|---|---|---|---|
| ICRA | Corporate (non-financial) | **30%** | adjusted equity | analytical |
| **CRISIL** | **Corporate (non-financial)** | **20%** | **adjusted net worth** | **analytical** |
| CRISIL | NBFC / HFC | **15%** | Tier I capital | regulatory (RBI), applied analytically |

Equity content is scored into three buckets — **Low 0-25% · Intermediate 26-50% · High 51-75%**. Note the ceiling is **75%, not 100%**: no corporate hybrid is ever treated as pure equity under this framework (compulsorily convertible securities are, but they are classified as equity outright rather than scored here).

**The eight scoring parameters**, of which CRISIL says the **first four carry higher weight**:

1. **Level of fixed coupon component** — the fixed component must be **materially lower, by at least 5%, than a comparable debt-market benchmark rate** to earn 'high' equity treatment. The greater the gap, the lower the debt content.
2. **Permanence** — **residual maturity under 5 years earns no equity treatment at all** (the same 5-year cliff ICRA applies, one of the few places the two agencies agree numerically). Where a call option exists, **the first call date is the residual maturity**, not the stated tenor. A replacement capital covenant extends residual maturity, but only counts if it *substantially* does so and is enforceable.
3. **Deferability** — **mandatory** deferral ranks above **optional** deferral, because it removes issuer discretion.
4. **Relevance of the deferral trigger** — a trigger that will never realistically be breached earns nothing ("the trigger for a highly rated issuer cannot be diminution of net worth by 80%"). Triggers tied to *profit* rank above triggers tied to *equity dividend payment*, since a strong issuer will pay dividends out of reserves in a bad year.
5. **Cumulation** — non-cumulative ranks above cumulative.
6. **Call options** — the shorter the period to call, the lower the equity content. Multiple call dates do not materially help.
7. **Step-ups** — reduce equity content; instruments without step-ups rank higher.
8. **Position in the capital structure** — greater subordination, higher equity content. **Non-subordinated hybrids are unlikely to get equity treatment whatever else they score.** If investors can initiate winding-up after non-service for **2 or more years**, it reads as debt.

**Standing instrument treatments:** compulsorily convertible → **pure equity**; optionally convertible → **usually debt** unless equity-like features are demonstrated; FCCBs → **mostly debt**, equity only where yield is very low or conversion price sits at/near market; preference shares in India → **mostly close to debt** despite being promoter-held, because of short maturity and high coupon.

**⚠ Default on a hybrid is still default.** *"If the issuer skips or defers payment on the instrument, the rating on the hybrid instrument will be downgraded to 'Crisil D', even though it may be permitted to do so as per the terms of the instrument."* Equity content governs the *capital-structure* treatment; it never softens *default recognition*. CRISIL also warns that hybrid rating transitions are **sharper** than conventional debt for exactly this reason.

## 8. Default recognition is FACILITY-TYPE-SPECIFIC — "1 day / 1 rupee" is only half the rule

This project's SOP has carried "the default-monitoring obligation (1-day/1-rupee → D)" as a single generic rule. For CRISIL that is correct only for facilities with a pre-defined repayment schedule. For working-capital and non-fund-based facilities the threshold is **30 days**, and CRISIL says so in a table (basics-of-ratings.md, Annexure I to Section III):

| Facility | Scale | Default recognised when |
|---|---|---|
| Term loan · WCTL · WCDL · debentures/bonds · CD/FD · CP | LT/ST | **Delay of one day, of one rupee**, from the scheduled date |
| Packing credit (pre-shipment) | ST | Overdue/unpaid **> 30 days** |
| Buyer's credit | ST | Continuously overdrawn **> 30 days** |
| Bill purchase / discounting / negotiation | ST | Overdue/unpaid **> 30 days** |
| **Cash credit** | **LT** | Continuously overdrawn **> 30 days** |
| **Overdraft** | ST | Continuously overdrawn **> 30 days** |
| Letter of credit | ST | Overdue **> 30 days from devolvement** |
| Bank guarantee | ST | Unpaid **30 days from invocation** |
| FX forward contract limit | ST | Crystallised losses unpaid **> 30 days** |

The 30-day threshold requires the overdrawing to be **without the express written consent of the bankers**, and CRISIL may ask the banker whether a delay was the lending bank's operational lapse rather than borrower stress.

**Curing period:** at least **90 days** of regularised, timely servicing before any upgrade, and the rating generally moves only to **non-investment grade**; upgrade to **investment grade** generally needs **365 days**. CRISIL may deviate on named grounds (management change, acquisition by a stronger firm, sizeable long-term inflow, regulatory benefit, force majeure, restructuring with the business profile intact, or a delay that was operational rather than credit-driven).

**Other default rules worth having in writing:** default on **unrated** external debt very likely drags the rated instrument to near-default, absent strong mitigants such as external credit enhancement; a restructuring request does **not** suspend the original schedule — default runs from the original dates until lenders formally approve; an **operational creditor's** insolvency petition, even if admitted, does not automatically force D (CRISIL may use Rating Watch instead) whereas a financial-creditor or self-initiated petition does; a coerced exchange with a haircut is default; and a past default discovered late is recorded by downgrading to D and **simultaneously** upgrading to reflect the subsequent track record.

## 9. Facility → rating scale is prescribed, and cash credit is LONG-term

Maturity for this purpose is the **original contracted maturity, not residual** — a seven-year term loan with eight months left is still rated long-term. Cash credit and WCDL are sanctioned for a year but rolled over, so RBI requires and CRISIL assigns **long-term** ratings to them.

| Long-term | Short-term |
|---|---|
| Cash credit · Working capital demand loan · Term loans · ECBs · Mortgage loan facility | Packing credit · Post-shipment credit · Purchase bill discounting · Bill purchase/discounting · Factoring/forfaiting · Short-term loan · Vendor financing · **Bank guarantee · Letter of credit · FX forward contract limit** |

*(FCNR loans follow tenure.)* Where a limit is **fungible** between long- and short-term draw-downs, the portion drawable long-term is rated on the long-term scale and the remainder on the short-term scale.

**Caution before mechanising this.** CRISIL's own published action for Creative Newtech (04-Dec-2025) rates "Export Packing Credit" at `Crisil BBB+/Stable`, i.e. on the long-term scale, where this table says packing credit is short-term. Either the facility is a sub-limit of a long-term line or the published annexure groups it — either way, **a checker built naively on this table would flag CRISIL's own publications as wrong**, which is failure mode 37's calibration lesson. Use the table analytically; do not gate on it without first reconciling it against a sample of published annexures.

## 10. Security gives NO rating uplift; policy-mandated cash is not free cash

**"Crisil Ratings does not provide any uplift to the facility rating on account of the underlying security."** A rating addresses probability of default; security affects loss-given-default, and lenders enforce security only *after* default. The worked example CRISIL gives is the **10-20% cash margin on an LC facility** — it does not prevent default, so it earns nothing. What *does* count is **unencumbered liquid assets**, which add genuine financial flexibility.

A refinement for corporate-services and IT issuers: where a company holds cash as policy to cover a stated number of months of employee cost, **CRISIL counts only the cash in excess of that policy requirement** as financial flexibility. Policy-required cash is, in effect, encumbered — the same principle as failure mode 45, arriving from a different direction.

## 11. Outlook and watch — CRISIL quantifies both, and neither attaches to C or D

- **Outlook horizon is six months to two years.** A Positive or Negative outlook means a **material likelihood, "at least one in three"**, of an upgrade/downgrade. This is the only numeric probability any of the three agencies puts on an outlook in the corpus read so far.
- **Outlooks are NOT assigned to `Crisil C` and `Crisil D` category ratings**, and never to short-term ratings. A report or scorecard printing "Crisil C/Stable" is malformed on CRISIL's own rule.
- **Rating watch is typically resolved in about 90 days**, applies to **all** instruments including short-term ones, and **ratings on watch carry no outlook**.

## 12. Rating scale is 20-point on the long-term side — FIXED 13-Sep-2026

CRISIL's long-term scale is **20 points**, `Crisil AAA` to `Crisil D`, with `+`/`-` applied **from AA down to C** — so **C+, C and C- all exist**, and D is a scale point. The short-term scale is **9 points**, A1+ through A4 plus D. `Ref_Scales` previously ran AAA (index 0) to C (index 16) with **no C+, no C- and no D at all**, so the sheet could not express a CRISIL default or a near-default gradation. **Extended 13-Sep-2026** to the full 20 points plus D: index 16 = C+, 17 = C, 18 = C-, 19 = D, with the clamp moved from `MIN(16,` to `MIN(19,` in the Rating sheet. **Indices 0-15 (AAA..B-) are unchanged**, which is what makes the change safe — every hard cap is expressed as an index (`MAX(C13,15)` = B-, `MAX(C13,13)` = B+, `MAX(C13,10)` = BB+) and therefore keeps its exact meaning. Applied to the template and all 22 live case workbooks; every one re-resolves its anchor and assigned grade unchanged. The same three grades were added to `_ICRA_LT_ANCHORS` and to both grade regexes in `check_sections.py`, and to the `SCALE` lists in `rate_engine.py`, `corpus_mine.py`, `corpus_power.py` and `corpus_stats.py`, which carried D but not C+/C-.

**A deliberate design point, recorded so nobody 'fixes' it:** the composite-to-index map in `Rating!C11` still multiplies by **16**, not 19. That multiplier is the back-tested calibration (power p=1.4, zero bias, `Docs/Scorecard_Backtest_Report_18Jul2026.md`); re-scaling it to 19 would move every case's anchor and invalidate the back-test. The three new grades are therefore reachable only through the **business-risk ceiling** (`Scorecard!C44`) or a **committee override** (`Inputs!C66`) — which is correct, because nothing in the financial composite alone should push an issuer into the C category; that is a judgement about imminent default, not a ratio result.

## 13. Information adequacy / INC — three numeric triggers

- **No-Default Statement not received for three consecutive months** → migrate to INC within **5 working days** (reduced from 7 by SEBI circular of 7 January 2025), unless the banker or debenture trustee confirms timely servicing.
- **Non-cooperation beyond six months** → the rating **must** be downgraded to non-investment grade with INC status if it is not already there.
- INC ratings are "unlikely to be in high safety category or above"; investment grade may be retained with INC only case-by-case, on cash-flow stability, timely servicing and satisfactory banker feedback.
- The mandated footnote is exactly: *"Issuer did not cooperate; based on best available information"*.
- Neither trigger applies to ratings already at INC or at D.

## 14. Business risk is descriptive, and industry risk sets a MEDIAN

CRISIL's business-risk framework is **industry risk → market position → operating efficiency**, and — as with ICRA and CareEdge — **not one of its parameters carries a numeric band**. This is the CRISIL leg of the evidence behind failure mode 53.

One framing here is worth borrowing outright: **"The industry risk rating largely indicates the median rating for companies in that industry"**, with market position, operating efficiency and financial position determining where an individual company sits relative to that median. That is a *starting point plus deviation* model, not a weighted average — and it is a better description of what the Stage 1 anchor plus business-risk ceiling is trying to do than anything currently written in the scorecard.

Two specific CRISIL cautions:

- **Market share is not market position.** *"A large market share is not always synonymous with competitive advantages or industry dominance if the company does not have the flexibility to determine the selling price of its products."* Where landed import cost governs prices, even a large player lacks pricing leadership — the Cochin Minerals situation exactly.
- **Risk appetite is a management-risk factor with a named red flag:** high leverage, or *"a propensity to undertake projects that are larger than existing operations"*, is explicitly "not viewed favourably". Project risk is weighted by **the size of the project relative to existing operations**.

**ESG materiality has a stated test:** sectoral characteristics, **proportion of foreign investment holding**, and **existence of external market borrowings**. An ESG section that does not engage with those three has not applied CRISIL's own materiality filter.

## 15. Guarantees — the 12-point framework, and when CE is NOT used

The `CE` suffix is applied **only if the supported rating exceeds the unsupported rating**. If the structure produces no uplift, no suffix is used — a guarantee that changes nothing is not disclosed as an enhancement. `SO` is for bankruptcy-remote structures; `CE` for external enhancement where the instrument is *not* bankruptcy remote.

A guarantee must satisfy **all twelve** points to support a CE rating: unconditional · irrevocable · legally enforceable · covering the facility **in its entirety** (partial guarantees give comfort only to their extent) · an obligation to **pay**, not merely to procure payment · a payment mechanism with stated invocation and payment timelines · payable on **first demand** · **without deduction** · with the guarantor's Indian Contract Act §133 rights **waived** (and the guarantee **re-affirmed** on any change of contract terms) · guarantor as **primary obligor** · payable **even in insolvency** of the borrower · and, for an **overseas guarantor**, a continuous rating from S&P, Fitch or Moody's corresponding to a lower risk weight than the borrower's standalone rating.

## 16. ⚠ Global-scale ratings map to the national scale 6 to 7 NOTCHES HIGHER

*Source: `basics-of-ratings.md` Section VIII. Added 13-Sep-2026 — this project had no rule anywhere on the subject, so a foreign parent's S&P grade could be, and would have been, used as though it sat on the Indian scale.*

> *"A global scale rating… tends to map to a rating on the Crisil Ratings scale which is typically **6 to 7 notches higher**."*

| Global scale (S&P) | Crisil national scale |
|---|---|
| **BBB+** | AAA or AA+ |
| **BB+** | AA- or A+ |
| **B** | BB+ or BB |

**The gap NARROWS at the lower end** — it is not a constant offset, so a single "+6" rule applied across the scale is wrong at both ends.

Four further rules that travel with it:
- The mapping uses the **global scale LOCAL CURRENCY** rating, not the foreign-currency one.
- It is refined by the parent's **outlook**, the industry/economic scenario, and recent rating-action history.
- **Scope limit, stated explicitly:** the mapping is used ONLY to assess a foreign parent when notching an Indian subsidiary. It is **never** used to rate a global entity on CRISIL's scale.
- Where the parent gives an **explicit guarantee**, the mapping question falls away — the rating then depends **solely** on the guarantor's credit quality (and government-guaranteed instruments carry the highest rating on the CRISIL scale).

**⚠ DO NOT CARRY THE 6-7 NOTCHES TO AN ICRA CASE.** ICRA maps from **Moody's**, not S&P, publishes **no notch count at all**, and describes a different curve shape: the divergence is **most pronounced in the lower investment-grade segment**, narrowing toward both higher investment grade and lower non-investment grade. ICRA also prefers a first-principles assessment, using mapping only where information access does not permit one, and warns specifically that an entity rated at India's sovereign level globally does **not** automatically map to `[ICRA]AAA`. See `ICRA_CONVENTIONS.md` for ICRA's own treatment. Applying CRISIL's number to an ICRA case is failure mode 33 in its purest form.

Mechanical enforcement: `check_sections.py` probe *"Global-scale rating mapped before use on the national scale (failure mode 61)"*; controls in `tools/test_re_and_globalscale.py`.

## 17. Fixed deposits — the one place CRISIL rates an instrument ABOVE the issuer

- An FD programme of more than one year is rated on the **20-point long-term scale**; bank FDs of up to one year go on the short-term scale.
- **In general the FD rating equals the issuer's long-term rating**, because deposits rank pari passu with other senior debt.
- **EXCEPTION — scheduled commercial banks: CRISIL may rate the FD programme ONE NOTCH ABOVE the issuer rating.** Its stated reasons: no depositor has lost money in an Indian scheduled commercial bank, systemic liquidity access, RBI oversight, and DICGC deposit insurance. Public/private ownership and the granularity and maturity profile of the deposit base are also weighed.
- Both RBI and the MCA require a **minimum investment-grade rating** before deposits may be raised.

## 18. Obligor / co-obligor (restricted) groups — CE does NOT apply

Where entities are bound by **legally enforceable cross-default agreements to which the lenders are party**, with cash-surplus entities supporting cash-deficit ones, CRISIL **consolidates the group**, rates the consolidated entity, and then derives individual entity ratings **equal to or close to** the group rating.

**The `CE` suffix may NOT be applied to these**, because the cash-flow pooling is already inside each entity's own credit profile — it is not third-party external support. This is a genuine trap: the structure looks like credit enhancement and is not.

*(Contrast ICRA, which for contractual surplus-sharing among SPVs likewise applies **no (CE) suffix**, but reaches it by a different route — pre-default timelines give all entities the same notional group rating, post-default timelines give an uplift capped at the group rating, and undefined timelines give no benefit at all.)*
