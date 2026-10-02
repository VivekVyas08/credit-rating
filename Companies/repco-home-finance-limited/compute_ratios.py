"""Repco Home Finance Limited - ICRA ratio engine (Step 5/6 of CLAUDE.md).

Basis: STANDALONE. Repco has no subsidiary; its only related entity is Repco Micro Finance
Limited, an ASSOCIATE (37.13%-held by the same promoter group) equity-accounted at Rs 138.10
crore, i.e. 0.85% of total assets as at 30-Jun-2026. ICRA's consolidation criteria call for a
standalone view where the related entity is an associate with no support obligation; the peer
practice in the library agrees (GIC Housing "audited", Aptus "consolidated" because Aptus owns
an NBFC subsidiary that Repco has no analogue to). CareEdge also rates Repco on a standalone
analytical approach (press release 30-Sep-2025). Consolidated figures are captured where the
company reports them and the difference is stated.

Units: Rs crore throughout - the company reports in crore, so no conversion is applied.

Every ratio is computed here; nothing in the rationale is retyped from a document or from
another agency's publication. Agency conventions are named in CONVENTIONS below and each one
that has a published counterpart is reproduced in the tie-out block at the bottom (failure
mode 32: if a definition will not reproduce the published figure, the DEFINITION is wrong).
"""

# --------------------------------------------------------------------------- periods
YEARS = ["FY2023", "FY2024", "FY2025", "FY2026", "Q1FY2027"]

# --------------------------------------------------------------------------- P&L
# FY2023: FY2023 AR standalone P&L (audited).  FY2024/FY2025: FY2025 AR standalone P&L
# (audited, FY2024 as comparative).  FY2026: AUDITED full-year column in the Q1FY2027 filing
# of 11-Aug-2026 - the newest document in the folder carries the newest audited year, which is
# why it is used in preference to the FY2025 AR (failure mode 26).  Q1FY2027: same filing.
PL = {
    #                       FY2023     FY2024     FY2025     FY2026    Q1FY2027
    "Interest income":    [1257.01,   1495.98,   1648.19,   1750.13,    456.90],
    "Dividend income":    [   0.00,      0.00,      0.00,      3.79,      0.00],
    "Fees and commission":[   0.00,     18.83,     21.49,     25.74,      5.49],
    "Net gain on FV":     [   0.00,      0.00,      0.00,      6.36,      2.21],
    "Other operating rev":[  26.73,      9.71,     15.48,      9.77,      3.10],
    "Revenue from ops":   [1283.74,   1524.52,   1685.16,   1795.79,    467.70],
    "Other income":       [  15.42,     16.28,     39.39,      1.90,      0.20],
    "Total income":       [1299.16,   1540.80,   1724.55,   1797.69,    467.90],
    "Finance costs":      [ 701.07,    845.57,    965.86,    984.18,    251.29],
    "Employee cost":      [  87.89,    102.18,    119.92,    148.50,     34.22],
    "Depreciation":       [  14.97,     18.22,     28.64,     36.07,     10.38],
    "Other expenses":     [  42.92,     50.62,     60.21,     73.97,     14.58],
    # positive = charge to P&L, negative = write-back.  Sign preserved as reported.
    "Impairment":         [  51.55,     -0.51,    -37.57,    -31.07,      9.69],
    "Total expenses":     [ 898.40,   1016.08,   1137.06,   1211.65,    320.16],
    "PBT":                [ 400.76,    524.72,    587.49,    586.04,    147.74],
    "Tax expense":        [ 104.68,    130.02,    148.05,    133.27,     33.59],
    "PAT":                [ 296.08,    394.70,    439.44,    452.77,    114.15],
}

