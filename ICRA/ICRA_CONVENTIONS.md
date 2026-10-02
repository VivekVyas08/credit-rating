# ICRA — corporate sector: ratio and mapping conventions

**Source, read 13-Sep-2026:** `960~Corporate Credit Rating Methodology`, `927~Financial Ratio Analysis`, `934~Consolidation`, `962~Explicit Third-Party Support`, `963~Implicit Parent or Group Support`, `998~Hybrid Instruments`, `1014~Liquidity Analysis (Non-Financial Sector)`, `110~Outlook and Rating Watch`, and `mapping.md`, read in full this session as the cross-cutting priority pass after the Cochin Minerals two-notch miss (three infra sector files — Power Thermal, Power Transmission, Roads HAM — were also read for the same-template confirmation, not reflected in this corporate-focused file). **Remaining gap:** `995~Structural Features`, `134~Default Recognition`, `138~Complexity Indicator`, `929~Banks & Financial Institutions`, `1003~NBFCs` and the ~90 other sector-specific files have NOT been read this session. Treat any gap here as "not yet extracted", never as "ICRA has no rule."

This is the ICRA twin of `CareEdge/CORPORATE_CONVENTIONS.md`. It exists because CLAUDE.md's Step 12b(a) previously asserted "ICRA OPBDIT strips other income unconditionally" — a claim that turned out to be false the moment the actual methodology was opened.

> Failure mode 32 in one line: *if a definition will not reproduce the agency's published figure, the definition is wrong.* Use these verbatim, and do not assume ICRA's numbers behave like CareEdge's or CRISIL's just because the formula names look similar.

---

## 1. Operating profit (OPBDITA) — **corrects a standing project error**

**Include:** revenue from operations net of indirect taxes, **plus core-related other income** — job-work income, sale of scrap, duty drawback, and similar items core to operations.

**Exclude — even when recurring:** interest income, dividend income, and other non-core income. ICRA's own footnote: *"other forms of income like the interest or dividend received are not considered under operating income though they might be recurring in nature."*

This is **not** an unconditional strip of all other income — it is the same core-vs-non-core split CareEdge and CRISIL both apply, worded slightly differently. The three agencies converge here far more than this project's documentation previously claimed; treating ICRA as "strip everything" caused core items (job-work, scrap, duty drawback) to be wrongly excluded from OPBDITA on any case where this rule was actually enforced as written.

## 2. PBIT margin and RoCE

```
PBIT margin = Profit before Interest and Tax / Operating Income     (manufacturing entities: depreciation is a proxy for reinvestment need)
RoCE         = Profit before Interest and Tax / Average Capital Employed
Capital Employed = Total Debt + Net Worth + Deferred Tax Liability
                    − Capital Work in Progress − Capital Advances
```

RoCE is read **in the context of business risk**, not in isolation: ICRA explicitly warns that a high RoCE earned in a high-risk business is not directly comparable to the same RoCE in a stable one, and that a track record of **volatile** RoCE reflects an infirm business position independent of the level.

**Indicative metrics (Financial Risk only — see §7 on why these do not extend to Business Risk):**

| Ratio | Strongest | Weakest |
|---|---|---|
| RoCE | ≥25% | <10% |
| Volatility in RoCE | ≤10% | >55% |

## 3. Leverage

```
Gearing            = Total Debt / Tangible Net Worth
Indebtedness Ratio = Total Outside Liabilities / Tangible Net Worth
                      (also computed against Market Capitalisation)
Debt to Profit Ratio    = Total Debt / Operating Profit
Accruals to Debt Ratio  = Net Cash Accruals / Total Debt
```

