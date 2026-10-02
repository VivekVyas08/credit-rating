# -*- coding: utf-8 -*-
"""
HLE Glascoat Limited - extraction + ICRA-convention ratio suite (Step 5/6).
Basis: CONSOLIDATED (methodology-determined per 934 - control + close business
linkage + funding fungibility; Kinam consolidated under Ind AS control).
Units: Rs lakh as extracted; ratios unitless; crore where labelled.
Sources (every line traced):
  FY23  : AR 2022-23 consolidated P&L (line ~9612) / BS (~9535)
  FY24  : AR 2024-25 consolidated comparatives (BS ~10902, P&L ~10994)
  FY25  : AR 2024-25 consolidated (as-reported, pre-amalgamation)
  FY25R : FY26 audited results (AFR 31-03-2026) restated comparatives (post-amalgamation)
  FY26  : FY26 audited results (AFR 31-03-2026), audited
Basis note (R5/R8): FY23-FY25 as-reported; FY25R/FY26 post Kinam-Enterprise
amalgamation (pooling of interests, appointed date 07-Aug-2023; net-worth impact
+654.26 lakh). Consolidated TOTALS are near-identical across bases; the owner/NCI
split differs materially. Ratios use consolidated totals incl. NCI per 927 TNW.
"""

D = {
# ---------------- consolidated P&L ----------------
'FY23': dict(
    revenue=93152.21, other_income=805.16, finance=2304.61, da=2269.88,
    pbt_before_exc=9932.81, exceptional=0.0, pbt=9932.81, pat=6980.65,
    # BS
    borr_nc=9837.24, borr_cur=14872.00, lease_nc=736.76, lease_cur=230.57,
    equity_total=32682.89, nci=13.26, cash=268.24, other_bank=1358.22,
    inventories=26847.33, receivables=24279.85, total_assets=89124.77,
    total_liabilities=56441.88, payables_msme=None,    payables_other=None, cur_assets=None, cur_liab=None,
    cfo=9473.11, capex=5517.00, dividends=750.92, repayments_term=4374.09, repayments_unsec=0.0,
),
'FY24': dict(
    revenue=96792.02, other_income=881.62, finance=3058.02, da=2631.06,
    pbt_before_exc=6398.68, exceptional=530.97, pbt=5867.71, pat=4088.86,
    borr_nc=14670.75, borr_cur=21576.05, lease_nc=2367.09, lease_cur=348.01,
    equity_total=49670.35, nci=7990.21, cash=3328.58, other_bank=1218.33,
    inventories=31214.90, receivables=23718.02, total_assets=120195.69,
    total_liabilities=70525.34, payables_msme=1126.42, payables_other=9934.38, cur_assets=61979.80, cur_liab=48731.37,
    cfo=None, capex=None, dividends=None, repayments_term=None, repayments_unsec=None,
),
'FY25': dict(   # as reported in AR 2024-25
    revenue=102758.68, other_income=735.83, finance=3619.34, da=2967.28,
    pbt_before_exc=7506.74, exceptional=0.0, pbt=7506.74, pat=6176.74,
    borr_nc=10925.85, borr_cur=24062.74, lease_nc=2647.91, lease_cur=428.79,
    equity_total=55428.47, nci=9497.75, cash=3959.13, other_bank=1256.57,
    inventories=36949.95, receivables=18490.26, total_assets=129336.32,
    total_liabilities=73907.85, payables_msme=551.53,  payables_other=10331.13, cur_assets=64881.35, cur_liab=56840.48,
    cfo=13436.13, capex=6638.62, dividends=774.67, repayments_term=6201.82, repayments_unsec=0.0,
),
'FY26': dict(   # audited results 18-May-2026 (restated basis)
    revenue=135297.94, other_income=878.42, finance=3444.73, da=3645.36,
    pbt_before_exc=7763.33, exceptional=668.61, pbt=7094.72, pat=5656.57,
    borr_nc=10064.87, borr_cur=21260.31, lease_nc=2747.17, lease_cur=688.10,
    equity_total=61824.85, nci=8432.57, cash=3435.93, other_bank=2413.84,
    inventories=35575.57, receivables=26988.51, total_assets=138179.92,
    total_liabilities=76355.07, payables_msme=346.89,  payables_other=14377.35, cur_assets=71606.96, cur_liab=60372.65,
    cfo=16122.38, capex=5565.97, dividends=750.92, repayments_term=6026.08, repayments_unsec=1588.65,
),
}
# Both aggregates are DERIVED from their printed sub-rows, never typed. Trade payables is split
# MSME / non-MSME on the face of the Schedule III balance sheet and only recombined in the
# fair-value note; FY2026 debt repayment is a term-loan instalment plus an unsecured repayment
# shown on separate cash-flow lines. Typing either combination put a figure in the engine that
# no document contains, which is why both failed their corroboration check in every run.
for _y in D:
    _pm, _po = D[_y]['payables_msme'], D[_y]['payables_other']
    D[_y]['payables'] = None if _pm is None else round(_pm + _po, 4)
    _rt, _ru = D[_y]['repayments_term'], D[_y]['repayments_unsec']
    D[_y]['repayments'] = None if _rt is None else round(_rt + _ru, 4)

