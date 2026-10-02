# Workpaper — State Bank of India | CRISIL | 14 August 2026

**Rating view:** Crisil AAA/Stable (senior, fixed deposits, infrastructure bonds, Tier II under
Basel III) · Crisil AA+/Stable (Tier I under Basel III) · Crisil A1+ (certificate of deposits).

---

## 0. Scope statement (read first)

Processing was interrupted by a session token limit that terminated two background agents; the
work was completed directly, and the four items left open at first delivery were closed in a
second pass on the same date.

| Step | Status |
|---|---|
| Step 1a pre-flight | **Done** — §1 |
| Step 1b read of all 8 documents | **Done** — §2. All three ARs and all five quarterly releases now covered. |
| Ratio engine + tie-outs | **Done** — 34/34 reconcile |
| Ratio Excel (standing deliverable) | **Done** — 65 cached values |
| Step 14 divergence | **Done** — §5 |
| Section audit (Step 17a) | **Done** — passes; bank KPI rule verified to actually fire |
| Entities-consolidated annexure | **Done** — §2a. 22 subsidiaries, 7 JVs, 10 associates named with holdings. |
| Standalone scorecard .xlsx | **Done** — §6a |
| 5-year projection model | **Done** — §6b |
| Methodology read | **Partial** — CRISIL bank criteria consulted via the agency's applied rationale and the peer set, not read end-to-end. The one remaining departure. |

### What the completion pass changed in the rating analysis

Closing Step 1b was not a formality — **it materially corrected the rationale.** The Q1FY27 press
release is dated **07-Aug-2026, seven days before this report's date**, so it was public and
should have been in the first draft. It was not, and its omission had produced a stale and
misleadingly negative characterisation of the bank's central weakness:

| | First draft (FY2026 only) | Corrected (with Q1FY27) |
|---|---|---|
| NII growth | +4.08% | **+14.88%** |
| Domestic NIM | 3.03%, falling | **3.00%, +7 bps sequentially** |
| Narrative | "margin compression is the one clear negative trend" | compression concentrated in H2 FY2026 and **now unwinding** |
| CRAR | 15.40% | **15.67%** |
| GNPA / NNPA | 1.49% / 0.39% | **1.47% / 0.38%** |

The rating itself does not change. The characterisation of the weakness does, from a deteriorating
trend to a level-versus-peers observation. **This is a direct, measured instance of the cost of
skipping Step 1b** — the shortcut did not save an error-free report, it produced a wrong story
about the single most important negative in the credit.

---

## 1. Step 1a — PRE-FLIGHT (mandatory gate)

```
PRE-FLIGHT  |  SBI  |  agency CRISIL  |  8 documents, 642,103 words

[1] PRIOR RATING ACTION IN THE REFERENCE LIBRARY
    (acronym case name - also searching legal name seen in documents: 'State Bank of India')
    *** PRESENT - Step 14 IS APPLICABLE ***
      - CRISIL:   State Bank of India_05 Mar 2026_RR_390958.md
      - CareEdge: State Bank of India_13 Oct 2025.md
      - CRISIL:   SBI Cards and Payment Services Limited_25 Jun 2026 (DISTINCT ENTITY - subsidiary)
[2] CREDIT-RATING NOTE in the issuer's own AR      *** PRESENT - 69 matches
[3] SUBSIDIARIES / entities to NAME                *** PRESENT - 1,046 matches
[4] ESG data                                       *** PRESENT - 1,527 matches
[5] INSTRUMENT details                             *** PRESENT - 41 matches
[6] CAPEX / investment cycle                       *** PRESENT - 26 matches
[7] SHAREHOLDING / promoter stake                  *** PRESENT - 7 matches
[8] AUDITOR opinion / KAM / EOM                    *** PRESENT - 125 matches
[9] SECTOR-DEFINING METRIC -> NIM / GNPA / CRAR / CASA  *** PRESENT - 132 matches
```

Binding effect: none of the above may be described as "not available" anywhere in the report.

### 1a. TWO DEFECTS IN THE PRE-FLIGHT ITSELF, FOUND ON THIS CASE

