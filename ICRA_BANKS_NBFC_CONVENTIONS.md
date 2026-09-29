# ICRA — financial sector (Banks/AIFIs and NBFCs): ratio, capital-instrument and notching conventions

**Source, read 13-Sep-2026:** `929~Banks & Financial Institutions, Rating Methodology, Oct 2024.md` (full) and `1003~NBFCs, Rating Methodology, Dec 2025.md` (full), read this session to complete the financial-sector half of ICRA's cross-cutting corpus (the corporate half is in `ICRA_CONVENTIONS.md`). This is the twin of `CRISIL/CRISIL_BANKS_NBFC_CONVENTIONS.md`.

This file exists because FM28 and FM32 in `CLAUDE.md` were both learned the hard way, on NABKISAN and HDFC Securities respectively — reporting bank-style metrics for an NBFC, or a generic net-worth basis instead of the agency's own. The definitions below are quoted or closely paraphrased from the methodology text, not inferred.

---

## 1. Banks and AIFIs — the five-factor framework

Industry Risk (operating environment, regulatory environment) → Business Risk (franchise, management/governance/reporting, risk management) → Financial Risk (asset quality, funding & liquidity, profitability, capital adequacy) → Promoter Support & Financial Flexibility → ESG. Franchise assessment explicitly **does not apply to AIFIs**, which are wholesale-funded by lending mandate rather than deposit franchise — do not penalise an AIFI for lacking a branch network or CASA base.

### Asset quality — indicative bands

| Metric | Strongly positioned | Weakly positioned |
|---|---|---|
| Gross NPA % | ≤2% | ≥6% |
| Net NPA % | ≤0.7% | ≥3.3% |
| Advances growth vs sector 3-yr CAGR | ≥+6% (>+20% over sector average is itself negatively assessed) | ≤−2% |
| Fresh slippage rate (annualised) | ≤1% | ≥4% |
| Top 20 group exposures / total exposures | ≤8% | ≥16% |

**Divergence disclosure threshold (RBI-mandated, and a genuine absence-claim trap):** banks must disclose asset-classification/provisioning divergence from RBI supervisory findings if additional provisioning required exceeds **10% of published profit before provisioning**, or additional gross NPAs identified exceed **15% of published incremental gross NPAs**. A search for "divergence" that returns nothing is not evidence of a clean book unless you've confirmed the disclosure obligation wasn't triggered — check both thresholds.

### Funding and liquidity — indicative bands

| Metric | Strongly positioned | Weakly positioned |
|---|---|---|
| Market share in deposits | ≥2.0% | ≤0.3% |
| CASA ratio | ≥45% | ≤30% |
| Cost of interest-bearing funds vs sector average | ≤−0.5% | ≥+0.5% |
| CASA growth vs sector 3-yr CAGR | ≥+6% | ≤−2% |
| Top 20 depositors / total deposits | ≤8% | ≥16% |
| LCR | ≥120% | ≤100% (regulatory floor) |
| NSFR | ≥120% | ≤100% (regulatory floor) |
| Credit-to-deposit (net worth included in denominator) | 75% | 90% |

**Credit-to-deposit ratio is adjusted to include net worth in the denominator** — do not compute a plain advances/deposits ratio and compare it to this band.

### Profitability — indicative bands

| Metric | Strongly positioned | Weakly positioned |
|---|---|---|
| NIM / Average Total Assets (ATA) | ≥3.5% | ≤2.5% |
| Core operating profit (pre-provisioning) / ATA | ≥3.0% | ≤2.0% |
| RoRWA | ≥1.8% | ≤0.8% |
| Provision coverage ratio (excl. write-offs) | ≥67% | ≤45% |
| Operating income growth | ≥20% | ≤6% |
| Core fee income / total income | ≥30% | ≤15% |

**A high RoE is not automatically a positive** — ICRA states this explicitly: it may reflect excessive underlying risk or excessive leverage rather than genuine strength. Never cite RoE alone as a strength driver.

### Capital adequacy — Basel III schedule and indicative bands

Regulatory minima (post 01-Oct-2021, as % of RWA): **CET1 5.50% + CCB 2.50% = 8.00% minimum**; Tier I 7.00% (+ CCB → 9.50%); total CAR 9.00% (+ CCB → 11.50%). D-SIB and CCCB add-ons stack on top.

| Metric | Strongly positioned | Weakly positioned |
|---|---|---|
| CET1/core capital, absolute (Rs crore) | ≥60,000 | ≤5,000 |
| Net NPA / CET1 (solvency) | ≤10% | ≥40% |
| CET1 cushion above regulatory level | ≥5.0% | ≤1.0% |
| Tier I cushion above regulatory level | ≥5.0% | ≤1.0% |
| CAR cushion above regulatory level | ≥5.0% | ≤1.0% |
| Leverage ratio (Tier I / total exposure) | ≥8.0% | ≤4.0% (regulatory floor: 4.0% D-SIB, 3.5% others) |
| Price/Book | ≥2.0x | ≤0.9x |
| Price/Earnings | ≥15x | ≤9x |
| RoE | ≥15% | ≤9% |
| Tier I requirement over next year / market cap | ≤0% | ≥25% |

**Solvency profile** = Net NPA / (Tangible Net Worth or CET1) — the capital coverage available for the UNPROVIDED portion of NPAs. Extend the same ratio to net non-performing investments and net security receipts held from ARCs where material.

### Basel II vs Basel III capital-instrument notching — a full, codeable decision tree

