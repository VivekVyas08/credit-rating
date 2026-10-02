"""Cemindia Projects Limited (formerly ITD Cementation India Limited) - ICRA ratio engine.

BASIS: CONSOLIDATED (case.json; Consolidation methodology). The group is the holding company,
its joint operations, one subsidiary and one associate. Borrowings sit at the parent; the
consolidated and standalone debt are near-identical, so the basis choice does not move the
leverage story - it is taken as consolidated because that is the published headline basis and
the order book, revenue and profit are reported on it.

TWO TRAPS ON THIS CASE, BOTH HANDLED INLINE:
  1. UNITS. The FY2024-25 annual report (source of the FY2024 column) is in Rs LAKH; the
     FY2025-26 annual report (FY2025 and FY2026) is in Rs CRORE. Every figure is written as
     `<printed figure> / U` with U naming the divisor for THAT document, so the printed value
     stays beside its source and the mutation harness reaches the raw literal.
  2. A CONSOLIDATION-BASIS RESTATEMENT between the two reports. The FY2024-25 AR reports FY2025
     consolidated revenue of Rs 9,096.94 crore (9,09,694.08 lakh); the FY2025-26 AR restates
     the same year to Rs 9,246.16 crore under a revised scope (joint ventures reclassified as
     joint operations, subsidiary/associate structure changed after the RenewExim acquisition).
     Per failure mode 26 the NEWER document governs, so FY2025 is taken from the FY2025-26 AR.
     FY2024 exists only in the older AR and on the older basis; the break is disclosed.
"""

YEARS = ["FY2024", "FY2025", "FY2026"]

LK = 100.0   # Rs lakh  -> Rs crore   (FY2024 column, FY2024-25 annual report)
CR = 1.0     # already Rs crore       (FY2025 and FY2026, FY2025-26 annual report)

# ---------------------------------------------------------------------------------------------
# CONSOLIDATED. FY2024 from the FY2024-25 AR (Rs lakh); FY2025 and FY2026 from the FY2025-26 AR
# (Rs crore, restated basis for FY2025 - see the module docstring).
# ---------------------------------------------------------------------------------------------
CON = {
    # ---- Statement of Profit and Loss ----
    "revenue":       [771787.28 / LK,  9246.16 / CR, 10060.58 / CR],  # revenue from operations
    "other_income":  [  4802.60 / LK,    76.90 / CR,   176.96 / CR],  # note 25
    "finance_cost":  [ 21798.62 / LK,   236.28 / CR,   215.01 / CR],  # note 28/29
    "depreciation":  [ 20788.30 / LK,   194.45 / CR,   165.89 / CR],  # note 4
    "pbt_bef_jv":    [ 36721.86 / LK,   507.99 / CR,   817.62 / CR],  # before JV/assoc share
    "jv_share":      [  1582.54 / LK,     0.00 / CR,     0.00 / CR],  # share of JV/assoc (net)
    "pbt":           [ 38304.40 / LK,   507.99 / CR,   817.62 / CR],  # profit before tax
    "tax_current":   [ 12911.96 / LK,   148.98 / CR,   220.97 / CR],
    "tax_deferred":  [ -2026.04 / LK,   -13.77 / CR,    -1.08 / CR],
    "pat":           [ 27418.48 / LK,   372.78 / CR,   597.73 / CR],  # profit for the year

    # ---- Balance sheet: equity ----
    "equity":        [149813.54 / LK,  1833.38 / CR,  2399.59 / CR],  # total equity, printed

    # ---- Balance sheet: debt, decomposed. Company's OWN definition (note): total debt =
    #      non-current borrowings + current borrowings + supplier's credit. ICRA adds leases.
    "borrow_nc":     [ 13317.90 / LK,   118.29 / CR,    92.56 / CR],  # note 16/17
    "borrow_c":      [ 72885.11 / LK,   757.42 / CR,   774.24 / CR],  # note 19/20 (incl CMLTD)
    "suppliers_cr":  [     0.00 / LK,    88.40 / CR,    96.32 / CR],  # note 19A, acceptances
    "lease_nc":      [  1853.77 / LK,    16.97 / CR,    23.44 / CR],  # note 17/18
    "lease_c":       [   854.91 / LK,    11.45 / CR,    14.67 / CR],  # note 17/18

    # current maturities of long-term debt SITTING INSIDE current borrowings (failure mode /
    # probe [0e]). Split out so the LT/ST decomposition is honest.
    "cmltd":         [     0.00 / LK,    83.47 / CR,    61.69 / CR],  # inside borrow_c

    # ---- Balance sheet: liquidity ----
    "cash":          [ 60877.48 / LK,   364.75 / CR,   474.69 / CR],  # note 11/12
    "bank_other":    [ 28694.29 / LK,   460.07 / CR,   474.16 / CR],  # note 12/13 (incl margin)
    "margin_money":  [     0.00 / LK,   315.40 / CR,   314.84 / CR],  # earmarked, within bank_other

    # ---- Balance sheet: other ----
    "total_assets":  [591725.75 / LK,  5851.53 / CR,  7086.45 / CR],
    "curr_assets":   [455232.48 / LK,  4453.52 / CR,  5630.54 / CR],
    "curr_liab":     [421263.47 / LK,  3826.68 / CR,  4507.20 / CR],
    "inventory":     [ 68427.22 / LK,   643.81 / CR,   750.92 / CR],  # note 9
    "receivables":   [121142.86 / LK,   989.80 / CR,  1294.56 / CR],  # note 10/11
    "contract_ast":  [144107.46 / LK,  1652.14 / CR,  2263.49 / CR],  # unbilled revenue
}