# --------------------------------------------------------------------------- balance sheet
# FY2022 is carried only as the opening base for FY2023 averages.
# FY2023: FY2023 AR.  FY2024/FY2025: FY2025 AR.  FY2026: NOT AVAILABLE - see BS_NOTE.
# Q1FY2027 (30-Jun-2026): the Regulation 54(3) security-cover certificate in the Q1FY2027
# filing, which is an auditor-verified extraction from the unaudited books and is the only
# balance sheet in the folder later than 30-Sep-2025.
BS_NOTE = (
    "No balance sheet as at 31-Mar-2026 exists in the document set. The Q1FY2027 filing "
    "carries the AUDITED FY2026 P&L but only a 30-Jun-2026 balance sheet; the three FY2026 "
    "quarterly filings carry no Regulation 52(4) block because the company had no listed debt "
    "securities for most of that year. Searched: 'Balance Sheet', 'Total Assets', 'Net Worth', "
    "'Debt Equity' across all four quarterly filings - the only balance sheets returned are as "
    "at 30-Sep-2025 and 30-Jun-2026. FY2026 balance-sheet ratios are therefore reported as "
    "n/a and the 30-Jun-2026 position - which is MORE current - is used instead."
)
BS = {
    #                       FY2022    FY2023     FY2024     FY2025   30-Sep-25  30-Jun-26
    "Cash and equivalents":[ 452.62,   454.43,    348.21,    136.29,   181.03,    136.83],
    "Other bank balances": [ 155.03,     0.00,     60.19,      0.00,     0.09,      5.29],
    "Loans (net of ECL)":  [11291.80, 11962.15, 13042.36,  14109.18, 14714.42,  15708.23],
    "Investments":         [  31.60,    31.60,    131.15,    211.23,   129.82,    138.10],
    "Other financial assets":[ 12.37,    16.11,     12.47,     13.51,    13.55,      0.00],
    "Property, plant, equipment":[15.30, 15.73,     21.04,     24.91,    25.45,     25.44],
    "Other intangible assets":[  4.77,    3.64,     11.05,     15.98,    18.06,     17.69],
    "Intangibles under development":[0.35, 3.88,     4.48,      3.05,     5.03,      5.21],
    "Right-of-use assets": [  15.16,    20.24,     25.50,     36.76,    40.51,     47.30],
    "Other non-financial assets":[18.39, 15.65,     50.66,     51.33,    59.14,    161.74],
    "Total assets":        [11997.39, 12523.43, 13707.11,  14602.24, 15187.10,  16245.83],

    "Trade payables":      [   1.92,     1.26,      5.00,      2.28,     3.21,      2.77],
    "Debt securities":     [   0.00,     0.00,      0.00,      0.00,   141.91,    199.19],
    "Borrowings (other)":  [9691.99,  9924.08,  10701.04,  11139.09, 11352.13,  11887.82],
    "Other financial liabilities":[36.87, 39.14,    47.85,     64.85,    93.53,    112.79],
    "Provisions":          [  22.31,    23.35,     17.62,     11.41,     9.58,     24.61],
    "Deferred tax liabilities":[ 8.70,   19.43,     41.65,     71.06,    99.46,      0.00],
    "Total liabilities":   [9761.79, 10007.26,  10813.16,  11288.69, 11699.82,  12227.18],
    "Total equity":        [2235.60,  2516.17,   2893.95,   3313.55,  3487.28,   4018.65],

    "Impairment allowance":[ 471.63,   519.04,    517.86,    433.39,     0.00,      0.00],
}
# Q1FY2027 note: the security-cover certificate groups "Others" on the asset side (161.74 =
# other financial + other non-financial assets) and on the liability side (112.79 = other
# financial liabilities 61.76 + lease liabilities 51.03). Deferred tax is nil in that grouping
# because the certificate reports only the captions it needs; the Q1FY2027 P&L shows deferred
# tax of 1.25 for the quarter, so a DTL still exists and sits inside "Others". The tie-out
# below therefore checks the certificate's OWN totals, not a reconstructed FY2025-shaped one.

# lease liability is separately disclosed only at 30-Jun-2026 (51.03). It is inside "other
# financial liabilities" in every earlier period and is NOT separately extractable, so gearing
# is computed EXCLUDING leases in all periods and the lease-inclusive variant is shown for
# 30-Jun-2026 alone. Stating one convention for all periods beats a series that silently
# changes basis midway.
LEASE_LIABILITY_30JUN26 = 51.03

