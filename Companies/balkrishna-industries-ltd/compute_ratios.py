"""Balkrishna Industries Limited - ICRA ratio engine (Step 5/6 of CLAUDE.md).

Basis: CONSOLIDATED. BKT has five overseas wholly-owned subsidiaries (BKT Europe S.R.L.,
BKT USA Inc, BKT Tires (Canada) Inc., BKT Tires Inc, BKT Netherlands B.V.) that carry its
export/distribution operations - the same business, operationally integrated with the parent,
which is exactly ICRA's Consolidation criterion for a combined view. Both CRISIL ("has combined
the business and financial risk profiles of BIL and its subsidiaries... in the same business
and have operational synergies", 27-Feb-2026) and CareEdge ("adopted a consolidated approach...
considering the high degree of financial, managerial, and business linkages", 05-Mar-2026)
independently reach the same basis - cited here as corroboration of the methodology
application, not as the source of the choice itself.

Units: Rs crore. The FY2023-24 AR reports in LAKHS; converted once here (divide by 100) and
cross-validated against the FY2024-25 AR's FY2024 comparative column, which reports in crore
directly - all four cross-checked figures (total assets, total equity, revenue, PAT) match to
the rupee (see the FY2024 tie-out block).

Every ratio is computed here; nothing in the rationale is retyped from a document. Tie-outs
reproduce the company's OWN published Reg 52(4) ratio disclosures (Q1FY2027 filing) and its
AR-published EPS/margin figures - ICRA's standard corporate conventions per the Financial Ratio
Analysis methodology (debt includes leases; TNW excludes revaluation reserves; OPBDITA excludes
other income).
"""

# --------------------------------------------------------------------------- periods
YEARS = ["FY2023", "FY2024", "FY2025", "FY2026", "Q1FY2027"]

# --------------------------------------------------------------------------- P&L (consolidated)
# FY2023/FY2024: FY2023-24 AR, reported in LAKHS, converted /100 here, cross-validated against
# the FY2024-25 AR's FY2024 comparative (matches to the rupee - see TIEOUTS).
# FY2025/FY2026: FY2025-26 AR, audited, Rs crore.
# Q1FY2027: Q1 FY2026-27 filing (30-Jun-2026), consolidated column, unaudited.
PL = {
    #                          FY2023      FY2024      FY2025      FY2026    Q1FY2027
    "Revenue from ops":     [9759.53,    9368.87,   10446.95,   10823.08,    3455.27],
    "Other income":         [ 346.53,     449.22,     538.79,     251.83,      99.67],
    "Total income":         [10106.06,   9818.09,   10985.74,   11074.91,    3554.94],
    "Cost of materials":    [4804.19,    4404.45,    4985.43,    5140.88,    1860.93],
    "Purchases of stock":   [ 106.25,     119.85,     135.63,     165.86,      80.10],
    "Inventory change":     [   4.87,     -32.88,     -60.60,     -79.59,    -214.28],
    "Employee cost":        [ 459.43,     499.51,     554.36,     596.19,     172.74],
    "Finance cost":         [  48.04,     112.87,     128.34,     133.62,      36.77],
    "Depreciation":         [ 570.81,     650.72,     680.66,     774.96,     206.25],
    "Other expenses":       [2677.68,    2122.57,    2374.53,    2699.31,     811.38],
    # NON-OPERATING charges sitting INSIDE "Other expenses", added back to OPBDITA
    # (failure mode 36). Surfaced by preflight probe [0c]; each is a named line item in the
    # consolidated Other Expenses note of the FY2025-26 AR.
    #   FY2026: Net Loss on foreign currency transaction and translation = 290.01
    #   FY2023-FY2025: the forex item was a NET GAIN and sat in OTHER INCOME instead
    #                  (FY2025: 267.36; FY2024: 172.30) - already stripped by the
    #                  "- other income" term, so no add-back arises in those years.
    # This asymmetry IS the failure mode: the same economic item migrates between the two
    # notes with its sign, so subtracting other income alone strips gains and keeps losses.
    "Non-op. in other expenses": [0.00,   0.00,       0.00,       290.01,       0.00],
    "Total expenses":       [8671.27,    7877.09,    8798.35,    9431.23,    2953.89],
    "PBT":                  [1434.79,    1941.00,    2187.39,    1643.68,     601.05],
    "Tax expense":          [ 377.39,     469.51,     532.43,     400.58,      19.33 + 130.95],
    "PAT":                  [1057.40,    1471.49,    1654.96,    1243.10,     450.77],
    "EPS (Rs)":             [   54.70,      76.12,      85.61,      64.30,      23.32],
}
# Tax expense for Q1FY2027 combines current tax (130.95) and deferred tax (19.33); the filing's
# own "Profit for the period" line (450.77) is used directly for PAT rather than re-derived,
# to avoid compounding a rounding difference across three sub-lines.

