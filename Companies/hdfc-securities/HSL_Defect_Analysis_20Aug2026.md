# HDFC Securities — defect analysis against the CareEdge published press release

**My report:** *HDFC Securities Limited_20 Aug 2026_CareEdge_Rating Rationale.md*
**Benchmark:** CARE Ratings Ltd press release, **HDFC Securities Limited, August 20, 2026** — the same date.

The published rating is **CARE A1+** on commercial paper of **₹20,000.00 crore** (enhanced from ₹18,000.00 crore) **and CARE AAA; Stable / CARE A1+** on **₹3,000.00 crore** of long-term / short-term bank facilities. Both **Reaffirmed**, with rating history back to **22-Dec-2023**.

I rated the CP A1+, which was right. Everything structural around it was wrong.

---

## A. I declared long-term debt NIL and concluded no long-term rating applies. CareEdge assigns **CARE AAA; Stable** on ₹3,000 crore.

This is the most serious error and it drove three others.

I read the contractual maturity tables correctly — every *drawn* borrowing sits in the "less than 1 year" bucket in both FY2025 and FY2026 — and then reasoned:

> long-term debt is NIL → no long-term instrument exists → no long-term rating → **"No outlook is assigned"**

Every step after the first is a non-sequitur. **A rating attaches to a sanctioned facility, not to a drawdown.** A ₹3,000 crore long-term/short-term bank facility carries a long-term rating whether it is drawn long, drawn short, or entirely undrawn. What the maturity table shows is how the company *chose to draw* in that year, which is a funding-mix observation, not a statement about the rated universe.

Consequences that cascaded from this one error:
- Missed the **CARE AAA; Stable** long-term rating entirely.
- Wrote **"No outlook is assigned, as both ratings are on the short-term scale."** CareEdge assigns **Outlook: Stable**.
- Wrote the rating action as **"Assigned"**. It is a **Reaffirmation** of ratings held since at least 22-Dec-2023.

**Failure mode 13 already covers the rated-limits-vs-drawn-debt distinction, and it did not fire** — because I had it pointing the wrong way. FM13 warns against presenting sanctioned limits as though they were drawn debt. I made the mirror-image error: I let drawn debt define the rated universe.

---

## B. Rated amounts: I reported outstanding balances in the rating table and called the programme size an evidenced absence.

CareEdge: **CP ₹20,000.00 crore** (enhanced from ₹18,000.00 crore), **bank facilities ₹3,000.00 crore**.
Me: CP "₹12,931.33 crore outstanding as on 31-Mar-2026", bank facilities "₹2,182.55 crore outstanding".

The absence search itself was honest — those limits genuinely are not in the annual report. But the conclusion drawn from it was wrong, and this is the part that must change:

**A rated limit is almost never disclosed in an issuer's annual report. It exists in the CRA press release.** So "not found in the issuer's documents" is the *expected* state for this data item, not a finding about it. Discovering the expected state and then substituting a different number — outstandings — put wrong figures in the most prominent table in the report, however carefully they were labelled.

Note the scale of the error: CP outstanding ₹12,931 crore against a **₹20,000 crore** rated programme. The utilisation headroom — roughly ₹7,000 crore, and the fact that the limit was *enhanced* from ₹18,000 crore — is itself rating-relevant information I could not report because I never had the limit.

---

## C. Three wrong financial conventions. All three now reconcile to CareEdge exactly.

I used generic corporate definitions where CareEdge uses financial-sector broking definitions. Working back from the published figures, the conventions are unambiguous:

**1. Net worth is TANGIBLE net worth, not total equity.**

```
TNW = total equity − deferred tax assets − intangible assets − intangible assets under development
FY2026: 3,595.92 − 15.57 − 78.23 − 5.63 = 3,496.49   →  published ₹3,496 crore  ✓
FY2025: 3,348.59 −  0.52 − 84.24 − 7.32 = 3,256.51   →  published ₹3,257 crore  ✓
```
I used total equity (₹3,595.92 crore / ₹3,348.59 crore) throughout.

**2. Overall gearing includes non-fund-based limits utilised.**