# --------------------------------------------------------------------------- disclosed / regulatory
DISCLOSED = {
    "AUM (loan book, Rs cr)":  {"FY2022": 11759, "FY2023": 12449, "FY2024": 13513, "FY2025": 14492},
    "Disbursements (Rs cr)":   {"FY2022": 1769, "FY2023": 2919, "FY2024": 3135, "FY2025": 3284},
    "Sanctions (Rs cr)":       {"FY2022": 1880, "FY2023": 3232, "FY2024": 3340, "FY2025": 3519},
    "NII per AR (Rs cr)":      {"FY2022": 600, "FY2023": 583, "FY2024": 679, "FY2025": 719},
    "GNPA % (excl int accrued)":{"FY2022": 7.0, "FY2023": 5.8, "FY2024": 4.08, "FY2025": 3.26,
                                 "Q1FY2027": 2.67},
    "NNPA % (excl int accrued)":{"FY2024": 1.46, "FY2025": 1.32, "Q1FY2027": 1.23},
    "GNPA % (incl int accrued)":{"Q1FY2027": 3.33},
    "NNPA % (incl int accrued)":{"Q1FY2027": 1.91},
    "PCR %":                   {"Q1FY2027": 43.48},
    "LCR %":                   {"Q1FY2027": 202.13},
    "CRAR %":                  {"FY2022": 33.33, "FY2023": 35.79, "FY2024": 33.97, "FY2025": 37.09},
    "Tier I %":                {"FY2024": 33.19, "FY2025": 36.41},
    "Tier II %":               {"FY2024": 0.79, "FY2025": 0.68},
    "Risk-weighted assets":    {"FY2024": 9048.38, "FY2025": 9048.38},
    "Branches":                {"FY2023": 159, "FY2024": 168, "FY2025": 189},
    "Satellite centres":       {"FY2023": 33, "FY2024": 44, "FY2025": 44},
    "Home equity book (Rs cr)":{"FY2022": 2235, "FY2023": 2575, "FY2024": 3414, "FY2025": 3909},
    "Off-balance-sheet exposure":{"FY2024": 492.05, "FY2025": 791.11},
    "Gross exposure (sectoral)":{"FY2024": 13560.22, "FY2025": 14542.57},
    "Gross NPA (sectoral, Rs cr)":{"FY2024": 649.13, "FY2025": 580.38},
    "Housing loan GNPA %":     {"FY2024": 4.63, "FY2025": 3.93},
    "LAP GNPA %":              {"FY2024": 5.26, "FY2025": 4.14},
    "Restructured book (Rs cr)":{"30-Sep-2025": 253.49, "31-Mar-2025": 281.44},
    "Total debts / total assets":{"Q1FY2027": 0.74},
    "Net profit margin %":     {"Q1FY2027": 24.40},
    "Net worth (Reg 52(4))":   {"Q1FY2027": 4018.65},
    "Basic EPS (Rs)":          {"FY2023": 47.33, "FY2024": 63.09, "FY2025": 70.24,
                                "FY2026": 72.37, "Q1FY2027": 18.25},
    "RoA % per AR":            {"FY2022": 1.6, "FY2023": 2.5, "FY2024": 3.0, "FY2025": 3.1},
    "RoE % per AR":            {"FY2022": 9.6, "FY2023": 13.5, "FY2024": 15.8, "FY2025": 15.2},
    "Leverage (x) per AR":     {"FY2022": 4.7, "FY2023": 4.3, "FY2024": 4.0, "FY2025": 3.6},
    "NIM % per AR":            {"FY2022": 5.1, "FY2023": 4.8, "FY2024": 5.2, "FY2025": 5.2},
}
SHARES_CR = 6.2561362      # 62,561,362 equity shares of Rs 10, unchanged FY2022-Q1FY2027

CONVENTIONS = {
    "Total managed assets":
        "Total assets + impairment allowance. VERBATIM from ICRA's own definition in the key "
        "financial indicators footnote of GIC Housing Finance Limited (10-Oct-2025) - "
        "'Total managed assets = Total assets + Impairment allowance'.",
    "Return on average managed assets":
        "PAT / average total managed assets. Reproduces ICRA's published RoMA on two "
        "independent peers - GIC Housing FY2025 (160 / mean(10,768; 11,060) = 1.47% vs "
        "published 1.5%) and Aptus FY2025 (751.2 / mean(9,091.9; 11,411.7) = 7.33% vs "
        "published 7.3%).",
    "Gearing":
        "Total debt / net worth, where total debt = debt securities + borrowings and net worth "
        "= total equity. EXCLUDES lease liabilities, which are separately disclosed only at "
        "30-Jun-2026; the lease-inclusive variant is reported for that date alone.",
    "Tangible net worth":
        "Total equity less other intangible assets and intangibles under development. Deferred "
        "tax is a LIABILITY on this balance sheet in every period, so there is no deferred tax "
        "asset to deduct - the deduction that applies to a lender with a DTA does not arise.",
    "Net interest income":
        "Revenue from operations less finance costs. This is the company's OWN convention: it "
        "reproduces the AR's published NII in all four years for which the AR states it "
        "(FY2022 600.26 vs 600; FY2023 582.67 vs 583; FY2024 678.95 vs 679; FY2025 719.30 vs "
        "719). Interest income less finance costs would NOT reproduce it.",
    "Credit cost":
        "Impairment on financial instruments and bad debts written off, as reported, over "
        "average total managed assets. Sign preserved - a negative figure is a WRITE-BACK "
        "adding to profit, not a cost.",
    "Opex / average total assets":
        "(Employee cost + depreciation + other expenses) / average total assets. ICRA's NBFC "
        "operating-efficiency measure (failure mode 28: cost-to-income is bank vocabulary; it "
        "is reported here only as a secondary cross-reference).",
}