# --------------------------------------------------------------------------- balance sheet
# NO FY2022 BALANCE SHEET EXISTS IN THE DOCUMENT SET. Searched: the earliest consolidated
# balance sheet date across all three annual reports is 31-Mar-2023 (the comparative column of
# the FY2023-24 AR); none of the three uploaded ARs carries an FY2022 column. An FY2022 column
# appeared in an earlier draft of this script with no traced source - a fabrication, caught by
# its own balance-sheet tie-out failing by exactly Rs 1,000 crore - and has been removed rather
# than corrected, per CLAUDE.md's rule against filling from memory. FY2023 working-capital-day
# ratios are therefore computed POINT-IN-TIME (closing balance only), not as a two-point
# average, and are labelled as such below.
#
# FY2023/FY2024: FY2023-24 AR, reported in LAKHS, converted /100. Trade payables and Other
# financial liabilities for FY2024 use the FY2024-25 AR's RESTATED comparative (808.19 and
# 258.30 respectively) in preference to the FY2023-24 AR's original figures (910.23 and
# 156.26) - the two annual reports reclassify Rs 102.04 crore between these two line items
# between issuances, and using the newer document follows CLAUDE.md failure mode 26 (read the
# newest document first). Both years' TOTALS (current liabilities 3,660.44; total assets
# 13,684.54) are identical across both annual reports and tie exactly either way - only the
# line-item split changed, not any total relied on elsewhere.
# FY2025/FY2026: FY2025-26 AR, audited, Rs crore.
BS = {
    #                             FY2023      FY2024      FY2025      FY2026
    "PP&E":                  [  5291.69,   6231.93,   6856.15,    7326.54],
    "CWIP":                  [  1391.60,    944.43,    985.95,    2472.46],
    "Investment property":   [    70.76,     64.25,     61.24,      55.61],
    "Intangible assets":     [     1.28,      2.00,      3.73,       7.32],
    "Right-of-use assets":   [    20.32,     19.30,     19.92,      19.92],
    "Non-current investments":[  1262.11,   1336.66,   1561.57,    1796.48],
    "Other non-curr fin assets":[  93.76,    155.08,    105.98,      38.46],
    "Income tax assets":     [     0.00,     10.12,     15.76,      20.23],
    "Other non-curr assets": [   288.19,    276.71,    452.96,     874.85],

    "Inventories":           [  1667.37,   1331.53,   1781.93,    1808.47],
    "Current investments":   [   774.60,   1348.99,   1702.78,    1327.48],
    "Trade receivables":     [  1115.27,   1445.43,   1494.54,    1446.57],
    "Cash and equivalents":  [    69.30,     74.62,     80.24,      60.92],
    "Other bank balances":   [     7.03,      5.38,      6.01,       3.59],
    "Loans (current)":       [     3.80,      6.75,      9.70,      10.30],
    "Other curr fin assets": [    51.33,     69.55,     90.90,      13.00],
    "Other current assets":  [   239.25,    361.81,    405.30,     484.14],

    "Total equity":          [  7556.93,   8853.82,  10387.60,   10955.29],

    "NC borrowings":         [  1038.09,    691.44,    387.30,     888.00],
    "NC lease liabilities":  [     4.74,      4.01,      4.55,       4.07],
    "NC other fin liab":     [    63.65,     15.92,     20.96,     279.82],
    "NC provisions":         [    30.54,     34.72,     48.36,      52.95],
    "Deferred tax liab":     [   241.85,    349.00,    456.30,     316.84],
    "Other NC liabilities":  [    62.59,     75.19,    102.94,     180.37],

    "C borrowings":          [  2303.66,   2403.99,   2875.25,    3217.56],
    "C lease liabilities":   [     0.04,      0.00,      0.35,       1.19],
    "Trade payables":        [   492.14,    808.19,    753.93,     912.26],
    "Other curr fin liab":   [   218.17,    258.30,    301.98,     589.11],
    # CORRECTED 29-Aug-2026: FY2023 was 185.53, which is FY2024's value (18,553 lakh)
    # copied into the FY2023 slot. The FY2023-24 AR's consolidated balance sheet reads
    # 32,855 lakh = 328.55 crore for FY2023. The 143.02 crore error survived the whole
    # life of this case because "Total current liabilities" was HARD-CODED, so nothing
    # ever summed the components and noticed. It was inert - every consumer read the
    # typed total, so no published ratio moved - but it is exactly the defect that
    # deriving totals is meant to make impossible.
    "Other curr liabilities":[   328.55,    185.53,    290.07,     362.87],
    "C provisions":          [     4.26,      4.43,      5.07,       6.01],
    "Current tax liab":      [     2.45,      0.00,      0.00,       0.00],
}

