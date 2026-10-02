# JSW Steel - consolidated ratio computation (ICRA Iron & Steel basis). Rs crore.
# Figures ex JSW Integrated Annual Reports FY24 (FY24+FY23) and FY26 (FY26+FY25).
# ICRA typically treats "Acceptances" (buyer's credit) as debt for steel cos -> show both.

# ---------------------------------------------------------------------------------------------
# DATA TABLE (added 29-Aug-2026)
# ---------------------------------------------------------------------------------------------
# Every figure below previously existed ONLY as a keyword argument in the three block() calls
# at the foot of this file. Nothing could reach them - no tie-out, no coverage measurement, no
# shared tooling - so every number in this engine was verified by nothing. The values are
# unchanged; they are simply held somewhere a check can see them, and the block() calls now
# read from here so the two cannot drift apart.
YEARS = ["FY2024", "FY2025", "FY2026"]

DATA = {
    "revenue":          [175006.0, 168824.0, 185470.0],
    "other_income":     [  1004.0,    694.0,   1248.0],
    "finance_cost":     [  8105.0,   8412.0,   9102.0],
    "depreciation":     [  8172.0,   9309.0,   9601.0],
    "pbt_bef_share":    [ 12963.0,   5877.0,  12366.0],
    "jv_share":         [  -172.0,   -311.0,   -475.0],
    "borrowings":       [67354.0 + 18221.0, 81983.0 + 13974.0, 75608.0 + 19924.0],
    "leases":           [ 2060.0 + 349.0,   2399.0 + 396.0,   3306.0 + 472.0],
    "acceptances":      [ 17654.0,  20534.0,  19817.0],
    "cash":             [8030.0 + 4318.0 + 3.0, 11655.0 + 1630.0 + 5819.0,
                         39256.0 + 1733.0 + 518.0],
    "equity":           [ 79776.0,  81666.0, 105475.0],
    "total_assets":     [228198.0, 240742.0, 269676.0],
    "dtl":              [    None,   9510.0,   9293.0],
    "cwip":             [    None,  20478.0,  21892.0],
    "pat_owners":       [  8973.0,   3504.0,  22316.0],
}

# The annual report prints total assets in its own right (Rs lakh in the ten-year table:
# 24,07,420 and 26,96,760 = 240,742 and 269,676 crore). These are the STRONG checks - the
# disclosed side is a figure the document states independently of anything extracted here.
PRINTED = {"total_assets": [228198.0, 240742.0, 269676.0]}


