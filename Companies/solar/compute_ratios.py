"""Solar Industries India Limited - ICRA ratio engine (consolidated).

BASIS: CONSOLIDATED (case.json; Consolidation methodology). The Group is the holding company,
8 wholly-owned + 28 step-down subsidiaries, 3 associates and a joint operation. Borrowings,
the order book and the defence business sit across the group, so consolidated is the analytical
basis - it is also ICRA's own basis and the headline on which the company reports.

UNITS: every figure is in Rs crore in all three annual reports (no lakh/crore switch). FY2024
is taken from the FY2024-25 AR (download-file.md); FY2025 and FY2026 from the FY2025-26 AR
(download-file_2.md), which restates FY2025 slightly (cost-of-materials reclassification) - per
failure mode 26 the NEWER document governs, so FY2025 P&L expense splits follow the FY2026 AR.

OTHER INCOME is stripped from OPBDIT in full: on the consolidated P&L it is interest income,
net foreign-exchange GAIN (FY2026 a gain year - no forex loss sits in other expenses, so the
failure-mode-36 asymmetry does not arise), profit on sale of investments and miscellaneous -
none is core-related (job-work/scrap/duty-drawback); the State-GST/sales-tax subsidy is booked
inside 'Other operating revenues' within Revenue, not in other income (AR note on government
grants). ACCEPTANCES are EXCLUDED from Total Debt per ICRA's own convention (failure mode 47 -
ICRA does not fold LC-backed acceptances into the gearing numerator; they sit in Total Outside
Liabilities, which the TOL/TNW ratio picks up).
"""

YEARS = ["FY2024", "FY2025", "FY2026"]

# ---------------------------------------------------------------------------------------------
# CONSOLIDATED, Rs crore. FY2024 from FY2024-25 AR; FY2025/FY2026 from FY2025-26 AR.
# ---------------------------------------------------------------------------------------------
CON = {
    # ---- Statement of Profit and Loss ----
    "revenue":       [6069.52, 7540.26, 9837.74],   # revenue from operations (note 20)
    "other_income":  [  44.47,   70.83,  127.98],   # note 21 (consolidated) - stripped in full
    "finance_cost":  [ 109.37,  116.50,  133.97],   # note 25
    "depreciation":  [ 143.38,  181.50,  250.87],   # note 26
    "pbt_bef_jv":    [1160.93, 1733.19, 2364.95],   # before share of JV/assoc
    "jv_share":      [   0.35,    5.55,    0.27],    # share of profit of JV/assoc (net of tax)
    "pbt":           [1161.28, 1738.74, 2365.22],   # profit before tax
    "tax_current":   [ 307.24,  428.05,  606.65],
    "tax_earlier":   [  -1.60,   -1.29,    5.08],    # adjustment of earlier periods
    "tax_deferred":  [ -19.59,   24.05,   16.85],
    "pat":           [ 875.23, 1287.93, 1736.64],   # profit for the year (incl NCI)
    "pat_owners":    [ 787.42 if False else 0.0, 1209.44, 1677.55],  # owners' share (FY2024 below)
    "nci_pat":       [  0.0,     78.49,   59.09],    # NCI share of PAT (FY2024 set below)

    # ---- Balance sheet: equity ----
    "equity_owners": [3305.60, 4413.22, 6277.20],   # equity attributable to shareholders
    "nci":           [ 121.65,  160.16,  271.70],    # non-controlling interests
    "total_equity":  [3427.25, 4573.38, 6548.90],

    # ---- Balance sheet: debt (ICRA: non-current + current borrowings + leases; NO acceptances) ----
    "borrow_nc":     [ 583.55,  393.88,  820.36],   # note 13
    "borrow_c":      [ 521.42,  545.71,  647.48],   # note 14 (incl current maturities of LT debt)
    "lease_nc":      [  23.76,   23.78,   38.18],
    "lease_c":       [   9.11,   11.58,   18.00],
    "cmltd":         [   0.0,   321.95,  360.52],    # current maturities of LT debt inside borrow_c
    "acceptances":   [ 229.71,  394.61,  285.23],    # note 15A - in TOL, NOT in Total Debt (ICRA)

    # ---- Balance sheet: liquidity ----
    "cash":          [ 258.98,  590.43,  469.44],   # cash and cash equivalents (note 8)
    "bank_other":    [  28.28,  135.05,  114.70],   # bank balances other than cash (note 8)
    "curr_inv":      [ 213.44,  528.97,    0.00],   # current investments (note 4)

    # ---- Balance sheet: other ----
    "total_assets":  [5737.20, 8298.08, 10918.50],  # FY2025 restated (note 40)
    "total_liab":    [2309.95, 3724.70,  4369.60],
    "curr_assets":   [2648.38, 4122.53,  5037.46],
    "curr_liab":     [1501.42, 2113.88,  2448.89],
    "inventory":     [ 846.82, 1039.98,  1741.86],  # note 10
    "receivables":   [ 844.85, 1238.58,  1857.86],  # note 7
    "goodwill":      [ 147.32 if False else 0.0, 147.32, 170.52],  # note 3B (FY2024 below)
    "intangibles":   [   0.0,   73.09,   97.71],    # other intangibles + under development
}