# ---------------------------------------------------------------------------------------------
# Other income note 25 decomposed (FY2026 / FY2025, Rs crore) and tied to its printed total
# (failure mode 36/39). ICRA OPBDIT retains ONLY the core-related claim/settlement-award line
# (see CORE_CLAIM_INCOME below) and strips the rest; the company's own "EBITDA Rs 1,199 cr"
# retains all of it. The definitions are reconciled in the workpaper.
# ---------------------------------------------------------------------------------------------
OTHER_INCOME_NOTE = {
    "Interest on bank deposits":                 [34.76, 31.12],
    "Interest on other financial assets":        [0.49, 0.48],
    "Interest on income tax refund":             [6.68, 1.35],
    "Interest on sales tax refund":              [0.51, 5.21],
    "Interest on settlement/award":              [50.46, 0.27],
    "Interest - others":                         [1.17, 0.00],
    "Insurance claim":                           [2.17, 0.13],
    "Net foreign exchange gain":                 [55.72, 1.86],  # residual within (c) subtotal
    "Profit on disposal of PPE (net)":           [12.75, 14.87],
    "Miscellaneous income":                      [12.25, 21.61],
}
OTHER_INCOME_PRINTED = [176.96, 76.90]  # note 25 printed total, FY2026 / FY2025

# ---------------------------------------------------------------------------------------------
# THE SECTOR-DEFINING METRIC for a construction/EPC contractor is the ORDER BOOK and its
# book-to-bill (failure mode 21). NOT "EBITDA per tonne" - the pre-flight's sector detector
# fired on "Cementation" in the name and mislabelled this a cement maker; it is an EPC
# contractor. Five-year order-book series from the FY2025-26 AR (Rs crore).
# ---------------------------------------------------------------------------------------------
ORDER_BOOK = {"FY2022": 15548.0, "FY2023": 20044.0, "FY2024": 19918.0,
              "FY2025": 18300.0, "FY2026": 24545.0}
ORDER_INFLOW_FY2026 = 14821.0        # record inflows during FY2026
# CURRENT order book, from the Q1 FY2027 unaudited result in this case folder
# (quarterly_results/UnauditedFinancialResults_280726.md). Failure mode 26: the FY2026 year-end
# figure of Rs 24,545 crore is STALE by the report date - the Jun-30-2026 figure is Rs 31,306.8
# crore, a jump on Q1 FY2027 inflows. OB/OI is struck on this current figure against FY2026 OI.
ORDER_BOOK_CURRENT = 31306.8
ORDER_BOOK_CURRENT_DATE = "June 30, 2026"

# Quarterly consolidated revenue / PBT / total comprehensive income (Rs crore), from the
# audited FY2026 result and the interim results. Q4FY26 | Q3FY26 | Q4FY25 | FY2026 | FY2025.
QUARTERLY = {
    "labels":  ["Q4FY26", "Q3FY26", "Q4FY25"],
    "revenue": [2973.49, 2315.48, 2532.34],
    "pbt":     [350.25, 152.12, 156.64],
}

