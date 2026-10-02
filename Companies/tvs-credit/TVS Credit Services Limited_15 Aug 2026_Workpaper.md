# Workpaper — TVS Credit Services Limited | ICRA | 15 August 2026

**Rating view:** [ICRA]AA+ (Stable) on long-term bank facilities and subordinated debt ·
[ICRA]A1+ on short-term facilities and commercial paper · [ICRA]AA (Stable) on perpetual debt.

---

## 0. THREE DATA-INTEGRITY PROBLEMS FOUND BEFORE ANY ANALYSIS

### 0.1 Six of nine uploaded documents belong to a different, unrelated company

The `quarterly_results` folder contains six files that are **Aptus Value Housing Finance India
Limited**, not TVS Credit. Verified by counting name occurrences in each file:

| File | "TVS Credit" | "Aptus" |
|---|---|---|
| `AptusHFCResultsQ1FY27.md` | 0 | 36 |
| `AptusValueFinancialResultsMarch2026.md` | 0 | 73 |
| `AptusValueFinancialresultsDecember2025.md` | 0 | 47 |
| `AptusValueFinancialsQ2FY26.md` | 0 | 61 |
| `AptusValueHousingFinanceIndiaLtd_AnnualReportFY24.md` | 0 | 512 |
| `Q1FinancialsFY2025-26.md` | 0 | 43 |

**This is not the Vedanta / Hindustan Zinc situation.** There the two entities were parent and
subsidiary in one group, and treating them together was defensible. Aptus Value Housing Finance
is a South-India-focused housing finance company with no ownership relationship to TVS Credit
Services or the TVS group. Using its results would have produced a rating on the wrong company.

**Action taken:** all six files were EXCLUDED. The rating rests solely on the three annual
reports, which are genuinely TVS Credit (verified below). **No quarterly data is used**, so the
rationale carries no post-FY2026 information — a real limitation, disclosed rather than hidden.

### 0.2 The FY2026 annual report is 27% corrupted

| File | Size | Replacement chars | Numeric table rows | Clean rows |
|---|---|---|---|---|
| `Annual-Report_2025-1.md` (FY2025) | 731,637 | **0.0%** | 2,627 | 2,627 |
| `Annual_Report_2026.md` (FY2026) | 761,091 | **27.1%** | 2,580 | 1,824 |
| `Annual_Report_Final.md` (FY2024) | 608,810 | **0.0%** | 2,310 | 2,287 |

The corruption is concentrated in design-heavy narrative pages where the ₹ glyph precedes figures,
which destroyed most narrative numerics (AUM, disbursements, growth rates). **The financial
statements themselves survived intact**, so the P&L, balance sheet and regulatory tables were
usable. Every figure in the rationale comes from a clean table row; no corrupted value was
reconstructed by guesswork.

**Consequence:** AUM and disbursement figures could not be extracted and do **not** appear in the
rationale. For an NBFC these are ordinarily headline metrics. Recorded as a gap.

### 0.3 An OCR decimal-point loss that would have been a material error

The standalone P&L (L3129) shows the FY2026 exceptional item as **`861`**. Against a profit before
exceptional items of Rs. 1,246.93 crore, an Rs. 861 crore exceptional item would have been the
dominant feature of the year and would have changed the rating discussion entirely.

It is wrong. The **consolidated** statement (L7670) shows the same line as **`8.61`** — the
decimal point was lost in the standalone table. The true figure is Rs. 8.61 crore, or 0.69% of
PBT: immaterial.

Caught by cross-checking standalone against consolidated (failure mode 15, corroboration). This is
now a permanent tie-out in `compute_ratios.py` and `build_spreads.py`: the exceptional item must
be under 5% of PBT, so a reappearance of the uncorrected figure fails the gate.

---

## 1. Step 1a — PRE-FLIGHT

```
PRE-FLIGHT  |  TVS Credit  |  agency ICRA  |  9 documents, 377,024 words
[1] PRIOR RATING ACTION      *** PRESENT (see note below)
[2] CREDIT-RATING NOTE in AR *** PRESENT - 95 matches
[3] SUBSIDIARIES to NAME     *** PRESENT - 415 matches
[4] ESG data                 *** PRESENT - 252 matches
[5] INSTRUMENT details       *** PRESENT - 230 matches
[6] CAPEX                    *** PRESENT - 31 matches
[7] SHAREHOLDING             *** PRESENT - 3 matches -> TVS Motor 85.63%
[8] AUDITOR opinion / KAM    *** PRESENT - 177 matches
[9] SECTOR METRIC -> NIM / GNPA / CRAR   *** PRESENT - 71 matches
```

