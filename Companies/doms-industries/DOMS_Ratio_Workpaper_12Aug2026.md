# DOMS Industries Limited — Ratio & Analytical Workpaper
**Agency: CRISIL | Sector: Corporate — Manufacturing (Consumer Discretionary / Stationery) | Basis: CONSOLIDATED | Data cutoff: Q1 FY2026-27 (30-Jun-2026); audited base FY2025-26**

---

## 0. DECLARED ANCHOR EXPOSURE (independence, R7 — declare + mitigate)

**I knew the outstanding CRISIL rating before forming my view, and could not avoid it.** The FY26 Annual
Report — mandatory reading under Step 1b/7b — states in two places that CRISIL upgraded the company's bank
facilities to **CRISIL AA-/Stable** during FY2025-26. This is the "issuer document encloses the CRA action"
situation logged in the HLE Glascoat lesson. **Mitigation applied:** the analytical view below was built
from the computed ratio suite, the CRISIL methodology factors and peer calibration, and the reasoning chain
is written out so it can be audited for reverse-engineering. Where my assessment would have differed, it is
stated. No CRA-published figure has been used as data anywhere in the deliverable.

**⚠ Corroboration flag — the AR contradicts itself on the prior rating:**
- L1854: *"upgraded from 'CRISIL A+/**Positive**' to 'CRISIL AA-/Stable'"*
- L4790: *"upgraded ... from 'CRISIL A+/**Stable**' to 'CRISIL AA-/Stable'"*

Same document, same event, two different prior outlooks. Neither is adopted; the rating-history line is
marked **to be confirmed by issuer**. (Flagged rather than silently resolved, per failure mode 15.)

**⚠ Corroboration flag — promoter holding disagrees across sources:**
- AR, as at 31-Mar-2026: **70.39%** (Promoter & Promoter Group, L4706)
- PL Capital, Aug-2026: **63.39%**

A ~7pp gap. Plausibly a genuine post-year-end sell-down or a different definition of "promoter group"
(FILA's 26.01% is inside the AR's promoter group). **Not resolved from the documents** — flagged, and no
shareholding-dependent conclusion is drawn.

---

## 1. Document Read Log (Step 1b)

| # | Document | Words | What it is | Key contribution | Material items |
|---|---|---|---|---|---|
| 1 | DIL_Annual_Report_FY_2025-26.md | 123,521 | Audited AR FY26 (+FY25 comp.), standalone & consolidated | Consolidated BS (L11253) & P&L (L11360); Note 36-37 contingent liabilities/commitments; Note 41 segments; Note 18/21 borrowings; auditor report + KAM (L6886-6920); credit-rating note (L1854, L4790); promoter holding (L4706, L8581) | Reynolds brand acquisition (Jun-2026, post-BS); 6 subsidiaries incl. stake changes; FILA 26.01%; the two corroboration flags above |
| 2 | DIL_Annual_Report_FY_2024-25.md | 118,999 | Audited AR FY25 (+FY24 comp.) | FY24 consolidated BS/P&L for the 3-year trend | Pioneer stake 51%→64% commitment (₹11.08cr, FY25) |
| 3 | DIL_Annual_Report_FY_2023-24.md | 110,998 | Audited AR FY24 (+FY23 comp.) | Confirmatory FY23/FY24 base; IPO year (listed 20-Dec-2023) | IPO proceeds ₹332.72cr, since fully utilised |
| 4 | Result_Release_Q1FY2027.md | 2,040 | Q1 FY27 results — **DATA CUTOFF** | Standalone + consolidated Q1 P&L; IPO utilisation note | **The dominant finding: revenue +19.2% but PAT −23.4% YoY; EBITDA margin −529bps** |
| 5 | Result_Release_Q4FY2026.md | 3,927 | Q4 & FY26 results | FY26 quarterly build; segment detail | Q4 margin already softening ahead of Q1FY27 |
| 6-8 | Result_Release_Q3/Q2/Q1FY2026.md | 2,541 / 3,371 / 2,168 | Quarterly results FY26 | Quarterly trend, cross-checked against AR full-year totals | — |
| 9 | PL_Capital...DOMS_Industries.md | 3,251 | Broker note, 04-Aug-2026, BUY, TP ₹2,703 | Independent corroboration of Q1FY27 margin collapse; FY27E/FY28E estimates; segment EBITDA margins | *"Prioritizing market share over margins in turbulent times"*; EPS cut 13%/5%; RM inflation named as cause |