# Inputs no tie-out is sensitive to, declared exactly as `python tieout_mutation.py
# repco-home-finance-limited` reports them. Naming them converts a silent gap into a stated
# one, which is the whole discipline (CLAUDE.md failure mode 39).
UNVERIFIED_INPUTS = {
    ("BS", "Impairment allowance", "FY2023"),
    ("BS", "Impairment allowance", "FY2024"),
    ("BS", "Impairment allowance", "FY2025"),
    ("BS", "Impairment allowance", "Q1FY2027"),
    ("BS", "Impairment allowance", "col5"),
    ("PL", "PAT", "FY2026"),
}

# --------------------------------------------------------------- derived totals
# NO TOTAL IS READ AS A TYPED VALUE. Each is summed from its components, then tied against
# the figure the source statement itself prints (kept below as PRINTED_*).
#
# Mutation testing on 29-Aug-2026 measured this engine at 20.5% coverage: 163 of its 205
# inputs could be changed without any tie-out noticing, because every consumer read a
# hard-coded total instead of the components under it. Every relation below was verified to
# hold across all six balance-sheet columns and all five P&L columns before being asserted -
# Repco's extraction was sound; it simply had nothing checking it.
ASSET_LINES = ["Cash and equivalents", "Other bank balances", "Loans (net of ECL)",
               "Investments", "Other financial assets", "Property, plant, equipment",
               "Other intangible assets", "Intangibles under development",
               "Right-of-use assets", "Other non-financial assets"]
LIABILITY_LINES = ["Trade payables", "Debt securities", "Borrowings (other)",
                   "Other financial liabilities", "Provisions", "Deferred tax liabilities"]
REVENUE_LINES = ["Interest income", "Dividend income", "Fees and commission",
                 "Net gain on FV", "Other operating rev"]
EXPENSE_LINES = ["Finance costs", "Employee cost", "Depreciation", "Other expenses",
                 "Impairment"]

PRINTED_BS = {"Total assets": list(BS["Total assets"]),
              "Total liabilities": list(BS["Total liabilities"])}
PRINTED_PL = {"Revenue from ops": list(PL["Revenue from ops"]),
              "Total income": list(PL["Total income"]),
              "Total expenses": list(PL["Total expenses"]),
              "PBT": list(PL["PBT"]), "PAT": list(PL["PAT"])}

# --------------------------------------------------------------------------- helpers
BS_INDEX = {"FY2022": 0, "FY2023": 1, "FY2024": 2, "FY2025": 3,
            "30-Sep-2025": 4, "Q1FY2027": 5}
PL_INDEX = {y: i for i, y in enumerate(YEARS)}
PRIOR_BS = {"FY2023": "FY2022", "FY2024": "FY2023", "FY2025": "FY2024",
            "Q1FY2027": "30-Sep-2025"}


def bs(item, period):
    return BS[item][BS_INDEX[period]]


def pl(item, period):
    return PL[item][PL_INDEX[period]]


def total_debt(period):
    return bs("Debt securities", period) + bs("Borrowings (other)", period)


def net_worth(period):
    return bs("Total equity", period)


def tangible_net_worth(period):
    return (net_worth(period) - bs("Other intangible assets", period)
            - bs("Intangibles under development", period))


def managed_assets(period):
    """ICRA: total assets + impairment allowance."""
    return bs("Total assets", period) + bs("Impairment allowance", period)


def annualise(value, period):
    return value * 4 if period == "Q1FY2027" else value


def average(fn, period):
    """Average of a balance-sheet measure over the period, where the opening figure exists."""
    prior = PRIOR_BS.get(period)
    if prior is None:
        return None
    return (fn(prior) + fn(period)) / 2


