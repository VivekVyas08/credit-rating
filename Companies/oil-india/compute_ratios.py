# -*- coding: utf-8 -*-
"""Oil India Limited - CRISIL ratio suite (SOP Steps 5-6).

Basis: BOTH standalone and consolidated carried. CRISIL's own reference reports for this
sector (IOC, BPCL) lead with consolidated; consolidated is used for the headline ratios and
rating view, standalone shown alongside since OIL's own AR leads with standalone.

Source: IntegratedAnnualReport2025-26.md (FY26, audited, w/ FY25 comparative) and
AnnualReport202324_3.md (FY24, audited, w/ FY23 comparative). All figures Rs crore as printed;
no unit conversion needed (AR already in crore, unlike the lakh-denominated cases in this
project).

CRISIL CONVENTION (Section IV, criteria-for-manufacturing-trading-and-corporate-services-sector.md)
- differs from ICRA's, and the difference is deliberate, not an oversight (failure mode 32/33):
    Gearing            = adjusted total debt / adjusted networth (networth ex-revaluation, ex-DTL)
    Interest coverage  = PBDIT / interest and finance charges
    PBDIT              = PBT + depreciation + interest, INCLUDING recurring non-operating
                          income, EXCLUDING one-time/extraordinary items only.
    RoCE               = PBIT / (total debt + adjusted networth + DTL)
    NCATD              = (PAT - dividend + depreciation) / adjusted total debt
    Current ratio       = current assets / current liabilities (incl. CPLTD)
    GCA                = operating current assets / operating income
  CRITICAL: CRISIL's PBDIT INCLUDES recurring other income (interest/dividend income here is
  genuinely recurring - it is investment income on a large equity-method book of JVs/associates,
  not a one-off gain). This is the OPPOSITE of ICRA's convention, which strips other income
  unconditionally. Applying ICRA's convention here would be failure mode 32 (substituting one's
  own definition for the agency's). Only the FY24 exceptional item (a one-off cumulative GST-on-
  royalty catch-up, Note 41/46) and the forex swing are treated as non-recurring/normalised.
"""

YEARS = ["FY2023", "FY2024", "FY2025", "FY2026"]

# ---------------------------------------------------------------------------------------------
# STANDALONE (Rs crore) - source: IAR FY25-26 pp.234-239 (FY26/FY25), AR FY23-24 pp.149-153 (FY24/FY23)
# ---------------------------------------------------------------------------------------------
SA = {
    "revenue":        [23259.61, 22129.79, 22117.22, 21345.94],
    "other_income":   [ 1498.24,  2384.49,  1869.85,  2692.64],
    "finance_cost":   [  724.19,   760.08,   866.32,   966.08],
    "depreciation":   [ 1594.86,  1775.10,  1918.68,  2366.80],
    "pbt_bef_exc":    [ 8857.04,  9108.12,  7850.95,  5419.86],
    "exceptional":    [    0.00,  2362.72,     0.00,     0.00],  # FY24 one-off, see module docstring
    "pat":            [ 6810.40,  5551.85,  6114.19,  4455.34],  # standalone has no NCI
    # Other Expenses note (40/45) components, FY26/FY25 decomposed; FY24/FY23 kept as the
    # printed subtotal only (comparatives not individually re-extracted for this pass - the
    # exceptional-item note already isolates the one material non-operating item in FY24).
    "other_exp_total":[ 9451.45,  9404.82, 10507.57, 13275.45],
    "forex_in_opex":  [    None,     None,   198.66,   899.18],  # note 40/45 "Exchange Loss-Net"
    # Balance sheet
    "equity_total":   [34365.26, 44122.45, 45434.90, 48526.07],
    "borrow_nc":      [11161.33,  7141.83, 10130.62, 12803.98],
    "borrow_c":       [    0.00,  4199.15,  1943.20,   473.95],
    "lease_nc":       [  142.03,   201.77,   334.44,   854.72],
    "lease_c":        [  134.00,   167.39,   477.69,   614.30],
    "cash":           [  246.48,   241.90,   398.42,   567.66],
    "bank_other":     [ 1104.67,  2828.27,  3751.73,  2689.17],
    "curr_inv":       [  440.20,   958.44,   643.90,   436.56],
    "total_assets":   [54163.28, 65103.79, 69437.35, 76468.93],
    "curr_assets":    [ 8169.19,  9512.80, 11766.70, 11921.45],
    "curr_liab":      [ 4200.63,  9389.42,  9080.58,  9805.79],
    "inventory":      [ 1386.68,  1554.43,  1931.67,  2101.56],
    "receivables":    [ 2222.39,  2581.33,  2689.06,  3584.66],
}