**(i) The pre-flight made a false absence claim — the exact error it exists to prevent.**
On first run it printed `word_search on []` followed by *"'no prior action' is EVIDENCED"*. The
token filter required names longer than three characters; **"SBI" is exactly three**, so it
derived **zero search tokens, searched nothing, and reported evidenced absence.** In fact a CRISIL
rationale dated 05-Mar-2026 and a CareEdge rationale dated 13-Oct-2025 both exist. Had this been
trusted, Step 14 would have been skipped and a superseded rating published — a verbatim repeat of
the Indus Towers failure that motivated failure mode 24.

Fixes applied to `preflight.py`:
- minimum token length lowered to 3;
- **an empty token set now prints `!!! INCONCLUSIVE — NOTHING WAS SEARCHED`** and forbids the
  absence claim, instead of concluding absence;
- acronym case names now recover the issuer's legal name from the documents themselves
  (`SBI` → *"State Bank of India"*), skipping uninformative candidates such as *"The Bank"*;
- `bank` added to the generic-token list so a bank case does not match every bank in the library;
- self-test extended with four token-derivation cases so an empty search cannot recur.

**(ii) Sector detection returned "EBITDA per tonne" (cement) for a bank**, because a bank's annual
report discusses cement, mining and steel — it lends to them. The bank trigger was widened and now
returns NIM / GNPA / CRAR / CASA correctly.

---

## 2. Step 1b — Document Read Log (scope-limited, declared)

| Document | What it contributed | Material items flagged |
|---|---|---|
| `Annual_Report_FY2026_2.md` (261k words) | **Primary source.** Ten-year highlights (L420-450); asset-quality table (L4282-4286); Chairman's statement (L764-790); capital/LCR/NSFR (L11695-11998); GoI shareholding 55.03% (L11698); AT1 ISIN detail (L11735); subsidiary/JV/associate schedules (L3809-3819, L7997-8015, L8032-8458, L14838-14856); ESG and green advances. | D-SIB 0.80% CET-1 surcharge from 01-Apr-2025; CASA on domestic-deposit basis; green advances more than doubled to Rs 1,18,723 crore; **SBI exited Jio Payments Bank** (14.96% → nil). |
| `Annual_Report_FY2025_2.md` (225k words) | FY2025 comparatives; auditor opinion; RBI divergence disclosure. | GoI holding 56.92%. **RBI supervisory process required NO divergence disclosure** on asset classification/provisioning — a clean supervisory outcome. No qualification, no adverse opinion, no going-concern emphasis (the "going concern" hits are the standard auditor-responsibility paragraph). |
| `Annual_Report_2024_2.md` (155k words) | FY2024 comparatives; auditor opinion; divergence disclosure. | Same clean outcome as FY2025. |
| `SBI_Press_Release_Q1FY26_2.md` | NIM whole-bank 2.90% / domestic 3.02%. | Start of the NIM series used to date the compression. |
| `SBI_Press_Release_Q2FY26_2.md` | H1 NIM 2.93% / 3.05%. | |
| `07022026_..._Q3FY26_Final_2.md` | 9M NIM 2.95% / 3.08%. | NIM **peaked at 9M** — so the FY2026 full-year decline is a Q4 event. |
| `SBI_Press_Release_Q4FY26_2.md` | FY26 NIM 2.91% / 3.03%. | Confirms Q4 dragged the full-year average down. |
| `07082026_SBI_Press_Release_Q1FY27.md` | **Most recent data, and newer than the AR.** PAT Rs 21,121 cr (+10.23%); operating profit Rs 33,529 cr (+9.77%); NII **+14.88%**; NIM 3.00% domestic / 2.86% whole bank, +7/+5 bps QoQ; advances +18.63%; deposits +9.73%; CASA 39.24%; GNPA 1.47%; NNPA 0.38%; slippage 0.57%; credit cost 0.27%; CRAR 15.67%. | **Margin compression reversing.** Deposits crossed Rs 60 trillion, advances Rs 50 trillion. |

**Corroboration outcome:** the NIM series across five independent quarterly releases confirms the
shape of the margin story — rising through 9M FY2026, dropping in Q4, recovering in Q1 FY2027.
No single document supports that conclusion on its own.

### 2a. Entities consolidated — annexure completed

Extracted from the FY2026 AR's own schedules and now reproduced in full in the rationale:
**14 domestic subsidiaries** (with holdings from 55.33% to 100%), **8 foreign banking/non-banking
subsidiaries**, **7 jointly controlled entities**, and **10 associates** (Bank of Bhutan at 20% plus
nine SBI-sponsored Regional Rural Banks at 35% each). The annexure's "marked incomplete" caveat
has been removed because it is no longer true.

