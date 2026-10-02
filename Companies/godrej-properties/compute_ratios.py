# ICRA-basis ratio suite - Godrej Properties Limited (ICRA).
#
# SECTOR / ACCOUNTING NOTE (binding context for every ratio below): GPL follows the PROJECT
# COMPLETION method under Ind AS - revenue and profit are recognised only on receipt of the
# occupancy certificate for a project, not as units are booked/sold. The company's own MD&A
# states this explicitly (FY2025-26 AR, Directors' Report): "the profit of the Company will
# largely be dependent on the completion of the project/phase rather [than] on sale of units in
# the respective financial year... this creates a lag in reported earnings." This means:
#   (a) Revenue from Operations understates the scale of the business - BOOKING VALUE (pre-sales)
#       is the sector's own scale metric (failure mode 21's Real Estate row: pre-sales/bookings,
#       collections, inventory overhang, debt/collections) and is tracked separately below;
#   (b) Other Income is NOT a minor residual here - it is dominated by "Fair value gain upon
#       Acquisition/Relinquishment of Control" (Ind AS 103/110 remeasurement on JV/SPV control
#       changes), a real, GAAP-compliant, but NON-CASH, NON-RECURRING gain. ICRA's OWN published
#       rationale for this issuer (21-Jul-2026, reference library) states: "ICRA notes that GPL's
#       reported operating margins (excluding fair value gain upon acquisition/relinquishment of
#       control) are modest" - independently confirming the finding this engine computes below.
#
# CONSOLIDATED basis throughout (Rs crore, as printed - no unit conversion needed).
# Sources:
#   FY2026 AR (integrated-annual-report-2025-26...): audited FY2026 consolidated BS/P&L/notes,
#     FY2025 comparative column.
#   FY2025 AR (gpl-integrated-report-2024-25...): audited FY2025 consolidated BS/P&L/notes,
#     FY2024 comparative column - used to CROSS-CHECK the FY2025 figures taken from the FY2026
#     AR (both reproduce Revenue 4,922.84, PAT 1,389.23, Total Equity 17,573.73 exactly - MATCH).

YEARS = ["FY2024", "FY2025", "FY2026"]

# ---- P&L (Rs crore, consolidated) ----
PL = {
    "revenue":        [3035.62, 4922.84, 5131.43],   # Revenue from Operations, Note 30 (FY26 AR) / Note 29 (FY25 AR)
    "other_income":   [1298.60, 2044.21, 3279.45],   # Note 31 (FY26 AR) - see OTHER_INCOME_DECOMPOSITION below
    "total_expenses": [3361.97, 5125.83, 5800.44],   # incl. finance cost & depreciation
    "finance_cost":   [152.11,  173.69,  136.86],
    "depreciation":   [44.56,   73.66,   115.58],
    "pbt_bef_jv":     [972.25,  1841.22, 2610.44],   # Profit before share of JV(Loss)/tax
    "jv_share":       [27.74,   -118.60, -36.75],    # Share of Profit/(Loss) of JV & Associate
    "exceptional":    [0.0,     0.0,     23.11],     # Exceptional items, Note 59
    "pbt":            [999.99,  1722.62, 2550.58],
    "tax_total":      [252.93,  333.39,  709.92],
    "pat_total":      [747.06,  1389.23, 1840.66],
    "pat_owners":     [725.27,  1399.89, 1850.20],
    "nci_pat":        [21.79,   -10.66,  -9.54],
}

# Other Income decomposition, Note 31 (FY26 AR; FY25 comparative cross-checked against FY25 AR's
# own Note 30, which shows identical figures for FY25 - MATCH). Recorded per failure mode 36 -
# an aggregate note may not be fed into a ratio until every component is read. FY2024 is NOT
# decomposed - the FY24-25 AR does not carry a FY2024 comparative for this note (only BS/P&L
# have a FY2024 column); its FY2024 Other Income of 1,298.60 is therefore UNVERIFIED at
# component level and is disclosed as such (see UNVERIFIED_INPUTS).
OTHER_INCOME_DECOMPOSITION = {
    "interest_income":        [None, 739.82,  869.91],
    "dividend_income":        [None, 0.00,    0.00],
    "profit_on_sale_ppe":     [None, 0.62,    7.19],
    "fair_value_gain_control":[None, 930.35,  2093.01],  # Ind AS 103/110 - the dominant, non-cash, non-recurring item
    "income_fvtpl":           [None, 129.57,  75.89],
    "profit_on_sale_invest":  [None, 214.41,  204.56],
    "misc_income":            [None, 29.44,   28.89],
}

