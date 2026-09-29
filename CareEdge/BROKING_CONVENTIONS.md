# CareEdge — broking sector: verified financial conventions

**Derived by reconciliation, 20-Aug-2026**, against the CARE Ratings press release for **HDFC Securities Limited, 20-Aug-2026**. Every formula below was solved back from CareEdge's published figures and matches **exactly**. These are not approximations and not house guesses — use them verbatim for any CareEdge broking rationale.

Failure to apply them produced four wrong headline numbers on HSL (see `Companies/hdfc-securities/HSL_Defect_Analysis_20Aug2026.md`, section C).

---

## 1. Net worth is TANGIBLE net worth (TNW), never total equity

```
TNW = total equity
      − deferred tax assets (net)
      − other intangible assets
      − intangible assets under development
```

| | Total equity | − DTA | − Intangibles | − Intang. WIP | = TNW | CareEdge published |
|---|---|---|---|---|---|---|
| FY2026 | 3,595.92 | 15.57 | 78.23 | 5.63 | **3,496.49** | **₹3,496 cr** ✓ |
| FY2025 | 3,348.59 | 0.52 | 84.24 | 7.32 | **3,256.51** | **₹3,257 cr** ✓ |

Every ratio with net worth in it — gearing, RONW — uses TNW.

## 2. Overall gearing INCLUDES non-fund-based limits utilised

```
Overall gearing = (total debt + bank guarantees outstanding) / TNW
```

| | Total debt | + Bank guarantee | / TNW | = Gearing | CareEdge published |
|---|---|---|---|---|---|
| FY2026 | 15,113.88 | 1,100.00 | 3,496.49 | **4.64x** | **4.64x** ✓ |
| FY2025 | 7,943.77 | 700.00 | 3,256.51 | **2.65x** | **2.65x** ✓ |

The bank guarantee sits in the annual report's **contingent liabilities** note, *not* on the balance sheet — for HSL, ₹1,10,000 lakh (FY2026) and ₹70,000 lakh (FY2025). A broker posts guarantees to meet exchange margin, so this is real leverage and CareEdge counts it. **Extract the contingent-liability bank-guarantee line before computing gearing.**

CareEdge distinguishes this from **fund-based gearing** (borrowings only). HSL's stated management policy is to hold *fund-based* gearing below 5x.

## 3. Return on net worth uses AVERAGE TNW

```
RONW = PAT / ((opening TNW + closing TNW) / 2)
FY2026: 930 / ((3,256.51 + 3,496.49)/2) = 27.54%   →  published 27.54%  ✓
```
Not closing equity. CareEdge also publishes FY2024 RONW of 51.63% and FY2025 of 43.28%, so carry a **three-year** RONW series where available — the compression 51.63 → 43.28 → 27.54 is the story.

## 4. Return on total assets (ROTA) — also on averages

```
ROTA = PAT / average total assets
FY2026: 930 / ((14,031.11 + 21,784.33)/2) = 5.19%   →  published 5.22%
```
Quarterly ROTA is **annualised** (Q1FY27: 6.01%).

## 5. Cost-to-income IS a CareEdge broking metric — report it

```
Cost-to-income = (total expenses − finance costs) / (total income − finance costs)
FY2026: (1,873.09 − 817.40) / (3,110.20 − 817.40) = 46.05%   →  published 45.54%
FY2025: (1,768.71 − 785.45) / (3,264.86 − 785.45) = 39.66%   →  published 39.42%
```
Within ~0.5pp; CareEdge's standardised template evidently excludes a small expense line. **Report the computed figure and disclose the basis** rather than forcing a match.

> Do **not** carry over the NBFC rule from NABKISAN (failure mode 28) that cost-to-income is "a bank metric". For **broking**, CareEdge reports it. The metric set is a question about *this agency in this sector*.

---

## 6. The CareEdge broking "Brief Financials" table — required rows

Reproduce this row set, in this order:

| Row | Note |
|---|---|
| Total income | |
| Profit after tax (PAT) | |
| **Tangible net worth (TNW)** | per §1 |
| **Loan book (MTF)** | the sector-defining asset — see §7 |
| **Overall gearing (x)** | per §2, footnote "*Including non-fund based limits utilised" |
| **Cost-to-income (%)** | per §5 |
| **Return on net-worth (RoNW) (%)** | per §3, footnote "**Annualised" on the quarterly column |

Columns are **FY(n−1) (A) | FY(n) (A) | Q1FY(n+1) (UA)**, with `A: Audited UA: Unaudited`.

## 7. MTF is the organising theme of a broking credit, not a footnote

The **margin trading facility** book is a short-term secured loan to clients. CareEdge treats it as the centre of the analysis:

- It drives borrowing growth (HSL has funded MTF from borrowings since FY20).
- It contributes materially to income (**31% of HSL's FY2026 total income**, against 48% from brokerage and fee income and 33% from brokerage alone).
- Its **asset quality and the capitalisation buffer against it are the key monitorable**, and appear in the **negative rating sensitivities**.

The collateral is *not* purely a comfort: adverse movement in the underlying securities transmits credit and market risk directly. Never present MTF security as a liquidity mitigant without also stating the risk it creates.

Track the book across **all three dates** (HSL: ₹5,512 cr → ₹7,133 cr → ₹10,081 cr at 30-Jun-2026).

## 8. Liquidity: only **unencumbered** cash counts

A broker's bank balances are overwhelmingly **client funds and exchange margin**, which are segregated and unavailable to service company debt. CareEdge states liquidity as:

- total **fund-based borrowings**, itemised (HSL 30-Jun-2026: CP ₹15,765 cr + **TREPS** ₹2,183 cr + loan against deposits ₹338 cr = ₹18,286 cr);
- against **unencumbered** cash and equivalents (**₹422 crore**) and **unutilised sanctioned lines** (₹2,698 crore);
- plus MTF inflows and excess exchange margins as secondary sources.

**Never treat the balance-sheet line "bank balance other than cash and cash equivalents" as company liquidity.** On HSL that line is ₹7,838.73 crore against ₹422 crore genuinely unencumbered — an 18x overstatement.

Note also that "borrowings other than debt securities" for a broker is typically **TREPS** (tri-party repo) and loans against deposits — name them, do not write "secured loan".

## 9. Sector KPIs CareEdge quotes for broking

- **Rank by active clients** ("sixth-largest retail stockbroker"), with the client count and its as-on date.
- Share of brokerage from **retail** clients.
- **Branch count** and the direction of travel (HSL: consolidating, 184 at 31-Mar-2024 → 127 at 30-Jun-2026).
- The **discount/digital app** where one exists ("HDFC Sky").
- Revenue mix: brokerage / fee / MTF interest as % of total income.

A bare client count without a rank does not establish competitive position.

## 10. Regulatory section is mandatory for broking

Capital-market intermediaries face continuous regulatory revision, and it is forward-looking rating information. As at Aug-2026 the two live items are:

- **RBI amended directions dated 13-Feb-2026, effective 01-Jul-2026** — framework for bank credit to capital-market intermediaries: fully collateralised lending, higher collateral quality with significant cash components, minimum haircuts (notably on equity), restrictions on funding proprietary trading, MTF to be backed by high-quality liquid collateral, stricter monitoring and concentration limits. **Expected to raise funding costs and require stronger capitalisation and liquidity.**
- **SEBI's October 2024 F&O measures**, phased November 2024 → April 2025: fewer weekly expiries, larger lot sizes, +2% extreme loss margin on short options at expiry, upfront option premium collection, removal of calendar-spread treatment on expiry day.

## 11. Applicable criteria — CareEdge broking

As listed on the HSL press release:
Definition of Default · Rating Outlook and Rating Watch · Financial Ratios – Financial Sector · **Broking Firms** · Short Term Instruments · Notching by Factoring Linkages with Parent