**Probe [1] over-reported and was checked, not trusted.** It returned Mangal Credit And Fincorp
(matched on "Credit"), TVS Holdings, TVS Motor and TVS Supply Chain (matched on "TVS"). A direct
search confirmed **no TVS Credit Services rationale exists in any reference library** — only the
parent and group siblings. Over-reporting is the safe direction for this probe, but the hits were
verified individually rather than accepted.

The **Step 14 anchor is therefore the issuer's own Step 7b disclosure**, not a library rationale.

---

## 2. Entity and routing corrections

**Identity verified before use.** All three annual reports are genuinely TVS Credit Services
Limited (224 / 200 / 13 name occurrences respectively).

**CIN discrepancy investigated, not assumed to be an error.** The FY2026 AR carries CIN
`U65920KA2008PLC218369` while FY2024 and FY2025 carry `U65920TN2008PLC069758`. The FY2026 AR
states the KA CIN as the company's own, with the registered office at No. 383, 16th Main, 3rd
Block, Koramangala, Bengaluru. This is a genuine **relocation of the registered office from Tamil
Nadu to Karnataka**, which changes the CIN state code — a corporate event, not a data fault. It is
stated in the rationale.

**Methodology re-routed.** The intake had defaulted the case to *Corporate Credit Rating
Methodology* with sector "Corporate (no specific sector methodology)". TVS Credit is an **NBFC-ICC
in the RBI Middle Layer** per its own FY2026 AR. Re-routed to *NBFCs, Rating Methodology
(Dec 2025)* + *Financial Ratio Analysis (Sep 2024)*. This is the second consecutive case where
intake mis-routed a financial-sector entity to corporate criteria (SBI, 14-Aug-2026 was the first).

---

## 3. Ratio engine — 9/9 tie-outs reconcile

| Tie-out | Result |
|---|---|
| FY2025 and FY2026 CRAR = Tier I + Tier II | Exact (20.30; 19.44) |
| FY2025 / FY2026 total expenses rebuilt from six components | Exact |
| FY2025 / FY2026 PBT = total income − total expenses | Exact |
| FY2025 / FY2026 net debt/equity reproduces the company's published 4.27x / 4.01x | Exact |
| FY2026 exceptional item immaterial vs PBT | 0.69% — confirms the OCR correction |

The P&L rebuilding exactly from its six expense components is the strongest evidence the
extraction is clean.

### Restatement recorded

The FY2025 AR reports FY2025 consolidated total income of Rs. 6,630.03 crore; the FY2026 AR's
comparative shows Rs. 6,609.77 crore — a Rs. 20.26 crore restatement. The FY2026 AR is used as the
authority for FY2025. Standalone and consolidated are close (FY2026: Rs. 7,196.00 crore vs
Rs. 7,197.07 crore) because subsidiaries are immaterial, but the two bases are never mixed inside
a single ratio.

---

## 4. Financial summary

| | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Total income (Rs. cr) | 5,795.19 | 6,608.68 | 7,196.00 |
| PAT (Rs. cr) | 571.83 | 767.25 | 913.17 |
| RoAA | — | 2.59% | **2.76%** |
| RoAE | — | — | 16.58% |
| Credit cost / avg assets | — | 4.38% | **3.50%** |
| Cost-to-income | — | 44.98% | **49.81%** |
| Gearing (x) | — | 4.99 | **4.56** |
| CRAR | — | 20.30% | 19.44% |
| Tier I CRAR | — | 15.84% | **16.49%** |
| Top-10 borrowings / total | — | 77.34% | 70.68% |

**The composition of FY2026's earnings growth is the analytical point.** PAT rose 19.02%, but the
credit cost fell 88 bps while the cost-to-income ratio rose 483 bps. Operating expenses grew 25.7%
against net total income growth of 13.5%. Earnings improved *despite* the cost line, carried by
lower impairment. If credit costs normalise upward while operating costs stay elevated,
profitability is squeezed from both sides at once. That is stated as the principal credit
challenge.

---

## 5. Rating view and Step 14

Scorecard (RatingScore tab): parent support 1 (w 0.40), profitability 2 (0.20), capitalisation 2
(0.20), asset quality 3 (0.10), funding 3 (0.10) → **composite 1.80, AA band**.

