# Indus Towers Limited — Ratio & Analytical Workpaper
**Agency: CRISIL | Sector: Telecom passive infrastructure (towers) | Basis: CONSOLIDATED | Data cutoff: Q1 FY2026-27; audited base FY2025-26 (AR signed 30-Apr-2026)**

---

## 1. Document Read Log (Step 1b)

| # | Document | Words | Contribution | Material items |
|---|---|---|---|---|
| 1 | Indus-IR-fq-2026.md (FY26 Integrated Report) | 173,171 | **Audited base** — consolidated BS L15152-15212, P&L L15238-15280, **Note 32 Other expenses L17160-17171** | **The write-back finding (below)**; 264,514 towers / 428,014 co-locations; auditor Deloitte Haskins & Sells LLP |
| 2 | Indus-Tower-AR-2025…md (FY25 AR) | 181,241 | FY24 comparative P&L (L12955-12990) and BS | Confirms FY25 write-back of Rs 50,771 mn |
| 3 | IndusTowers_AnnualReport_FY24…md | 172,738 | FY24 base / longer-run context | — |
| 4-8 | Quarterly-Report Q1FY26 → Q1FY27 | 11.5k-22.6k each | Quarterly build; Q1FY27 is the data cutoff | — |
| 9-20 | **12 × term-sheet / SEBI NCD filings** | 167-822 each | **Issuer-filed instrument data** — ISINs, allotment, maturity, coupon, amount issued/outstanding, trustee, listing, record dates, redemption confirmations | **First case in this project with real instrument documents** — Annexure I is issuer-sourced, not TBC |

**Declared gap:** no sector-assumptions/broker note — no external forward view of any kind. All forward statements are my own, labelled.

---

## 2. ⚠ THE BINDING NORMALISATION — reported figures tell the opposite story

Note 32 (Other expenses) discloses **"Allowances for doubtful receivables and advances (net)"**:

| | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Allowance line (Rs mn) | none material | **(50,771)** | **(2,560)** |

Both are **net reversals** — write-backs of provisions previously taken against receivables, consistent with the **Vodafone Idea recovery**. They sit inside "Other expenses" and therefore inside reported EBITDA, PBT and PAT. In FY25 they turned the entire "Other expenses" line negative (a Rs 44,531 mn credit).

**Consequence if not normalised:**

| | FY2025 | FY2026 | Change |
|---|---|---|---|
| EBITDA **as reported** | 21,190 | 18,453 | **−12.9% — looks like a collapse** |
| EBITDA **normalised** | 16,113 | 18,197 | **+12.9% — the business grew** |
| Normalised margin | 53.5% | **56.0%** | +250bps |

Every ratio in this workpaper is computed on the **normalised** basis with reported shown alongside. Presenting the reported trend without this adjustment would misstate the direction of the credit.

---

## 3. Computed ratio suite (consolidated, Rs crore — `compute_ratios.py`)

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Revenue | 28,601 | 30,123 | **32,493** |
| EBITDA (normalised) / margin | 15,055 / 52.6% | 16,113 / 53.5% | **18,197 / 56.0%** |
| EBITDA (reported) | 15,055 | 21,190 | 18,453 |
| PAT (normalised) | 6,036 | 6,098 | **6,954** |
| **Borrowings only** | 4,312 | 2,262 | **921** |
| Lease liabilities | 16,219 | 18,893 | 20,206 |
| Debt incl. leases | 20,531 | 21,156 | 21,127 |
| Liquid assets | 63 | 3,342 | **5,858** |
| **Net debt excl. leases** | 4,249 | **(1,080)** net cash | **(4,937) NET CASH** |
| Net debt incl. leases | 20,468 | 17,814 | 15,269 |
| Gearing excl. / incl. leases | 0.159x / 0.76x | 0.070x / 0.65x | **0.023x / 0.53x** |
| TOL/TNW | 1.07x | 0.94x | **0.80x** |
| Net debt (incl leases)/EBITDA | 1.36x | 1.11x | **0.84x** |
| Interest coverage | 8.1x | 8.7x | **9.6x** |
| RoCE | 18.9% | 18.1% | 18.2% |
| **Receivable days** | 82 | 58 | **55** |