---

## 2. Computed ratio suite (consolidated, Rs crore — `compute_ratios.py`)

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Revenue | 1,537.1 | 1,912.6 | 2,326.4 |
| OPBDITA / margin | 272.7 / **17.7%** | 348.4 / **18.2%** | 402.6 / **17.3%** |
| PAT (total / owners) | 159.7 / 153.1 | 213.5 / 202.3 | 239.6 / 230.2 |
| Total debt (incl. leases) | 171.9 | 211.8 | **141.3** |
| Cash + bank deposits | 305.9 | 225.4 | **61.8** |
| Net debt | **(134.0)** net cash | **(13.6)** net cash | **79.5** net debt |
| Gearing (debt/TNW) | 0.20x | 0.20x | **0.11x** |
| TOL/TNW | 0.41x | 0.40x | **0.31x** |
| Total debt/OPBDITA | 0.63x | 0.61x | **0.35x** |
| Net debt/OPBDITA | (0.49x) | (0.04x) | **0.20x** |
| Interest coverage | 15.9x | 23.2x | **37.3x** |
| NCATD | 1.23x | 1.33x | 2.32x |
| Current ratio | 2.97x | 2.68x | 2.17x |
| RoCE | 21.8% | 21.6% | **21.8%** |
| Inventory / Receivable days | 53 / 15 | 56 / 26 | 59 / 26 |
| Segment mix (Stationery/Hygiene) | n/d | 94.1% / 5.9% | **91.3% / 8.7%** |

**Tie-out (corroboration gate — all five PASS):** FY26 EBITDA computed 40,259.00 lakhs vs company-disclosed
**40,259.62** ✓; revenue 2,32,637 vs **2,32,636.52** ✓; PAT 23,956 vs **23,956.25** ✓; margin 17.3% vs
company-stated **17.3%** ✓; segment revenue sums to the total after inter-segment elimination ✓.

**Basis note:** RoCE computed as EBIT/(debt + total equity), excluding deferred tax liability (₹10-11 crore,
under 1% of capital employed) — basis stated rather than silently varied from the CRISIL formula.

---

## 3. Q1 FY2027 — the live development (data cutoff)

| | Q1 FY27 | Q1 FY26 | Change |
|---|---|---|---|
| Revenue (consolidated) | 670.5 | 562.3 | **+19.2%** |
| PAT (consolidated) | 45.3 | 59.1 | **−23.4%** |
| EBITDA margin (standalone, computed) | 12.1% | 17.4% | **−529bps** |
| Materials cost / revenue (standalone) | 64.3% | 60.1% | +420bps |

**Independently corroborated:** PL Capital (04-Aug-2026) computes consolidated EBITDA margin **−525bps to
12.3%** and gross margin **−400bps to 38.2%**, attributing both to *"sharp RM inflation"* — within 4bps of
my independently computed standalone figure. Segment EBITDA margins at Q1FY27 per the same note:
Stationery **13.4%**, Hygiene **6.7%** — confirming the hygiene mix shift is structurally dilutive.

---

## 4. Multi-year TREND extraction (not snapshots — new binding requirement)

| Trend | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | Direction |
|---|---|---|---|---|---|---|
| Revenue (₹ cr) | ~750* | ~1,150* | 1,537 | 1,913 | 2,326 | **+23% CAGR FY24-26** |
| EBITDA (₹ cr) | 69.7 | 186.7 | 272.7 | 348.4 | 402.6 | rising in absolute terms |
| EBITDA margin | ~9.3%* | ~16.2%* | 17.7% | 18.2% | **17.3%** | **peaked FY25, now falling** |
| PAT (₹ cr) | 17.1 | 102.9 | 159.7 | 213.5 | 239.6 | rising, decelerating |
| Hygiene share of revenue | — | — | n/d | 5.9% | **8.7%** | **rising — margin-dilutive** |
| Net debt | — | — | (134.0) | (13.6) | **79.5** | **net cash → net debt** |
| Cash + deposits (₹ cr) | — | — | 305.9 | 225.4 | **61.8** | **−80% over two years** |

