# CRISIL — real estate: the CFO-based ratio set, LRD and CMBS

*Source: `criteria-for-real-estate-developers-lrd-and-cmbs.md` (9,219 words), read in full 13-Sep-2026 as part of the completed CRISIL methodology corpus. Added because this project had been assessing developers on accrual coverage and ordinary gearing — the ratios CRISIL explicitly does not use for the sector. This is the root cause behind failure mode 40 (Godrej Properties).*

---

## 0. Why this file exists

Failure mode 40 records that the scorecard's accrual interest-coverage hard cap forced Godrej Properties from A+ to B+ and manufactured **nine of its twelve notches** of apparent divergence, and that the remedy adopted was to let the cap be *disapplied in writing*.

That remedy was directionally right and diagnostically wrong. The cap fired because accrual interest coverage is negative **by construction** for a developer under Ind AS project-completion accounting — but the deeper point is that **CRISIL publishes a different ratio set for the sector, and this project simply was not using it.** Disapplying a wrong ratio is not the same as computing the right one.

---

## 1. The developer ratio set — what CRISIL actually computes

**CFO (adjusted)** is the spine of the whole framework:

```
CFO (adjusted) = Collections
               - Construction expenses
               - Other operating expenses
               - JV / JDA / DM-related outflows
```

Everything else is built on it:

| Ratio | Computation | CRISIL's own gloss |
|---|---|---|
| **Debt to CFO (adjusted)** | Debt outstanding / CFO (adjusted) | *"akin to the debt to EBITDA ratio"* |
| **CFO (adjusted) to interest** | CFO (adjusted) / Interest obligations | *"akin to the interest coverage ratio used for assessing manufacturing and services entities"* |
| **Cash buffer ratio** | (CFO adj − tax + debt availed for construction + other cash-flow items) / (Principal + Interest) | — |
| **Adequacy of committed receivables** | Committed receivables from ongoing projects / (Balance construction cost + cumulative debt servicing of ongoing projects) | its corollary is **the velocity of new sales required** |

**⚠ The cash buffer ratio counts debt to be availed as an INFLOW.** That looks wrong against every other sector's convention and is deliberate: in real estate, construction debt is *working capital* bridging the gap until customer advances arrive. Treating it as a financing item rather than an operating inflow understates the developer's actual cash position.

**Leverage (Debt/Equity) is NOT the financial-position measure.** It is used only as a **structural anchor inside FINANCIAL FLEXIBILITY** — a secondary consideration, not the primary leverage read. A developer assessed primarily on gearing is being assessed on the wrong axis.

**Net-debt approach is permitted** where surplus cash is genuinely unencumbered and is not held for working capital, operations or land acquisition.

---

## 2. Sale versus lease — two tracks, analysed separately then combined

- **Residential and commercial-for-SALE** → the CFO ratios above.
- **Commercial-for-LEASE** → **DSCR**.

CRISIL is explicit that these are assessed separately and only then combined, because *"simple addition of cash flow will not reflect the risks appropriately."* A developer with both must not be run through one blended ratio set.

*(This is why the failure-mode-60 probe clears a report that quotes DSCR or LRD: that report is on the legitimate lease track, not on the wrong track.)*

---

## 3. Business risk — three rules that invert corporate instincts

- **Industry risk has "limited relevance."** Real estate is a **micro-market** business; a national industry view says little about a specific project's demand.
- **Market share is measured IN THE MICRO MARKET**, not nationally.
- **Development track record** is measured in **area developed (sq ft)**, time and cost overruns, and years present in that micro market.
- **Customer advances fund 50–70% of project cost** — which is why collections, not accrual revenue, is the operating metric.
- **Project mix by stage: a steady pipeline across stages is the most favourable.** An early-stage skew carries implementation and funding risk; a near-complete skew gives good near-term cash but forces a launch spike later. Neither extreme is a strength.

---

## 4. LRD — lease rental discounting

```
DSCR = (Lease rentals + CAM + parking - operating expenses - taxes)
       / Scheduled principal and interest
```

- The **average DSCR over the debt tenure** is the primary driver.
- **⚠ Opposite of toll roads:** *"requisite DSCR levels for the INITIAL years can be relatively LOWER than the long-term average."* A toll road is riskiest early; a leased asset is contracted early and riskiest at expiry. Never carry the infrastructure DSCR calibration across.
- **LTV = debt on maturity / market value at maturity** — a key driver for REITs.
- **WALE** is assessed on **two** bases: first (lock-in) expiry and ultimate expiry.
- Escrow + waterfall + DSRA are standard structural expectations.
- **Warehouses** are judged on cubic space, approachability and **built-to-suit** leasing.

---

## 5. CMBS

- Two dates matter: **indicative maturity** (principal repaid, primarily by **refinancing**) and **legal final maturity**. The **tail period** between them sizes the time available to sell the property.
- **Failure to repay by legal final maturity = default.** Failure at indicative maturity is not.
- **DSCR here "primarily represents the INTEREST service coverage ratio"**, since principal is expected to come from refinance rather than from cash flow.
- The developer may **pledge its entire SPV shareholding** so the trustee can sell the SPV rather than the asset itself — faster, and it preserves the asset's contracts.
- **Parent credit risk still matters**: a distressed developer or a liquidator can obstruct the sale, which is why a CMBS is not fully de-linked from its sponsor.

---

## 6. Binding consequences for this project

1. **Never rate a residential/commercial-for-sale developer on accrual interest coverage or ordinary gearing.** Compute CFO (adjusted) and the four ratios in §1.
2. **The Step 12b hard cap on interest coverage is inapplicable to this sector by construction, not by judgement.** Disapplying it (`Inputs!C67 = "N"`) remains correct, but the written reason must say *the sector uses a different ratio set*, and the CFO ratios must then actually appear.
3. **State which track the entity is on** — sale, lease, or both assessed separately.
4. Mechanical enforcement: `check_sections.py` probe *"Real-estate developer assessed on CRISIL's own CFO ratio set (failure mode 60)"*; controls in `tools/test_re_and_globalscale.py`.
