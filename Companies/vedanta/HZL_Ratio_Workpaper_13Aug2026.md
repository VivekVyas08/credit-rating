# Hindustan Zinc Limited — Ratio & Analytical Workpaper
*(filed under the "Vedanta" case at your direction)*

**Agency: CRISIL | Sector: Materials — Mining / Non-ferrous (zinc-lead-silver) | Basis: CONSOLIDATED | Data cutoff: Q3 FY2025-26 investor presentation; audited base FY2025-26 (AR dated 24-Apr-2026)**

---

## 0. ENTITY IDENTIFICATION (declared — read before using any figure)

The case folder is labelled **"Vedanta"**. Every financial document in it belongs to
**HINDUSTAN ZINC LIMITED** (CIN **L27204RJ1966PLC001208**):

| Document | Entity | Evidence |
|---|---|---|
| Integrated-Annual-Report-2025-26.md | Hindustan Zinc Ltd | CIN L27204RJ1966PLC001208; signed Arun Misra (CEO & WTD), Udaipur; 302 HZL mentions |
| Integrated_Annual_Report_FY_2025 / FY_2024 | Hindustan Zinc Ltd | same CIN |
| 4 × quarterly filings / earnings presentations | Hindustan Zinc Ltd | *"Hindustan Zinc Limited — The World's Largest Integrated Zinc Producer"* |
| Motilal_Oswal...Vedanta.md | Vedanta Ltd (broker note) | 17 Vedanta vs 3 HZL mentions |

**Vedanta Limited and Hindustan Zinc Limited are separate listed legal entities** — Vedanta Ltd
holds **60.71%** of HZL (reduced from 63.42%) and the **Government of India holds 27.92%**. I
raised this and you directed that the report be produced; it is produced **on the entity the
documents actually support**, because the only Vedanta-Limited document present is a broker
note, which under this project's binding data rule is a craft/context reference and never a
data source. Producing "Vedanta Limited" financials from a subsidiary's accounts plus a broker
note would have been fabrication.

**This is not a limitation on the analysis — it is arguably the right lens anyway.** HZL's credit
is *dominated* by the Vedanta relationship (dividend upstreaming, group governance), so Vedanta is
analysed throughout as the **parent-linkage rating factor**, which is where it actually bites.

---

## 1. Document Read Log (Step 1b)

| # | Document | Words | Contribution | Material items |
|---|---|---|---|---|
| 1 | Integrated-Annual-Report-2025-26.md | 225,728 | FY26 audited consolidated BS (L26333) & P&L (L26422); auditor's report; dividends; shareholding | **EMPHASIS OF MATTER — short-seller allegations re Vedanta Resources Ltd + "ongoing matters for which information has been sought by regulators/authorities"** (L26003, Note 43); CoP at 5-yr low US$959/t |
| 2 | Integrated_Annual_Report_FY_2025 | 197,078 | FY24 comparatives (BS L21702, P&L L21777) | FY25 dividend ₹12,253cr = 118% of PAT |
| 3 | Integrated_Annual_Report_FY_2024 | 222,466 | Longer-run context | Scheme of Arrangement (general reserve → retained earnings, effective FY25) with an NCLT undertaking to maintain **minimum net worth of ₹5,000 crore** |
| 4-7 | Q1/Q2/Q3 FY26 earnings presentations + SE-Intimation 24-Apr-2026 | 4.3k-7.6k | Quarterly build; production/cost trends | Cost-of-production trajectory |
| 8 | Motilal_Oswal...Vedanta.md | 5,776 | **Vedanta Ltd** broker note — context only | Not used as a data source (different entity + binding rule) |

**Declared gaps:** no term sheets/sanction letters → rated amount TBC; no bank-limit utilisation
data; no Vedanta-Limited financial statements (see §0).

---

