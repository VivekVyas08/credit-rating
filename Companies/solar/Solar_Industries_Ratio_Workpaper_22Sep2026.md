# Solar Industries India Limited — Ratio Workpaper (ICRA basis)
*Prepared 22-Sep-2026. Data cutoff: FY2025-26 audited (Board approval / audit 15-May-2026). Engagement type: surveillance (CP programme, [ICRA]A1+ reaffirmed and enhanced).*

---

## 1. Document Read Log (Step 1b)

| File | Coverage | Material items found |
|---|---|---|
| `download-file_2.md` (FY2025-26 AR, Rs crore) | Board's report, MD&A, consolidated + standalone financials, auditor's report incl. KAM, credit-rating note (9.9), related-party/AOC-1 entity list, borrowings notes, other-income note | Consolidated revenue Rs 9,837.74 cr (+30.5%), PBT 2,365.22, PAT 1,736.64, net worth (owners) 6,277.20; **CP [ICRA]A1+ (ICRA), CRISIL AA+/Positive LT bank/NCD, CRISIL A1+ ST**; order book ~Rs 21,300 cr; defence revenue Rs 2,634 cr (+94%); capex ~Rs 1,556 cr; promoter 95.11%; acceptances Rs 285.23 cr; 8 direct + 28 step-down subsidiaries + 3 associates |
| `download-file.md` (FY2024-25 AR, Rs crore) | FY2025 + FY2024 consolidated financials | FY2024 base: revenue 6,069.52, PBT 1,161.28, PAT 875.23, net worth (owners) 3,305.60; FY2025 pre-restatement (total assets 8,261.32 vs 8,298.08 restated in FY2026 AR) |
| `download-file_1.md` (FY2023-24 AR, Rs crore) | FY2024 base and pre-defence-ramp history | Read for the earlier base; consistent with the FY2024-25 AR comparatives |
| Quarterly results (Q2/Q3/Q4 FY2026; `download-file_3/4/5/7`, duplicates as `_ (2)`) | Quarterly presentations/results (Feb 3, Nov 10 2025; May 15 2026) | Interim revenue/EBITDA/PAT trend; the "(2)" files are exact duplicates and were read once each |

**Pre-flight (Step 1a) run and recorded.** Key outputs:
1. **Prior rating action PRESENT** — ICRA `Solar Industries India Limited_02 Feb 2026_140695` (CP Rs 500 cr, [ICRA]A1+), CRISIL `_23 Apr 2026` (AA+). Step 14 applies; the CP rated-amount is imported under the five-condition amendment.
2. **AR credit-rating note (9.9) PRESENT** (46 matches) — ICRA CP A1+; CRISIL AA+/Positive (LT), A1+ (ST). The anchor exposure is declared.
3. **[0c] aggregate-note contaminants** — forex gain (111.13 standalone), interest income, investment gains: all non-operating, stripped from OPBDIT (see §4). FY2026 is a forex-GAIN year; no forex loss in other expenses, so the FM36 asymmetry does not arise.
4. **[0e] acceptances Rs 285.23 cr** inside current liabilities — EXCLUDED from Total Debt per ICRA (FM47), retained in TOL.

---

## 2. Methodology routing (Steps 2/3)

| File | Scope test | Applied? |
|---|---|---|
| `960~Corporate Credit Rating Methodology, Jul 2025.md` | Non-financial corporate | **YES** |
| `1026~Chemicals, Rating Methodology, Jun 2026.md` | Chemicals — explosives are an energetic-chemicals manufacture; scope covers commodity/specialty chemical manufacturers | **YES** (nearest sector methodology; the defence business has no dedicated ICRA methodology, so Corporate + Chemicals govern) |

Cross-cutting: Consolidation (basis), Implicit Parent/Group Support (Not Applicable — no rated parent), Liquidity Analysis (descriptor), LT↔ST mapping.

---

## 3. Basis determination (R12)

