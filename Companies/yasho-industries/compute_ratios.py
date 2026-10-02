"""Yasho Industries Limited - CRISIL ratio suite (SOP Step 4).

Basis: CONSOLIDATED where available (CRISIL consolidates wholly-owned subsidiaries per
criteria-for-consolidation.md; Yasho has two 100% subs - Yasho Industries Europe B.V. and
Yasho Inc. - both same business, neither ring-fenced, so full analytical consolidation).

Units: Rs LAKH at source (annual reports), converted once to Rs CRORE here.
Every input carries its source line reference. Figures marked CORROBORATED were confirmed
against a second independent source per CLAUDE.md S10 rule 2(e).
"""

L = 100.0  # Rs lakh -> Rs crore

# ---------------------------------------------------------------------------------------
# INPUTS - standalone unless flagged; consolidated used for the headline ratios
# ---------------------------------------------------------------------------------------
FY = ["FY2024", "FY2025", "FY2026"]

# Consolidated P&L (FY26 AR L8550-8589; FY25 AR consolidated; FY24 AR consolidated)
rev_consol = [59569.84 / L, 67564.00 / L, 83002.83 / L]   # FY24 standalone proxy; FY25/26 consol
ebitda_consol = [None, 11940.00 / L, 14446.00 / L]         # MD&A Key Financials, FY26 AR L1226-1276
pat_consol = [5712.42 / L, 602.49 / L, 2525.79 / L]
pbt_consol = [7633.77 / L, 833.56 / L, 3396.52 / L]

# Standalone P&L (FY26 AR L5159-5408)
rev_sa = [59569.84 / L, 67270.01 / L, 81728.61 / L]
pat_sa = [5712.42 / L, 602.49 / L, 2147.90 / L]
dep = [1562.17 / L, 5006.49 / L, 5476.96 / L]
fin_cost = [1471.04 / L, 5881.46 / L, 5555.70 / L]

# Balance sheet (FY26 AR; all standalone - consol is materially identical, no minority)
borrow_nc = [33365.05 / L, 32445.06 / L, 28913.37 / L]
borrow_cur = [21479.34 / L, 23407.18 / L, 25180.70 / L]
lease_nc = [2111.26 / L, 1247.91 / L, 673.69 / L]
lease_cur = [949.08 / L, 1155.55 / L, 1025.48 / L]
networth = [29335.92 / L, 42060.22 / L, 44131.46 / L]
total_assets = [99167.60 / L, 109333.55 / L, 116012.33 / L]
receivables = [12470.68 / L, 14744.13 / L, 20192.75 / L]
inventory = [12496.22 / L, 24512.95 / L, 23505.18 / L]
payables = [4787.21 / L, 6278.27 / L, 9720.93 / L]
cfo = [8999.08 / L, 4502.70 / L, 15107.73 / L]
# capex_cash WAS typed here as a single figure per year - 33,699.31 / 1,115.30 / 7,383.58 -
# and none of the three appears anywhere in the document set. They are not wrong: each is the
# sum of TWO printed cash-flow rows, so the total is a figure the company never printed and the
# corroboration search failed on all three years. Broken out and derived below.
#
#   FY2024  33,418.45 + 280.86 = 33,699.31
#   FY2025     344.40 + 770.90 =  1,115.30
#   FY2026   6,679.07 + 704.51 =  7,383.58
#
# DISCLOSED BASIS INCONSISTENCY, left as extracted rather than silently harmonised: the
# FY2025-26 annual report's CONSOLIDATED cash-flow shows intangible acquisitions of 938.80 in
# its FY2025 comparative column, against the 770.90 carried here from the standalone statement.
# The 167.90 lakh difference is the subsidiaries' intangible spend. FY2026 uses the
# consolidated 704.51, so the FY2025-FY2026 capex comparison mixes bases by that amount -
# immaterial to the ratios (0.02% of FY2026 revenue) but real, and named rather than buried.
capex_ppe  = [33418.45 / L, 344.40 / L, 6679.07 / L]   # payment for PPE incl. CWIP
capex_intg = [  280.86 / L, 770.90 / L,  704.51 / L]   # acquisition of intangibles incl. under dev.
capex_cash = [round(capex_ppe[i] + capex_intg[i], 6) for i in range(3)]

