# SESSION HANDOFF — read this first in a new session
*Updated 18-Jul-2026 (v1.2 process-governance redesign + IIFL case delivered). Verified against disk.*

## 1. Start the new session with THIS message

> Read `UNIFIED_RATING_GUIDE.md` (now v1.2 — 8 phases, rules R1–R16), `CLAUDE.md` (§6 governance overlay reconciled), `AGENCIES.md` and this `SESSION_HANDOFF.md` at the project root, then confirm you understand: (a) the ONE flow, now with a **Rating-Committee decision (Steps 17b/17c)** and **surveillance (Phase 8)** — the operator proposes/confirms inputs but does NOT set the grade; (b) the data rule (company documents only; CRA reports/actions reference-only); (c) **basis is methodology-determined, not an operator choice (R12)**; (d) the open items in §5. Then wait for my instruction.

Everything below is on disk — nothing depends on the previous chat.

## 0. WHAT HAPPENED THIS SESSION (17–18 Jul 2026) — the delta since the 16-Jul state

1. **IIFL Finance rating DELIVERED** (CareEdge · **NBFC** · **standalone** · all debt). Sector was mis-set to "Bank" at intake → corrected to NBFC (verified from the FY26 AR). Outcome (analyst view): **CARE AA; Stable** (NCDs/sub-debt/bank facilities) · **CARE AA-; Stable** (Perpetual Debt, Tier-1, notched −1) · **CARE PP-MLD AA; Stable** · **CARE A1+** (CP). Scorecard **anchor = CARE A+** (2 notches below — divergence explained, non-binding). Files at project root + `Companies/iifl/`: rationale (`IIFL Finance Limited_17 Jul 2026_CARE_Rating Rationale.md`), workpaper, `compute_ratios.py`, `IIFL_Financial_Spreads.xlsx`, `Rating_Scorecard_IIFL_Finance.xlsx`, `IIFL_Finance_5yr_Model.xlsx`.
2. **PROCESS REDESIGN → guide v1.2** after a credit-rating-head audit of the flow itself: added **R12–R16**, **§0A roles/engagement-types**, **Reviewer + Rating Committee (17b/17c)**, **issuer review (18b)**, **surveillance (Phase 8, Steps 20–21)**; basis methodology-determined; materiality defined; anchor governed; entity-appropriate ratio tracks & tie-out (screener not universal); proportionate modelling; structured ESG; outlook-vs-watch; peer SET (2–3). **CLAUDE.md §6 reconciled** to match (governance overlay). The two governing files now agree.
3. **New Step-5 deliverable rule:** immediately after reading the AR, GENERATE `<Co>_Financial_Spreads.xlsx` FROM the script (Extraction + RatioSuite + TieOut tabs) — the script stays source of truth (R6), Excel is the review/feed layer.
4. **Scorecard/xlsx RENDER FIX** (was shipping blank cells): fill inputs → compute every formula with the `formulas` package → write results back as **literal values** → verify with `load_workbook(..., data_only=True)` (0 formula-only cells). This is now the standard; `formulas.write()` mangles sheet names — do not use it.
5. **SCORECARD BACK-TESTED & CALIBRATED (18-Jul-2026).** 396 ICRA-rated issuers + JSW/IIFL fully-scored cases. Baseline anchor was **+2.13 notches too low** — cause was the **composite→grade map** (too harsh in the IG zone), NOT the financial bands. Applied to the master: map → range-preserving power **p=1.4** (bias→+0.13, verified via the `formulas` engine); new **`Ref_Qualitative`** rubric sheet (item #4); mandatory **support-notch discipline** in README/Inputs. **±1/80% shown unreachable from financials alone** (Spearman 0.32) — anchor re-scoped to a zero-biased **±2 screening band**. Open items #1 and #4 closed. Report: `Scorecard_Backtest_Report_18Jul2026.md`.

## 2. What this project is

A credit-rating agent producing **ICRA / CRISIL / CareEdge**-style rating rationales from a company's own documents, with a 5-year forecast model and a scorecard anchor.

**Read in this order:**

| File | Role |
|---|---|
| `CLAUDE.md` | **The law.** SOP + **§6 governance overlay** (roles, committee, surveillance, R12–R16), failure modes 1–15, response protocol. Wins on any conflict. |
| `UNIFIED_RATING_GUIDE.md` | **The process you follow — v1.2.** ONE flow, **8 phases**, rules **R1–R16** · §0A roles/engagement-types · §1 agency quick-reference · §2 the flow (analytical 1–19 + decision 17b/17c + issuer 18b + surveillance 20/21) · §4 failure modes · §5 lessons. |
| `Knowledge Base/` (00–06) | **ONE knowledge base — every file covers all three agencies.** |
| `AGENCIES.md` | Folder layout, agency conventions, scorecard/forecast rules. |

## 3. The rules that matter most (full text: UNIFIED_RATING_GUIDE §0 R1–R16)

1. **Company documents are the ONLY data source.** screener.in / web = **cross-check only** (verify a figure already extracted from the AR, or labelled market context) — never a source of a report figure. **AR wins on disagreement.**
2. **All three agencies' reference rationales AND published rating actions are craft/context ONLY** — never a source of any figure, not even attributed. *(User directive 14-Jul-2026; the old "carry from the CRA record, attributed" allowance is WITHDRAWN.)*
3. **Undisclosed amounts** (CP-programme / bank-facility limits) = **"to be confirmed by issuer"** — never reconstructed. *A total that ties while individual lines are wrong is still wrong.*
4. **Rated LIMITS ≠ drawn BORROWINGS** — state both; reconcile at component level (LT/ST/leases) vs the AR **and** screener.in.
5. **Never mix computation bases in one ratio row** — show each labelled, defined once in a "Basis of preparation" note.
6. **Every step has a stop-and-ask gate — ask, then WAIT.** Never assume the answer.
7. **Form the rating view BEFORE opening the prior report** (Step 13 before Step 14) — *relaxed for surveillance engagements, where the prior rating IS the anchor.*
8. **Deliver model + scorecard + Financial_Spreads .xlsx WITH written reasoning** — never a bare file; render-verify every workbook.
9. **When challenged ("are you sure?") — re-audit against the sources and report what failed. Never reassure without re-checking.**
10. **(R12) Basis is METHODOLOGY-determined, not an operator choice.** Operator's alternate basis = labelled supplementary view only.
11. **(R13) Materiality is defined:** ≥1% TNW / ≥5% PBT / plausible ≥1-notch / any regulatory-governance-default item regardless of size.
12. **(R14) The rating is a Rating-COMMITTEE decision** on the complete re-verified package (Steps 17b Reviewer → 17c Committee + minutes). Step 15 = analyst's *proposed* view, not approval. Operator/issuer never set the grade.
13. **(R15) Every rating carries surveillance + an engagement type** (new/surveillance/event/withdrawal/provisional/INC — declared at Step 1). Delivery sets up monitoring, doesn't "close the file".
14. **(R16) Independence/conflict/confidentiality:** operator ≠ decision-maker; rating is UPSI until published; invoke policies 129/136/68.

## 4. Current state (verified on disk; counts 16-Jul, process v1.2 + IIFL 18-Jul-2026)

- **Knowledge Base UNIFIED** — every file covers all three agencies:
  - `01` = all three methodology libraries (ICRA 120 · CRISIL 20 consolidated masters · CareEdge 73 papers) + how each is structured + gaps.
  - `02` = **Part A** sector→methodology for all three side by side (incl. insurance / infra / structured / public finance); **Part B** empirical, **pivoted by company: 1,220 companies, 320 covered by 2+ agencies**.
  - `03` = three house styles side by side. `04` = three analytical frameworks side by side. `05` = SOP + all logged lessons. `06` = craft library (ICRA-built, cross-agency ring-fenced).
  - Per-agency KBs were archived, then deleted 01-Sep-2026 as unused (nothing read them) — **do not recreate them.**
- **Libraries:** ICRA 120 methodologies / 649 reference reports · CRISIL 20 / 613 · CareEdge 73 / 803.
- **KB audit + corpus dedupe (16-Jul-2026):** a full KB audit fixed 6 issues (the withdrawn "carry from CRA record, attributed" wording in `05`; "655"→654 report count; a dangling `PROCESS AMENDMENTS` cross-ref; spurious Part-B sector tags; a CareEdge apostrophe-glyph filename mismatch) and de-duplicated the corpus: **3 byte-identical ICRA methodology copies removed + `418` renamed → 123→120**; **5 content-identical ICRA reference reports removed (`Rationale-…`/`(1)` twins of clean dated reports) → 654→649** (CRISIL 613 / CareEdge 803 were already clean); **`02` Part B merged 24 name-variant/duplicate rows → 1,244→1,220 companies, 305→320 multi-agency**. All counts above reconcile to disk; the new figures are propagated across `00`–`06`, `UNIFIED_RATING_GUIDE.md`, `AGENCIES.md` and this file.
- **Tools:** `Rating_Scorecard.xlsx` (root; agency + sector dropdowns, 22 sectors incl. Bank/NBFC/HFC — **insurers not covered**; **composite→grade map BACK-TESTED & calibrated 18-Jul-2026 (power p=1.4, zero bias) + new `Ref_Qualitative` rubric sheet** — §5 #1/#4; financial bands intentionally left as-is). Anchor = zero-biased **±2 screening band**, not a point grade. Forecasting is now **proportionate** (Step 12): full 5-yr model for corporates; an **NBFC lending model** for financial-sector (the corporate 3-statement template doesn't fit a lender — hand-built for IIFL); light sensitivity for CP-only/INC/surveillance. Credit-Ratios + Debt-Breakup tabs still mandatory where a model is built.
- **Web app:** `Start-ICRA-Rating-App.bat` → http://localhost:5050. *Run it yourself — if Claude starts it, it dies when the session ends.*
- **Completed cases:** HAL, SBI, ITC (ICRA+CRISIL+CARE), JSW Steel (ICRA 10-Jul; CRISIL 13-Jul), **IIFL Finance (CARE, NBFC, standalone — 17-Jul; full deliverable set incl. Financial_Spreads + scorecard + 5-yr model)**. IIFL request file marked DELIVERED. No other pending requests.
- **IIFL note for the next session:** the assigned **CARE AA** is a *finely-balanced* call the credit-rating-head audit flagged (see §5) — scorecard says A+, and standalone gearing 5.26x / CRAR 17.84% are weaker than the AA peer Manappuram (3.18x / 21.3%); **AA vs AA- is unresolved**. Corrected figures already in the report: standalone GNPA 1.13% / NNPA 0.58% (Note 38A.6), rated total ₹38,660.85 cr (NCD 9,562.92 + CP 5,742.90, no double-count), liquidity 12m-debt ₹15,590 cr / cover 1.48 months.

## 5. OPEN ITEMS — pick up here

| # | Item | What to do |
|---|---|---|
| 1 | ~~**Scorecard UNCALIBRATED**~~ **DONE 18-Jul-2026 — re-scoped, see `Scorecard_Backtest_Report_18Jul2026.md`** | Back-tested on **396 ICRA-rated issuers + JSW/IIFL fully-scored cases**. Finding: baseline anchor **+2.13 notches too low** — NOT the financial bands (proven un-tunable; left as-is) but the **composite→grade map**. Fix applied to `Rating_Scorecard.xlsx`: map → range-preserving power **p=1.4** (bias→+0.13); example issuer now AA (was AA−). **The ±1/80% target is unreachable from financials alone** (Spearman 0.32; isotonic ceiling 47%) — premise of the old item falsified. Anchor now binds as a **zero-biased ±2 screening band** (guide/CLAUDE Step 12b updated). Residual gap is qualitative → item #4 (now done) + support discipline. |
| 2 | **IIFL: AA vs AA- unresolved** *(credit-rating-head finding F1)* | Standalone gearing 5.26x / CRAR 17.84% are weaker than the AA peer Manappuram (3.18x / 21.3%); scorecard says A+; 2-notch analyst override. Decide: hold AA (strengthen the rationale vs the leverage/capital gap) or move to AA-. Also for IIFL: gold-price shock NOT stress-tested (methodology-named variable), ROMA not computed, FY24 AR read only via FY25 comparatives, per-ISIN codes still TBC. |
| 3 | **No ESG overlay in the scorecard** | Agencies embed ESG; the scorecard can't see it. Add a sector-materiality map + a scored adjustment (~0 to +0.5 on the composite). |
| 4 | ~~**Qualitative scores unanchored**~~ **DONE 18-Jul-2026** | Added the **`Ref_Qualitative`** sheet to `Rating_Scorecard.xlsx`: a 1–6 rubric for Industry/Business/Management, one descriptor per level, lifted from ICRA/CRISIL/CareEdge methodology language (R14 reproducibility). *Remaining:* an ESG-materiality overlay (item #3) and back-testing the rubric on more fully-scored cases as they accrue. |
| 5 | **JSW Steel ICRA report (10-Jul) still violates the data rule** | Carries CRA-sourced rated amounts + a "carried from ICRA's public record" note. Strip them; keep AR-sourced NCDs (₹6,750 cr / 6 ISINs); mark CP + bank limits TBC. The 13-Jul CRISIL report is the clean pattern. |
| 6 | **Routing map Part A unreviewed synthesis; PDF→md conversions spot-checked only** | Part A is my mapping (Part B is empirical). ~2,000 md conversions; a 20-file table-fidelity audit would settle it. |
| 7 | **Rating Committee / surveillance are documented but not operationalised** | The v1.2 flow defines Steps 17b/17c (committee+minutes) and Phase 8 (surveillance) — but there's no committee-minutes template, no surveillance tracker/calendar in the web app yet. Build the minutes template + a surveillance register when convenient. |

## 6. Environment quirks that will bite

- **No LibreOffice** → openpyxl saves formulas with NO cached value, so a formulas-only workbook shows **blank cells** in any non-recalc viewer. **THE FIX (now standard):** fill inputs → compute every formula with the `formulas` pip package → write the results back as **LITERAL VALUES** (openpyxl) → verify with `openpyxl.load_workbook(..., data_only=True)` (expect **0 formula-only cells**). **Do NOT use `formulas.ExcelModel().write()`** — it mangles/uppercases sheet names and corrupts the file. Working build scripts from the IIFL case are in `scratchpad/` (`build_scorecard.py`, `build_model.py`, `build_spreads.py`).
- **`formulas` solution key format:** `"'[File_Name.xlsx]SHEETNAME'!CELL"` — the FILENAME keeps its case, the SHEET is UPPERCASED. (Getting this wrong returns None for every cell.)
- **`__pycache__` staleness bit me:** when a builder `importlib`-loads `compute_ratios.py`, a stale `.pyc` can serve OLD values — `rm -rf Companies/<slug>/__pycache__` before rebuilding if numbers look stale.
- **Note/label cells must not start with `=`**; and R-dict values may be strings now (guard `round()` with `isinstance(v,(int,float))`).
- The Windows console is cp1252 — a final `print()` with `—`/`✓`/`₹` crashes with UnicodeEncodeError AFTER the file is already saved (harmless; the workbook is fine — verify separately).
- Heredocs with apostrophes break in bash → write Python to a script file. The user runs the webapp on port 5050 himself — verify with `curl`, don't kill it.

## 7. How to run a rating (short version)

1. Create the case in the web app (company, **agency**, sector) → upload documents → **Request rating**.
2. Say **"process the pending rating requests"**, or paste the case's kickoff prompt into a dedicated session.
3. The agent follows `UNIFIED_RATING_GUIDE.md`, **stopping at every gate to ask you**.
4. Deliverables land in `Companies/<slug>/` + the project root and appear on the case page: rationale · workpaper · 5-yr model .xlsx · scorecard .xlsx · valuation · charts.

## 8. Continuing in Claude Cowork instead of Claude Code

Same folder, same files — nothing is Code-specific about the knowledge. Paste the §1 message as your first message. Set `CLAUDE.md` as the Project Instructions (or just tell the agent to read it). The `.claude/skills/` (icra-rating, icra-doc-extract, icra-ratio-engine, icra-report-skeleton, finance-research) are Claude Code features — in Cowork their content is superseded by `CLAUDE.md` + `UNIFIED_RATING_GUIDE.md`, which are self-contained. **Cowork limitation:** no shell, so the "compute every number in code" rule (R6/Step 5) can't run a Python script — either do the extraction in the Analysis tool if available, or keep rating runs in Claude Code and use Cowork for reading/reviewing.
