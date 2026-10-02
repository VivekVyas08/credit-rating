# Rating Committee — Minutes

**Issuer:** Cochin Minerals and Rutile Limited · **Agency:** CareEdge · **Date:** 13 September 2026
**Engagement type (R15):** new assignment, first-time · **Basis:** Standalone

---

## 1. Attendance and roles (R14/R16)

Chair · Lead Analyst (presented; **proposed** view only, Step 15) · Independent Reviewer
(four-eyes, Step 17b) · three voting members. The operator supplied documents and raised the
request; the operator did **not** set the grade.

## 2. Package before the Committee

Rationale draft · workpaper · `compute_ratios.py` (**30/30 tie-outs, 94.3% mutation coverage**
of 105 inputs) · `CMRL_Financial_Spreads.xlsx` · `CMRL_5yr_Model.xlsx` (base + stress) ·
`Rating_Scorecard_...xlsx` · pre-flight output.

## 3. Decision

| | Long-term | Short-term | Outlook |
|---|---|---|---|
| Analyst proposal (original, 13-Sep-2026) | CARE A- | CARE A2+ | Stable |
| Committee decision (original, 13-Sep-2026) | CARE A- | CARE A2+ | Stable |
| **Committee decision (REVISED, 13-Sep-2026 — see §3a)** | **CARE BBB** | **CARE A3+** | **Stable** |

### 3a. Revision — the original decision was made on a defective anchor

The Committee reconvened the same day after two errors were found in the package it had relied on.

**(i) A false absence-claim removed Step 14 entirely (failure modes 20/24/29).** The rationale
asserted three times, in bold, that no CRA had published a rating action for this issuer.
CareEdge's own action of **04 September 2026** — nine days earlier — was in
`CareEdge/Report for Reference/`, and `preflight.py` probe [1] had reported it **PRESENT**,
printed its rated-amount lines and stated in terms *"You may NOT write 'no prior rating action'."*
The mechanical gate worked; the report contradicted it, and no check compares a report against the
pre-flight output. The published action reads **CARE BBB; Stable / CARE A3+**, held continuously
since 01-Dec-2023.

**(ii) Business risk was averaged into the financial composite (failure mode 53).** The scorecard
blended a descriptive business-risk judgement with numerically banded financial ratios, so an
effectively unlevered balance sheet carried the Stage 1 anchor to AA-. Applying business risk as a
**ceiling** instead — `Inputs!C69 = BBB`, justified at `D69` — moves the anchor to BBB and the
short-term grade to A3+, **with zero overlay notches**, reproducing the published action on both
scales.

**Decision.** The Committee substitutes **CARE BBB; Stable / CARE A3+** for its original
CARE A-; Stable / CARE A2+. Rated amounts are imported from the published action under the
five-condition amendment and labelled CRA-published, not issuer-confirmed. Two divergences remain
open (FY2025 PBILDT; the LC-backed creditor split behind the gearing difference) and are disclosed
in the report's Step 14 table rather than closed by adjusting inputs.

**Dissent:** none recorded. **Anchor divergence:** nil — the anchor and the assigned rating now
agree, which is itself the point: the previous 3-notch bridge was doing work the ceiling should
have done.

**Rated amounts: TO BE CONFIRMED BY ISSUER.** LT→ST mapping checked: A− maps to A2+.

**Vote: 3–0. No dissent.**

## 4. The pre-flight hit the Committee expressly rejected

The Committee was shown that pre-flight probe [1] returned **Cochin Shipyard Limited**, carrying
₹2,280 crore of rated facilities, and **Sarda Energy & Minerals Limited**, on partial name
overlap only (match 1/3). **Neither is this issuer.** The Committee directed that:

1. no peer's rated amount be imported — importing one is a worse error than leaving the amount to be confirmed (failure mode 29's own warning);
2. the absence of any prior rating be stated as **evidenced**, resting on a word-boundary search of all three libraries returning nothing and on probe [2] finding **zero** rating disclosures across three annual reports;
3. Annexure-2 record a first assignment with **no invented history**.

## 5. Anchor divergence — expressly resolved (>±2 notches)

Stage 1 anchor **AA−** (index 3) → Stage 2 overlay **−3** → Stage 3 **CARE A−; Stable**.

- **−2 scale and concentration:** ₹294.92 crore of revenue, a single product, a single site. The manufacturing criteria make size, market share and diversification explicit business-risk factors and this issuer is weak on each.
- **−1 raw-material access:** domestic ilmenite supply has "declined significantly" on the Company's own account, forcing imports; the metallisation project was impaired and abandoned for precisely this reason.
- **Support notches: nil.** Standalone listed issuer, no group support claimed.
- **Hard caps left live** — accrual metrics are meaningful for a manufacturer.

The Committee noted that the anchor is high **because the financial inputs are close to ideal**
— negligible debt, net cash, 122x coverage — and that the entire risk in this credit sits
outside the financial statements. It recorded this as a clean illustration of why the scorecard
is a screening band and not a rating.

## 6. What the Committee weighed

**The balance sheet is not the question.** Total debt is ₹6.21 crore against ₹172.03 crore of
net worth and ₹38.17 crore of unencumbered cash. Even in the stress case — revenue back to
₹285 crore and margin at 5.5% — the Company retains ₹28.60 crore of net cash. There is no
servicing or refinancing question at any point in the projection.

**The business is the question.** Revenue fell 7.6% in FY2026, the PBILDT margin compressed for
a second year to 7.96% from 12.61% two years earlier, PAT halved and RoCE fell to 12.28% from
24.02%. The cause is a conversion-spread squeeze the Company does not control: synthetic rutile
realisations fell while ilmenite did not follow.

**The write-off is the most informative single fact.** The ₹5.05 crore impairment of the
metallisation CWIP, abandoned for "short supply of main raw material, ilmenite from the
domestic market", demonstrates that the constraint has already cost the Company a growth
avenue. The Committee treated it as business-risk evidence, not as an earnings charge — it is
excluded from PBILDT by construction.

**Why Stable and not Positive.** Q1 FY2027 is a genuine and large improvement: revenue +72.2%
year on year, profit before exceptional items +231%, and one quarter's PAT within 1% of the
whole of FY2026. The Committee weighed a Positive outlook and rejected it: **one unaudited,
seasonally unadjusted quarter is not a trend**, and the underlying ilmenite constraint is
unresolved. It set the positive triggers so that a sustained recovery would be recognised.

**Why not higher.** A rating above A− would require the scale and diversification the issuer
does not have. Its financial profile alone would support more; its business profile will not.

## 7. Surveillance (R15)

Next scheduled review by **13 September 2027**. Event-driven triggers: any interruption to
ilmenite availability, domestic or imported; PBILDT margin below 6% or revenue returning to the
FY2026 level; overall gearing above 0.50x or erosion of the net cash position; any debt-funded
capital expenditure; confirmation of sanctioned limits by the issuer, which would allow the
rated amounts to be stated. Default monitoring: 1-day/1-rupee → D.

## 8. Outstanding

**Sanctioned facility limits remain unconfirmed.** The Committee asks that term sheets or
sanction letters be obtained from the issuer, which is the only route to stating a rated amount
for this issuer — no CRA publication exists to import one from, and none should be.

*Minuted 13 September 2026.*