## 2. Computed ratio suite (consolidated, ₹ crore — `compute_ratios.py`)

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Revenue from operations | 28,932 | 34,083 | **40,844** |
| OPBDITA / margin | 13,656 / **47.2%** | 17,388 / **51.0%** | 22,064 / **54.0%** |
| PAT / margin | 7,759 / 26.8% | 10,353 / 30.4% | **13,832 / 33.9%** |
| Total debt (incl. leases) | 8,722 | 10,967 | **8,728** |
| Liquid (cash+bank+current investments) | 10,049 | 9,326 | **13,673** |
| **Net debt / (net cash)** | **(1,327)** net cash | 1,641 net debt | **(4,945) NET CASH** |
| Gearing | 0.57x | 0.82x | **0.39x** |
| TOL/TNW | 1.23x | 1.59x | **0.87x** |
| Total debt/OPBDITA | 0.64x | 0.63x | **0.40x** |
| Net debt/OPBDITA | (0.10x) | +0.09x | **(0.22x)** |
| Interest coverage | 14.3x | 15.9x | **25.0x** |
| RoCE | 42.6% | 56.6% | **58.3%** |
| Current ratio | 1.16x | 1.04x | 1.47x |
| Inventory / Receivable days | 24 / 2 | 20 / 1 | 18 / 4 |
| **Dividend upstreamed** | n/e | **12,253 = 118% of PAT** | 4,225 = 31% of PAT |

**Tie-out (corroboration gate):**
- FY26 balance sheet balances: assets 42,370 = equity 22,629 + liabilities 19,741 ✓
- **FY26 EPS independent cross-check: PAT 13,832 ÷ 4,225mn shares (₹2 face, ₹845cr capital) = ₹32.74 vs reported ₹32.74 — EXACT MATCH** ✓ (independently confirms PAT and share count)
- FY26 equity roll-forward: 13,326 + 13,832 − 229 (OCI) − 4,225 (div) = 22,704 vs reported **22,629** — a **₹75 crore residual (0.3%)**, unexplained by the four movements above and **flagged rather than ignored**. Most likely share-based payment/ESOP or an other-equity transfer; the FY26 statement of changes in equity was not read to line level. Immaterial to every ratio (0.3% of net worth) but recorded per the honest-arithmetic rule.

---

## 3. THE PARENT-LINKAGE ARITHMETIC (what actually drives this rating)

| | FY2025 | FY2026 |
|---|---|---|
| Dividend paid | **₹12,253 cr** | ₹4,225 cr |
| As % of that year's PAT | **118%** | 31% |
| Share to Vedanta Ltd (60.71%) | **₹7,439 cr** | ₹2,565 cr |
| Share to Government of India (27.92%) | ₹3,421 cr | ₹1,180 cr |
| Closing net worth | 13,326 (**down** from 15,195) | **22,629** (rebuilt) |

**Reading.** In FY25 HZL upstreamed **more than its entire year's earnings** — net worth fell
₹1,869 crore — and *still* closed the year with 15.9x interest coverage and total debt/OPBDITA of
0.63x. In FY26 the payout normalised to 31%, net worth rebuilt by ₹9,303 crore and the company
swung to **net cash of ₹4,945 crore**.

**That asymmetry is the core of the rating view:** the extraction risk is real, recurring and
parent-driven — but the underlying cash generation is large enough to absorb a >100%-of-earnings
raid and still leave the balance sheet investment-grade by a wide margin. The 27.92% Government of
India holding, the listed status and SEBI's related-party framework (material RPTs require
majority-of-minority approval) are structural constraints on how far extraction can go.

---

## 4. Business profile (CRISIL Section V — Materials / Mining)

*Routing: the case was created under the generic manufacturing master. HZL is a **mining and
non-ferrous metals** producer, so `criteria-for-manufacturing-trading-and-corporate-services-sector.md`
**Section V (materials sector — mining)** governs the sector factors, with Section I as base
framework and Section IV for ratio definitions. Scope verified: Section V explicitly covers mining
and non-ferrous.*