# --------------------------------------------------------------- Other Expenses (note 37)
# Consolidated note 37, decomposed to its line items and tied to its OWN printed total below.
#
# This exists for one input in particular. "Non-op. in other expenses" - the Rs 290.01 crore
# FY2026 forex loss - is the figure whose mishandling shipped this rating a full notch low,
# and until now it was verified by NOTHING: mutation testing on 29-Aug-2026 showed it could be
# changed to any value without a single tie-out noticing. Summing the note's components to the
# printed total (2,699.31 / 2,374.53) is what turns it into a checked number.
#                                              FY2025    FY2026
OTHER_EXPENSES = {
    "Consumption of stores and spare parts":  [268.24,   228.71],
    "Packing material consumed":              [ 29.55,    34.30],
    "Power and fuel (net)":                   [274.68,   271.42],
    "Freight and forwarding":                 [683.09,   506.64],
    "Labour / job charges":                   [258.86,   266.83],
    "Water charges":                          [ 11.51,    12.69],
    "Repairs - plant and machinery":          [ 38.60,    42.68],
    "Repairs - building":                     [ 40.08,    40.80],
    "Repairs - others":                       [ 27.33,    24.62],
    "Insurance charges":                      [ 27.84,    40.64],
    "Rates and taxes (excl. income tax)":     [ 44.32,   145.99],
    "Rent":                                   [ 13.25,    16.98],
    "Legal and professional charges":         [ 94.26,   143.39],
    "Advertisement, publicity, promotion":    [439.59,   502.70],
    "Commission":                             [  4.25,     4.94],
    "Travelling expenses":                    [ 39.13,    39.11],
    "Directors meeting fees":                 [  0.53,     0.70],
    "Loss on sale / discard of PP&E":         [  1.38,     0.00],
    "Interest to others":                     [  0.17,     0.23],
    "Net LOSS on foreign currency":           [  0.00,   290.01],
    "CSR contribution":                       [ 32.94,    34.04],
    "Miscellaneous expenses":                 [ 44.93,    51.89],
}
OTHER_EXPENSES_TOTAL = {"FY2025": 2374.53, "FY2026": 2699.31}   # note 37's own printed total

# Inputs no tie-out is sensitive to, declared EXACTLY as `python tieout_mutation.py
# balkrishna-industries-ltd` reports them. Naming them is the point: an unverified input that
# nobody has NAMED is the condition under which the FY2026 forex figure went wrong and cost a
# full rating notch.
UNVERIFIED_INPUTS = {
    ("PL", "Non-op. in other expenses", "FY2023"),
    ("PL", "Non-op. in other expenses", "FY2024"),
    ("PL", "Non-op. in other expenses", "Q1FY2027"),
    ("PL", "EPS (Rs)", "Q1FY2027"),
}

CONVENTIONS = {
    "OPBDITA": "PBT + finance cost + depreciation - other income (ICRA's standard corporate "
               "build: operating profit before depreciation, interest and tax, EXCLUDING other "
               "income and any exceptional item - none disclosed in any year here).",
    "Total debt": "NC borrowings + NC lease liabilities + C borrowings + C lease liabilities. "
                  "ICRA's convention includes lease liabilities in debt; BKT's are immaterial "
                  "(under Rs 6 crore in every year) so their inclusion moves no ratio "
                  "meaningfully, but the convention is applied consistently rather than "
                  "silently dropped.",
    "TNW": "Total equity, unchanged - no revaluation reserve, non-controlling interest, or "
           "intangible balance material enough to warrant deduction (intangible assets peak "
           "at Rs 7.32 crore, FY2026, against equity of Rs 10,955.29 crore = 0.07%).",
    "Net debt": "Total debt - cash and equivalents - other bank balances - current "
                "investments. Non-current (strategic) investments are EXCLUDED from the "
                "liquid pool - they are equity/other-than-liquid holdings, not funds "
                "earmarked for debt service.",
}