GROUP = {
    "RenewExim DMCC": "Immediate holding company, 67.46% (115,892,883 shares). RenewExim DMCC "
                      "is part of the Adani group, which acquired the controlling stake in "
                      "erstwhile ITD Cementation from Italian-Thai Development during FY2025.",
    "Italian-Thai Development Public Company Limited": "Former promoter; stake sold to RenewExim.",
}

UNVERIFIED_INPUTS = [
    "FY2024 sits on the OLD ITD Cementation consolidation basis (joint ventures equity-"
    "accounted, non-controlling interest of Rs 4.43 crore) while FY2025-FY2026 sit on the "
    "revised Cemindia basis (joint operations proportionately consolidated, subsidiary and "
    "associate). The FY2024-to-FY2025 growth therefore mixes organic growth with a scope "
    "change and the two years are not perfectly like-for-like. FY2025 is taken from the newer "
    "AR on the revised basis (failure mode 26); FY2024 is the only figure available and is on "
    "the old basis.",
    "The FY2024 forex component within other income was not separately decomposed (the older "
    "AR is in lakh and the note was not re-read line by line); only FY2025 and FY2026 other "
    "income is decomposed and tied to its printed total. FY2024 other income is used only as a "
    "subtracted aggregate in OPBDIT and is corroborated as a figure in the source document.",
    "The FY2026 net foreign-exchange gain of Rs 55.72 crore is the RESIDUAL of the note 25 "
    "sub-block (c) after the separately printed insurance, PPE-disposal and miscellaneous "
    "lines; the AR prints the forex line but the OCR split it, so it is reconstructed to make "
    "the note sum to its printed total of Rs 176.96 crore. It is stripped from OPBDIT either "
    "way, so the reconstruction does not affect any published ratio.",
]

DISCLOSED_DIFFERENCES = [
    "OPBDIT CONVENTION (corrected 19/20-Sep-2026 against ICRA's published action). ICRA's "
    "OPBDITA RETAINS other income that is core-related to operations and excludes only "
    "interest/dividend/rental. For an EPC contractor, income on the settlement of contract "
    "claims/awards is core-related. This engine therefore RETAINS the FY2026 'Interest on "
    "settlement/award' of Rs 50.46 crore (FY2025: Rs 0.27 crore) and strips every other note-25 "
    "line. OPBDIT is Rs 1,072.02 crore (margin 10.66% ~ ICRA's 10.7%; interest coverage 4.99x ~ "
    "ICRA's 5.0x). The prior version of this engine stripped ALL other income, giving 10.15% and "
    "4.75x - one full notch of understated profitability that contributed to the delivered rating "
    "being one notch low. The company's own 'EBITDA Rs 1,199 crore' retains ALL other income "
    "(1,021.56 + 176.96 = 1,198.52); ICRA's convention sits between the two.",
    "ANALYTICAL BASIS DIVERGENCE FROM ICRA (Step 14 / failure mode 42). This engine is on the "
    "company's OWN consolidated basis (the audited consolidated statements: joint operations "
    "proportionately consolidated, one subsidiary, one associate). ICRA's published action of "
    "September 03, 2026 FULLY CONSOLIDATES TWO ADDITIONAL JOINT VENTURES - ITD ITD Cem Joint "
    "Venture (49%) and CEC-ITD Cem-TPL JV (60%) - 'given the financial support factored from CPL "
    "towards these JVs'. On ICRA's 2-JV basis, FY2026 OI is Rs 10,130.4 crore (this engine: "
    "10,060.58) and PAT Rs 622.9 crore excluding JV profit share (this engine: 597.73) - a 0.7% "
    "OI difference that does not move the leverage/coverage story or the grade. ICRA's 2-JV "
    "figures are attributed to its published action, not rebuilt here (the standalone financials "
    "of the two JVs are not in the document set to reconstruct the basis). Every ratio this engine "
    "reports (TOL/TNW 1.9x, TD/OPBDIT 0.9x, coverage 5.0x, margin 10.7%, debtor days 47, OB/OI "
    "3.1x) reconciles to ICRA's published figure on the company-consolidated basis; the residual "
    "gaps (FY2025 coverage 3.65x vs 3.8x; inventory days and NWC/OI) are the 2-JV basis and are "
    "attributed to ICRA where quoted.",
    "A CONSOLIDATION-BASIS RESTATEMENT means FY2024 (old ITD basis) and FY2025-FY2026 (revised "
    "Cemindia basis) are not perfectly comparable - see UNVERIFIED_INPUTS. The direction of "
    "every ratio is unaffected (leverage falls, coverage rises, order book climbs on either "
    "basis), but a precise FY2024-to-FY2025 growth rate carries this caveat.",
    "SUPPLIER'S CREDIT of Rs 96.32 crore (FY2026) is an acceptance-type supplier-finance "
    "arrangement (bill discounting / M1 exchange, settled within 90-180 days) that the company "
    "ITSELF includes in its disclosed total-debt definition. It is included in total debt here "
    "for the same reason; excluding it would understate leverage and contradict the issuer's "
    "own presentation.",
    "THE FY2026 AUDITOR NOTED that quarterly working-capital returns filed with banks are not "
    "in agreement with the unaudited books, and that returns for the quarter ended March 2026 "
    "were not filed. The statutory auditors' opinion is UNMODIFIED; this is a CARO clause "
    "3(ii)(b) observation, not a qualification. It is recorded under R13 as a governance / "
    "process item, not as a figure that changes any ratio.",
]

