# Creative Newtech Limited — Ratio & Analytical Workpaper
**Agency: CRISIL | Business: technology-products DISTRIBUTION (+ emerging brand licensing) | Basis: CONSOLIDATED | Data cutoff: Q1 FY2026-27 (30-Jun-2026); audited base FY2025-26**

---

## 0. ROUTING CORRECTION (Step 2 — failure mode 4, scope-mismatched methodology)

**The case was created under "Corporate — Manufacturing & Services (master criteria)". That is the
wrong primary scope and has been corrected.**

Evidence the entity is a **trader/distributor**, not a manufacturer:
- **Purchases of stock-in-trade = ₹2,552.28cr on revenue of ₹2,699.77cr — 94.5% of revenue** (FY26 audited).
- Revenue is disclosed entirely as **"Sale of Products — Traded Goods"** (Note 23, FY24-25 AR).
- The AR states: *"We transitioned from being a **volume-led distributor** to a high-margin, brand-first enabler"* and *"stepped decisively beyond the traditional boundaries of distribution"*.
- Gross margin 7.9% (FY26) / 8.4% (FY25) — distribution economics, not manufacturing.

**Correct routing:** CRISIL `criteria-for-manufacturing-trading-and-corporate-services-sector.md`
**Section II — methodology for trading companies** governs the ratio emphasis and the business-risk
factor set, with **Section I** as the base framework and **Section IV** for generic ratio definitions.

**Scope caveat, declared:** Section II states it *"has limited applicability for entities that also have
significant manufacturing operations."* CNL has a brand-licensing/contract-manufacturing arm (the AR lists
"Brand Licensing and Contract Manufacturing" among its businesses). That arm is **not separately quantified
in any document supplied**, so I cannot size it — on the 94.5%-purchases evidence it is clearly not yet
"significant" relative to distribution, but this is stated as a limitation rather than assumed away.

Section II's named ratio set is therefore computed **in addition to** the generic suite: RoCE · interest
coverage · **total indebtedness ratio** · **cash-to-indebtedness ratio** · **risk coverage** · current ratio
· GCA days.

---

## 1. Document Read Log (Step 1b)

| # | Document | Words | What it is | Key contribution | Material items |
|---|---|---|---|---|---|
| 1 | OutcomeBM14052026-1.md | 7,412 | Board outcome 14-May-2026 — **AUDITED FY26 results**, standalone + consolidated, unmodified opinion | **The FY26 audited base**: consolidated BS (L538+) and P&L (L606+), with FY25 audited comparatives | The FY25→FY26 leverage move; **CFO change** — Abhijit Kanvinde resigned 14-Apr-2026, Ajit Thakur appointed 14-May-2026 |
| 2 | Annual-Report-FY24-25.md | 81,227 | Audited AR FY25 (+FY24 comp.) | FY24 consolidated BS (L6356+); segment note (Note 23) giving revenue by segment and **by geography**; FY24/FY25 PBT and finance cost | Business-model evidence (distributor→brand transition); **majority-export revenue mix** |
| 3 | Annual-Report-2024.md | 77,514 | Audited AR FY24 | FY24 confirmatory base | — |
| 4 | 1-Annual-Report-2023.md | 68,020 | Audited AR FY23 | Longer-run context | — |
| 5 | Financial-Results-Q1-FY27.md | 4,371 | Q1 FY27 results — **DATA CUTOFF** | Consolidated revenue ₹476.07cr (+21.2% YoY); finance costs ₹7.63cr (**+153% YoY**) | Interest burden compounding faster than revenue |
| 6 | Financial-Results-Q3-FY26.md | 3,195 | Q3 FY26 results | Quarterly build within FY26 | — |
| 7 | Financial-Results-Q2-H1-FY26.md | 5,381 | Q2/H1 FY26 results | Quarterly build | — |
| 8 | OutcomeBM06082025.md | 3,670 | Board outcome 06-Aug-2025 (Q1 FY26) | Q1 FY26 comparative base | — |