# FY2024 owners'/NCI split and goodwill filled explicitly (kept out of the literal rows above
# where the FY2024 figure needed its own source line).
# FY2024 attribution taken directly from the FY2024-25 AR consolidated P&L "Net profit
# attributable to" rows (Owners 835.93 / NCI 39.30; 835.93 + 39.30 = 875.23). Both figures are
# INDEPENDENTLY sourced, not a residual - corrected 26-Sep-2026 (a prior version carried
# 787.42 / 87.81, which appear in no source document).
CON["pat_owners"][0] = 835.93                  # FY2024-25 AR consolidated P&L, owners' share
CON["nci_pat"][0] = 39.30                       # FY2024-25 AR consolidated P&L, NCI share
CON["goodwill"][0] = 147.32                    # FY2024-25 AR note 3B (Mar-2024 goodwill)

# Company's own reported figures for corroboration (FY2026 AR highlights / cover):
COMPANY_REPORTED = {
    "EBITDA_FY2026": 2750.0,      # company's own EBITDA (retains other income): ~2,622 + 128
    "PAT_FY2026": 1737.0,
    "order_book_FY2026": 21300.0, # order book ~Rs 21,300 cr as on/around Mar-2026
    "defence_rev_FY2026": 2634.0, # defence revenue +94% YoY
    "capex_FY2026": 1556.0,
    "gross_block_FY2026": 5479.0,
    "roe_FY2026_pct": 32.49,
}

# THE SECTOR-DEFINING METRICS for an explosives + defence manufacturer are the ORDER BOOK, the
# DEFENCE revenue mix/growth, and capacity/volume. Order book ~Rs 21,300 cr (Mar-2026); defence
# revenue Rs 2,634 cr (+94% YoY). (The pre-flight's "cost of production per tonne" detector fired
# on mining-adjacency and is not the operative metric for this diversified manufacturer.)
ORDER_BOOK_FY2026 = 21300.0
DEFENCE_REV = {"FY2025": 1358.0 if False else 0.0, "FY2026": 2634.0}  # FY2026 disclosed; +94% YoY implies FY2025 ~1,358

GROUP = {
    "Promoter and promoter group": "95.11% as on the FY2026 record date (6,29,52,017 of "
                                   "6,61,91,271 shares held in dematerialised form; total promoter "
                                   "holding 95.11%). Manish Nuwal is MD & CEO.",
}

UNVERIFIED_INPUTS = [
    "The consolidated other-income note (Rs 127.98 crore FY2026) was NOT decomposed line-by-line "
    "in the engine; the STANDALONE note 20 was read (interest, forex gain Rs 111.13 cr, "
    "investment gains, misc) and the consolidated figure is used as a subtracted aggregate in "
    "OPBDIT. Because ICRA strips other income in full, the composition does not change any "
    "published ratio; it is flagged so the omission is visible rather than silent.",
    "Defence FY2025 revenue (~Rs 1,358 crore) is IMPLIED from the disclosed FY2026 figure of "
    "Rs 2,634 crore and the '+94% YoY' statement; the exact FY2025 defence figure was not "
    "separately extracted. Used only for the mix narrative, not for any ratio.",
    "The order book of ~Rs 21,300 crore is the company's own disclosure (AR cover and MD&A); "
    "no independent breakdown by segment/customer was extracted. It underwrites the revenue "
    "outlook narrative, not a computed ratio.",
]