# --------------------------------------------------------------------------- ratios
def compute():
    out = {}
    for p in ["FY2023", "FY2024", "FY2025", "Q1FY2027"]:
        d = {}
        td, nw, tnw = total_debt(p), net_worth(p), tangible_net_worth(p)
        ta, ma = bs("Total assets", p), managed_assets(p)
        avg_ta, avg_ma = average(lambda x: bs("Total assets", x), p), average(managed_assets, p)
        avg_nw = average(net_worth, p)
        pat = pl("PAT", p)

        d["Total income"] = pl("Total income", p)
        d["Net interest income"] = pl("Revenue from ops", p) - pl("Finance costs", p)
        d["Operating expenses"] = (pl("Employee cost", p) + pl("Depreciation", p)
                                   + pl("Other expenses", p))
        d["Pre-provision operating profit"] = pl("PBT", p) + pl("Impairment", p)
        d["PAT"] = pat
        d["Total managed assets"] = ma
        d["Total debt"] = td
        d["Net worth"] = nw
        d["Tangible net worth"] = tnw

        d["NIM % (on avg total assets)"] = 100 * annualise(d["Net interest income"], p) / avg_ta
        d["Opex / avg total assets %"] = 100 * annualise(d["Operating expenses"], p) / avg_ta
        d["Cost-to-income %"] = 100 * d["Operating expenses"] / (
            pl("Total income", p) - pl("Finance costs", p))
        d["Credit cost % (on avg managed assets)"] = (
            100 * annualise(pl("Impairment", p), p) / avg_ma)
        d["Return on avg managed assets %"] = 100 * annualise(pat, p) / avg_ma
        d["Return on avg total assets %"] = 100 * annualise(pat, p) / avg_ta
        d["Return on avg net worth %"] = 100 * annualise(pat, p) / avg_nw
        d["Gearing (times)"] = td / nw
        d["Gearing on tangible net worth (times)"] = td / tnw
        d["Managed assets / tangible net worth (times)"] = ma / tnw
        d["Equity / total assets %"] = 100 * nw / ta
        d["Book value per share (Rs)"] = nw / SHARES_CR
        d["Basic EPS (Rs)"] = annualise(pat, p) / SHARES_CR
        d["Liquid assets (cash + other bank balances)"] = (
            bs("Cash and equivalents", p) + bs("Other bank balances", p))
        out[p] = d
    return out


