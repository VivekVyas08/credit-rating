# CareEdge — non-financial (corporate) sector: ratio conventions

**Source, read 20-Aug-2026:** `Methodology/Financial_Ratios_Non_Financial_Sector_March_2025.md` and `Methodology/Liquidity Analysis of Non-Financial Sector Entities - Sept 2024.md`, both newly added to the corpus.

This is the corporate twin of `BROKING_CONVENTIONS.md`. It matters disproportionately: **520 of the 631 CareEdge reference reports carrying a Brief Financials table are corporate, PBILDT-based.** Until these two documents were added, every corporate rationale was inferring PBILDT, overall gearing and interest coverage from peer reports rather than reading the definitional source. Applies to **manufacturing, trading and service** entities.

> Failure mode 32 in one line: *if a definition will not reproduce the agency's published figure, the definition is wrong.* Use these verbatim.

---

## 1. Annualisation — applies to growth and return ratios

Every growth ratio and ROCE/RONW carries a `× (12 / No. of Months)` factor. Part-year figures are annualised **before** comparison, never after.

## 2. Total operating income (TOI)

**Include** the entire operating income, with indirect taxes (GST, excise, sales tax, service tax) **netted off** gross sales to reach core sales. Also include core-related other income:

job-work income · royalty / technical knowhow / commission **received** in relation to core operations · refund of indirect taxes · sale of scrap · cash discount received · duty drawback and export incentives · exchange-rate **gain** (not debt-related)

**Exclude — even when recurring:** interest income, dividend income, rental income. CareEdge is explicit that recurrence does not make an item operating.

> Note the asymmetry against ICRA: excise is netted off here. Earlier work on Gujarat treated excise as an *expense line*, so reported revenue was gross of excise — that is the issuer's presentation, not CareEdge's TOI.

## 3. PBILDT

TOI less **all** operating expenses: raw material, cost of traded goods, stores and spares, power and fuel, employee costs, selling and distribution, administrative and general — including royalty / knowhow / commission **incurred**, insurance, directors' fees, exchange-rate **loss** (not debt-related) and bad debts.

## 4. PAT

```
PAT = PBILDT
      − interest and finance charges, net of capitalised interest
      − depreciation / amortisation, INCLUDING depreciation on right-of-use assets
      ± non-operating income / expense (incl. profit or loss on sale of assets and investments)
      ± prior period items (including income tax)
      − tax expense (current and deferred)
```
Finance charges include interest on term loans, working capital, unsecured promoter/group loans, **interest on lease liability**, premium on redemption of bonds and preference shares, and FX gain/loss **on debt**.

## 5. Gross cash accruals (GCA) — one trap

```
GCA = PAT + inherently non-cash expenditure
```
Add back depreciation and amortisation, deferred tax provision and write-offs — but **EXCLUDE depreciation on right-of-use assets created under Ind AS 116**. Note the asymmetry: ROU depreciation is deducted in PAT (§4) and **not** added back in GCA.

**Not added back:** provisions for bad debts, doubtful debts or warranties — these are not inherently non-cash.

## 6. Tangible net worth (TNW)

**Include:** equity share capital · all reserves and surplus **except revaluation reserve** · unsecured loans from promoters / group entities **that are subordinated to outside loans** · equity share warrants · share application money · ESOPs outstanding · minority interest (consolidated financials).

**Deduct:** miscellaneous expenditure not written off · accumulated losses.

**Intangibles** are generally excluded — *but included when critical to core operations*. CareEdge names four such cases:
telecom licence fees paid to the GoI · mining surface rights · media rights (movie, audio, video, broadcasting, television, theatrical, satellite, music, digital, overseas, copyright) · intellectual property rights, typically in IT and pharma.

> This differs from the **financial-sector** TNW in `BROKING_CONVENTIONS.md`, which deducts deferred tax assets and *all* intangibles with no critical-to-operations exception. Do not carry one across to the other.

## 7. Return ratios

```
ROCE = [(PBIT ± non-operating income/expenses ± extraordinary items ± OCI) × (12/months)]
       / Avg(TCE_t, TCE_t−1) × 100

TCE  = Tangible Networth + Total Debt + Net Deferred Tax Liabilities/(Assets)
       OR  Net Fixed Assets + Net Working Capital

RONW = [(PAT ± OCI) × (12/months)] / Avg(TNW_t, TNW_t−1) × 100
```
Both are on **average** capital, and both fold in **other comprehensive income**. Deferred tax sits **inside** the ROCE denominator while being excluded from TNW for gearing — the same split CRISIL applies.

## 8. Leverage

| Ratio | Definition |
|---|---|
| Long-term debt–equity | Total long-term debt **including current portion** / TNW |
| **Overall gearing** | **Total debt INCLUDING acceptances / creditors on LC** / TNW |
| TOL / TNW | Total outside liabilities / TNW — TOL = total debt + other long-term liabilities and provisions, **net of DTL/DTA** |