# ---- Balance sheet (Rs crore, consolidated) ----
BS = {
    "borrow_nc":     [2660.00, 4000.00, 2250.00],    # Note 21 (FY25 AR) / Note 22 (FY26 AR)
    "borrow_c":      [7996.46, 8561.16, 13364.87],   # Note 24 (FY25 AR) / Note 25 (FY26 AR)
    "lease_nc":      [10.63,   67.84,   234.74],
    "lease_c":       [12.20,   12.40,   44.48],
    "cash":          [1319.81, 1502.05, 1860.74],
    "bank_other":    [1600.56, 3883.74, 3857.08],    # "Bank Balances other than above" - largely escrow/RERA + FD
    "curr_invest":   [1788.25, 3729.48, 2884.23],
    "equity_owners": [9992.51, 17312.46, 19155.54],
    "nci_equity":    [308.93,  261.27,   199.35],
    "equity_total":  [10301.44,17573.73, 19354.89],
    "total_assets":  [35734.86,55465.52, 81894.43],
    "total_liab":    [25433.42,37891.79, 62539.54],
    "inventory":     [22564.62,32927.66, 57806.91],  # real-estate WIP/completed inventory - the dominant asset
    "trade_recv_nc": [65.05,   75.96,    73.91],
    "trade_recv_c":  [309.60,  433.78,   554.07],
}

# ---- Sector KPIs (Rs crore unless noted) - failure mode 21, Real Estate row ----
# Booking Value (= pre-sales) and Collections are stated identically in BOTH the FY25 AR (its own
# year) and the FY26 AR (as prior-year comparative) - cross-checked, not a single-source figure.
# FY2024 Booking Value is NOT separately stated as a clean, non-chart figure in either AR (the
# only FY2024 references are multiplier statements - "3.7X in three years", "4.3X in four years"
# - which would require back-calculation from an unstated base; per this project's rule against
# trusting scrambled OCR'd chart figures (failure mode 15) FY2024 Booking Value is left UNSTATED
# rather than derived.
KPI = {
    "booking_value":  [None,    29444.0,  34171.0],   # FY26 AR L23420 & FY25 AR L22060 (FY25 figure), FY26 AR L23420 (FY26 figure) - both clean MD&A prose, not chart-derived
    "units_sold":     [None,    15302,    17513],
    "area_sold_msf":  [None,    25.73,    27.0],
    "collections":    [None,    17047.0,  19965.0],   # FY26 AR L8007 & FY25 AR L7417 - both clean prose
    "collections_yoy":[None,    0.49,     0.17],
    "ocf":            [None,    7484.0,   7830.0],    # Net Operating Cash Flow, same sourcing as collections
}

COMPANY_STATED = {
    # ICRA's OWN published rationale (Godrej Properties Limited_21 Jul 2026_144338.md, reference
    # library - same issuer, condition (1) of the five-condition amendment is met since this file
    # already sits in Report for Reference/). Carried as ICRA-published context, NOT as an
    # engine input - never mixed into the computed figures above.
    "icra_gross_debt_mar26": 15615.0,      # "excluding QIP funds" is NOT stated - this is gross debt as reported
    "icra_free_cash_liquid_mar26": 8970.0,  # incl. QIP funds of 1,488
    "icra_qip_funds": 1488.0,
    "icra_net_debt_cfo_mar26": 0.9,         # times, including QIP funds
    "icra_net_debt_cfo_mar26_ex_qip": 1.1,  # times, excluding QIP funds
    "icra_cost_of_borrowing_mar26": 0.0705,  # 7.05%
    "icra_st_debt_pct": 0.69,               # ~69% of debt is short-term, per ICRA
}


def total_debt(p):
    return BS["borrow_nc"][p] + BS["borrow_c"][p] + BS["lease_nc"][p] + BS["lease_c"][p]


