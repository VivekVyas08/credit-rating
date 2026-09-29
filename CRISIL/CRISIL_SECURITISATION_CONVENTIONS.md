# CRISIL — securitisation: risk framework, legal tests, credit-enhancement sizing, and the portfolio-analysis traps that generalise

**Source, read in full 06-Sep-2026:** `CRISIL/Methodology/criteria-for-securitisation-transactions.md` — Section I (risk primer and legal framework), Section II (ABS), Section III (CDO), Section IV (RMBS). **Not read:** `criteria-for-future-flow-transactions.md` and `criteria-for-assigning-recovery-risk-ratings-to-security-receipts.md`, which are separate files. Treat any gap here as "not yet extracted."

> **⚠ Read §7 even if you never rate a securitisation.** Three of the portfolio-analysis traps in this criteria are not securitisation-specific at all — they apply to any lender we rate, and one of them is currently unaddressed in four delivered NBFC/HFC/bank cases.

---

## 1. Why securitisation needs its own framework

In conventional lending a lender holds a loan and collects from the borrower. In securitisation the lender **sells the right to future collections** to a third party. The investor's recourse to the originator is therefore **limited to the credit enhancement the originator provided** — nothing more. That single structural fact reorders every risk.

**Two execution routes in India:**
- **PTC route** — receivables sold to an SPV (usually a trust), which issues pass-through certificates. The originator receives consideration upfront.
- **Direct assignment** — a pool assigned directly to the investor, no SPV. **Credit enhancement is NOT permitted in direct assignment transactions where a bank or NBFC is buyer or seller**, under the RBI Securitisation Directions, 2025 (separate directions exist for Commercial Banks, Small Finance Banks, AIFs and NBFCs).