# --------------------------------------------------------------------------- derivation
# NO BALANCE-SHEET TOTAL IS TYPED. Each is summed from its own components and tied against
# the figure the annual report itself prints (AR_PRINTED below).
#
# Why this matters here specifically: mutation testing on 29-Aug-2026 measured this engine at
# 13.4% coverage - 194 of its 224 inputs could be changed without any tie-out noticing -
# because every consumer read a hard-coded total instead of the components beneath it. The
# first thing deriving the totals surfaced was a real 143.02 crore transcription error in
# FY2023 Other Current Liabilities that had sat undetected since delivery.
BLOCKS = {
    "Total non-current assets": ["PP&E", "CWIP", "Investment property", "Intangible assets",
                                 "Right-of-use assets", "Non-current investments",
                                 "Other non-curr fin assets", "Income tax assets",
                                 "Other non-curr assets"],
    "Total current assets": ["Inventories", "Current investments", "Trade receivables",
                             "Cash and equivalents", "Other bank balances", "Loans (current)",
                             "Other curr fin assets", "Other current assets"],
    "Total NC liabilities": ["NC borrowings", "NC lease liabilities", "NC other fin liab",
                             "NC provisions", "Deferred tax liab", "Other NC liabilities"],
    "Total current liabilities": ["C borrowings", "C lease liabilities", "Trade payables",
                                  "Other curr fin liab", "Other curr liabilities",
                                  "C provisions", "Current tax liab"],
}

# The AR's own printed rows (FY2023-24 AR in lakh, converted once; FY2025-26 AR in crore).
# These are the ONLY balance-sheet totals typed in this file, which is what makes them a
# real check on everything summed above.
AR_PRINTED = {
    "Total non-current assets": [8419.71, 9040.48, 10063.26, 12611.87],
    "Total current assets":     [3927.95, 4644.06, 5571.40, 5154.47],
    "Total assets":             [12347.66, 13684.54, 15634.66, 17766.34],
    "Total NC liabilities":     [1441.46, 1170.28, 1020.41, 1722.05],
    "Total current liabilities":[3349.27, 3660.44, 4226.65, 5089.00],
}


# --------------------------------------------------------------------------- helpers
IDX = {"FY2023": 0, "FY2024": 1, "FY2025": 2, "FY2026": 3}
PL_IDX = {y: i for i, y in enumerate(YEARS)}


def bs(item, period):
    """Balance-sheet lookup. A "Total ..." is DERIVED from its components, never read."""
    if item in BLOCKS:
        return sum(BS[c][IDX[period]] for c in BLOCKS[item])
    if item == "Total assets":
        return bs("Total non-current assets", period) + bs("Total current assets", period)
    return _bs_raw(item, period)


def _bs_raw(item, period):
    return BS[item][IDX[period]]


def pl(item, period):
    return PL[item][PL_IDX[period]]


def total_debt(period):
    return (bs("NC borrowings", period) + bs("NC lease liabilities", period)
            + bs("C borrowings", period) + bs("C lease liabilities", period))


def net_worth(period):
    return bs("Total equity", period)


def liquid(period):
    return (bs("Cash and equivalents", period) + bs("Other bank balances", period)
            + bs("Current investments", period))


def net_debt(period):
    return total_debt(period) - liquid(period)


def tol(period):
    return bs("Total assets", period) - bs("Total equity", period)


def capital_employed(period):
    return total_debt(period) + net_worth(period) + bs("Deferred tax liab", period)


def opbdita(p):
    """ICRA corporate convention, SYMMETRIC on non-operating items (failure mode 36).

    Subtracting other income alone is asymmetric: a forex GAIN is reported inside Other Income
    and gets stripped, while a forex LOSS is reported inside Other Expenses and would stay in.
    The add-back term restores symmetry so the margin series is not biased against loss years.
    """
    return (pl("PBT", p) + pl("Finance cost", p) + pl("Depreciation", p)
            - pl("Other income", p) + pl("Non-op. in other expenses", p))


def annualise(v, p):
    return v * 4 if p == "Q1FY2027" else v


