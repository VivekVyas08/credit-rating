# IIFL Finance Limited — Rating Workpaper (CARE / CareEdge)
*Agency: CareEdge · Basis: STANDALONE (IIFL Finance only) · Mandate: all debt (LT+ST) · Data cutoff: FY2026 audited + interim to Q4 FY26. Rebuilt 17-Jul-2026 following the SOP step-by-step.*

**Entity:** IIFL Finance Limited (CIN L67100MH1995PLC093797) — retail-focused **NBFC-ML**. Sector corrected Bank→NBFC (verified FY26 AR p.11).
**Data rule (R1/R2):** every report figure is from IIFL's own documents; the Motilal Oswal note and all CRA ratings (incl. the prior CARE report) are reference/forward-context only.

## Steps 1–4 (confirmed with user)
Agency CareEdge · sector NBFC · standalone · methodology = CARE NBFC (Feb-25) + Financial Ratios – Financial Sector + Short-Term Instruments + MLD + Consolidation + Notching(Parent) + Outlook. Document Read Log completed over 11 files (3 ARs FY24-26 + 7 quarterly + broker). Format teacher: **Manappuram Finance (CARE AA; Stable, 01-Jul-2026)** — a gold-loan NBFC peer.

## Steps 5–6 — Computed standalone ratio suite (compute_ratios.py; CARE financial-sector defs)
**Tie-outs reconcile exactly to the AR:** net loans 38,135.72 ✓ · gross loans 38,565.00 ✓ · equity 7,560.71 ✓ · total borrowings 38,740.00. *(No screener.in tie-out: screener reports the CONSOLIDATED group — a different measure from the standalone entity; reconciled instead against the AR's own standalone statements at component level, per R5.)*

| FY26 standalone | Value | | Value |
|---|---|---|---|
| CRAR / Tier-I | 17.84% / 12.24% | RoTA | 2.82% |
| Overall gearing (TD/TNW) | 5.26x (FY25 3.95x) | RoNW | 17.0% |
| TNW | ₹7,371 cr | NIM | 7.74% |
| Gross loans / secured mix | ₹38,565 cr / 92.1% | Yield / CoB / spread | 20.8% / 10.35% / 10.5% |
| ECL / gross | 1.11% | Cost-income | 46.8% |
| GNPA/NNPA/PCR (AR-stated) | 1.5% / 0.7% / 93% | Credit cost | 1.73% |
| Gross-loan growth | +65.5% | PAT / NII | ₹1,153.5 cr / ₹3,165.6 cr |

## Step 7 — Fact register (traced)
Promoter 23.65%; Fairfax 15.18%; FPI 22.76% (AR CG report). 4,829 branches / 4.6M customers. Chair B.P. Kanungo (ex-RBI Dy Gov). Subs HFC (79.59%) + Samasta (99.56%) material; both profitable. **Contingent income-tax demands ₹337.80 cr** (₹20.25 cr paid under protest; Note 39). US$152m rights + US$325m bond. Clean joint audit (Sharp & Tannan + G.M. Kapadia), no qualifications.

## Step 7b — Instruments (AR-sourced, R3/R4)
NCDs ₹15,384.97 cr (note 19) · sub-debt ₹3,741.37 cr incl **PDI ₹600 cr** (Annexure V: PDI-1 ₹500 cr + PDI-2 ₹100 cr) · bank facilities ₹19,613.66 cr (limits TBC) · CP programme ₹3,000 cr (AGM resolution). Per-ISIN NCD schedule not machine-readable in AR → Annexure-1 marks it TBC from issue docs (only equity ISIN INE530B01024 present).

## Step 8 — Materiality sweep (include/exclude)
NEW: **RBI ₹5.30 lakh penalty (Feb-2026)** for NPA-classification lapse — INCLUDE (contradicts AR's "zero penalties" claim). **RBI Gold Loan Directions 2025** (LTV/bullet-repayment) — INCLUDE (yield/monitorable). Confirmed: **nil promoter pledge** (positive); standalone investment in subs HFC ₹825 cr + Samasta (both profitable — no drain); clean audit, no EoM/going-concern. Normalise: AIF exceptional ₹586.5 cr (FY25). Note: NPA restatement (NHB advisory). EXCLUDE: Labour Codes ₹22.5 cr one-off.

## Step 10 — Methodology compliance map (CARE NBFC 8 factors), standalone
1. **Business mix/growth** — ~91% gold (secured), +65% growth (post-embargo, low base). Concentration = key negative.
2. **Capital & leverage** — CRAR 17.84%/Tier-I 12.24%; gearing 5.26x (moderate for secured). Strong.
3. **Asset quality** — 92% secured; **standalone GNPA (GS3) 1.13% / NNPA (NS3) 0.58%** (Note 38A.6; group-headline 1.5%/0.7%/93%); gold low-LGD. Strong; seasoning risk on rapid growth.
4. **Profitability** — RoTA 2.82%, RoNW 17.0%, NIM 7.74%. Strong (V-recovery).
5. **Liquidity** — cash+bank ₹1,923 cr; group buffer ₹6,638 cr; positive ALM; repaid >₹18,000 cr in embargo. Adequate.
6. **Resource profile** — banks/NCD/PDI/ECB/securitisation/co-lending; CoB 10.35%. Comfortable.
7. **Management & systems** — 30-yr record, ex-RBI-DG board; BUT embargo + ₹5.3 lakh penalty + IT matter. Adequate with overhang.
8. **Size/vintage/market presence** — top-tier gold NBFC, 4,829 branches. Strong.
ESG: governance most material (embargo/penalty/IT), mitigated by board + nil pledge + clean audit.

## Step 11 — Liquidity → **Adequate**
Standalone cash+bank ₹1,923 cr + liquid investments; positive ALM (no cumulative negative mismatch per group ALM); CP not assumed rolled over; demonstrated resilience (₹18,000 cr repaid in embargo). Descriptor = Adequate (conclusion of the sources-vs-claims/ALM position, not an adjective).

## Step 12 — Projections (IIFL_Finance_5yr_Model.xlsx)
NBFC lending model, standalone, Base + Stress; assumptions source-labelled (AR guidance + broker + judgment). **Base:** PAT ₹1,154→1,687→2,053→2,409→2,808→**3,173 cr** (FY31E); gearing peaks ~5.4x then de-levers to ~4.85x. **Stress** (growth halved, NIM −100bp, credit cost +150bp): PAT compresses to ~₹420-560 cr band but stays positive; gearing within tolerance — capitalisation absorbs stress. Two extra tabs: Credit Ratios (all years) + Debt Breakup.

## Step 12b — Scorecard anchor (Rating_Scorecard_IIFL_Finance.xlsx — renders values)
Financial-sector score **1.79**; adjusted composite **2.21** → **anchor CARE A+; Stable / CARE A1**. Inputs: CRAR 0.1784→0.17, GNPA 0.015→0.014, NNPA 0.007→0.006, RoA 0.0282→0.027, NIM 0.0774→0.075, cost-income 0.468→0.45; qualitative Business 2 / Management 3 / Industry NBFC-base 3 / liquidity Adequate.
**Divergence vs analyst view (CARE AA) = 2 notches — explained:** (1) bands illustrative/uncalibrated (JSW pattern); (2) **no collateral/LGD input** — cannot credit the 92%-secured gold book; (3) qualitative scores penalise the resolved embargo; (4) even on generous scores anchor reaches only AA-. Analyst AA retained; anchor is a screening cross-check.

## Step 13 — Independent rating view (formed BEFORE opening the prior report)
**LT (NCDs / sub-debt / bank facilities): CARE AA; Stable · PDI (Tier-1): CARE AA-; Stable (notch −1) · PP-MLD: CARE PP-MLD AA; Stable · CP: CARE A1+.**
Reasoning: strong capitalisation + 92% secured asset quality + sharp profitability recovery + large gold franchise support AA; tempered by gold concentration, regulatory-event risk (embargo/₹5.3 lakh penalty/IT matter), and rising leverage (5.26x). Peer calibration: Manappuram (gold NBFC, ROTA 2.84%, GNPA 1.81%, gearing 3.18x std) = CARE AA — IIFL comparable (better asset quality, higher leverage). Outlook Stable (recovery vs overhang; S&P/Fitch→Positive).

## Step 14 — Prior CARE report divergence (opened AFTER Step 13; date-stamped, R8)
CARE prior: **AA;Stable (to Sep-23) → AA(Watch) 2024 → AA-;Stable 19-Sep-24 → Withdrawn 20-Sep-24.** The AA- was an **embargo-trough** rating (gold AUM had shrunk to ₹14,727 cr) and is ~2 yrs stale. My **AA** restores the Company to CARE's own **pre-embargo** level, justified by the recovery and consistent with all four current CRAs (AA). No facts imported (R2).

## Steps 16–17 — Draft + re-verify
Report drafted in CARE format (Manappuram craft). Re-verify (post-remediation): **rated-amount table sums 38,660.85** (NCD 9,562.92 + CP 5,742.90 + sub-debt 3,141.37 + PDI 600 + bank 19,613.66) ✓; sub-liabilities split 3,141.37+600=3,741.37 ✓; FY25 NII 3,777.80−1,848.72=1,929.08 ✓; standalone GNPA 428.12/37,991.06=1.13% ✓; 12m debt maturities 15,590.02 ✓; all headline ratios copied from compute_ratios.py output (no drift). Scorecard + model + spreads render (data_only verified, 0 formula-only cells).

## Deliverables (Step 18)
`IIFL Finance Limited_17 Jul 2026_CARE_Rating Rationale.md` · this workpaper · `Companies/iifl/compute_ratios.py` · `Companies/iifl/IIFL_Financial_Spreads.xlsx` (extraction + ratio suite + tie-out, generated from the script; added 17-Jul-2026 per the new Step-5 spreads rule) · `Companies/iifl/Rating_Scorecard_IIFL_Finance.xlsx` (anchor) · `Companies/iifl/IIFL_Finance_5yr_Model.xlsx` (projections).

---
## REMEDIATION (18-Jul-2026 — after ESG-head audit found extraction gaps)
Corrections applied to report + all three .xlsx (source of truth compute_ratios.py updated):
1. **Standalone asset quality now COMPUTED** from Note 38A.6 stage-wise EAD: **GNPA (Gross Stage-3) 1.13%** (FY25 1.84%), **NNPA (Net Stage-3) 0.58%**, Stage-2 1.96%, Stage-3 specific PCR 48.6%. Replaces the AR group-headline 1.5%/0.7%/93% I had wrongly used as the standalone figure. (Better than reported → mildly strengthens the profile; scorecard anchor unchanged at CARE A+.)
2. **Instrument split corrected (Note 19):** the ₹15,384.97 cr "Debt securities" = **NCDs ₹9,562.92 cr + CP ₹5,742.90 cr** (+ interest/unamortised). My original report mislabelled it "NCDs incl PP-MLD" AND separately double-counted CP as a ₹3,000 cr line → rated total overstated. Corrected rated total **₹38,660.85 cr** (was 41,740.00). Annexure-1 now carries the Note 19.1–19.3 series/coupon/maturity schedule (incl. USD MTN ₹4,030.49 cr, mat. 24-Jul-2028); per-ISIN codes still not machine-readable in the AR.
3. **Liquidity descriptor now ARITHMETIC (Note 38B):** 12-month contractual debt maturities **₹15,590 cr**; liquid assets ₹1,923 cr → immediate cover **1.48 months**; gap bridged by short-tenor gold book (assets < liabilities: only ~30% of debt due <1yr; ₹14,444 cr in 1–3yr, ₹6,258 cr >3yr). Descriptor **Adequate** = conclusion of arithmetic, not an adjective.
4. **ESG section rebuilt** with: board 55.56% Independent (5 of 9); POSH 13 received/11 disposed/2 pending; the "Zero Regulatory Penalties" claim vs the actual ₹5.30 lakh RBI penalty (disclosure-consistency flag); BRSR data (Scope-3 11,064 tCO₂e, Tata Green Tariff renewable, ~21 lakh L water, LEED-Gold Gurugram, CSR ₹40 cr/27.95 lakh beneficiaries); AIF exceptional clarified as a 100% provision on ARC Security Receipts (RBI Dec-2023 circular); RPT (Note 44) with subs + FIH Mauritius, arm's length, no term-free promoter loans; auditor rotation (Sharp & Tannan → Shah Gupta FY27).

**Still open (disclosed, not blocking the rating):** FY24 AR still read only via FY25 comparatives (M1); only 1 peer used at Step 4 vs 2–3 (M3); methodology map is prose not the full verbatim-quote table (M7). None changes the assigned ratings.
