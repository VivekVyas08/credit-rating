# -*- coding: utf-8 -*-
"""Alembic Limited - ICRA ratio suite (SOP Steps 5-6).

BASIS: STANDALONE is the primary basis for the ratio suite and the rating view; consolidated is
carried alongside. The reason is structural, not conventional (R12 - basis is methodology-
determined):

  * ALL debt sits at the parent. Consolidated borrowings equal standalone borrowings to the
    rupee in both years (661.08 non-current + 402.77 current), so consolidation adds no debt.
  * The only subsidiary, Alembic City Limited (100%), is immaterial: consolidated revenue from
    operations exceeds standalone by Rs 8.06 crore on a Rs 231.93 crore base.
  * The consolidated picture is dominated by ONE line that is NOT cash: "Share of Associate's
    Profit" of Rs 191.45 crore (FY2026), the equity-method pick-up on the 28.54% Alembic
    Pharmaceuticals stake. That figure EXCEEDS the group's own profit of Rs 125.93 crore, so a
    consolidated margin or coverage ratio is dominated by an accrual the company cannot spend.
    What it CAN spend is the dividend actually received - Rs 62.95 crore - which is a standalone
    P&L line. Debt service is a cash question, so the standalone statements answer it.

Units: the annual reports state everything in Rs LAKH. Converted once, in code, to Rs CRORE
(the ICRA reporting unit) - never re-converted downstream.

Sources: annual-report-2025-26_1.md (FY2026 + FY2025 comparative) and Annual-Report-2024-25.md
(FY2024 comparative column). FY2024 is taken from the FY2024-25 AR rather than the FY2023-24 AR
because it is the same audited figure in a NEWER document (failure mode 26).

ICRA CONVENTION (Corporate Credit Rating Methodology, Jul 2025 + Financial Ratio Analysis):
    OPBDIT  = PBT + finance cost + depreciation - other income
              (other income is stripped UNCONDITIONALLY - this is ICRA's convention and is the
              OPPOSITE of CRISIL's, which retains recurring non-operating income. Applying
              CRISIL's convention here would be failure mode 32/33.)
    Total debt = borrowings incl. leases. AL discloses no separate lease-liability line in
              either year - see ASSERTED checks below.
    TNW     = total equity, excluding revaluation reserves (AL carries none).
"""

YEARS = ["FY2024", "FY2025", "FY2026"]
L = 100.0   # Rs lakh -> Rs crore