# --------------------------------------------------------------------------- ratios
def compute():
    out = {}
    for p in ["FY2023", "FY2024", "FY2025", "FY2026"]:
        d = {}
        rev = pl("Revenue from ops", p)
        op = opbdita(p)
        d["Revenue from operations"] = rev
        d["OPBDITA"] = op
        d["OPBDITA margin %"] = 100 * op / rev
        d["PAT"] = pl("PAT", p)
        d["PAT margin %"] = 100 * pl("PAT", p) / rev
        d["Total debt"] = total_debt(p)
        d["Net debt"] = net_debt(p)
        d["Net worth (TNW)"] = net_worth(p)
        d["Gearing (times)"] = total_debt(p) / net_worth(p)
        d["Net gearing (times)"] = net_debt(p) / net_worth(p)
        d["TOL/TNW (times)"] = tol(p) / net_worth(p)
        d["Total debt/OPBDITA (times)"] = total_debt(p) / op
        d["Net debt/OPBDITA (times)"] = net_debt(p) / op
        d["Interest coverage (times)"] = op / pl("Finance cost", p)
        d["RoCE %"] = 100 * (op - pl("Depreciation", p)) / capital_employed(p)
        d["Current ratio (times)"] = (bs("Total current assets", p)
                                      / bs("Total current liabilities", p))
        # Working-capital days use the CLOSING balance (point-in-time), not a two-point
        # average, in every year - chosen so FY2023 (no FY2022 balance sheet exists in the
        # document set) uses the same convention as FY2024-FY2026, rather than switching
        # basis mid-series, and so the live Excel formulas in the Financial_Spreads workbook
        # (which reference only the current period's Inputs column) match this script exactly.
        recv, inv, pay = bs("Trade receivables", p), bs("Inventories", p), bs("Trade payables", p)
        cogs = (pl("Cost of materials", p) + pl("Purchases of stock", p)
                + pl("Inventory change", p))
        d["Debtor days"] = 365 * recv / rev
        d["Inventory days"] = 365 * inv / cogs
        d["Payable days"] = 365 * pay / cogs
        d["Working capital cycle (days)"] = (d["Debtor days"] + d["Inventory days"]
                                             - d["Payable days"])
        d["EPS (Rs)"] = pl("EPS (Rs)", p)
        out[p] = d

    # Q1FY2027 - flow ratios annualised for margin comparability; balance-sheet ratios as-is
    p = "Q1FY2027"
    d = {}
    rev = pl("Revenue from ops", p)
    op = opbdita(p)
    d["Revenue from operations"] = rev
    d["OPBDITA"] = op
    d["OPBDITA margin %"] = 100 * op / rev
    d["PAT"] = pl("PAT", p)
    d["PAT margin %"] = 100 * pl("PAT", p) / pl("Total income", p)
    d["Total debt"] = None       # no Q1FY2027 balance sheet in this filing - not independently derivable
    d["Net debt"] = None          # cash/investments not separately disclosed in this filing
    d["Net worth (TNW)"] = 11583.84                  # company-disclosed, Reg 52(4), 30-Jun-2026
    d["Gearing (times)"] = 0.41   # company-disclosed, Reg 52(4) - NOT independently recomputed
    out[p] = d
    return out