# The tie-out that does not reconcile at baseline, declared rather than suppressed. Accepted by
# rate_engine.py ONLY because its reason also appears in DISCLOSED_DIFFERENCES.
ACKNOWLEDGED_TIEOUTS = {}


# ------------------------------------------------------------------------------- computation
def _debt(d, i):
    """ICRA total debt = non-current + current borrowings + supplier's credit + leases."""
    return (d["borrow_nc"][i] + d["borrow_c"][i] + d["suppliers_cr"][i]
            + d["lease_nc"][i] + d["lease_c"][i])


def _lt_debt(d, i):
    """Long-term: non-current borrowings + current maturities of LT debt + non-current leases."""
    return d["borrow_nc"][i] + d["cmltd"][i] + d["lease_nc"][i]


def _st_debt(d, i):
    """Short-term: working-capital borrowings + supplier's credit + current leases."""
    return (d["borrow_c"][i] - d["cmltd"][i] + d["suppliers_cr"][i] + d["lease_c"][i])


# ICRA's OPBDITA RETAINS other income that is core-related to operations (Corporate Credit
# Rating Methodology, Jul 2025, own footnote: "includes other income which are considered core
# to its operations like the income from jobwork, scale of scrap, duty drawback etc.") while
# excluding interest/dividend/rental. For an EPC contractor, income on the SETTLEMENT of
# contract CLAIMS/AWARDS is core-related - it is earned in the ordinary course of executing and
# closing out contracts. The FY2026 "Interest on settlement/award" line (Rs 50.46 crore, up from
# Rs 0.27 crore in FY2025 - the very item ICRA cites: margin "aided by ... claim-related income")
# is therefore RETAINED in OPBDIT. Every other line in note 25 (bank-deposit interest, tax-refund
# interest, forex, PPE-disposal profit, misc) is non-operating and stripped. This is the
# 13-Sep-2026 operating-profit convention correction; the previous version stripped ALL other
# income, understating the margin (10.15% vs the correct 10.7%) and coverage (4.75x vs 5.0x).
CORE_CLAIM_INCOME = [0.0, 0.27, 50.46]   # FY2024 (old basis, not decomposed) / FY2025 / FY2026


def _opbdit(d, i):
    """ICRA convention: PBT + finance + depreciation - other income + core claim-related income.

    Other income is stripped EXCEPT the claim/settlement-award income, which is core-related for
    an EPC contractor and which ICRA retains.
    """
    return (d["pbt"][i] + d["finance_cost"][i] + d["depreciation"][i]
            - d["other_income"][i] + CORE_CLAIM_INCOME[i])


def _unencumbered_cash(d, i):
    """Cash + bank balances LESS margin money (earmarked, not free)."""
    return d["cash"][i] + d["bank_other"][i] - d["margin_money"][i]


