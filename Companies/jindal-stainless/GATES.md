# Gates: Jindal Stainless Limited - CareEdge rating

OWNS: Companies/jindal-stainless/**

Scope: a complete CareEdge rating on Jindal Stainless Limited (JSL; integrated stainless steel
manufacturer) - ratio engine with tie-outs, ratio Excel, Step 12 5-yr 3-statement model, Step
12b scorecard, and the rationale in CareEdge's published format, passing the delivery gate.
Toolchain: Python 3 with openpyxl and `formulas` (the latter lets the gates EVALUATE the
workbooks rather than merely assert their formulas exist); oracles in `verify_jsl.py`.

Hazards identified at pre-flight, all gated below:
(a) CareEdge ALREADY rates this issuer - its 09-Oct-2025 rationale is in the reference library,
    so under the five-condition amendment the rated-amount table MAY be imported verbatim,
    dated and labelled. This is a REAFFIRMATION-shaped case, not a fresh assignment;
(b) FOUR other "Jindal ..." entities sit in the same libraries (Jindal Steel, Jindal Saw,
    Jindal Poly Films, Jindal Drilling) - none of their amounts may be imported as JSL's;
(c) the aggregate-note contaminant probe fires heavily on this issuer - forex both ways,
    exceptional items, asset-sale gain/loss, impairment, interest/dividend income. Every one
    gets a written include/exclude decision BEFORE PBILDT is built (failure mode 36 applied at
    build time, not retrofitted);
(d) the auto-picked Step 4 peer (Suzlon Energy) is the wrong sector and was discarded;
(e) a capacity-utilisation conflict (5% newest vs 60% older) had to be resolved by reading
    context, not by mechanically preferring the newest number - the 5% was a mis-parsed
    fragment, and the real capacity picture (3 MTPA India + 1.2 MTPA Indonesia = 4.2 MTPA) is
    taken from the AR's own narrative.

- [x] G1: routing verified - CareEdge Manufacturing Companies criteria plus the non-financial
      Financial Ratios and Liquidity Analysis criteria, and NO other agency's methodology
  CHECK: python verify_jsl.py routing
  EXPECT: ROUTING VERIFIED
  EVIDENCE: exit=0; output=ROUTING VERIFIED (26-Aug-2026). Confirms the CareEdge methodology
  library exists, contains the Manufacturing and Financial Ratios criteria, that the rationale
  names all three applicable criteria with vintage, and that it cites no ICRA or CRISIL
  methodology (AGENCIES.md forbids applying one agency's methodology text to another's report).

- [x] G2: the same-issuer CareEdge rated-amount table is imported verbatim with all five
      amendment conditions satisfied, and NO amount from a different "Jindal ..." entity
      appears
  CHECK: python verify_jsl.py rated_amounts
  EXPECT: RATED AMOUNTS SOUND
  EVIDENCE: exit=0; output=RATED AMOUNTS SOUND (26-Aug-2026). All four published lines present
  verbatim (5,900.00 / 11,000.00 / 99.00 / 1,000.00); line integrity verified against the
  published total of 17,999.00; publication date 09-Oct-2025 stamped; labelled CRA-published
  rather than issuer-confirmed; the limits-vs-drawn-debt distinction stated with both figures
  (17,999.00 of limits against 7,460.33 of drawn debt); and none of the four wrong-entity
  names appears anywhere in the report.

- [x] G2C: the rated-amounts oracle REJECTS a report importing a wrong-entity amount
  CHECK: python verify_jsl.py rated_amounts --control
  EXPECT: CONTROL OK
  EVIDENCE: exit=0; output=CONTROL OK - oracle rejected the injected break (1 finding).
  The control injects "13,750.00 (Jindal Steel)" into the long-term bank facilities row by
  REGEX on the row rather than by exact-string replacement, and asserts the substitution
  count is 1 before testing - the Balkrishna control twice decayed into a silent no-op when
  surrounding prose changed, and reported success while injecting nothing.

- [x] G3: the ratio engine runs and every tie-out reconciles
  CHECK: python compute_ratios.py
  EXPECT: /\b(\d+)\/\1 (tie-outs |checks )?reconcile/
  EVIDENCE: exit=0; output ends "26/26 tie-outs reconcile" (26-Aug-2026, after correction #2 below). This gate did real
  work rather than rubber-stamping: the FIRST engine failed the balance-sheet tie in ALL FOUR
  years, on four separate genuine errors, each fixed against the source rather than tuned away:
    (a) FY2023 total equity entered as 11,931.18 vs the AR's 11,967.57 - non-controlling
        interest of 36.39 dropped;
    (b) FY2024 non-current assets typed as 15,934.24 while the file's OWN components summed to
        16,034.64 - a 100.40 transcription error only a component-level check can see;
    (c) FY2025 non-current assets typed as 19,359.71 vs components at 19,359.74, previously
        written up as a "0.03 rounding difference between documents" - that write-up was false;
        it was arithmetic, not the documents, and the false disclosure is withdrawn;
    (d) FY2025/26 current provisions read off a garbled table fragment as 66.55 and 60.67
        against true figures of 6.65 and 6.07 - a factor-of-ten misread that the AR's own
        current-liability totals (13,242.81 / 13,987.64) expose exactly.
  The engine was restructured so NO subtotal is hard-coded: every total is summed from its
  components and compared against the AR's printed row, making a component-vs-total
  disagreement structurally impossible to reintroduce.
  A FIFTH error was caught by reading note 39/40 rather than by the tie-out: the FY2025 7.06
  crore Jindal Coke stake loss and the FY2026 17.40 crore Ind AS 103 gain both sit INSIDE
  exceptional items, which the PBILDT base already excludes - adding them back double-counted
  and had overstated FY2025 PBILDT by 7.06 crore.
  The suite now reproduces the company's OWN published figures exactly on four independent
  bridges: the AR's own EBITDA line (FY2025 4,666.63; FY2026 5,560.43, to the paisa), the
  older AR's capital-management EBITDA once the associate share and exceptional item are
  bridged back (FY2023 3,696.05; FY2024 4,856.57), total borrowings excluding leases
  (FY2023 3,871.43; FY2024 5,948.19) and the company's own debt-equity ratio (32.35% /
  41.38%). Reproducing a published ratio on the company's own definition is what proves the
  extraction (failure mode 32).

- [x] G4: the ratio Excel exists, carries its four tabs, every TieOut row passes, and its LIVE
      formulas reproduce the Python engine
  CHECK: python verify_jsl.py spreads
  EXPECT: SPREADS OK
  EVIDENCE: exit=0; output=SPREADS OK (26-Aug-2026). The gate EVALUATES the workbook with
  `formulas` rather than asserting formulas exist: all four tabs present, every TieOut verdict
  cell computes to PASS, and the workbook's own PBILDT formula reproduces compute_ratios.py in
  all four years to within 0.01. Evaluation also caught a real defect at build time - four
  Source-column notes began with "=" and Excel parsed them as broken formulas.

- [x] G5: Step 12 satisfied - a 5-yr 3-statement model with debt DERIVED from the funding gap,
      no error cells, and non-zero projected finance costs
  CHECK: python verify_jsl.py step12
  EXPECT: STEP 12 SATISFIED
  EVIDENCE: exit=0; output=STEP 12 SATISFIED (26-Aug-2026). Six tabs present; zero cells
  resolve to an Excel error; closing debt in every projected column is a live MAX() formula,
  not a typed input. Two real defects were caught here and fixed, not asserted away:
    (i) the first build hard-coded the two Balance_Sheet rows that P_and_L references; a
        section header shifted the sheet by one, and PROJECTED FINANCE COSTS CAME OUT ZERO for
        all five years while the model looked entirely plausible. Row anchors are now
        module-level constants used by both builders, build_bs asserts it wrote to them, and
        this gate independently asserts finance costs are positive in every projected year;
    (ii) PBILDT-per-tonne divided by sales volume, which the company discloses only from
        FY2025, returning #DIV/0! for FY2023-24. Now guarded to report "n/a - volume not
        disclosed" rather than an error, and never back-filled with an estimate.
  Base case: debt peaks at ~7,815 crore in FY2027 and falls to nil by FY2031; gearing 0.42x ->
  0.00x; interest coverage 9.81x -> guarded n/m. Capex was raised from an initial 3,200 crore
  taper to 4,000 crore starting at the FY2026 actual run-rate (~4,226 crore, implied by the
  net-block roll-forward), because the lower figure manufactured a deleveraging that the
  company's own 3.5 MTPA growth ambition contradicts.

- [x] G6: Step 12b satisfied - a filled Rating_Scorecard carrying an anchor grade, disclosed
      in the rationale
  CHECK: python verify_jsl.py step12b
  EXPECT: STEP 12B SATISFIED
  EVIDENCE: exit=0; output=STEP 12B SATISFIED (26-Aug-2026). Rating!C12 = "AA", read back
  through the template's OWN Inputs -> Ratios -> Scorecard -> Rating chain (sector = Iron &
  Steel / Metals / Mining, base 4; business 2; management 2; support notch 0; liquidity
  Strong). The anchor is LEVEL with the assigned rating, so there is no divergence to resolve,
  and the rationale states it.

- [x] G7: the rationale passes the delivery gate with no mandatory section missing and no
      quality probe firing
  CHECK: python verify_jsl.py gate
  EXPECT: DELIVERY GATE CLEAN
  EVIDENCE: exit=0; output=DELIVERY GATE CLEAN (26-Aug-2026). check_sections.py returns [PASS]
  with all quality probes clean. Two probes fired on the first draft and both were genuine:
    (i) failure mode 20 - the draft claimed instrument details were "not disclosed in the
        company's own documents". THE SEARCH PROVED OTHERWISE: `INE[0-9A-Z]{9,10}` returns
        seven hits across three annual reports, and the FY2025-26 AR records the redemption of
        1,875 NCDs (Rs 187.50 crore) under ISIN INE220G07119. Annexure-1 now carries the
        evidenced detail and the arithmetic closes (2,865 less 1,875 = the 990 outstanding);
    (ii) failure mode 14 - the CRA publication date was not adjacent to the CRA-published
        label. Fixed in the report by moving the date beside the label, NOT by loosening the
        200-character window, which is a reasonable requirement.
  Two genuine false positives in the probe itself were fixed and re-verified (see the
  toolchain note at the end).

- [x] G8: the operating-profit build states its forex / exceptional / one-off treatment
      explicitly, applied FROM THE START rather than retrofitted
  CHECK: python verify_jsl.py opm_normalisation
  EXPECT: OPM NORMALISATION VERIFIED
  EVIDENCE: exit=0; output=OPM NORMALISATION VERIFIED (26-Aug-2026). The rationale names the
  forex treatment, quantifies BOTH sides of the swing (87.15 loss FY2026 / 70.04 gain FY2025),
  quantifies the asset-disposal adjustment (11.61), states that exceptional items are excluded
  by construction, and states explicitly that the Jindal Coke and Ind AS 103 items are NOT
  added back a second time.

- [x] G8C: the normalisation oracle REJECTS a report with the treatment paragraph removed
  CHECK: python verify_jsl.py opm_normalisation --control
  EXPECT: CONTROL OK
  EVIDENCE: exit=0; output=CONTROL OK - oracle rejected the injected break (4 findings). The
  control strips the whole computation-basis paragraph while LEAVING the margin figures in
  place, which is exactly the shape of the Balkrishna failure, and asserts the substitution
  happened before testing.

- [x] G9: the sector-defining metric set is present with numbers, and the capacity conflict
      flagged at pre-flight is resolved and explained rather than silently picked
  CHECK: python verify_jsl.py sector_metrics
  EXPECT: SECTOR METRICS PRESENT
  EVIDENCE: exit=0; output=SECTOR METRICS PRESENT (26-Aug-2026). Sales volume 2.57 MT, PBILDT
  per tonne as a dated SERIES (19,927 FY2025 -> 21,681 FY2026) rather than a snapshot,
  realisation, group melting capacity 4.2 MTPA WITH its 3 MTPA India / 1.2 MTPA Indonesia
  split, and the company's own 3.5 MTPA aspiration. The per-tonne figure independently
  corroborates CareEdge's own published "~Rs 20,000 per tonne" benchmark for FY2022-FY2025,
  which is a useful external check on the PBILDT convention.

- [x] G10: the rating view is defensible - a judgement no command can decide
  EVIDENCE: assigned CARE AA; Stable / CARE A1+. Formed from the metrics before the peer
  conclusion was weighed: PBILDT margin 12.97% and rising, PBILDT per tonne rising, gearing
  0.42x, total debt/PBILDT 1.34x, net debt/PBILDT 0.81x, interest coverage 9.81x, RoCE 21.43%,
  liquidity Strong on Rs 2,931.60 crore of verified-unencumbered assets, and a funding-gap
  model that deleverages. The scorecard anchor independently returns AA. HONEST DISCLOSURE OF
  A CONTAMINATION RISK: CareEdge's own conclusion (CARE AA; Stable) was necessarily seen at
  Step 7b, because failure mode 29 requires the rated-amount table to be extracted from the
  same-issuer rationale BEFORE drafting, and the grade sits in the same table. The view is not
  independent of that knowledge in the strict sense; what can be said is that the quantitative
  anchor was computed from the audited financials alone and returned the same grade, and that
  the ratio suite would not support a different one.

## Toolchain fixes made during this case (verified, not asserted)

Two genuine FALSE POSITIVES in the shared delivery gate were found by this case and fixed at
source, because a checker that rejects a correct report trains the reader to ignore it:

1. **FM14 date format.** The probe accepted only "09-Oct-2025" style dates. CareEdge's OWN
   house format is "October 09, 2025" (month first), so every correctly dated CareEdge report
   would have failed forever. Widened to accept day-first, month-first and ISO forms.
2. **FM14 masthead trigger.** The probe triggered on the bare "Press Release" line that opens
   every CareEdge rationale - a masthead, not an attribution - and no date can follow it on
   that line, so the probe was unsatisfiable for the whole format. A standalone masthead line
   is now stripped before the check; "per CareEdge's press release of 09-Oct-2025" is
   untouched, which is the case the probe exists to police.
3. **FM14 direction.** The probe looked only FORWARD for the date. It now looks BOTH WAYS
   within 200 characters, and requires EVERY attribution to be dated rather than just one.

Re-verified after all three changes: the target report passes; a positive control with every
date stripped still fires; and a full-corpus run returns 12 passed / 2 failed - identical to
the pre-change baseline, so no regression.


## Post-delivery correction #2, 26-Aug-2026 - the forex line was the WRONG FIGURE

The operator challenged the Brief Financials table ("I think they might be wrong"). They were.
Re-auditing against the notes rather than reassuring produced two findings.

**1. THE FOREX FIGURES WERE NOT THE P&L LINE AT ALL - they were cash-flow adjustments.**
The engine carried "Forex loss/(gain)" of [-15.57, 32.41, -70.04, 87.15]. Those are the
**"Net unrealised foreign exchange (gain)/loss"** rows from the CASH-FLOW RECONCILIATION,
which capture only the unrealised portion of the result. The actual profit-and-loss line, in
the Other Expenses note (FY2025-26 note 34; FY2023-24 note 33), is a **NET GAIN in all four
years**: 68.48, 190.04, 154.37 and 78.41. FY2026 had been entered as an 87.15 crore LOSS
against an audited 78.41 crore GAIN - wrong in magnitude AND in direction.

Two consequences. First, the add-back logic was built on a false premise: it restored a forex
gain on the theory that it sat in Other Income and had been stripped by the "- other income"
term. It never sat in Other Income - note 29 decomposes Other Income fully and contains no
forex line at all. Since CareEdge treats non-debt forex as operating and the gain already sits
inside Other Expenses, **no add-back is warranted in any year**. Second, the false add-back had
inflated FY2023 PBILDT by 15.57 and FY2025 by 70.04.

Corrected figures: PBILDT FY2025 4,666.63 (was 4,736.67) and FY2026 5,560.43 (was 5,572.04);
margin FY2025 11.87% (was 12.05%) and FY2026 12.94% (was 12.97%); interest coverage FY2025
7.63x (was 7.74x) and FY2026 9.79x (was 9.81x); total debt/PBILDT FY2025 1.37x (was 1.35x);
PBILDT per tonne ~19,630 and ~21,640 (was 19,927 and 21,681). Return on capital employed in
the rationale was also corrected from 21.43% to 19.25%: the 21.43% was the MODEL's
closing-capital-employed measure quoted beside engine figures computed on AVERAGE capital
employed, which was an inconsistent basis rather than a wrong number.

**THE GENERAL LESSON, and why the tie-outs did not catch it:** a cash-flow reconciliation line
and a P&L note line are DIFFERENT MEASURES OF THE SAME ITEM. Only the note states what the P&L
actually booked. Every tie-out still passed throughout, because PBILDT was being tied to the
company's own published EBITDA - and the base reproduces that exactly whether or not a spurious
add-back is applied on top. The tie-outs verified the base; nothing verified the add-back.

**2. FOUR OF THE THEN-22 TIE-OUTS WERE CIRCULAR.** The "EPS" checks compared
`R[p]["EPS (Rs)"]` against `PL["EPS basic (Rs)"]` - the same cell, since the ratio suite reads
EPS straight out of PL. They could never fail, so "22/22 reconcile" overstated how much of the
engine was actually verified. Removed and replaced with two genuinely independent checks per
year, both using separately printed P&L figures:
  * Total income = revenue + other income (43,306.14 = 42,954.66 + 351.48);
  * PAT attribution: owners + non-controlling interest = PAT (3,193.45 + (8.88) = 3,184.57).
Now 26/26, and every one of them compares two independently sourced numbers.

**What did NOT change: the rating.** CARE AA; Stable / CARE A1+ stands. The margin trend still
improves (11.87% -> 12.94%), PBILDT per tonne still rises and still sits above CareEdge's own
~Rs 20,000 benchmark, gearing is untouched at 0.42x, and the scorecard anchor still returns AA.
The forex finding actually strengthens one part of the analysis and weakens another: the
"earnings swung violently in both directions" weakness was FICTION and has been withdrawn, but
the real picture - a persistent net forex GAIN worth up to 4.0% of PBILDT, now less than half
its FY2024 peak - is a more material and more honest disclosure, and the rationale now says so.

## Post-delivery correction #3, 26-Aug-2026 - full figure audit of the report

The operator asked for the remaining numbers to be checked. `audit_figures.py` was written to
do it mechanically: it extracts EVERY numeric token from the rationale and classifies each as
(1) reproducible from the ratio engine, (2) present verbatim in the document set, or (3)
neither - derived or unsourced. Category (3) is then verified by hand, one figure at a time.

**Result: 42 engine-matched, 86 document-matched, 19 requiring explicit verification.**

ONE further real error was found, in the stress case. The rationale asserted the stress would
take total debt/PBILDT to "approximately 1.9 times and interest coverage to approximately 4.1
times". The model's Stress_Case tab computes **1.76x and 7.29x**. The 4.1x had never been
derived from anything at all - it was a naked assertion, and it understated stressed coverage
by nearly half, making the stress look materially worse than the model's own arithmetic shows.
Corrected in the rationale AND in the model's read-across note; the tab itself was right
throughout, so this was purely prose drifting from computation.

Everything else in category (3) verified clean, each recomputed from its components:
  capex ~4,225 cr (18,041.62 - 14,876.46 + 1,060.30) | net block 9,776.21 and 18,041.62 (sum of
  PP&E, CWIP, ROU, investment property) | operating NWC 4,050.81 -> 3,008.34 | unencumbered
  liquid 2,931.60 (2,935.15 - 3.55 under lien) | internal accrual 4,244.87 (3,184.57 + 1,060.30)
  | PBILDT per tonne ~19,630 / ~21,640 | forex as 4.04% and 3.31% of PBILDT | revenue +20.3% |
  the CareEdge rated amounts, verified against the published action rather than the issuer's
  documents (which is why the script cannot see them).
Every ESG and narrative figure spot-checked against the annual report and confirmed: 61.13% of
R&D and 10.69% of capex to environmental/social, 100% sustainable sourcing, 5,303 workforce,
0.72 MT slag capacity under a 15-year Harsco partnership, global melt 64.16 -> 64.35 -> 65.76 MT.

- [x] G11: the stress figures quoted in the rationale match the model's computed Stress_Case tab
  CHECK: python verify_jsl.py step12
  EXPECT: STEP 12 SATISFIED
  EVIDENCE: exit=0 live. POSITIVE CONTROL: reverting the rationale to the old "1.9 / 4.1"
  wording makes the gate emit two precise FAIL lines naming both computed values and exits 1.
  The FIRST version of this check PASSED that control and was therefore worthless - it searched
  the whole document for the substring "1.8"/"7.3", which occur inside unrelated numbers
  ("11.87", "7,460.33", "5,451.81"). Rewritten to scope the search to the stress SENTENCE and
  parse the quoted figures properly. A check that cannot fail its own control is not a check.

- [x] G12: tie-out COVERAGE is measured by mutation, and every input no check is sensitive to
      is declared
  CHECK: python verify_jsl.py coverage
  EXPECT: COVERAGE MEASURED
  EVIDENCE: exit=0; "coverage 98.2%, 5 unverified input(s), all declared" (26-Aug-2026).
  The harness perturbs each of the engine's 278 inputs, re-runs the suite, and reports those
  no tie-out notices. Acting on it took this case from 94.5% to 98.2%: the Other Expenses
  note was decomposed to its 25 line items and TIED to the note's own printed total (7,894.46
  / 6,924.31), and the printed PBT waterfall was tied step by step. The five that remain -
  basic EPS in all four years (no weighted share count in the data) and the FY2024 forex line
  (note 33 not decomposed) - are declared in the engine's UNVERIFIED_INPUTS and feed no ratio.
  TWO POSITIVE CONTROLS, both failing correctly:
    A. drop a declared entry -> "these inputs are verified by NO tie-out and are not declared
       in UNVERIFIED_INPUTS: [('Forex gain in Other Expenses', 'FY2024')]";
    B. declare a stale entry -> "UNVERIFIED_INPUTS declares entries the harness no longer
       reports ... [('PAT', 'FY2026')]".
  The FIRST version of this gate passed its own control: it looked for the input's first word
  somewhere in DISCLOSED_DIFFERENCES, and "eps" still appeared in an unrelated sentence. That
  is the same substring-coincidence failure as the first stress check, in the same session.
  Rewritten to compare SETS.

## Post-delivery correction #4, 26-Aug-2026 - methodology change so this cannot recur

Three operator challenges in a row found real errors that all passing tie-outs had missed. The
common cause was not carelessness in any one number: it was that **nothing measured what the
tie-outs actually covered**. Two failure modes were added to CLAUDE.md, each with mechanical
enforcement, per the section 8a rule that no failure mode may ship as prose:

**Failure mode 38 - a cash-flow reconciliation row is not a P&L line.** Both statements name
the same items; the cash-flow row is the non-cash adjustment bridging PBT to operating cash
flow (for forex, the unrealised slice only), while the note states what the P&L booked.
Enforced by `preflight.py` probe **[0d] SAME ITEM IN TWO STATEMENTS**, which classifies each
parsed table row as cash-flow-shaped or note-shaped and flags items whose amounts do not
intersect. Verified: on this case it prints the 87.15 / 70.04 cash-flow row beside the note's
own figures and names the conflict.

**Failure mode 39 - counting passes is not measuring coverage.** Enforced by the new
`tieout_mutation.py` at the project root, reusable across every case, plus gate G12 above.
The demonstration is decisive: reinstating this case's four circular EPS checks raises the
headline from 26/26 to 30/30 - reading as BETTER verification - while measured coverage does
not move by a single input.

The generalisable rule the exercise produced: **failure mode 36 requires an aggregate note to
be DECOMPOSED; decomposition is not verification. A decomposition must be TIED BACK to the
note's own printed total**, which is what converts every line inside it from a typed number
into a checked one. Both rules are now in the shared `icra-ratio-engine/ratio_template.py`, so
future cases inherit them at the point the engine is first written.

**Corollary, learned twice in one session: a check that cannot fail its own positive control is
not a check.** The stress-consistency gate and the first version of G12 both passed their
controls through substring coincidence and were rewritten until they genuinely failed.

**Finding beyond this case, not acted on here:** running the harness across the corpus shows
**Balkrishna Industries at 13.4% coverage** against its reported "18/18 tie-outs reconcile" -
almost its entire balance sheet is verified by nothing, because that engine hard-codes its
subtotals instead of summing components and tying to the AR's printed total. Flagged for
separate work; the rating there rests on figures that were independently corroborated against
ICRA's published rationale, so this is a verification-coverage gap rather than a known error.