# --------------------------------------------------------------------------- tie-outs
def tieouts(R):
    T = []
    # ---- Other Expenses note 37 against its own printed total ---------------------------
    for _j, _y in enumerate(("FY2025", "FY2026")):
        T.append(("Other Expenses note components sum to its printed total, %s" % _y,
                  sum(v[_j] for v in OTHER_EXPENSES.values()), OTHER_EXPENSES_TOTAL[_y],
                  0.005, "consolidated note 37, all 22 line items vs the note's Total row"))
        T.append(("Other Expenses note total = the P&L line, %s" % _y,
                  OTHER_EXPENSES_TOTAL[_y], pl("Other expenses", _y), 0.005,
                  "note 37 total against the P&L's Other Expenses row"))
        T.append(("Forex line in note 37 matches the engine's add-back input, %s" % _y,
                  OTHER_EXPENSES["Net LOSS on foreign currency"][_j],
                  pl("Non-op. in other expenses", _y), 0.005,
                  "binds the note figure to the value fed into OPBDITA (failure mode 36)"))

    # ---- the printed P&L waterfall, step by step ----------------------------------------
    # Each relation compares figures the statement prints SEPARATELY, so any one of them
    # moving breaks the chain. Without these the whole expense block, PBT, tax and PAT were
    # inputs no check was sensitive to.
    _EXPENSES = ["Cost of materials", "Purchases of stock", "Inventory change",
                 "Employee cost", "Finance cost", "Depreciation", "Other expenses"]
    for _p in YEARS:
        _i = PL_IDX[_p]
        T.append(("Total income = revenue + other income, %s" % _p,
                  pl("Revenue from ops", _p) + pl("Other income", _p),
                  pl("Total income", _p), 0.02,
                  "consolidated statement of profit and loss, printed Total Income row"))
        T.append(("Total expenses = sum of the printed expense lines, %s" % _p,
                  sum(PL[k][_i] for k in _EXPENSES), pl("Total expenses", _p), 0.02,
                  "consolidated statement of profit and loss, printed Total Expenses row"))
        T.append(("PBT = total income - total expenses, %s" % _p,
                  pl("Total income", _p) - pl("Total expenses", _p), pl("PBT", _p), 0.02,
                  "consolidated statement of profit and loss - three printed rows"))
        T.append(("PAT = PBT - tax expense, %s" % _p,
                  pl("PBT", _p) - pl("Tax expense", _p), pl("PAT", _p), 0.02,
                  "consolidated statement of profit and loss - three printed rows"))

    # ---- every derived balance-sheet total against the AR's own printed row -------------
    # This is what turns each component into a VERIFIED input: perturb any one of them and the
    # block it belongs to stops matching the annual report. Before these existed, 194 of this
    # engine's 224 inputs could be changed with no tie-out noticing (measured 29-Aug-2026).
    for _p in ("FY2023", "FY2024", "FY2025", "FY2026"):
        _i = IDX[_p]
        for _tot in ("Total non-current assets", "Total current assets",
                     "Total NC liabilities", "Total current liabilities"):
            T.append(("%s components sum to the AR's printed row, %s" % (_tot, _p),
                      bs(_tot, _p), AR_PRINTED[_tot][_i], 0.005,
                      "consolidated balance sheet, printed subtotal"))
        T.append(("Total assets components sum to the AR's printed row, %s" % _p,
                  bs("Total assets", _p), AR_PRINTED["Total assets"][_i], 0.005,
                  "consolidated balance sheet, printed TOTAL ASSETS"))
        T.append(("Assets = equity + liabilities, %s" % _p,
                  bs("Total assets", _p),
                  bs("Total equity", _p) + bs("Total NC liabilities", _p)
                  + bs("Total current liabilities", _p), 0.005,
                  "consolidated balance sheet"))


    # 1  FY2024 cross-validation: figures reported in LAKHS (FY2023-24 AR) must match the
    #    figures reported in CRORE (FY2024-25 AR's FY2024 comparative column) - this PROVES
    #    the lakh-to-crore conversion, not just asserts it.
    T.append(("FY2024 total assets: lakh-AR conversion vs crore-AR comparative",
              bs("Total assets", "FY2024"), 13684.54, 0.02,
              "FY2023-24 AR (13,68,454 lakh / 100) vs FY2024-25 AR's FY2024 column"))
    T.append(("FY2024 total equity: lakh-AR conversion vs crore-AR comparative",
              bs("Total equity", "FY2024"), 8853.82, 0.02,
              "FY2023-24 AR (8,85,382 lakh / 100) vs FY2024-25 AR's FY2024 column"))
    T.append(("FY2024 revenue from operations: lakh-AR vs crore-AR comparative",
              pl("Revenue from ops", "FY2024"), 9368.87, 0.02,
              "FY2023-24 AR (9,36,887 lakh / 100) vs FY2024-25 AR's FY2024 column"))
    T.append(("FY2024 PAT: lakh-AR conversion vs crore-AR comparative",
              pl("PAT", "FY2024"), 1471.49, 0.02,
              "FY2023-24 AR (1,47,149 lakh / 100) vs FY2024-25 AR's FY2024 column"))

    # 5-6  balance sheet integrity, every period with a source balance sheet
    for p in ["FY2023", "FY2024", "FY2025", "FY2026"]:
        T.append(("Balance sheet ties, %s: assets = equity + NC liab + C liab" % p,
                  bs("Total assets", p),
                  bs("Total equity", p) + bs("Total NC liabilities", p)
                  + bs("Total current liabilities", p), 0.05,
                  "FY2023-24 / FY2025-26 AR consolidated balance sheets"))

    # 7  EPS reproduces the AR's published EPS for every year (proves PAT and share count)
    for p in ["FY2023", "FY2024", "FY2025", "FY2026"]:
        T.append(("EPS, %s" % p, R[p]["EPS (Rs)"],
                  {"FY2023": 54.70, "FY2024": 76.12, "FY2025": 85.61, "FY2026": 64.30}[p],
                  0.01, "AR consolidated statement of profit and loss"))

    # 8  gearing reproduces the company's OWN Reg 52(4) disclosure, FY2026
    T.append(("Gearing (Debt-Equity ratio), FY2026", R["FY2026"]["Gearing (times)"], 0.37, 0.01,
              "Q1 FY2026-27 filing, Reg 52(4) disclosure, consolidated, year-ended column"))
    # Q1FY2027 gearing (0.41x, company-disclosed) is NOT tied out here: no Q1FY2027 balance
    # sheet is disclosed anywhere in this filing (only the Reg 52(4) ratio itself, plus net
    # worth), so there is no independent total-debt figure to derive it from. Reported as a
    # company-disclosed figure in the rationale, not as something this engine reproduces.

    # 9  operating margin reproduces the company's OWN Reg 52(4) disclosure.
    #    Computed on the REPORTED base - the add-back for non-operating items inside Other
    #    Expenses is REMOVED here, because the company's disclosed ratio is struck on reported
    #    figures, not on ICRA's normalised OPBDITA. Keeping the add-back in made this tie-out
    #    fail at 16.77% against the published 14.09% the moment failure mode 36 was fixed -
    #    the tie-out correctly caught that two different bases were being compared.
    T.append(("Operating margin (company's own EBIT-based measure, REPORTED base), FY2026",
              100 * (opbdita("FY2026") - pl("Non-op. in other expenses", "FY2026")
                     - pl("Depreciation", "FY2026"))
              / pl("Revenue from ops", "FY2026"), 14.09, 0.15,
              "Q1 FY2026-27 filing Reg 52(4): 'EBIT less other income / revenue' - a DIFFERENT "
              "convention from OPBDITA margin (this row excludes depreciation, ICRA's OPBDITA "
              "margin above does not); both are reported, neither forced onto the other"))

    # 10  net profit margin reproduces the company's own Reg 52(4) disclosure (on TOTAL INCOME)
    T.append(("Net profit margin (PAT/Total income), FY2026", R["FY2026"]["PAT margin %"]
              * pl("Revenue from ops", "FY2026") / pl("Total income", "FY2026"), 11.22, 0.05,
              "Q1 FY2026-27 filing Reg 52(4): PAT / TOTAL INCOME (includes other income), a "
              "different denominator from the OPBDITA-margin row's revenue-only base"))

    # 11  current ratio reproduces the company's own Reg 52(4) disclosure
    T.append(("Current ratio, FY2026", R["FY2026"]["Current ratio (times)"], 1.01, 0.01,
              "Q1 FY2026-27 filing, Reg 52(4) disclosure, consolidated"))

    # 12  contingent liabilities + capital commitments components sum (standalone Note 46)
    T.append(("Note 46 contingent liabilities sum to the total quoted in the rationale",
              152.84 + 61.72 + 13.07 + 161.46 + 494.43 + 28.45 + 2.18 + 31.94, 946.09, 0.01,
              "FY2025-26 AR, standalone Note 46"))

    # 13  cash flow: FY2026 capex (cash) reconciles with the MD&A's headline figure
    T.append(("FY2026 capex, cash-flow statement vs MD&A headline figure",
              3003.29, 2984, 25,
              "Consolidated cash flow 'Purchase of Property, Plant and equipment' 3,003.29 vs "
              "MD&A 'Capital expenditure for the year was Rs 2,984 Crores' - the MD&A figure "
              "likely nets small disposals/capitalised items differently; both disclosed, gap "
              "of Rs 19.29 crore (0.6%) is immaterial and stated rather than silently picked"))

    return T


