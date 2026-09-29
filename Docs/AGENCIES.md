# Multi-agency structure (ICRA · CRISIL · CareEdge)

> **⚑ THE PROCESS IS ONE FILE:** `UNIFIED_RATING_GUIDE.md` (project root) — one flow, all three agencies, stop-and-ask gate at every step. This file explains the folder layout; that file is what you follow.

This project was ICRA-only and is now **multi-agency**. Each rating agency has the same three-part reference layout. ICRA stays at the project root (unchanged, so nothing breaks); CRISIL and CareEdge live in their own top-level folders.

| Agency | Methodology | Reference rationales | Knowledge Base | Long-term scale | Short-term scale |
|---|---|---|---|---|---|
| **ICRA** (default) | `Methodology/` (root) | `Report for Reference/` (root) | **`Knowledge Base/` (root) — SHARED: one KB for all three agencies** | `[ICRA]AAA … [ICRA]D` | `[ICRA]A1+ … A4, D` |
| **CRISIL** | `CRISIL/Methodology/` | `CRISIL/Report for Reference/` | ← the shared root `Knowledge Base/` (per-agency KB archived 14-Jul-2026) | `CRISIL AAA … CRISIL D` | `CRISIL A1+ … A4, D` |
| **CareEdge** | `CareEdge/Methodology/` | `CareEdge/Report for Reference/` | ← the shared root `Knowledge Base/` (per-agency KB archived 14-Jul-2026) | `CARE AAA … CARE D` | `CARE A1+ … A4, D` |

The three agencies use the **same SEBI-standardised rating symbols** (AAA…D, A1+…A4, `+`/`-` modifiers) with different prefixes, so the analytical machinery is shared; what differs per agency is **report format, section order, house style, methodology names/vintages, and the rating-factor framework**.

## How to produce a report in a given agency's style

The anti-hallucination philosophy is unchanged and applies per agency:

1. **Pick the agency** from the user's request ("do a CRISIL rating", "CARE-style rationale"). Default = ICRA if unspecified.
2. **Read that agency's Methodology** (`<Agency>/Methodology/`) — its own rating-factor framework and indicative thresholds. Never apply ICRA's methodology text to a CRISIL/CARE report.
3. **⚑ OPEN A PEER REPORT — SAME AGENCY, SAME SECTOR — BEFORE DRAFTING OR COMPUTING ANYTHING (strengthened 20-Aug-2026).** This rule previously said "learn the format", meaning section order and headings. That reading is too narrow and it failed: the HDFC Securities rationale had the right sections and the wrong *numbers*, because the peer report answers far more than layout. It fixes **(a)** the Brief Financials **row set**, which forks by entity type — of 631 CareEdge reference reports carrying the table, 520 are corporate (PBILDT-based), 49 financial-sector (TNW-based, all 2025+), 19 bank (NIM/GNPA-based); **(b)** the **ratio definitions**, which live in the table footnotes (`*including non-fund-based limits utilised` is the whole of CareEdge's gearing convention); and **(c)** whether the header table states **limits**. `preflight.py` probe **[1b]** now finds the peers automatically and prints their row set and footnotes — read it. *(HDFC Securities, 20-Aug-2026: `Anand Rathi Share and Stock Brokers Limited_06 Jul 2026.md` and `Angel One Limited_03 Jul 2026.md` sat in this library, published six weeks earlier, each carrying the exact required rows — Tangible net worth, Loan book (Margin Trading Facility), Overall gearing*, Cost-to-income, RONW — and the gearing footnote. Neither was opened. All four of failure modes 31–34 would have been prevented by opening either one.)*

3b. **⚑ CareEdge ratio definitions now exist at source (20-Aug-2026).** The corpus is complete at **77/77** against the published site. Before computing any CareEdge ratio, read `CareEdge/CORPORATE_CONVENTIONS.md` for manufacturing/trading/services or `CareEdge/BROKING_CONVENTIONS.md` for financial-sector entities. These replace inference from peer reports for the ratio DEFINITIONS - the peer report (item 3) still governs the row SET and format.

3a. **Learn that agency's format from its own reference reports** (`<Agency>/Report for Reference/`) — section order, headings ("Key Rating Drivers", "Strengths"/"Weaknesses"), house phrasing, KI-table rows. Do NOT assume the format from memory; extract it from the agency's own published rationales (same as the ICRA craft rule).
4. **Facts still come only from the company's documents;** the Report-for-Reference rationales of ALL THREE agencies (ICRA, CRISIL, CareEdge) teach craft/context ONLY — never a source of any figure. Amounts the company does not disclose are marked "to be confirmed by issuer" (user directive, 14-Jul-2026).

   **⚑ NARROWED 13-Aug-2026, and re-affirmed 19-Aug-2026 — see CLAUDE.md §"AMENDMENT to the 14-Jul-2026 data directive" for the binding text.** A CRA-published **rated-amount table** MAY be imported where **all five** conditions hold: (1) the operator supplied that CRA's **primary published rationale** as a case document; (2) it is reproduced **verbatim, every line, with the publication date stamped**; (3) it is labelled **CRA-published, not issuer-confirmed**, with issuer confirmation recorded as outstanding; (4) **line integrity is verified** — the lines sum to the published total; (5) the **rated-limits-vs-drawn-debt distinction is stated explicitly**, with the drawn figure given. Fail any one and the amount reverts to "to be confirmed by issuer". This still bars reconstructing, splitting, estimating or rounding an undisclosed amount, and bars carrying a stale table as the current structure.

5. **⚑ CareEdge rated amounts — ALWAYS capture the long-term / short-term split (operator instruction, 19-Aug-2026).** CareEdge publishes its rated quantum in the header table of every press release, split by facility type, and repeats it facility-by-facility in Annexure-1 with maturity dates. When a CareEdge press release is available for the issuer, the report's Rating Action table and Annexure I **must** carry those amounts and that split — not a bare total, and not "to be confirmed by issuer". CareEdge's own row labels are the ones to use: *Long Term Bank Facilities*, *Long Term / Short Term Bank Facilities*, *Short Term Bank Facilities*, with Annexure-1's instrument names (e.g. "Fund-based - LT-Term Loan", "Fund-based - LT/ST-Working Capital Limits"). Amounts are written in CareEdge house style with the rupee symbol — `₹29.00 crore`, not `Rs 29 crore`. *(First applied: Riba Textiles, 19-Aug-2026 — ₹29.00 cr LT term loan maturing March 2029 + ₹65.00 cr LT/ST working-capital limits = ₹94.00 cr, against drawn borrowings of ₹75.88 cr.)*
6. **Name the deliverable with the agency:** e.g. `<Company>_<date>_CRISIL_Rating Rationale.md`, `<Company>_<date>_CARE_Rating Rationale.md`, `<Company>_<date>_Rating Rationale.md` (ICRA).

## The Knowledge Base is SHARED — one KB, all three agencies (14-Jul-2026)

**Do not build or recreate per-agency Knowledge Bases.** There is exactly ONE at the project root, and **every file in it covers all three agencies**:

| File | Coverage |
|---|---|
| `Knowledge Base/01_Methodology_Index.md` | all three libraries — ICRA 120 files · CRISIL 20 consolidated masters · CareEdge 73 papers — plus how each is structured and its gaps |
| `Knowledge Base/02_Sector_Routing_Map.md` | **Part A** sector→methodology for all three side by side; **Part B** what each agency actually cited, **pivoted by company** (1,220 companies; 320 multi-agency) |
| `Knowledge Base/03_Report_Template.md` | all three house styles side by side + the instrument-table data rule |
| `Knowledge Base/04_Core_Analytical_Framework.md` | all three analytical frames side by side (ICRA 4-factor · CRISIL 3-risk-profile · CareEdge A–E) |
| `Knowledge Base/05_SOP_Report_Creation.md` | the SOP + every logged lesson |
| `Knowledge Base/06_Rationale_Construction_Library.md` | craft (ICRA-built; ring-fenced for cross-agency use) |

The former `CRISIL/Knowledge Base/` and `CareEdge/Knowledge Base/` were archived as stale and deleted 01-Sep-2026 (nothing referenced them; the standing instruction below still applies) — do not recreate them. The per-agency folders now hold **raw data only**: `<Agency>/Methodology/` and `<Agency>/Report for Reference/`.

## Forecasting — equity-research plugin (SOP Step 12)

Every rating case builds its projections with the **equity-research plugin's initiating-coverage workflow, Tasks 1–4 run individually in order** (company research → **full 5-year 3-statement Excel model in the plugin's native format** → valuation analysis → charts), outputs saved in `Companies/<slug>/`. Task 5 (report assembly) is not run — the agency-style rating rationale is the deliverable. Rating overlays: **Task 1 research uses the user's documents + Indian sources via web search (AR/investor decks, BSE/NSE filings, screener.in, agency rationales, RBI/SEBI, business press) — never SEC EDGAR**; model drivers are source-labelled from the company's documents + sector-assumptions note; a stress case flexing the applicable methodology's named variables is mandatory; the model carries **two tabs beyond the plugin's six**: **Credit Ratios** (agency-convention suite — coverage, gearing, TOL/TNW, TD/EBITDA, TD/GCA, ROCE, current ratio, net debt — by formula for every historical and projected year) and **Debt Breakup** (statutory LT/ST/lease decomposition tied to the AR balance sheet AND screener.in; instrument-type and currency view from the AR's own disclosures; the AR's net-debt bridge with arithmetic tie-out; a rated-limits-vs-drawn-debt panel with the carried CRA table's DATE — a prior-year rating action is the latest public record, never "the current structure"); the base-case outputs are **copied (never live-linked) into the Rating_Scorecard assumptions**; valuation informs financial flexibility only. **Delivery: the filled model and scorecard .xlsx files are shared with the user together with written reasoning (key drivers, qualitative scores, anchor grade) — never a bare file.** The web app detects the model/valuation/chart outputs on the case page.

## Quantitative anchor — Rating_Scorecard.xlsx (SOP Step 12b)

`Rating_Scorecard.xlsx` at the project root is the grading calculator used by every rating regardless of agency: pick the agency + closest sector (22 sectors incl. Bank / NBFC / HFC, which switch to the financial-sector ratio framework), fill three years of financials + projections + qualitative scores (1–6), and it outputs an anchor grade on that agency's scale with its house-style rating line. Per case, work on a copy `Companies/<slug>/Rating_Scorecard_<Company>.xlsx` — never the master. The anchor is a screening cross-check: bands/weights are illustrative until back-tested against real rating outcomes, and any >1-notch divergence between the anchor and the analyst rating view must be explained in the workpaper. The web app detects the filled copy as a case output.

## Cross-agency use (a strength for ratings)

When rating a company, the OTHER agencies' published rationales on the same company (if present in their `Report for Reference/` folders) are useful **craft/consistency** references and confirm the rating landscape — but still never a source of facts. (Example already seen: JSW Steel's own annual report disclosed that ICRA, CRISIL-peer CARE and India Ratings all rate it AA — a corroboration point, not an input.)
