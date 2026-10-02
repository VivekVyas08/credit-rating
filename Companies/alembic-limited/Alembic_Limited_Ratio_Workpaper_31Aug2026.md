# Alembic Limited — Ratio Workpaper (ICRA basis)
*Prepared 31-Aug-2026. Data cutoff: FY2025-26 audited (Board approval 19-May-2026). Engagement type: NEW rating (surveillance commitment set at §12).*

## 1. Document Read Log (Step 1b)

| File | Coverage | Material items found |
|---|---|---|
| annual-report-2025-26_1.md (60,058 words) | Standalone + consolidated balance sheet, P&L, statement of changes in equity; auditor's report incl. Emphasis of Matter and Key Audit Matters; note 6 Investments; note 28 Other Income; note 36(A)/(B) commitments and contingent liabilities; note 36(T) segment report; tax reconciliation; BRSR entity table; corporate-governance credit-rating disclosure; CSR | Electricity-duty litigation (EoM); Rs 1,585.38 lakh Chapter VI-A tax deduction; market value of quoted investments Rs 3,885.89 cr; Paushak fair-value fall driving a Rs 103 cr OCI hit; AR's own credit-rating table is **stale** (see §7) |
| Annual-Report-2024-25.md (60,639 words) | FY2025 + FY2024 comparative columns, both bases; note 6 investments incl. prior-year market value; auditor's report | FY2024 figures used throughout (newer document than the FY23-24 AR carrying the same audited year — failure mode 26); FY2024 market value Rs 5,823.75 cr |
| Annual-Report-2023-24.md (58,456 words) | P&L incl. FY2023 comparative; exceptional-item note; auditor's report; note 6 | **FY2023 exceptional item of Rs 10.61 cr and the QUALIFIED audit opinion it drew** — outside the three-year window but recorded under R13; FY2023 market value Rs 3,156.46 cr |

**Known gaps, handled per Step 1 (all three declared in the request):**
- **No quarterly/interim results.** The data cutoff is therefore 31-Mar-2026 audited, with **no bring-down check possible** between the cutoff and this report's date. This is stated in the rationale's disclaimer rather than glossed. For a company whose central rating driver is a *marked-to-market* investment portfolio, this is a material limitation, not a formality — the portfolio's value on any later date is unknown to this exercise.
- **No instrument term sheets / sanction letters.** Rated amounts are taken from ICRA's own published action of 30-May-2025 under the five-condition amendment (§7), not reconstructed.
- **No sector-assumptions document.** The forward view rests on the company's own disclosures; the Step 12 treatment is scaled accordingly and recorded in `case.json`.

## 2. Methodology routing and a SCOPE REJECTION (Step 2/3, failure mode 4)

The request pre-selected two methodology files. One of them **does not fit, and is not cited**:

**`941~Investment Companies, Rating Methodology, Jan 2025.md` — REJECTED on its own scope statement.** It defines its scope as investment companies *"that do not have significant operations of their own and depend on investment income and/or divestment of their investments to service their debt"*. Alembic Limited fails that test on its own numbers: Rs 231.93 crore of FY2026 revenue from operations against Rs 62.95 crore of dividend income — operations are roughly 79% of the revenue base, and the real-estate segment alone contributed Rs 78.59 crore of segment profit. AL is an operating company that also holds a large investment portfolio, not an investment company. Citing this methodology would be failure mode 4.

**Applied: `960~Corporate Credit Rating Methodology, Jul 2025.md`, alone**, plus the cross-cutting Consolidation and Parent/Group Support approaches. Per Section 5's routing rule, where no sector methodology exists the Corporate methodology applies alone — and there is no ICRA real-estate-developer methodology in the folder for a company of this shape (a landholder developing and leasing its own estate rather than a pure residential developer).

**The rejection does not discard the analysis the Investment Companies methodology points at.** The market value of the listed portfolio is the dominant rating factor here and is treated as such under the Corporate methodology's *financial flexibility* factor — which is where it belongs for an operating company.