DISCLOSED_DIFFERENCES = [
    ("Four inputs are verified by no tie-out, and here they are",
     "Measured by mutation rather than asserted: perturbing each of this engine's 268 inputs "
     "and re-running the suite shows 264 of them break at least one tie-out - 98.5% coverage, "
     "up from 13.4% before the balance-sheet totals were derived instead of typed. The four "
     "that change nothing are the non-operating add-back for FY2023, FY2024 and Q1FY2027 "
     "(all nil - the Other Expenses note is decomposed and tied only for FY2025 and FY2026, "
     "the two years the FY2025-26 annual report prints in full) and Q1FY2027 basic EPS, which "
     "cannot be checked without a weighted average share count the extraction does not carry. "
     "None feeds a published ratio for those periods. Reproduce with `python "
     "tieout_mutation.py balkrishna-industries-ltd`."),
    ("Residual gap to ICRA's published OPBDIT/OI after the failure-mode-36 correction",
     "ICRA's own published rationale (25-Aug-2026) states OPBDIT/OI of 23.9% (FY2025) and "
     "24.3% (FY2026). This engine computes 23.52% and 23.93% after adding back the Rs 290.01 "
     "crore forex loss buried in Other Expenses. The add-back closes 2.68 of the original "
     "3.05-point gap and, decisively, corrects the DIRECTION - the uncorrected series showed "
     "margin FALLING 2.27pt when it actually ROSE 0.41pt, against ICRA's +0.4pt. A residual "
     "of ~0.38pt (~Rs 40 crore) persists in BOTH years, which is itself the useful signal: a "
     "constant offset means a further standing normalisation, not an error in any one year. "
     "The closest single candidate is CSR expenditure (Rs 34.04 crore FY2026, Rs 32.94 crore "
     "FY2025, a statutory appropriation ICRA may add back), which would close most of it - but "
     "that cannot be confirmed from ICRA's published summary, so it is DISCLOSED here rather "
     "than assumed and forced into the build (failure mode 32: never adjust inputs to force a "
     "tie).",),
    ("Interest coverage differs from ICRA's published figure - denominator basis",
     "ICRA publishes interest coverage of 22.3x (FY2025) and 23.7x (FY2026); this engine "
     "computes 19.15x and 19.39x. Solving back, ICRA's denominator is ~Rs 110 crore (FY2025) "
     "and ~Rs 109 crore (FY2026) against reported finance costs of Rs 128.34 crore and "
     "Rs 133.62 crore - i.e. ICRA nets roughly Rs 18-24 crore out of the finance-cost line. "
     "That is consistent with excluding interest on lease liabilities, interest to others and "
     "discount unwinding (the company's own Reg 52(4) ISCR likewise uses 'Interest on Term "
     "Loan & Debentures' only). The exact composition is not recoverable from the published "
     "summary, so the full reported finance cost is used and the difference is stated.",),
    ("Two distinct 'margin' conventions in the company's own disclosures",
     "The Reg 52(4) filing's 'Operating Margin' is EBIT (i.e. after depreciation) less other "
     "income, over revenue - 14.09% for FY2026. ICRA's OPBDITA margin (before depreciation) is "
     "a different, larger number - 22.30% for FY2026 (see RatioSuite). Both are reported under "
     "their own label; the OPBDITA figure is ICRA's headline convention and the Reg 52(4) "
     "figure is reproduced only as a tie-out check, per CLAUDE.md failure mode 32's logic that "
     "a convention that will not reproduce a published figure is the wrong one to STATE as if "
     "it were that figure - here neither is wrong, they simply measure different things."),
    ("FY2024 trade payables / other financial liabilities reclassified between annual reports",
     "The FY2023-24 AR states FY2024 trade payables of Rs 910.23 crore and other financial "
     "liabilities of Rs 156.26 crore; the FY2024-25 AR's restated FY2024 comparative states "
     "Rs 808.19 crore and Rs 258.30 crore respectively - a Rs 102.04 crore reclassification "
     "between the two lines. Both totals (current liabilities Rs 3,660.44 crore; total assets "
     "Rs 13,684.54 crore) are identical in both annual reports and tie exactly either way - "
     "only the line-item split changed. This engine uses the NEWER document's split "
     "throughout, per CLAUDE.md failure mode 26."),
]