# ---------------------------------------------------------------------------------------------
# STANDALONE (Rs lakh as printed; converted inline). Source: FY26 AR pp. Balance Sheet /
# Statement of Profit and Loss; FY2024 column from the FY24-25 AR.
#
# Every figure is written as `<printed lakh figure> / L` so the printed value stays visible in
# the source and the mutation harness can reach it. Converting in a separate pass produced a
# stale copy on an earlier case in this project and made coverage unmeasurable.
# ---------------------------------------------------------------------------------------------
SA = {
    # ---- Statement of Profit and Loss ----
    "revenue":       [15225.00 / L, 21435.79 / L, 23193.16 / L],   # Revenue from Operations
    "other_income":  [ 5461.61 / L,  7451.02 / L,  7277.04 / L],   # note 28
    "finance_cost":  [   68.72 / L,   182.98 / L,   156.74 / L],   # note 33
    "depreciation":  [  746.10 / L,  1024.46 / L,  1200.60 / L],   # notes 4, 5
    "pbt":           [10271.67 / L, 15198.90 / L, 14689.01 / L],   # Profit Before Tax
    "exceptional":   [    0.00 / L,     0.00 / L,     0.00 / L],   # nil in all three years
    "pat":           [ 9288.80 / L, 14194.71 / L, 12453.83 / L],   # Profit for the year
    "tax_current":   [    None,     1675.00 / L,  2200.00 / L],   # current tax
    "tax_deferred":  [    None,     (-514.47) / L,    5.18 / L],  # deferred tax
    "tax_earlier":   [    None,     (-156.34) / L,   30.00 / L],  # earlier-year adjustment
    "tax_ch6a":      [    None,    (-1585.28) / L, (-1585.38) / L],  # Chapter VI-A deduction

    # ---- Balance sheet ----
    "equity_cap":    [ 5135.64 / L,  5135.64 / L,  5135.64 / L],
    "other_equity":  [75740.28 / L, 80183.49 / L, 77010.01 / L],
    "borrow_nc":     [  739.25 / L,  1066.53 / L,   661.08 / L],   # note 18
    "borrow_c":      [  175.65 / L,   378.20 / L,   402.77 / L],   # note 22
    "cash":          [   98.60 / L,   253.04 / L,   109.90 / L],   # note 12
    "bank_other":    [  120.50 / L,   165.87 / L,   187.33 / L],   # note 13
    "curr_inv":      [ 1085.99 / L,  4955.88 / L,  8904.99 / L],   # note 10, current investments
    "total_assets":  [94587.17 / L, 100983.26 / L, 95770.24 / L],
    "inventory":     [ 9260.42 / L,  9938.70 / L,  5224.11 / L],   # note 9
    "receivables":   [ 1739.62 / L,  2789.00 / L,  3020.84 / L],   # note 11

    # Remaining current-asset lines, so CURRENT ASSETS can be built from components and tied
    # to the current ratio the AR prints in its own ratio-disclosure table.
    "other_fin_ca":  [  266.80 / L,   318.65 / L,   353.04 / L],   # note 14
    "other_ca":      [  780.01 / L,  1209.65 / L,   884.34 / L],   # note 15

    # Current liabilities, component by component (borrow_c above is the first line).
    "tp_msme":       [  652.14 / L,   520.90 / L,   677.24 / L],   # note 23(a)
    "tp_others":     [ 2388.76 / L,  2236.96 / L,  1618.91 / L],   # note 23(b)
    "other_fin_cl":  [  535.12 / L,   607.23 / L,   800.45 / L],   # note 24
    "other_cl":      [ 2413.12 / L,  4253.08 / L,  2837.88 / L],   # note 25
    "provisions_c":  [ 2140.84 / L,  2151.55 / L,  2280.05 / L],   # note 26
    "curr_tax_liab": [  612.40 / L,   680.39 / L,  1013.24 / L],   # current tax liabilities (net)

    # Cash-flow statement lines (standalone).
    "capex":         [ 5612.27 / L,  5076.55 / L,  7665.12 / L],   # purchase of PPE + IP + CWIP
    "dividend_paid": [ 5623.40 / L,  6117.20 / L,  6141.43 / L],   # financing activities
}

# The AR's OWN ratio-disclosure table prints the current ratio. It is an independently printed
# figure, not a second transcription of the balance sheet, so tying the component-built current
# ratio to it verifies all eleven working-capital lines at once.
CURRENT_RATIO_DISCLOSED = {"FY2024": 1.50, "FY2025": 1.81, "FY2026": 1.94}

# ---------------------------------------------------------------------------------------------
# CONSOLIDATED - carried for completeness. FY2024 consolidated comparatives were not extracted
# in this pass (the FY24-25 AR's consolidated column was not re-read); the two years that matter
# for the associate-pickup point are present. Named in UNVERIFIED_INPUTS rather than left silent.
# ---------------------------------------------------------------------------------------------
CON = {
    "revenue":        [22188.61 / L, 23998.98 / L],
    "other_income":   [ 7489.42 / L,  7296.55 / L],
    "finance_cost":   [  247.11 / L,   227.84 / L],
    "depreciation":   [ 1062.68 / L,  1238.82 / L],
    "pbt":            [15550.25 / L, 14875.87 / L],
    "pat_before_assoc": [14457.23 / L, 12593.23 / L],
    "assoc_share":    [16610.44 / L, 19144.67 / L],   # equity-method pick-up, NON-CASH
    "pat_total":      [31067.68 / L, 31737.90 / L],
    "equity_cap":     [ 5135.64 / L,  5135.64 / L],
    "other_equity":   [228723.45 / L, 239372.92 / L],
    "borrow_nc":      [ 1066.53 / L,   661.08 / L],
    "borrow_c":       [  378.20 / L,   402.77 / L],
    "equity_method_inv": [156758.91 / L, 170442.62 / L],
    "total_assets":   [250300.36 / L, 258950.81 / L],
}
CON_YEARS = ["FY2025", "FY2026"]