**CONSOLIDATED.** The group carries the order book, the defence business (SDAL) and overseas mining-services operations across 8 direct + 28 step-down subsidiaries and 3 associates; borrowings and the defence ramp sit across the group. ICRA's own basis is "SIIL + SDAL (Solar Group)"; the full consolidation used here subsumes that and is the reported headline basis.

---

## 4. Ratio suite (ICRA convention, consolidated, Rs crore)

`compute_ratios.py` — **123 of 123 tie-outs reconcile; mutation-measured coverage 100.0%.**

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Operating income | 6,069.52 | 7,540.26 | **9,837.74** |
| OPBDIT (ICRA convention) | 1,369.56 | 1,965.91 | **2,622.08** |
| OPBDIT/OI (%) | 22.56 | 26.07 | **26.65** |
| PAT (incl NCI) | 875.23 | 1,287.93 | **1,736.64** |
| PAT (owners) | 835.93 | 1,209.44 | **1,677.55** |
| PAT/OI (%) | 14.42 | 17.08 | **17.65** |
| Total debt (excl acceptances) | 1,137.84 | 974.95 | **1,524.02** |
|   — of which long-term | 607.31 | 739.61 | 1,219.06 |
|   — of which short-term | 530.53 | 235.34 | 304.96 |
| Tangible net worth (owners) | 3,305.60 | 4,413.22 | **6,277.20** |
| TOL/TNW (times) | 0.70 | 0.84 | **0.70** |
| Total debt/OPBDIT (times) | 0.83 | 0.50 | **0.58** |
| Interest coverage (times) | 12.52 | 16.87 | **19.57** |
| Gearing (times) | 0.34 | 0.22 | **0.24** |
| Liquid inv + cash | 500.70 | 1,254.45 | **584.14** |
| Inventory days | 50.9 | 50.3 | 64.6 |
| Debtor days | 50.8 | 60.0 | 68.9 |

**Reconciliation to ICRA's published figures (02 Feb 2026):** ICRA reports TD/OPBDITA ~0.5x FY2025 (here 0.50x ✓) and ~0.4x H1FY26; interest coverage ~17.2x FY2025 (here 16.87x — within rounding of the small OPBDIT-convention/period difference) and 18.6x H1FY26; OPM ~24-26% FY2024/FY2025 (here 22.56%/26.07%). All consistent.

**OPBDIT convention (FM36).** Other income is interest, net forex gain and investment gains — non-operating, stripped in full. The GST/sales-tax subsidy sits in Revenue ("other operating revenues"), correctly retained. Company's own EBITDA ~Rs 2,750 cr retains other income (2,622 + 128 ≈ 2,750).

**Debt composition (FM47).** ICRA total debt = non-current + current borrowings + leases; **acceptances Rs 285.23 cr EXCLUDED** (in TOL). Gearing 0.24x, TOL/TNW 0.70x.

---

## 5. Methodology Compliance Map (Step 10)

| Rating factor | Company evidence | Assessment |
|---|---|---|
| **Industry / operating environment** | Commercial explosives (mining/infra demand) + fast-growing defence; energetic-chemicals manufacture | Favourable growth, moderate cyclicality (rubric score 2) |
| **Scale & market position** | Market leader in Indian commercial explosives; Coal India/SCCL/exports; defence order book; revenue Rs 9,838 cr (+30.5%) | **Strong** — the binding qualitative strength |
| **Operating efficiency / margin** | OPBDIT/OI 22.56 → 26.07 → 26.65%; backward integration | **Strong** and improving |
| **Leverage** | Gearing 0.24x; TD/OPBDIT 0.58x; TOL/TNW 0.70x | **Very strong** |
| **Coverage** | Interest coverage 19.57x | **Very strong** |
| **Working capital** | Inventory 64.6 days, debtor 68.9 days; expanding with defence ramp | Moderate — the main watch item |
| **Liquidity** | Cash + investments Rs 584.14 cr; capex internally funded | **Strong** (§7) |
| **Management & governance** | Promoter 95.11%; professional team; unmodified audit | Adequate-to-strong |
| **Parent / support** | Promoter-owned, no rated parent | **Not Applicable** |