| Section V factor | Evidence | Assessment |
|---|---|---|
| **Pricing characteristics** | Zinc/lead/silver are LME-linked commodities; HZL is a price-taker | Inherent cyclicality — the principal business risk |
| **Cost position** *(Section V: "a low-cost position is important in an industry where producers have limited pricing flexibility")* | **Cost of production at a 5-year low of US$959/tonne, down 9% YoY**; integrated mine-to-metal | **Exceptional** — first-quartile global cost; the single most important credit strength |
| **Ore reserves / reserve replacement** | Long-life Rampura Agucha and other Rajasthan assets; integrated operations | Strong (detailed R&R tables not extracted) |
| **Production diversification** | Multiple mines; zinc + lead + **silver** by-product | Good — silver credits materially cushion zinc-price downcycles |
| **Regulatory risk** | Mining royalty ₹4,948 cr (FY26) = 12.1% of revenue, a large regulated cost; GoI is both regulator-adjacent and 27.92% shareholder | Moderate |
| **Geographical concentration** | Concentrated in Rajasthan | Moderate concentration risk |
| **Market position** | *"World's Largest Integrated Zinc Producer"* | Dominant |
| **Governance** | **Auditor's EMPHASIS OF MATTER**: short-seller allegations re Vedanta Resources Ltd and subsidiaries, plus *"ongoing matters for which information has been sought by regulators/authorities"* (opinion **not modified**); management assesses allegations as without merit | **The key non-financial risk** — see §5 |

---

## 5. Materiality sweep (Step 8)

| Finding | Decision | Reason |
|---|---|---|
| **Auditor's Emphasis of Matter** — short-seller allegations against VRL and subsidiaries; regulators/authorities have sought information (Note 43) | **Include as a named driver and monitorable** | Passes R13 on the regulatory/governance limb *regardless of quantum*. Opinion is unmodified and management assesses no adjustment required — but an open regulatory enquiry touching the controlling group is precisely a rating-relevant governance item |
| Dividend upstreaming of 118% of PAT (FY25) | **Include — central** | The defining financial-policy risk |
| NCLT undertaking: **maintain minimum net worth of ₹5,000 crore** (Scheme of Arrangement) | Include, one line | A binding floor; current net worth ₹22,629 cr gives 4.5x headroom — a genuine structural protection against extreme extraction |
| Mining royalty ₹4,948 cr = 12.1% of revenue | Include in cost discussion | Large regulated cost line |
| Cash-flow-hedge loss ₹319 cr (OCI, FY26) | Note only | Below the line; hedging is active |
| Exceptional items | Exclude from OPBDITA | +₹25 cr FY26, −₹83 cr FY25 — immaterial, and excluded from operating profit by convention |
| New Labour Codes (notified 21-Nov-2025, effective 01-Apr-2026) | Note as forward cost item | Company has assessed and accounted for incremental impact |
| ₹75 cr equity roll-forward residual | Flag, not resolved | 0.3% of net worth (§2) |

---

## 6. Liquidity (Step 11)

| Sources | ₹ cr | Claims | ₹ cr |
|---|---|---|---|
| Cash + bank | 319 | Current borrowings | 3,638 |
| **Current investments (liquid funds)** | **13,354** | Current lease liabilities | 184 |
| FY26 gross cash accrual (PAT + dep) | 17,622 | Buyers'/suppliers' credit | 105 |
| | | Non-current borrowings (total) | 4,614 |

**Conclusion: Superior.** Liquid assets of ₹13,673 crore exceed **total** debt of ₹8,728 crore —
the company is net cash — and annual cash accrual of ₹17,622 crore is roughly twice total debt.
Even the FY25 stress case (₹12,253 crore of dividends in a single year) left the company able to
service all obligations comfortably. The descriptor is the arithmetic's conclusion, not an
adjective. *(Bank-limit utilisation data is absent, but with liquid assets exceeding total debt the
descriptor does not depend on it — unlike the Creative Newtech case in this project.)*