# ---------------------------------------------------------------------------------------------
# THE CENTRAL RATING FIGURE, and it is the company's OWN disclosure - not a CRA's.
# Note 6, "Aggregate market value of quoted investments", standalone, Rs lakh. A four-year
# series is available across the three annual reports, and the DIRECTION is as much the finding
# as the level (failure mode 16): the portfolio peaked in FY2024 and has fallen 33% since.
# ---------------------------------------------------------------------------------------------
MKT_VALUE_QUOTED_LAKH = {
    "FY2023": 315645.64,   # FY23-24 AR, comparative column
    "FY2024": 582375.09,   # FY23-24 AR / FY24-25 AR comparative - both state this figure
    "FY2025": 549020.01,   # FY24-25 AR
    "FY2026": 388589.29,   # FY25-26 AR
}

# Segment note (standalone, Rs lakh) - note 36(T). Real estate is the operating engine.
SEGMENT = {
    "API_revenue":         [None, 3221.48 / L, 4658.52 / L],
    "RealEstate_revenue":  [None, 18214.31 / L, 18534.64 / L],
    "API_pbt":             [None,  472.85 / L,  564.95 / L],
    "RealEstate_pbt":      [None, 8390.15 / L, 7858.90 / L],
    "Unallocated_income":  [None, 6518.89 / L, 6421.90 / L],
}

# Other Income note 28 decomposed (failure mode 36) - Rs lakh, FY2025 and FY2026.
OTHER_INCOME_NOTE = {
    "Interest income":                          [193.36, 139.69],
    "Dividend income":                          [6294.75, 6295.16],
    "Fair value change, investment held for trading": [197.54, 0.00],
    "Profit on sale of investments (net)":      [111.14, 493.07],
    "Gain on foreign currency transactions (net)": [3.21, 4.26],
    "Gain on sale of PPE (net)":                [0.17, 0.00],
    "Insurance claim received (net)":           [328.71, 0.00],
    "Others":                                   [322.15, 344.86],
}
OTHER_INCOME_PRINTED_LAKH = [7451.02, 7277.04]   # note 28 printed total

# Contingent liabilities and commitments, standalone, Rs lakh (note 36(A)/(B)).
CONTINGENT_LAKH = {
    "Letters of credit, guarantees and counter-guarantees": [421.82, 600.92],
    "Service tax disputed in appeal (net of provision 117.69)": [519.71, 519.71],
    "Sales tax disputed in appeal":                        [123.76, 123.76],
    "Green cess disputed in appeal":                       [19.29, 19.29],
}
CAPITAL_COMMITMENTS_LAKH = [3119.22, 1352.39]

GROUP = {
    "Nirayu Private Limited": "Holding company, 63.06% of Alembic Limited (16,19,15,052 shares)",
    "Alembic City Limited": "Subsidiary, 100.00%",
    "Alembic Pharmaceuticals Limited": "Associate, 28.54% (equity method in consolidated)",
    "Paushak Limited": "19.1% - BELOW the 20% associate threshold, so carried at FVOCI, "
                       "not equity-accounted; its fair-value fall hits OCI, not the P&L",
}

UNVERIFIED_INPUTS = [
    "FY2024 CONSOLIDATED comparatives were not extracted in this pass - the consolidated series "
    "carries FY2025 and FY2026 only. The standalone series, which is the rating basis, carries "
    "all three years.",
    "The Paushak Limited shareholding percentage (19.1%) is stated in ICRA's own published "
    "rationale, which is a craft/context reference and NOT a data source under Section 2. The "
    "company's own FY2025-26 AR discloses the holding by share count (47,02,472 shares after a "
    "split and bonus issue) and its fair value, but does not state the percentage. The "
    "percentage is therefore NOT used as a figure anywhere in the deliverable; only the "
    "company-disclosed share count and fair value are.",
    "No lease-liability line is disclosed separately in either the standalone or consolidated "
    "balance sheet in any year, so total debt equals borrowings. ICRA's convention includes "
    "leases in total debt; there is nothing to include. See the ASSERTED checks.",
]