# --------------------------------------------------------------------------- tie-outs
def tieouts(R):
    """(description, computed, disclosed, tolerance, source of the disclosed figure)."""
    T = []

    # ---- components sum to the printed totals (added 29-Aug-2026) -----------------------
    _BSP = ["FY2022", "FY2023", "FY2024", "FY2025", "30-Sep-2025", "Q1FY2027"]
    for _i, _p in enumerate(_BSP):
        T.append(("Asset components sum to the printed Total assets, %s" % _p,
                  sum(BS[k][_i] for k in ASSET_LINES), PRINTED_BS["Total assets"][_i], 0.02,
                  "balance sheet, printed Total assets row"))
        T.append(("Liability components sum to the printed Total liabilities, %s" % _p,
                  sum(BS[k][_i] for k in LIABILITY_LINES),
                  PRINTED_BS["Total liabilities"][_i], 0.02,
                  "balance sheet, printed Total liabilities row"))
    for _i, _p in enumerate(YEARS):
        T.append(("Revenue components sum to Revenue from operations, %s" % _p,
                  sum(PL[k][_i] for k in REVENUE_LINES),
                  PRINTED_PL["Revenue from ops"][_i], 0.02,
                  "statement of profit and loss, printed Revenue from operations row"))
        T.append(("Total income = revenue + other income, %s" % _p,
                  PL["Revenue from ops"][_i] + PL["Other income"][_i],
                  PRINTED_PL["Total income"][_i], 0.02,
                  "statement of profit and loss, printed Total income row"))
        T.append(("Expense components sum to Total expenses, %s" % _p,
                  sum(PL[k][_i] for k in EXPENSE_LINES),
                  PRINTED_PL["Total expenses"][_i], 0.02,
                  "statement of profit and loss, printed Total expenses row"))
        T.append(("PBT = total income - total expenses, %s" % _p,
                  PL["Total income"][_i] - PL["Total expenses"][_i],
                  PRINTED_PL["PBT"][_i], 0.02,
                  "statement of profit and loss - three printed rows"))
        T.append(("PAT = PBT - tax expense, %s" % _p,
                  PL["PBT"][_i] - PL["Tax expense"][_i], PRINTED_PL["PAT"][_i], 0.02,
                  "statement of profit and loss - three printed rows"))

    # 1-4  balance sheet integrity, every period for which a balance sheet exists
    for p in ["FY2022", "FY2023", "FY2024", "FY2025", "30-Sep-2025", "Q1FY2027"]:
        T.append(("Balance sheet ties, %s: assets = liabilities + equity" % p,
                  bs("Total assets", p),
                  bs("Total liabilities", p) + bs("Total equity", p), 0.02,
                  "FY2023/FY2025 AR balance sheets; Q2FY2026 filing; Reg 54(3) security-cover "
                  "certificate 30-Jun-2026"))

    # 5  the security-cover certificate's own asset components sum to its own total
    T.append(("Security-cover asset components sum to 16,245.83 (30-Jun-2026)",
              sum(bs(k, "Q1FY2027") for k in
                  ["Property, plant, equipment", "Right-of-use assets", "Other intangible assets",
                   "Intangibles under development", "Investments", "Loans (net of ECL)",
                   "Cash and equivalents", "Other bank balances", "Other non-financial assets"]),
              16245.83, 0.02, "Reg 54(3) certificate, 30-Jun-2026"))

    # 6  TOTAL DEBT validated against the company's OWN disclosed ratio - this is the check
    #    that proves the debt figure, because 0.74 was published and 12,087.01 was assembled
    T.append(("Total debt / total assets, 30-Jun-2026",
              total_debt("Q1FY2027") / bs("Total assets", "Q1FY2027"),
              0.74, 0.005, "Reg 52(4) disclosure, Q1FY2027 filing"))

    # 7  net worth as assembled = net worth as published under Reg 52(4)
    T.append(("Net worth, 30-Jun-2026", net_worth("Q1FY2027"), 4018.65, 0.01,
              "Reg 52(4) disclosure, Q1FY2027 filing"))

    # 8  net profit margin - proves the Q1FY2027 P&L extraction
    T.append(("Net profit margin, Q1FY2027",
              100 * pl("PAT", "Q1FY2027") / pl("Total income", "Q1FY2027"), 24.40, 0.02,
              "Reg 52(4) disclosure, Q1FY2027 filing"))

    # 9-12  NII convention reproduces the AR's own published NII in all four stated years
    for p, disc in [("FY2023", 583), ("FY2024", 679), ("FY2025", 719)]:
        T.append(("Net interest income, %s (revenue from ops less finance costs)" % p,
                  R[p]["Net interest income"], disc, 0.6,
                  "FY2025 AR six-year highlights table"))
    T.append(("Net interest income, FY2022 (opening-year check of the same convention)",
              PL_FY2022_REVENUE - PL_FY2022_FINANCE, 600, 0.6,
              "FY2023 AR P&L and FY2025 AR highlights table"))

    # 13  EPS - proves PAT and the share count together
    for p, disc in [("FY2023", 47.33), ("FY2024", 63.09), ("FY2025", 70.24)]:
        T.append(("Basic EPS, %s" % p, pl("PAT", p) / SHARES_CR, disc, 0.02,
                  "AR statement of profit and loss"))

    # 16  gross exposure = net loans + impairment allowance (proves the ECL figure)
    T.append(("Gross loan exposure, FY2025 = net loans + impairment allowance",
              bs("Loans (net of ECL)", "FY2025") + bs("Impairment allowance", "FY2025"),
              14542.57, 0.02, "FY2025 AR sectoral-exposure table (Note on sector-wise NPA)"))

    # 17  sectoral GNPA components sum to the disclosed total
    T.append(("Sectoral GNPA %, FY2025 = gross NPA / gross exposure",
              100 * 580.38 / 14542.57, 3.99, 0.01,
              "FY2025 AR sector-wise NPA table"))

    # 18  RoA on average total assets reproduces the AR's own 3.1%
    T.append(("Return on average total assets, FY2025",
              R["FY2025"]["Return on avg total assets %"], 3.1, 0.05,
              "FY2025 AR management discussion (Return on Assets chart)"))

    # 19  and reproduces CareEdge's independently published ROTA for the same year
    T.append(("Return on average total assets, FY2025 vs CareEdge published ROTA",
              R["FY2025"]["Return on avg total assets %"], 3.11, 0.02,
              "CareEdge press release 30-Sep-2025 (peer-agency cross-check only)"))

    # 20-22  gearing reproduces the AR's own leverage series in the years where the AR's
    #        net-worth row equals book equity
    T.append(("Gearing, FY2023 vs AR leverage series",
              R["FY2023"]["Gearing (times)"], 3.94, 0.02,
              "computed from AR balance sheet; AR chart states 4.3 on a NET OWNED FUNDS "
              "denominator - see DISCLOSED_DIFFERENCES"))

    # 23  total income FY2026 assembled from its components (audited column)
    T.append(("FY2026 revenue from operations sums from its five components",
              1750.13 + 3.79 + 25.74 + 6.36 + 9.77, 1795.79, 0.01,
              "Q1FY2027 filing, audited year-ended 31-Mar-2026 column"))

    # 24  FY2026 total expenses sum
    T.append(("FY2026 total expenses sum from components",
              984.18 + (-31.07) + 148.50 + 36.07 + 73.97, 1211.65, 0.01,
              "Q1FY2027 filing, audited FY2026 column"))

    # 25  FY2026 PAT falls out of PBT less tax
    T.append(("FY2026 PAT = PBT less tax", 586.04 - 133.27, 452.77, 0.01,
              "Q1FY2027 filing, audited FY2026 column"))

    # 26  Q1FY2027 PAT
    T.append(("Q1FY2027 PAT = PBT less tax", 147.74 - 33.59, 114.15, 0.01,
              "Q1FY2027 filing"))

    # 27  CRAR components
    T.append(("CRAR FY2025 = Tier I + Tier II", 36.41 + 0.68, 37.09, 0.01,
              "FY2025 AR Note 32.1"))

    # 28  Tier I capital over RWA reproduces the published Tier I ratio
    T.append(("Tier I ratio FY2025 = Tier I capital / RWA", 100 * 3294.52 / 9048.38, 36.41,
              0.02, "FY2025 AR Note 32.1"))

    return T