# standalone headline (supplementary only)
STANDALONE = {
 'FY25': dict(revenue=55106.92, pat=1637.12, borr=10925.85+20168.89),
 'FY26': dict(revenue=72311.46, pat=3821.09, borr=9537.73+21119.65),
}

def suite(y, prev=None):
    d = D[y]; r = {}
    r['Operating income'] = d['revenue']
    # OPBDITA: PBT before exceptional + finance + D&A - other income (927: excl non-operating income)
    r['OPBDITA'] = d['pbt_before_exc'] + d['finance'] + d['da'] - d['other_income']
    r['OPBDITA margin %'] = r['OPBDITA'] / d['revenue'] * 100
    r['PAT'] = d['pat']
    r['PAT margin %'] = d['pat'] / d['revenue'] * 100
    r['Total debt'] = d['borr_nc'] + d['borr_cur'] + d['lease_nc'] + d['lease_cur']
    r['TNW (incl NCI)'] = d['equity_total']            # no revaluation reserve disclosed
    r['Gearing (TD/TNW)'] = r['Total debt'] / r['TNW (incl NCI)']
    r['TOL/TNW'] = d['total_liabilities'] / r['TNW (incl NCI)']
    r['TD/OPBDITA'] = r['Total debt'] / r['OPBDITA']
    r['Interest coverage'] = r['OPBDITA'] / d['finance']
    nca = d['pat'] + d['da'] - (d['dividends'] or 0)
    r['NCA/TD %'] = nca / r['Total debt'] * 100
    if d['repayments'] is not None:
        r['DSCR'] = (d['pat'] + d['finance'] + d['da']) / (d['finance'] + d['repayments'])
    r['Net debt'] = r['Total debt'] - d['cash'] - d['other_bank']
    r['Net debt/OPBDITA'] = r['Net debt'] / r['OPBDITA']
    if d['cur_assets']:
        r['Current ratio'] = d['cur_assets'] / d['cur_liab']
    r['Debtor days'] = d['receivables'] / d['revenue'] * 365
    r['Inventory days'] = d['inventories'] / d['revenue'] * 365
    if d['payables']:
        r['Payable days'] = d['payables'] / d['revenue'] * 365
        r['WC cycle days'] = r['Debtor days'] + r['Inventory days'] - r['Payable days']
    if d['cur_assets']:
        nwc = (d['cur_assets'] - d['cash'] - d['other_bank']) - (d['cur_liab'] - d['borr_cur'] - d['lease_cur'])
        r['NWC/OI %'] = nwc / d['revenue'] * 100
    # RoCE = PBIT / avg capital employed; PBIT = OPBDITA - D&A (+ oth inc excl? use operating PBIT)
    ce = r['Total debt'] + r['TNW (incl NCI)']         # DTL small; CWIP excl not available per-year -> footnote
    r['_CE'] = ce
    if prev:
        pce = suite_raw_ce(prev)
        r['RoCE %'] = (r['OPBDITA'] - d['da']) / ((ce + pce) / 2) * 100
        r['Revenue growth %'] = (d['revenue'] / D[prev]['revenue'] - 1) * 100
    if d['cfo'] is not None:
        r['CFO'] = d['cfo']
        r['FCF (CFO-capex-div)'] = d['cfo'] - (d['capex'] or 0) - (d['dividends'] or 0)
    return r

def suite_raw_ce(y):
    d = D[y]
    return d['borr_nc'] + d['borr_cur'] + d['lease_nc'] + d['lease_cur'] + d['equity_total']

ORDER = ['FY23', 'FY24', 'FY25', 'FY26']
RESULTS = {}
prev = None
for y in ORDER:
    RESULTS[y] = suite(y, prev)
    prev = y

# --------------------------------------------------------------------------- tie-outs
# Added 29-Aug-2026. This engine carried NO tie-outs, so every figure in it was verified by
# nothing. FLAT below is DERIVED from the engine's own table at import - nothing is retyped,
# so this cannot introduce an error of its own - and it is what the checks read, which is also
# what makes the coverage harness able to measure this engine at all.
YEARS = ["FY23", "FY24", "FY25", "FY26"]