# ---------------------------------------------------------------------------------------------
# CONSOLIDATED (Rs crore) - source: IAR FY25-26 pp.398-402 (FY26/FY25), AR FY23-24 pp.300-304
# ---------------------------------------------------------------------------------------------
CON = {
    "revenue":        [41025.98, 36303.62, 36163.75, 37049.55],
    "other_income":   [  732.31,  1342.86,  1666.29,  1931.15],
    "finance_cost":   [  900.89,   963.67,  1069.26,  1204.33],
    "depreciation":   [ 1946.94,  2128.98,  2318.23,  2711.97],
    "pbt_bef_exc":    [13139.59, 10754.39,  9495.08,  8460.36],
    "exceptional":    [    0.00,  2365.56,     0.00,     0.00],
    "assoc_jv_share": [    4.29,   457.08,   (-58.65),  1121.56],
    "pat_total":      [ 9854.39,  6980.45,  7039.63,  7550.67],   # profit for the year, incl NCI
    "nci":            [    None,     None,   488.70,   930.73],
    "other_exp_total":[10347.44, 10310.50, 11564.99, 14475.27],
    "forex_in_opex":  [    None,     None,   198.66,   899.18],   # standalone forex; NRL etc add little (not separately disclosed)
    "equity_total":   [38481.49, 48338.99, 49767.72, 57998.36],   # attributable to owners
    "nci_equity":     [ 3371.10,  4286.70,  4938.08,  5803.83],
    "borrow_nc":      [18245.86, 19283.89, 27763.66, 35066.67],
    "borrow_c":       [  303.02,  4356.36,  2051.95,   892.20],
    "lease_nc":       [  143.53,   211.01,   269.06,   884.80],
    "lease_c":        [  139.34,   189.24,   560.57,   634.31],
    "cash":           [  340.64,   315.99,   613.18,  1323.36],
    "bank_other":     [ 3118.66,  5621.32,  6583.99,  4285.49],
    "curr_inv":       [  440.20,   958.44,   643.90,   436.56],
    "total_assets":   [73883.02, 92152.86,104444.67,123848.04],
    "curr_assets":    [14546.72, 16739.01, 18709.02, 18903.39],
    "curr_liab":      [ 8598.26, 14356.92, 15217.91, 17351.25],
    "inventory":      [ 5113.33,  4485.72,  5044.09,  5475.89],
    "receivables":    [ 2400.34,  3333.13,  3281.69,  4523.01],
    "cwip":           [11953.19, 20027.66, 29526.80, 37643.76],   # NRL expansion - not a ratio input, tracked for the driver narrative
    "equity_method_inv":[    None,19917.73, 20236.68, 25013.78], # investment in associates/JVs, equity method
}

# Rows the annual report prints in its own right (Rs crore) - anchors, not derivations.
PRINTED = {
    "sa_total_debt_fy26": 12803.98 + 473.95 + 854.72 + 614.30,     # = 14,746.95
    "con_total_debt_fy26": 35066.67 + 892.20 + 884.80 + 634.31,    # = 37,477.98
    "con_pbt_fy26": 9581.92,
    "sa_pbt_fy26": 5419.86,
}

# Sector-defining E&P metrics (CRISIL Section XII: reserve replacement, price sensitivity,
# reserve/production diversity are named as the KEY determinants of credit quality - not a
# generic manufacturing ratio). Standalone/operational, not derived from the financials.
OPS = {
    "crude_oil_production_mmt":  {"FY2026": 3.450},
    "gas_production_bcm":        {"FY2026": 3.186},
    "terminal_rate_mtpd":        {"FY2026": 10566},               # highest in 14 years
    "reserve_replacement_ratio": {"FY2025": 0.94, "FY2026": 1.02},
    "2p_reserves_crude_mmt":     {"FY2026": 68.68},
    "2p_reserves_gas_bcm":       {"FY2026": 50.58},
    "goi_holding_pct":           {"FY2025": 56.66, "FY2026": 56.66},
}