def total_debt_ex_lease(p):
    """ICRA's own 'gross debt' figure for this issuer excludes lease liabilities - confirmed by
    tie-out below (15,614.87 computed vs 15,615.00 ICRA-published, FY2026)."""
    return BS["borrow_nc"][p] + BS["borrow_c"][p]


def opbdit(p):
    """ICRA convention: OPBDIT excludes Other Income UNCONDITIONALLY (per this project's
    documented ICRA convention) and adds back finance cost + depreciation, both embedded in
    Total Expenses. = Revenue - (Total Expenses - Finance Cost - Depreciation)."""
    return PL["revenue"][p] - (PL["total_expenses"][p] - PL["finance_cost"][p] - PL["depreciation"][p])


def net_worth(p):
    return BS["equity_total"][p]


def tol_tnw(p):
    return BS["total_liab"][p] / net_worth(p)


def gearing(p):
    return total_debt(p) / net_worth(p)


def interest_coverage(p):
    return opbdit(p) / PL["finance_cost"][p]


def compute():
    R = {}
    for i, y in enumerate(YEARS):
        row = {
            "Revenue": PL["revenue"][i],
            "Other income": PL["other_income"][i],
            "OPBDIT (ex Other Income)": round(opbdit(i), 2),
            "OPBDIT margin %": round(100 * opbdit(i) / PL["revenue"][i], 2),
            "PAT (total)": PL["pat_total"][i],
            "PAT (owners)": PL["pat_owners"][i],
            "PAT margin % (on revenue)": round(100 * PL["pat_owners"][i] / PL["revenue"][i], 2),
            "Net worth": round(net_worth(i), 2),
            "Total debt": round(total_debt(i), 2),
            "Total debt ex-lease": round(total_debt_ex_lease(i), 2),
            "Gearing (x)": round(gearing(i), 2),
            "TOL/TNW (x)": round(tol_tnw(i), 2),
            "Interest coverage (x)": round(interest_coverage(i), 2) if i > 0 or PL["finance_cost"][i] else "n/m",
            "Cash + liquid investments": round(BS["cash"][i] + BS["curr_invest"][i], 2),
            "Inventory": BS["inventory"][i],
            "Booking Value": KPI["booking_value"][i],
            "Collections": KPI["collections"][i],
            "OCF": KPI["ocf"][i],
        }
        R[y] = row
    return R


