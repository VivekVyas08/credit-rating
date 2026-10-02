# CRISIL-basis ratio suite for Happy Forgings Limited - RESEARCH NOTE feed (no rating).
# Identical source data/computation to compute_ratios.py (same company, same session, already
# All figures Rs crore, STANDALONE (consolidated is materially identical - subsidiary
# investment is Rs 0.9 cr, immaterial; see workpaper basis note).
# Sources (all traced): Annual-Report-FY-2025-26.md (FY26 audited + FY25 comparative,
# Standalone Balance Sheet L7449-7504, P&L L7508-7549, Note 14.2 Borrowings L9270-9276,
# Note 29 Contingent Liabilities L9799-9811); Happy-Forgings-Limited-AR-2024-25.md
# (FY25 audited + FY24 comparative, Standalone BS L7668-7722, P&L L7747-7785).
#
# Conventions (icra-ratio-engine SKILL.md, adapted per CRISIL criteria-for-manufacturing
# -trading-and-corporate-services-sector.md Section IV): no excise netting (GST-regime
# manufacturer, no excise line in P&L); OPBDITA excludes other income/exceptionals;
# debt includes leases (NIL - no separate Ind AS 116 lease-liability line disclosed in the
# borrowings note across all 3 years; company has ZERO term/non-current debt in every year
# per Note 14 and the FY26 auditor's CARO remark "did not have any term loans outstanding");
# PAT = owners (no NCI, standalone); no JV share; no below-the-line exceptional items in
# any of the 3 years' P&L (FY25 Other Income included a one-off Rs 6.4 cr pre-tax /
# Rs 4.8 cr post-tax insurance receipt per the company's own Q1FY27 IR deck footnote -
# immaterial at 1.8% of FY25 PBT, flagged in the workpaper, not stripped out here).

YEARS = ["FY2024", "FY2025", "FY2026"]          # oldest -> newest

DATA = {
    # ------- P&L (per year), Rs crore -------
    "revenue":      [1358.24, 1408.89, 1546.34],   # Revenue from operations
    "excise":       [0,       0,       0      ],   # not applicable - GST regime
    "other_income": [13.36,   37.57,   30.81  ],   # Other income
    "finance_cost": [11.78,   7.53,    10.47  ],   # Finance costs
    "depreciation": [64.73,   77.06,   89.04  ],   # Depreciation & amortisation
    "pbt_bef_exc":  [324.39,  359.67,  401.99 ],   # PBT (no exceptional line in any year)
    "jv_share":     [0,       0,       0      ],   # none
    "exceptional":  [0,       0,       0      ],   # none reported below the line
    "pat_total":    [242.99,  267.57,  301.64 ],   # Profit for the year
    "nci":          [0,       0,       0      ],   # standalone, no NCI
    "norm_pat":     [None,    None,    None   ],   # not separately disclosed by company
    # ------- Balance sheet (as at year-end), Rs crore -------
    "borrow_nc":    [0,       0,       0      ],   # zero non-current borrowings all 3 years (Note 14)
    "borrow_c":     [143.31,  227.29,  329.62 ],   # Current borrowings (Note 14.2)
    "leases":       [0,       0,       0      ],   # no separate lease-liability line disclosed
    "acceptances":  [0,       0,       0      ],   # none disclosed
    "cash":         [121.73,  216.12,  289.88 ],   # cash + other bank balance + current investments
    "liquid_inv":   [0,       0,       0      ],   # folded into "cash" above (see note)
    "equity_total": [1612.49, 1849.69, 2128.28],   # Total equity
    "total_assets": [1885.95, 2214.64, 2632.96],   # Total assets
    "dtl":          [31.62,   39.33,   48.99  ],   # Deferred tax liabilities (net)
    "cwip":         [121.94,  116.28,  229.31 ],   # Capital work-in-progress
}

# ------- CRISIL's 8 financial-risk parameters (Section IV) - additional inputs, Rs crore -------
DIVIDEND       = [37.68,  37.68,   28.28  ]  # Dividend paid (cash flow statement, standalone)
RECEIVABLES    = [356.92, 426.54,  394.78 ]  # Trade receivables, year-end
INVENTORY      = [224.17, 232.42,  232.76 ]  # Inventories, year-end
PAYABLES       = [55.53,  45.36,   59.43  ]  # Trade payables, year-end
CURRENT_ASSETS = [741.65, 918.60,  1070.99]  # Total current assets
CURRENT_LIAB   = [241.83, 325.63,  455.69 ]  # Total current liabilities (incl. current borrowings)
DEBT_PAYABLE_1YR = [143.31, 227.29, 329.62]  # all debt is short-term/on-demand working capital

def _f(x): return f"{x:,.0f}" if x is not None else "n/a"