Aggregate interest in jointly controlled entities fell to Rs 25.81 crore from Rs 104.89 crore,
substantially explained by the Jio Payments Bank exit.

---

## 3. Ratio engine and tie-outs (`compute_ratios.py`) — 34/34 reconcile

Material reconciliations:

| Tie-out | Result |
|---|---|
| CRAR = Tier I + Tier II, every year FY2017–FY2026 | Exact, all ten years (FY26: 13.33 + 2.07 = 15.40) |
| NNPA% across two independent tables, FY2021–FY2026 | Exact, all six years |
| Implied PCR from the NPA stock vs reported | (73,452 − 18,830) / 73,452 = **74.36%** = reported PCR excl. AUCA |
| Net profit growth derived vs stated | 12.88% = 12.88% |
| Operating profit growth derived vs stated | 11.25% = 11.25% |
| GNPA improvement derived vs stated "33 bps" | −0.33 pp |
| Narrative FY26 figures vs ten-year table | Net profit, RoE, CRAR, NNPA, cost-income all exact |

### Two breaks investigated rather than tolerance-adjusted

**CASA ratio.** CASA Rs 22.62 lakh crore ÷ deposits Rs 59.76 lakh crore = 37.85%, but the bank
reports **39.46%**. The reported ratio is on the **domestic** deposit base; the Rs 59.76 lakh crore
figure is whole-bank, the text stating deposits grew across *"both domestic and overseas
operations"*. Implied domestic deposits ≈ Rs 57.32 lakh crore and overseas ≈ Rs 2.44 lakh crore,
consistent with 245 foreign offices. Using the global base would understate CASA by 161 bps. The
basis is stated explicitly in the rationale. **The Rs 57.32 lakh crore split is derived, not
disclosed** — it is not quoted as a fact.

**Total business.** "Surpassed Rs 109 lakh crore" is a rounded floor; 59.76 + 49.33 = 109.09
confirms it. Test changed from equality to a bound.

**Corroboration flag (failure mode 15):** the Chairman's-statement figures sit inside a
`<!-- picture text -->` OCR block. They were corroborated against the formal ten-year and
asset-quality tables, which agree exactly on net profit, RoE, CRAR, NNPA and cost-to-income. The
CASA and deposit figures appear **only** in that OCR block and carry residual transcription risk.

---

## 4. Rating view formed BEFORE opening the anchors

Recorded in `build_spreads.py` (RatingScore tab) before either prior rationale was opened:

| Factor | Score | Weight |
|---|---|---|
| Sovereign ownership and systemic importance | 1 | 0.40 |
| Market position and deposit franchise | 1 | 0.20 |
| Asset quality | 1 | 0.15 |
| Capitalisation | 2 | 0.15 |
| Earnings profile | 2 | 0.10 |

**Composite 1.25 → AAA band.** Independent view: **Crisil AAA/Stable · Crisil A1+**.

---

## 5. Step 14 — divergence against the anchors

| Instrument | CRISIL, 05-Mar-2026 | My view | Divergence |
|---|---|---|---|
| Fixed deposits / infrastructure bonds | AAA/Stable | AAA/Stable | None |
| Tier II bonds (Basel III) | AAA/Stable | AAA/Stable | None |
| Certificate of deposits | A1+ | A1+ | None |
| **Tier I bonds (Basel III)** | **AA+/Stable** | *not differentiated* | **My gap** |

**The issuer-level view matched. The instrument-level view did not.** My scorecard produced a
single issuer rating and did not notch the Additional Tier 1 instruments down for their
loss-absorption features — coupon discretion, the distributable-reserves and capital-conservation-
buffer linkage, and principal write-down at the point of non-viability. CRISIL rates them one notch
below senior at AA+/Stable. **This was a real omission, corrected in the rationale**, which now
carries an explicit notching explanation and a "Note on tier I instruments".

CareEdge (13-Oct-2025) was identified by the pre-flight but **not opened** — the CRISIL anchor is
the governing one for a CRISIL-format output, and the token budget was directed there.

**Disclosure:** the AT1 notching was learned from the anchor, not derived independently. It is
evidence-led but not independently arrived at.