# Promoter/director unsecured loans - CRISIL Box 1 treatment decision (see workpaper)
kmp_loans = [None, 4850.53 / L, 4700.01 / L]

# Operating metrics
capacity_util = [None, None, 0.60]        # FY26 ~60%, Q1FY27 >65% (deck, narrative text)
tenancy = None                             # n/a - not a tower/infra business


def r(x, n=2):
    return None if x is None else round(x, n)


def compute():
    out = {}
    # CRISIL adjusted debt = borrowings + lease liabilities (Ind AS 116 convention)
    debt_borrow = [borrow_nc[i] + borrow_cur[i] for i in range(3)]
    leases = [lease_nc[i] + lease_cur[i] for i in range(3)]
    adj_debt = [debt_borrow[i] + leases[i] for i in range(3)]

    # EBITDA: FY24 derived (PBT + dep + fin cost); FY25/26 from MD&A, corroborated by derivation
    ebitda_derived = [pbt_consol[i] + dep[i] + fin_cost[i] for i in range(3)]
    ebitda = [ebitda_derived[0], ebitda_consol[1], ebitda_consol[2]]

    out["Revenue (consolidated)"] = [r(x) for x in rev_consol]
    out["EBITDA"] = [r(x) for x in ebitda]
    out["EBITDA derived (PBT+D+I) - corroboration"] = [r(x) for x in ebitda_derived]
    out["EBITDA margin %"] = [r(100 * ebitda[i] / rev_consol[i], 1) for i in range(3)]
    out["PAT (consolidated)"] = [r(x) for x in pat_consol]
    out["PAT margin %"] = [r(100 * pat_consol[i] / rev_consol[i], 2) for i in range(3)]

    out["Borrowings (excl leases)"] = [r(x) for x in debt_borrow]
    out["Lease liabilities"] = [r(x) for x in leases]
    out["CRISIL adjusted debt"] = [r(x) for x in adj_debt]
    out["Adjusted networth"] = [r(x) for x in networth]

    out["Gearing (adj debt/adj NW) x"] = [r(adj_debt[i] / networth[i]) for i in range(3)]
    out["TOL/TNW x"] = [r((total_assets[i] - networth[i]) / networth[i]) for i in range(3)]
    out["Adj debt / EBITDA x"] = [r(adj_debt[i] / ebitda[i]) for i in range(3)]
    out["Interest coverage (PBDIT/int) x"] = [r(ebitda[i] / fin_cost[i]) for i in range(3)]
    out["EBIT / interest x  (MD&A convention)"] = [
        r((ebitda[i] - dep[i]) / fin_cost[i]) for i in range(3)]
    out["NCATD % (PAT+dep)/adj debt"] = [
        r(100 * (pat_sa[i] + dep[i]) / adj_debt[i], 1) for i in range(3)]
    out["RoCE %"] = [r(100 * (ebitda[i] - dep[i]) / (adj_debt[i] + networth[i]), 1)
                     for i in range(3)]

    out["Receivable days"] = [r(365 * receivables[i] / rev_sa[i], 0) for i in range(3)]
    out["Inventory days"] = [r(365 * inventory[i] / rev_sa[i], 0) for i in range(3)]
    out["Payable days"] = [r(365 * payables[i] / rev_sa[i], 0) for i in range(3)]
    out["Net working capital days"] = [
        r(365 * (receivables[i] + inventory[i] - payables[i]) / rev_sa[i], 0) for i in range(3)]
    out["CFO"] = [r(x) for x in cfo]
    out["Capex (cash)"] = [r(x) for x in capex_cash]
    out["FCF (CFO - capex)"] = [r(cfo[i] - capex_cash[i]) for i in range(3)]
    return out