## 3. Basis determination (R12 — methodology-determined, not an operator choice)

**STANDALONE**, with consolidated carried alongside. Three structural reasons, all verified in the engine:

1. **Consolidation adds no debt.** Consolidated borrowings equal standalone borrowings to the rupee in both disclosed years (Rs 661.08 lakh non-current + Rs 402.77 lakh current). The 100% subsidiary, Alembic City Limited, carries none. Tied out in code.
2. **The subsidiary is immaterial to scale.** Consolidated revenue exceeds standalone by Rs 8.06 crore on a Rs 231.93 crore base.
3. **The consolidated P&L is dominated by a non-cash line.** "Share of Associate's Profit" of **Rs 191.45 crore** (FY2026) — the equity-method pick-up on the 28.54% Alembic Pharmaceuticals stake — **exceeds the group's own profit of Rs 125.93 crore**. Any consolidated margin or coverage ratio is therefore driven by an accrual the company cannot spend. What it *can* spend is the **dividend actually received, Rs 62.95 crore**, which is a standalone P&L line. Debt service is a cash question; the standalone statements answer it.

## 4. Ratio suite (ICRA convention, standalone, Rs crore)

`compute_ratios.py` — **162/163 tie-outs reconcile; mutation-measured coverage 100.0%**. The single non-reconciling check is a documented, explained divergence (§6), not an extraction error.

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Operating income | 152.25 | 214.36 | 231.93 |
| OPBDIT | 56.25 | 89.55 | 87.69 |
| OPBDIT/OI (%) | 36.95 | 41.78 | 37.81 |
| PAT | 92.89 | 141.95 | 124.54 |
| PAT/OI (%) | 61.01 | 66.22 | 53.70 |
| Total debt | 9.15 | 14.45 | **10.64** |
| Tangible net worth | 808.76 | 853.19 | 821.46 |
| TOL/TNW (times) | 0.17 | 0.18 | 0.17 |
| Total debt/OPBDIT (times) | 0.16 | 0.16 | **0.12** |
| Interest coverage (times) | 81.85 | 48.94 | **55.95** |
| Gearing (times) | 0.01 | 0.02 | 0.01 |
| Net debt | (3.90) | (39.30) | **(81.38)** |
| Dividend income | – | 62.95 | 62.95 |