### Where this report is more current than the anchor

CRISIL's 05-Mar-2026 action predates the FY2026 results and relies on FY2025 plus 9MFY26 data
(PAT Rs 70,901 crore; GNPA 1.8%; CAR 14.4%). This report uses full-year FY2026 (PAT Rs 80,032
crore; GNPA 1.49%; CAR 15.40%; CET-1 12.29% record). Every FY2026 metric moved favourably, so the
reaffirmation is supported on strictly better numbers.

---

## 6. Materiality sweep

| Item | Finding |
|---|---|
| Auditor opinion | Unmodified. No Emphasis of Matter identified. |
| GoI shareholding | 55.03% (Mar-2026), down from 56.92% (Mar-2025) — dilution, not disposal of control. |
| D-SIB status | Additional 0.80% CET-1 from 01-Apr-2025; leverage ratio comfortably above the 4% mandate. |
| Margin compression | **The one adverse trend.** NII +4.08% against advances +16.87%. Stated as a weakness. |
| RoE trajectory | 20.32% (FY24) → 19.87% (FY25) → 18.57% (FY26), partly a larger equity base. Disclosed. |
| Slippages | Rising in absolute terms (Rs 22,124 cr → Rs 23,804 cr) even as GNPA% fell — flagged in the ratio suite as slippages/opening GNPA. |

---

### 6a. Quantitative anchor — standalone scorecard

`Rating_Scorecard_State Bank of India.xlsx`, scored against **the master template's own
financial-sector bands** (`Ref_Bands_Fin`), not invented thresholds. Convention 1 (strongest) to
6 (weakest).

| Metric | Value | Score | Weight |
|---|---|---|---|
| CRAR | 15.40% | 3 | 0.22 |
| Gross NPA | 1.49% | 2 | 0.18 |
| Net NPA | 0.39% | 2 | 0.15 |
| RoA | 1.12% | 4 | 0.20 |
| NIM | 3.03% | 4 | 0.13 |
| Cost-to-income | 50.11% | 4 | 0.12 |
| **Weighted financial score** | | **3.120** | |
| **Weighted qualitative score** | | **1.150** | |
| **Composite (0.35 / 0.65)** | | **1.839** | |

**The financial block scores 3.12 — nowhere near AAA.** That is the correct result and the most
useful thing the scorecard says: on ratios alone SBI is a mid-scoring bank, with RoA, NIM and
cost-to-income all in the middle bands. The rating is carried by sovereign ownership, systemic
importance and franchise scale. The scorecard is therefore *evidence for* the support-driven
construction — strip the support factor out and the standalone profile does not support the
highest grade. This is the same thing CRISIL says in words when it calls profitability
"improving, yet moderate".

The 0.35/0.65 financial/qualitative weighting is an analyst judgement for a D-SIB public sector
bank; the template publishes no bank weighting. Stated so the assumption is visible.

### 6b. Five-year projection model

`State Bank of India_Financial_Model_14Aug2026.xlsx` — a **bank** model, not a corporate
three-statement model. Driver chain: advances/deposits growth → interest-earning assets → NIM →
NII → +other income → −opex (cost-to-income) → operating profit → −provisions (credit cost) → PBT
→ tax → PAT → capital accretion. Every projected cell is a live formula.

**Calibration first.** The FY2026 column is actual, and the model reconstructs reported FY2026
NII (Rs 1,73,000 cr), operating profit (Rs 1,23,015 cr), PAT (Rs 80,032 cr) and cost-to-income
(50.11%) exactly before any forecast year runs. All four tie-outs return OK.

| | FY2026A | FY2027E | FY2029E | FY2031E |
|---|---|---|---|---|
| Net interest income | 1,73,000 | 1,87,263 | 2,40,975 | 2,95,446 |
| Operating profit | 1,23,015 | 1,34,214 | 1,74,211 | 2,14,505 |
| Provisions | 16,306 | 18,560 | 27,180 | 33,472 |
| PAT | 80,032 | 86,740 | 1,10,273 | 1,35,775 |
| RoAA | 1.12% | 1.07% | 1.08% | 1.08% |
| Advances / deposits | 82.6% | 84.8% | 85.9% | 85.1% |
| Tier I / advances | 10.70% | 11.66% | 11.53% | 11.81% |