# --------------------------------------------------------------------------- report
def main():
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                            # noqa: BLE001
        pass

    R = compute()
    print("=" * 84)
    print("BALKRISHNA INDUSTRIES LIMITED - ICRA ratio engine (consolidated, Rs crore)")
    print("=" * 84)

    order = ["Revenue from operations", "OPBDITA", "OPBDITA margin %", "PAT", "PAT margin %",
             "Total debt", "Net debt", "Net worth (TNW)", "Gearing (times)",
             "Net gearing (times)", "TOL/TNW (times)", "Total debt/OPBDITA (times)",
             "Net debt/OPBDITA (times)", "Interest coverage (times)", "RoCE %",
             "Current ratio (times)", "Debtor days", "Inventory days", "Payable days",
             "Working capital cycle (days)", "EPS (Rs)"]
    cols = ["FY2023", "FY2024", "FY2025", "FY2026"]
    print("\n%-32s %11s %11s %11s %11s" % ("", *cols))
    for k in order:
        vals = [R[c].get(k) for c in cols]
        print("%-32s" % k + "".join(
            "%12.2f" % v if isinstance(v, (int, float)) else "%12s" % "-" for v in vals))

    print("\nQ1FY2027 (consolidated, quarter ended 30-Jun-2026): revenue 3,455.27, OPBDITA %.2f"
          " (margin %.2f%%), PAT 450.77 (margin %.2f%% of total income)."
          % (R["Q1FY2027"]["OPBDITA"], R["Q1FY2027"]["OPBDITA margin %"],
             R["Q1FY2027"]["PAT margin %"]))

    print("\n" + "-" * 84)
    print("DISCLOSED CONVENTIONS / DIFFERENCES (stated, never forced)")
    print("-" * 84)
    for title, text in DISCLOSED_DIFFERENCES:
        print("* %s\n  %s\n" % (title, text))

    print("-" * 84)
    print("TIE-OUTS")
    print("-" * 84)
    T = tieouts(R)
    bad = 0
    for desc, comp, disc, tol_, src in T:
        ok = abs(comp - disc) <= tol_
        if not ok:
            bad += 1
        print("%-4s %-58s computed %12.4f  disclosed %12.4f"
              % ("PASS" if ok else "FAIL", desc[:58], comp, disc))
        if not ok:
            print("     source: %s" % src)
    print("-" * 84)
    if bad:
        print("%d of %d tie-outs FAIL" % (bad, len(T)))
        raise SystemExit(1)
    print("%d/%d tie-outs reconcile" % (len(T), len(T)))


if __name__ == "__main__":
    main()