**Four risk categories**, and the framework is built on them: **credit** (borrowers in the pool fail to pay), **counterparty** (servicer, designated bank, swap provider fail to perform), **legal** (the originator's insolvency reaches the receivables or the enhancement), **market** (prepayment, interest rates, macro).

**Structures worth being able to name:** fully amortising vs bullet; **par** (investor pays pool principal outstanding, generating excess interest spread) vs **premium** (investor pays more than principal for all the cash flow); par-with-EIS-flow-back vs **par-with-EIS-turbo-amortisation**; **senior-subordinate** tranching; fixed vs floating (a floating coupon over a fixed-rate pool creates interest-rate risk, mitigated by a swap); and **replenishment** structures, where collections buy new assets during a defined period and only interest is paid to investors before amortisation begins.

## 2. Legal risk — bankruptcy remoteness is the building block

An assignment is valid and bankruptcy remote when the assets are **put beyond the reach of the originator or its creditors even in insolvency**, and the transferee has unrestricted rights. CRISIL tests five things:

1. **Extent of recourse and risk retained by the originator.** The critical failure mode: *"in cases where the originator retains a high level of risk in the assets, the courts may reclassify the securitisation as 'secured borrowing' by the originator"* — which destroys bankruptcy remoteness entirely. CRISIL "may regard transactions with unusually high risk retention as inconsistent with the RBI guidelines". The originator must still meet the RBI **Minimum Retention Requirement**, which exists so the originator keeps a stake and therefore does proper due diligence — so retention is required but must not be *excessive*. Both directions are live.
2. **Option and obligation to repurchase.** No obligation to repurchase or support after sale, except a **clean-up call**, whose threshold **must not exceed 10% of the original value** of the underlying exposures or notes. Using collections during a revolving period to buy fresh assets against pre-defined eligibility criteria is *not* treated as inconsistent.
3. **Intention of the parties**, as evidenced in the documents — including the purchase price. *"An unfair purchase price can be scrutinised by the courts and could question the validity of such sale."*
4. **Extent of control retained** over the sold assets — must be minimal.
5. **Appointment of the originator as servicer.** Standard in India (there are few backup servicers) and *prima facie* fine — **but it is vitiated if the servicer indemnifies the transferee against obligor payment defaults, or services without adequate consideration.** The transferee's right to replace a non-performing servicer strengthens the position.

**Stamp duty is a uniquely Indian and uniquely severe risk.** Rates vary by state. Under the Indian Evidence Act, 1872, a document that is unstamped or inadequately stamped **cannot be adduced as evidence** — rendering it unenforceable unless the deficiency is paid at enforcement — and the penalty can run to **ten times the deficiency**.

**An independent legal opinion is a POLICY REQUIREMENT for every transaction**, from external transaction counsel, confirming: the transfer does not contravene the underlying loan documents · it constitutes an **absolute and valid sale** · the receivables are **bankruptcy remote** from the originator · the credit enhancement is bankruptcy remote (cash collateral) or enforceable by the trustee and legally adequate (guarantee) · the documents are valid, enforceable and compliant · and all documents were executed per stamp duty and registration law.

## 3. Credit enhancement — forms, and how it is SIZED

**External** — exposes investors to a counterparty other than the pool borrowers:
- **Cash collateral**: a designated account operable **only by the trustee**, fixed deposits, or liquid mutual fund investments. Where it sits in an FD, **the bank's credit quality becomes a rating consideration**; in a liquid fund, the fund's credit quality rating is analysed. For bankruptcy remoteness CRISIL asks: is it in a separate account accessible only by the trustee? If a current account, do the documents state the money is **held in trust** for the trustee's benefit? If an FD, are the **maturity proceeds endorsed to the trustee upfront**? (The originator may still take residual amounts after payouts.)
- **Guarantee** (bank or corporate): evaluated under the 12-point guarantee framework in `basics-of-ratings.md` §XI; the guarantor's rating drives the counterparty view.

**Internal** — from the structure itself:
- **Subordination / over-collateralisation.** Over-collateralisation for a tranche is the protection offered by the tranches subordinate to it. CRISIL's illustration: pool EMIs Rs 100, senior payout Rs 90, subordinated strip Rs 10 — collections of Rs 95 pay the senior Rs 90 and the subordinate Rs 5; collections of Rs 90 or less go entirely to the senior.
- **Excess interest spread (EIS)** — pool yield minus PTC yield. In par structures EIS is subordinated to investor payouts and behaves like over-collateral. Residual EIS may flow back to the originator, be **trapped in a TRA** (where it remains available for later months), or **turbo-amortise** the PTCs. **Prepayments and re-pricing cause substantial EIS variation** — it is not a stable cushion.

### How much enhancement: the peak cumulative shortfall

The cash-flow model has three steps — project pool collections, project investor payouts, compare monthly — and the sizing mechanic is specific:

> **"The peak of these monthly cumulative shortfalls is a key input to determining the enhancement requirement… it represents the maximum shortfall that needs to be covered during the transaction tenure."**

Not total expected loss — the **peak of the cumulative monthly shortfall**. Stresses over the base case are calibrated on: the target rating, the pool-versus-portfolio comparison, historical volatility of rated pools, prepayment expectations for the asset class, the originator's track record, and geographical and borrower concentration.

**A minimum cash collateral is required regardless of how strong the pool looks**, for two contingencies CRISIL names explicitly: **event-driven liquidity stress** (its own example is COVID lockdowns and regulatory moratoria, where collections in affected months collapse) and **MIS or banking failures** (servicer MIS delayed by a system breakdown, or banking failures delaying transfer to the collection-and-payout account). Both are operational, neither is a credit event, and both can break a timely payout.

Credit enhancement may be **reset and the excess withdrawn** under the RBI Master Direction (Securitisation of Standard Assets) Directions, 2021.

## 4. CDO — the two coverage tests and the correlation effect

**Over-collateralisation test:** OC ratio = current collateral value / aggregate outstanding of the tranche being tested, checked periodically against a minimum (CRISIL's illustration uses **105%**). On a breach, **payments to junior tranches are suspended** and cash flows prepay the senior tranche until the ratio is cured.

**Interest coverage test:** aggregate expected interest inflows / aggregate interest payable to the tranches. Below a trigger (illustratively **1.1 times**), senior amortisation accelerates, lowering subsequent interest outflow, until cured.

**The Monte Carlo model.** A proprietary tool simulates portfolio default and shortfall distributions. Each trial generates one random number per cash flow — *"if the pool consists of 30 five-year loans, 150 numbers will be generated in each simulation"* — and each asset defaults or pays consistently with the PD implied by its rating and tenure, drawn from CRISIL's own default matrix (built on ratings since 1987). Inputs: asset ratings and PDs · asset cash flows (net of expected prepayment and rate movement) · **asset correlation assumptions** · recovery level and timing.

**The correlation point is the one to remember:** raising pairwise correlation from 0 to 0.5 across a hypothetical 100-asset pool leaves **the mean shortfall unchanged** while standard deviation and both extremes rise sharply — *"more frequent extreme events ('fat tails')"*. Assets in the same industry are assumed more correlated than across industries; **same-corporate-group borrowers get higher correlation still**. A pool that looks fine on average loss can be materially riskier purely on concentration.

**Recoveries** are a function of security liquidity and value, the lender's legal and operational seniority, and the servicer's track record — benchmarked on the banking sector's historical NPA recoveries. **No benefit is given for recoveries expected after the CDO's scheduled maturity.**

Tranche ratings come from benchmarking each tranche's weighted-average shortfall (after credit enhancement) against that of a vanilla bond.

## 5. Pool characteristics that drive the analysis

Assessed for ABS and RMBS alike: **asset class · LTV ratio · original tenure · geographical distribution · borrower profile · borrower diversification · seasoning profile · loan cycle · interest rate · loan amount · overdue profile**, with RMBS adding the **instalment-to-income ratio (IIR)**.

**Securitised pools are typically cherry-picked** — the pool is usually *better* than the originator's overall portfolio — which is exactly why CRISIL runs an explicit **pool-versus-portfolio comparison** rather than reading pool quality on its own.

## 6. Counterparty risks specific to the structure

**Servicer risk** (collection performance and the absence of backup servicers in India), **commingling risk** (pool collections mixed with the originator's own funds before transfer), **swap counterparty risk**, and **collection-and-payout account risk**. These are addressed structurally — defined deposit timelines for the servicer, trustee monitoring of the C&P account, and the minimum cash collateral described in §3.

---

## 7. ⚠ THREE PORTFOLIO-ANALYSIS TRAPS THAT ARE NOT SECURITISATION-SPECIFIC

These come from the ABS/RMBS originator-analysis sections, but nothing about them is confined to securitisation. They apply to **any lender this project rates**.

### 7.1 Write-offs flatter delinquency — and we have never checked for it

> *"Writing off loans leads to recognition of losses and the exposure is usually removed from the portfolio of the originator in the delinquency analysis. Thus, the exposure does not show up in any of the delinquency buckets, which leads to an apparent improvement in the dpd profile of the portfolio. **All else being equal, originators adopting aggressive write-off policies will show better delinquency levels than others.**"*

CRISIL's remedy: obtain **historic write-off data net of recoveries** from previously written-off contracts, cumulate it, and express it as a percentage of portfolio principal ~12 months prior — *"a proxy for net losses on a static pool basis."*

**This project has a live gap here.** Four delivered lender cases quote asset-quality metrics and **none of them mentions write-offs at all**: Repco Home Finance (8 asset-quality references, 0 write-off), Aptus Value Housing (6/0), IIFL (4/0), SBI (2/0). Repco is the sharpest — its rationale reports GNPA improving *every year*, 7.0% in FY2022 to 2.67% at 30-Jun-2026, with no write-off figure anywhere. **An improving GNPA alongside accelerating write-offs is not an improvement**, and on the evidence in those reports we cannot tell which we are looking at. Recorded as failure mode 59.

### 7.2 Lagged delinquency — a growing book understates its own dpd

In a rapidly growing portfolio, days-past-due levels are **understated**, because recently disbursed contracts perform well initially and **cannot yet have aged into the higher buckets**. CRISIL therefore computes **lagged delinquencies** — dividing by the principal outstanding of, say, twelve months earlier rather than the current month. Its worked example: 180+ dpd of **1.0% un-lagged becomes 1.25% lagged**, a quarter higher.

Any fast-growing NBFC or HFC we rate is exposed to this arithmetic, and a headline dpd or GNPA improvement during a growth phase should be tested against a lagged denominator before it is called an improvement.

### 7.3 Static pool beats portfolio snapshot

**Static pool analysis** — following a cohort originated in one month or quarter, with no additions or deletions — is how CRISIL forms loss expectations, because a securitised pool is itself static. A **dynamic portfolio** view (contracts added daily) shows recent trend but cannot separate vintage effects from growth effects. Where vintage data exists for a lender, the cohort view is the more honest one; where it does not, the portfolio snapshot should be read knowing what it cannot show.