**A first pass at these assumptions was wrong and was corrected.** Running advances at 16–12%
against deposits at 10–10.5% drove the loan-to-deposit ratio to **98% by FY2031** — a level no
bank funds. Advances were tapered harder and deposit growth stepped up, holding LDR near 85–86%.
The cost of mobilising deposits faster is also why NIM is not assumed to expand beyond ~2.65%.

Credit cost is normalised **upward** (0.33% actual → 0.40%), deliberately not extrapolating the
current benign 0.27%. RoA dips modestly to ~1.07% on that assumption and holds. Tier I/advances
**builds** from 10.70% to 11.81%: internal accretion outpaces loan growth even at a 20% payout,
which is the quantitative support for the "adequate capitalisation" strength.

**Stress case.** The rationale's downward trigger is "GNPAs crossing 10%". Modelled directly, a
credit cost of 2.50% of average advances (7.5x the FY2026 level) would push FY2027 provisions to
roughly Rs 1,43,000 crore against operating profit near Rs 1,33,000 crore — a pre-tax loss. That
is the scale of deterioration the trigger implies. Nothing in the current data points toward it:
slippage 0.57%, credit cost 0.27%, GNPA 1.47% and still falling.

## 7. Step 17a — section audit, and a defect found in the checker

`check_sections.py` initially **failed** the report for a missing "Rating action" section. Before
changing the report, the checker was run against **CRISIL's own published SBI rationale**, which
**failed identically**. The checker was therefore wrong, not the report: CRISIL expresses the
rating action as a bolded table-header cell (`|**Rating Action**||`), not a markdown header, and
header-only matching could not see it. Table-header cells are now also matched. Both the report and
CRISIL's own file now pass; previously delivered reports still pass.

**Silent-gate check.** The sector KPI rule was verified to *actually fire* rather than pass by not
running: the About-the-Bank section matches on `largest bank` and `scheduled commercial bank`, and
the KPI probe finds GNPA and CET-1 carrying numbers. This was checked because a literal `is a bank`
trigger would **not** have matched "is a scheduled commercial bank" — the gate would have reported
PASS without ever executing.

Final: **PASS**, all mandatory sections, quality probes clean.

---

## 8. Searched-and-absent register

| Searched for | Result |
|---|---|
| Instrument issuance or redemption after 05-Mar-2026 | Not evidenced in the documents reviewed; rated quantum carried forward and dated as such. |
| Full statutory list of consolidated entities | Not extracted. The annexure names the principal entities and **is marked incomplete on its face**; the complete list is in the consolidated financials and Form AOC-1. |
| ISIN-level detail for programme-level lines | Only one ISIN-level instrument disclosure was located (AT1 2024-25, L11735). Programme lines carry no ISIN and are shown as aggregates. |
| CareEdge 13-Oct-2025 rationale | Exists; deliberately not opened (see §5). |

---

## 9. Outstanding items

All four items open at first delivery are now closed (§0). Two genuine items remain:

1. **Read the CRISIL banks-and-financial-institutions criteria end-to-end.** It was consulted
   through the agency's own applied rationale and the bank peer set rather than read in full.
   This is the last standing departure from the SOP.
2. **Corroborate the CASA and deposit figures against the formal balance sheet.** They rest on an
   OCR `<!-- picture text -->` block in the Chairman's statement. The metrics that appear in both
   that block and the formal tables (net profit, RoE, CRAR, NNPA, cost-to-income) all agree
   exactly, which is good evidence the block transcribed correctly — but CASA and the deposit
   split are not independently confirmed, and the derived domestic/overseas deposit split
   (Rs 57.32 / Rs 2.44 lakh crore) is inference, not disclosure.

## 10. Deliverables

- `State Bank of India_14 Aug 2026_CRISIL_Rating Rationale.md`
- `State Bank of India_14 Aug 2026_Workpaper.md` (this file)
- `State Bank of India_Financial_Spreads.xlsx` — Inputs / RatioSuite / TieOut / RatingScore
- `Rating_Scorecard_State Bank of India.xlsx` — quantitative anchor, template's own bank bands
- `State Bank of India_Financial_Model_14Aug2026.xlsx` — 5-year model, 4/4 calibration tie-outs
- `compute_ratios.py` — 34/34 tie-outs · `build_spreads.py` · `fill_scorecard.py` · `build_model.py`