**Total Debt** = long-term and short-term debt + lease liabilities¹ + off-balance-sheet liabilities (e.g. discounted receivables) + debt component of hybrid instruments (per ICRA's own contractual-terms assessment) − cash reserves earmarked for debt servicing².

¹ *For entities where Ind AS-116 does not apply, ICRA makes suitable adjustments for future lease rentals.*
² *Only if usable before the debt-servicing due date; if usable only after, the reserve is instead deducted from gross debt, and it does not support liquidity.*

**⚠ Total Outside Liabilities is a WIDER number than Total Debt**, and — unlike CareEdge and CRISIL — **this methodology text does not name acceptances / creditors on LC as a component of Total Debt for gearing.** They appear to sit inside Total Outside Liabilities (the Indebtedness Ratio denominator target), not inside Total Debt (the Gearing numerator). This is a real, evidenced difference from CareEdge (`CORPORATE_CONVENTIONS.md` §10: "acceptances / creditors on LC" explicitly IN total debt) and from CRISIL (which folds in guarantees and factored receivables too, see `CRISIL_CONVENTIONS.md`). **Do not carry the CareEdge/CRISIL LC-inclusion rule into an ICRA gearing calculation without independently confirming it against an ICRA-published figure for that issuer** — the Cochin Minerals-style miss runs in both directions: applying a peer agency's WIDER debt definition to ICRA would overstate its gearing exactly as applying ICRA's narrower one to CareEdge understated Cochin Minerals'.

**Tangible Net Worth** = Net Worth − Revaluation Reserves + Minority Interest + Share Application Money + equity component of hybrid instruments (per ICRA's contractual-terms assessment).

**Total Outside Liabilities** = Total Debt + all long-term and short-term external liabilities (Deferred Tax Liability, creditors, other operating/non-operating liabilities).

**Net Cash Accruals** = Net Profit after Tax + Depreciation − Dividend on Preference and Equity Shares.

**Indicative metrics:**

| Ratio | Strongest | Weakest |
|---|---|---|
| Indebtedness Ratio | ≤0.9x | >3.0x |
| Debt to Profit Ratio | ≤0.5x | >5.0x |

## 4. Coverage

```
Interest Coverage Ratio = Operating Profit / Interest expense
DSCR = (Net Profit After Tax + Interest + Depreciation)
       / (Gross Interest + Repayment + Dividend on Preference Shares)
```

Interest coverage is most relevant where most debt is non-amortising (working capital, bullet term debt); it says nothing about principal repayment capacity, which is what DSCR is for. A DSCR below 1x is **not automatically** a stress signal — ICRA explicitly allows for financial flexibility, refinancing ability, or liquidity/internal sources to offset it, and for project-finance structures with long moratoria and ballooning schedules, low early-year coverage can be by design.

**Indicative metrics:**

| Ratio | Strongest | Weakest |
|---|---|---|
| Interest Coverage | ≥18.0x | <2.0x |
| DSCR | ≥4.0x | <1.1x |

## 5. Liquidity

```
Current Ratio            = Current Assets / Current Liabilities
Gross Cash Conversion Cycle = Debtor Days + Inventory Days
Working Capital Cycle    = Debtor Days + Inventory Days − Payable Days
Working Capital Intensity = Net Working Capital / Operating Income
```

Internal resources: cash flows from operations, **unencumbered** cash and cash equivalents, monetisable physical/financial assets. External: undrawn credit lines, shareholder capital. ICRA explicitly reserves a slice of operating income for day-to-day operations before assessing surplus cushion. Full detail deferred to `Rating Approach – Liquidity Analysis (Non-Financial Sector)`, **not yet read this session.**

## 6. Cash flow measures

```
FFO (Fund Flow from Operations) = Operating Cash Flows − Interest Paid
CFO (Cash Flow from Operations) = FFO − cash consumed funding working capital
RCF (Retained Cash Flows)       = CFO − Dividends Paid
FCF (Free Cash Flows)           = RCF − Capex − Debt Repayments
Cash Flow Ratios                = FFO/Total Debt and RCF/Total Debt
```

## 7. The structural point this file exists to make

ICRA's own Credit Risk Categorisation splits Industry / Business / Financial / Management / Other Factors into separate buckets. **Only the Financial Risk factors (profitability, leverage, coverage above) carry a numeric Strongest/Weakest indicative band.** Business Risk factors — competitive position, scale, market share, diversification, asset quality — are assessed with **descriptive** Strongly-positioned / Weakly-positioned language and NO numeric threshold anywhere in this methodology. ICRA states this explicitly for scale: *"ICRA does not form an unfavourable view of an entity merely because it has a small scale."*

**This is the same structural split found in CareEdge's Manufacturing methodology** (see `CareEdge/Docs/corpus_review/findings_CareEdge_methodology_01.md`), and it is why this project's scorecard tool — which folds Business Risk into the same weighted composite as the Financial Risk ratios — produces anchors that are wrong by multiple notches for small-but-financially-clean issuers. **BINDING: no scale/diversification/competitive-position score may be averaged numerically with a leverage/coverage/profitability ratio in the anchor composite.** Business Risk factors gate or bound Stage 1; they are not inputs to its arithmetic.

## 8. Liquidity — sources and claims, over a "near term" that is not always 12 months

Internal sources: fund flows from operations (measured **post interest and tax, pre-working-capital-changes**, excluding non-cash items) + core-related non-operating fund flows (assessed for **sustainability, timing, value** before being counted — a promoter dividend stream is discretionary and not assumed) + unencumbered cash/liquid investments. External: undrawn lines of credit (assessed against the **lower of sanctioned limit or drawing power**, over 12-24 months of utilisation history) + committed parent/investor funding (only what is **already committed with a track record**, never expectation of extraordinary support — that is a rating factor, not a liquidity source).

**Encumbered cash (DSRA, margin for non-fund-based limits) is a liquidity source ONLY if usable on or before the due date it secures** — otherwise it merely nets against gross debt (same rule as §3's footnote 2, restated here because it governs Step 11, not just gearing).

**"Near term" is not fixed at 12 months** — ICRA explicitly widens or narrows the window for seasonal businesses (sugar, cotton ginning, wind/solar) or lumpy-collection entities (education) where cash obligations and inflows bunch on a monthly/quarterly basis that a 12-month aggregate would hide.

**Liquidity's weight in the rating varies by how binding it is, not a fixed factor:** ICRA states three regimes explicitly — (a) poor liquidity caps the rating in non-investment grade *regardless* of other credit positives; (b) strong-vs-exceptionally-strong liquidity has diminishing marginal benefit once other factors are already strong/adequate; (c) even strong liquidity cannot rescue a rating if the fundamental business/financial risk profile is weak. This is itself a caution against a scorecard treating liquidity as one more additive score.

## 9. Hybrid instruments — a codeable equity-credit table with a hard cap

Not present anywhere else in this project's tooling. Source: `998~Hybrid Instruments, Rating Methodology, Nov 2025.md`.

**Equity credit (0-25% / 25-50% / 50-100%) is assessed on three axes**, each independently scored:

| Axis | Weak → equity credit low | Strong → equity credit high |
|---|---|---|
| Trigger strength for payment deferral | Optional deferral (issuer's discretion); or mandatory but only at a level near actual default (e.g. DSCR <1.0x) | Mandatory, triggers well before senior-debt distress (e.g. DSCR <1.5x, or >2-notch downgrade) |
| Permanence of deferral | Cumulative (deferred payment accrues, paid later) | Non-cumulative (deferred payment permanently foregone) |
| Residual tenor | <5 years → **zero equity credit regardless of trigger strength** | ≥5 years, mandatory+strong+non-cumulative → up to 100% |

**A zero/near-zero coupon instrument is treated as equivalent to "mandatory and strong, non-cumulative."** Optionally convertible instruments are analysed as non-convertible (no conversion assumed); mandatorily convertible instruments get 25-100% by the same three axes, or a flat 100% if conversion is due within 3 years, the entity is investment grade, and the coupon does not exceed the entity's general market borrowing rate.

**⚑ HARD CAP: total hybrid equity credit may not exceed 30% of the entity's Adjusted Equity** (= conventional equity + hybrid equity credit), for non-financial entities. Formula for the capped figure:

```
Capped Hybrid Equity = (0.30 × Conventional Equity) / (1 − 0.30) = 0.4286 × Conventional Equity
```

This binds regardless of how strong the instrument's own attributes are — a 75%-eligible instrument can still be capped down to an effective 43% implied credit if the entity has issued enough hybrid capital to breach the 30% adjusted-equity ceiling (ICRA's own worked example). **Never apply an instrument's Table-1 percentage directly to net worth without checking this cap first.**

Balance-sheet adjustment: hybrid equity credit adds to net worth, the balance to debt. P&L adjustment: the hybrid's payment splits into fixed (interest-like) and optional (dividend-like) expense in the **same proportion as the equity credit** — e.g. 40% equity credit on a coupon means 40% of that coupon is treated as an optional/equity-like outflow, not fixed interest.

## 10. Consolidation — beyond CareEdge's framework, ICRA distinguishes "Consolidation" from "Consolidated View"

Source: `934~Rating Approach, Consolidation, Nov 2024.md`. Broadly mirrors CareEdge's Consolidation criteria (same triggers: business linkage, control, guarantees/cross-default, moral obligation, fund-flow history) but adds a distinction CareEdge's file does not make explicit:

- **"Consolidation"** — parent and subsidiaries assessed together, but each entity's OWN rating can still differ (weaker subsidiaries uplifted from standalone by degree of expected support, not automatically equalised).
- **"Consolidated View"** — used when linkages are so complete that all entities are treated as **operating as a single enterprise in substance** (common brand/management/high cash-flow fungibility), and **every entity gets the identical rating** as the parent, not merely an uplifted one.

**Worked "adjusted gearing" example worth replicating in any case with material inter-group investment:** a balance sheet showing 0.6x headline gearing can be genuinely 3.2x on an adjusted basis once net worth trapped funding non-fungible group investments is backed out of the denominator — **low headline gearing is not automatically a credit positive** if it is the mechanical floor imposed by margin/investment requirements rather than a real deleveraging choice.

**Infrastructure SPV nuances not covered by the generic corporate consolidation rule:** DSRA at one SPV cannot support another SPV or the parent; surplus-cash upstreaming timing (post-covenant-satisfaction) may lag the year the cash was generated, and this lag is a liquidity-assessment input, not a consolidation input; a stronger SPV with escrowed, ring-fenced cash flows and **no cross-default** to the parent can be rated ABOVE a weaker parent; the same SPV WITH a cross-default clause is instead uplifted bottom-up from its standalone rating (not automatically equalised) and can be rated above the parent only if it has no funding dependence on the parent.

## 11. Parent/group support notching — no numeric formula exists here either

Source: `963~Implicit Parent or Group Support, Rating Methodology, Jul 2025.md`. Confirms and extends §7's structural point: **the extent of notch-up for parent/group support is illustrated only qualitatively** — "Low" likelihood of support → final rating close to standalone; "Very High" → close to the parent's rating; "Moderate"/"High" → somewhere in between, with no stated formula converting the four willingness factors (business linkages, strategic importance, reputation sensitivity, demonstrated intent) or two ability factors (parent's own rating, structural constraints on fund flow) into a specific notch count. **Any tool that reports a support-notch count as a precise, derived number is presenting a judgment call as an arithmetic one** — the number itself must be argued in the workpaper the same way a Stage 2 overlay notch is argued, not read off a formula that does not exist in ICRA's own methodology.

Government-owned entities get a SEPARATE willingness framework (strategic-sector role, systemic-consequence-of-default, ownership control, dominance of the entity's service, limited private-sector substitutability, support track record) rather than the corporate parent-subsidiary one — do not apply the corporate factors to a sovereign-linked issuer.

## 12. LT↔ST rating mapping

Source: `Methodology/mapping.md`. The chart itself is an unreadable image in the markdown conversion — no cell-level table survives — but the surrounding prose gives the two anchor points and the mapping logic:

- **[ICRA]AAA or [ICRA]AA → always [ICRA]A1+.**
- **[ICRA]B or [ICRA]C → always [ICRA]A4.**
- In between, a long-term grade can map to **either of two** adjacent short-term grades (e.g. [ICRA]A+ → [ICRA]A1+ **or** [ICRA]A1), and the choice is driven by the entity's **relative liquidity assessment** — a superior/strong liquidity profile earns the stronger short-term grade at the same long-term level.

This is **ICRA's own mapping and applies to ICRA reports only.** CLAUDE.md's Step 13 previously stated this table without naming its agency and applied it to CareEdge and CRISIL reports as well. See `CRISIL_CONVENTIONS.md` §5 for CRISIL's materially different, entity-type-dependent table (corporates vs financial-sector entities vs primary dealers vs banks get different mappings at the same long-term grade). **CareEdge's own LT-ST table is corrupted (blank) in the reference library — do not reconstruct it from ICRA's or CRISIL's shape.**