**Lease treatment — stated, not buried.** CRISIL's adjusted-debt convention includes lease liabilities. For a tower operator, ground leases are the dominant liability: **Rs 20,206 crore of leases against Rs 921 crore of borrowings** at FY26. Reporting only one basis would materially mislead in either direction — excluding leases makes the company look almost debt-free; including them makes it look 22x more levered than its borrowings. Both are shown throughout.

**Tie-out (corroboration gate):**
- FY26 balance sheet balances: assets 71,316 = equity 39,646 + liabilities 31,670 ✓
- **FY26 EPS cross-check: PAT Rs 71,449 mn ÷ 2,638.1 mn shares = Rs 27.08 vs reported Rs 27.09** ✓
- FY25 EPS cross-check: computes to Rs 37.65 vs reported **Rs 37.31** — a 0.9% gap, **flagged not ignored**; almost certainly a weighted-average share count during FY25 differing from the year-end count. Immaterial to every ratio (no ratio uses per-share data), but recorded.
- Note 32 components reconcile to the P&L "Other expenses" line in both years ✓

---

## 4. Business profile

**Scale and position:** 264,514 towers and 428,014 co-locations — India's largest telecom tower operator, providing passive infrastructure on long-term contracts. Revenue of Rs 32,493 crore with a 56.0% normalised EBITDA margin reflects the annuity-like economics of the model: contracted rentals, high operating leverage, and energy costs (power and fuel of Rs 11,996 crore, 37% of revenue) largely passed through.

**The defining risk — customer concentration and counterparty quality.** The Indian tower market is served by three mobile network operators, and Indus's revenue is concentrated in **Bharti Airtel** (also its major shareholder) and **Vodafone Idea**. The Rs 50,771 mn provision reversal in FY25 and Rs 2,560 mn in FY26 are direct, audited evidence that receivables from a major customer were previously assessed as doubtful and have only recently been recovered. Receivable days have normalised from 82 (FY24) to 55 (FY26), and the FY26 report notes Vodafone Idea's AGR relief and resumption of network investment after a prolonged period of constrained spending — but the exposure to a financially stressed counterparty is structural, not resolved.

**Related-party dimension:** Bharti Airtel Limited is both the largest customer and the controlling shareholder. This aligns interests and underpins the tenancy base, but it also means concentration cannot be diversified away within the current market structure.

---

## 5. Materiality sweep (Step 8)

| Finding | Decision | Reason |
|---|---|---|
| **Allowance write-backs (Rs 50,771 mn FY25, Rs 2,560 mn FY26)** | **Normalise, and make it a named driver** | Reverses the apparent earnings direction — the single most important analytical adjustment in this case |
| Lease liabilities Rs 20,206 crore vs borrowings Rs 921 crore | **Both bases reported throughout** | Presenting one alone materially misleads |
| Borrowings fell 79% over two years (Rs 4,312 cr → Rs 921 cr) | Include | Deleveraging is a core strength |
| NCD programme fully redeemed within FY26 | Include in Annexure I | Confirmed from issuer-filed SEBI statements |
| Depreciation adjusted with general reserve under a Scheme of Arrangement (Rs 795 mn FY26, Rs 878 mn FY25) | Note; no adjustment | Presentation item disclosed by the company; immaterial to leverage/coverage |
| FY25 EPS 0.9% cross-check gap | Flag, unresolved | Weighted-average share count; no ratio affected |

---

## 6. Liquidity (Step 11)

| Sources | Rs cr | Claims | Rs cr |
|---|---|---|---|
| Cash + bank balances | 1,552 | Current borrowings | 921 |
| Current investments | 4,305 | Current lease liabilities | 2,677 |
| FY26 normalised cash accrual (PAT + dep) | 14,095 | Non-current borrowings | **nil** |