| Instrument | Issuer-disclosed ICRA rating | My view | Divergence |
|---|---|---|---|
| Long-term bank facilities | AA+ (Stable) | AA+ (Stable) | None |
| Short-term bank facilities | A1+ | A1+ | None |
| Subordinated debt | AA+ (Stable) | AA+ (Stable) | None |
| **Perpetual debt** | **AA (Stable)** | **AA (Stable)** | **None** |
| Commercial paper | A1+ | A1+ | None |

**The hybrid notch-down was applied before the disclosure table was read.** On the SBI case
(14-Aug-2026) I produced a single issuer-level view and failed to notch Additional Tier 1
instruments; CRISIL's rationale corrected me. Here that lesson was applied proactively, and the
issuer's disclosure subsequently confirmed perpetual debt at exactly one notch below senior. This
is the first case in this project where a Step 14 finding was carried forward and prevented a
repeat rather than being re-learned.

Also disclosed by the issuer: **CRISIL upgraded the Tier II bond from AA/Positive to AA+/Stable**
during FY2026, and the AR states CRISIL, ICRA and Brickwork upgraded the company. The rating is on
an improving path.

---

## 6. Materiality sweep

| Item | Finding |
|---|---|
| Exceptional items | Rs. 8.61 crore, 0.69% of PBT — immaterial once the OCR error is corrected (§0.3) |
| Parent shareholding | TVS Motor 85.63% — the dominant rating factor |
| Registered office | Relocated Tamil Nadu → Karnataka; CIN changed accordingly |
| Funding concentration | Top-10 borrowings 70.68%, improved from 77.34% but still high |
| Tier II amortisation | Tier II CRAR fell 4.46% → 2.95%, the reason total CRAR eased despite Tier I rising |
| Litigation | GST and service-tax disputes disclosed; individually small (largest Rs. 4.08 crore) |
| Cost-to-income | **Deteriorated 483 bps** — the clearest negative in FY2026 |

---

## 7. Step 17a — section audit, and what the gate caught

First run returned **WARN: absence-claims are unevidenced (failure mode 20)**. Annexure I said
rated amounts were "Not disclosed" and that no ISIN-level schedule was located — asserted, not
proven.

Running the search that the gate demanded **disproved my own claim**:

| Pattern | Hits |
|---|---|
| `rated amount` | 0 |
| `amount rated` | 0 |
| `Rs\. ?[0-9,]+ crore.{0,40}(rated\|programme\|limit)` | 0 |
| `ISIN` | **126** |
| `INE[0-9A-Z]{9}` | **15 unique ISINs** |

The amounts are genuinely absent — now evidenced. But **the ISINs were present all along**, and I
had written that they were not. Annexure I now lists all 15. The gate converted a false statement
into a correct one before publication; without it the report would have carried an untrue absence
claim, which is the single most-repeated failure in this project.

Final: **PASS**, all mandatory sections, quality probes clean.

---

## 8. Searched-and-absent register

| Searched | Result |
|---|---|
| Gross / net stage 3 (NPA) ratios | **Not located.** Asset quality is assessed on the impairment charge alone. A real gap for an NBFC. |
| AUM and disbursements | **Not extractable** — destroyed by the 27% OCR corruption in the narrative sections of the FY2026 AR (§0.2). |
| Rated amounts per programme | Absent — evidenced by three zero-hit patterns (§7). |
| ISIN-level schedule | **Present** — 15 ISINs, now in Annexure I. |
| TVS Credit rationale in reference libraries | Absent — only parent (TVS Motor, TVS Holdings) and sibling (TVS Supply Chain). |
| Post-FY2026 quarterly data | Not used — the only quarterly files supplied belong to Aptus (§0.1). |

---

## 9. Outstanding items

1. **Obtain genuine TVS Credit quarterly results.** The rationale currently has no post-March-2026
   information because the supplied quarterlies are a different company.
2. **Obtain a clean copy of the FY2026 annual report** to recover AUM, disbursements and the
   stage 3 asset-quality ratios.
3. **Read the ICRA NBFC methodology end-to-end.** House style and the analytical frame were taken
   from the methodology index and the SBI Cards peer rationale (structurally the closest peer — a
   parent-supported NBFC), not from a full read.
4. Confirm whether the Aptus files were intended for a separate Aptus case.

## 10. Deliverables

- `TVS Credit Services Limited_15 Aug 2026_ICRA_Rating Rationale.md`
- `TVS Credit Services Limited_15 Aug 2026_Workpaper.md` (this file)
- `TVS Credit Services Limited_Financial_Spreads.xlsx` — Inputs / RatioSuite / TieOut / RatingScore
- `compute_ratios.py` — 9/9 tie-outs · `build_spreads.py`