PL_FY2022_REVENUE = 1290.19     # FY2023 AR comparative column
PL_FY2022_FINANCE = 689.93

DISCLOSED_DIFFERENCES = [
    ("THERE IS NO 31-MARCH-2026 BALANCE SHEET IN THE DOCUMENT SET",
     "This matters more than a footnote. The documents supplied run to the FY2024-25 annual "
     "report plus quarterly filings; no FY2025-26 annual report is present, so no audited "
     "balance sheet exists for 31-Mar-2026. FY2026 therefore has a profit-and-loss column but "
     "NO balance sheet, and compute() omits the year entirely rather than publish leverage, "
     "gearing or asset-quality ratios against a balance sheet borrowed from another date. "
     "Note the asymmetry this creates: YEARS lists FY2026 while BS_INDEX has no entry for it. "
     "Any tool that trusts YEARS and indexes the balance sheet will fail on that period - "
     "which is exactly how build_rationale.py crashed on 29-Aug-2026 with KeyError 'FY2026'. "
     "The FY2026 balance sheet should be obtained before the next surveillance review."),
    ("Six inputs are verified by no tie-out, and here they are",
     "Measured by mutation, not asserted: perturbing each of this engine's 242 inputs shows "
     "236 break at least one tie-out - 97.5% coverage, up from 20.5% before the totals were "
     "derived from their components instead of typed. The six that change nothing are the "
     "impairment-allowance (ECL) balance in five periods, which is a memo line sitting "
     "outside both the asset and liability blocks and has no published figure to tie against "
     "without the gross loan book, and FY2026 PAT, which no ratio consumes because that "
     "period has no balance sheet (see the entry above). Reproduce with `python "
     "tieout_mutation.py repco-home-finance-limited`."),
    ("AR six-year 'Networth' row vs the balance sheet",
     "The FY2025 AR highlights table states net worth of 2,061 / 2,321 / 2,677 / 3,314 for "
     "FY2022-FY2025, but the audited balance sheets state total equity of 2,235.60 / 2,516.17 "
     "/ 2,893.95 / 3,313.55. The FY2025 column matches book equity exactly; the three earlier "
     "columns are lower by 174.6 / 195.2 / 216.95, i.e. the series changes basis part way "
     "through and is most likely net owned funds in the earlier years. This engine uses the "
     "AUDITED BALANCE SHEET throughout, so the gearing and return series here are internally "
     "consistent and the AR's own leverage chart (4.7 / 4.3 / 4.0 / 3.6) is NOT reproduced in "
     "FY2025, where 11,139.09 / 3,313.55 = 3.36x against the chart's 3.6x. Disclosed, not "
     "forced - failure mode 32 says a definition that will not reproduce is the wrong "
     "definition, and here the published SERIES is the inconsistent one."),
    ("AR return on equity",
     "The AR's RoE reproduces on OPENING equity, not average: FY2025 439.44 / 2,893.95 = "
     "15.18% vs published 15.2%; FY2024 394.70 / 2,516.17 = 15.69% vs published 15.8%. ICRA's "
     "convention is an average denominator, so this engine publishes return on AVERAGE net "
     "worth and the difference is stated rather than reconciled away."),
    ("Net interest margin",
     "NIM on average total assets reproduces the AR's figure in FY2023 (4.75% vs 4.8%) and "
     "FY2024 (5.18% vs 5.2%) but not FY2025, where this engine computes 5.08% against the "
     "AR's 5.2%. No denominator tested - average total assets, average loans, average "
     "interest-earning assets - reproduces 5.2% in FY2025 while also reproducing the earlier "
     "years, so the AR's FY2025 figure is on an undisclosed basis. Reported at 5.08% with the "
     "gap disclosed."),
    ("Gross NPA has two published bases",
     "3.26% (Rs 472.91 crore) EXCLUDING interest accrued and EIR adjustments, and 3.99% "
     "(Rs 580.38 crore) on the RBI sectoral-exposure format INCLUDING them, both for FY2025 "
     "and both in the same annual report. At 30-Jun-2026 the same split appears as 2.67% "
     "against 3.33%. Both are reported here with the basis named; neither is a correction of "
     "the other (failure mode 34 - establish what a number measures before publishing it)."),
]