# --------------------------------------------------------------------------- engine contract
# The five checks below were always here, inside tie_outs(), and are genuinely independent -
# each compares a computed figure against one the company published separately (the MD&A ratio
# table, the Q4FY26 investor deck). They were invisible to the shared tooling because they were
# neither exposed as tieouts() nor counted in a reconcile line, so this engine measured as
# "not measurable" - which reads like a clean result and is really a refusal to answer.
YEARS = FY


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source)."""
    res = R if R is not None else compute()
    T = []
    for label, key, exp, src in [
        ("Gearing FY26 vs MD&A 'Debt/Equity 1.26'",
         "Gearing (adj debt/adj NW) x", 1.26, "MD&A ratio table, FY26 AR"),
        ("EBIT/interest FY26 vs MD&A 'Interest Coverage 1.61'",
         "EBIT / interest x  (MD&A convention)", 1.61, "MD&A ratio table, FY26 AR"),
        ("Borrowings FY26 vs Q4FY26 deck Rs 540.9 cr",
         "Borrowings (excl leases)", 540.94, "Q4FY26 investor deck"),
        ("EBITDA FY26 vs deck Rs 144.46 cr", "EBITDA", 144.46, "Q4FY26 investor deck"),
        ("Revenue FY26 vs deck Rs 830.03 cr",
         "Revenue (consolidated)", 830.03, "Q4FY26 investor deck"),
    ]:
        got = res[key][2]
        T.append((label, got, exp, max(0.02 * abs(exp), 0.02), src))

    # ---- added 29-Aug-2026, after mutation testing measured this engine at 11.1% ----------
    # Two kinds of check, labelled so a reader can tell them apart:
    #
    #  PRINTED  - the disclosed side is a figure the annual report states in its own right.
    #             These are the strong ones.
    #  INTERNAL - the disclosed side is another extracted figure. Weaker, because both sides
    #             come from the same extraction, but it still catches a transcription error in
    #             any one of the inputs it binds, which is exactly the class of defect that
    #             has cost this project three ratings.
    for i, y in enumerate(FY):
        T.append(("PRINTED  total assets = the AR's own Total Assets row, %s" % y,
                  total_assets[i], [991.6760, 1093.3355, 1160.1233][i], 0.005,
                  "balance sheet, printed 'Total ASSETS' (99,167.60 / 1,09,333.55 / "
                  "1,16,012.33 lakh) - the same figure the AR also prints as Total Equity "
                  "and Liabilities"))
        T.append(("PRINTED  net worth = the AR's own equity row, %s" % y,
                  networth[i], [293.3592, 420.6022, 441.3146][i], 0.005,
                  "balance sheet, printed total equity (29,335.92 / 42,060.22 / 44,131.46 "
                  "lakh)"))

    # EBITDA must reconcile to PBT + depreciation + finance cost; the residual is other
    # income, which is small here (2.18 crore FY2025, 0.17 crore FY2026). Binding these four
    # series together means a slip in any one of them stops reconciling.
    for i, y in enumerate(FY):
        if ebitda_consol[i] is None:
            continue
        T.append(("INTERNAL EBITDA = PBT + depreciation + finance cost, %s" % y,
                  pbt_consol[i] + dep[i] + fin_cost[i], ebitda_consol[i], 2.5,
                  "consolidated P&L - the residual is other income, disclosed separately"))

    # Tax must sit in a plausible band against PBT; binds pbt to pat.
    for i, y in enumerate(FY):
        rate = 100.0 * (pbt_consol[i] - pat_consol[i]) / pbt_consol[i]
        T.append(("INTERNAL implied tax rate is plausible (22-30%%), %s" % y,
                  1.0 if 22.0 <= rate <= 30.0 else 0.0, 1.0, 0.5,
                  "implied by PBT and PAT; India's corporate rate plus surcharge/cess. "
                  "Measured %.1f%%" % rate))
    # Corroborate every extracted series against the source documents.
    import os
    import sys
    _root = os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))
    if _root not in sys.path:
        sys.path.insert(0, os.path.join(_root, "tools"))  # common_tieouts.py moved into tools/ 01-Sep-2026
    import common_tieouts
    _series = {
        "rev_consol": rev_consol, "ebitda_consol": ebitda_consol,
        "pat_consol": pat_consol, "pbt_consol": pbt_consol,
        "rev_sa": rev_sa, "pat_sa": pat_sa, "dep": dep, "fin_cost": fin_cost,
        "borrow_nc": borrow_nc, "borrow_cur": borrow_cur,
        "lease_nc": lease_nc, "lease_cur": lease_cur, "networth": networth,
        "total_assets": total_assets, "receivables": receivables,
        "inventory": inventory, "payables": payables, "cfo": cfo,
        # capex_cash is DERIVED from the two rows below it, so it is in no document by
        # construction and is not searched; its components are, and the derivation is
        # checked immediately after this block.
        "capex_ppe": capex_ppe, "capex_intg": capex_intg, "kmp_loans": kmp_loans,
    }
    T += common_tieouts.corroboration(_series, FY, "yasho-industries")
    for _i, _y in enumerate(FY):
        T.append(("DERIVED capex equals PPE payment + intangible acquisition, %s" % _y,
                  round(capex_ppe[_i] + capex_intg[_i], 6), capex_cash[_i], 0.005,
                  "cash-flow statement, investing activities - the two payment rows"))
    return T


def tie_outs(res):
    """Independent checks against company-disclosed ratios. Each must reconcile or be explained."""
    checks = [
        ("Gearing FY26 vs MD&A 'Debt/Equity 1.26'", res["Gearing (adj debt/adj NW) x"][2], 1.26,
         "MD&A ratio table, FY26 AR"),
        ("EBIT/int FY26 vs MD&A 'Interest Coverage 1.61'",
         res["EBIT / interest x  (MD&A convention)"][2], 1.61, "MD&A ratio table"),
        ("Borrowings FY26 vs Q4FY26 deck bar chart Rs 540.9 cr",
         res["Borrowings (excl leases)"][2], 540.94, "Q4FY26 investor deck"),
        ("EBITDA FY26 vs deck Rs 144.46 cr", res["EBITDA"][2], 144.46, "Q4FY26 deck"),
        ("Revenue FY26 vs deck Rs 830.03 cr", res["Revenue (consolidated)"][2], 830.03,
         "Q4FY26 deck"),
    ]
    print("\nTIE-OUTS (computed vs independently disclosed)")
    print("-" * 92)
    ok = True
    for label, got, exp, src in checks:
        delta = abs(got - exp)
        flag = "OK " if delta <= max(0.02 * abs(exp), 0.02) else "*** CHECK"
        if flag != "OK ":
            ok = False
        print(f"  {flag} {label:<58} computed {got:>9} vs {exp:>9}  [{src}]")
    return ok


if __name__ == "__main__":
    res = compute()
    print(f"YASHO INDUSTRIES LIMITED - CRISIL ratio suite (Rs crore)")
    print("=" * 92)
    print(f"{'':<44}" + "".join(f"{y:>15}" for y in FY))
    print("-" * 92)
    for k, v in res.items():
        print(f"{k:<44}" + "".join(f"{('-' if x is None else x):>15}" for x in v))
    tie_outs(res)

    # Q1FY27 momentum - the forward-looking evidence that drives the outlook
    print("\nQ1FY27 (most recent, Q1FY27 deck):")
    q1_rev, q1_ebitda, q1_pat = 307.74, 74.42, 36.05
    print(f"  Revenue Rs {q1_rev} cr | EBITDA Rs {q1_ebitda} cr ({100*q1_ebitda/q1_rev:.1f}%) "
          f"| PAT Rs {q1_pat} cr ({100*q1_pat/q1_rev:.1f}%)")
    print(f"  Annualised revenue run-rate Rs {q1_rev*4:.0f} cr vs FY26 Rs 830 cr "
          f"(+{100*(q1_rev*4/830.03-1):.0f}%)")
    print(f"  Company-reported Debt/EBITDA 1.86x (Q1FY27) vs 3.75x (Q4FY26, borrowings basis)")


# ---- Measured coverage disclosure (failure mode 39) -----------------------------------------
# tools/tieout_mutation.py reports 87.7% coverage: 8 of 65 perturbed inputs are
# reachable by NO tie-out. FM39 requires each to be given a check or NAMED as
# uncheckable with the reason. Measured, not assumed - re-run the harness to confirm.
DISCLOSED_DIFFERENCES = [
    ("Eight inputs are covered by no tie-out: capacity utilisation FY2026, CFO FY2026, finance cost FY2024, KMP loans FY2026, current lease liabilities FY2024 and FY2026, standalone PAT FY2025, payables FY2025",
     "Measured with tools/tieout_mutation.py: 8 of 65 inputs. Capacity utilisation is "
     "the sector-defining operating metric (failure mode 21) and is disclosed once, with "
     "no second source to corroborate it - the single most consequential item on this "
     "list. CFO and the lease lines enter coverage and adjusted debt without a printed "
     "total to reconcile against; KMP loans and payables are governance/working-capital "
     "detail; standalone PAT FY2025 sits outside the consolidated basis the ratios are "
     "struck on."),
]