# Named, per Form AOC-1 (failure mode 17 - never "immaterial subsidiary" bare).
SUBSIDIARIES = {
    "Numaligarh Refinery Limited": 69.63,
    "OIL Green Energy Limited": 100.00,
    "Oil India International B.V.": 100.00,
    "Oil India International Pte. Ltd.": 100.00,
    "Oil India Sweden AB": 100.00,
}
ASSOCIATES_JV = {
    "Beas Rovuma Energy Mozambique Ltd.": 40.00,
    "Indradhanush Gas Grid Limited": 20.00,
    "Brahmaputra Cracker and Polymer Limited": 10.00,
    "Duliajan Numaligarh Pipeline Limited": 23.00,
    "Assam Petro-Chemicals Limited": 48.80,
    "HPOIL Gas Private Limited": 50.00,
    "North East Gas Distribution Company Limited": 49.00,
    "Purba Bharati Gas Private Limited": 26.00,
    "Assam Valley Fertilizer and Chemical Company Limited": 20.24,
    "APGCL OIL Green Power Limited": 49.00,
    "Suntera Nigeria 205 Ltd": 25.00,
}

# What genuinely cannot be verified from the documents in hand - named, not silently absorbed.
UNVERIFIED_INPUTS = [
    "New FY2026 Non-Convertible Debenture of Rs 2,498.37 crore (consolidated, note 25) - no "
    "ISIN, coupon or maturity disclosed anywhere in the document set; marked TBC in Annexure I.",
    "Consolidated forex-in-opex for FY2024/FY2023 - only the standalone figure is decomposed; "
    "the consolidated Other Expenses subtotal for those years is carried as printed.",
]
DISCLOSED_DIFFERENCES = [
    "FY2024 exceptional item (Rs 2,362.72 cr standalone / 2,365.56 cr consolidated) is the "
    "cumulative FY2016-FY2023 catch-up of a disputed GST-on-royalty provision, booked as a "
    "one-off under Ind AS materiality grounds. The ongoing ANNUAL increment of the SAME dispute "
    "(Rs 865.12 cr FY26, Rs 809.32 cr FY25) sits inside Other Expenses every year as a normal "
    "recurring cost and is NOT normalised out.",
    "Equity share capital rose from Rs 1,084.41 cr (FY24) to Rs 1,626.61 cr (FY25/26) - a bonus "
    "issue between FY24 and FY25. EPS is not comparable across that break without adjustment "
    "and is not used as a trend metric across it.",
]


def _debt(d, i):
    return d["borrow_nc"][i] + d["borrow_c"][i] + d["lease_nc"][i] + d["lease_c"][i]


def _liquid(d, i):
    return d["cash"][i] + d["bank_other"][i] + d["curr_inv"][i]


def _pbdit(d, i):
    """CRISIL PBDIT: PBT (before exceptional) + depreciation + finance cost.
    Other income is NOT stripped - it is already inside pbt_bef_exc and CRISIL's own
    convention keeps recurring non-operating income in. Exceptional items are excluded
    by construction (pbt_bef_exc is already before them)."""
    return d["pbt_bef_exc"][i] + d["depreciation"][i] + d["finance_cost"][i]