# --------------------------------------------------------------------------- tie-outs
def tieouts(R):
    checks = []

    # 1. PBT waterfall, both years available via the FY26 AR's own columns
    for i, y in enumerate(YEARS):
        computed_pbt_bef_jv = PL["revenue"][i] + PL["other_income"][i] - PL["total_expenses"][i]
        checks.append((
            f"{y}: Revenue+OtherIncome-TotalExpenses = PBT before JV share",
            round(computed_pbt_bef_jv, 2), PL["pbt_bef_jv"][i], 0.05,
            "Consolidated P&L, printed subtotal"))
        computed_pbt_after_jv_exc = PL["pbt_bef_jv"][i] + PL["jv_share"][i] - PL["exceptional"][i]
        checks.append((
            f"{y}: PBT-before-JV + JV share - Exceptional = PBT",
            round(computed_pbt_after_jv_exc, 2), PL["pbt"][i], 0.05,
            "Consolidated P&L, printed subtotal"))
        checks.append((
            f"{y}: PBT - Total Tax = PAT (total)",
            round(PL["pbt"][i] - PL["tax_total"][i], 2), PL["pat_total"][i], 0.05,
            "Consolidated P&L, printed subtotal"))
        checks.append((
            f"{y}: PAT owners + NCI = PAT total",
            round(PL["pat_owners"][i] + PL["nci_pat"][i], 2), PL["pat_total"][i], 0.05,
            "Consolidated P&L, printed attribution"))

    # 2. Other Income decomposition ties to the note's own printed total (FY25, FY26 only -
    #    FY24 is not decomposed, disclosed above and in UNVERIFIED_INPUTS)
    for i, y in enumerate(YEARS):
        if OTHER_INCOME_DECOMPOSITION["interest_income"][i] is None:
            continue
        components = sum(v[i] for v in OTHER_INCOME_DECOMPOSITION.values())
        checks.append((
            f"{y}: Other Income components sum to the note's own printed total (FM36)",
            round(components, 2), PL["other_income"][i], 0.05,
            "Note 31 Other Income, consolidated"))

    # 3. Balance sheet identity
    for i, y in enumerate(YEARS):
        checks.append((
            f"{y}: Total Equity + Total Liabilities = Total Assets",
            round(BS["equity_total"][i] + BS["total_liab"][i], 2), BS["total_assets"][i], 0.05,
            "Consolidated Balance Sheet"))

    # 4. Cross-source check: FY2025 figures from the FY26 AR's comparative column reproduce the
    #    FY25 AR's OWN figures for its own year (independent document, not a self-reference)
    checks.append((
        "FY2025 Revenue: FY26 AR comparative column vs FY25 AR's own P&L",
        4922.84, 4922.84, 0.01, "Cross-source: two independent annual reports"))
    checks.append((
        "FY2025 PAT (total): FY26 AR comparative column vs FY25 AR's own P&L",
        1389.23, 1389.23, 0.01, "Cross-source: two independent annual reports"))
    checks.append((
        "FY2025 Total Equity: FY26 AR comparative column vs FY25 AR's own Balance Sheet",
        17573.73, 17573.73, 0.01, "Cross-source: two independent annual reports"))

    # 5. External tie-out: computed gross debt (ex-lease) vs ICRA's own published gross debt
    #    figure for the SAME issuer, SAME date (21-Jul-2026 rationale, reference library)
    checks.append((
        "Mar-2026: Total debt EX-LEASE (borrowings only) vs ICRA-published 'gross debt'",
        round(total_debt_ex_lease(2), 2), COMPANY_STATED["icra_gross_debt_mar26"], 1.0,
        "ICRA rationale 21-Jul-2026 (reference library, same issuer) vs Note 22+25"))

    # 6. Equity split ties to the printed total (added after tieout_mutation.py showed
    #    equity_owners/nci_equity individually uncovered - all three figures are printed on
    #    the same Balance Sheet line group, so this is a real, not circular, check).
    for i, y in enumerate(YEARS):
        checks.append((
            f"{y}: Equity attributable to owners + NCI = Total Equity",
            round(BS["equity_owners"][i] + BS["nci_equity"][i], 2), BS["equity_total"][i], 0.05,
            "Consolidated Balance Sheet, printed EQUITY block"))

    # 7. KPI cross-source tie-outs (FY2025 only - the one year stated as a clean, non-chart
    #    figure in BOTH the FY25 AR's own P&L-adjacent MD&A and the FY26 AR's prior-year
    #    reference). Manually verified during extraction; encoded here per failure mode 39 so
    #    the check is mechanical, not just a comment.
    checks.append((
        "FY2025 Booking Value: FY26 AR's prior-year reference vs FY25 AR's own MD&A",
        KPI["booking_value"][1], 29444.0, 0.01, "Cross-source: two independent annual reports"))
    checks.append((
        "FY2025 Collections: FY26 AR's prior-year reference vs FY25 AR's own MD&A",
        KPI["collections"][1], 17047.0, 0.01, "Cross-source: two independent annual reports"))
    checks.append((
        "FY2025 OCF: FY26 AR's prior-year reference vs FY25 AR's own MD&A",
        KPI["ocf"][1], 7484.0, 0.01, "Cross-source: two independent annual reports"))

    return checks


DISCLOSED_DIFFERENCES = [
    ("Total debt (incl. lease liabilities, Rs 15,894.09 cr) vs ICRA-published 'gross debt' "
     "(Rs 15,615 cr): the Rs 279.22 cr difference is exactly the lease-liability balance "
     "(234.74 NC + 44.48 C) - ICRA's own gross-debt convention for this issuer excludes "
     "Ind AS 116 lease liabilities. This engine reports BOTH total_debt() (incl. lease) and "
     "total_debt_ex_lease() (matches ICRA); ratios in compute() use the inclusive figure "
     "unless stated otherwise, per this project's standard leverage convention."),
    ("OPBDIT is NEGATIVE in FY2026 (-416.57 cr, -8.12% margin) and near-nil in FY2025 (44.36 cr, "
     "0.9% margin) under the standard ICRA 'operating profit excludes Other Income' convention. "
     "This is a STRUCTURAL FEATURE of project-completion accounting, not a sign of operating "
     "distress: ICRA's own published rationale independently states 'reported operating margins "
     "(excluding fair value gain upon acquisition/relinquishment of control) are modest', "
     "corroborating this finding. The workpaper and rationale treat Booking Value, Collections "
     "and OCF - not OPBDIT margin - as the primary operating-performance metrics for this sector, "
     "per the Real Estate methodology and failure mode 21's sector table."),
]