---

## 7. Rating view (Step 13)

**Standalone assessment.** Best-in-class on essentially every metric: OPBDITA margin **54.0%**
(up from 47.2% two years ago), RoCE **58.3%**, interest coverage **25.0x**, gearing **0.39x**, and
a **net cash position of ₹4,945 crore**. Revenue compounded 18.8% over FY24-26 while the cost of
production fell to a five-year low of US$959/tonne. This is the world's largest integrated zinc
producer operating at first-quartile cost, which means profitability persists deep into a
commodity downcycle — the defining question for any mining credit.

**Constraints.** (i) Commodity price exposure — zinc/lead/silver are LME-linked and HZL is a
price-taker; (ii) **parent linkage** — Vedanta Ltd at 60.71% has demonstrated willingness to
upstream more than 100% of annual earnings, and the wider group carries materially higher leverage
than HZL itself; (iii) **governance** — an unmodified opinion but with an Emphasis of Matter
covering short-seller allegations against the controlling group and open regulatory information
requests.

**Support notching:** **none, in either direction.** Under CRISIL's parent/group linkage criteria a
subsidiary stronger than its parent may be *capped* by group considerations. Here the insulating
factors are unusually strong and specific: a **27.92% Government of India shareholding**, separate
listing, SEBI's majority-of-minority approval requirement for material related-party transactions,
and an **NCLT undertaking to maintain minimum net worth of ₹5,000 crore**. HZL is rated on its own
standalone profile; no uplift is available (none is needed) and no cap is applied.

**Independent view: CRISIL AAA / Stable.**

**The AAA vs AA+ judgment call, stated openly.** AA+ is defensible if one weights the parent drag
more heavily — a controlling shareholder that took 118% of earnings in one year, and an EOM
touching group governance, are not trivial. I have settled on **AAA** because the standalone
financial profile is not merely strong but *shock-absorbing*: HZL sustained that 118% extraction
and still closed FY25 with 15.9x coverage and 0.63x debt/OPBDITA, then rebuilt to net cash within
twelve months. A rating is an opinion on ability to service debt, and on the evidence this balance
sheet services its debt through both commodity downcycles and aggressive parent extraction. **The
factor that would change this view is not zinc prices — it is a structural escalation in
extraction** (e.g. large debt-funded special dividends or intercompany exposure to the parent), or
an adverse regulatory finding from the matters flagged in the Emphasis of Matter.

**Step 14 divergence:** no prior CRISIL action for HZL was found in the reference library, and the
supplied documents contain no credit-rating note. The view is formed with **no anchor exposure**,
and equally with no external benchmark.

---

## 8. Disclosed scoping decisions (Rule 1)

1. **Entity**: rated HZL, the entity the documents support; Vedanta analysed as parent-linkage factor (§0).
2. **Routing corrected** to Section V (materials/mining) from the generic manufacturing master (§4).
3. **Rated amount TBC** — no term sheets and no credit-rating note in the supplied documents.
4. **₹75 cr equity residual flagged, not resolved** (§2).
5. **FY24 dividend not extracted** — shown as n/e, not estimated.
6. **5-year model and scorecard anchor (Steps 12/12b) not built.** For a commodity producer the
   forecast turns on LME zinc/silver price decks, which are absent from the document set (the only
   broker note is for a different entity). A model built on an invented price deck would be false
   precision. **Offered as the next step if you supply a price assumption.**
7. **Peer reports not read for this sector** — the CRISIL peers read earlier in this session are
   auto-component manufacturers; mining-sector calibration does not transfer. Limitation on peer
   benchmarking strength.

---

*Every figure computed in `compute_ratios.py` from Hindustan Zinc Limited's audited consolidated
statements or traced to a document location. No CRA-published amount used as data.*

---

