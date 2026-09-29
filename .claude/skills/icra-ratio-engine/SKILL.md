---
name: icra-ratio-engine
description: Reusable ICRA-definition ratio computation for rating/research workpapers (Steps 5-6 of the SOP). Copy the bundled ratio_template.py to Companies/<slug>/compute_ratios.py, fill the extracted line items, run it. Encodes the ICRA conventions and past-error fixes (OI net of excise, leases in debt, acceptances toggle, NCI-adjusted PAT, normalised vs reported earnings). Triggers - "compute the ratios", "build the workpaper numbers", "ratio suite".
---

# Ratio engine (Steps 5–6)

1. Copy `ratio_template.py` (in this skill folder) to `Companies/<slug>/compute_ratios.py`.
2. Fill ONLY the extraction blocks — every value hand-traced from the statements, units stated (Rs crore), source note recorded in the inline comment. No value enters the template from a broker note or prior report.
3. Run it; paste the output table into the workpaper. The script prints each ratio WITH its inputs so the Response Protocol's data trail comes free.

## Conventions baked into the template (do not re-derive; do not silently override)
- **OI:** revenue from operations; for excise/cess-heavy sectors (tobacco, liquor) OI is **net of excise duty** — reconcile margins to the anchor's KI basis at Step 14 (ITC lesson: 30.9% gross vs 34.6% net).
- **OPBDITA:** PBT-before-exceptionals + finance cost + depreciation − other income − JV/associate share.
- **Total debt:** borrowings (NC + current) + lease liabilities; **acceptances/buyer's credit shown BOTH ways** (steel/trading lesson). Net debt = total debt − cash − current liquid investments.
- **PAT:** attributable to owners, continuing operations (subtract NCI — JSW/ITC lesson); show **reported AND normalised** (exceptionals identified cash vs non-cash, from the company's own disclosure where available).
- **TNW:** excludes revaluation reserves; TOL = total assets − total equity.
- **RoCE:** op PBIT / (debt + net worth + DTL − CWIP), period-end (state if averaging).
- Bank/NBFC variants: use the metric stubs at the bottom of the template (GNPA/NNPA/CET-1/CRAR/NIM; AUM/Stage-3/gearing/RoMA).