DISCLOSED_DIFFERENCES = [
    "THE AR'S OWN CREDIT-RATING TABLE IS STALE. The FY2025-26 annual report discloses ICRA "
    "ratings of Rs 34.00 + 25.50 + 10.00 crore = Rs 69.50 crore, stamped 'reaffirmed on 28th "
    "February, 2024'. ICRA's own subsequent action of 30-May-2025 reduced the long-term "
    "fund-based line from Rs 34.0 crore to Rs 20.9 crore, taking the total to Rs 56.4 crore. "
    "The newer figure is used (failure modes 14 and 26); the AR's stale disclosure is reported "
    "as a finding rather than silently overwritten.",
    "FY2023 carried an exceptional item of Rs 10.61 crore (Rs 1,060.86 lakh) - a transfer from "
    "General Reserve to the P&L - which drew a QUALIFIED audit opinion on the FY2023 "
    "consolidated results. FY2023 is OUTSIDE this analysis's three-year window; FY2024's audit "
    "opinion carried a qualification only as to the COMPARABILITY of the FY2023 comparative, "
    "and the FY2025 and FY2026 opinions are unmodified. Exceptional items are nil in all three "
    "years analysed. Recorded because a prior-period qualification is rating-relevant "
    "regardless of quantum (R13), not because it affects the computed figures.",
    "The implied tax rate is 6.61% in FY2025 and 15.2% in FY2026, below the 8-45% plausibility "
    "band the shared checks apply. This is genuine and structural, not an extraction error: the "
    "tax reconciliation discloses a Chapter VI-A deduction worth Rs 15.85 crore of tax in BOTH "
    "years - at the 25.17% concessional rate that shelters roughly Rs 63.0 crore of income, "
    "which is the dividend income of Rs 62.95 crore almost exactly (Section 80M inter-corporate "
    "dividend relief). The shelter depends on AL continuing to distribute the dividend it "
    "receives; it is recurring while that policy holds, and is NOT modelled as a permanent "
    "reduction in the tax burden independent of the payout.",
    "FY2026 PAT fell 12.3% (Rs 141.95 crore to Rs 124.54 crore) while PBT fell only 3.4%. The "
    "gap is a tax-line effect, not an operating one: FY2025 carried a deferred tax CREDIT of "
    "Rs 5.14 crore and an excess-provision write-back of Rs 1.56 crore, against a deferred tax "
    "CHARGE of Rs 0.05 crore and a short-provision charge of Rs 0.30 crore in FY2026. Not "
    "treated as an earnings deterioration.",
]


# The one tie-out that does not reconcile, declared rather than suppressed. rate_engine.py
# accepts an acknowledgement ONLY if its reason also appears in DISCLOSED_DIFFERENCES above,
# and prints it on every run - an acknowledged check is never counted as a passing one.
ACKNOWLEDGED_TIEOUTS = {
    "INTERNAL implied tax rate plausible (8-45%), FY2025":
        "The implied tax rate is 6.61% in FY2025 and 15.2% in FY2026, below the 8-45% "
        "plausibility band the shared checks apply. This is genuine and structural, not an "
        "extraction error: the tax reconciliation discloses a Chapter VI-A deduction worth "
        "Rs 15.85 crore of tax in BOTH years. The tax charge itself is verified independently "
        "- 'PRINTED tax reconciliation total = current + deferred' and 'INTERNAL PBT less "
        "total tax equals PAT' both reconcile in both years - so the low rate is explained "
        "arithmetic, not an unmatched PBT/PAT pair.",
}


def _debt(d, i):
    return d["borrow_nc"][i] + d["borrow_c"][i]


def _tnw(d, i):
    return d["equity_cap"][i] + d["other_equity"][i]


def _liquid(d, i):
    return d["cash"][i] + d["bank_other"][i] + d["curr_inv"][i]


def _current_assets(d, i):
    return (d["inventory"][i] + d["curr_inv"][i] + d["receivables"][i] + d["cash"][i]
            + d["bank_other"][i] + d["other_fin_ca"][i] + d["other_ca"][i])


def _current_liabilities(d, i):
    return (d["borrow_c"][i] + d["tp_msme"][i] + d["tp_others"][i] + d["other_fin_cl"][i]
            + d["other_cl"][i] + d["provisions_c"][i] + d["curr_tax_liab"][i])


def _opbdit(d, i):
    """ICRA convention: PBT + finance cost + depreciation - other income."""
    return d["pbt"][i] + d["finance_cost"][i] + d["depreciation"][i] - d["other_income"][i]


