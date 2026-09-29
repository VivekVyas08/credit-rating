# Independent Audit — Vodafone Idea rating and the two toolchain fixes

## **01 September 2026**

*Scope: the complete output of this working session — the Vodafone Idea Limited rating case, the webapp output-discovery fix, and the scorecard cached-value fix. Every check below was re-run from scratch for this audit; nothing is carried forward from the earlier working notes. Where a result is stated, the command that produced it is named.*

---

## 1. What this audit found, in one paragraph

The Vodafone Idea rating package is sound on its evidence and its arithmetic: 243 of 246 tie-outs reconcile, mutation-measured coverage is 98.4%, all 28 headline claims re-verify against the primary document, and every projection figure quoted reproduces from the model. **Two material defects were found in my own work and corrected during this audit** — the rating action was labelled "assigned" while the report's own tables showed a prior rating and a previous rated amount, and the anchor divergence was overstated as 12 notches when it is 9. Both are now fixed. Three items remain open and are listed at section 7; one of them needs your decision, and the other two pre-date this session.

---

## 2. Verification performed

| # | Check | Command | Result |
|---|---|---|---|
| A1 | Ratio engine reconciles | `python compute_ratios.py` | **243 of 246**, 3 declared acknowledgements |
| A2 | Coverage measured by mutation, not asserted | `python tieout_mutation.py vi` | **98.4%** — 187 inputs perturbed, 184 register on a check |
| A3 | Anchor reproduces offline | `python rate_engine.py vi --engine local` | **B-**, deterministic |
| A4 | Delivery gate | `python check_sections.py "<report>.md"` | **PASS** — all mandatory sections, all quality probes |
| A5 | Headline claims vs the primary document | 28 targeted greps of the FY2025-26 annual report | **28 of 28 present** |
| A6 | Computed-figure drift | Engine re-run against the draft text | **No drift.** Two figures absent are simply not quoted |
| A7 | Derived percentages | 25 recomputations | All reconcile; one corrected earlier in the session (ARPU) |
| A8 | Projection figures | `python forward_model.py` | **6 of 6** reproduce exactly |
| A9 | Subsidiary names in Annexure II | 7 greps of the annual report | **7 of 7 present**, full legal names |
| A10 | Scorecard readable in any viewer | openpyxl `data_only=True` across all workbooks | **13 checked, 0 with blank formula cells** |
| A11 | Webapp fix, on the live server | HTTP GET to `127.0.0.1:5050` | **200**, all 6 Vi outputs listed |
| A12 | No regression in the rating engine | `python test_rate_engine.py` | **all checks passed** |
| A13 | Scorecard inputs unaltered by the recalc | Direct cell read-back | Inputs and qualitative scores unchanged |

---

## 3. Finding 1 — MATERIAL, CORRECTED: the rating action contradicted its own tables

**What was wrong.** The report was headed *"Vodafone Idea Limited: [ICRA]A- (Stable); assigned"*, and the Summary of rating action carried the same word. But the same table showed a **Previous rated amount of Rs. 2,327.00 crore**, and the Rating history section showed an unbroken series — [ICRA]BBB- (Stable) assigned April 2025, upgraded to [ICRA]BBB (Positive) in March 2026, upgraded to [ICRA]A- (Stable) in June 2026.

**Why it matters.** "Assigned" means a first-time rating. A first-time rating cannot have a previous rated amount or a three-year history. The report asserted two incompatible things about its own subject.

**Correction applied.** The action is now **reaffirmed**, which is what it is: the last rating outstanding is [ICRA]A- (Stable) from ICRA's action of 02 June 2026, and this exercise reaches the same level on the same amount. The Summary table now shows Rs. 727.00 crore in both the previous and current columns, consistent with a reaffirmation. ICRA's June action — which both upgraded the rating *and* reduced the amount from Rs. 2,327.00 crore — is reproduced verbatim with its date in the Rating history section, where it belongs, so the five-condition amendment is still satisfied.

**A regression this introduced, and its fix.** The rewrite separated the CRA-attribution phrase from its date, and the failure-mode-14 probe caught it immediately. The date is now stamped beside the attribution. *This is the value of the gate: the correction was itself checked.*

---

## 4. Finding 2 — MATERIAL, CORRECTED: the anchor divergence was overstated

**What was wrong.** The workpaper stated, twice, that the divergence between the scorecard anchor (B-) and the rating view (A-) was **12 notches**. I also reported 12 to you in conversation.