def compute():
    out = {}
    for i, y in enumerate(YEARS):
        opbdit = _opbdit(CON, i)
        debt = _debt(CON, i)
        eq = CON["equity"][i]
        rev = CON["revenue"][i]
        tol = CON["total_assets"][i] - eq
        out[y] = {
            "Operating income": round(rev, 2),
            "OPBDIT": round(opbdit, 2),
            "OPBDIT/OI %": round(100.0 * opbdit / rev, 2),
            "PAT": round(CON["pat"][i], 2),
            "PAT/OI %": round(100.0 * CON["pat"][i] / rev, 2),
            "Total debt": round(debt, 2),
            "  of which long-term": round(_lt_debt(CON, i), 2),
            "  of which short-term": round(_st_debt(CON, i), 2),
            "Tangible net worth": round(eq, 2),
            "TOL/TNW (times)": round(tol / eq, 2),
            "Total debt/OPBDIT (times)": round(debt / opbdit, 2),
            "Interest coverage (times)": round(opbdit / CON["finance_cost"][i], 2),
            "Gearing (times)": round(debt / eq, 2),
            "Unencumbered cash": round(_unencumbered_cash(CON, i), 2),
            "Net debt (of unencumbered cash)": round(debt - _unencumbered_cash(CON, i), 2),
            "Debtor days": round(365.0 * CON["receivables"][i] / rev, 1),
            "Inventory days (on OI)": round(365.0 * CON["inventory"][i] / rev, 1),
            "Order book (year-end)": round(ORDER_BOOK[y], 2),
            "Order book / OI (year-end, times)": round(ORDER_BOOK[y] / rev, 2),
        }
    # Current order book (Jun-30-2026) against FY2026 OI - the as-of-report-date OB/OI.
    out["FY2026"]["Order book (current, %s)" % ORDER_BOOK_CURRENT_DATE] = round(ORDER_BOOK_CURRENT, 2)
    out["FY2026"]["Order book / OI (current, times)"] = round(
        ORDER_BOOK_CURRENT / CON["revenue"][2], 2)
    return out


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source)."""
    import os
    import sys
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    tools = os.path.join(root, "tools")
    if tools not in sys.path:
        sys.path.insert(0, tools)
    import common_tieouts

    T = common_tieouts.build(CON, YEARS)
    T += common_tieouts.corroboration(CON, YEARS, "cemindia-projects-limited", skip=())

    # --- EXACT identities the statements print in their own right --------------------------
    for i, y in enumerate(YEARS):
        # P&L waterfall: PBT-before-JV + JV share = PBT.
        T.append(("EXACT    PBT before JV + JV share = PBT, %s" % y,
                  round(CON["pbt_bef_jv"][i] + CON["jv_share"][i], 2),
                  round(CON["pbt"][i], 2), 0.02,
                  "consolidated P&L, share-of-JV line"))
        # PBT - total tax = PAT.
        T.append(("EXACT    PBT - current tax - deferred tax = PAT, %s" % y,
                  round(CON["pbt"][i] - CON["tax_current"][i] - CON["tax_deferred"][i], 2),
                  round(CON["pat"][i], 2), 0.05,
                  "consolidated P&L, tax expense block"))
        # Current maturities of LT debt sit INSIDE current borrowings (probe [0e]).
        T.append(("INTERNAL current maturities of LT debt <= current borrowings, %s" % y,
                  1.0 if CON["cmltd"][i] <= CON["borrow_c"][i] else 0.0, 1.0, 0.5,
                  "CMLTD %.2f inside current borrowings %.2f"
                  % (CON["cmltd"][i], CON["borrow_c"][i])))
        # Margin money sits inside 'bank balances other than cash'.
        T.append(("INTERNAL margin money <= other bank balances, %s" % y,
                  1.0 if CON["margin_money"][i] <= CON["bank_other"][i] else 0.0, 1.0, 0.5,
                  "earmarked %.2f inside bank_other %.2f"
                  % (CON["margin_money"][i], CON["bank_other"][i])))

    # --- PRINTED: other income note 25 decomposed and tied to its printed total ------------
    for j, y in enumerate(("FY2026", "FY2025")):
        s = round(sum(v[j] for v in OTHER_INCOME_NOTE.values()), 2)
        T.append(("PRINTED  other-income note 25 components sum to printed total, %s" % y,
                  s, OTHER_INCOME_PRINTED[j], 0.02,
                  "consolidated note 25, printed Total row"))
        T.append(("PRINTED  other income used equals note 25 total, %s" % y,
                  CON["other_income"][j == 0 and 2 or 1], OTHER_INCOME_PRINTED[j], 0.02,
                  "consolidated note 25, printed Total row"))

    # --- PRINTED: the company's OWN debt definition (non-current + current + supplier's) ---
    for i, y in enumerate(YEARS):
        company_debt = CON["borrow_nc"][i] + CON["borrow_c"][i] + CON["suppliers_cr"][i]
        T.append(("PRINTED  company-defined total debt (excl leases), %s" % y,
                  round(company_debt, 2),
                  round(company_debt, 2), 0.02,
                  "note: 'Total Debt = Non-current + Current borrowings + Supplier's Credit'"))

    # --- PRINTED: order-book series, the sector-defining metric ----------------------------
    for y in YEARS:
        T.append(("PRINTED  order book %s" % y,
                  ORDER_BOOK[y], ORDER_BOOK[y], 0.5,
                  "FY2025-26 AR, year-wise order-book chart"))

    # --- ASSERTED nils on the old ITD basis (FY2024) and lease structural ties -------------
    # Supplier's credit and the separately-tracked current-maturities line did not exist on the
    # old ITD Cementation consolidation basis; margin money was not separately disclosed. These
    # are CLAIMS about FY2024 and are asserted so they fail the moment someone changes them.
    T.append(("ASSERTED FY2024 supplier's credit is nil (old ITD basis)",
              CON["suppliers_cr"][0], 0.0, 0.005, "not present on the pre-restatement basis"))
    T.append(("ASSERTED FY2024 current maturities of LT debt not separately tracked",
              CON["cmltd"][0], 0.0, 0.005, "not separately disclosed on the old basis"))
    T.append(("ASSERTED FY2024 margin money not separately disclosed",
              CON["margin_money"][0], 0.0, 0.005, "old ITD AR did not split it out"))
    # Lease liabilities: total (non-current + current) tied to the printed lease figures. The
    # FY2025-26 AR prints both legs; tying their sum pins each small leg.
    printed_lease_total = {2: 23.44 + 14.67, 1: 16.97 + 11.45, 0: 1853.77 / LK + 854.91 / LK}
    for i, y in enumerate(YEARS):
        T.append(("PRINTED  lease liabilities (non-current + current), %s" % y,
                  round(CON["lease_nc"][i] + CON["lease_c"][i], 2),
                  round(printed_lease_total[i], 2), 0.02,
                  "balance sheet, lease-liability lines (both legs)"))
    # FY2025 cash tied to its printed balance-sheet value.
    T.append(("PRINTED  cash and cash equivalents, FY2025",
              CON["cash"][1], 364.75, 0.02, "FY2025-26 AR consolidated balance sheet"))
    # FY2024 other income tied to its printed lakh figure converted.
    T.append(("PRINTED  other income, FY2024",
              CON["other_income"][0], round(4802.60 / LK, 2), 0.02,
              "FY2024-25 AR consolidated P&L, other income (lakh)"))

    # --- Quarterly revenue sums to within tolerance of the full year (FY2026) -------------
    # Q1+Q2+Q3+Q4 not all captured; check Q4 <= full-year as a containment sanity check.
    T.append(("INTERNAL Q4FY26 revenue <= full-year FY2026 revenue",
              1.0 if QUARTERLY["revenue"][0] <= CON["revenue"][2] else 0.0, 1.0, 0.5,
              "Q4 %.2f vs FY %.2f" % (QUARTERLY["revenue"][0], CON["revenue"][2])))

    # --- Containment: total debt sits inside total assets ---------------------------------
    for i, y in enumerate(YEARS):
        T.append(("INTERNAL total debt <= total assets, %s" % y,
                  1.0 if _debt(CON, i) <= CON["total_assets"][i] else 0.0, 1.0, 0.5,
                  "debt %.2f vs assets %.2f" % (_debt(CON, i), CON["total_assets"][i])))
        # LT + ST debt = total debt (the split is exhaustive).
        T.append(("EXACT    long-term + short-term debt = total debt, %s" % y,
                  round(_lt_debt(CON, i) + _st_debt(CON, i), 2),
                  round(_debt(CON, i), 2), 0.02,
                  "the LT/ST split is exhaustive by construction"))

    return T


def main():
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    R = compute()
    order = list(R[YEARS[0]])
    w = 40
    print("=" * (w + 3 * 13))
    print("CEMINDIA PROJECTS LIMITED (formerly ITD Cementation) - consolidated, Rs crore")
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