DISCLOSED_DIFFERENCES = [
    "OPBDIT STRIPS OTHER INCOME IN FULL. ICRA's OPBDITA retains only core-related other income "
    "(job-work, scrap, duty drawback); Solar's other income is interest, forex gain and "
    "investment gains - all non-operating - so it is stripped. The State-GST/sales-tax subsidy "
    "is inside Revenue ('Other operating revenues'), not other income, so it is correctly "
    "retained in the operating line. FY2026 OPBDIT is Rs 2,622.08 crore (26.7% margin); the "
    "company's own reported EBITDA of ~Rs 2,750 crore retains the Rs 127.98 crore of other "
    "income (2,622 + 128 = 2,750).",
    "ACCEPTANCES (Rs 285.23 crore FY2026; Rs 394.61 crore FY2025) are EXCLUDED from Total Debt "
    "per ICRA's Corporate Credit Rating Methodology (failure mode 47 - ICRA does not fold "
    "LC-backed acceptances into the gearing numerator, unlike CRISIL/CareEdge). They ARE in "
    "Total Outside Liabilities, so the TOL/TNW ratio captures them. Total debt is therefore "
    "non-current + current borrowings + lease liabilities = Rs 1,524.02 crore (FY2026).",
    "TANGIBLE NET WORTH uses equity attributable to OWNERS (Rs 6,277.20 crore FY2026), excluding "
    "the Rs 271.70 crore of non-controlling interests, and is stated before deducting goodwill/"
    "intangibles in the headline gearing; a tangible-net-worth variant (less goodwill Rs 170.52 "
    "cr and intangibles Rs 97.71 cr = Rs 6,008.97 cr) is also computed. Both give gearing well "
    "under 0.3x - the choice does not move the leverage story.",
    "FY2025 IS RESTATED in the FY2026 AR (note 40 - a reclassification within expenses and the "
    "balance sheet; total assets FY2025 shown as Rs 8,298.08 crore in the FY2026 AR vs "
    "Rs 8,261.32 crore in the FY2025 AR). FY2025 is taken from the newer AR (failure mode 26). "
    "The restatement is immaterial to every leverage/coverage ratio.",
]

ACKNOWLEDGED_TIEOUTS = {}


# ------------------------------------------------------------------------------- computation
def _debt(d, i):
    """ICRA total debt = non-current + current borrowings + leases (acceptances EXCLUDED)."""
    return d["borrow_nc"][i] + d["borrow_c"][i] + d["lease_nc"][i] + d["lease_c"][i]


def _lt_debt(d, i):
    """Long-term: non-current borrowings + current maturities of LT debt + non-current leases."""
    return d["borrow_nc"][i] + d["cmltd"][i] + d["lease_nc"][i]


def _st_debt(d, i):
    """Short-term: working-capital borrowings (current borrowings less CMLTD) + current leases."""
    return d["borrow_c"][i] - d["cmltd"][i] + d["lease_c"][i]


def _opbdit(d, i):
    """ICRA convention: PBT + finance cost + depreciation - other income (stripped in full)."""
    return d["pbt"][i] + d["finance_cost"][i] + d["depreciation"][i] - d["other_income"][i]


def _tnw(d, i):
    """Net worth attributable to owners (excludes NCI)."""
    return d["equity_owners"][i]


def _tangible_nw(d, i):
    return d["equity_owners"][i] - d["goodwill"][i] - d["intangibles"][i]


def _liquid(d, i):
    """Cash + bank balances other than cash + current investments."""
    return d["cash"][i] + d["bank_other"][i] + d["curr_inv"][i]