**The correct figure is 9.** On the workbook's own 17-notch scale — AAA, AA+, AA, AA-, A+, A, A-, BBB+, BBB, BBB-, BB+, BB, BB-, B+, B, B- , C — A- is index 6 and B- is index 15. The difference is 9.

**Correction applied.** Both occurrences now read 9 notches and state the index arithmetic so the figure can be checked at a glance.

**Assessment of consequence.** None on the rating. The divergence is far outside the ±2 screening band at either figure, and the resolution — that the whole distance is the support case the scorecard cannot see — is unchanged. But it was a wrong number in a delivered document, and it was wrong in the direction that made my own analysis sound more dramatic.

---

## 5. The Vodafone Idea rating — audit of the conclusion itself

**Rating: [ICRA]A- (Stable), reaffirmed, on Rs. 727.00 crore of long-term fund-based term loans.** No short-term rating; the rated instrument is a term loan.

### The evidence supporting it

| Element | Figure | Verified against |
|---|---|---|
| Interest coverage FY2026 | 0.88 times | Engine; consolidated P&L |
| Total debt / OPBDIT | 10.13 times | Engine |
| Net worth | Negative Rs. 35,758 crore | Consolidated balance sheet |
| Government obligation within total debt | Rs. 1,45,454 crore of Rs. 1,92,528 crore (76%) | Directors' Report, tied to notes 22(B) and 26(B) |
| Payable in the first ten years | Rs. 1,144 crore | Directors' Report |
| Rated instrument as a share of total debt | 0.4% | Computed |
| Unencumbered liquidity | Rs. 3,608 crore | Company's own stated basis |
| Operating cash flow FY2026 | Rs. 19,411 crore | Consolidated cash-flow statement |
| Government shareholding | 49.00% | Note 4, five occurrences |
| Support demonstrated three times | Rs. 16,133 cr (Feb-2023), Rs. 36,950 cr (Apr-2025), AGR cut 27% and deferred | Notes 3 and 4 |

### The audit's view of the judgment

The grade rests on a weak standalone profile lifted by demonstrated Government and promoter support. **That reasoning is defensible and is fully disclosed**, including the constraint that limits it: the 49% holding is deliberately below majority, no management control has been taken, and no debt is guaranteed. The methodology's own footnote 4 — which allows weak metrics to coexist with low assessed credit risk where a strong promoter group will extend distress support — is quoted in the workpaper rather than paraphrased.

**Two features of this case deserve explicit acknowledgement as weaknesses of the conclusion, not strengths:**

1. **The forward model does not show deleveraging.** In the base case total debt rises every year to FY2031 and interest coverage stalls near 1.3 times. In the stress case coverage falls back below 1.0 times by FY2029. The rating is not supported by a projected recovery in the credit metrics; it is supported by the smallness of the rated obligation and by the identity of the principal creditor.
2. **The largest obligation sits outside the forecast window.** Rs. 10,608 crore a year from FY2036 is 37% of base-case FY2031 operating profit. The analysis says so plainly, but no five-year model can test it.

---

## 6. Audit of the two toolchain fixes

### 6.1 Webapp output discovery

**Defect.** Vodafone Idea's rating rationale did not appear in the tool. The case is registered as "Vi" while the deliverable is filed under the legal name; files in the shared project root are matched by name, and "Vi" does not appear in "Vodafone Idea Limited". Separately, `.py` was not a recognised extension, so the ratio engine, forecast model and scorecard builder were invisible for every case.

**Fix and its evidence.** Names are now also derived from the case folder's own deliverables — safe by construction, since a file in the case folder belongs to that case. Regression-tested by snapshotting all 27 cases before and after: **zero outputs lost, and no root file claimed by two different companies.** Vi went from 2 outputs to 6; **SBI's rationale and PDF, which were also missing, are now visible.**

**Two defects in my own fix, both caught by that regression test:** `build_spreads.py` was being labelled "Rating Rationale", and the name derivation was picking up "company context" from `COMPANY_CONTEXT.md`. Both corrected.

### 6.2 Scorecard cached values

**Defect.** openpyxl cannot evaluate formulas, and on save it writes each formula cell as `<f>…</f><v></v>` — formula preserved, cached result empty. Excel hides this by recalculating on load. Nothing else does. **Five workbooks rendered completely blank** in any other viewer — including this project's own webapp preview — from the Ratios sheet down to the final grade.