**Conclusion: Superior.** Liquid assets of Rs 5,858 crore exceed **all** borrowings of Rs 921 crore by more than six times — the company is **net cash of Rs 4,937 crore excluding leases** — and normalised annual cash accrual of Rs 14,095 crore is roughly fifteen times total borrowings. Non-current borrowings are nil. Lease obligations are contractual operating commitments serviced from the same rental streams they support, not a refinancing risk. *(Bank-limit utilisation data was not available, but with liquid assets exceeding total borrowings six-fold the descriptor does not turn on it.)*

---

## 7. Rating view (Step 13)

**Standalone assessment.** The financial profile is very strong and improving on every measure: normalised EBITDA margin expanded 340bps over two years to **56.0%**, borrowings fell **79%** to Rs 921 crore, the company moved to **net cash excluding leases**, interest coverage reached **9.6x**, TOL/TNW improved to 0.80x, and receivable days normalised from 82 to 55 as the Vodafone Idea position recovered. RoCE is steady at ~18% on a capital base that includes Rs 20,206 crore of capitalised ground leases.

**Constraint.** Revenue is concentrated in two mobile network operators, one of which — Vodafone Idea — has a materially weaker credit profile, evidenced in these very accounts by Rs 5,077 crore of provisions taken and subsequently written back. Recovery is real and receivable days confirm it, but the concentration is structural: it cannot be diversified within a three-operator market, and a renewed deterioration at that counterparty would flow directly into receivables and cash conversion.

**Support notching:** none applied. Bharti Airtel is the controlling shareholder and largest customer; the relationship is commercially integral rather than a support undertaking, and no guarantee or keepwell is disclosed in the documents reviewed. Indus is rated on its standalone profile.

**LT/ST mapping:** at AA+ (corporates), CRISIL's Table 1 maps to **A1+**.

**Independent view: Crisil AA+ / Stable · Crisil A1+.**

**The AA+ vs AAA judgment call, stated openly.** On the financial metrics alone — net cash excluding leases, 9.6x coverage, 56% margins, nil long-term borrowings — a case for AAA exists. I have settled one notch below because concentration risk here is not theoretical: the accounts themselves record a Rs 5,077 crore provision cycle against a single counterparty within the last two years. AAA denotes the highest safety with essentially no adverse-scenario sensitivity; a revenue base dependent on a stressed operator does not meet that bar, however strong the balance sheet. **The factor that would move this to AAA is a durable improvement in counterparty quality or genuine customer diversification** — not further balance-sheet strengthening, which is already close to its practical limit.

**Step 14 divergence:** no prior CRISIL action for Indus Towers was found in the reference library and the supplied documents contain no credit-rating note. View formed with **no anchor exposure** and no external benchmark.

---

## 8. Disclosed scoping decisions (Rule 1)

1. **Routing:** the case was created under the generic manufacturing master. Indus is **telecom passive infrastructure** — I applied Section I (base framework) and Section IV (financial ratios), and treated the annuity/contract-rental economics and counterparty concentration explicitly rather than forcing a manufacturing sector template. CRISIL's Section XI covers *mobile telephony services* (operators), whose scope does not fit a tower landlord; the infrastructure criteria are the closer analogue and the business-risk factors used are drawn from that logic. **Declared as a judgment call, not a clean scope match.**
2. **Annexure I is issuer-sourced** — a first for this project (see §9 in the rationale).
3. **FY25 EPS 0.9% cross-check gap** flagged, unresolved (§3).
4. **5-year model and scorecard anchor (Steps 12/12b) not built.** The forecast turns on tenancy/co-location additions and Vodafone Idea's capex trajectory; with no broker note or sector-assumptions document supplied there is no external anchor for either, and inventing one would be false precision. **Offered as the next step.**
5. **Peer reports not read for this sector** — the CRISIL peers read earlier in this session are auto-component manufacturers; tower/infrastructure calibration does not transfer. Limitation on peer benchmarking strength behind the AA+/AAA call.