---

## 6. Support assessment — Parent/Group support: Not Applicable

Solar is a promoter-owned (95.11%) listed group with no rated parent whose credit could be notched onto it, and no external guarantee. The rating rests on the consolidated profile; no uplift or drag. FM56 checked — there is no weaker parent to drag it.

---

## 7. Liquidity (Step 11) — Strong

**Sources:** cash, bank balances and current investments of Rs 584.14 crore (Mar-2026); FY2026 operating cash generation well above the Rs 133.97 crore interest bill (coverage 19.6x); strong internal accruals that fully fund the base-case capex (no new debt FY2027-FY2031). **Claims:** modest debt of Rs 1,524.02 crore, largely long-tenor term debt/NCDs (Rs 1,219.06 cr) plus short working-capital lines; capex ~Rs 1,556 cr/year, self-funded. **Descriptor: Strong** — a large multi-year capex/defence build-out consumes much of the free cash flow (Strong not Superior); ample accrual and balance-sheet headroom means no near-term pressure (Strong not Adequate).

---

## 8. Step 12 forward view + 12b anchor

`forward_model.py` (base + stress). Base case: revenue growth ~13-22% tapering off the order book, margin held ~26.5-27%, capex Rs 1,200-1,600 cr — **funded entirely from internal accruals**, leverage falling to <0.15x TD/OPBDIT and coverage rising above 24x. Stress (growth halved, margin to ~22.5%, capex held): leverage stays well inside 1x TD/OPBDIT and coverage above 10x. Step-12 scaling: a focused forward model on the rating-driving variables (order-book conversion, margin, capex/funding gap) — proportionate for a CP-only, top-grade, stable surveillance mandate; recorded in `case.json`.

**Stage-1 anchor: AA+ / A1+** (composite 1.65, index 1). Support notches 0. No hard-cap disapplication (coverage 19.6x, strong net worth). Business-risk gate (FM53): business risk (score 2) is a **strength**, not weaker than financial risk, so the gate does not bind. The anchor's long-term AA+ matches CRISIL's published AA+; the **short-term maps to A1+**, which is ICRA's mandate.

**Assigned rating: [ICRA]A1+** (commercial paper). Stage-2 overlay 0 — the anchor already sits at AA+/A1+; the CP short-term rating is the highest grade and no committee overlay is needed. LT/ST mapping (ICRA §8): AAA/AA-band → A1+ always.

---

## 9. Divergence against prior action (Step 14)

ICRA's published action of **02 Feb 2026** (in the reference library):
- **ICRA:** CP Rs 250 → 500 cr, **[ICRA]A1+; reaffirmed and assigned for enhanced amount**. **This exercise reaches [ICRA]A1+ — no divergence.**
- **Basis:** ICRA takes a "SIIL + SDAL (Solar Group)" view; the full consolidation used here subsumes it. Immaterial to the ratios.
- **Ratio reconciliation:** TD/OPBDIT 0.50x/0.50x (FY2025), coverage 16.87x/~17.2x, OPM 26.07%/24-26% — all tie.
- **Defence order book:** ICRA cites Rs 16,000 cr defence order book (Sep-2025, incl Rs 6,084 cr Pinaka); the AR's ~Rs 21,300 cr is the TOTAL group order book (FY2026) — both real, different scopes and dates, stated as such.
- **CRISIL:** rates the LT bank/NCD AA+/Positive and ST A1+ — outside ICRA's mandate; noted, not rated here.

---

## 10. Surveillance (R15)

Next review ≥ annual (bank-loan facilities are CRISIL's, not in scope; the CP is ICRA's). Event-driven triggers: (1) a large debt-funded acquisition/capex step-up lifting leverage materially; (2) a sharp/prolonged demand or ammonium-nitrate cost shock compressing margins; (3) a stretch in the working-capital cycle as the defence book executes; (4) any material change in the group structure or promoter stance. Default monitoring: 1-day/1-rupee on the CP programme (scheduled-repayment instrument).