**Declared gaps (Step 1):**
- **No FY2025-26 ANNUAL REPORT.** FY26 financials come from the audited results filing, which carries the
  statements but **not the notes** — so FY26 contingent liabilities, related-party transactions, borrowing
  terms/security, and the credit-rating note are **unavailable**. This is a material information gap and is
  reflected in the rating conclusion.
- **No sector-assumptions / broker note** — unlike the other cases in this project, there is **no external
  forward view of any kind**. All forward statements below are my own, labelled as such.
- **No term sheets / sanction letters** → rated amount is "to be confirmed by issuer".
- **No bank-limit utilisation data** — CRISIL's own named liquidity test for non-financial entities.

---

## 2. Computed ratio suite (consolidated, ₹ crore — `compute_ratios.py`)

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Revenue | 1,713.1 | 1,774.5 | **2,699.8** |
| Gross margin | n/a | 8.38% | **7.91%** |
| OPBDITA / margin | n/a¹ | 54.7 / 3.08% | **91.1 / 3.37%** |
| PAT (total / owners) | n/a¹ | 53.1 / 46.2 | 70.3 / 61.8 |
| **Total debt** | 73.6 | 71.8 | **324.3** |
| Gearing (debt/TNW) | 0.33x | 0.23x | **0.84x** |
| **TOL/TNW (total indebtedness)** | 0.61x | 0.72x | **1.42x** |
| **Cash-to-indebtedness** | n/a¹ | 0.248x | **0.040x** |
| Interest coverage | 7.03x² | 5.38x | **4.41x** |
| Total debt/OPBDITA | n/a¹ | 1.31x | **3.56x** |
| Net debt/OPBDITA | n/a¹ | 0.30x | **3.32x** |
| RoCE | n/a¹ | 14.0% | **12.6%** |
| NCATD | n/a¹ | 0.76x | **0.22x** |
| Current ratio | 2.73x | 2.36x | **1.68x** |
| GCA days | 75 | 107 | **125** |
| Receivable / Inventory days | 31 / 17 | 49 / 22 | **76 / 23** |
| **Risk coverage** @20% loss on recv+inv | 5.0x cover | 4.5x cover | **2.6x cover** (38% of networth) |

¹ FY24 depreciation and other income were not extracted (FY24 P&L detail not pulled) — OPBDITA-based ratios
are marked **n/a with reason** rather than estimated. ² FY24 coverage is a **PBT-based proxy**
((PBT+interest)/interest), explicitly labelled and **not comparable** to the FY25/FY26 OPBDITA-based figures.

**Tie-out (corroboration gate — all PASS):** FY26 PBT computed 8,176.00 lacs vs filing **8,176.20** ✓;
FY26 PAT 7,029.00 vs **7,029.29** ✓; FY26 balance sheet balances (assets = equity + liabilities) ✓; and a
genuine **cross-source** check — FY25 PBT of **6,154.50** in the audited filing matches **6,154.51** in the
FY24-25 AR's segment note, two independent documents ✓.

---

## 3. The FY25 → FY26 move (this is the credit story)

| | FY2025 | FY2026 | Change |
|---|---|---|---|
| Revenue | 1,774.5 | 2,699.8 | **+52.1%** |
| Total debt | 71.8 | 324.3 | **+351.6% (4.5×)** |
| Trade receivables | 237.8 | 565.1 | **+137.7%** — 2.6× the revenue growth rate |
| Cash + bank | 55.2 | 22.2 | **−59.8%** (cash alone 43.9 → **5.4**) |
| Finance cost | 10.2 | 20.7 | **+103.5%** |