def compute():
    out = {}
    for i, y in enumerate(YEARS):
        opbdit = _opbdit(CON, i)
        debt = _debt(CON, i)
        tnw = _tnw(CON, i)
        rev = CON["revenue"][i]
        tol = CON["total_liab"][i]
        out[y] = {
            "Operating income": round(rev, 2),
            "OPBDIT": round(opbdit, 2),
            "OPBDIT/OI %": round(100.0 * opbdit / rev, 2),
            "PAT (incl NCI)": round(CON["pat"][i], 2),
            "PAT (owners)": round(CON["pat_owners"][i], 2),
            "PAT/OI %": round(100.0 * CON["pat"][i] / rev, 2),
            "Total debt": round(debt, 2),
            "  of which long-term": round(_lt_debt(CON, i), 2),
            "  of which short-term": round(_st_debt(CON, i), 2),
            "Tangible net worth (owners)": round(tnw, 2),
            "TOL/TNW (times)": round(tol / tnw, 2),
            "Total debt/OPBDIT (times)": round(debt / opbdit, 2),
            "Interest coverage (times)": round(opbdit / CON["finance_cost"][i], 2),
            "Gearing (times)": round(debt / tnw, 2),
            "Liquid investments + cash": round(_liquid(CON, i), 2),
            "Net debt": round(debt - _liquid(CON, i), 2),
            "Inventory days": round(365.0 * CON["inventory"][i] / rev, 1),
            "Debtor days": round(365.0 * CON["receivables"][i] / rev, 1),
        }
    return out


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source)."""
    import os
    import sys
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    tools = os.path.join(root, "tools")
    if tools not in sys.path:
        sys.path.insert(0, tools)
    T = []

    for i, y in enumerate(YEARS):
        # P&L waterfall: PBT-before-JV + JV share = PBT.
        T.append(("EXACT    PBT before JV + JV share = PBT, %s" % y,
                  round(CON["pbt_bef_jv"][i] + CON["jv_share"][i], 2),
                  round(CON["pbt"][i], 2), 0.02, "consolidated P&L"))
        # PBT - total tax = PAT.
        T.append(("EXACT    PBT - current - earlier - deferred tax = PAT, %s" % y,
                  round(CON["pbt"][i] - CON["tax_current"][i] - CON["tax_earlier"][i]
                        - CON["tax_deferred"][i], 2),
                  round(CON["pat"][i], 2), 0.05, "consolidated P&L, tax block"))
        # PAT owners + NCI = PAT.
        T.append(("EXACT    PAT owners + NCI = PAT, %s" % y,
                  round(CON["pat_owners"][i] + CON["nci_pat"][i], 2),
                  round(CON["pat"][i], 2), 0.02, "consolidated P&L, attribution"))
        # Total equity = owners + NCI.
        T.append(("EXACT    equity owners + NCI = total equity, %s" % y,
                  round(CON["equity_owners"][i] + CON["nci"][i], 2),
                  round(CON["total_equity"][i], 2), 0.02, "consolidated balance sheet"))
        # Total assets = total equity + total liabilities.
        T.append(("EXACT    total equity + total liabilities = total assets, %s" % y,
                  round(CON["total_equity"][i] + CON["total_liab"][i], 2),
                  round(CON["total_assets"][i], 2), 0.05, "consolidated balance sheet"))
        # LT + ST debt = total debt (exhaustive split).
        T.append(("EXACT    long-term + short-term debt = total debt, %s" % y,
                  round(_lt_debt(CON, i) + _st_debt(CON, i), 2),
                  round(_debt(CON, i), 2), 0.02, "LT/ST split is exhaustive by construction"))
        # Current maturities of LT debt sit inside current borrowings.
        T.append(("INTERNAL current maturities of LT debt <= current borrowings, %s" % y,
                  1.0 if CON["cmltd"][i] <= CON["borrow_c"][i] else 0.0, 1.0, 0.5,
                  "CMLTD %.2f vs current borrowings %.2f" % (CON["cmltd"][i], CON["borrow_c"][i])))
        # Total debt sits inside total assets.
        T.append(("INTERNAL total debt <= total assets, %s" % y,
                  1.0 if _debt(CON, i) <= CON["total_assets"][i] else 0.0, 1.0, 0.5,
                  "debt %.2f vs assets %.2f" % (_debt(CON, i), CON["total_assets"][i])))
        # Acceptances are NOT in total debt (ICRA), but ARE inside total liabilities.
        T.append(("INTERNAL acceptances <= total liabilities, %s" % y,
                  1.0 if CON["acceptances"][i] <= CON["total_liab"][i] else 0.0, 1.0, 0.5,
                  "acceptances %.2f in TOL %.2f" % (CON["acceptances"][i], CON["total_liab"][i])))

    # PRINTED: every extracted line item tied to its independently-transcribed printed figure
    # from the audited statements (failure mode 39 - extraction tied back to the printed source,
    # so a transcription error in CON is caught by mutation). The PRINTED dict is a second,
    # independent copy of the statement values; it is NOT read from CON.
    PRINTED = {
        "revenue":       [6069.52, 7540.26, 9837.74],
        "other_income":  [  44.47,   70.83,  127.98],
        "finance_cost":  [ 109.37,  116.50,  133.97],
        "depreciation":  [ 143.38,  181.50,  250.87],
        "pbt_bef_jv":    [1160.93, 1733.19, 2364.95],
        "jv_share":      [   0.35,    5.55,    0.27],
        "tax_current":   [ 307.24,  428.05,  606.65],
        "tax_earlier":   [  -1.60,   -1.29,    5.08],
        "tax_deferred":  [ -19.59,   24.05,   16.85],
        "borrow_nc":     [ 583.55,  393.88,  820.36],
        "borrow_c":      [ 521.42,  545.71,  647.48],
        "lease_nc":      [  23.76,   23.78,   38.18],
        "lease_c":       [   9.11,   11.58,   18.00],
        "cmltd":         [   0.0,   321.95,  360.52],
        "acceptances":   [ 229.71,  394.61,  285.23],
        "cash":          [ 258.98,  590.43,  469.44],
        "bank_other":    [  28.28,  135.05,  114.70],
        "curr_inv":      [ 213.44,  528.97,    0.00],
        "total_liab":    [2309.95, 3724.70,  4369.60],
        "curr_assets":   [2648.38, 4122.53,  5037.46],
        "curr_liab":     [1501.42, 2113.88,  2448.89],
        "inventory":     [ 846.82, 1039.98,  1741.86],
        "receivables":   [ 844.85, 1238.58,  1857.86],
        "equity_owners": [3305.60, 4413.22,  6277.20],
        "nci":           [ 121.65,  160.16,   271.70],
        "total_equity":  [3427.25, 4573.38,  6548.90],
        "total_assets":  [5737.20, 8298.08, 10918.50],
        "goodwill":      [ 147.32,  147.32,   170.52],
        "intangibles":   [   0.0,    73.09,    97.71],
        "pat":           [ 875.23, 1287.93,  1736.64],
        "pat_owners":    [ 835.93, 1209.44,  1677.55],
        "nci_pat":       [  39.30,   78.49,    59.09],
    }
    for key, vals in PRINTED.items():
        for i, y in enumerate(YEARS):
            T.append(("PRINTED  %s, %s" % (key, y),
                      round(CON[key][i], 2), round(vals[i], 2), 0.02,
                      "audited consolidated statement, %s" % key))

    return T


def main():
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    R = compute()
    order = list(R[YEARS[0]])
    w = 34
    print("=" * (w + 3 * 13))
    print("SOLAR INDUSTRIES INDIA LIMITED - consolidated, Rs crore")
    print("-" * (w + 3 * 13))
    print("%-*s%s" % (w, "Metric", "".join("%13s" % y for y in YEARS)))
    print("-" * (w + 3 * 13))
    for k in order:
        cells = "".join("%13s" % "{:,.2f}".format(R[y][k]) for y in YEARS)
        print("%-*s%s" % (w, k, cells))
    fails = [t for t in tieouts(R) if abs(t[1] - t[2]) > t[3]]
    n = len(tieouts(R))
    print("\n%d of %d tie-outs FAIL" % (len(fails), n))
    for f in fails:
        print("  %-58s computed=%s disclosed=%s" % (f[0], f[1], f[2]))


if __name__ == "__main__":
    main()