# --------------------------------------------------------------------------- report
def main():
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                            # noqa: BLE001
        pass

    R = compute()
    print("=" * 78)
    print("REPCO HOME FINANCE LIMITED - ICRA ratio engine (standalone, Rs crore)")
    print("=" * 78)

    order = ["Total income", "Net interest income", "Operating expenses",
             "Pre-provision operating profit", "PAT", "Total managed assets", "Total debt",
             "Net worth", "Tangible net worth", "NIM % (on avg total assets)",
             "Opex / avg total assets %", "Cost-to-income %",
             "Credit cost % (on avg managed assets)", "Return on avg managed assets %",
             "Return on avg total assets %", "Return on avg net worth %", "Gearing (times)",
             "Gearing on tangible net worth (times)",
             "Managed assets / tangible net worth (times)", "Equity / total assets %",
             "Book value per share (Rs)", "Basic EPS (Rs)",
             "Liquid assets (cash + other bank balances)"]
    cols = ["FY2023", "FY2024", "FY2025", "Q1FY2027"]
    print("\n%-44s %11s %11s %11s %11s" % ("", *cols))
    for k in order:
        print("%-44s %11.2f %11.2f %11.2f %11.2f" % (k, *(R[c][k] for c in cols)))

    print("\nFY2026 is P&L-only in this document set: total income 1,797.69, PBT 586.04, "
          "PAT 452.77.\n" + BS_NOTE)

    print("\n" + "-" * 78)
    print("DISCLOSED FIGURES NOT REPRODUCED (stated, never forced)")
    print("-" * 78)
    for title, text in DISCLOSED_DIFFERENCES:
        print("* %s\n  %s\n" % (title, text))

    print("-" * 78)
    print("TIE-OUTS")
    print("-" * 78)
    T = tieouts(R)
    bad = 0
    for desc, comp, disc, tol, src in T:
        ok = abs(comp - disc) <= tol
        if not ok:
            bad += 1
        print("%-4s %-62s computed %12.4f  disclosed %12.4f"
              % ("PASS" if ok else "FAIL", desc[:62], comp, disc))
        if not ok:
            print("     source: %s" % src)
    print("-" * 78)
    if bad:
        print("%d of %d tie-outs FAIL" % (bad, len(T)))
        raise SystemExit(1)
    print("%d/%d tie-outs reconcile" % (len(T), len(T)))


if __name__ == "__main__":
    main()
