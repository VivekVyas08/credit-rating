# UNIFIED RATING GUIDE — ICRA · CRISIL · CareEdge
### One knowledge base, one flow, all three agencies. Read this file; it is the process.

*This file is the PROCESS. The single **`Knowledge Base/`** (files 00-06) is the reference layer — **every file in it now covers all three agencies**. The per-agency folders hold only raw data: `<Agency>/Methodology/` (the criteria files) and `<Agency>/Report for Reference/` (format teachers). The old per-agency Knowledge Bases are archived. CLAUDE.md remains the law on any conflict.*

---

## 0. THE RULES THAT NEVER CHANGE (all three agencies, every case)

| # | Rule |
|---|---|
| R1 | **The company's own documents are the ONLY source of data.** Annual reports, results decks, term sheets, the sector-assumptions note. **Distinguish SOURCE from CROSS-CHECK:** a third-party database (screener.in) or web research may be used **only to VERIFY a figure already extracted from the company's documents**, or for market/industry context labelled as such — **never to supply a figure that enters the report**. If screener and the AR disagree, **the AR wins** and the difference is explained by basis. |
| R2 | **ICRA, CRISIL and CareEdge published rationales AND published rating actions are REFERENCE ONLY** — they teach format, craft, driver taxonomy and calibration. **Never a source of any figure**, not even attributed. (User directive, 14-Jul-2026; the earlier "carry from CRA record, attributed" allowance is withdrawn.) |
| R3 | **Amounts the company does not disclose do not appear as data.** Write "to be confirmed by issuer" and ask for term sheets/sanction letters. Never reconstruct, never guess a split. *A total that ties while individual lines are wrong is still wrong.* |
| R4 | **Rated LIMITS ≠ balance-sheet BORROWINGS.** Limits include undrawn non-fund-based (LC/BG) and unallocated lines. State both; reconcile drawn debt at COMPONENT level (LT/ST/leases) against the AR **and** the appropriate independent cross-check for the entity type (screener.in for listed corporates; the AR's own statements + regulatory returns for financial-sector/standalone — screener is consolidated-only; see Step 6). |
| R5 | **Never mix computation bases in one ratio row.** Where two exist (AR headline excl-leases vs model incl-leases; excl vs incl acceptances) show BOTH rows, each labelled, defined once in a "Basis of preparation" note. Prefer the AR's own headline metrics for headline reporting. |
| R6 | **Every number computed in code** from the documents into the workpaper, before any rating view. **Every qualitative claim traced** to a document location. No "~" figures. |
| R7 | **Form your rating view BEFORE opening the company's prior report.** The prior report is opened only at Step 14, only for the divergence table. |
| R8 | **Date-stamp anything carried.** A prior-year rating action is "the latest public record", never "the current structure". Re-derive the current picture from the latest AR. |
| R9 | **Every step below has a STOP-AND-ASK gate.** Ask the question, wait for the answer, then proceed. Never assume the answer. |
| R10 | **Deliver the model + scorecard .xlsx WITH written reasoning** — never a bare file. |
| R11 | **Response protocol (every response, chat included):** (a) follow the governing step strictly, never deviate silently; (b) **self-audit claim-by-claim BEFORE sending** — is each claim traced, do the numbers reconcile, what would falsify it; (c) attach the data point + source behind every material conclusion inline (*conclusion — figures — source*). No naked assertions; unverified statements labelled. **When challenged ("are you sure?") — re-audit against the sources and report what failed; never reassure without re-checking.** |
| R12 | **The analytical BASIS (consolidated / standalone / combined) is METHODOLOGY-DETERMINED, not an operator preference.** Derive it from the applicable consolidation criteria (Step 5) and state the criterion. The operator may *request* an alternative basis only as a clearly-labelled **supplementary view**; it never overrides, or is presented as, the methodology basis. *(Fixes the IIFL standalone-override defect.)* |
| R13 | **Materiality is defined, not intuited.** A finding is MATERIAL if it meets any of: ≥ **1% of tangible net worth** (or ≥ 5% of PBT), OR a plausible **≥1-notch** rating impact, OR any regulatory/governance/default/covenant/fraud/going-concern item **regardless of size**. Immaterial items are logged once, not carried into the rating. Every Step-8 and Step-17 item states material / immaterial and why. |
| R14 | **The rating is a RATING-COMMITTEE decision, taken on the COMPLETE, re-verified package (draft included), by a body separate from the lead analyst.** The operator runs the tool but does **not** set the grade; the issuer never sets the grade. Committee minutes (members, the vote, dissent, the final rating/outlook and its rationale) are a mandatory output. *(No committee = no rating.)* |
| R15 | **Every rating carries a SURVEILLANCE commitment and an ENGAGEMENT TYPE.** Declare the type at Step 1 — *new assignment / surveillance / event-driven review / withdrawal / provisional / issuer-non-cooperating (INC)* — and route accordingly (§0A). Delivery is not "close the file"; it sets up ongoing monitoring (Phase 6). |
| R16 | **Independence, conflict & confidentiality (invoke the policy layer, don't leave it inert).** Operator ≠ decision-maker; fee/business discussions are segregated from the analytical function; the issuer provides facts and a **pre-publication factual review only**; the rating is UPSI until published (confidentiality per policy 129); conduct per 136; methodology reviewed on a calendar per 68. |
| R17 | **PROCESSING A QUEUE NEVER CHANGES THE SCOPE OF A CASE IN IT.** "Process the pending rating requests" is an instruction about ORDER, not about depth. Each case in a batch gets the same steps, the same artefacts and the same gates as a case raised on its own. Where scope must genuinely be reduced, it is reduced **per case, in writing, with a reason** — never as an unstated house style adopted because several cases arrived together. *(Six consecutive ratings between 15-Aug and 21-Aug-2026 shipped with no Step 12 forward view for exactly this reason; the cause was batch mode, not missing documents — every case that DID get a model also lacked a sector report.)* |
| R18 | **DISCLOSURE IS NOT AUTHORISATION.** Writing "not built in this pass" in a delivery scope does not convert an omission into a decision. An omission may be *disclosed* only where it was **authorised** — by the operator, by an engagement-type rule, or by a recorded scaling decision. Otherwise the choice is binary: **build it, or stop and ask.** A disclosed gap that nobody authorised reads as considered, escapes challenge, and therefore repeats — which is precisely how failure mode 35 survived six cases while being stated in every one of them. |

---

## 0A. ROLES, ENGAGEMENT TYPES & GOVERNANCE (who decides, and which steps apply)

**Roles (kept separate — this is where independence lives).**
| Role | Does | Does NOT |
|---|---|---|
| **Operator** (the "user" in the ASK gates) | runs the tool, supplies documents, answers scope/gap questions, confirms *inputs* | set or approve the **grade**; override a methodology determination (basis, scope statement) |
| **Lead Analyst** (the flow itself) | all analysis, forms an independent *proposed* view (Step 13) | make the final decision alone |
| **Reviewer** (four-eyes, Step 17b) | independent check of numbers, methodology fit, disclosure completeness | negotiate fees |
| **Rating Committee** (Step 17c) | **takes the decision** on the complete verified package; records minutes | rely on unverified inputs |
| **Issuer** | provides facts; a **pre-publication factual review** (Step 18b) | approve or negotiate the grade |

**Engagement types (declare at Step 1 — they change which steps run).**
- **New assignment** → full flow (Steps 1–19 + committee + surveillance setup).
- **Surveillance / periodic review** → the prior rating **is** the anchor; run 1b, 5–13 on the *latest* data, then a "what-changed-since" delta vs the prior rating (R7 is relaxed here — the prior rating is legitimately the starting point for surveillance, unlike a fresh assignment).
- **Event-driven review** → triggered by a material event; scope to the event + affected factors; may result in a Watch.
- **Withdrawal** → confirm no-dues/NOC + rationale; publish withdrawal.
- **Provisional** → prefix + list pending steps/documents.
- **INC (issuer-non-cooperating)** → the outcome of the **information-adequacy decision** below.

**Information-adequacy / INC decision (early gate, part of Step 1).** Before rating, decide whether the available disclosure is *adequate* to rate. If not — and the issuer does not cooperate — the outcome is an **INC rating on best-available information**, not a forced full rating. This is a decision, not just a report variant.

**Proportionality.** Not every engagement runs the heavy machinery. A CP-only mandate, an INC, or a stable investment-grade **surveillance affirmation** does **not** require a full 5-year 3-statement model or a valuation (see Step 12). Scale the work to the mandate; record the scaling decision.

---

## 1. AGENCY QUICK-REFERENCE (the only things that differ)

| | **ICRA** | **CRISIL** | **CareEdge (CARE)** |
|---|---|---|---|
| **LT scale** | `[ICRA]AAA … [ICRA]D` | `Crisil AAA … Crisil D` | `CARE AAA … CARE D` |
| **ST scale** | `[ICRA]A1+ … A4, D` | `Crisil A1+ … A4, D` | `CARE A1+ … A4, D` |
| **Rating line style** | `[ICRA]AA (Stable) / [ICRA]A1+` | `Crisil AA/Stable / Crisil A1+` | `CARE AA; Stable / CARE A1+` |
| **EBITDA is called** | **OPBDIT** | **EBITDA** | **PBILDT** |
| **Leverage names** | Gearing, TOL/TNW, Total debt/OPBDIT | Gearing, TOL/Adj networth, Debt/EBITDA, NCA/TD | **Overall gearing**, **TD/PBILDT**, **TD/GCA** |
| **Analytical frame** | Industry → Business → Financial → Management → Other → ESG | **3 risk profiles**: Business (industry risk / market position / operating efficiency) → Financial (accounting quality / cash-flow adequacy / liquidity & flexibility) → Management (+ project risk, ESG) | **Blocks A–E**: A Economy & Industry → B Business → C Financial → D Management → E Project + ESG |
| **Liquidity test signature** | Sources-vs-claims over 12 months → descriptor | **Bank-limit utilisation vs drawing power** (monthly) | CP carve-out from WC limits → **back-up liquidity** & drawing-power variation |
| **Liquidity descriptors** | Superior/Strong/Adequate/Stretched/Poor | same | same (CARE often says "Strong" where others say "Superior") |
| **Methodology structure** | **One file per sector** + `960 Corporate` master | **Consolidated masters** — route to FILE then internal SECTION | **One paper per sector** + Manufacturing **or** Services base master |
| **Methodology folder** | `Methodology/` | `CRISIL/Methodology/` | `CareEdge/Methodology/` |
| **Routing lookup** | **ONE Knowledge Base for all three:** `Knowledge Base/01` (index) + `Knowledge Base/02` (routing map) | ← same file | ← same file |
| **Format teacher** | `Report for Reference/` (649) | `CRISIL/Report for Reference/` (613) | `CareEdge/Report for Reference/` (803) |
| **Report format** | Summary of rating action → Rationale → KRD → Env & social → Liquidity → Sensitivities → Analytical approach → About → KFI → Annexures I/II | Rating Action → Detailed Rationale → Analytical Approach → KRD Strengths/Weaknesses → Liquidity → **ESG Profile** → Outlook → Sensitivity factors → About → KFI → Annexures → **Links to related criteria** | **Press Release** → Rationale & key rating drivers → **Sensitivities** → Analytical approach → Outlook → Detailed KRD (A–E) → **Applicable criteria** (name exact papers) → **Industry classification table** → Brief Financials → **Annexures 1–6** |
| **Deliverable name** | `<Co>_<date>_Rating Rationale.md` | `<Co>_<date>_CRISIL_Rating Rationale.md` | `<Co>_<date>_CARE_Rating Rationale.md` |
| **Signature requirement** | Methodology name **+ vintage** in Analytical approach | "Links to related criteria" names the exact files | **"Applicable criteria"** must name every exact paper |
| **Rating Watch** | `&` suffix (e.g. `[ICRA]AA+&`) + "Rating Watch with Positive/Negative/Developing Implications"; **no outlook while on Watch** | "Rating Watch with … Implications" | "Rating Watch with … Implications" (`Assigning Outlook or Rating Watch` paper) |
| **Complexity indicator** (mandatory in every report) | Simple / Moderately Complex / Highly Complex (policy `138`). Basel III Tier-2 = **Highly Complex**; plain facilities = Simple; CP = Very Simple | Complexity level per instrument in the instrument annexure | Annexure-4 "Complexity level of instruments rated" |
| **Consolidated-entity list** | **Annexure II** — entity, ownership %, consolidation method (or "Not Applicable") | "Annexure – List of entities consolidated" (extent + rationale) | **Annexure-6** (extent: Full/Moderate + rationale) |
| **Other suffixes / states** | `(CE)` credit enhancement; **provisional** per policy `107`; `; ISSUER NOT COOPERATING` per policy `132` | `PP-MLD` prefix for principal-protected MLDs; INC per basics-of-ratings §V | `PP-MLD` prefix; INC per `Information_Adequacy_Risk-and-INC`; provisional per `Policy-on-Assignment-of-Provisional-Ratings` |

**⚑ LT→ST mapping is NOT identical across the three agencies — corrected 13-Sep-2026.** This line previously read *"(identical, SEBI-standard, all three)"* and gave one table. That table is **ICRA's own** (`Methodology/mapping.md`); it was being applied to CRISIL and CareEdge reports with nothing checking whether that was even approximately right.

| Agency | What its own methodology actually says | Where |
|---|---|---|
| **ICRA** | Two **fixed anchors only** — AAA/AA→A1+ always, B/C→A4 always. The middle band maps to either of two adjacent ST grades, chosen by the entity's own liquidity assessment. | `ICRA/ICRA_CONVENTIONS.md` §8 |
| **CRISIL** | A **full table** (`basics-of-ratings` Table 1) that **varies by entity type at the same LT grade** — at A−, a *corporate* maps to (A1)/A2+ while a *bank* maps to A1+/(A1), a full notch better. Look up by **entity type**, not just agency. | `CRISIL/CRISIL_CONVENTIONS.md` §6 |
| **CareEdge** | Its own mapping table is **corrupted in the reference library** — structure survived PDF conversion, every data cell is blank (failure mode 49). **Do not reconstruct it from ICRA's or CRISIL's shape.** Verify any CareEdge LT-ST pair against that issuer's own published action (Step 14) and flag the file for re-extraction. | `Rating_of_Short_Term_Instruments_Feb_2025.md` |

Enforced by `check_sections.py` probe *"LT-ST mapping matches this agency's own table"*; the CareEdge corruption is printed at Step 1a by `preflight.py` probe **[10]**.

**⚑ The operating-profit measures are NOT interchangeable either, and are not simply three names for one thing.** ICRA's **OPBDITA** and CareEdge's **PBILDT** both *retain* core-related other income (job-work, scrap sales, duty drawback) while excluding interest/dividend/rental even when recurring. CRISIL's **PBDIT** is the outlier and the widest of the three — it retains **all** recurring non-operating income, interest and dividends included, excluding only one-time/extraordinary items. Read the agency's own conventions file before computing any operating-profit measure; never infer it from another agency's rule.

**⚑ CRISIL quantifies things the other two leave qualitative (added 06-Sep-2026).** Its **outlook** means a *material likelihood, "at least one in three"*, over **six months to two years**, and is **never assigned to a `Crisil C` or `Crisil D` grade**, to a short-term rating, or to a rating on Watch (a Watch resolves in ~**90 days**). Its **default trigger is per facility type** — 1 day/1 rupee for scheduled-repayment facilities, but **30 days** for cash credit, overdraft, packing credit, bill discounting, LC and BG (failure mode 55); curing is **90 days** to non-investment grade, **365** to investment grade. Its **INC** triggers are numeric: NDS missing **3 consecutive months** → INC within **5 working days**; non-cooperation beyond **6 months** → mandatory downgrade to non-investment grade. Its long-term scale is **20-point** (C+, C, C- and D all exist — this project's `Ref_Scales` stops at a single C and has no D). And **security earns no rating uplift at all**: a 10-20% LC cash margin does not prevent default, so it counts for nothing, though *unencumbered* liquid assets do count. Sources and detail: `CRISIL/CRISIL_CONVENTIONS.md` §§7-15.

**⚑ Total Debt composition differs too (failure mode 47).** CareEdge and CRISIL both fold **LC-backed acceptances/creditors** into Total Debt for gearing; CRISIL goes wider still (guarantees, factored receivables, pension liabilities, derivatives, contingent liabilities, each assessed for devolvement likelihood). **ICRA's Corporate methodology does not** — those sit in Total Outside Liabilities, the *Indebtedness Ratio* denominator, not in the *Gearing* numerator. *(Cochin Minerals: statutory gearing 0.04x against CareEdge's published 0.31x, the gap being ~Rs 47 crore of LC-backed creditors.)*

---

## 2. THE FLOW — Steps 1–21, **31 headers** (the numbered steps plus the sub-steps `1a · 1b · 7b · 12b · 12c · 12d · 17a · 17b · 17c · 18b`), running from LEARN & SCOPE through the DECISION & GOVERNANCE steps to **Phase 8 surveillance**. Every step has a gate. **Three of the 31 are MECHANICAL gates that run a script and read its verdict — `1a` pre-flight · `6` mutation coverage · `17a` delivery loop — and per CLAUDE.md §8a those scripts, not the prose, are the enforcement.** Each step: what you do (all agencies) → agency branch → **ASK and WAIT**. *(The analyst PROPOSES through Step 15; the Rating Committee DECIDES at Step 17c on the complete, re-verified package — R14. Iteration: if any step invalidates an earlier one, return to that step and re-run forward — the flow is not one-way.)*

### PHASE 1 — LEARN & SCOPE (no numbers yet)

#### Step 1 — Input inventory, engagement type, information adequacy
Table in chat: every document | period | audited/unaudited | standalone/consolidated. Below it the MISSING list (term sheets → ask; latest results → ask or disclose cutoff; sector-assumptions note → ask).
**Declare the ENGAGEMENT TYPE** (new / surveillance / event-driven / withdrawal / provisional / INC — §0A) — it changes which steps run.
**Establish the MANDATE SCOPE — which instruments/facilities am I actually rating?** A long-term instrument gets a rating **+ outlook**; a **short-term-only mandate (e.g. a CP programme) gets NO outlook**. Never assign an LT rating the agency has not been mandated for. *(ITC: only its CP is ICRA-rated -> `[ICRA]A1+`, no outlook.)*
**Data-freshness rule (R15 support):** state the data cutoff; use the latest **audited** statements + latest **interim**; if the audited financials are older than ~15 months, flag it; and run a **material-events bring-down check between the cutoff and publication** (Step 18b) — an issuer can default the day after your cutoff.
**Information-adequacy / INC decision (§0A):** judge whether disclosure is adequate to rate. If not and the issuer won't cooperate → route to **INC on best-available information**, not a forced full rating.
> **🛑 ASK:** "Here is the inventory, gaps, engagement type and information-adequacy call. **Which agency — ICRA, CRISIL or CareEdge? Which instruments (LT/ST/both)? Confirm the sector.** How do I handle each gap (provide / proceed and disclose / INC)?"

#### Step 1a — RUN THE PRE-FLIGHT FIRST (mechanical entry gate — binding)
**Before reading anything**, run:

```bash
python tools/preflight.py <case-slug>
```

It searches the reference library **and** every uploaded document, and prints WHAT EXISTS: prior rating actions (with the **rated-amount lines extracted**, so they cannot be deferred out of sight — R29), the AR's own credit-ratings note, subsidiaries to name, ESG data, instrument details, capex, promoter stake, auditor opinion, and the sector-defining KPI. **Paste the output verbatim into the workpaper Read Log.**

Four probes carry the extraction traps that cost this project real notches, and they run here — not later, when the figure is already in a draft:
- **[0b] OPERATING METRICS ACROSS DOCUMENTS** — prints each metric's value per file, newest-first, and flags `!!` where the same metric differs between documents, or where a metric appears **only in an older document** (the subtler trap: nothing contradicts it, so it reads as current). *(R30 — HDFC Securities shipped a branch trend inverted because two endpoints came from different reports.)*
- **[0c] AGGREGATE-NOTE CONTAMINANTS** — lists every non-operating component sitting inside Other Income / Other Expenses, largest-first. *(R36 — an undecomposed forex loss put a margin trend the wrong way up and shipped a rating a full notch low.)*
- **[0d] SAME ITEM IN TWO STATEMENTS** — flags any item whose cash-flow-reconciliation figure and P&L-note figure disagree. *(R38 — a forex figure entered wrong in **both magnitude and sign** and survived three rounds of checking.)*
- **[1] PRIOR RATING ACTIONS** — the two searches of R24, run for you.

**Binding effect: anything the pre-flight reports PRESENT may never later be written as "not available", "not disclosed" or "not extractable"** — only a second, *recorded* search that contradicts this run can override it. Anything it reports absent is **evidenced** absent and safe to state, citing this run. *(R20 — a false absence-claim is an untrue statement about your own evidence base; on Indus Towers it published a rating one notch wrong while the correct rating sat in four places in the issuer's own AR.)*

> **🛑 ASK:** "Pre-flight run — present: [list]; evidenced-absent: [list]; `!!` flags: [metric conflicts / aggregate contaminants / two-statement conflicts]. **Anything here you want me to chase before I start reading?**"

#### Step 1b — Read EVERY document, one by one, in full (binding gate)
Document Read Log in the workpaper: one row per file — what it is / key facts / material items. Broker & sector notes are mandatory reading (they carry the forward base case and live events). A file not in the log has not been read. *(Use `icra-doc-extract` for token efficiency.)*

**Two sub-gates before any extracted figure is allowed forward (added 11-Aug-2026, failure modes 15-17):**
- **CORROBORATE — traced is not verified.** Every mix/share %, headline financial, debt/cash figure, capacity/volume and order-book/capex number is checked against a *second* document in the case folder where one exists; the company's own audited/filed document wins any disagreement and the divergence is written down. **A figure whose only source is a chart / `picture text` block is marked "to be confirmed by issuer" — never shipped as clean fact** (the value-runs and legend in those blocks are NOT positionally aligned; a one-row mis-alignment put a wrong segment share into a delivered report on 11-Aug-2026).
- **TREND, not snapshot.** For every business-mix, capacity, margin and leverage metric, record the longest available time series and its direction — not just the latest value. The multi-year direction is frequently the rating driver; the snapshot is a data point. Also capture every consolidated/related entity's **full legal name** (grep `AOC-1`), regardless of materiality.
> **🛑 ASK:** "Document Read Log complete — here it is, with the corroboration checks and the multi-year trends noted. **Any document I should weight differently, or anything you know that isn't in these files?**"

#### Step 2 — Route to methodology (agency-specific)
| ICRA | CRISIL | CareEdge |
|---|---|---|
| `960 Corporate` + the sector file (or Corporate alone if no sector file). Banks → `929` **alone**; NBFC/HFC → `1003`. | Manufacturing/trading master: **Section I + Section IV (ratios) + the sector Section**; always add `basics-of-ratings` + `criteria-for-consolidation`. Banks → `criteria-for-banks-and-FIs`; NBFC → `finance-and-securities`. | Base master (**Manufacturing** or **Services**) + the sector paper if one exists + the always-on set (Default, Short Term Instruments, Financial Ratios – Non-financial, Outlook, Consolidation, Liquidity, Withdrawal). *Gaps: FMCG/IT/mining/O&G/PV/2W/chemicals have NO sector paper → master alone.* |

**Beyond corporates / banks / NBFCs — the rest of the routing (do not omit):**

| Entity type | ICRA | CRISIL | CareEdge |
|---|---|---|---|
| **Insurance** | `936 General` / `937 Life` (hybrids -> `998`) | `criteria-for-insurance-companies` (I general, II life) | `Non-Life-Insurance-Sector` + `Financial-Ratios-Insurance`. **Note: the scorecard does NOT cover insurers — rate them outside it** |
| **Infra SPV / project** | asset methodology (Roads HAM/BOT/Annuity, Airports, Ports, Power Thermal/Transmission/Distribution/Solar&Wind, Telecom Towers, CGD) **+ `938 Project Finance` if under construction**; `1021 Expected Loss` for EL-scale | `criteria-for-infrastructure-sectors` -> I drivers + II power / III annuity-HAM / IV toll; EL -> `crisils-criteria-for-expected-loss-ratings...` | `Criteria-Methodology-Infrastructure-Sector-Ratings` + the asset paper; under construction -> `Project_Stage_Entities`; EL -> `Expected_Loss_Ratings_for_Infrastructure_Projects` |
| **Structured finance** | `950 Securitisation` / `940 CDO` / `831 Pooled Loan` / `944 Security Receipts` | `criteria-for-securitisation-transactions` (II ABS / III CDO / IV RMBS / V covered bonds); `criteria-for-future-flow-transactions`; SR recovery criteria | `Criteria_Asset-Mortgage-Backed-Securitisation`; `Criteria-Pools-Backed-by-Wholesale-Assets`; `Rating_Methodology_Recovery_Ratings` |
| **Public finance** | `939 State Governments` / `835 Urban Local Bodies` | `criteria-for-public-finance` (I municipal / II state) | `Criteria_Rating_Methodology_State_Governments` |
| **Holding / investment co** | `941 Investment Companies` | `criteria-for-holding-companies` | `Rating-of-Investment-Holding-Companies-Debt` |
| **Cross-cutting (any rating)** | Financial Ratio Analysis, Liquidity Analysis, Consolidation, Implicit/Explicit Support, Structural Features, Hybrids, Outlook & Watch, Default Recognition, LT-ST mapping, Complexity Indicator | `basics-of-ratings` + `criteria-for-consolidation` + `criteria-for-factoring-parent-group-government-linkages` | the always-on policy set + `Consolidation-and-Combined-Approach` + `Notching_by_Factoring_Linkages_with_Parent` / `...with_Govt` |

**⚑ THE CONVENTIONS FILES ARE PART OF THE ROUTE, NOT OPTIONAL BACKGROUND (added 13-Sep-2026).** The methodology file tells you which factors to assess; the conventions file tells you how that agency **defines** the numbers you assess them with. Getting the first right and the second wrong produces arithmetic that is correct and answers the wrong question (failure mode 32).

| Entity class | ICRA | CRISIL | CareEdge |
|---|---|---|---|
| **Corporate** | `ICRA/ICRA_CONVENTIONS.md` | `CRISIL/CRISIL_CONVENTIONS.md` | `CareEdge/CORPORATE_CONVENTIONS.md` |
| **Bank / NBFC / HFC** | `ICRA/ICRA_BANKS_NBFC_CONVENTIONS.md` | `CRISIL/CRISIL_BANKS_NBFC_CONVENTIONS.md` | — |
| **Broking / securities** | — | `CRISIL/CRISIL_BANKS_NBFC_CONVENTIONS.md` §3 | `CareEdge/BROKING_CONVENTIONS.md` |
| **Infrastructure / project SPV** | — | **`CRISIL/CRISIL_INFRASTRUCTURE_CONVENTIONS.md`** | — |
| **Structured finance (ABS/RMBS/CDO)** | — | **`CRISIL/CRISIL_SECURITISATION_CONVENTIONS.md`** | — |

Three traps these files exist to stop, all three of which produced a real error: the **operating-profit** definitions differ (§1 above); the **Total Debt** composition differs (failure mode 47); and **three hybrid-instrument caps** look alike and are not — ICRA corporate **30% of adjusted equity**, CRISIL corporate **20% of adjusted net worth**, CRISIL NBFC/HFC **15% of Tier I capital** (the last regulatory, the others analytical). Three caps inside ten percentage points, three different bases (failure mode 51; the CRISIL corporate one was found 06-Sep-2026 and the check had been blind to it).

Cross-check the company in that agency's `02_Sector_Routing_Map` Part B (what the agency actually cited for real peers). **Verify each file's scope statement before citing it** — a scope mismatch is failure mode 4 (e.g. the corporate Hybrid methodology cited for a bank).
> **🛑 ASK:** "I propose these methodology files for <agency>: [list, with vintages]. **Confirm, or tell me to add/remove any.**"

#### Step 3 — Read the routed methodology IN FULL, this session
Extract each factor and every indicative-metrics table. If a threshold table is an unreadable image, **say so — never invent thresholds**.
> **🛑 ASK:** "Methodology read. Indicative bands extracted: [list]. **[N] tables were unreadable images — proceed without them, or can you supply them?**"

#### Step 4 — Learn format + calibration from a PEER SET (2–3, not one)
Pick a **peer set of 2–3 close comparables** in `<Agency>/Report for Reference/` (resolves the guide-vs-SOP contradiction; one peer is too thin for calibration). Extract **section order, headings, table shapes, house phrasing** *and* **calibration** — what metric levels earn AA vs A in this sector. **R2: no facts, no figures.**
> **🛑 ASK:** "Peer set for <agency> house style + calibration: [2–3 reports]. **Confirm, or name better peers.**"

### PHASE 2 — INDEPENDENT DATA WORK (company documents ONLY)

#### Step 5 — Extract into code
Every line item → `Companies/<slug>/compute_ratios.py`. Units converted once, in code. Consolidated and standalone both captured.
**BASIS is methodology-determined (R12), not an operator choice.** Derive consolidated / standalone / combined from the applicable consolidation criteria and **state the criterion that decides it**. If the operator asks for a different basis, produce it as a clearly-labelled **supplementary view** and STILL show the methodology basis as primary — never substitute. *(IIFL lesson: the methodology would consolidate similar-business lending subsidiaries; a "standalone" request is a supplementary lens, disclosed as a deviation.)*
**Financial Spreads (user directive, 17-Jul-2026):** immediately after the AR is read and extracted, GENERATE `Companies/<slug>/<Co>_Financial_Spreads.xlsx` **from the script** — three tabs: Extraction (every line item, all years, AR note reference per row), RatioSuite (the full agency-convention suite), TieOut (component-level reconciliation with PASS/FAIL). The script stays the source of truth (R6 — Excel is the review/feed layer, never hand-typed); values written LITERALLY and render-verified (`data_only` read-back, zero formula-only cells). The Step-12 model and Step-12b scorecard draw their historical inputs from this one workbook.
> **🛑 ASK:** "Extraction script built + Financial_Spreads.xlsx generated. Basis proposed: **[consolidated/standalone]** because [reason]. **Confirm the basis.**"

#### Step 6 — Compute the FULL ratio suite + EXTERNAL TIE-OUT
Use the **track that fits the entity** (the spine is not one-size; pick one): **Corporate** (profitability/leverage/coverage/working-capital/cash-flows, OPBDIT/EBITDA/PBILDT naming) · **Financial-sector** bank/NBFC/HFC (CRAR/Tier-I, GNPA/NNPA/GS3, credit cost, NIM, RoTA/RoMA, cost-income, gearing, ALM — *no EBITDA/working-capital rows*) · **Infra/project** (DSCR, EL) · **Structured** (pool/CE/waterfall). 3–5 yr trend.
**Tie-out gate (binding) — use the RIGHT independent cross-check for the entity, not always screener.in:** listed corporate → screener.in (consolidated); **financial-sector / standalone basis** → the entity's own audited statements at **component level** + regulatory returns where available (screener is consolidated-only and may be the wrong basis); **unlisted** → AR components + peer sanity. Reconcile borrowings **and its LT/ST/lease components**, revenue/income, PAT, net worth; explain every difference by basis in one line. *A matching grand total hides single-cell errors.*

**MEASURE WHAT THE TIE-OUTS COVER — a suite can be 100% green and verify nothing (R39, binding):**

```bash
python tools/tieout_mutation.py <case-slug>
```

It perturbs every numeric input in `compute_ratios.py`, re-runs `tieouts()`, and reports the inputs **no tie-out is sensitive to**. A passing count answers "how many checks passed", which is not the question — the question is *which inputs would any check notice if they were wrong*. Two ways a green suite hides an unverified input: a **circular check** comparing a value to itself, and an input **no check is downstream of**. **Every input the harness reports as verified-by-nothing must either gain a check, or be NAMED in `DISCLOSED_DIFFERENCES` as uncheckable, with the reason.** *(Jindal Stainless reported "22/22 reconcile" while four checks compared a cell to itself and the forex figure that was wrong in magnitude AND sign was covered by nothing. Reinstating the circular checks raises the headline to 30/30 — better-looking verification — while measured coverage does not move by a single input.)*

**Decomposition is not verification.** R36 requires an aggregate note to be decomposed before use; what converts every line inside it from a typed number into a *checked* one is **tying the decomposition back to the note's own printed total**.
> **🛑 ASK:** "Ratios computed on the [corporate/financial-sector/…] track; tie-out vs [source] at component level: [result]; mutation coverage **[N]%**, uncheckable inputs named: [list]. **Confirm before I proceed.**"

#### Step 7 — Trace every qualitative claim
Shareholding, board, order book, concentration, contingent liabilities, capex plans, litigation, auditor KAMs, subsidiary/JV list. Covers the Analytical-approach table and **every approximated figure**.
> **🛑 ASK:** "Fact register with source locations: [table]. **[N] claims I could not trace — do you have a source, or shall they be dropped from the report?**"

#### Step 7b — Instrument details from the ANNUAL REPORT
Grep the AR for `INE[0-9A-Z]{9,10}`, "Non-Convertible Debenture", "ISIN", "Commercial Paper". The Corporate Governance report + borrowings note + ratings note carry ISINs, coupons, amounts, maturities, CP-outstanding.
**R3 applies:** limits the company does not disclose (bank facilities, CP programme size) = **"to be confirmed by issuer"**. **Never** import them from any CRA action.
> **🛑 ASK:** "Instrument details from the AR: [ISIN table]. **Undisclosed: [CP limit / bank-facility limits] — can you provide term sheets or sanction letters?** Otherwise they stay marked TBC."

#### Step 8 — Materiality sweep across EVERY document
Hunt the untouched sections of every file — regulatory/tax changes, exceptional items (cash vs non-cash — **normalise them out**), settlements, guarantees, RPTs, governance, restatements, capex/JV/M&A, covenant and leverage-cap disclosures. Verify company figures against the **company's own** document, not a broker's paraphrase.
**Apply the R13 materiality test to each finding:** MATERIAL if ≥1% of TNW (or ≥5% of PBT), OR plausibly ≥1-notch, OR any regulatory/governance/default/covenant/fraud/going-concern item **regardless of size**. Each finding: *material / immaterial + the test it meets + include/exclude*. Immaterial items are logged once, not carried into the rating.
> **🛑 ASK:** "Sweep findings, each tagged material/immaterial with the test + decision: [list]. **Anything here you read differently?**"

#### Step 9 — Save the workpaper
`<Company>_Ratio_Workpaper_<date>.md`: computed suite, trend commentary, Read Log, fact register, sweep decisions, tie-out note, caveats.
> **🛑 ASK:** "Workpaper saved — every number now traceable to a document. **Review it before I start the analysis, or shall I proceed?**"

### PHASE 3 — INDEPENDENT ANALYSIS & RATING VIEW

#### Step 10 — Apply the methodology factor by factor → **Methodology Compliance Map**
One row per factor: *factor (as the methodology names it) | section | company's evidence/metric | vs the indicative band | weight*. Every notching criterion quoted **verbatim** (this is a table, not prose).
**Structured ESG block:** don't leave ESG as a one-line afterthought — map the E/S/G factors **material to THIS sector** (per the methodology's ESG guidance) and state each one's rating direction (most ESG is asymmetric: material unmitigated risks pull down; favourable ESG rarely pulls up).
| ICRA | CRISIL | CareEdge |
|---|---|---|
| Industry → Business → Financial → Management → Other → ESG | Business (industry risk / **market position** / **operating efficiency**) → Financial (accounting quality / **cash-flow adequacy** / liquidity & flexibility) → Management (**risk appetite explicit**) | A Economy & Industry → B Business (**diversification**, size/market share, earnings capacity, cost structure) → C Financial (**no refinancing/equity assumed**) → D Management (**pledge viewed negatively**) → E Project + ESG |
> **🛑 ASK:** "Compliance Map complete — [N] factors scored, [N] data-unavailable. **Review the scoring before I form the view.**"

#### Step 11 — Liquidity
Sources-vs-claims arithmetic over ~12 months. The descriptor is the **conclusion of arithmetic, never an adjective**. Apply the agency's signature test (§1): CRISIL → bank-limit utilisation vs drawing power; CareEdge → CP carve-out/back-up liquidity; ICRA → sources-vs-claims.
> **🛑 ASK:** "Liquidity arithmetic → descriptor **[X]**. **Confirm.**"

#### Step 12 — Projections (MANDATORY; the SHAPE is proportionate, the STEP is not)
**⚠ Read this before the list below.** "Proportionate" governs **which artefact you build**, never **whether you build one**. Between 15-Aug and 21-Aug-2026 six consecutive ratings shipped with no forward view at all, because "proportionate to the mandate" was read as licence to skip — and the omission was disclosed in each delivery scope, which made it look considered and let it repeat (failure mode 35). A rating is a forward-looking opinion. A rating with no forward view is not a lighter version of the job; it is a different job.

**Every case leaves this step with one of two things, and there is no third option:**
1. the artefact for its entity type, from the list below, **plus** the Step 12b scorecard; or
2. a **`step12_scaling_decision`** written into `case.json` — one or two sentences naming which lighter treatment applies and why. `check_sections.py` refuses to pass the case without one of these.

**Scale the model to the engagement (R15 proportionality) — do not force a heavy equity-research model on every rating:**
- **Corporate with term debt** → full 5-yr 3-statement model (below).
- **Financial-sector (bank/NBFC/HFC)** → a **lending model** (AUM/book growth → NII → credit cost → PAT; balance sheet; the Credit-Ratios & Debt-Breakup tabs) — the corporate 3-statement / equity-research template does **not** fit a lender.
- **CP-only / INC / stable IG surveillance** → a focused **sensitivity** on the 2–3 rating-driving variables, not a full model. Record the scaling decision.
- **Valuation is OPTIONAL** and, where produced, informs financial flexibility **only** (assess market-cap cushion directly rather than building a full valuation just to ring-fence it out of the grade).

For a full corporate model, run initiating-coverage **Tasks 1–4 individually** into `Companies/<slug>/`: research → **5-yr 3-statement model** → (optional) valuation → charts. **Task 5 skipped.**
- **Task 1 research: uploaded documents first, then INDIAN sources** (AR/investor decks, BSE/NSE, screener.in, business press) — **never SEC EDGAR**.
- Model carries **two extra tabs**: **Credit Ratios** (agency-convention suite, all years, by formula) and **Debt Breakup** (statutory LT/ST/lease decomposition tied to AR + screener at component level; instrument/currency view from AR disclosures; the AR's own net-debt bridge with tie-out; drawn-vs-limits panel, anything carried **dated** and marked reference-only).
- **Stress case mandatory**, flexing the variables the applicable methodology names.
- Every driver **source-labelled**: sector doc / historical / AR guidance / analyst judgment.
- Valuation informs **financial flexibility only** — never the grade.
> **🛑 ASK:** "Assumptions table with sources + base and stress results: [table]. **Sign off on the assumptions before I rate.**"

#### Step 12b — Scorecard anchor (governed)
Fill `Companies/<slug>/Rating_Scorecard_<Company>.xlsx` (copy of the root master — never the master; same agency; Bank/NBFC/HFC → financial-sector block). Feed the **quantitative inputs from AUDITED ACTUALS** (the Financial Spreads), so the anchor is genuinely independent — **do not let the analyst's own Step-12 forward assumptions drive it** (that contaminates the cross-check). Qualitative scores 1–6, each justified in the methodology's own language.
**Anchor governance (BACK-TESTED 18-Jul-2026 — see `Docs/Scorecard_Backtest_Report_18Jul2026.md`):** the composite→grade map was recalibrated (range-preserving power **p=1.4**) against **396 ICRA-rated issuers + the JSW/IIFL fully-scored cases**, removing a **+2.1-notch downward bias** (the cause of the JSW A−-vs-AA and IIFL A+-vs-AA misses). The **financial bands were shown NOT to be the constraint and left unchanged**; a `Ref_Qualitative` rubric and mandatory **support-notch discipline** were added. The anchor now **binds as a zero-biased ±2-notch screening band** — reliable to ~±1 only in the **A+…BBB− range**, and it still structurally **under-rates AA+/AAA and over-rates BB-and-below** unless the parent/group/government **support notch** and the **qualitative rubric** are applied per issuer. **Rule:** a divergence **beyond ±2 notches**, or **any** divergence for AA+/AAA or BB-and-below, is a **flag the Reviewer (17b) and Rating Committee (17c) must expressly resolve and minute** — closed by the qualitative/support narrative, never by talking the rating to CRA consensus. *(±1/80% is unreachable from financials alone — Spearman(financial score, grade)=0.32; the residual dispersion is irreducibly qualitative.)*
**⚑ THE BUSINESS-RISK GATE (added 13-Sep-2026, failure mode 53 — run this before reading the anchor back).** `Scorecard!E22` averages the business-risk score into the same composite as the financial ratios. **Neither ICRA nor CareEdge rates that way**: both band Financial Risk numerically and assess Business Risk — scale, market share, competitive position, diversification — descriptively only, with no formula converting "small scale" into notches. ICRA says outright that it *"does not form an unfavourable view of an entity merely because it has a small scale"*, a sentence with no numeric encoding. Averaging therefore lets a small, clean, debt-free issuer's ratios silently outvote the business weakness that should bound it.

```bash
python tools/add_business_risk_gate.py <case-slug>    # one-off per workbook; idempotent
python tools/recalc_workbook.py "<the workbook>"
```

The sheet then **derives** the divergence (`Scorecard!C41`) and raises the **GATE** (`C42`) when business risk is weaker by ≥2 points. The **ceiling itself is typed**, not derived — deriving it would re-commit the original error of inventing a business-risk-to-notch formula neither agency publishes:

| | |
|---|---|
| `Inputs!C69` | the best grade this issuer can reach **on business risk alone**, regardless of its ratios |
| `Inputs!D69` | the written reason — **required**, exactly like `D67` for a hard-cap disapplication |
| `Rating!C15` | bounded as `MAX(cap chain, ceiling index)`. Index 0 = AAA, 16 = C, so a ceiling on the *grade* is a floor on the *index*; unset = 0 = no-op |

*Verification: CMRL's anchor was **AA-** on gearing 0.04x and coverage 122x. Entering the **BBB** ceiling its business risk warrants moves the anchor to **BBB — CareEdge's own published grade for the same issuer on the same date**. Across the 23 case workbooks the gate fires on 4; Dhampur is independently a known miss, which is evidence the trigger measures something real rather than fitting the case it was built from.*

> **🛑 ASK:** "Anchor grade **[X]** (fed from audited actuals); business-risk gate **[fired / not fired]**, ceiling **[grade or none, with reason]**; divergence from my view **[N notches]**; qualitative scores + reasons: [list]. **Adjust any score, or the ceiling?**"

#### Step 12c — Scope the workbook to ONE agency and recalculate (added 01-Sep-2026)
`Rating_Scorecard.xlsx` is a **TRI-AGENCY TEMPLATE** — ICRA, CRISIL and CareEdge scales, bands and operating-profit conventions sit side by side. **A filled copy is not deliverable as it stands.**

```
python tools/annotate_scorecard.py <case-slug>
```

- **Scope** — clears the other two agencies from `Ref_Scales`, README and the band sheets, and writes only the rating agency's own operating-profit convention onto the Rating sheet (**corrected 13-Sep-2026 — this bracket previously said "ICRA OPBDIT strips other income unconditionally", which is false and had gone unchallenged since the file was written.** ICRA's own Corporate Credit Rating Methodology (July 2025) states in its footnote that operating profit *"includes other income which are considered core to its operations like the income from jobwork, scale of scrap, duty drawback etc."* So: **ICRA OPBDITA** and **CareEdge PBILDT** both retain core-related other income and both exclude interest/dividend/rental; **CRISIL PBDIT** is the widest, retaining all recurring non-operating income including interest and dividends. Sources: `ICRA/ICRA_CONVENTIONS.md` §1 · `CRISIL/CRISIL_CONVENTIONS.md` §1 · `CareEdge/CORPORATE_CONVENTIONS.md` §2-3. Any ICRA case where a core-related other-income item was excluded on the strength of the old wording should be re-checked). **They are not interchangeable — offering three lets the reader apply the wrong one (R32).**
- **Verify** — reads Stage 3 (below) and prints `MATCHES` or `*** MISMATCH ***` against this case's own rationale.
- **Recalculate** — `recalc_workbook.py`, so every computed cell is readable outside Excel.

**Order is recalculate → annotate → recalculate**, enforced in the script: openpyxl saves formulas with no cached value, so an un-recalculated workbook displays **blank** in any non-Excel reader, and annotating first quotes `None` for every figure it reads out of the workbook.

**Limit:** the tool scopes the TEMPLATE. It does **not** rewrite an analyst justification cell that names another agency — that is a finding for a person to resolve, not text to scrub (failure mode 40).

#### Step 12d — THE WORKBOOK IS A THREE-STAGE SHEET; ITS HEADLINE IS THE *ASSIGNED* RATING (added 02-Sep-2026)

The sheet used to print the anchor and nothing else, formatted exactly like a rating — so a reader opening it beside the report saw **two different grades with no connection** (Vodafone Idea anchor B− vs rating A−; Godrej Properties B+ vs AA+). Operator instruction: *"make it in a way that they both are the same and they are both linked to each other."*

| Stage | What it is | Set where | Filled at |
|---|---|---|---|
| **1 — Financial anchor** | Screening view from audited financials ALONE; blind to franchise, parentage, sector accounting | computed; `Inputs!C42` | **Step 12b** |
| **2 — Committee overlay** | The bridge: each adjustment a **named notch with its justification beside it** | `Inputs!B60:D64` | **Step 17c** |
| **3 — Assigned rating** | **The sheet's headline — what the rationale states** | computed, or `Inputs!C66` override | **Step 17c** |

**⚑ THIS RE-SEQUENCES THE FLOW.** Stage 3 records a decision that does not exist at Step 12b — the Committee decides at 17c. So the workbook is **no longer finished at Step 12b**: 12b fills Stage 1 and leaves 2–3 empty; **17c fills Stage 2 and 3**; 18 verifies. It is a living document completed at the decision, not an artefact abandoned early.

**The divergence is COMPUTED (`Rating!C34`), never typed.** The first two hand-typed notch counts in this project were both wrong — GPL's draft said "9" where the chain gives 3 after the sector correction; Vodafone Idea said "12" where it was 9.

**Hard caps may be disapplied, but only in writing.** The caps test *accrual* metrics: `interest coverage < 1x` forces B+. For a project-completion real-estate developer, accrual coverage is negative **by construction** while cash coverage is exceptionally strong (GPL: OCF/interest **57.2x**). Left to fire, that one cap moved GPL from A+ to B+ and manufactured **nine of its twelve notches**. Set `Inputs!C67 = "N"` **with a reason in `Inputs!D67`**. It is a *sector-applicability correction*, never a judgement uplift — the uplift goes in Stage 2 where it can be seen.

**Four gate probes enforce this** (each positive-controlled by deliberately breaking the link): Stage 3 exists · Stage 3 **equals** the rationale · every overlay notch carries a justification · a disapplied cap carries a written reason.

> **🛑 ASK:** "Workbook scoped to **[agency]** ([N] cross-agency cells cleared); anchor **[X]** → overlay **[+N]** → assigned **[rating]**, which **[MATCHES / DOES NOT MATCH]** the rationale; [M] cached values written. **Deliver?**"

#### Step 13 — Form YOUR rating view (before the prior report — R7)
Standalone → support notching **in both directions** (criteria quoted) → instrument-level adjustments → LT/ST mapping consistency (§1) → outlook per the agency's outlook policy.
**Group ratings:** if the entity is a subsidiary, establish the **parent's / group's credit profile first** — you cannot notch a subsidiary without the anchor it notches from.
**⚑ A WEAKER PARENT DRAGS A STRONGER SUBSIDIARY DOWN (added 06-Sep-2026, failure mode 56).** This flow only ever described notching *up*. CRISIL's notch-down criteria trigger whenever the parent is weaker than the subsidiary, or a company's standalone rating sits above its group's — so **a strong-looking standalone is the case where the drag is most likely to be missed, not the case where it can be skipped**. Outcomes are bounded: no drag at one end, **subsidiary equated with the parent** at the other. CRISIL weights *past not-at-arm's-length transactions* above every other parameter. Three further CRISIL-only brakes, none of which ICRA or CareEdge state: **group** notch-up is "typically limited" where **parent** notch-up is not; **infrastructure SPVs** cap at 1-2 notches (failure mode 52); and in a **homogenous group** an entity with **EBITDA below 10% of the group's** notches down up to 2 (1 if it has either healthy financials or group-matching growth; equated if both), a pre-operational project entity up to 3. GRE support resolves on a 2x2 whose top-right quadrant is **"equate to Crisil AAA"**. All of it: `CRISIL/CRISIL_BANKS_NBFC_CONVENTIONS.md` §§6-9. **Do not carry these numbers to an ICRA or CareEdge case.**
**Outlook vs Watch (decide explicitly):** assign an **Outlook** (Stable/Positive/Negative) for a directional medium-term view; assign a **Rating Watch** instead when a **discrete event** with unclear-but-near-term credit implications is pending (M&A, regulatory action, resolution) — no outlook while on Watch (§1). State which and why.
> **🛑 ASK:** "My independent view: **[rating]/[outlook]/[ST]**, reasoning: [chain]. Anchor said [X]; divergence explained by [reason]. **Confirm before I open the prior report.**"

#### Step 14 — ONLY NOW open the company's prior report
**RUN THE DIFF, do not eyeball it (added 13-Sep-2026):**

```bash
python tools/step14_diff.py <case-slug>
```

It aligns the agency's own action for this issuer against ours BY PERIOD and fails on any unexplained divergence in the analytical BASIS, the RATED AMOUNT, or the Brief Financials rows. This is the project's only **validation** gate: every other check verifies internal consistency and therefore scores full marks on a report built off the wrong statement, period or definition. Dhampur Bio Organics shipped at 34/34 tie-outs and 100% coverage with the basis wrong, the rated amount overstated by Rs 72.40 crore and liquidity overstated ~8x; this diff catches all three, and comparing only the GRADE - which is what Step 14 used to mean in practice - catches none of them.

Compare rating, outlook, drivers, descriptor, figures → **divergence table**, each difference explained (*my analysis found / postdates the anchor / I correct my view, with reason*). **R2 still applies — no facts flow in.** If none exists, benchmark peers and say so.
> **🛑 ASK:** "Divergence table: [table]. **Any divergence you want me to reconsider?**"

#### Step 15 — Analytical-package sign-off (the analyst's PROPOSED view — NOT the rating decision)
This gate confirms the *analytical package* is complete enough to draft; it is **not** the rating approval (R14 — the Rating Committee decides at 17c, on the drafted + re-verified package).
> **🛑 ASK:** "**Proposed** view: rating [X], outlook [Y], ST [Z]; rated instruments [list, TBC items flagged]; assumptions [as signed off]; anchor divergence [N notches]. **Proceed to draft (this goes to Reviewer + Committee, not final) — or change anything now?**"

### PHASE 4 — DRAFTING

#### Step 16 — Draft in the agency's exact format
Use §1's section order for the selected agency + the peer's house style (Step 4) + `icra-report-skeleton` where applicable. **Every number COPIED from the workpaper output** — never retyped from notes, memory or the anchor. Include the **"Basis of preparation"** note (R5) if two bases exist.
**Rating history — source rule (every agency's format demands a 3-year annexure):** under R1/R2 it may **NOT** be taken from any CRA's published record. Take it from the **company's own AR ratings note** (listed issuers disclose each CRA's ratings and action dates), attributed to the AR; anything the AR does not disclose is marked **"to be confirmed by issuer"**. For a first-time exercise assignment, write "first assignment in this exercise" — never invent history.
**Mandatory mechanics (§1 rows):** the **complexity indicator** for every rated instrument; the **consolidated-entity annexure** (ICRA Annexure II / CRISIL list / CARE Annexure-6) with ownership % and method, or "Not Applicable"; **Rating Watch** handled per §1 (no outlook while on Watch); `(CE)` / `PP-MLD` / provisional / INC tags where they apply; methodology **names + vintages** in the analytical-approach or criteria section.
> **🛑 ASK:** "Draft ready — [N] words, [N] sections. **Review before I re-verify and finalise?**"

#### Step 17 — Re-verify the drafted text against the script AND against source
Number-by-number drift check; check the named failure modes (§4).

**⚠ The drift check alone is NOT sufficient — it only covers COMPUTED numbers.** Every figure that
reaches the draft without passing through the computation script — segment/geography/product mix %,
capacity and utilisation, order book, shareholding, capex guidance, customer counts, contingent-liability
quanta — **bypasses the drift check entirely** and must be re-verified separately against its source
document, and against the corroborating second source identified at Step 1b. *(This is exactly how a
wrong segment share reached a delivered report on 11-Aug-2026: it was never in the script, so a clean
"all N figures match" drift result said nothing about it.)* Produce **two** results, not one:
- *Computed figures:* "all N match the script" or the fix list.
- *Non-computed figures:* "all M re-checked against source (and against the corroborating source where one exists)" or the fix list.
> **🛑 ASK:** "Re-verification — computed: [result]; non-computed/source-traced: [result]. **Proceed to Reviewer + Committee?**"

#### Step 17a — THE DELIVERY LOOP: audit → fix → re-audit, and do not stop until it is clean (binding)
Written guidance alone failed to stop a mandatory section being dropped from **four consecutive rationales**, so this is a script, not a rule to remember. And individually the project's checks had to be run and read one at a time — it was possible to call a case delivered having satisfied four of them and never noticed the fifth. One command runs all five:

```bash
python tools/delivery_audit.py <case-slug>     # one case
python tools/delivery_audit.py --all           # every case
```

It aggregates and prints a single verdict — **READY TO SHARE** or **NOT READY** — naming the specific failing check:

| Check | What it refuses to pass |
|---|---|
| `compute_ratios.py` tie-outs | any tie-out that does not reconcile |
| `tieout_mutation.py` coverage | an input **no tie-out is sensitive to** that is not named in `DISCLOSED_DIFFERENCES` (R39) |
| `check_sections.py` | a missing mandatory section, or any quality probe: ESG carries a company-disclosed number · liquidity descriptor named · rated amount stated or marked TBC · limits-not-outstandings · operating-profit normalisation named · no verbatim reuse of an agency publication · Step 12 built or scoped · the four scorecard probes |
| `annotate_scorecard.py` | Stage 3 ≠ the rationale's headline grade |
| ratio workpaper present | a case delivered with no `<Company>_Ratio_Workpaper_<date>.md` (Step 9) |

**The loop is:** run it → if NOT READY, open the named check's own output and fix **exactly** what it reports (do not guess at a broader rewrite it did not ask for) → run it again → repeat until it reads READY. **Never tell the operator a deliverable is ready while this exits non-zero.**

**What the loop is, and is not.** A script cannot loop itself into fixing an *analytical* gap — closing a missing Liquidity section or naming an unchecked input requires a document to be read, which §8a reserves for the analyst, never for a checker. `delivery_audit.py` is not that judgment; it is the **gate the judgment must pass**. It invents no fixes and lowers no bar.

*Trust the tool, but verify the finding:* when a check fires, confirm it against the document before "fixing" it — during calibration this checker produced false positives (an ICRA report has **no separate Outlook header by design**; `<u>` markup broke a header anchor). **A checker is evidence, not a verdict.**

> **🛑 ASK:** "Delivery audit: **[READY TO SHARE / NOT READY]**. Failing: [check + specific finding]. **Fixing these now — anything you read differently?**"

### PHASE 5 — DECISION & GOVERNANCE (the rating is MADE here, not before — R14)

#### Step 17b — Independent Reviewer (four-eyes)
A reviewer separate from the lead analyst checks: numbers re-tie, methodology fit + scope statements, **basis is the methodology basis (R12)**, materiality applied (R13), the anchor divergence is resolved not buried, and **SEBI-mandated disclosures are all present** (rating definition, 3-yr history, non-cooperation status, complexity, sensitivities, liquidity, lenders, entities-consolidated, the FSR/regulator annexure). Reviewer signs or returns to the failing step (iteration is allowed — §2).
> **🛑 ASK:** "Reviewer check: [pass / list of returns]. **Send to Committee — or rework?**"

#### Step 17c — RATING COMMITTEE (the decision + minutes)
The Committee (a body separate from the lead analyst) decides the rating/outlook on the **complete, re-verified package**. Record **minutes**: members present, the proposed vs decided rating, the vote, any dissent, the **express resolution of the anchor divergence**, and the decision rationale. The Committee's rating — not the analyst's proposal, not the operator, not the issuer — is the rating (R14). A material number change here loops back to Step 17.

**WRITE THE DECISION INTO THE SCORECARD HERE (added 02-Sep-2026 — see Step 12d).** The minutes are not the only record: fill **Stage 2** (`Inputs!B60:D64`) with the notching that bridges the Step 12b anchor to the decided grade — **one named notch per line, each with its justification beside it** — and, where the Committee sets a grade directly rather than by notching, `Inputs!C66` with its reason in `D66`. Stage 3 then computes the assigned rating and the sheet's headline becomes the decision. Re-run `python tools/recalc_workbook.py <the workbook>`. **Anything the Committee relied on that is not written into Stage 2 is invisible to every later reader of the file.**
> **🛑 ASK:** "Committee decision: **[rating/outlook/ST]**, vote [x-y], divergence resolved by [reason], minutes recorded; scorecard Stage 2 filled ([N] notches, each justified) and Stage 3 now reads **[assigned rating]**. **Confirm to proceed to issuer factual review.**"

### PHASE 6 — ISSUER REVIEW & PUBLISH

#### Step 18b — Issuer factual review, appeal, and bring-down
Share the draft with the issuer for a **factual-accuracy review only** (not grade negotiation). Handle any representation/appeal via a fresh Committee look if warranted. **Bring-down check:** confirm no material event between the data cutoff and publication (R15/Step 1). Then publish.
> **🛑 ASK:** "Issuer factual review: [corrections / none]; appeal: [n/a or outcome]; bring-down: [clean/event]. **Publish?**"

### PHASE 7 — DELIVER & LEARN

#### Step 18 — Deliver together, with reasoning (R10)
Report + workpaper + **Financial_Spreads.xlsx** + **model .xlsx** + **scorecard .xlsx** + (optional) valuation/charts + **Committee minutes**. Written reasoning: key drivers with sources, each qualitative score, the anchor grade and its divergence. Data-cutoff, computation basis and caveats **inside** the report. Offer .docx/.pdf.

**Run the verification and read its verdict before delivering:** `python tools/annotate_scorecard.py <case-slug>` prints `MATCHES` or `*** MISMATCH ***` for the workbook's Stage 3 against the rationale. **A mismatch is resolved on the sheet — by correcting the Stage 2 overlay or the report — never by restating the grade in prose.** The delivery gate fails the case if they differ.
> **🛑 ASK:** "Delivered: [file list incl. minutes]. **Anything to adjust before I set up surveillance (Phase 6)?**"

#### Step 19 — Log lessons the same day
Any mistake found at any stage → this file's §5 + `Knowledge Base/05_SOP_Report_Creation.md` + memory.
> **🛑 ASK:** "Lessons from this case: [list]. **Anything you want captured as a standing rule so it never recurs?**"

### PHASE 8 — SURVEILLANCE (a rating is a living opinion, not a one-off — R15)

#### Step 20 — Set up surveillance
Record: next scheduled review date (**periodic, ≥ annual**); the **monitorables/triggers** that force an event-driven review (covenant breach, rating-linked acceleration, regulatory action, results miss vs the base case, promoter/ownership change, liquidity event); the **default-monitoring** obligation (1-day/1-rupee → move to D per the default policy); and the surveillance data feed. INC/withdrawn ratings still carry the applicable monitoring.
> **🛑 ASK:** "Surveillance set: next review [date]; triggers [list]; default watch on. **Confirm.**"

#### Step 21 — Periodic / event-driven review (re-enters the flow as a *surveillance* engagement)
On the scheduled date or a trigger, re-run as a **surveillance** engagement (§0A): latest data through 1b/5–13, then a "what-changed-since" delta vs the current rating → Reviewer → Committee → publish (affirm / change / Watch / downgrade). The prior rating is the legitimate anchor here (R7 relaxed for surveillance).
> **🛑 ASK:** "Review trigger: [scheduled/event]. **Run the surveillance review now?**"

---

## 3. THE SEVEN RULES (older formulation, kept for continuity — **§0 R1-R11 governs on any conflict**)

1. Reference reports are **teachers, not sources** (-> R2). 2. **My view forms before the anchor is opened** (-> R7). 3. Nothing is verified until **computed or traced** — "it matches the old report" is not verification (-> R6). 4. **Verification before drafting; re-verification after drafting** (-> Steps 6 / 17). 5. **Missing inputs are asked for, not improvised** (-> R3). 6. Every **judgment, divergence and limitation is disclosed in the deliverable itself**. 7. **Every step has visible output. No output = not done. "Mostly yes" does not exist.**

---

## 4. NAMED FAILURE MODES (each caused a real error — check explicitly)

1. **Anchor-inherited facts** → trace, attribute, or ask.
2. **"~" figures** → memory leakage; trace or replace with "-".
3. **Carried ratios** → compute everything.
4. **Scope-mismatched methodology citation** (e.g. corporate Hybrid methodology cited for a bank) → read the scope statement.
5. **Material omissions** → the materiality sweep exists for this.
6. **Undisclosed divergences** → footnote in the report, not just chat.
7. **Number drift during writing** → post-draft re-verification.
8. **Verification claimed but not evidenced** → no output = not done.
9. **Unread documents** ("listed and waved off") → every file in the Read Log. *(ITC: missed the GST 2.0 cigarette-tax reset.)*
10. **"Instrument details not available" / copied anchor Annexure** → extract from the AR (Step 7b). *(JSW: missed 6 NCD ISINs.)*
11. **Company figure from a broker's paraphrase** → verify against the company's own document. *(JSW leverage cap: AR 3.75x vs broker 3.0x.)*
12. **Invented / mis-split rated-amount lines** → a total that ties while lines are wrong is still wrong. *(JSW: term-loan 24,614 vs actual 20,195; unallocated 3,952 vs 8,372 — mis-split by the same 4,419, hidden by the correct 94,660 total.)*
13. **Rated limits conflated with drawn borrowings** → different measures; state both, reconcile at component level. *(JSW: limits 94,660 vs drawn 99,310 — both correct.)*
14. **Stale-dated table pasted as current** → date-stamp everything carried; re-derive from the latest AR. *(JSW: pasted ICRA's 2025 action while the FY26 AR held net debt 53,870, deleveraging 37,250, tranche-2 7,875, mix 64% FC — all unused.)*
15. **Mixed bases in one ratio row** → show both, labelled. *(JSW KFI: FY26 at 1.81x AR-basis beside FY25 at 3.48x model-basis.)*

**⚑ This list is an EXTRACT, not the register — corrected 13-Sep-2026.** It stopped at 15 while `CLAUDE.md` §8 carried **53**, so the flow document the operator is told to follow was silently 38 failure modes behind the law. **`CLAUDE.md` §8 is the register; read it, not this extract.** The ones added since this list was last synced, in one line each:

| # | In one line | Enforced by |
|---|---|---|
| 16–35 | Trend-vs-snapshot · unnamed consolidated entities · derived debt path · dropped mandatory section · **false absence-claims** · sector-defining metric · resolving-vs-live risk · partial totals · the two prior-rating searches · **wrong domain vocabulary** · stale figure beside a newer file · rated list vs capital structure · wrong sector's metric set · over-generalised sector rule · **answer sat in the reference library** · undated metric series · drawn debt ≠ rated universe | `preflight.py` · `check_sections.py` |
| 36–40 | Aggregate note fed in undecomposed · verbatim reuse of an agency publication · cash-flow row used where the P&L note is the source · **tie-outs counted instead of coverage measured** · scorecard contradicting its own rationale | `[0c]` · `[0d]` · `tieout_mutation.py` · `annotate_scorecard.py` |
| 41–46 | **Verification measured and called validation** · basis asserted not derived · a date stamp is provenance not freshness · post-balance-sheet event in the rated period · encumbered cash as liquidity (all sectors) · capacity quoted where throughput is the metric | `step14_diff.py` · `[0e]` · `check_sections.py` |
| **47** | **Total Debt composition differs by agency** — CareEdge/CRISIL fold in LC-backed acceptances, ICRA does not | `check_sections.py` *"Total-debt basis stated…"* — found 3 real gaps in the delivered corpus |
| **48** | CRISIL's four-factor promoter-unsecured-loan test has no equivalent here | `preflight.py` **[0f]** |
| **49** | A reference-library table can be **silently corrupted** by PDF conversion and still look present | `corpus_table_integrity.py`, wired into `preflight.py` **[10]** |
| **50/51** | ICRA's 30%-of-adjusted-equity hybrid cap is unencoded; it is **not** CRISIL's 15%-of-Tier-I cap | `check_sections.py` *"Hybrid-instrument cap not conflated…"* (50 partial — see §8) |
| **52** | CRISIL caps infra-SPV parent-support notch-up at **1-2**; ICRA states no ceiling | `check_sections.py` *"Infrastructure-SPV support notching…"* |
| **53** | **Business risk averaged against numeric financial bands** — the largest single miss in this project | `add_business_risk_gate.py` + `check_sections.py` *"Business-risk gate…"* (**BLOCKING**) |
| **54** | An **outlook on a C or D grade** — CRISIL never publishes one, and the scorecard generated it unconditionally | `check_sections.py` *"Outlook not assigned to a C or D…"* + the `Rating!C36` guard |
| **55** | **"1 day / 1 rupee" is only half of CRISIL's default rule** — 30 days for CC/OD/LC/BG/packing credit | no check possible (surveillance behaviour, not report text) — SOP Step 20 corrected instead |
| **56** | The **notch-DOWN direction did not exist in this flow** — a weak parent drags a strong subsidiary | no check possible (needs the parent's rating) — Step 13/15 procedure corrected instead |
| **57** | A project-finance **DSCR that includes the DSRA or sponsor support is not a CRISIL DSCR**; DSCR is also calibrated by asset class | partial — 4 infrastructure `SECTOR_KPI` entries, `test_infra_kpi.py` 11/11 (the exclusion itself is a property of the computation, not the text) |
| **58** | **Expected Loss is a separate 7-point scale with published numeric bands** (EL = PD × LGD over instrument life) and the scorecard cannot express it — rate EL mandates outside it | `check_sections.py` *"Expected-loss rating matches its stated loss estimate"*, 11 controls |
| **59** | An **asset-quality improvement that never mentions write-offs** proves nothing — write-offs empty every delinquency bucket | `check_sections.py` *"Asset-quality improvement addresses write-offs"*, 8 controls — **found 4 real gaps** (Aptus, NABKISAN, Repco, SBI) |
| — | **Prior-rating absence-claim contradicted by the library** (FM20/24/29) | `check_sections.py`, **BLOCKING** — found Cochin Minerals and Creative Newtech |

---

## 5. LESSONS (append every new one here + KB 05, same day)

- **ITC:** ICRA operating income is **net of excise duty** (30.9% gross vs 34.6% correct margin). Confirm the rating basis (consolidated vs standalone) and the actual mandate scope — ITC's only ICRA-rated instrument is CP → A1+, **short-term, no outlook**.
- **ITC:** broker/sector notes are **not optional colour** — they carry the forward base case; the anchor's forward claims are often contradicted by the company's own latest documents.
- **SBI:** methodology citations must pass the **scope statement** test — `998 Hybrid Instruments` excludes bank hybrids (covered inside `929`).
- **JSW Steel:** the AR is the primary source for the debt structure, not just the P&L — its net-debt bridge, funding-mix charts and NCD statements carry the current picture the CRA's older action cannot.
- **JSW Steel:** verbatim copying is not analysis. Fidelity fixes mis-splits; only **dating + AR re-derivation** fixes staleness.
- **PROCESS REDESIGN (18-Jul-2026, credit-rating-head audit of the flow itself).** Fixed structural loopholes: **R12** basis is methodology-determined not an operator choice (IIFL standalone-override); **R13** materiality is defined (%TNW / notch / regulatory-regardless); **R14** the rating is a **Rating-Committee** decision on the complete re-verified package (added Steps 17b Reviewer + 17c Committee + minutes; Step 15 reframed as the analyst's *proposed* view, not approval); **R15** every rating carries a surveillance commitment + engagement type (added §0A roles/branches, Step 1 info-adequacy/INC + data-freshness, Phase 6 Steps 20–21 surveillance, Step 18b issuer factual review/appeal/bring-down); **R16** independence/conflict/confidentiality invoked; Step 4 now a 2–3 peer set (was "the closest peer"); Step 6 entity-appropriate track + tie-out (screener is not universal); Step 12 model is proportionate to the mandate (financial-sector lending model, not the corporate 3-statement template; valuation optional); Step 12b anchor fed from **audited actuals** not analyst projections, and a >1-notch divergence must be **committee-resolved** (the scorecard stays non-binding until back-tested); Step 10 structured ESG-materiality block; Step 13 parent-rating-first + explicit Outlook-vs-Watch. **CLAUDE.md §6 reconciled 18-Jul-2026** (governance overlay added: R12–R16, roles, Reviewer/Committee 17b/17c, issuer review 18b, surveillance 20/21; Step 15 reframed; §9 interaction protocol updated).

- **SCORECARD BACK-TESTED (18-Jul-2026).** 396 ICRA-rated issuers (379 corporate + 17 financial) + the JSW/IIFL fully-scored cases. Finding: the baseline anchor was **+2.13 notches too low systematically** (not the un-tunable financial bands — the **composite→grade map** was too harsh in the IG zone). Fix applied to `Rating_Scorecard.xlsx`: map → range-preserving power **p=1.4** (bias → +0.13), a `Ref_Qualitative` 1–6 rubric (open item #4), and mandatory support-notch discipline. **±1/80% proven unreachable from financials alone** (Spearman 0.32; isotonic ceiling 47% within-1) — the anchor is a **zero-biased ±2 screening band**, not a point rating; residual dispersion is qualitative/support. Bands deliberately left unchanged (tuning overfits). Full record: `Docs/Scorecard_Backtest_Report_18Jul2026.md`.

---

## 6. WHERE THE LOOKUP DATA LIVES (this file is the flow; these are the tables)

| Need | ICRA | CRISIL | CareEdge |
|---|---|---|---|
| Which methodology file covers what | **`Knowledge Base/01`** — one index, all three libraries (ICRA 120 · CRISIL 20 masters · CareEdge 73) | ← same file | ← same file |
| What the agency actually cited per company | **`Knowledge Base/02`** — one map: Part A conceptual (3 agencies side by side) + Part B empirical **pivoted by company** (1,220 companies, 320 multi-agency) | ← same file | ← same file |
| Format teacher (craft only — R2) | `Report for Reference/` | `CRISIL/Report for Reference/` | `CareEdge/Report for Reference/` |
| Deeper framework digest | **`Knowledge Base/04`** — all three frameworks side by side | ← same file | ← same file |
| Rationale craft library | `Knowledge Base/06` (ICRA-built) + `Knowledge Base/03` (all three formats) | **CRISIL's own peers** for format; 06 only for agency-neutral craft. **Never import ICRA section order/phrasing** | **CareEdge's own peers** for format; 06 only for agency-neutral craft. **Never import ICRA section order/phrasing** |
| Scorecard | `Rating_Scorecard.xlsx` (root; agency + sector dropdowns — one file, all three) | ← same | ← same |

---

## 7. THE TOOLCHAIN — every script, and the step that runs it

Per CLAUDE.md §8a, **no failure mode may be added to §4 as prose alone**: it ships with a probe, or with a written statement of why no mechanical check is possible. These scripts are that enforcement layer — the prose above explains *why*, this table is the *mechanism*.

| Script | Run at | What it does | Gate behaviour |
|---|---|---|---|
| `preflight.py <slug>` | **Step 1a** | Prints what EXISTS across the library + every uploaded document; probes `[0b]` metric-across-documents, `[0c]` aggregate-note contaminants, `[0d]` same-item-two-statements, `[0e]` balance-sheet aggregates + earmarked deposits, **`[0f]` promoter/related-party unsecured loans (CRISIL, FM48)**, `[1]` prior rating actions **with rated amounts extracted**, **`[10]` methodology table integrity (FM49)** | Anything reported PRESENT may never later be called "not available" |
| `corpus_table_integrity.py [file…]` | **Step 1a** (via preflight) · Step 3 | Walks every methodology table across all three corpora and flags one whose **data cells are blank while its skeleton survives** — the PDF-conversion corruption that passes any header-only check. `--selftest` = 3 controls | Exit 1 on any corruption; a threshold from a flagged table may not be quoted |
| `add_business_risk_gate.py [slug]` | **Step 12b** (one-off per workbook) | Adds the FM53 gate: derives the business-vs-financial divergence, raises the flag, binds `Inputs!C69` ceiling into `Rating!C15` as a MAX. Idempotent. `--selftest` = 5 controls | Gate YES + no ceiling + no written waiver ⇒ `check_sections.py` fails the case |
| `step14_diff.py <slug>` | **Step 14** | The only check that asks why **our** number differs from **the agency's own** number for the same issuer — aligned by period | `delivery_audit.py` gate 6; fails on unexplained divergence |
| `test_fm47_52.py` | after touching `check_sections.py` | Positive controls for the FM47/51/52 probes and the LT-ST mapping check | 10/10 must pass — a check that cannot fail its own control is not a check |
| `tieout_mutation.py <slug>` | **Step 6** | Perturbs every numeric input, re-runs `tieouts()`, names inputs **no tie-out is sensitive to** | Uncheckable inputs must be named in `DISCLOSED_DIFFERENCES` |
| `make_spreads.py` | Step 5 | Generates `<Co>_Financial_Spreads.xlsx` **from** the script (Extraction / RatioSuite / TieOut) | Excel is generated, never hand-typed (R6) |
| `fill_scorecard.py` | Step 12b | Fills the scorecard's Stage-1 inputs from the extraction script | — |
| `restructure_scorecard.py` | one-off | Rebuilds the template to the three-stage layout (12d) | — |
| `recalc_workbook.py <xlsx>` | 12c · 17c | Writes cached values so computed cells are readable outside Excel | An un-recalculated workbook displays **blank** to any non-Excel reader |
| `annotate_scorecard.py <slug>` | **12c + Step 18** | Scopes the workbook to ONE agency, annotates, recalculates, and **verifies Stage 3 against the rationale** | Prints `MATCHES` / `*** MISMATCH ***`; **exits non-zero if it could not verify at all** |
| `check_sections.py [file]` | **Step 17a** | Agency-aware section audit + ~20 quality probes (headers only, never body text). **Two tiers since 13-Sep-2026:** most probes WARN; those named in `BLOCKING_PROBES` fail the case like a missing mandatory section — currently the business-risk gate (FM53) and the prior-rating absence contradiction (FM20/24/29) | Non-zero exit **blocks delivery**; a BLOCKING probe is non-zero |
| `test_fm20_prior_absence.py` | after touching `check_sections.py` | Controls for the prior-rating absence probe, including the two that caught its own miscalibration | 8/8 must pass |
| `test_infra_kpi.py` | after touching `SECTOR_KPI` | Controls for the four infrastructure sector metrics — they fire on nothing in the corpus, so they are exercised synthetically | 11/11 must pass |
| **`test_no_control_chars.py`** | **after ANY regex edit** | Scans every tool for C0 control characters. Six times in one session a `` word boundary was written as byte 0x08 (a literal backspace): the file imports, the probe runs, and it matches **nothing** | must report clean |
| `delivery_audit.py <slug>` | **Step 17a** | Aggregates all five gates into one verdict | **READY TO SHARE** / **NOT READY** — the loop runs until READY |
| `rate_engine.py <slug>` | cross-check | Produces an outcome two independent ways and reports the gap (§8) | Aborts with exit 1 if any tie-out fails — no outcome is produced at all |
| `research_audit.py <slug>` | `finance-research` skill | The research-note equivalent of the delivery loop | Runs until **READY TO SHARE** |
| `md_to_docx.js` · `doc_figures.py` · `make_public.py` | Step 18 | Conversion / figures / publishable copy | — |

**§8 — TWO ROUTES TO AN OUTCOME (`rate_engine.py`).** Full documentation in `Docs/RATING_ENGINES.md`.

```bash
python tools/rate_engine.py <case-slug> [--engine local|api|both] [--model ID]
```

- **local** — the filled scorecard evaluated offline through its own formula chain. No key, no model, byte-identical every run. **This is the Step 12b anchor, made runnable.**
- **api** — Claude via the Messages API, returning a schema-constrained rating **view**.
- **agent** — a local Claude Code agent inheriting this file, the skills and the case folders, so it can process a request end to end (the api engine cannot: it only ever sees the computed ratio table).

**BINDING — the division of labour is not negotiable.** The API engine receives the ratio engine's **verified computed output**. It never sees the source documents and is never asked to extract a figure: every material error this project has made was an **extraction** error (R30/R36/R38), those are caught by tie-outs and mutation coverage, and putting documents in front of a model would reintroduce that failure class in the one place no tie-out reaches. **The engine establishes what is true; the model decides what it means.** Divergence between routes is a finding to resolve under the Step 12b anchor-divergence rule — **never a number to average**.

**Credentials:** `--set-key` stores the key in the user's HOME, never in this project folder (which is zipped and emailed with the reports). `--show-key` / `--clear-key` manage it. With no credential the local engine still runs and the API engine reports itself unavailable. The key is never printed, logged, or written to `--json` output.

*Guide version 2.0 — 13-Sep-2026 (CRISIL and CareEdge corpora COMPLETE; the issues raised by reading them in full are now fixed. Five changes, each mechanically enforced. **(1) Sector metrics:** `criteria-for-manufacturing-trading-and-corporate-services-sector.md` publishes the defining operating metrics for **22 industries** and `SECTOR_KPI` held entries for six of them, so failure mode 21 was unenforced for most of the delivered corpus — steel, pharma, tyres, FMCG, E&P, textiles, IT services and speciality chemicals all shipped with no sector-metric gate at all. **19 entries added**, then tightened against eight real false positives (24 controls). **(2) Real estate, failure mode 60:** CRISIL publishes a CFO-based ratio set for developers and this project was using accrual coverage and gearing — the root cause behind failure mode 40/Godrej, whose recorded remedy treated the symptom. New `CRISIL/CRISIL_REAL_ESTATE_CONVENTIONS.md`. **(3) Global scale, failure mode 61:** a global-scale rating maps to CRISIL's national scale **6-7 notches higher**; the project had no rule on this anywhere. ICRA maps from Moody's with no notch count, so the number must not travel. **(4) Rating scale, failure mode 62:** `Ref_Scales` could not express C+, C- or D; extended to the full 20 points plus D across the template and 22 case workbooks with every anchor and assigned grade unchanged. **(5) Failure mode 63:** CRISIL's financial-sector supplementary parameters can constrain but never lift — enforced by the existing failure-mode-53 gate, stated explicitly rather than assumed. Two pre-existing false positives were found and fixed in passing: the LT-ST probe classified a distributor as a bank on the words 'bank facilities', and the hotel/telecom/pharma sector triggers matched segment names, customer lists and demerged businesses. **ICRA-sourced issues are deliberately NOT addressed here** — that corpus is still being read.)*

*Guide version 1.9 — 06-Sep-2026 (CRISIL securitisation criteria read in full — the risk primer and legal framework, ABS, CDO and RMBS — and written up as `CRISIL/CRISIL_SECURITISATION_CONVENTIONS.md`. Structured-finance content: bankruptcy remoteness as the building block, with a **10% clean-up-call ceiling** and the trap that excessive risk retention lets a court reclassify a sale as **secured borrowing**; credit enhancement sized on the **peak of monthly CUMULATIVE shortfalls**, never expected loss, with a minimum cash collateral required regardless; CDO over-collateralisation and interest-coverage triggers; and the Monte Carlo correlation result that raising pairwise correlation leaves the **mean unchanged** while fattening both tails. **But the most useful findings are not about securitisation at all** — §7 of that file carries three originator-analysis traps that apply to every lender we rate, and the first of them is now failure mode 59: an asset-quality improvement reported without write-offs, found live in four delivered cases.)*

*Guide version 1.8 — 06-Sep-2026 (CRISIL expected-loss criteria read in full and written up as `CRISIL_INFRASTRUCTURE_CONVENTIONS.md` §9. **EL is a separate seven-point scale with published numeric bands** — EL = PD × LGD over the instrument's original maturity, capped at project life — and `Rating_Scorecard.xlsx` has no EL scale at all, so EL mandates are rated outside it. The conceptual trap: **PD is assessed on base-case conditions and LGD on tail scenarios**, so one scenario set cannot produce both. New failure mode 58 with an 11-control arithmetic probe. Separately, a workflow guard: `test_no_control_chars.py`, after a `` word boundary was silently written as a literal backspace byte six times in one session — a regex that matches nothing and passes everything.)*

*Guide version 1.7 — 06-Sep-2026 (CRISIL infrastructure criteria read in full — all four sections plus the P90 annexure — and written up as `CRISIL/CRISIL_INFRASTRUCTURE_CONVENTIONS.md`. Headline findings: the **DSCR formula excludes parent support and DSRA**, stated three times and easy to get wrong in exactly the cases where it inflates the number; DSCR is **calibrated by asset class** (transmission can run thin, toll and renewables need more); renewables use the **P90 PLF**, with seasonality liquidity floors of ~2 months of debt obligation for solar and at least 4 for wind; and infrastructure **inverts three corporate instincts** — pricing flexibility, demand risk and monopoly. New failure mode 57 plus four infrastructure `SECTOR_KPI` entries. Also recorded: the analytical root of failure mode 52 — CRISIL's criteria actively try to delink an SPV from its sponsor, which is why the parent-support notch-up is capped at 1-2.)*

*Guide version 1.6 — 06-Sep-2026 (CRISIL full-corpus pass, the counterpart to the CareEdge one. Read in full: `basics-of-ratings.md` Sections I-V, VII and XII; the manufacturing criteria's Section I; **all four** sections of the parent/group/government linkage criteria; **both** sections of the consolidation criteria. Four findings changed the flow: a **third hybrid cap** (CRISIL corporate 20% of adjusted net worth) that the FM51 check had been blind to; **facility-type-specific default recognition** (30 days for working-capital and non-fund-based facilities, not 1 day) which the SOP had stated as a single generic rule; the **notch-DOWN direction**, entirely absent from Step 13; and **no outlook on a C or D grade**, which the scorecard could have generated. New failure modes 54-56. Still unread and named as such in the conventions files: infrastructure, securitisation, real estate/LRD/CMBS, public finance, insurance, and the fund/ICE/holding-company/security-receipt criteria.)*

*Guide version 1.5 — 13-Sep-2026 (BLOCKING probe tier added on operator instruction: a quality probe named in `check_sections.py`'s `BLOCKING_PROBES` now stops delivery instead of warning, because the corpus run showed three cases tripping the business-risk gate, printing the warning and still reading READY TO SHARE — failure mode 35 in miniature. Two entries so far. All four flagged cases worked through; the new prior-rating probe found a fifth, Creative Newtech.)*

*Guide version 1.4 — 13-Sep-2026 (methodology + flow sync after reading the CareEdge, ICRA and CRISIL cross-cutting corpora. **Six corrections, three of which were live falsehoods in this file:** (1) the LT→ST mapping was labelled "identical, SEBI-standard, all three" and given ICRA's own table — it is agency-specific and, within CRISIL, entity-type-specific; (2) Step 12c asserted "ICRA OPBDIT strips other income unconditionally" — ICRA's own methodology footnote says the opposite; (3) §4 listed 15 failure modes against the law's 53, leaving the operating flow 38 behind. Added: the conventions files as a routing step, the Total-Debt-composition and hybrid-cap divergences, the Step 12b **business-risk gate** (FM53), and five scripts the toolchain index had never named — `corpus_table_integrity.py`, `add_business_risk_gate.py`, `step14_diff.py`, `test_fm47_52.py`, and preflight probes `[0e]`/`[0f]`/`[10]`.)*

*Guide version 1.3 — 04-Sep-2026 (added the three MECHANICAL GATES the flow had never named: Step 1a pre-flight, Step 6 mutation coverage, Step 17a delivery loop; added §7 toolchain index and §8 rate_engine; corrected the step count 23→31 headers and the surveillance phase reference 6→8. Found by audit: the guide instructed the operator to "follow it" while omitting both enforcement scripts CLAUDE.md §8a designates as the mechanism — `preflight.py` and `delivery_audit.py` had **zero** mentions in this file.)*

*Guide version 1.2 — 18-Jul-2026 (v1.2 process-governance redesign: added R12–R16 + §0A roles/engagement-types + Reviewer/Committee decision steps 17b/17c + issuer review 18b + Phase 6 surveillance 20/21; basis methodology-determined; materiality defined; anchor governed; entity-appropriate tracks/tie-out; proportionate modelling; structured ESG; outlook-vs-watch. v1.1 14-Jul-2026: source-vs-cross-check; routing restored; rating-history source rule; mandate scope; craft ring-fenced.) On any conflict: CLAUDE.md > this file > the per-agency KB files. **CLAUDE.md §6 was reconciled to this redesign on 18-Jul-2026 (governance overlay: R12–R16, roles, Reviewer/Committee steps 17b/17c, issuer review 18b, surveillance 20/21) — the law and the flow now agree.***