```
Gearing = (total debt + bank guarantees outstanding) / TNW
FY2026: (15,113.88 + 1,100) / 3,496.49 = 4.64x   →  published 4.64x  ✓
FY2025: ( 7,943.77 +   700) / 3,256.51 = 2.65x   →  published 2.65x  ✓
```
The bank guarantee is disclosed in the annual report at ₹1,10,000 lakh (FY2026) and ₹70,000 lakh (FY2025) — **I extracted neither.** I published gearing of 2.37x → 4.20x. The published figures are 2.65x → 4.64x, and **5.28x as on 30-Jun-2026**.

**3. Return on net worth is computed on AVERAGE TNW.**

```
RONW = PAT / average TNW
FY2026: 930 / ((3,256.51 + 3,496.49)/2) = 27.54%  →  published 27.54%  ✓
```
I published "return on equity 25.86%" on closing total equity. CareEdge also gives FY2024 at 51.63% and FY2025 at 43.28%, making the multi-year compression — 51.63 → 43.28 → 27.54 — far more visible than my two-point series.

Each of these is a definitional choice that changes the number without changing the underlying facts. That is precisely the class of error the workbook's "Convention" column exists to prevent, and I filled that column with my own conventions rather than the agency's.

---

## D. I excluded cost-to-income on a sector rule I applied too broadly.

My Annexure III stated:

> "Lending-company metrics (Stage III, CRAR, AUM) and bank metrics (NIM, GNPA, CASA) are **not** applicable to a broking intermediary and are deliberately not reported."

CareEdge's broking template reports **cost-to-income (39.42% / 45.54% / 39.70%)** and **ROTA (5.22%, 6.01% annualised)**. I reported neither, and I wrote an explicit justification for the omission.

This is failure mode 28 misapplied. FM28 came from NABKISAN, where cost-to-income was the *wrong* metric for an NBFC. I generalised that into "cost-to-income is a bank metric" and carried it to a different sector. **The metric set is a question about a specific agency in a specific sector, answerable only by looking at that agency's published reports in that sector** — not by reasoning from a rule learned in an adjacent sector.

---

## E. Liquidity overstated by an order of magnitude.

Me: "liquid assets of **₹9,622.71 crore**", "cash cover on CP of **0.74x**, flat across both years".
CareEdge: "**unencumbered** cash and cash equivalent of **₹422 crore**" plus unutilised sanctioned lines of ₹2,698 crore.

For a broker, the great majority of bank balances are **client funds and exchange margin** — legally segregated, not available to service company debt. I took the balance-sheet line "Bank balance other than cash and cash equivalents" (₹7,838.73 crore) at face value and treated it as company liquidity. The word *unencumbered* is doing all the work in CareEdge's sentence, and I did not ask the question.

My 0.74x ratio, and the "flat at ~0.74x, liquidity scaled with the borrowing" narrative built on it, are both meaningless as constructed. The liquidity *descriptor* — Strong — happened to match, for the wrong reasons.

---

## F. MTF is the spine of this credit. I treated it as a footnote.

CareEdge organises the entire rationale around the margin trading facility: the book grew **₹5,512 cr → ₹7,133 cr → ₹10,081 crore as on 30-Jun-2026** (+41% in a single quarter), it drives the borrowing growth, it contributes **31% of total income**, and its asset quality is named as **the key monitorable** and appears in the negative sensitivities.

I called it the "margin funding book", used it as a *mitigant* ("secured against listed securities, self-liquidating"), and **never extracted the ₹10,081 crore Q1FY27 figure** — despite having the June 2026 results open and reading the debt figures off them. The security is real, but CareEdge's point is the opposite of mine: expanding a secured book against volatile collateral *creates* credit and market risk, and the capitalisation buffer against it is what matters.

I also missed that borrowings have been deployed to fund MTF since FY20 — the structural reason debt is growing, which I described as an unexplained tension.

---

## G. Missed the regulatory overhang entirely — the main forward-looking risk.

CareEdge devotes a full section to it:
- **RBI amended directions dated 13-Feb-2026, effective 01-Jul-2026**: a comprehensive framework for bank credit to capital-market intermediaries — fully collateralised lending, higher collateral quality with significant cash components, minimum haircuts on equity collateral, restrictions on funding proprietary trading, MTF required to be backed by high-quality liquid collateral, stricter concentration limits. **Expected to increase funding costs.**
- **SEBI's October 2024 F&O measures**, phased November 2024 to April 2025: fewer weekly expiries, larger lot sizes, +2% extreme loss margin, upfront option premium collection.