\* FY22/FY23 EBITDA and PAT are from the AR's own five-year chart (corroborated: the chart's FY25 EBITDA
34,845 and PAT 21,354 lakhs match the audited statements exactly, so the series is reliable); the FY22/FY23
revenue figures are back-derived from the disclosed margins and are marked approximate.

**Two trends matter more than any single-year figure:**
1. **Margin has turned.** 17.7% → 18.2% → 17.3% → **12.1-12.3% (Q1FY27)**. The FY26 dip was mix (Uniclan);
   the Q1FY27 collapse is raw-material inflation the company has chosen not to fully pass through.
2. **The liquidity buffer has been spent.** Cash and deposits fell ₹305.9cr → ₹61.8cr across two years,
   funding capex (CWIP up to ₹162.1cr) and acquisitions — moving the group from net cash to net debt. The
   balance sheet is still very strong, but the *cushion* is materially thinner than the ratios alone imply.

---

## 5. Group structure & entities (every entity NAMED — binding, regardless of materiality)

| Entity | Holding | Business | Note |
|---|---|---|---|
| **DOMS Industries Limited** | — | Stationery & art materials | Rated parent; CIN L36991GJ2006PLC049275 |
| **Uniclan Healthcare Private Limited** | 75% | Baby hygiene (diapers, wet wipes) | **Material** — FY26 revenue ₹203.1cr (8.7% of group); 3rd diaper line commissioned; EBITDA margin 6.7% (dilutive) |
| **Pioneer Stationery Private Limited** | 51% → **64%** (raised in FY26) | Paper stationery | Stake increase completed; ₹11.08cr commitment in FY25 |
| **Micro Wood Private Limited** | 51.77% | Packaging | — |
| **Skido Industries Private Limited** | 51% | School bags | — |
| **Super Treads Private Limited** | acquired 01-Jun-2025 | Paper stationery (Siliguri, West Bengal) | Eastern-market proximity |
| **Clapjoy Innovations Private Limited** | 30% | Toys | **Associate** (equity method, ₹1.50cr carrying value) — not consolidated |