**Reading:** the company funded a 52% revenue expansion almost entirely with short-term debt and supplier
credit while receivables grew nearly three times as fast as sales. Receivable days rose 31 → 49 → **76**
across three years. That is either a deliberate purchase of growth through extended channel credit, or a
collection deterioration — **the documents do not distinguish between the two**, and there is no ageing
schedule, no customer-concentration disclosure, and no management commentary explaining it in the
supplied set. Either way it has consumed the balance sheet's liquidity: cash-to-indebtedness fell from
0.248x to **0.040x**.

**Q1 FY2027 (cutoff):** revenue ₹476.07cr, **+21.2% YoY** — growth continues, but finance costs of
₹7.63cr are **+153% YoY** and annualise near ₹30.5cr against FY26's ₹20.7cr. The interest burden is
compounding faster than the revenue it funds.

---

## 4. Business profile (Section II factor set)

| Section II factor | Evidence | Assessment |
|---|---|---|
| **Industry risk** | Technology-product distribution — thin structural margins, brand-owner dependent, obsolescence-prone categories | **Moderate-to-high** |
| **Business size & sustainability** | ₹2,700cr revenue, 20+ year record, distributor for OM SYSTEM (Olympus carve-out), Honeywell (licensed), others; active distributors across South Asia, SE Asia, Middle East, Africa | **Adequate** — real scale and franchise |
| **Inventory risk** | Inventory 23 days, ₹173.4cr; consumer-tech categories carry genuine obsolescence risk | **Moderate** — short holding is a mitigant |
| **Receivables risk** | ₹565.1cr = **76 days and 1.46× networth**; no ageing or concentration disclosed | **HIGH — the dominant risk** |
| **Supplier risk** | Dependent on principals' brand mandates; distribution agreements terminable (terms not disclosed) | Moderate; **contract terms not available** |
| **Forex risk** | **Majority of revenue is outside India** (FY25: ₹1,096cr vs ₹678cr domestic = 61.5% export). No hedging policy found in the supplied documents | **Material and UNQUANTIFIED** — a real gap |
| **Risk coverage** (Section II's shock test) | Networth ₹387.3cr vs receivables+inventory ₹738.6cr. A 20% loss = **38% of networth**, cover only **2.6×** (was 5.0× in FY24) | **Weakened materially** |
| **Management** | 20+ year promoter-led record; profitable growth; **but** CFO turnover (resigned Apr-2026, successor May-2026) amid a 4.5× debt increase | Neutral, with a governance-continuity watch item |

**Segment & geography (FY25, latest disclosed — FY26 split unavailable, no FY26 AR):**
Enterprise Business ₹1,205.95cr (68%) · Fast Moving Social/Media Gadgets ₹385.36cr (22%) ·
Fast Moving Consumer Tech ₹182.04cr (10%) · Fast Moving Electronics ₹1.12cr.
Geography: **Outside India ₹1,096.07cr (61.5%)** · India ₹678.41cr (38.5%).

---

## 5. Liquidity (Step 11) — sources vs claims

| Sources | ₹ cr | Claims | ₹ cr |
|---|---|---|---|
| Cash + bank balances (31-Mar-2026) | 22.2 | Short-term borrowings (revolving) | **324.3** |
| FY26 gross cash accrual (PAT + dep) | 71.8 | Trade payables | 185.1 |
| Undrawn bank limits | **Not disclosed — TBC** | Non-current debt repayment | 0.01 |

**Conclusion: Stretched-to-Adequate.** Cash of ₹22.2cr covers under 7% of ₹324.3cr of short-term debt, and
gross cash accrual of ₹71.8cr is 0.22× total debt (NCATD). The position depends **entirely** on the
continued rollover of working-capital lines and on receivables converting to cash on schedule — neither of
which can be verified from the supplied documents, because **bank-limit sanction and utilisation data are
absent**. Current ratio of 1.68x and receivables of ₹565.1cr against short-term debt of ₹324.3cr provide
asset cover on paper; the question the documents cannot answer is collection quality. **The descriptor is
deliberately not upgraded to "Strong" or "Adequate" without utilisation data — it is the arithmetic's
honest conclusion, and the arithmetic has a hole in it.**

---

## 6. Rating view (Step 13)

**Standalone assessment.** Creative Newtech is a genuine, profitable, growing technology-products
distributor with two decades of operating history, real principal relationships and ₹2,700cr of revenue.
Revenue grew 52% and PAT 32% in FY26; RoCE at 12.6% remains above cost of capital.

Against that, every credit metric that matters moved the wrong way in a single year: gearing 0.23x →
**0.84x**, total indebtedness 0.72x → **1.42x**, interest coverage 5.38x → **4.41x**, total debt/OPBDITA
1.31x → **3.56x**, cash-to-indebtedness 0.248x → **0.040x**, risk coverage 4.5× → **2.6×**. The business
carries a **3.37% EBITDA margin**, so it has very little absorptive capacity: a 100bps gross-margin slip on
FY26 revenue is roughly ₹27cr, or **30% of EBITDA**. Combined with 61.5% unhedged-so-far export exposure and
receivables at 1.46× networth, the downside tail is meaningfully fatter than the headline growth suggests.

This is not a distressed profile — coverage above 4x and gearing below 1x are adequate, and the company is
comfortably profitable. But it is a **moderate** credit whose safety margin narrowed sharply in one year.

**Support notching:** none — no parent; NCI relates to operating subsidiaries.
**Instrument adjustments:** none — plain bank facilities.
**LT/ST mapping** (CRISIL Basics of Ratings, Table 1, corporates): BBB+ → **A2**.

**Independent view: Crisil BBB+ / Stable · Crisil A2.**

Outlook Stable, not Negative: the leverage build funded real, profitable revenue growth rather than losses,
the company remains solidly profitable, and short-term debt is asset-backed by receivables and inventory of
₹738.6cr against ₹324.3cr of debt. Outlook would move to Negative on any of: receivable days extending
beyond ~90, interest coverage falling below 3.5x, or a material bad-debt or forex loss.

**The BBB+ vs A− judgment call, stated openly.** A− is defensible on scale, growth and a still-sub-1x
gearing. I have settled one notch lower because of four *unverifiable* items rather than four bad numbers:
(i) no bank-limit utilisation data; (ii) no receivables ageing or customer concentration; (iii) no forex
hedging policy against 61.5% export revenue; (iv) **no FY26 annual report**, hence no FY26 contingent
liabilities or related-party disclosure. With a working-capital-funded distributor, those four are precisely
the disclosures that determine whether 76-day receivables are healthy growth or an early warning. **Supply
them and this could reasonably move to A−.**

**Step 14 divergence:** no prior rating action for this entity was found in the CRISIL reference library,
and the supplied documents contain **no credit-rating note** (the FY26 AR, which would carry it, was not
uploaded). The view above is therefore formed with **no anchor exposure at all** — the cleanest independence
position of the cases run in this project — but equally with **no external benchmark** to check it against.

---

## 7. Disclosed scoping decisions (Rule 1)

1. **Routing corrected from manufacturing to trading (Section II)** — §0, with the manufacturing-arm scope
   caveat declared rather than assumed away.
2. **Rated amount not stated** — no credit-rating note in the supplied documents and no sanction letters;
   marked "to be confirmed by issuer", not reconstructed.
3. **FY24 OPBDITA-based ratios marked n/a**, and FY24 coverage shown only as a clearly-labelled PBT proxy —
   not estimated to fill the row.
4. **FY26 segment/geography split unavailable** (no FY26 AR) — FY25 split shown and dated, not rolled forward.
5. **5-year model and scorecard anchor (Steps 12/12b) — BUILT 01-Sep-2026. This entry previously read
   "not built in this pass ... offered as the next step", and that framing was itself the defect** (failure
   mode 35: a disclosed gap reads as a considered decision and therefore survives). The reasoning given —
   that a forecast without receivables ageing would be false precision — had it backwards: receivable
   BEHAVIOUR is precisely what the model needed to flex, and days are computable from the audited balance
   sheet without an ageing schedule. `forward_model.py` now projects FY2027-FY2031 with the debt path
   DERIVED from the working-capital funding gap, and `fill_scorecard.py` fills the Step 12b anchor. What
   remains genuinely unavailable is bank-limit utilisation data, which affects the liquidity descriptor's
   precision, not the projection.
6. **Peer reference reports not read for this sector** — the CRISIL reference library was searched, but the
   peers read earlier in this session (Ramkrishna Forgings, Craftsman Automation) are auto-component
   manufacturers. House-style transfers; **trading-sector calibration does not**, and this weakens the peer
   benchmarking behind the BBB+/A− call. Stated as a limitation.

---

*Data cutoff: Q1 FY2026-27 (30-Jun-2026); audited base FY2025-26 (audited results filing, unmodified
opinion). Every figure computed in `compute_ratios.py` from audited consolidated statements or traced to a
document location. No CRA-published amount used as data.*


---

## STEP 12b — SCORECARD ANCHOR (added 01-Sep-2026)

**Anchor grade: Crisil BBB-/Stable / Crisil A3.** Proposed rating in the rationale: **Crisil BBB+/Stable**.
The divergence is **two notches**, which is INSIDE the anchor's calibrated ±2 screening band, so it is a
flag to explain rather than a committee escalation (the escalation rule bites beyond ±2, or at any distance
for AA+/AAA and BB-and-below).

**What the anchor cannot see, and why the view sits above it.** The adjusted composite is 4.34, driven down
by the FY2026 balance sheet: gearing 0.84x, total debt/OPBDITA 3.56x, interest coverage 4.41x and a
NEGATIVE operating cash flow of Rs 273.10 crore. Every one of those is a *point-in-time* consequence of a
single year in which revenue grew 52.1% and the receivable book grew 137.7%. The scorecard reads the
resulting leverage as a standing condition. The forward model, working from the same audited figures, shows
it is not: hold receivable days flat at the FY2026 level of 76 — assume no improvement whatever — and the
funding gap still turns NEGATIVE in FY2029, debt peaks at Rs 359 crore in FY2028 and falls to Rs 228 crore
by FY2031, with total debt/OPBDITA at 1.19x and gearing at 0.28x. The leverage is growth-funding, not
structural, and it self-liquidates as growth tapers.

**Support notches: 0.** No parent, no group. Entered as zero so the anchor stays honestly standalone.

**Qualitative scores.** Industry: no override — the Trading / Distribution sector base of 4 is used, which
is the correct scope (the case was created under a manufacturing master and re-routed to CRISIL's trading
criteria, Section II). Business risk **4** — a thin-spread intermediary on other people's brands (gross
margin 7.91%, purchases 94.5% of revenue), offset by genuine segment diversification and the
brand-licensing route to a better margin. Management **4** — unmodified audit opinion, but receivable days
went 49 to 76 in one year, and the FY2026 consolidated cash-flow statement carries a depreciation figure
(30.43 lakh) that does not reconcile to its own P&L (152.10 lakh). Liquidity **Stretched** — the descriptor
is the conclusion of the sources-and-claims arithmetic recorded in `fill_scorecard.py`, not an adjective:
the whole Rs 324.25 crore of debt is current, cash is Rs 5.36 crore, other bank balances of Rs 16.82 crore
include margin money and are not shown to be unencumbered, and FY2026 operating cash flow was negative
Rs 273.10 crore.

**The single monitorable this produces:** receivable days. At 76 days the credit self-funds by FY2029; the
stress case holds growth constant and stretches them to 92, and debt then rises every year to Rs 804 crore
with coverage compressing to 1.62x and gearing to 1.45x. For a distributor on short-term working-capital
lines the risk is not that sales fall — it is that sales are made and not collected.