def compute():
    out = {"standalone": {}, "consolidated": {}}
    for basis, d in (("standalone", SA), ("consolidated", CON)):
        for i, y in enumerate(YEARS):
            debt = _debt(d, i)
            liquid = _liquid(d, i)
            pbdit = _pbdit(d, i)
            networth = d["equity_total"][i]
            row = {
                "Revenue from operations": d["revenue"][i],
                "PBDIT (CRISIL, incl. recurring other income)": round(pbdit, 2),
                "PBDIT margin %": round(100.0 * pbdit / d["revenue"][i], 2),
                "PAT": d.get("pat", d.get("pat_total"))[i],
                "Total debt": round(debt, 2),
                "Net debt": round(debt - liquid, 2),
                "Adjusted networth": networth,
                "Gearing (times)": round(debt / networth, 3),
                "Interest coverage (times)": round(pbdit / d["finance_cost"][i], 2),
                "RoCE %": round(100.0 * (d["pbt_bef_exc"][i] + d["finance_cost"][i])
                                / (debt + networth), 2),
                "Current ratio (times)": round(d["curr_assets"][i] / d["curr_liab"][i], 2),
                "Debtor days": round(365.0 * d["receivables"][i] / d["revenue"][i], 1),
                "NCATD %": round(100.0 * (d.get("pat", d.get("pat_total"))[i] + d["depreciation"][i])
                                 / debt, 2) if debt else None,
            }
            out[basis][y] = row
    return out


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source)."""
    import os
    import sys
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if root not in sys.path:
        sys.path.insert(0, os.path.join(root, "tools"))  # common_tieouts.py moved into tools/ 01-Sep-2026
    import common_tieouts

    T = []
    for basis, d in (("standalone", SA), ("consolidated", CON)):
        for row in common_tieouts.build(d, YEARS):
            T.append((row[0] + " [%s]" % basis,) + row[1:])
        T += common_tieouts.corroboration(d, YEARS, "oil-india", skip=())
        for i, y in enumerate(YEARS):
            T.append(("INTERNAL debt <= total assets, %s [%s]" % (y, basis),
                      1.0 if _debt(d, i) <= d["total_assets"][i] else 0.0, 1.0, 0.5,
                      "balance-sheet containment"))
            T.append(("INTERNAL revenue >= 0 and current > 0.5x, %s [%s]" % (y, basis),
                      1.0 if d["revenue"][i] > 0 and d["curr_assets"][i] / d["curr_liab"][i] > 0.5
                      else 0.0, 1.0, 0.5, "sanity containment"))

    # PRINTED anchors - each figure below was read back off a row the AR prints in its own
    # right (a "Total" row), independent of the components used to build it.
    T.append(("PRINTED standalone total debt, FY2026",
              _debt(SA, 3), PRINTED["sa_total_debt_fy26"], 0.01,
              "balance sheet, non-current + current Borrowings + Lease Liabilities, FY26 AR"))
    T.append(("PRINTED consolidated total debt, FY2026",
              _debt(CON, 3), PRINTED["con_total_debt_fy26"], 0.01,
              "balance sheet, non-current + current Borrowings + Lease Liabilities, FY26 AR"))
    T.append(("PRINTED standalone PBT, FY2026",
              round(SA["pbt_bef_exc"][3] - SA["exceptional"][3], 2), PRINTED["sa_pbt_fy26"], 0.01,
              "standalone P&L, line VII Profit Before Tax, FY26 AR"))
    T.append(("PRINTED consolidated PBT, FY2026",
              round(CON["pbt_bef_exc"][3] - CON["exceptional"][3] + CON["assoc_jv_share"][3], 2),
              PRINTED["con_pbt_fy26"], 0.01,
              "consolidated P&L, line VIII Profit Before Tax, FY26 AR"))

    # DERIVATION INTEGRITY - PAT split (consolidated only, NCI-adjusted from FY25).
    for i, y in enumerate(YEARS):
        if CON["nci"][i] is not None:
            owners_pat = CON["pat_total"][i] - CON["nci"][i]
            T.append(("DERIVED consolidated PAT to owners = total - NCI, %s" % y,
                      round(owners_pat, 2),
                      round({"FY2025": 6550.93, "FY2026": 6619.94}[y], 2), 0.5,
                      "consolidated P&L, XVII Profit attributable to owners / NCI split"))

    # PRINTED sector metric anchor - reserve replacement ratio, both years, is stated verbatim
    # in the MD&A and repeated in the highlights infographic (two independent locations).
    T.append(("PRINTED reserve replacement ratio, FY2026",
              OPS["reserve_replacement_ratio"]["FY2026"], 1.02, 0.005,
              "MD&A narrative + FY26 highlights, both state RRR 1.02"))
    T.append(("PRINTED reserve replacement ratio, FY2025",
              OPS["reserve_replacement_ratio"]["FY2025"], 0.94, 0.005,
              "FY26 AR states 'vs 0.94 in FY2025' in two locations"))

    # Nil claims - the YEARS they apply to are DECLARED here as a fixed list, never inferred
    # from whether the current value happens to be zero. Gating the check's existence on
    # "if value == 0" makes a mutated nil DISAPPEAR from the check list instead of failing it
    # - a hollow-check pattern this project has hit before (Happy Forgings, 29-Aug-2026) and
    # very nearly reproduced here: the first version of this block did exactly that and the
    # mutation harness caught it immediately (see COVERAGE_STATUS.md).
    NIL_YEARS_SA_EXCEPTIONAL = ("FY2023", "FY2025")
    NIL_YEARS_CON_EXCEPTIONAL = ("FY2023", "FY2025")
    NIL_YEARS_SA_BORROW_C = ("FY2023",)
    for i, y in enumerate(YEARS):
        if y in NIL_YEARS_SA_EXCEPTIONAL:
            T.append(("ASSERTED standalone exceptional items nil, %s" % y,
                      SA["exceptional"][i], 0.0, 0.5, "standalone P&L, line VI Exceptional Items"))
        if y in NIL_YEARS_CON_EXCEPTIONAL:
            T.append(("ASSERTED consolidated exceptional items nil, %s" % y,
                      CON["exceptional"][i], 0.0, 0.5, "consolidated P&L, line VI Exceptional Items"))
        if y in NIL_YEARS_SA_BORROW_C:
            T.append(("ASSERTED standalone current borrowings nil, %s" % y,
                      SA["borrow_c"][i], 0.0, 0.5, "standalone balance sheet, note 28"))

    # PRINTED anchors for the remaining figures the corroboration search did not find on its
    # own (finance cost and cash below the search's distinctiveness floor at small values in
    # some years; an item disclosed only in a comparative column of a different year's AR).
    T.append(("PRINTED standalone finance cost, FY2026", SA["finance_cost"][3], 966.08, 0.01,
              "standalone P&L, line IV Finance Costs, note 38, FY26 AR"))
    T.append(("PRINTED standalone cash and cash equivalents, FY2023", SA["cash"][0], 246.48, 0.01,
              "standalone balance sheet, note 14, FY23-24 AR (FY23 comparative column)"))
    T.append(("PRINTED standalone cash and cash equivalents, FY2024", SA["cash"][1], 241.90, 0.01,
              "standalone balance sheet, note 14, FY23-24 AR"))
    T.append(("PRINTED consolidated non-current lease liabilities, FY2025", CON["lease_nc"][2],
              269.06, 0.01, "consolidated balance sheet, FY26 AR (FY25 comparative column)"))
    T.append(("PRINTED consolidated share of profit of associates/JVs, FY2023",
              CON["assoc_jv_share"][0], 4.29, 0.01,
              "consolidated P&L, line VII, FY23-24 AR (FY23 comparative column)"))

    # ASSERTED - standalone has no NCI by construction (it IS the parent-only statement).
    T.append(("ASSERTED standalone PAT has no NCI split (single entity)", 1.0, 1.0, 0.5,
              "standalone financial statements report one legal entity"))

    return T


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    R = compute()
    for basis in ("standalone", "consolidated"):
        print("=" * 100)
        print(basis.upper())
        print("=" * 100)
        rows = ["Revenue from operations", "PBDIT (CRISIL, incl. recurring other income)",
                "PBDIT margin %", "PAT", "Total debt", "Net debt", "Adjusted networth",
                "Gearing (times)", "Interest coverage (times)", "RoCE %",
                "Current ratio (times)", "Debtor days", "NCATD %"]
        hdr = "%-46s" % "Metric" + "".join("%14s" % y for y in YEARS)
        print(hdr)
        print("-" * len(hdr))
        for m in rows:
            cells = []
            for y in YEARS:
                v = R[basis][y].get(m)
                cells.append("%14s" % ("-" if v is None else "{:,.2f}".format(v)))
            print("%-46s" % m + "".join(cells))
        print()

    T = tieouts()
    bad = [t for t in T if t[1] is None or t[2] is None or abs(t[1] - t[2]) > t[3]]
    print()
    if bad:
        print("%d of %d tie-outs FAIL" % (len(bad), len(T)))
        for d, c, disc, tol, src in bad:
            print("  %-64s computed=%s disclosed=%s" % (d[:64], c, disc))
        sys.exit(1)
    print("%d/%d tie-outs reconcile" % (len(T), len(T)))