**Fix and its evidence.** `recalc_workbook.py` evaluates with the same `formulas` engine `rate_engine.py` already uses for its offline anchor, so the values written are by construction the ones the grade is read from, and injects each into the cell's `<v>`. The `<f>` is untouched, so the workbook stays live. **All 10 formula workbooks now fully populated, all structurally valid, and every grade unchanged.**

**Two defects in my own fix, both caught by its built-in verification:** a path join produced `xl/xl/worksheets/…` and wrote nothing; and my "empty cell" test compared strings, which discarded `Rating!C10` — whose legitimate result is the string `"None"`, the workbook's own wording for *no hard caps applied*.

### 6.3 A larger defect exposed while adding the guard

Adding a delivery-gate probe for 6.2 required resolving each rationale to its case folder. `check_sections.py` was doing that as `path.parent` — but rationales live in the project root while `case.json` lives in `Companies/<slug>/`. **Every case-level probe below that line has therefore been silently inert on almost every delivered report, including the failure-mode-35 Step 12 check** — the one probe written specifically to stop batch mode dropping the forward view. Fixed by matching the rationale against each case's registered name and aliases. Now live, it immediately surfaces genuine Step 12 gaps on Vedanta/Hindustan Zinc.

---

## 7. Open items

| # | Item | Status |
|---|---|---|
| 1 | **`Companies/sbi/` and `Companies/state-bank-of-india/` are duplicate folders for the same issuer.** The empty July folder wins the name match over the August folder that holds all the deliverables, producing a false Step 12 warning. | **Needs your decision.** Deleting the empty duplicate clears it. Not actioned — removing a case folder is not mine to do. |
| 2 | Dhampur Bio Organics and IIFL Finance fail on mandatory sections | **Pre-existing**, unrelated to this session |
| 3 | `Companies/vi/RATING_REQUEST.md` was auto-deleted by the webapp's self-heal once the fix made the rationale visible to the case. This is the designed behaviour, but it removed the delivery annotation written into that file. | **Noted.** The case still shows as delivered because the rationale is found. |

---

## 8. Limitations of the work itself, restated

These were disclosed in the deliverables and are repeated here so the audit does not read as an unqualified pass.

1. **Step 13/14 independence was partially compromised.** Failure mode 29 requires extracting the rated-amount table before drafting; on this case that table sits at the top of the same file as ICRA's rationale, so opening it exposed ICRA's opening reasoning before the qualitative view was written down. The entire quantitative view — engine, tie-outs, operating metrics, forward model, scorecard — was fixed in code beforehand. Recorded in the workpaper at section 14.
2. **One figure comes only from ICRA's publication.** The Rs. 25,000 crore term debt / Rs. 10,000 crore non-fund-based funding split is not in the issuer's documents — searched for "25,000", "25000", "non-fund based facility" and "term debt" across the annual report and all four quarterly presentations. It is attributed in the report, not presented as issuer-disclosed.
3. **Three of 187 engine inputs are covered by no check** — the Q4 FY2026 customer ARPU and two data-usage figures. They are corroborated as present in the source, but corroboration cannot distinguish a mis-transcription when the mutated value also happens to appear in a 443,000-word document set. Named in the engine's own disclosures.
4. **No filing after 31 March 2026 was supplied.** The DoT letter finalising the AGR dues is dated 30 April 2026 and is inside the annual report, but no bring-down check beyond the audited year-end was possible.
5. **The scorecard mis-scores a negative-net-worth issuer on two inputs.** Gearing computes to −4.5 times and scores 1 — "strongest" — because a negative denominator inverts the ratio. The hard cap on negative net worth is what produces the correct B- anchor. The report marks gearing and TOL/TNW as not meaningful for exactly this reason.

---

## 9. Conclusion

The rating package is fit to go forward to the Reviewer and Rating Committee stages, which have not been performed — under the governance overlay the grade is a committee decision and what exists today is the analyst's proposed view. The two material defects found in this audit were in the report's framing and in a stated notch count, not in its evidence or its arithmetic; both are corrected. The two toolchain fixes are verified on the live server and across all thirteen scorecards, and each was regression-tested against the specific failure it could have introduced.

**The most useful thing this audit produced is not in the rating at all.** It is the discovery that a delivery-gate probe had been inert for months on the files it was written to police, because of a single line resolving a directory. That is worth more attention than either of the defects it was looking for.

---

*Prepared as an analytical exercise. Not an official ICRA publication and not a rating assigned by ICRA Limited. Data cut-off for the underlying case: 31 March 2026 (audited).*