Debt–equity and overall gearing are both **adjusted for exposure to group entities**, and CareEdge also weighs the impact of **non-fund-based limits availed**.

## 9. Coverage

```
Interest coverage = PBILDT / (total interest and finance charges
                              − amortisation of premium on debentures
                              − interest capitalised)

DSCR      = (GCA + interest and finance charges − internal accruals committed for capex/investment)
            / (gross long-term debt repayable in the year + standalone CP
               + short-term debt repayment + interest and finance charges)

Cash DSCR = same numerator, less 25% of the INCREASE in working capital
```
The 25% is margin money assumed met from GCA; the other 75% is assumed funded by working capital borrowings. **Cumulative DSCR** for the final projection year equals the average DSCR over the facility's tenure.

Also reported: term debt / GCA · total debt / GCA · term debt / PBILDT · total debt / PBILDT · total debt / CFO (CFO being cash from operations after working-capital changes).

## 10. Total debt — what counts

**Include:** all short- and long-term debt · redeemable preference share capital · optionally convertible debentures · interest-free loans · foreign currency loans · vehicle loans · fixed deposits · unsecured loans · commercial paper · inter-corporate borrowings · borrowings from promoters, associates and group entities · bills discounted · **acceptances / creditors on LC, including capex LCs** · **lease liability** · mobilisation advances backed by financial bank guarantees (typically construction).

**Add for *adjusted* leverage:** any corporate guarantee given to lenders of subsidiaries or group entities.

**Exclude:** debt fully backed by dedicated / lien-marked fixed deposits or cash margin.

**Reclassify:** promoter/related-party borrowings subordinated to outside loans move to TNW — but their **interest expense stays a normal interest expense**.

## 11. Hybrid instruments

| Instrument | Treatment |
|---|---|
| Redeemable preference shares | **Debt** — fixed tenure and fixed dividend. *Exception:* issued to promoters and redeemable only after outstanding term debt → **quasi-equity** |
| Compulsorily convertible | **Quasi-equity**, part of TNW. *Exception:* investor has an exit option, or conversion is conditional → **debt** |
| Optionally convertible (OCPS / OCDs / FCCBs) | **Debt** — redemption cannot be ruled out until actual conversion |

## 12. Turnover and liquidity ratios

Average inventory period · average collection period · average creditors period · working capital cycle (= inventory + collection − creditors) · fixed asset turnover (on **gross block net of intangibles such as goodwill**) · working capital turnover · current ratio · quick ratio.

Inventory, collection and creditor periods all use `Avg(t, t−1) × 30 × No. of Months` over the relevant cost or sales base — not a closing-balance snapshot.

---

## 13. Liquidity — the descriptor and what counts as cash

CareEdge discloses liquidity at one of four levels, and `check_sections.py` already enforces that one is named:

**Superior/Strong · Adequate · Stretched · Poor**

**Unencumbered cash and equivalents — counts:** cash balance · bank balance in current account · liquid mutual funds · listed large-cap / index equity (non-strategic) · listed corporate bonds of highly rated entities · government securities · unencumbered fixed deposits.

**Encumbered — does NOT count:** DSRA balances · margin money · FDs earmarked against a loan or facility. CareEdge "generally does not factor the availability of such funds".

**Also excluded:** investments in, and loans and advances to, **group entities** — not liquid even when classified short-term, because availability depends on the group entity's credit profile.

> This generalises failure mode 34 beyond broking: for *any* non-financial entity, cash is not liquidity until shown to be unencumbered.

**Unutilised lines** are assessed as the lower of sanctioned working-capital limits and available drawing power, against monthly maximum and average utilisation, typically over the preceding 12 months. Consistently high utilisation signals weak liquidity. Undrawn lines **reduce but do not eliminate** default risk — they can be withdrawn, which matters most for CP carved out of working-capital limits.

## 14. Default recognition — the thresholds behind CARE D

From `Policy on Default Recognition_Jan 2025.md`:

- **Listed / proposed-to-be-listed debt securities, and any facility with a pre-defined repayment schedule:** one-day-one-rupee delay = default.
- **No pre-defined schedule** (cash credit, overdraft): continuously overdrawn **more than 30 days**.
- **Packing credit, bill discounting, buyer's credit:** overdue / overdrawn more than 30 days.
- **Letter of credit:** overdue more than 30 days from devolvement. **Bank guarantee:** unpaid more than 30 days from invocation.
- **Curing period:** generally **90 days** to move out of CARE D into speculative grade; generally **365 days** to reach investment grade.
- Non-servicing in anticipation of a restructuring approval **is** a default. Rescheduling agreed *before* the due date is not — unless done to avoid default or bankruptcy.
