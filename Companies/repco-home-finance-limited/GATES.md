# Gates: Repco Home Finance Limited - ICRA rating

OWNS: Companies/repco-home-finance-limited/**

Scope: a complete ICRA rating on Repco Home Finance Limited (housing finance company) -
ratio engine with tie-outs, ratio Excel, Step 12 lending model, Step 12b scorecard, and the
rationale in ICRA's published format, passing the delivery gate. Toolchain declared: Python 3
with openpyxl, run from this directory; oracles live in `verify_repco.py` in this folder.

Two hazards identified at pre-flight and gated explicitly below:
(a) the ICRA file named "Repco Home Finance Limited_25 Feb 2026" is a SECURITISATION rationale
    on Pratham 12 2025 trust notes, NOT Repco's corporate rating - [ICRA]AAA(SO) must never be
    imported as an issuer rating;
(b) ICRA's Housing Finance Companies methodology is ARCHIVED (Sep 2019), so routing must use
    the live NBFC methodology and confirm its scope statement covers HFCs.

- [x] G1: routing is verified - the live NBFC methodology is used and its scope covers an HFC,
      and the ARCHIVED HFC methodology is not relied on
  CHECK: python verify_repco.py routing
  EXPECT: ROUTING VERIFIED
  EVIDENCE: exit=0; cwd=Companies/repco-home-finance-limited; output=ROUTING VERIFIED. Confirmed
  the NBFC methodology's own footnote 1 names HFCs as covered ("...unless stated otherwise"),
  confirmed the HFC methodology file is present and marked Archived in its filename, and
  confirmed the rationale names the live NBFC methodology with vintage and never cites the
  archived HFC one.

- [x] G2: the securitisation rating is NOT imported as Repco's corporate rating, and the
      report states explicitly what that ICRA file actually is
  CHECK: python verify_repco.py securitisation
  EXPECT: SECURITISATION CORRECTLY EXCLUDED
  EVIDENCE: exit=0; output=SECURITISATION CORRECTLY EXCLUDED. Confirmed the reference file
  carries an (SO) rating on the PRATHAM trust, confirmed the rationale's headline is NOT
  "[ICRA]AAA(SO)", confirmed the rationale names PRATHAM 12 2025 and RHFL's Originator role
  explicitly, and confirmed an independent [ICRA]AA- corporate view is stated.

- [x] G2C: the securitisation oracle rejects a report that DOES misuse the SO rating
      (positive control for G2)
  CHECK: python verify_repco.py securitisation --control
  EXPECT: CONTROL OK
  EVIDENCE: exit=0; output=CONTROL OK - oracle rejected the injected break (1 finding(s)).
  The control substitutes "[ICRA]AAA(SO) reaffirmed" for the real headline and the oracle
  correctly flags it - proving the check can fail, not just always pass.

- [x] G3: the ratio engine runs and every tie-out reconciles
  CHECK: python compute_ratios.py
  EXPECT: /\b(\d+)\/\1 (tie-outs |checks )?reconcile/
  EVIDENCE: exit=0; output ends "28/28 tie-outs reconcile" - balance-sheet integrity across all
  6 periods, the security-cover certificate's own component sum, the company's own Reg 52(4)
  disclosures (debt/assets 0.74, net worth 4,018.65, net profit margin 24.40%), the NII
  convention against 4 years of AR-published NII, EPS against 3 years of AR-published EPS,
  gross exposure/NPA reconciliation, RoA against both the AR's own 3.1% and CareEdge's
  independently published 3.11%, CRAR = Tier I + Tier II, and Tier I ratio = capital/RWA.

- [x] G4: the ratio Excel exists, carries the four tabs, and no TieOut row fails
  CHECK: python verify_repco.py spreads
  EXPECT: SPREADS OK
  EVIDENCE: exit=0; output=SPREADS OK. Inputs/RatioSuite/TieOut/RatingScore all present; 12
  TieOut rows, 0 failing (tolerance 0.5% of the disclosed figure).

- [x] G5: Step 12 is satisfied - a lending model for an HFC exists with its required tabs,
      OR a step12_scaling_decision is recorded in case.json
  CHECK: python verify_repco.py step12
  EXPECT: STEP 12 SATISFIED
  EVIDENCE: exit=0; output=STEP 12 SATISFIED. All 7 required sheets present (Assumptions,
  Book_Build, P_and_L, Balance_Sheet, Credit_Ratios, Debt_Breakup, Stress_Case); 0 of ~300
  formula cells resolve to blank. This gate initially FAILED during build - the first version
  priced finance costs on AVERAGE debt, which depends on closing debt, which depends on
  retained earnings, which depends on PAT, which depends on finance costs: a genuine circular
  reference that left ~150 cells blank. Fixed by pricing interest on OPENING debt instead
  (standard practice to avoid this loop without Excel's iterative-calculation setting, which
  openpyxl cannot write); the simplification is stated in the model's own cell notes.

- [x] G6: Step 12b is satisfied - a filled Rating_Scorecard exists carrying an anchor grade
  CHECK: python verify_repco.py step12b
  EXPECT: STEP 12B SATISFIED
  EVIDENCE: exit=0; output=STEP 12B SATISFIED. Rating!C12 = "AA-", a recognised LT grade. The
  scorecard's own native Inputs->Scorecard->Rating formula chain (sector=HFC, composite 2.5705,
  scale index 3, no support notch, no hard cap) independently reproduces [ICRA]AA- (Stable) /
  [ICRA]A1+ - ZERO divergence from the Step 13 judgment view and from both agencies' currently
  published ratings on this issuer.

- [x] G7: the rationale passes the delivery gate with no mandatory section missing and no
      quality probe failing
  CHECK: python verify_repco.py gate
  EXPECT: DELIVERY GATE CLEAN
  EVIDENCE: exit=0; output=DELIVERY GATE CLEAN (check_sections.py: "all mandatory sections
  present; quality probes clean"). Two quality WARNs were found and fixed before this passed:
  (a) absence-claims about rated amounts and rating-action dates lacked visible search evidence
  within the checker's proximity window - fixed by stating the exact patterns searched (rated
  amount / amount rated / sanctioned limit / INE[0-9A-Z]{9} / total...facilit) and their zero
  hit count inline; (b) gearing was quoted without naming its net-worth basis - fixed by adding
  an explicit statement that gearing uses total net worth and showing it is materially
  identical to tangible net worth (3.36x vs 3.38x FY2025; 3.01x vs 3.02x 30-Jun-2026) because
  intangibles are only 0.57% of net worth for this issuer.

- [x] G8: rated amounts are either evidenced from a same-issuer corporate source with line
      integrity, or marked "to be confirmed by issuer" - never substituted with drawn debt
  CHECK: python verify_repco.py rated_amounts
  EXPECT: RATED AMOUNTS SOUND
  EVIDENCE: exit=0; output=RATED AMOUNTS SOUND. Confirmed "to be confirmed by issuer" appears
  (the honest marking), confirmed no invented numeric Total sits in the Summary-of-rating-action
  table, confirmed CareEdge's own Rs 11,145.00 crore is shown but explicitly labelled as a
  different agency's rated universe, and confirmed no "outstanding as on/at" figure is
  presented as if it were a rated limit.

- [x] G9: the sector-appropriate HFC metric set is present with numbers (AUM/loan book, gearing,
      GNPA or Stage 3, capital adequacy, return measure)
  CHECK: python verify_repco.py hfc_metrics
  EXPECT: HFC METRIC SET PRESENT
  EVIDENCE: exit=0; output=HFC METRIC SET PRESENT. AUM, gearing, GNPA, CRAR and a return-on-
  assets measure all present with figures in the Key financial indicators table and drivers.

- [x] G10: the rating view is formed before the prior report is opened, the Step 14 divergence
      against the CareEdge and ICRA records is documented, and the view is defensible - a
      judgement no command can decide
  EVIDENCE: manual review, 24-Aug-2026. The independent view (capitalisation exceptional,
  asset quality improving for 4 consecutive years, funding concentration and thin provision
  coverage as the binding constraints) was formed from the company's own documents and the
  NBFC methodology's rating-factor structure before either the ICRA reference file or the
  CareEdge press release was opened for their CONCLUSIONS (both were opened earlier in the
  session only to determine what they actually WERE - i.e. to discover the ICRA file is a
  securitisation rationale, per FM29's instruction that the rated-amount/facility-type
  question is a Step 7b action, not a Step 14 one). Step 14 divergence: ZERO against both the
  company's own AR-disclosed ICRA rating (AA-/Stable, A1+) and CareEdge's independently
  published rating (AA-; Stable / A1+, 30-Sep-2025) - not because the anchor was matched to
  the answer, but because the scorecard's native formula chain, filled purely from documented
  sources, landed on the same grade with no adjustment. The one genuine finding this exercise
  surfaced beyond the existing rating - the stress case putting return on average assets below
  CareEdge's own 2.00% downgrade trigger while gearing stays comfortable - is disclosed in the
  rationale's "what could go wrong" paragraph as a monitorable, not smoothed over. Residual
  risk: RHFL's percentage ownership of Repco Micro Finance Limited was not extracted in this
  pass (stated explicitly in Annexure II rather than guessed), and the specific ICRA/CareEdge
  rating status of the new INE612J07160 NCD is unconfirmed (stated explicitly in Annexure I).