---

*Every figure computed in `compute_ratios.py` from audited consolidated statements or traced to a document location. Instrument data is from issuer-filed SEBI statements. No CRA-published amount used as data.*

---

## STEP 12 / 12b — FORWARD VIEW AND SCORECARD ANCHOR (added 01-Sep-2026)

**Anchor grade: Crisil AA+/Stable / Crisil A1+.** Rating in the corrected rationale:
**Crisil AAA/Stable**. The divergence is **one notch**, well inside the ±2 screening band.

**The anchor landing on AA+ is itself the finding, and it is worth stating plainly.** AA+ is
exactly where the ORIGINAL, withdrawn draft of this rationale landed — the draft that capped the
rating for counterparty concentration and was corrected on 13-Aug-2026 under failure mode 22.
The scorecard, fed nothing but audited financials and the qualitative scores, reproduces that
answer. That is not a coincidence and it is not a criticism of the scorecard: it is the anchor
behaving exactly as its back-testing says it does. **The entire step from AA+ to AAA is
qualitative** — it rests on reading the Vodafone Idea provision write-backs as evidence that a
risk has RESOLVED rather than evidence that it is live, and on recognising that a subsidiary
which has outgrown its parent support notch is showing an upgrade signal. No financial ratio
carries that reading, which is precisely why the support notch is entered as **0** and the
argument is made in the rating view instead of being absorbed into a notch.

**What the scorecard is actually measuring on this issuer.** Total debt on the CRISIL adjusted
convention is Rs 21,126.9 crore, of which **Rs 20,206.0 crore — 95.6% — is ground-lease
liabilities** and only Rs 920.9 crore is borrowed money. The gearing and debt/EBITDA cells
therefore describe a contractual, revenue-matched obligation, not leverage in the ordinary
sense. On borrowings alone the ratios are: borrowings/OPBDITA 0.05x, and liquid resources of
Rs 5,857.5 crore against total borrowings of Rs 920.9 crore — 6.4x cover on the whole book.
Both bases are reported here because presenting only one would materially mislead.

### The forward view

| | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---|---|---|---|---|
| Tenancy ratio (base) | 1.611 | 1.611 | 1.612 | 1.615 | 1.620 |
| Tenancy ratio (stress) | 1.554 | 1.496 | 1.444 | 1.402 | 1.366 |
| Normalised OPBDITA (base) | 19,313 | 20,725 | 21,943 | 23,460 | 24,772 |
| Normalised OPBDITA (stress) | 17,177 | 16,576 | 16,271 | 16,289 | 16,469 |
| Funding gap (base) | (4,331) | (5,821) | (7,122) | (8,655) | (9,546) |
| Funding gap (stress) | (2,743) | (2,734) | (2,902) | (3,320) | (3,369) |

**The funding gap is NEGATIVE in every year of both cases.** The company does not need external
funding even while spending more than Rs 8,000 crore a year of capex, and even if tenancy falls
to 1.366x and revenue per co-location declines for three consecutive years. Borrowings, already
down 79% in two years (Rs 4,311.8 crore to Rs 920.9 crore), extinguish in FY2027 in the base
case. This is the arithmetic behind the **Superior** liquidity descriptor.

**What the model deliberately does not assume: a distribution policy.** The surplus accumulates
in the projection, which is not a forecast that it will. Three historical years produced a
Rs 2,640 crore buyback (FY2025), nothing (FY2024) and nothing (FY2026) — two different answers
and no stated policy, so any payout assumption would be invented. The cash and net-worth lines
are a residual, not a projected balance sheet. The credit conclusion is unaffected: a
distribution large enough to matter would still leave the gap negative in every year.

**The monitorable is tenancy, not leverage.** The ratio has fallen two years running because
towers were added faster than tenants were found for them, including 12,606 towers and
co-locations acquired from Bharti Airtel in FY2025. The exposure on this credit runs to the
earnings level through a three-operator customer market — not to the capital structure.