**F.I.L.A. — Fabbrica Italiana Lapis ed Affini S.p.A. holds 26.01%** and is inside the AR's Promoter &
Promoter Group. A Shareholders Agreement with FILA was executed 07-May-2025. FILA is also a **customer**
(exports to FILA Group = 7.3% of revenue per the AR's channel chart). Two FILA executives sit on the board
as Non-Executive Directors.

**Parent-support notching decision: NIL uplift applied.** CRISIL's parent/group linkage criteria require
assessing economic incentive, control and stated posture. FILA holds a **26.01% minority** — not control —
and no support undertaking, guarantee or keepwell is disclosed in any document reviewed. The relationship is
strategic-commercial (distribution/export offtake), not a support obligation. **Standalone credit profile
carries the rating; no notch is taken for FILA.** *(Conversely, no drag is applied either — FILA's own credit
profile is not in the document set and is not assumed.)*

---

## 6. Materiality sweep (Step 8)

| Finding | Quantum | Decision | Reason |
|---|---|---|---|
| **Reynolds brand acquisition** (Asset Purchase Agreement, **June 2026** — post-BS, pre-cutoff) | Consideration **not disclosed** in documents reviewed | **Include as a named driver + monitorable**; quantum marked TBC | Worldwide perpetual ownership of the Reynolds brand + IP, business assets, employees, contracts *and associated liabilities* in pens/markers/highlighters/school supplies. Strategically material regardless of price; the undisclosed consideration and assumed liabilities are a genuine gap |
| Q1FY27 margin collapse | −529bps EBITDA margin | **Include — central to the rationale** | Far exceeds R13 materiality on every limb |
| Capital commitments | ₹93.78cr (FY26) vs ₹65.28cr (FY25) | Include | Ongoing capacity build (Umbergaon line from Q2FY27E) |
| Contingent liabilities — GST | **₹11.28cr (FY25) → ₹0.51cr (FY26)** | Include, one line | A large *favourable* movement (−96%); worth noting as resolved exposure, not a risk |
| Contingent liabilities — Income tax | ₹0.26cr → ₹0.10cr | Exclude from drivers | Immaterial |
| Cash/deposit drawdown | ₹305.9cr → ₹61.8cr over 2 years | **Include — liquidity discussion** | Explains the net-cash → net-debt shift |
| IPO proceeds | ₹332.72cr, **fully utilised** as at 30-Jun-2026, per objects | Include, one line | Clean utilisation, no deviation reported; ICRA-style monitoring-agency confirmation not applicable |
| Auditor opinion | Unqualified; single KAM (revenue recognition timing); Price Waterhouse Chartered Accountants LLP | Include in analytical approach | Clean |
| Promoter holding discrepancy | 70.39% vs 63.39% | **Flag, draw no conclusion** | Unresolved across sources (see §0) |

---

## 7. Methodology Compliance Map (Step 10)

*Methodology read this session: CRISIL **Criteria for manufacturing, trading and corporate services sector**
(March 2026) — Section I (framework), Section IV (financial ratios), Section VIII (consumer staples &
discretionary, as the closest scope match for branded stationery/art materials); **Basics of Ratings**
(LT/ST mapping Table 1, outlook policy); **Criteria for consolidation** (basis determination).*

| CRISIL rating factor | Company evidence | Assessment |
|---|---|---|
| **Industry risk** | Branded stationery/art materials — school-linked, seasonal, moderate cyclicality; RM (paper, pigments, polymers, wood) exposed to input inflation as now demonstrated | Moderate — steadier than industrial cyclicals, but input-cost pass-through is imperfect |
| **Market position** | Leading domestic branded stationery player; distribution 130+ super stockists, 6,250+ distributors, **145,000+ retail outlets**, 1,000+ sales force; brand portfolio + Reynolds addition; FILA export channel | **Strong** — distribution depth is the durable moat |
| **Operating efficiency** | EBITDA margin 17.3% FY26 but **12.1-12.3% Q1FY27**; GM −400bps; capacity expansion (Umbergaon from Q2FY27E) not yet absorbing | **Weakening at the margin** — the key negative |
| **Accounting quality** | Unqualified opinion, single standard KAM, Big-4-network auditor, no restatements found | Clean |
| **Adequacy of cash flows** | Interest coverage 37.3x; NCATD 2.32x; RoCE stable 21.8% | **Very strong** |
| **Financial position / capital structure** | Gearing **0.11x**, TOL/TNW 0.31x, total debt/OPBDITA 0.35x, net debt/OPBDITA 0.20x | **Very strong** |
| **Liquidity & financial flexibility** | Cash+deposits ₹61.8cr (down from ₹305.9cr); current ratio 2.17x; WC bank limits sanctioned (>₹5cr, amount not disclosed); listed with ₹13,700cr market cap | **Adequate, materially thinner than two years ago** |
| **Management risk** | 47-yr operating history; professional board; disciplined M&A track record (6 acquisitions integrated); but rising risk appetite — Reynolds + heavy capex + margin sacrifice for share | Neutral-to-slightly-cautious |
| **Consolidation basis (R12)** | Material operating subsidiaries; NCI ₹82.4cr; Hygiene is a separate reportable segment | **Consolidated** — methodology-determined, not an operator choice |
| **Parent/group support** | FILA 26.01% minority, no support undertaking disclosed | **No notch** (see §5) |

---

## 8. Liquidity (Step 11) — sources vs claims, ~12 months

| Sources | ₹ cr | Claims | ₹ cr |
|---|---|---|---|
| Cash + bank deposits (31-Mar-2026) | 61.8 | Capital commitments | 93.8 |
| FY26 gross cash accrual (PAT + dep) | 327.7 | Reynolds consideration | **Not disclosed — TBC** |
| Expected FY27 GCA (broker-implied, attributed) | ~300-330 | Debt repayment (non-current borrowings) | 38.1 |
| Undrawn WC limits | **Not disclosed — TBC** | Lease obligations (current) | 15.5 |

**Conclusion: Adequate** *(not "Strong")*. Annual cash accrual of ~₹328cr comfortably covers the ~₹147cr of
identified claims several times over, and gearing at 0.11x leaves large untapped debt headroom. But the
descriptor is held at Adequate rather than Strong for three evidenced reasons: (a) the on-balance-sheet
liquid buffer has fallen 80% in two years to ₹61.8cr; (b) the Reynolds consideration is undisclosed and
therefore unquantifiable against these sources; (c) average bank-limit utilisation — CRISIL's own named
liquidity test — is **not available** in the document set. Descriptor is the conclusion of the arithmetic,
and the arithmetic has two holes in it.

---

## 9. Rating view (Step 13)

**Standalone assessment.** The financial risk profile is very strong and, on the FY26 audited position,
improving: gearing fell to 0.11x, total debt/OPBDITA to 0.35x, interest coverage rose to 37.3x, and RoCE
held at 21.8% through a heavy investment year. Revenue compounded 23% over FY24-26 with a genuinely deep
distribution moat (145,000+ outlets). Against this: EBITDA margin has turned down (18.2% FY25 → 17.3% FY26 →
12.1-12.3% Q1FY27), the liquid buffer has been spent from ₹305.9cr to ₹61.8cr, and the group is
simultaneously absorbing a brand acquisition of undisclosed cost and a capacity build not yet productive.

The margin compression is real but **the balance sheet absorbs it with room to spare**: even holding the
Q1FY27 margin flat for a full year, EBITDA of roughly ₹330cr against finance costs of ₹10.8cr implies
coverage near 30x and net debt/OPBDITA well inside 0.5x. Nothing in the deterioration threatens debt
service; it is an earnings-quality and return-trajectory issue, not a solvency one.

**Support notching:** none (FILA 26.01% minority, no undertaking — §5).
**Instrument adjustments:** none — plain bank facilities, no hybrids or structured features.
**LT/ST mapping:** at AA− (corporates), CRISIL's Table 1 maps to **A1+** — *(no short-term facility is
evidenced in the documents as rated; stated for completeness only)*.

