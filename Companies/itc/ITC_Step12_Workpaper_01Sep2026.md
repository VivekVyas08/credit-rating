# ITC Limited — Step 12 / 12b workpaper addendum

**Date: 01-Sep-2026.** This addendum closes the Step 12 (forward view) and Step 12b (scorecard
anchor) gap on the three ITC rationales delivered in July 2026 — ICRA 09-Jul-2026, CareEdge
11-Jul-2026, CRISIL 11-Jul-2026. Every figure below is computed in `compute_ratios.py` or
`forward_model.py` from ITC's own Report and Accounts; nothing is taken from a CRA publication.

---

## 1. Why this case needed three scorecards

ITC was rated by all three agencies out of a single case folder. A scorecard carries one
agency's scale, bands and operating-profit convention (Step 12c), so one workbook cannot serve
three reports. `fill_scorecard.py` therefore writes three:

| Workbook | Agency | Rating date | Rating in that rationale |
|---|---|---|---|
| `Rating_Scorecard_ITC Limited_ICRA.xlsx` | ICRA | 09-Jul-2026 | `[ICRA]A1+` |
| `Rating_Scorecard_ITC Limited_CRISIL.xlsx` | CRISIL | 11-Jul-2026 | `Crisil AAA/Stable / Crisil A1+` |
| `Rating_Scorecard_ITC Limited_CareEdge.xlsx` | CareEdge | 11-Jul-2026 | `CARE A1+` |

**Note what the ICRA and CareEdge mandates actually are: a Rs 500 crore COMMERCIAL PAPER
programme, rated on the short-term scale alone.** Neither carries a long-term grade. Only
CRISIL's rationale rates ITC long-term.

**Anchor grade in all three workbooks: AAA / A1+.** Against CRISIL's `Crisil AAA/Stable` that is
a zero-notch divergence; against the two short-term-only mandates the anchor's `A1+` matches the
rating exactly. There is nothing to reconcile on this credit, which is itself worth saying —
most of this project's anchor work is about explaining divergence, and here there is none.

---

## 2. The convention difference, disclosed rather than applied

The three agencies define operating profit differently, and on ITC the difference is real money:

| Basis | Definition | FY2026 operating profit | Margin on OI of 78,868.40 |
|---|---|---|---|
| ICRA `OPBDIT` | PBT + finance cost + depreciation **less other income, unconditionally** | 27,317.91 | 34.64% |
| CareEdge `PBILDT` | TOI less operating expenses; interest/dividend/rental **excluded from TOI**; indirect taxes netted off gross sales | 27,317.91 | 34.64% |
| CRISIL `EBITDA` | PBDIT, which **retains recurring non-operating income** | *29,743.71 if applied strictly* | *37.71%* |

Other income was Rs 2,425.80 crore in FY2026 — a **308 basis point** spread between the two
readings.

**All three workbooks are fed Rs 27,317.91 crore.** That is deliberate and it is not laziness:
all three delivered rationales state that figure. ICRA publishes OPBDIT/OI of 34.6%; CareEdge
publishes PBILDT of 27,318; and CRISIL publishes interest coverage of **321 times**, which on
finance costs of Rs 85.17 crore implies 27,318 and not 29,744. A scorecard contradicting its own
rationale is the defect failure mode 40 exists to prevent, so the difference is **disclosed here
rather than silently applied**. It is a narrow point in substance as well: ITC's other income is
treasury return on surplus cash and dividends from associates, not income from operations, which
is the reading under which CRISIL would strip it too.

---

## 3. The forward view

### The fact the headline hides

| | FY2025 | FY2026 | Change |
|---|---|---|---|
| Gross cigarette revenue (segment note 23B, consolidated) | 35,893.57 | 40,601.00 | **+13.1%** |
| Excise | 6,289.44 | 11,044.93 | **+75.6%** |
| **Cigarette revenue NET of excise** | **29,604.13** | **29,556.07** | **−0.2%** |

