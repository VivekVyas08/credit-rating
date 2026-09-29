# CareEdge methodology corpus — gap against the published site

> ## ✅ CLOSED — 20 August 2026
>
> All four documents were supplied and added. The corpus is now **77/77** against the published site.
> The ratio definitions from #1 and #2 have been extracted into **`CareEdge/CORPORATE_CONVENTIONS.md`**,
> and the default thresholds from #3 are recorded there too. Details below are retained as the record
> of how the gap was found and why it mattered.

**Checked 20-Aug-2026** against <https://www.careratings.com/criteria_methodologies>.
Site lists **77**; `CareEdge/Methodology/` holds **73**. All 73 map to a site entry, so the gap is exactly **4**.

The page is JavaScript-rendered — a plain fetch returns only the shell. It has to be read in a browser.

---

## The 4 missing documents

| # | Title on the site | Category | Download |
|---|---|---|---|
| 1 | **Financial Ratios – Non financial Sector** | General | `https://www.careratings.com/upload/pdf/get-rated/Financial_Ratios_Non_Financial_Sector_March_2025.pdf` |
| 2 | **Liquidity Analysis of Non-financial sector entities** | General | `https://www.careratings.com/upload/pdf/get-rated/Liquidity%20Analysis%20of%20Non-Financial%20Sector%20Entities%20-%20Sept%202024.pdf` |
| 3 | **Policy on Default Recognition** | General | `https://www.careratings.com/upload/pdf/get-rated/Policy%20on%20Default%20Recognition_Jan%202025.pdf` |
| 4 | **Manmade Yarn Manufacturing** | Manufacturing / Trading / Services | `https://www.careratings.com/upload/pdf/get-rated/Criteria_Manmade_Yarn_Manufacturing.pdf` |

All four are **cross-referenced by criteria we already hold** but exist nowhere as files — the signature of a real gap rather than a naming mismatch:

- *Policy on Default Recognition* is cited by the Restructuring, INC and Curing Period papers.
- *Financial Ratios – Non financial Sector* is cited by Auto Dealership, City Gas Distribution and Construction, among 26 documents.
- *Liquidity Analysis of Non-financial sector entities* is cited by Power Distribution, Manufacturing and Real Estate, among 9.
- *Manmade Yarn* is referenced only by the Cotton Textile criteria.

---

## Why #1 and #2 matter more than the count suggests

**#1 — Financial Ratios – Non financial Sector.** This is the *corporate* twin of `Financial Ratios – Financial Sector`, which we do hold. That distinction is not academic: the financial-sector paper is the document whose conventions (tangible net worth, gearing including non-fund-based limits, RONW on average TNW) were got wrong on HDFC Securities, producing 4.20x against a published 4.64x.

**520 of the 631 CareEdge reference reports carrying a Brief Financials table are corporate, PBILDT-based.** So the ratio-definition paper governing the large majority of CareEdge output is precisely the one absent from the corpus. Every corporate rationale to date has been built by inferring PBILDT, overall gearing and interest coverage from peer reports rather than from the definitional source. That has not visibly gone wrong yet, but it is the same exposure, in the larger population.

**#2 — Liquidity Analysis of Non-financial sector entities.** `check_sections.py` already *enforces* that a rationale names a liquidity descriptor — Superior / Strong / Adequate / Stretched / Poor. This is the document that defines what those words mean and what thresholds separate them. The gate demands a descriptor whose definitional source is not held.

#3 is a core policy that three held papers depend on. #4 is narrow — one textile sub-sector — and matters only if a manmade-yarn issuer comes up.

---

## Suggested priority

1. **Financial Ratios – Non financial Sector** — governs most corporate output.
2. **Liquidity Analysis of Non-financial sector entities** — supplies the descriptor thresholds already being enforced.
3. **Policy on Default Recognition** — core policy, three dependants.
4. **Manmade Yarn Manufacturing** — narrow sector, add for completeness.

Convert to `.md` in `CareEdge/Methodology/` in the usual way. Once added the corpus is 77/77 and `preflight` probe [1b] picks them up automatically — no code change needed.


---

## Closure record — 20 August 2026

| # | Document | Added as | Size |
|---|---|---|---|
| 1 | Financial Ratios – Non financial Sector | `Financial_Ratios_Non_Financial_Sector_March_2025.md` | 28,158 b |
| 2 | Liquidity Analysis of Non-financial sector entities | `Liquidity Analysis of Non-Financial Sector Entities - Sept 2024.md` | 10,401 b |
| 3 | Policy on Default Recognition | `Policy on Default Recognition_Jan 2025.md` | 16,970 b |
| 4 | Manmade Yarn Manufacturing | `Criteria_Manmade_Yarn_Manufacturing.md` | 22,596 b |

Each was content-checked, not merely counted — every expected section is present (growth/profitability/leverage/coverage/turnover tables and the hybrid-instrument treatment in #1; all four liquidity descriptors and the unencumbered-cash definition in #2; the facility-by-facility default table and curing periods in #3; the full business-and-financial-risk framework in #4).

### What the documents changed

**A second, DIFFERENT tangible net worth definition.** The corporate TNW is not the financial-sector TNW:

| | Financial-sector (broking) | Corporate (mfg / trading / services) |
|---|---|---|
| Deferred tax assets | **deducted** | not deducted |
| Intangibles | **all deducted** | deducted **except those critical to core operations** — telecom licences, mining surface rights, media rights, IPRs |

Carrying one across to the other is precisely failure mode 32. Both are now documented side by side.

**Confirmation that failure mode 34 generalises.** The Liquidity Analysis criteria states that DSRA balances, margin money, FDs earmarked against a facility, and investments or loans to group entities are all excluded from available liquidity. The "cash is not liquidity until shown to be unencumbered" rule, learned on a broker, is CareEdge's stated position for **every** non-financial entity.

**Two conventions worth flagging because they are easy to get wrong:**
- **GCA excludes right-of-use depreciation** while PAT deducts it — an asymmetry that silently overstates GCA if missed.
- **Overall gearing includes acceptances / creditors on LC**, and Cash DSCR deducts **25% of the increase in working capital**.

### Enforcement change

`check_sections.py`'s net-worth-basis probe (failure mode 32) previously fired only on financial-sector entities. It now covers **all CareEdge reports**, since these documents prove CareEdge uses tangible net worth for corporates too. Measured before enabling: 3 of 14 CareEdge reports quoting gearing do not name their basis — low noise, and each is a genuine omission.