## STEP 12 / 12b — FORWARD VIEW AND SCORECARD ANCHOR (added 01-Sep-2026)

**Anchor grade: Crisil AA/Stable / Crisil A1+.** Rating in the rationale: **Crisil AAA/Stable**.
The divergence is **two notches**, inside the calibrated ±2 screening band.

**Why the view sits above the anchor.** The scorecard is fed the Metals & Mining sector base of
4 — correctly, because zinc is a cyclical single commodity — and that industry score is the
single largest drag on the composite. What it cannot see is that Hindustan Zinc occupies the
position within that cycle that the sector score is designed to penalise the ABSENCE of: a zinc
cost of production excluding royalty of **US$ 959 per tonne**, a five-year low and a genuine
first-quartile global position, on 13.9 Mnt of reserves and 50 Mnt of resources. A first-quartile
producer and a fourth-quartile producer in the same commodity carry the same sector score and do
not carry the same credit risk. The balance sheet says the same thing: **net CASH of Rs 4,945
crore**, with Rs 17,008 crore of operating cash flow against Rs 8,728 crore of total debt
including leases.

**Support notches: 0 — and on this issuer that is the FAVOURABLE entry, not the neutral one.**
The support cell exists to notch a subsidiary UP towards a stronger parent. Vedanta Limited is
not stronger. Its call on this balance sheet runs through the DIVIDEND, and the evidence is
Rs 12,253 crore paid in FY2025 against Rs 4,225 crore in FY2026 — a 66% swing in one year with
no stated distribution policy. The honest scorecard entry would be a negative notch; zero is used
because the drag is modelled where it actually bites, in the stress case, and recording it in
both places would double-count it.

### The arithmetic that decides this credit

The company published both sides of its own funding equation over exactly this window:

| | Company's stated figure |
|---|---|
| Capex, five years | Rs 40,000 – 50,000 crore (1.1 → 2.0 Mtpa refined capacity) |
| Pre-growth-capex FCF, five years | Rs 55,000 – 65,000 crore |
| **Headroom on the midpoints** | **Rs 15,000 crore, i.e. Rs 3,000 crore a year** |
| Dividend actually paid, FY2025 | **Rs 12,253 crore** |

**The capex is comfortably fundable. The dividend is what decides whether the company ends the
window in net cash or net debt.**

| | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---|---|---|---|---|
| Net debt / (cash), base | — | — | — | — | **(25,704)** |
| Net debt, stress | — | — | — | — | **34,506** |

The stress combines an 18% realisation fall with an 8% cost increase **and** a dividend held near
the FY2025 rate — because on this issuer those are correlated, not independent. It also caps the
dividend at distributable reserves, which surfaces a finding the uncapped arithmetic hid:
**Rs 7,055 crore of the stress-case distribution is not legally payable**. That is the point at
which the parent's claim on cash stops being satisfiable, and it is a genuine protection for
creditors rather than a modelling artefact.

### Governance

The FY2026 consolidated audit report carries an **Emphasis of Matter** drawing attention to
Note 43, *"regarding allegations made during the year by a short seller, and ongoing matters for
which information has been sought by regulators/authorities"*. The opinion itself is unmodified
and the disclosure is full, but this is an unresolved overhang at the reporting date and the
management score of **3** reflects it rather than scoring it as absent.

### The monitorable

**The dividend, not the debt and not the zinc price.** Capex is fundable from the company's own
published FCF estimate; the balance sheet is net cash; the cost position is first-quartile. What
would change this credit is a sustained return to FY2025-scale distributions while the Rs 45,000
crore programme is being spent.

*Twelve opening-balance tie-outs reconcile in `forward_model.py`. One disclosed difference: the
company states FY2026 EBITDA of Rs 22,162 crore against the Rs 22,064 crore computed here and
published in the rationale — a Rs 98 crore gap being other income the company treats as operating
and the strict convention strips. The margin is 54% on either basis.*