**The entire gross growth in the cigarette segment was tax.** Net revenue was flat, and all of
FY2026's group growth (75,323 → 78,868, +4.7%) came from Agri, Paperboards and FMCG-Others.

### Why FY2026 understates the reset

In the company's own words (Q4 FY2026 press release), the GST rate moved *"from 28% of
transaction value to 40% of retail sale price along with a steep hike in excise duties w.e.f 1st
February, 2026 upon phasing out of Compensation Cess"*, producing *"an unprecedented increase in
tax incidence on cigarettes"*. **FY2026 contains two months of that regime. FY2027 contains
twelve.**

### What the model deliberately does not do

It does **not** annualise the two months of new-regime excise into an FY2027 figure. The annual
report gives no month-wise split of the excise line, so any split would be invented; and the GST
component never passes through reported revenue at all, since GST is collected as agent and
netted off while excise is grossed up. The reset reaches ITC's P&L through **volume and mix** —
higher retail prices, and the growth in illicit trade the company explicitly flags — so net
operating income is the modelled primitive and the stress case flexes it directly.

### Base and stress

| Rs crore | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 |
|---|---|---|---|---|---|
| Operating income (base) | 82,023 | 87,765 | 94,786 | 102,369 | 110,558 |
| OPBDIT margin (base) | 33.8% | 34.5% | 35.0% | 35.2% | 35.2% |
| Operating income (stress) | 75,714 | 74,199 | 75,683 | 78,711 | 82,646 |
| OPBDIT margin (stress) | 31.0% | 30.5% | 31.5% | 32.0% | 32.5% |
| Net debt (base) | (23,260) | (25,252) | (27,372) | (29,719) | (32,299) |
| Net debt (stress) | (22,892) | (24,222) | (25,534) | (26,943) | (28,480) |

**The credit conclusion does not move.** Even in the stress — legal volumes falling for two
consecutive years and margin compressing more than 350 basis points — ITC remains in net cash
of more than Rs 28,000 crore while maintaining an 88% dividend payout. The dividend is
deliberately **not** cut in the stress case: ITC has distributed roughly 90% of earnings for
years, and a stress that quietly assumes the board conserves cash would flatter the balance
sheet on no evidence.

---

## 4. Qualitative scores

- **Industry:** no override; the FMCG / Consumer staples sector base of 2 is used. The risk to
  this franchise is fiscal and regulatory rather than competitive, and that is what the sector
  score carries.
- **Business risk 1** — dominant cigarette position alongside genuinely material Agri,
  Paperboards and FMCG-Others businesses, which delivered all of FY2026's growth. Not seriously
  contestable on this horizon.
- **Management 1** — unmodified opinion; hotels demerger executed and disclosed cleanly with
  FY2024 comparatives flagged as not like-for-like rather than quietly restated; capital
  allocation explicit and consistent; and the tax reset disclosed in plain terms rather than
  presenting 13.1% gross cigarette growth without noting net revenue was flat.
- **Support 0** — not applicable. No parent, and ITC is a net creditor to the financial system.
- **Liquidity Superior** — liquid assets of Rs 23,759.43 crore against **total** debt of
  Rs 2,399.06 crore including leases, a 9.9x cover on the whole book, plus Rs 18,464.31 crore of
  operating cash flow against Rs 2,182.89 crore of capex. The only claim of any size is the
  dividend, which is discretionary.

---

## 5. The monitorable

**Legal cigarette volume, not the excise line, and not leverage.** The exposure created by the
February 2026 reset runs to the size of the profit pool, not to whether the debt is paid. The
company itself states the reset is driving *"rapid growth in illicit cigarette volumes"* and
leaving *"a large component of tobacco consumption remaining outside the tax net"*. FY2027 is the
first full year of that regime and is the period to watch.

*Twelve opening-balance tie-outs reconcile in `forward_model.py`, covering operating income,
OPBDIT, the segment arithmetic above, capex, dividend, payout ratio, effective tax rate and the
liquid-assets-to-debt ratio.*