My report mentioned "regulatory intervention in derivative-segment rules remains a live variable" as a single clause. For a company funding a fast-growing MTF book with bank credit and CP, a rule effective seven weeks before the rating date that directly governs that funding is not a clause — it is a section.

---

## H. Franchise position: no ranking, no peer context.

CareEdge: **sixth-largest retail stockbroker by active clients**, ~**10.05 lakh active clients as on 31-Jul-2026**, ~95% of Q1FY27 brokerage from retail, and the **"HDFC Sky"** discount-broking app targeting new-age investors.

I wrote "over 1 million customers access services digitally" — numerically consistent, but a bare count with no rank says nothing about competitive position, which is the thing the section exists to assess.

---

## I. Over-reach: I built a headline finding on a denominator I never verified.

My corrected report led with "revenue yield on turnover **halved**, 2,040 → 1,037 — the defining operating fact of FY2026", from average daily turnover rising 82% while income fell 4.7%.

CareEdge attributes the income decline to lower **brokerage income in unfavourable market conditions**, and notes brokerage recovering in Q1FY27 on better volumes. It computes no such ratio.

The problem is not that the ratio is unconventional — it is that I never established what the 82% turnover figure *measures*. It almost certainly includes derivative **notional** turnover, which grew 83% and against which revenue is not a meaningful denominator; a notional-value denominator will always show collapsing "yield" as derivative mix rises. **I fixed a year-attribution error (FM30) and then over-corrected into a manufactured insight built on an unexamined basis.**

---

## J. Smaller items

| # | Mine | Published |
|---|---|---|
| J1 | HDFC Bank **94.01%** (31-Mar-2026) | **93.99%** as on 30-Jun-2026 — the newer figure |
| J2 | "Secured loan ₹2,182.55 cr" | **TREPS borrowings ₹2,183 cr**, plus **loan against deposits ₹338 cr** |
| J3 | No industry classification | Financial services / Capital markets / Stockbroking and allied |
| J4 | Not noted | HSL is **debt-listed on BSE**; incorporated April 2000 as a JV; HBL took 55% control in FY06 |
| J5 | Not noted | Management intends to hold **fund-based gearing below 5x** |
| J6 | Not noted | Board linkage: HBL nominee director; MD & CEO Dhiraj Relli formerly Head of Branch Banking at HBL |

---

## What was right, and should survive the rebuild

Not everything failed, and the rebuild should not discard these:

- **Total income, PAT and Q1FY27 figures match exactly**: 3,265 / 3,110 / 950 and 1,125 / 930 / 297.
- **PAT margin 29.90% (FY26) and 31.27% (Q1FY27)** — identical to CareEdge.
- **MTF book ₹5,512 cr and ₹7,133 cr** — correct for both audited years.
- **Brokerage and fee income ₹1,516 crore ≈ 48% of income** — matches CareEdge's 48%.
- **Interest income ₹1,498 cr / ₹1,418 cr** — I extracted these and then failed to use them.
- **Branch contraction 184 → 134 → 128** — my FM30 self-correction was *validated*: CareEdge writes "consolidating branches, reducing the count to 127 as on June 30, 2026, from 184 as on March 31, 2024". Had I not caught that, the report would have claimed expansion against a published finding of consolidation.
- **Liquidity descriptor Strong**, **analytical approach Standalone with parent linkage**, **CP rated A1+**, and the **~80% dividend payout** constraining net-worth growth — all consistent with the published view.

---

## Root causes, stated plainly

Four distinct causes, not one:

1. **Reasoning from drawn debt to the rated universe** (A, B). A rating attaches to a facility. The balance sheet tells you about drawdowns and can never enumerate rated limits.
2. **Substituting my own definitions for the agency's** (C). Net worth, gearing and return each have a specific CareEdge financial-sector meaning that reconciles exactly once applied — so this was fully knowable from the arithmetic, without the press release.
3. **Generalising a sector rule across sectors** (D). FM28 learned on an NBFC was applied to a broker and produced a written justification for omitting the right metrics.
4. **Accepting a balance-sheet caption at face value** (E, I). "Bank balance" is not free cash for a broker; an 82% turnover figure is not a revenue denominator. Both errors are the same shape: using a number without establishing what it measures.
