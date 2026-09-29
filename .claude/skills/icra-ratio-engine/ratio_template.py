# ICRA-basis ratio suite - TEMPLATE (copy to Companies/<slug>/compute_ratios.py and fill).
# All figures Rs crore. EVERY value below must be hand-traced to a statement line;
# record the source note in the trailing comment. Never fill from a broker note or anchor.
#
# Conventions (see icra-ratio-engine SKILL.md): OI net of excise where applicable;
# OPBDITA excludes other income / JV share / exceptionals; debt includes leases;
# acceptances shown both ways; PAT = owners, continuing (minus NCI); reported vs normalised.
#
# ⚠ FAILURE MODE 36 - READ BEFORE FILLING `other_expense_addbacks` BELOW.
# `Other Income` and `Other Expenses` are COMPOSITES, not line items. Run
#     python preflight.py <slug>          -> probe [0c] AGGREGATE-NOTE CONTAMINANTS
# and give EVERY component it prints an explicit include-or-exclude decision here.
# The trap is asymmetry, not carelessness: the same forex item is reported inside OTHER INCOME
# when it is a GAIN and inside OTHER EXPENSES when it is a LOSS. Subtracting other_income
# therefore strips the gain automatically but LEAVES THE LOSS INSIDE opex - biasing every loss
# year downward. Balkrishna Industries, 25-Aug-2026: a Rs 290.01 crore forex loss left inside
# Other Expenses produced a 21.25% margin against the agency's actual 24.3%, inverted the
# year-on-year direction, and cost a full rating notch.

# ⚠ FAILURE MODE 38 - WHERE THE FIGURE COMES FROM MATTERS AS MUCH AS WHAT IT IS.
# The cash-flow reconciliation and the Other Income / Other Expenses NOTES both name the same
# items - forex, asset disposals, impairments, write-backs - and they are NOT the same number.
# The cash-flow row is the NON-CASH adjustment that bridges PBT to operating cash flow (for
# forex, the UNREALISED slice only). The NOTE states what the P&L actually booked.
#     -> Take every add-back figure from the NOTE. Never from the cash-flow reconciliation.
#     -> `python preflight.py <slug>` probe [0d] flags items whose two sources disagree.
# Jindal Stainless, 26-Aug-2026: forex was taken from the cash-flow rows (-70.04 / +87.15)
# when the audited note showed net GAINS of 154.37 / 78.41 - wrong in magnitude AND in sign,
# and it survived three rounds of checking because every tie-out still passed.
#
# ⚠ FAILURE MODE 39 - DECOMPOSING A NOTE IS NOT VERIFYING IT.
# Probe [0c] makes you decompose the aggregate note. That is half the job. A decomposition
# that is not TIED BACK to the note's OWN PRINTED TOTAL is still a set of typed numbers that
# nothing checks. Add the note's line items as an input table and tie their sum to the printed
# total - that single tie-out turns every line inside the note into a verified input.
#     -> Then MEASURE coverage instead of counting passes:
#            python tieout_mutation.py <slug>
#        It perturbs each input and reports the ones NO tie-out is sensitive to. Every input it
#        names must gain a check or be listed in DISCLOSED_DIFFERENCES as uncheckable, with the
#        reason. A green suite proves nothing on its own: on Jindal Stainless four of "22/22"
#        tie-outs compared a value to ITSELF and could never fail.
#     -> Never write a tie-out whose computed and disclosed sides read the same cell.

YEARS = ["FY2024", "FY2025", "FY2026"]          # oldest -> newest

DATA = {
    # ------- P&L (per year) -------
    "revenue":      [None, None, None],   # Revenue from operations        <- P&L
    "excise":       [0,    0,    0   ],   # Excise duty (0 if none/not netted by ICRA for this sector)
    "other_income": [None, None, None],   # Other income                   <- P&L
    "finance_cost": [None, None, None],   # Finance costs                  <- P&L
    "depreciation": [None, None, None],   # Depreciation & amortisation    <- P&L
    "pbt_bef_exc":  [None, None, None],   # PBT before exceptional items (before JV share where disclosed)
    "jv_share":     [0,    0,    0   ],   # Share of profit/(loss) of JVs/associates (sign as reported)
    "exceptional":  [0,    0,    0   ],   # Exceptional items (gain +, charge -); note CASH vs NON-CASH
    # NON-OPERATING items sitting INSIDE Other Expenses, added back to OPBDITA (positive = the
    # charge to add back). Forex losses, loss on asset sale, impairments, interest-to-others.
    # MUST be reconciled against preflight probe [0c] - leave at 0 only after checking, never
    # by default. The mirror of `other_income`, which the OPBDITA build already subtracts.
    "other_expense_addbacks": [0, 0, 0],
    "pat_total":    [None, None, None],   # Profit for the year (continuing)
    "nci":          [0,    0,    0   ],   # Non-controlling interests' share of PAT
    "norm_pat":     [None, None, None],   # Company-DISCLOSED normalised PAT if published; else None -> computed
    # ------- Balance sheet (as at year-end) -------
    "borrow_nc":    [None, None, None],   # Non-current borrowings
    "borrow_c":     [None, None, None],   # Current borrowings (incl. current maturities if classified there)
    "leases":       [None, None, None],   # Lease liabilities (NC + current)
    "acceptances":  [0,    0,    0   ],   # Acceptances / buyer's credit (0 if none)
    "cash":         [None, None, None],   # Cash & cash equivalents + other bank balances
    "liquid_inv":   [None, None, None],   # CURRENT investments (liquid); NOT non-current strategic stakes
    "equity_total": [None, None, None],   # Total equity incl. NCI (net worth; check revaluation reserves)
    "total_assets": [None, None, None],   # Total assets
    "dtl":          [None, None, None],   # Deferred tax liabilities (net)
    "cwip":         [None, None, None],   # Capital work-in-progress
}

def _f(x): return f"{x:,.0f}" if x is not None else "n/a"

def compute(i):
    d = {k: v[i] for k, v in DATA.items()}
    oi      = d["revenue"] - d["excise"]
    # + other_expense_addbacks keeps the build SYMMETRIC: other_income is subtracted, so
    # non-operating charges buried in Other Expenses must be added back, or a forex LOSS is
    # penalised while a forex GAIN is stripped (failure mode 36).
    opbdita = (d["pbt_bef_exc"] - d["jv_share"] + d["finance_cost"] + d["depreciation"]
               - d["other_income"] + d["other_expense_addbacks"])
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
    # Make the normalisation VISIBLE every run - a silent 0 is how failure mode 36 hides.
    _ab = d["other_expense_addbacks"]
    print(f"     less other income {_f(d['other_income'])}; "
          f"add back non-op. in opex {_f(_ab)}"
          f"{'  <-- 0: confirm against preflight [0c]' if not _ab else ''}")
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

if __name__ == "__main__":
    for i in range(len(YEARS)):
        compute(i)
    print("\nReminder: mark not-meaningful ratios n/m with reason; reconcile the newest year "
          "to the company's own disclosed net debt / leverage (state the lease/acceptance basis).")

# ---- BANK variant (fill instead, per 929): GNPA%, NNPA%, slippage, PCR, CET-1, CRAR (vs minima
#      incl. CCB/D-SIB), NIM, PAT/ATA, RoRWA, cost-to-income, CASA%, LCR, credit/deposit.
# ---- NBFC variant (per 1003): AUM, AUM growth, GNPA/Stage-3, CRAR, gearing, NIM, credit cost, RoMA.