**Independent view: CRISIL AA− / Stable.**

Outlook Stable rather than Negative: the compression is input-driven and explicitly a strategic
market-share choice, the company guides to 18-20% topline growth, and the leverage/coverage profile has
enormous headroom to absorb a multi-year margin reset. Outlook would come under pressure if margin fails to
recover toward mid-teens through FY28 *while* leverage rises on the Reynolds integration.

**Step 14 divergence:** the outstanding rating disclosed in the AR is CRISIL AA−/Stable. My independently
reasoned view **converges** with it. Declared limitation: I knew that rating before forming the view (§0) —
this convergence is therefore weaker evidence than the Happy Forgings case, where the anchor was not visible
until after the view was formed. What I can say honestly is that the metric profile (gearing 0.11x, coverage
37x, RoCE 21.8%, ₹2,326cr revenue) sits naturally in the AA−/AA band on the peer calibration used, and that
I found no factor that would argue for a different letter.

---

## 10. Disclosed scoping decisions (Rule 1 — named, not silent)

1. **Rated amount is NOT stated.** The AR discloses the rating but never the facility quantum, and no term
   sheets/sanction letters were uploaded. Per the binding data rule the amount is **"to be confirmed by
   issuer"** — not reconstructed, and not imported from any CRA publication.
2. **Rating history is incomplete and internally contradictory** (§0) — presented as TBC rather than resolved.
3. **The 5-year model and the `Rating_Scorecard.xlsx` anchor (Step 12/12b) are NOT built in this pass.**
   The rating view above rests on the computed suite, the methodology map and peer calibration. Given the
   entity's complexity (six subsidiaries, two segments, NCI, an undisclosed-consideration acquisition and a
   live margin break), a model built now would carry an unquantifiable acquisition and an unresolved margin
   trajectory — I would rather build it once the Reynolds consideration and FY27 H1 margins are known than
   ship a false-precision forecast. **Offered as the immediate next step.**