**Market value of quoted investments (company's own note-6 disclosure, Rs crore):**

| FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| 3,156.46 | **5,823.75** | 5,490.20 | **3,885.89** |

### Trend, not snapshot (failure mode 16)
- **The portfolio has fallen 33% from its FY2024 peak** — Rs 5,823.75 cr → Rs 5,490.20 cr → Rs 3,885.89 cr. The FY2026 fall alone is Rs 1,604.31 crore (29.2%). This is the single most important direction in the file and it runs *against* the credit, even though the absolute level remains overwhelming (365x total debt).
- **Operating income has grown strongly**: Rs 152.25 cr → 214.36 → 231.93, +52% over two years, driven by real estate.
- **Net cash has deepened every year**: Rs (3.90) cr → (39.30) → (81.38). The company is progressively more liquid.
- **OPBDIT margin peaked in FY2025** (41.78%) and eased to 37.81% in FY2026 — the segment note attributes this to real-estate segment profit falling from Rs 83.90 cr to Rs 78.59 cr on flat revenue, i.e. project mix, not a demand problem.
- **PAT fell 12.3% while PBT fell only 3.4%** — a tax-line effect, explained at §6, not an earnings deterioration.

## 5. Segment analysis (note 36(T), standalone, Rs crore)

| Segment | FY2025 revenue | FY2026 revenue | FY2025 PBT | FY2026 PBT |
|---|---|---|---|---|
| Real Estate | 182.14 | 185.35 | 83.90 | 78.59 |
| API | 32.21 | 46.59 | 4.73 | 5.65 |
| **Total** | **214.36** | **231.93** | **88.63** | **84.24** |
| Unallocated income (dividends, investment gains) | | | 65.19 | 64.22 |

**Real estate is the operating engine — 80% of revenue and 93% of segment profit.** The API business grew 45% year-on-year but remains small at 20% of revenue and 7% of segment profit. The sector-defining metric question (failure mode 21) resolves to real-estate metrics, not pharma ones: bookings, unsold inventory and rental income. **Project-level booking percentages and rental-income figures were searched for and are NOT disclosed in the annual reports** — the AR discusses projects qualitatively without per-project booking data. Recorded as an evidenced gap; the pre-flight's own sector detector flagged "utilisation / EBITDA per tonne", which is a metals signature and does not apply here.

## 6. Normalisation and tax decisions, written (failure mode 36)

**Other Income note 28 decomposed in full and tied to its printed total** (Rs crore, FY2025 → FY2026):

| Component | FY2025 | FY2026 | Treatment |
|---|---|---|---|
| Dividend income | 62.95 | 62.95 | Stripped from OPBDIT per ICRA convention. **Recurring and cash — the single most important item for debt service**, and treated as such in the liquidity analysis rather than the margin. |
| Interest income | 1.93 | 1.40 | Stripped; recurring |
| Profit on sale of investments | 1.11 | 4.93 | Stripped; non-recurring by nature |
| Fair-value change, trading investments | 1.98 | – | Stripped; non-recurring |
| Insurance claim received (net) | 3.29 | – | Stripped; **genuine one-off** (Rs 4.33 cr claim less Rs 1.05 cr loss on the damaged asset) |
| Forex gain (net) | 0.03 | 0.04 | Stripped; immaterial |
| Gain on sale of PPE | 0.00 | – | Stripped; immaterial |
| Others | 3.22 | 3.45 | Stripped |
| **Total (ties to printed note 28)** | **74.51** | **72.77** | |

**Forex is a GAIN in every year (Rs 0.03 cr / Rs 0.04 cr) and there is no forex loss anywhere in Other Expenses** — searched. The failure-mode-36 asymmetry trap (a gain stripped from Other Income while a loss stays inside operating costs) therefore does not arise here, but it was checked rather than assumed.

**Exceptional items are nil in all three years.** The Rs 10.61 crore item the pre-flight flagged belongs to **FY2023**, outside this window.

**The tax rate is low and it is STRUCTURAL, not a one-off.** Implied tax rates of 6.61% (FY2025) and 15.2% (FY2026) fall below the 8–45% plausibility band the shared checks apply. The tax reconciliation explains it precisely: a **Chapter VI-A deduction worth Rs 15.85 crore of tax in both years**, which at the 25.17% concessional rate shelters roughly Rs 63.0 crore of income — the dividend income of Rs 62.95 crore, almost to the rupee. This is Section 80M inter-corporate dividend relief, and it is available **because AL passes the dividend through to its own shareholders** (dividends paid Rs 61.41 crore in FY2026 against Rs 62.95 crore received - standalone cash flow, financing activities). The shelter is recurring while that payout policy holds; it is **not** modelled as a permanent tax advantage independent of the payout.

## 7. Rated amounts — and a stale-table finding (Step 7b, failure modes 14/26/29)

**The company's own annual report carries a STALE rating table.** The FY2025-26 AR's corporate-governance section discloses ICRA facilities of Rs 34.00 + 25.50 + 10.00 crore = **Rs 69.50 crore**, stamped *"reaffirmed on 28th February, 2024"*. ICRA's own subsequent action of **30-May-2025** reduced the long-term fund-based line from Rs 34.0 crore to Rs 20.9 crore, taking the total to **Rs 56.4 crore**.

The newer figure is used. Per the five-condition amendment, all five are met: (1) ICRA's primary published rationale for this issuer is in `Report for Reference/`; (2) reproduced verbatim, every line, date-stamped; (3) labelled CRA-published, not issuer-confirmed; (4) line integrity verified — 20.9 + 25.5 + 10.0 = 56.4 exactly; (5) the limits-vs-drawn distinction is stated: **rated limits Rs 56.4 crore against drawn debt of Rs 10.64 crore.**

## 8. Qualitative fact register (traced, corroborated)

- **Group structure:** **Nirayu Private Limited holds 63.06%** of AL (16,19,15,052 shares, unchanged FY2025→FY2026) — AL is itself a subsidiary. AL holds **28.54% of Alembic Pharmaceuticals Limited** (associate, equity-accounted in consolidated) and **47,02,472 shares of Paushak Limited** post a split and bonus issue during FY2026 (below the 20% associate threshold, hence carried at FVOCI). **Alembic City Limited** is a 100% subsidiary.
- **The Paushak markdown is what moved net worth.** Paushak's carrying value fell from Rs 265.50 cr to Rs 162.52 cr — a Rs 102.99 crore fall routed through OCI, which is why tangible net worth fell from Rs 853.19 cr to Rs 821.46 cr despite Rs 124.54 crore of PAT.
- **Alembic Pharmaceuticals is carried at COST (Rs 86.65 crore) in the standalone accounts** and has been for both years. Standalone book value therefore understates the economic position by an order of magnitude — the market value of quoted investments is Rs 3,885.89 crore against a standalone net worth of Rs 821.46 crore.
- **Auditor's opinion FY2026: UNMODIFIED**, both bases, with an Emphasis of Matter on the electricity-duty litigation. Key Audit Matter: litigations, provisions and contingent liabilities.
- **Contingent liabilities (standalone, FY2026):** letters of credit and guarantees Rs 6.01 cr; service tax in appeal Rs 5.20 cr (net of a Rs 1.18 cr provision); sales tax Rs 1.24 cr; green cess Rs 0.19 cr — **Rs 12.64 crore quantified in total, 1.5% of net worth.** Capital commitments Rs 13.52 crore (down from Rs 31.19 crore).
- **The electricity-duty matter is the one genuinely open-ended exposure.** A provision of Rs 20.52 crore has been made for the principal; **Rs 35.00 crore was deposited with the Supreme Court on 26-May-2023** and the appeal admitted. **The interest is disclosed as unascertainable** and is not acknowledged by the company — so the exposure cannot be sized from the documents. That is a real limitation on the analysis, not a formality. Counterparties per the AR: the State of Gujarat, the Collector of Electricity Duty, the Chief Auditor and the Industries Commission. **The AR gives no 2004 notice date and does not describe a High Court ruling** — those appear only in ICRA's published rationale, which under Section 2 supplies no facts, so they are NOT used anywhere in this case.
- **ESG — the BRSR carries a quantified dataset, and an earlier draft of this workpaper wrongly
  said it did not (failure mode 20, caught on self-audit before delivery).** All figures below
  are the company's own BRSR disclosures, FY2026 against FY2025:

  | BRSR metric | FY2026 | FY2025 | Direction |
  |---|---|---|---|
  | Scope 1 emissions (MT CO2e) | 565.05 | 379 | up 49% |
  | Scope 2 emissions (MT CO2e) | 820.35 | 1,290 | down 36% |
  | Scope 1 + 2 total | 1,385.40 | 1,669 | **down 17%** |
  | Emission intensity per rupee of turnover | 0.00000060 | 0.00000078 | down 23% |
  | Total energy consumed (GJ) | 83,320.45 | 1,10,097.07 | down 24% |
  | Renewable share of energy | **26.7%** | 23.2% | up 3.5pt |
  | Water withdrawal (kl) | 1,05,941 | 82,330 | up |
  | Water consumption (kl) | 19,071 | 82,330 | down |
  | LTIFR, employees and workers | **Nil** | Nil | – |
  | POSH complaints | Nil | Nil | – |

  The emission-intensity arithmetic was verified rather than transcribed: 1,385.40 MT against
  revenue of Rs 231.93 crore gives 5.97e-7, and 1,669 MT against Rs 214.36 crore gives 7.79e-7 —
  reproducing both printed intensity figures, which also confirms the first column is FY2026 and
  not the comparative.

  Qualitative: the new commercial building holds a **USGBC Silver rating**; API water consumption
  fell 9.22% and power consumption by 7,61,137 kWh against a ~3,00,000 kWh target (the company
  attributes the overshoot to one-time debottlenecking, not a run-rate); captive windmills and
  co-generation supplement grid power; air-emission and water data are externally evaluated by
  Birla Vishvakarma Mahavidyalaya. **CSR obligation Rs 1.12 crore, fully spent, no unspent
  balance.** Governance: 8 directors of whom **4 are independent (50%), including one woman
  independent director**; a non-executive promoter chairman; four board meetings held; no
  conflict-of-interest complaints against directors or KMP in either year.

  **Genuinely absent, and searched:** the BRSR reports no Scope 3 inventory, no net-zero or SBTi
  commitment (the company states it has no GHG-reduction project, only power-consumption goals),
  and no external assurance of the energy data. The AR also states that energy-conservation
  investment is "embedded in project cost and is not separately quantified".

## 9. Methodology Compliance Map (Step 10 — Corporate Credit Rating Methodology, July 2025)

| Rating factor | Company evidence | Assessment |
|---|---|---|
| Industry risk | Two unrelated businesses: real-estate development/leasing (cyclical, local to Vadodara) and API manufacturing (competitive, small scale) | Moderate; diversification is partial because both are small relative to the investment portfolio |
| Business risk / market position | Real estate 80% of revenue, Rs 185.35 cr; API Rs 46.59 cr, +45% y-o-y; land bank held for development | Modest operating scale — this is the binding constraint on the rating |
| Operating efficiency | OPBDIT margin 36.95% → 41.78% → 37.81% | Strong margins, characteristic of a landholder developing its own estate at low land cost |
| **Financial risk** | Gearing 0.01x; total debt Rs 10.64 cr; TOL/TNW 0.17x; interest coverage 55.95x; **net cash Rs 81.38 cr** | **Exceptionally strong — effectively unlevered** |
| **Financial flexibility** | **Quoted investments at market value Rs 3,885.89 cr = 365x total debt**, against standalone net worth of Rs 821.46 cr | **The dominant strength.** Tempered by a 33% fall from the FY2024 peak |
| Management & governance | Unmodified FY2026 opinion; FY2023 qualification (transfer from General Reserve to P&L as an exceptional item) now behind; stable promoter holding | Adequate; the FY2023 episode is recorded under R13 and is a genuine, if historic, governance mark |
| Parent/group | Nirayu Private Limited holds 63.06%; no support is required and none is assumed | No notching in either direction — see §10 |

## 10. Parent/group treatment

AL is 63.06%-held by **Nirayu Private Limited**, an unlisted holding company for which **no financial information whatsoever is in the document set** — searched. Under ICRA's parent/group approach, notching requires an assessment of the parent's own credit profile, and that cannot be performed on this evidence. **No uplift is taken.** Nor is a cap applied: AL requires no support in any scenario these documents evidence (net cash, 365x asset cover on debt), and capping a self-sufficient subsidiary on an unassessable parent would be a conclusion the evidence does not support. The rating is therefore on AL's standalone profile, and **the absence of parent financials is disclosed as a limitation** rather than resolved by assumption.

## 11. Liquidity (Step 11 — sources vs claims, ~12 months)

**Sources:** cash and bank balances Rs 2.97 crore + current investments Rs 89.05 crore = **Rs 92.02 crore of on-balance-sheet liquidity**; recurring dividend income of **Rs 62.95 crore** (received in both FY2025 and FY2026 at a near-identical figure); FY2026 OPBDIT of Rs 87.69 crore; and, behind all of it, **Rs 3,885.89 crore of listed, quoted investments** that are saleable.

**Claims:** total debt of **Rs 10.64 crore** (of which Rs 4.03 crore is current); capital commitments of Rs 13.52 crore; finance cost of Rs 1.57 crore; dividend paid Rs 61.63 crore.

**Descriptor: Superior.** On-balance-sheet liquidity alone (Rs 92.02 cr) covers total debt 8.6 times; dividend income alone covers total debt 5.9 times and finance cost 40 times; the quoted portfolio covers total debt 365 times. The arithmetic does not admit a weaker descriptor. **The one caveat is stated rather than buried:** the portfolio's realisable value moves with two listed share prices and has fallen 33% in two years, so the *magnitude* of the cushion is volatile even though its *adequacy* is not remotely in question at these debt levels.

## 12. Step 12 scaling decision and surveillance (R15, failure mode 35)

Recorded in `case.json`. A full 5-year 3-statement model is **not** the proportionate artefact here, and the reason is specific: with total debt of Rs 10.64 crore against Rs 3,885.89 crore of listed securities, no plausible path for revenue, margin or capex changes the debt-servicing conclusion. What *does* move this credit is the market value of two listed holdings and the litigation outcome — neither of which a 3-statement projection models. A **focused sensitivity on those two variables plus the real-estate segment** is used instead: `Alembic_Limited_Sensitivity_Model_31Aug2026.md`.

**Surveillance:** annual review; event-driven triggers are (a) a Supreme Court ruling on the electricity-duty appeal, (b) a further material fall in the quoted portfolio, (c) any debt-funded acquisition or land purchase, (d) a change in the Nirayu shareholding.

## 13. Step 12b anchor and divergence

`Rating_Scorecard_Alembic_Limited.xlsx`, filled by `fill_scorecard.py` from the engine's own
outputs (never retyped) and evaluated offline through the workbook's own formula chain via
`python rate_engine.py alembic-limited --engine local`.

**Anchor grade: AA-.** Sector taken as *Real Estate / Construction* (base score 4.5), which is
the nearest of the workbook's 22 sectors given that real estate is 80% of revenue. Qualitative
scores: **Business risk 4** — modest, single-city operating scale is the binding constraint;
**Management & governance 3** — unmodified FY2026 opinion, held off a 2 by the FY2023
qualification and the density of related-party dealing; **support notches 0** — no uplift (the
holding company cannot be assessed) and no cap (no support is needed); **liquidity Superior**;
**outlook Stable**. Each justification is written into `fill_scorecard.py` beside the score.

**Divergence: none.** The anchor (AA-), the independent judgment view (AA-) and the prior
published action (AA-) coincide, so there is no anchor-divergence to resolve under the Step 12b
rule. Worth recording that this is the first case in this project where all three agree: the two
preceding cases both read one notch low at the AA+/AAA boundary, consistent with the documented
calibration limitation in `Scorecard_Backtest_Report_18Jul2026.md`. AA- sits inside the band
where the backtest reports the anchor is reliable to about +/-1 notch, which is part of why it
lands here.

**Projection inputs** (copied, not linked, from the focused sensitivity): revenue growth 8%/8%,
OPBDIT margin 37.5%, capex Rs 70 crore a year, net new debt **-4.0 crore a year derived from the
funding gap** (accrual ~138 less dividend ~61 less capex 70 leaves a ~7 crore surplus, so no
external borrowing is required and the only movement is scheduled repayment), implied interest
rate 12.5% on the average book, tax 16%, dividend payout 49%.

## 14. Divergence against the prior ICRA action (Step 14)

See §7 for the rated amounts (extracted at Step 7b per failure mode 29, before the view was
formed). ICRA's published action of **30-May-2025** rates AL **[ICRA]AA- (Stable) / [ICRA]A1+**
on Rs 56.4 crore.

**On the grade there is no divergence.** The independent view formed here — exceptional
financial flexibility and effectively nil leverage, held back by modest operating scale and a
portfolio whose value has fallen a third in two years — arrives at [ICRA]AA- (Stable) /
[ICRA]A1+. The Step 12b scorecard anchor, run through the workbook's own formula chain,
**also returns AA-**, so judgment view, anchor and prior action agree. This is the first case in
this project where all three coincide without an anchor-divergence to resolve.

### The ratios DO diverge, materially, and the reason is a single definitional choice

| Metric, FY2025 | ICRA published | Computed here | Gap |
|---|---|---|---|
| Operating income | 280.6 | 214.36 | 66.24 |
| OPBDIT/OI | 55.5% | 41.78% | 13.7pt |
| Interest coverage | 85.1x | 48.94x | 36.2x |
| PAT | 141.9 | 141.95 | – |
| Total debt/OPBDIT | 0.1x | 0.16x | – |
| TOL/TNW | 0.2x | 0.17x | – |

**PAT reproduces to the rupee, which localises the divergence precisely: it is not an extraction
difference, it is a classification difference above the PAT line.** Solving for the single
add-back `X` that each published ratio implies gives three independent answers that agree:

| Year | X from the margin | X from interest coverage | X from operating income |
|---|---|---|---|
| FY2024 | 46.10 | 45.94 | 45.95 |
| FY2025 | 66.11 | 66.17 | 66.24 |

Agreement to within Rs 0.15 crore across three routes proves the whole gap is **one amount added
to operating income and to OPBDIT simultaneously.** That amount is the investment income:
dividend received was **Rs 45.91 crore in FY2024** and **Rs 62.95 crore in FY2025** (standalone
cash flow / note 28), with the small residual matching the note's "Others" line of Rs 3.22 crore
in FY2025.

**ICRA is treating AL as an investment company** — its published Analytical approach cites the
Investment Companies methodology alongside the Corporate one — and on that reading dividend
income is operating revenue rather than other income. **This exercise reached the opposite
routing conclusion at §2, on that methodology's own scope statement**, which covers entities
that do not have significant operations of their own; AL's Rs 231.93 crore of FY2026 operating
revenue and Rs 78.59 crore of real-estate segment profit do not fit that description.

Under §4 of the master prompt, where a reference report conflicts with a methodology's scope,
**the methodology wins and the divergence is disclosed** — which is what is done here. The
divergence is disclosed in the rationale itself (failure mode 6), not only in this workpaper.

**It changes no conclusion.** The dividend income is not discarded by the stricter convention;
it is analysed where it does the work — in liquidity and financial flexibility, where Rs 62.95
crore of recurring cash against Rs 10.64 crore of debt and Rs 1.57 crore of finance cost is
decisive. The narrower convention is also the more conservative one: it reports a 37.81%
operating margin rather than a ~55% one, and 55.95x interest cover rather than ~85x, and still
supports the same grade.

### Other differences worth recording

- ICRA's rationale quotes **project-level booking percentages, a 102-acre land bank and a
  working-capital headroom figure** that are **not in the annual reports** — searched. Under
  Section 2 the reference library teaches craft and supplies no facts, so none of that is used
  here. Its absence from this report is a documented evidence limitation, not an oversight.
- ICRA states Paushak at **19.1%/19.07%**. The FY2025-26 AR discloses the holding by share count
  (47,02,472 shares after a split and bonus issue) and fair value, not by percentage. The
  percentage is therefore not used as a figure anywhere in the deliverable.
- **AL's own annual report carries a stale rating table** (Rs 69.50 crore, 28-Feb-2024) that the
  30-May-2025 action superseded — see §7. Reported as a finding.