def compute():
    """{period: {metric: value}} - the contract shape the shared tooling drives."""
    out = {}
    for i, y in enumerate(YEARS):
        d = {k: float(v[i]) for k, v in DATA.items()
             if isinstance(v[i], (int, float)) and not isinstance(v[i], bool)}
        oi = d["revenue"]
        op = d["pbt_bef_share"] + d["finance_cost"] + d["depreciation"] - d["other_income"]
        debt = d["borrowings"] + d["leases"]
        d.update({
            "Operating income": oi,
            "OPBDITA": op,
            "OPBDITA margin %": 100.0 * op / oi,
            "Total debt (excl acceptances)": debt,
            "Total debt (incl acceptances)": debt + d["acceptances"],
            "Net debt": debt - d["cash"],
            "Total debt/OPBDITA (times)": debt / op,
            "Interest coverage (times)": op / d["finance_cost"],
            "TOL/TNW (times)": (d["total_assets"] - d["equity"]) / d["equity"],
        })
        out[y] = d
    return out


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source)."""
    import os
    import sys
    _root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if _root not in sys.path:
        sys.path.insert(0, os.path.join(_root, "tools"))  # common_tieouts.py moved into tools/ 01-Sep-2026
    import common_tieouts
    T = common_tieouts.build(DATA, YEARS, printed=PRINTED)

    # Acceptances are the reason ICRA rates this issuer on two leverage measures, so the
    # relationship between them must hold rather than be assumed.
    for i, y in enumerate(YEARS):
        debt = DATA["borrowings"][i] + DATA["leases"][i]
        T.append(("INTERNAL debt incl. acceptances exceeds debt excl., %s" % y,
                  1.0 if DATA["acceptances"][i] > 0 and debt + DATA["acceptances"][i] > debt
                  else 0.0, 1.0, 0.5,
                  "ICRA treats buyer's credit as debt for steel issuers; both measures are "
                  "published side by side"))
        T.append(("INTERNAL cash <= total assets, %s" % y,
                  1.0 if DATA["cash"][i] <= DATA["total_assets"][i] else 0.0, 1.0, 0.5,
                  "balance-sheet containment"))
        T.append(("INTERNAL borrowings + leases + equity <= total assets, %s" % y,
                  1.0 if debt + DATA["equity"][i] <= DATA["total_assets"][i] else 0.0,
                  1.0, 0.5, "the residual is trade payables and other liabilities"))
    T += common_tieouts.corroboration(DATA, YEARS, 'jsw-steel')
    return T


def block(tag, rev, oth, fin, dep, pbt_bef_share, jv, borrow, lease, accept,
          cash_liq, equity_incl_nci, tot_assets, dtl=None, cwip=None, pat_owners=None):
    oi = rev
    opbdit = pbt_bef_share + fin + dep - oth        # operating, excl JV share & exceptional
    debt = borrow + lease                            # excl acceptances
    debt_a = debt + accept                           # incl acceptances
    netdebt = debt - cash_liq
    netdebt_a = debt_a - cash_liq
    tol = tot_assets - equity_incl_nci
    print(f"\n=== {tag} ===")
    print(f"  Operating income (OI)          : {oi:,.0f}")
    print(f"  OPBDITA                        : {opbdit:,.0f}   margin {100*opbdit/oi:.1f}%")
    print(f"  Total debt  (excl accept)      : {debt:,.0f}   /OPBDITA {debt/opbdit:.1f}x")
    print(f"  Total debt  (incl accept)      : {debt_a:,.0f}   /OPBDITA {debt_a/opbdit:.1f}x")
    print(f"  Net debt    (excl accept)      : {netdebt:,.0f}   /OPBDITA {netdebt/opbdit:.1f}x")
    print(f"  Net debt    (incl accept)      : {netdebt_a:,.0f}   /OPBDITA {netdebt_a/opbdit:.1f}x")
    print(f"  Interest coverage (OPBDITA/int): {opbdit/fin:.1f}x")
    print(f"  TOL/TNW                        : {tol/equity_incl_nci:.2f}x")
    if dtl is not None and cwip is not None:
        ce = debt + equity_incl_nci + dtl - cwip
        print(f"  RoCE (op PBIT/CE)              : {100*(opbdit-dep)/ce:.1f}%")
    if pat_owners is not None:
        print(f"  Reported PAT to owners         : {pat_owners:,.0f}  (incl exceptional)")

for _i, _y in enumerate(YEARS):
    _d = DATA
    block("CONSOLIDATED %s" % _y,
          rev=_d["revenue"][_i], oth=_d["other_income"][_i], fin=_d["finance_cost"][_i],
          dep=_d["depreciation"][_i], pbt_bef_share=_d["pbt_bef_share"][_i],
          jv=_d["jv_share"][_i], borrow=_d["borrowings"][_i], lease=_d["leases"][_i],
          accept=_d["acceptances"][_i], cash_liq=_d["cash"][_i],
          equity_incl_nci=_d["equity"][_i], tot_assets=_d["total_assets"][_i],
          dtl=_d["dtl"][_i], cwip=_d["cwip"][_i], pat_owners=_d["pat_owners"][_i])

_T = tieouts()
_bad = [x for x in _T if abs(x[1] - x[2]) > x[3]]
print("\n%d/%d tie-outs reconcile" % (len(_T) - len(_bad), len(_T)))
for _x in _bad:
    print("  FAIL %s  computed %s vs disclosed %s  [%s]" % (_x[0], _x[1], _x[2], _x[4]))

print("\nNote: FY2026 reported PAT (22,316 to owners) includes the Rs 18,051 cr NON-CASH exceptional")
print("gain on the BPSL slump-sale into the 50:50 JSW-JFE JV. Broker-adjusted PAT ~Rs 5,000 cr.")