| Instrument | Coupon deferral trigger | Principal write-down/conversion | ICRA's rating |
|---|---|---|---|
| Basel II-Lower Tier II | None (no CRAR-linked constraint) | No | = base/senior/issuer rating |
| Basel II-Upper Tier II | CRAR < 9% regulatory minimum; interest **cumulative** | No | Notched down from senior |
| Basel II-Tier I / IPDI | CRAR < 9%; interest **non-cumulative** | No | Notched down from senior (ICRA does not distinguish this from Upper Tier II on notching, despite the higher LGD of non-cumulative interest, because ratings reflect PD not LGD) |
| Basel III-Tier II | No coupon constraint; write-off/conversion **only at PONV** | Yes, at PONV | Base rating, but **notched down for lower-investment-grade or non-investment-grade banks** (higher PONV probability) |
| Basel III-Tier I (AT1) | Coupon restricted once CET1 (incl. CCB) < 8.0%; capital-conservation schedule below that (100% conservation at 5.50–6.125% CET1, tapering to 0% above 8.0%) | Yes, write-off/conversion at CET1 < **6.125%** or PONV | **Notched down from senior**, extent driven by (a) asset quality/profitability outlook, (b) level of distributable reserves, (c) relative CET1 cushion and track record of maintaining it, (d) capital-raising ability/investor diversity |

**PSB-specific carve-out:** ICRA notches Basel III-Tier I bonds down from the **supported** (government-uplifted) rating of a PSB, not its standalone profile — because of a demonstrated track record of GoI regulatory relaxations and capital support timed to protect Tier I coupon servicing (RBI's February 2017 redefinition of distributable reserves; early call-option exercise directives in 2018; share-premium-account loss offsets). **Do not apply a PVB's Tier I notching logic to a PSB without checking whether this carve-out changes the anchor.**

## 2. NBFCs (incl. HFCs, ARCs, and other RBI-regulated lending entities)

Business Risk (business profile, operating environment) → Financial Risk (profitability, liquidity/financial flexibility, capital adequacy, asset quality) → Management Risk → Ownership/Parentage → ESG. Business risk and management are explicitly weighted **above** financial risk in the overall assessment — "an NBFC with strong business and management credentials... is viewed more favourably than an entity with similar or even stronger financial metrics but a moderate business profile."

### Scale — indicative bands (a genuine numeric band, unlike the corporate methodology's qualitative scale treatment)

| Metric | Strongest | Weakest |
|---|---|---|
| AUM | >Rs 75,000 crore | <Rs 5,000 crore |
| Largest product as % of AUM | <20% | >90% |
| Single-state concentration | <15% | >80% |
| Track record | >15 years, established market-responsiveness | <3 years, no track record |

**AUM formula:** on-balance-sheet advances + off-book securitisation portfolio (direct assignment/co-lending) + business-correspondent book. Confirmed identical in substance to CRISIL's own AUM formula (§2 of the CRISIL twin file) — genuine cross-agency convergence, unlike the corporate operating-profit definitions.

### Gearing — TWO distinct ratios, not one

```
Managed gearing  = (on-balance-sheet borrowings + off-balance-sheet portfolio via
                     direct assignment/co-lending) / Tangible Net Worth
Adjusted gearing = on-balance-sheet borrowings / (Tangible Net Worth adjusted for
                     risk attributable to the off-balance-sheet portfolio, e.g. FLDG)
```
Also adjusted for intangibles (goodwill etc). **These measure the same underlying leverage from two different directions — grossing up the numerator vs. discounting the denominator — and are not interchangeable; state which one a published figure uses before comparing to it.**

### Asset quality — indicative bands by asset class

| Metric | Retail (ex-microfinance), strongest / weakest | HFC, strongest / weakest |
|---|---|---|
| 90+ dpd incl. 1-yr write-offs | <2.0% / >6.9% | <1.5% / >5.5% |

**Solvency:** Net stressed assets / Net worth — strongest <7.5%, weakest >30%.

**As NBFC asset-quality indicators are distorted by growth**, ICRA analyses NPAs on a **static-pool or lagged basis** for high-growth entities — a plain point-in-time GNPA% understates emerging stress in a fast-growing book. Cross-NBFC GNPA comparisons across DIFFERENT asset classes are explicitly discouraged (different write-off policies, different accounting) — compare gross-of-write-off figures for a like-for-like read.

### Hybrid instruments (perpetual debt) — same notch-down logic as banks, no numeric floor stated

Notched down from senior debt when the instrument permits interest deferral upon CRAR breach or CRAR-breaching payment — extent of notching depends on capital buffer and expected profitability trajectory, no fixed notch count given (unlike CRISIL's stated 1-3 notch AT1 range for banks — see the CRISIL twin file, §1).

### ARCs — a distinct sub-framework nested inside the NBFC methodology

Applies the same Business/Financial/Management skeleton, plus ARC-specific factors: **redemption ratio** (security receipts redeemed / SRs issued), **recovery ratio** (recovery / acquisition value), vintage of acquired assets (resolution horizon up to 8 years — older vintages carry higher impairment risk), and the linkage between an ARC's own asset quality and the **recovery-rating profile of the SRs it holds** (its valuation and fee income are directly tied to SR recovery ratings, not to a conventional GNPA metric).

## 3. Cross-cutting reminder

ICRA's financial-sector methodologies, like its corporate one, give **numeric indicative bands only for the Financial Risk factors** (asset quality, capital, funding, profitability above) and **qualitative-only treatment for Business Risk and Management factors** (franchise, governance, risk management systems). The same rule as `ICRA_CONVENTIONS.md` §7 applies here without exception: do not average a numeric asset-quality score with an invented numeric franchise/governance score inside one composite.