def compute(i):
    d = {k: v[i] for k, v in DATA.items()}
    oi      = d["revenue"] - d["excise"]
    opbdita = d["pbt_bef_exc"] - d["jv_share"] + d["finance_cost"] + d["depreciation"] - d["other_income"]
    debt    = d["borrow_nc"] + d["borrow_c"] + d["leases"]
    debt_a  = debt + d["acceptances"]
    liquid  = d["cash"] + d["liquid_inv"]
    pat_own = d["pat_total"] - d["nci"]
    norm    = d["norm_pat"] if d["norm_pat"] is not None else pat_own - d["exceptional"]
    tol     = d["total_assets"] - d["equity_total"]
    ce      = debt + d["equity_total"] + d["dtl"] - d["cwip"]
    print(f"\n=== {YEARS[i]} ===")
    print(f"  OI (net of excise {_f(d['excise'])})     : {_f(oi)}")
    print(f"  OPBDITA                        : {_f(opbdita)}   margin {100*opbdita/oi:.1f}%")
    print(f"  PAT to owners (reported)       : {_f(pat_own)}   normalised: {_f(norm)}")
    print(f"  PAT/OI (reported)              : {100*pat_own/oi:.1f}%")
    print(f"  Total debt excl/incl accept    : {_f(debt)} / {_f(debt_a)}")
    print(f"  Total debt/OPBDITA excl/incl   : {debt/opbdita:.1f}x / {debt_a/opbdita:.1f}x")
    print(f"  Net debt/OPBDITA  excl/incl    : {(debt-liquid)/opbdita:.1f}x / {(debt_a-liquid)/opbdita:.1f}x")
    print(f"  Interest coverage              : {opbdita/d['finance_cost']:.1f}x")
    print(f"  TOL/TNW                        : {tol/d['equity_total']:.2f}x")
    print(f"  RoCE (op PBIT/CE, period-end)  : {100*(opbdita-d['depreciation'])/ce:.1f}%")
    print(f"  [inputs] debt={_f(debt)} (b_nc {_f(d['borrow_nc'])} + b_c {_f(d['borrow_c'])} + leases {_f(d['leases'])}); "
          f"liquid={_f(liquid)}; CE={_f(ce)}")

    # ---- CRISIL Section IV parameters (criteria-for-manufacturing-trading-and-corporate-services-sector.md) ----
    gearing = debt_a / d["equity_total"]
    ncatd = (pat_own - DIVIDEND[i] + d["depreciation"]) / debt_a if debt_a else float("inf")
    current_ratio = CURRENT_ASSETS[i] / CURRENT_LIAB[i]
    gca_days = 365 * CURRENT_ASSETS[i] / oi
    recv_days = 365 * RECEIVABLES[i] / oi
    inv_days = 365 * INVENTORY[i] / oi
    pay_days = 365 * PAYABLES[i] / oi
    cdscr_num = pat_own + d["depreciation"] + d["finance_cost"]
    cdscr = cdscr_num / (DEBT_PAYABLE_1YR[i] + d["finance_cost"])
    roce_crisil = (opbdita - d["depreciation"] + d["other_income"]) / (debt_a + d["equity_total"] + d["dtl"])
    print(f"  Gearing (adj debt/adj networth) : {gearing:.2f}x")
    print(f"  NCATD (net cash accrual/debt)   : {ncatd:.2f}x  ({'n/m - near-zero external debt' if debt_a < 5 else ''})")
    print(f"  Current ratio                   : {current_ratio:.2f}x")
    print(f"  GCA / Receivable / Inventory / Payable days : {gca_days:.0f} / {recv_days:.0f} / {inv_days:.0f} / {pay_days:.0f}")
    print(f"  CDSCR                           : {cdscr:.1f}x")
    print(f"  RoCE (CRISIL basis, PBIT/CE)    : {100*roce_crisil:.1f}%")

if __name__ == "__main__":
    for i in range(len(YEARS)):
        compute(i)
    print("\nReminder: mark not-meaningful ratios n/m with reason; reconcile the newest year "
          "to the company's own disclosed net debt / leverage (state the lease/acceptance basis).")
    print("\n=== TIE-OUT vs company's own IR-deck-disclosed figures (Rs crore, standalone) ===")
    print("FY26: revenue 1,546 (co: 1,546 OK) | EBITDA co-basis 471 vs computed",
          f"{DATA['pbt_bef_exc'][2] + DATA['finance_cost'][2] + DATA['depreciation'][2] - DATA['other_income'][2]:.0f}",
          "(co EBITDA excludes other income, matches) | Debt/Equity co 0.15x vs computed",
          f"{(DATA['borrow_c'][2]) / DATA['equity_total'][2]:.2f}x",
          "| Net Debt/EBITDA co -0.19x (net cash, co includes liquid MF/FD as cash) vs computed here",
          f"{(DATA['borrow_c'][2] - DATA['cash'][2]) / (DATA['pbt_bef_exc'][2] + DATA['finance_cost'][2] + DATA['depreciation'][2] - DATA['other_income'][2]):.2f}x")

# ---- BANK variant (fill instead, per 929): GNPA%, NNPA%, slippage, PCR, CET-1, CRAR (vs minima
#      incl. CCB/D-SIB), NIM, PAT/ATA, RoRWA, cost-to-income, CASA%, LCR, credit/deposit.
# ---- NBFC variant (per 1003): AUM, AUM growth, GNPA/Stage-3, CRAR, gearing, NIM, credit cost, RoMA.