4. **Peer reference reports were not re-read this session** — the CRISIL house style and sector calibration
   were taken from the Ramkrishna Forgings and Craftsman Automation rationales read earlier in this same
   session. Both are auto-component, not stationery; the *format* transfers, the *sector calibration* does
   not. Stated as a limitation on the peer-benchmarking strength.

---

*Data cutoff: Q1 FY2026-27 (30-Jun-2026); audited base FY2025-26. Every figure computed in
`compute_ratios.py` from the company's audited consolidated statements or traced to a document location.
No CRA-published amount has been used as data.*

---

## STEP 12 / 12b — FORWARD VIEW AND SCORECARD ANCHOR (added 01-Sep-2026)

**Anchor grade: Crisil AA+/Stable / Crisil A1+.** Proposed rating in the rationale:
**Crisil AA-/Stable**. The divergence is **two notches and the anchor is HIGHER**, which is
inside the calibrated ±2 screening band and therefore a flag to explain rather than a committee
escalation.

**Why the view sits below the anchor.** The scorecard reads a balance sheet that is, on its own
terms, close to unimpeachable: total debt including leases of Rs 141.26 crore against tangible
net worth of Rs 1,219.73 crore (gearing 0.12x), total debt/OPBDITA 0.35x, interest cover 37x,
and operating cash flow of Rs 254.34 crore. On financial ratios alone this is a AA+ balance
sheet. What the scorecard cannot see is SCALE and the concentration of the franchise. Revenue
is Rs 2,326.37 crore; the company is the number-two player in a category with one much larger
incumbent, and the FY2027 margin print demonstrates that it absorbs raw-material inflation
rather than passing it through. The anchor's own back-testing records that it under-rates
AA+/AAA less than it over-rates the lower grades, but it has no scale term at all — a small
company with a pristine balance sheet scores like a large one.

**Support notches: 0.** F.I.L.A. — Fabbrica Italiana Lapis ed Affini S.p.A. holds 26.01% within
a 70.39% promoter group (Indian promoters 44.38%) and is simultaneously a commercial
counterparty, exports to the FILA Group being a named revenue channel. A 26% strategic
shareholder that is also a customer is not a parent providing implicit support, and notching for
it would be an invention.

**Industry override: 3, not the FMCG sector base of 2.** None of the template's 22 sectors is
stationery. FMCG / Consumer staples is the closest structural match — a branded consumer
manufacturer selling through roughly 145,000 retail outlets — but a staples base score of 2
assumes pricing power that the Q1 FY2027 accounts disprove. The override is set to 3 and this
is its justification.

### The forward view

| | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---|---|---|---|---|
| Revenue (base) | 2,768 | 3,267 | 3,789 | 4,320 | 4,838 |
| OPBDITA margin (base) | 14.0% | 15.8% | 16.2% | 16.5% | 16.5% |
| Capex | 350 | 250 | 180 | 160 | 160 |
| Total debt (base) | 222 | 140 | 55 | 56 | 57 |
| Total debt (stress) | 268 | 322 | 313 | 260 | 190 |

**The finding is that the balance sheet absorbs the greenfield in both cases.** Even in the
stress — margin held near the Q1 FY2027 level of about 12% for two years, a slower volume ramp,
working capital stretched from 10.5% to 12.5% of revenue, and the full capex programme spent —
peak debt is Rs 322 crore against a tangible net worth that never falls. That is a statement
about the starting point, not about the strength of the FY2027 earnings.

**The monitorable is therefore an earnings monitorable, not a leverage one:** whether the
OPBDITA margin recovers from 12.08% towards the mid-teens as the price increases already taken
work through and the Umbergaon capacity absorbs fixed cost. A second year at Q1 FY2027 margins
would not threaten the balance sheet; it would change what the franchise is worth.