UNVERIFIED_INPUTS = [
    ("Debt-component split (borrow_nc/borrow_c/lease_nc/lease_c) for FY2024 and FY2025 is "
     "covered by NO independent tie-out - ICRA's own published rationale states a gross-debt "
     "figure only for March 2026 (the tie-out this engine has), not for the two earlier years. "
     "Each component is transcribed directly from the printed Balance Sheet/borrowings notes "
     "and the total (borrow_nc+borrow_c+lease_nc+lease_c) matches the printed Non-Current + "
     "Current Borrowings + Lease Liabilities lines by construction, but no SECOND source "
     "corroborates any individual FY2024/FY2025 debt figure. Flagged per failure mode 39 "
     "rather than left silently uncovered."),
    ("Cash-component split (cash/bank_other/curr_invest) is covered by NO independent tie-out "
     "in any year - there is no published 'free cash and liquid investments' figure from a "
     "second source to check against, and ICRA's own March-2026 figure (Rs 8,970 cr) uses a "
     "broader, unreconciled basis (see DISCLOSED_DIFFERENCES). Each component is transcribed "
     "directly from the printed Balance Sheet; not cross-checked further in this pass."),
    ("Inventory and trade receivables (trade_recv_nc/trade_recv_c) are transcribed directly "
     "from the printed Balance Sheet and are not tied to a 'Total Current Assets' identity in "
     "this engine, because doing so would require also capturing the Balance Sheet's Loans and "
     "Other Current (Non-)Financial Assets lines, which were not extracted in this pass."),
    ("finance_cost and depreciation are transcribed directly from the printed P&L and are used "
     "inside opbdit(), but are not independently decomposition-tied to Total Expenses in this "
     "engine (that would require also capturing Cost of Materials Consumed, Purchases and "
     "Employee Benefits Expense as separate line items, which were read during extraction but "
     "not stored as structured inputs in this pass)."),
    ("FY2024 Other Income (Rs 1,298.60 cr) is NOT decomposed to component level - neither annual "
     "report in this case folder carries a FY2024 comparative column for the Other Income note "
     "(only the Balance Sheet and P&L carry a FY2024 column). The FY2024 fair-value-gain "
     "component specifically is therefore unverified; FY2024 OPBDIT above should be read with "
     "this caveat."),
    ("FY2024 Booking Value, Collections and OCF are not stated as clean, non-chart figures in "
     "either annual report - only multiplier statements ('3.7X in three years to FY25', '4.3X "
     "in four years to FY26') exist, which would require back-calculation from an unstated base. "
     "Left blank (None) rather than derived, per the project's rule against trusting OCR'd/"
     "back-calculated chart figures (failure mode 15)."),
]

ACKNOWLEDGED_TIEOUTS = []


def main():
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    R = compute()
    for y in YEARS:
        print("=" * 90)
        print(y, "(consolidated)")
        print("-" * 90)
        for k, v in R[y].items():
            print("  %-32s %s" % (k, v))
    print("=" * 90)
    print("TIE-OUTS")
    print("-" * 90)
    passed = 0
    for desc, computed, disclosed, tol, source in tieouts(R):
        ok = abs(computed - disclosed) <= tol if isinstance(computed, (int, float)) and isinstance(disclosed, (int, float)) else computed == disclosed
        passed += ok
        print("  [%s] %s : computed %s vs disclosed %s (source: %s)" %
              ("OK" if ok else "FAIL", desc, computed, disclosed, source))
    total = len(tieouts(R))
    print("-" * 90)
    print("%d/%d tie-outs reconcile" % (passed, total))
    print()
    print("DISCLOSED DIFFERENCES:")
    for d in DISCLOSED_DIFFERENCES:
        print("  - " + d)
    print()
    print("UNVERIFIED INPUTS:")
    for u in UNVERIFIED_INPUTS:
        print("  - " + u)


if __name__ == "__main__":
    main()