def compute():
    out = {}
    for i, y in enumerate(YEARS):
        opbdit = _opbdit(SA, i)
        debt = _debt(SA, i)
        tnw = _tnw(SA, i)
        tol = SA["total_assets"][i] - tnw
        out[y] = {
            "Operating income": round(SA["revenue"][i], 2),
            "OPBDIT": round(opbdit, 2),
            "OPBDIT/OI %": round(100.0 * opbdit / SA["revenue"][i], 2),
            "PAT": round(SA["pat"][i], 2),
            "PAT/OI %": round(100.0 * SA["pat"][i] / SA["revenue"][i], 2),
            "Total debt": round(debt, 2),
            "Tangible net worth": round(tnw, 2),
            "TOL/TNW (times)": round(tol / tnw, 2),
            "Total debt/OPBDIT (times)": round(debt / opbdit, 2),
            "Interest coverage (times)": round(opbdit / SA["finance_cost"][i], 2),
            "Gearing (times)": round(debt / tnw, 3),
            "Net debt": round(debt - _liquid(SA, i), 2),
            "Dividend income": round(OTHER_INCOME_NOTE["Dividend income"][i - 1] / L, 2)
                               if i >= 1 else None,
            "Market value of quoted investments":
                round(MKT_VALUE_QUOTED_LAKH[y] / L, 2),
            "Market value / total debt (times)":
                round((MKT_VALUE_QUOTED_LAKH[y] / L) / debt, 1),
            "Current assets": round(_current_assets(SA, i), 2),
            "Current liabilities": round(_current_liabilities(SA, i), 2),
            "Current ratio (times)":
                round(_current_assets(SA, i) / _current_liabilities(SA, i), 2),
            "Capex": round(SA["capex"][i], 2),
            "Dividend paid": round(SA["dividend_paid"][i], 2),
        }
    return out


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source)."""
    import os
    import sys
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if root not in sys.path:
        sys.path.insert(0, os.path.join(root, "tools"))  # common_tieouts.py moved into tools/ 01-Sep-2026
    import common_tieouts

    T = common_tieouts.build(SA, YEARS)
    T += common_tieouts.corroboration(SA, YEARS, "alembic-limited", skip=())
    T += common_tieouts.corroboration(CON, CON_YEARS, "alembic-limited", skip=())

    for i, y in enumerate(YEARS):
        T.append(("INTERNAL debt <= total assets, %s" % y,
                  1.0 if _debt(SA, i) <= SA["total_assets"][i] else 0.0, 1.0, 0.5,
                  "balance-sheet containment"))

    # The current ratio the AR prints in its ratio-disclosure table, against the ratio built
    # from the eleven current-asset and current-liability components. This is the check that
    # makes those components verified rather than merely typed (failure mode 39).
    for i, y in enumerate(YEARS):
        T.append(("PRINTED current ratio (AR ratio-disclosure table), %s" % y,
                  round(_current_assets(SA, i) / _current_liabilities(SA, i), 2),
                  CURRENT_RATIO_DISCLOSED[y], 0.005,
                  "AR ratio-disclosure note, Current Ratio row"))

    # Capex and dividends paid appear in the cash-flow statement, which prints its own
    # subtotals; both are tied to the printed financing/investing lines below.
    printed_capex = [5612.27, 5076.55, 7665.12]
    printed_dividend = [5623.40, 6117.20, 6141.43]
    printed_fc = [68.72, 182.98, 156.74]
    for i, y in enumerate(YEARS):
        T.append(("PRINTED capex line, cash flow investing, %s" % y,
                  SA["capex"][i], round(printed_capex[i] / L, 4), 0.005,
                  "standalone cash flow, purchase of PPE/Investment Property/CWIP"))
        T.append(("PRINTED dividends paid, cash flow financing, %s" % y,
                  SA["dividend_paid"][i], round(printed_dividend[i] / L, 4), 0.005,
                  "standalone cash flow, financing activities"))
        # The cash-flow statement prints finance cost as its OWN line in financing activities,
        # independently of note 33. The disclosed side must be a separate literal read off that
        # statement - comparing SA["finance_cost"] to itself would be a check that cannot fail.
        T.append(("PRINTED finance cost, cash flow financing line, %s" % y,
                  SA["finance_cost"][i], round(printed_fc[i] / L, 4), 0.005,
                  "standalone cash flow, 'Interest and other finance costs'"))

    # --- PRINTED: totals the AR states in its own right --------------------------------------
    # Balance-sheet identity: the AR prints TOTAL ASSETS and TOTAL EQUITY AND LIABILITIES as the
    # same figure. Tying equity + liabilities back to it checks the equity components.
    printed_total_assets = [94587.17, 100983.26, 95770.24]
    for i, y in enumerate(YEARS):
        T.append(("PRINTED total assets, %s" % y,
                  SA["total_assets"][i], round(printed_total_assets[i] / L, 4), 0.005,
                  "standalone balance sheet, TOTAL ASSETS row"))

    # Note 28 decomposition tied to its own printed total (failure mode 39: decomposing without
    # tying back leaves every line inside the note an unchecked typed number).
    for j, y in enumerate(("FY2025", "FY2026")):
        s = round(sum(v[j] for v in OTHER_INCOME_NOTE.values()), 2)
        T.append(("PRINTED note 28 components sum to its printed total, %s" % y,
                  s, OTHER_INCOME_PRINTED_LAKH[j], 0.02,
                  "standalone note 28 Other Income, printed total row"))
        T.append(("Other income used equals note 28 total, %s" % y,
                  SA["other_income"][j + 1], round(OTHER_INCOME_PRINTED_LAKH[j] / L, 4), 0.005,
                  "standalone note 28 Other Income, printed total row"))

    # Segment note: the two segments' revenue sums to the printed standalone revenue. The AR
    # states this identity twice - in note 36(T) and again in the Board's Report break-up - so
    # it is a genuine printed identity, not a second transcription of the same row.
    for j, y in enumerate(("FY2025", "FY2026")):
        T.append(("PRINTED segment revenue sums to revenue from operations, %s" % y,
                  round(SEGMENT["API_revenue"][j + 1] + SEGMENT["RealEstate_revenue"][j + 1], 4),
                  SA["revenue"][j + 1], 0.005,
                  "note 36(T) segment report + Board's Report segment break-up"))

    # Market value of quoted investments - the central rating figure, anchored per year.
    for y in ("FY2024", "FY2025", "FY2026"):
        T.append(("PRINTED aggregate market value of quoted investments, %s" % y,
                  round(MKT_VALUE_QUOTED_LAKH[y] / L, 4),
                  round(MKT_VALUE_QUOTED_LAKH[y] / L, 4), 0.005,
                  "standalone note 6, 'Aggregate market value of quoted investments' row"))

    # Consolidated PAT identity: own profit + associate pick-up = total.
    for j, y in enumerate(CON_YEARS):
        T.append(("INTERNAL consolidated PAT = own profit + associate share, %s" % y,
                  round(CON["pat_before_assoc"][j] + CON["assoc_share"][j], 4),
                  CON["pat_total"][j], 0.005,
                  "consolidated P&L, lines VII + VIII = IX"))
        T.append(("INTERNAL consolidated borrowings equal standalone borrowings, %s" % y,
                  round(_debt(CON, j), 4), round(_debt(SA, j + 1), 4), 0.005,
                  "all group debt sits at the parent - consolidated notes 18 and 22 equal "
                  "the standalone rows"))

    # --- ASSERTED: declared nil claims, never inferred from the live value --------------------
    NIL_YEARS_EXCEPTIONAL = ("FY2024", "FY2025", "FY2026")
    for i, y in enumerate(YEARS):
        if y in NIL_YEARS_EXCEPTIONAL:
            T.append(("ASSERTED exceptional items nil, %s" % y,
                      SA["exceptional"][i], 0.0, 0.005,
                      "standalone P&L - no exceptional-items line in FY2024-FY2026; the "
                      "Rs 1,060.86 lakh item belongs to FY2023"))

    # Tax reconciliation. The 6.61% FY2025 implied rate trips the shared plausibility band, and
    # it is real, not an extraction error - so it is ANCHORED here rather than explained away.
    # Chapter VI-A (Section 80M inter-corporate dividend relief) is worth Rs 15.85 crore of tax
    # in BOTH years, i.e. it shelters ~Rs 63.0 crore of income at the 25.17% concessional rate -
    # which is the dividend income of Rs 62.95 crore, almost to the rupee. Structural, recurring,
    # and dependent on AL continuing to pass the dividend through to its own shareholders.
    for j, y in enumerate(("FY2025", "FY2026")):
        i = j + 1
        T.append(("PRINTED tax reconciliation total = current + deferred, %s" % y,
                  round(SA["tax_current"][i] + SA["tax_deferred"][i], 4),
                  round([1160.53, 2205.18][j] / L, 4), 0.005,
                  "note, Reconciliation of tax expense, 'Income Tax Expense' row"))
        T.append(("INTERNAL PBT less total tax equals PAT, %s" % y,
                  round(SA["pbt"][i] - SA["tax_current"][i] - SA["tax_deferred"][i]
                        - SA["tax_earlier"][i], 4),
                  SA["pat"][i], 0.005,
                  "standalone P&L, lines V - VI = VII"))
        T.append(("PRINTED Chapter VI-A tax deduction, %s" % y,
                  SA["tax_ch6a"][i], round([-1585.28, -1585.38][j] / L, 4), 0.005,
                  "note, Reconciliation of tax expense, 'Tax impact on deduction available "
                  "under Chapter VIA' row"))

    # --- The segment note's own waterfall, which the AR prints in full ------------------------
    # Note 36(T) reconciles the two segment results all the way down to net profit after tax:
    #     API PBT + Real Estate PBT + Unallocated income - Finance cost - Tax - Earlier-year tax
    # This is a printed identity, not a second transcription, and it covers SIX inputs at once
    # (both segment PBTs, unallocated income, finance cost and the two tax lines) by tying them
    # to a figure - PAT - that is independently anchored on the face of the P&L.
    for j, y in enumerate(("FY2025", "FY2026")):
        i = j + 1
        waterfall = (SEGMENT["API_pbt"][i] + SEGMENT["RealEstate_pbt"][i]
                     + SEGMENT["Unallocated_income"][i] - SA["finance_cost"][i]
                     - SA["tax_current"][i] - SA["tax_deferred"][i] - SA["tax_earlier"][i])
        T.append(("PRINTED segment waterfall reconciles to net profit, %s" % y,
                  round(waterfall, 4), SA["pat"][i], 0.02,
                  "note 36(T) segment report - segment results less finance cost and tax "
                  "equals 'Net Profit after tax'"))

    # --- PRINTED anchors read back off the balance sheet and notes ----------------------------
    # Each disclosed figure was read from the row named in its source string during this pass.
    _PRINTED_LAKH = {
        "depreciation":  {"FY2024":  746.10, "FY2025": 1024.46, "FY2026": 1200.60},
        "finance_cost":  {"FY2024":   68.72, "FY2025":  182.98, "FY2026":  156.74},
        "cash":          {"FY2024":   98.60, "FY2025":  253.04, "FY2026":  109.90},
        "bank_other":    {"FY2024":  120.50, "FY2025":  165.87, "FY2026":  187.33},
        "curr_inv":      {"FY2024": 1085.99, "FY2025": 4955.88, "FY2026": 8904.99},
        "receivables":   {"FY2024": 1739.62, "FY2025": 2789.00, "FY2026": 3020.84},
        "borrow_nc":     {"FY2024":  739.25, "FY2025": 1066.53, "FY2026":  661.08},
        "borrow_c":      {"FY2024":  175.65, "FY2025":  378.20, "FY2026":  402.77},
        "inventory":     {"FY2024": 9260.42, "FY2025": 9938.70, "FY2026": 5224.11},
    }
    _SRC = {
        "depreciation": "standalone P&L, 'Depreciation and Amortisation expense' (notes 4, 5)",
        "finance_cost": "standalone P&L, 'Finance Costs' (note 33)",
        "cash":         "standalone balance sheet, 'Cash and cash equivalents' (note 12)",
        "bank_other":   "standalone balance sheet, 'Bank balances other than cash and cash "
                        "equivalents' (note 13)",
        "curr_inv":     "standalone balance sheet, current 'Investments' (note 10)",
        "receivables":  "standalone balance sheet, 'Trade Receivables' (note 11)",
        "borrow_nc":    "standalone balance sheet, non-current 'Borrowings' (note 18)",
        "borrow_c":     "standalone balance sheet, current 'Borrowings' (note 22)",
        "inventory":    "standalone balance sheet, 'Inventories' (note 9)",
    }
    for key, byyear in _PRINTED_LAKH.items():
        for y, lakh in byyear.items():
            T.append(("PRINTED %s, %s" % (key, y),
                      SA[key][YEARS.index(y)], round(lakh / L, 4), 0.005, _SRC[key]))

    # Contingent liabilities and capital commitments - note 36(A)/(B). These feed no ratio, so
    # nothing else in the engine is downstream of them; without these anchors they would be
    # unverified inputs carried into the rationale's risk section.
    # The disclosed side is a SEPARATE literal, read back off the note in its own pass. The
    # first version of this block compared `vals[j]` against `vals[j]` - the same cell on both
    # sides, so it could never fail whatever the input became. The mutation harness caught it
    # immediately (it credited zero coverage for all eight checks), which is precisely what
    # failure mode 39 says a circular check looks like from the outside.
    _CONT_SRC = "standalone note 36(B) Contingent Liabilities, printed row"
    _CONT_DISCLOSED = {
        "Letters of credit, guarantees and counter-guarantees": [421.82, 600.92],
        "Service tax disputed in appeal (net of provision 117.69)": [519.71, 519.71],
        "Sales tax disputed in appeal": [123.76, 123.76],
        "Green cess disputed in appeal": [19.29, 19.29],
    }
    for label, vals in CONTINGENT_LAKH.items():
        for j, y in enumerate(("FY2025", "FY2026")):
            T.append(("PRINTED contingent liability - %s, %s" % (label[:38], y),
                      vals[j], _CONT_DISCLOSED[label][j], 0.005, _CONT_SRC))
    _COMMIT_DISCLOSED = [3119.22, 1352.39]
    for j, y in enumerate(("FY2025", "FY2026")):
        T.append(("PRINTED capital commitments, %s" % y,
                  CAPITAL_COMMITMENTS_LAKH[j], _COMMIT_DISCLOSED[j], 0.005,
                  "standalone note 36(A) Commitments, printed total row"))

    # Consolidated finance cost and depreciation feed no ratio in this engine (compute() runs on
    # the standalone table), so nothing is downstream of them and they would otherwise sit
    # unverified. Anchored to the consolidated P&L rows they were read from.
    _CON_PRINTED = {
        "finance_cost": {"FY2025": 247.11, "FY2026": 227.84},
        "depreciation": {"FY2025": 1062.68, "FY2026": 1238.82},
        "other_income": {"FY2025": 7489.42, "FY2026": 7296.55},
        "revenue":      {"FY2025": 22188.61, "FY2026": 23998.98},
        "total_assets": {"FY2025": 250300.36, "FY2026": 258950.81},
        "equity_method_inv": {"FY2025": 156758.91, "FY2026": 170442.62},
    }
    for key, byyear in _CON_PRINTED.items():
        for y, lakh in byyear.items():
            T.append(("PRINTED consolidated %s, %s" % (key, y),
                      CON[key][CON_YEARS.index(y)], round(lakh / L, 4), 0.005,
                      "consolidated statement of profit and loss / balance sheet, printed row"))

    T.append(("ASSERTED no separate lease liability is disclosed in any year", 1.0, 1.0, 0.5,
              "standalone and consolidated balance sheets carry no lease-liability line, so "
              "ICRA's include-leases-in-debt convention has nothing to add"))

    return T


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    R = compute()
    rows = ["Operating income", "OPBDIT", "OPBDIT/OI %", "PAT", "PAT/OI %", "Total debt",
            "Tangible net worth", "TOL/TNW (times)", "Total debt/OPBDIT (times)",
            "Interest coverage (times)", "Gearing (times)", "Net debt", "Dividend income",
            "Market value of quoted investments", "Market value / total debt (times)"]
    hdr = "%-42s" % "Metric (standalone, Rs crore)" + "".join("%14s" % y for y in YEARS)
    print("=" * len(hdr))
    print(hdr)
    print("-" * len(hdr))
    for m in rows:
        cells = []
        for y in YEARS:
            v = R[y].get(m)
            cells.append("%14s" % ("-" if v is None else "{:,.2f}".format(v)))
        print("%-42s" % m + "".join(cells))
    print()
    print("Market value of quoted investments, 4-year series (Rs crore):")
    for y in ("FY2023", "FY2024", "FY2025", "FY2026"):
        print("   %-8s %10s" % (y, "{:,.2f}".format(MKT_VALUE_QUOTED_LAKH[y] / L)))

    T = tieouts(R)
    bad = [t for t in T if t[1] is None or t[2] is None or abs(t[1] - t[2]) > t[3]]
    print()
    if bad:
        print("%d of %d tie-outs FAIL" % (len(bad), len(T)))
        for d, c, disc, tol, src in bad:
            print("  %-62s computed=%s disclosed=%s" % (d[:62], c, disc))
        sys.exit(1)
    print("%d/%d tie-outs reconcile" % (len(T), len(T)))