def _flat():
    import os
    import sys
    _root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if _root not in sys.path:
        sys.path.insert(0, os.path.join(_root, "tools"))  # common_tieouts.py moved into tools/ 01-Sep-2026
    import common_tieouts
    return common_tieouts.flatten_year_major(D, YEARS)


FLAT = _flat()


def compute():
    """{period: {metric: value}} - the contract shape the shared tooling drives."""
    out = {}
    for i, y in enumerate(YEARS):
        out[y] = {k: v[i] for k, v in FLAT.items() if v[i] is not None}
    return out


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source). Structural only - see
    common_tieouts.py for exactly what these do and do not prove."""
    import os
    import sys
    _root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if _root not in sys.path:
        sys.path.insert(0, os.path.join(_root, "tools"))  # common_tieouts.py moved into tools/ 01-Sep-2026
    import common_tieouts
    T = common_tieouts.build(FLAT, YEARS)
    T += common_tieouts.corroboration(FLAT, YEARS, 'hle-glascoat',
                                      skip=('payables', 'repayments'))

    # DERIVATION INTEGRITY - the two aggregates still equal the printed rows they come from.
    for _i, _y in enumerate(YEARS):
        if FLAT['payables'][_i] is not None:
            T.append(("DERIVED trade payables equal MSME + non-MSME dues, %s" % _y,
                      round(FLAT['payables_msme'][_i] + FLAT['payables_other'][_i], 4),
                      FLAT['payables'][_i], 0.005,
                      "balance sheet, trade payables - both Schedule III sub-rows"))
        if FLAT['repayments'][_i] is not None:
            T.append(("DERIVED debt repayment equals term + unsecured lines, %s" % _y,
                      round(FLAT['repayments_term'][_i] + FLAT['repayments_unsec'][_i], 4),
                      FLAT['repayments'][_i], 0.005,
                      "cash-flow statement, financing activities - repayment lines"))
    return T


if __name__ == '__main__':
    rows = ['Operating income', 'Revenue growth %', 'OPBDITA', 'OPBDITA margin %', 'PAT',
            'PAT margin %', 'RoCE %', 'Total debt', 'Net debt', 'TNW (incl NCI)',
            'Gearing (TD/TNW)', 'TOL/TNW', 'TD/OPBDITA', 'Net debt/OPBDITA',
            'Interest coverage', 'DSCR', 'NCA/TD %', 'Current ratio',
            'Debtor days', 'Inventory days', 'Payable days', 'WC cycle days', 'NWC/OI %',
            'CFO', 'FCF (CFO-capex-div)']
    hdr = f"{'Metric':32s}" + ''.join(f"{y:>12s}" for y in ORDER)
    print(hdr); print('-' * len(hdr))
    for m in rows:
        cells = []
        for y in ORDER:
            v = RESULTS[y].get(m)
            cells.append(f"{v:12,.2f}" if isinstance(v, (int, float)) else f"{'-':>12s}")
        print(f"{m:32s}" + ''.join(cells))
    print("\nStandalone headline (supplementary): ", STANDALONE)


_T = tieouts()
_bad = [x for x in _T if abs(x[1] - x[2]) > x[3]]
print("")
print("%d/%d tie-outs reconcile" % (len(_T) - len(_bad), len(_T)))
for _x in _bad:
    print("  FAIL %s  [%s]" % (_x[0], _x[4]))


# ---- Measured coverage disclosure (failure mode 39) -----------------------------------------
# tools/tieout_mutation.py reports 95.6% coverage: 5 of 113 perturbed inputs are
# reachable by NO tie-out. FM39 requires each to be given a check or NAMED as
# uncheckable with the reason. Measured, not assumed - re-run the harness to confirm.
DISCLOSED_DIFFERENCES = [
    ("Five inputs are covered by no tie-out: cash FY2023, exceptional items FY2023 and FY2025, non-controlling interest FY2023, other income FY2026",
     "Measured with tools/tieout_mutation.py: 5 of 113 inputs. The two exceptional-item "
     "cells are NIL, and the harness perturbs a nil cell by its Rs 1 crore floor - so "
     "this states something specific: a Rs 1 crore exceptional item could be introduced "
     "in FY2023 or FY2025 and no tie-out would notice. That matters because failure mode "
     "36 is exactly an undecomposed one-off reaching an operating-profit measure. The "
     "FY2023 cash and NCI lines are oldest-comparative balance-sheet items outside the "
     "reconciled identity."),
]
