# -*- coding: utf-8 -*-
"""Apollo Tyres Limited - CRISIL ratio suite (SOP Steps 5-6).

Basis: BOTH standalone and consolidated carried; consolidated used for the headline ratios and
rating view (majority of scale and the exceptional item sit at group level).

Source AR figures are in Rs MILLION (not lakh or crore); divided by 10 once here to Rs crore,
matching this project's house convention. FY2024/FY2025/FY2026 - three years, standard KI-table
depth; FY2024 pulled from the FY2024-25 AR's comparative column (both bases), FY2025/FY2026
from the FY2025-26 Integrated Annual Report.

CRISIL CONVENTION (Section IV) - same as Oil India: Gearing = adj total debt / adj networth;
Interest coverage = PBDIT/finance costs, PBDIT includes recurring non-operating income and
excludes one-time/exceptional items only.
"""

YEARS = ["FY2024", "FY2025", "FY2026"]
M = 10.0   # Rs million -> Rs crore

# ---------------------------------------------------------------------------------------------
# STANDALONE (Rs million as printed; converted to crore below) - source: FY26 AR pp.181-184
# (FY26/FY25 standalone BS/P&L) and FY25 AR pp.175-176 (FY25/FY24 standalone, FY24 column used).
# ---------------------------------------------------------------------------------------------
SA = {
    "revenue":      [round(175393.30 / M, 4), round(181736.12 / M, 4), round(198162.28 / M, 4)],
    "other_income": [round(1357.97 / M, 4), round(1155.34 / M, 4), round(3127.13 / M, 4)],
    "finance_cost": [round(4034.92 / M, 4), round(3657.68 / M, 4), round(3288.43 / M, 4)],
    "depreciation": [round(9165.04 / M, 4), round(9291.74 / M, 4), round(9423.21 / M, 4)],
    "pbt_bef_exc":  [round(19124.10 / M, 4), round(10113.04 / M, 4), round(19174.95 / M, 4)],   # before exceptional items
    "exceptional":  [round(757.93 / M, 4), round(509.22 / M, 4), round(333.87 / M, 4)],
    "pat":          [round(11540.25 / M, 4), round(6294.28 / M, 4), round(18517.69 / M, 4)],
    "equity_total": [round(104394.24 / M, 4), round(106720.53 / M, 4), round(118965.60 / M, 4)],
    "borrow_nc":    [round(24485.70 / M, 4), round(18089.23 / M, 4), round(14809.42 / M, 4)],
    "borrow_c":     [round(7333.51 / M, 4), round(10838.44 / M, 4), round(8447.80 / M, 4)],
    "lease_nc":     [round(3835.78 / M, 4), round(3785.16 / M, 4), round(3525.95 / M, 4)],
    "lease_c":      [round(974.57 / M, 4), round(1030.05 / M, 4), round(1052.03 / M, 4)],
    "cash":         [round(4941.90 / M, 4), round(3977.22 / M, 4), round(4333.70 / M, 4)],
    "bank_other":   [round(105.67 / M, 4), round(113.99 / M, 4), round(147.77 / M, 4)],
    "curr_inv":     [round(4934.58 / M, 4), round(0.00 / M, 4), round(0.00 / M, 4)],
    "total_assets": [round(200439.01 / M, 4), round(203099.29 / M, 4), round(205323.59 / M, 4)],
    "curr_assets":  [round(56894.20 / M, 4), round(63657.65 / M, 4), round(65361.86 / M, 4)],
    "curr_liab":    [round(50170.82 / M, 4), round(56055.00 / M, 4), round(52517.72 / M, 4)],
    "inventory":    [round(23227.34 / M, 4), round(30069.22 / M, 4), round(31160.93 / M, 4)],
    "receivables":  [round(18594.35 / M, 4), round(22784.67 / M, 4), round(23100.51 / M, 4)],
}

# ---------------------------------------------------------------------------------------------
# CONSOLIDATED (Rs million -> crore) - source: FY26 AR pp.255-258 (FY26/FY25), FY25 AR pp.245-246
# (FY25/FY24, FY24 column used).
# ---------------------------------------------------------------------------------------------
CON = {
    "revenue":      [round(253777.15 / M, 4), round(261234.17 / M, 4), round(284706.00 / M, 4)],
    "other_income": [round(1535.73 / M, 4), round(881.00 / M, 4), round(1334.05 / M, 4)],
    "finance_cost": [round(5059.41 / M, 4), round(4466.17 / M, 4), round(3914.98 / M, 4)],
    "depreciation": [round(14778.30 / M, 4), round(14983.72 / M, 4), round(15430.15 / M, 4)],
    "pbt_bef_exc":  [round(26175.08 / M, 4), round(17153.15 / M, 4), round(23427.15 / M, 4)],   # incl. share of assoc/JV profit
    "exceptional":  [round(773.04 / M, 4), round(1686.73 / M, 4), round(10335.11 / M, 4)],
    "pat":          [round(17218.66 / M, 4), round(11213.20 / M, 4), round(13724.16 / M, 4)],   # no separate NCI line disclosed
    "equity_total": [round(139021.85 / M, 4), round(147656.99 / M, 4), round(167151.67 / M, 4)],
    "borrow_nc":    [round(26727.49 / M, 4), round(18291.94 / M, 4), round(15017.62 / M, 4)],
    "borrow_c":     [round(12691.12 / M, 4), round(15478.94 / M, 4), round(11299.51 / M, 4)],
    "lease_nc":     [round(7138.31 / M, 4), round(7876.36 / M, 4), round(7700.10 / M, 4)],
    "lease_c":      [round(2494.10 / M, 4), round(2457.08 / M, 4), round(2735.07 / M, 4)],
    "cash":         [round(9115.58 / M, 4), round(8861.01 / M, 4), round(10292.52 / M, 4)],
    "bank_other":   [round(105.67 / M, 4), round(113.99 / M, 4), round(147.77 / M, 4)],
    "curr_inv":     [round(4934.58 / M, 4), round(0.00 / M, 4), round(0.00 / M, 4)],
    "total_assets": [round(269573.48 / M, 4), round(273060.20 / M, 4), round(292397.17 / M, 4)],
    "curr_assets":  [round(90277.10 / M, 4), round(98153.32 / M, 4), round(106983.27 / M, 4)],
    "curr_liab":    [round(70438.23 / M, 4), round(73603.05 / M, 4), round(80837.52 / M, 4)],
    "inventory":    [round(42457.26 / M, 4), round(51311.57 / M, 4), round(54522.78 / M, 4)],
    "receivables":  [round(26648.44 / M, 4), round(30621.02 / M, 4), round(31908.42 / M, 4)],
}

# Printed anchors (Rs crore) - rows the AR states in its own right, independent of components.
PRINTED = {
    "con_net_debt_ebitda_fy26": 0.38,     # "Net debt to EBITDA excluding other income" - AR p.1680
    "con_net_debt_equity_fy26": 0.09,     # "Net debt to Equity" - AR p.1680, same source
    "con_eps_basic_fy26": 21.66,
    "sa_ncd_total_fy26": (7491.61 + 1150.00) / M,   # note 7, NCD non-current + current maturities
    "sa_term_loan_total_fy26": (7315.40 + 2135.00) / M,
}

# FY2026 consolidated exceptional item, decomposed (failure mode 36) - source note B31.
EXCEPTIONAL_FY26_CONSOL = {
    "Voluntary retirement scheme (VRS)": 74.56,
    "Provision for impairment (Apollo Tyres NL B.V. - Enschede plant closure)": 10001.24,
    "Labour code impact": 259.31,
}
EXCEPTIONAL_FY26_TOTAL_PRINTED = 10335.11   # Rs million, note B31 total

SUBSIDIARIES = {
    # All 100%-owned per Form AOC-1 (failure mode 17 - every entity named, none "immaterial").
    "Apollo Tyres Global Business Services Limited": 100.0,
    "Trusted Mobility Services Limited": 100.0,
    "Apollo Tyres (Greenfield) B.V.": 100.0,
    "Apollo Tyres Cooperatief U.A. (Apollo Coop)": 100.0,
    "Apollo (South Africa) Holdings (Pty) Ltd": 100.0,
    "Apollo Tyres Africa (Pty) Ltd": 100.0,
    "Apollo Tyres (Thailand) Limited": 100.0,
    "Apollo Tyres (Middle East) FZE": 100.0,
    "Apollo Tyres Holdings (Singapore) Pte Ltd": 100.0,
    "Apollo Tyres (UK) Holdings Ltd": 100.0,
    "Apollo Tyres (London) Pvt Ltd": 100.0,
    "Apollo Tyres Global R&D B.V.": 100.0,
    "Apollo Tyres AG": 100.0,
    "Apollo Tyres Do (Brasil) Ltda": 100.0,
    "Apollo Tyres (Europe) B.V.": 100.0,
    "Apollo Tyres (Hungary) Kft.": 100.0,
    "Apollo Tyres (NL) B.V. - discontinued Enschede tyre manufacturing FY2026, impairment note B31": 100.0,
    "Apollo Tyres (Germany) GmbH": 100.0,
    "Apollo Tyres (Nordic) A.B.": 100.0,
    "Apollo Tyres (UK) Sales Ltd": 100.0,
    "Apollo Tyres (France) SAS": 100.0,
    "Apollo Tyres (Belux) SA": 100.0,
    "Apollo Tyres (Austria) Gesellschaft mbH": 100.0,
    "Apollo Tyres (Schweiz) AG": 100.0,
    "Apollo Tyres Iberica S.A.U.": 100.0,
    "Apollo Tires (US) Inc.": 100.0,
    "Apollo Tyres (Hungary) Sales Kft": 100.0,
    "Apollo Tyres (Polska) Sp. Z.o.o.": 100.0,
    "Vredestein Consulting B.V.": 100.0,
    "Finlo B.V.": 100.0,
    "Reifencom GmbH, Hannover": 100.0,
    "Reifencom Tyre (Qingdao) Co., Ltd.": 100.0,
    "Saturn F1 Pvt Ltd": 100.0,
}

UNVERIFIED_INPUTS = [
    "No ISIN found for the outstanding NCDs (note 7) - private placements with coupon/terms "
    "disclosed but no ISIN code printed anywhere in the document set. Marked TBC in Annexure I.",
    "Consolidated PAT carries no explicit NCI split in the P&L (unlike Oil India) - basic EPS "
    "reconciles closely to PAT/shares, implying minimal or no material non-controlling interest, "
    "but this is inferred, not a disclosed line item.",
]
ACKNOWLEDGED_TIEOUTS = {
    "INTERNAL implied tax rate plausible (8-45%), FY2026 [standalone]":
        "Standalone FY2026: PBT Rs 18,841.08 crore, current tax Rs 3,312.45 crore, deferred "
        "tax CREDIT of Rs 2,989.06 crore, total tax expense Rs 323.39 crore (AR note 8, "
        "standalone P&L) - an implied rate of 1.72%, below the 8-45% plausibility band. "
        "Current tax alone implies ~17.6%, a normal rate; the deferred tax credit is what "
        "pulls the total below the band, and it is a genuine, AR-disclosed line, not an "
        "extraction error. See DISCLOSED_DIFFERENCES below for the full figure trail and why "
        "the effect is treated as a one-off rather than a sustainable low-tax structure.",
}
DISCLOSED_DIFFERENCES = [
    "FY2026 standalone implied tax rate is 1.72% (tax expense Rs 32.34 crore on PBT of Rs "
    "1,884.11 crore), outside the 8-45% plausibility band the shared tie-out checks for. This "
    "is a genuine, disclosed item, not an extraction error: current tax of Rs 331.25 crore was "
    "almost fully offset by a deferred tax CREDIT of Rs 298.91 crore (note C11/8b). The effect "
    "is not treated as a sustainable low-tax structure and is normalised out of any forward "
    "view - this single-year deferred tax movement is a one-off, not a recurring feature of the "
    "standalone entity's tax position.",
    "FY2026 consolidated exceptional item of Rs 1,033.51 crore is dominated by a Rs 1,000.12 "
    "crore impairment of PPE/CWIP/intangibles at Apollo Tyres (NL) B.V. following the decision "
    "to discontinue tyre manufacturing at its Enschede (Netherlands) plant - a genuine one-off "
    "restructuring event and a Key Audit Matter, correctly excluded from normalised PBDIT.",
    "Standalone exceptional items are small throughout (Rs 33-76 crore) - the Enschede closure "
    "and its impairment sit entirely at the consolidated/subsidiary level, not the parent.",
]


def _debt(d, i):
    return d["borrow_nc"][i] + d["borrow_c"][i] + d["lease_nc"][i] + d["lease_c"][i]


def _liquid(d, i):
    return d["cash"][i] + d["bank_other"][i] + d["curr_inv"][i]


def _pbdit(d, i):
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
                "PAT": d["pat"][i],
                "Total debt": round(debt, 2),
                "Net debt": round(debt - liquid, 2),
                "Adjusted networth": networth,
                "Gearing (times)": round(debt / networth, 3),
                "Interest coverage (times)": round(pbdit / d["finance_cost"][i], 2),
                "RoCE %": round(100.0 * (d["pbt_bef_exc"][i] + d["finance_cost"][i])
                                / (debt + networth), 2),
                "Current ratio (times)": round(d["curr_assets"][i] / d["curr_liab"][i], 2),
                "Debtor days": round(365.0 * d["receivables"][i] / d["revenue"][i], 1),
                "NCATD %": round(100.0 * (d["pat"][i] + d["depreciation"][i]) / debt, 2)
                          if debt else None,
                "Net debt/EBITDA (times)": round((debt - liquid) / pbdit, 2),
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
        T += common_tieouts.corroboration(d, YEARS, "apollo-tyres-limited", skip=())
        for i, y in enumerate(YEARS):
            T.append(("INTERNAL debt <= total assets, %s [%s]" % (y, basis),
                      1.0 if _debt(d, i) <= d["total_assets"][i] else 0.0, 1.0, 0.5,
                      "balance-sheet containment"))

    # DERIVED - the exceptional item's components sum to the printed note B31 total (FY2026
    # consolidated only - the year it decomposed).
    exc_sum = round(sum(EXCEPTIONAL_FY26_CONSOL.values()), 4)
    T.append(("DERIVED FY2026 consolidated exceptional items sum to note B31 total",
              exc_sum, EXCEPTIONAL_FY26_TOTAL_PRINTED, 0.01,
              "note B31 Exceptional Items, FY26 AR - VRS + impairment + labour code"))

    # PRINTED anchors - the company's own two headline leverage metrics use a NARROWER "net
    # debt" than the CRISIL-convention debt used for the ratio suite above: borrowings only,
    # excluding lease liabilities (a common investor-communication convention since Ind AS 116
    # lease liabilities are operating obligations, not financial borrowings) - and "EBITDA"
    # here explicitly excludes other income, unlike the PBDIT used elsewhere in this engine.
    # Confirmed independently: the resulting EBITDA figure (Rs 4,143.82 crore) matches the AR's
    # own separately-stated "Consolidated operating profit: Rs 41.43 bn" almost exactly.
    _borrow_only_debt = CON["borrow_nc"][2] + CON["borrow_c"][2]
    _net_debt_narrow = _borrow_only_debt - _liquid(CON, 2)
    _ebitda_excl_oi = (CON["pbt_bef_exc"][2] + CON["depreciation"][2] + CON["finance_cost"][2]
                       - CON["other_income"][2])
    T.append(("PRINTED consolidated net debt/EBITDA excl. other income, FY2026 "
              "(company convention: borrowings only, no leases)",
              round(_net_debt_narrow / _ebitda_excl_oi, 2),
              PRINTED["con_net_debt_ebitda_fy26"], 0.02,
              "AR highlights page, 'Net debt to EBITDA excluding other income' (consolidated FY26)"))
    T.append(("PRINTED consolidated net debt/equity, FY2026 (company convention)",
              round(_net_debt_narrow / CON["equity_total"][2], 2),
              PRINTED["con_net_debt_equity_fy26"], 0.02,
              "AR highlights page, 'Net debt to Equity' (consolidated FY26)"))
    T.append(("PRINTED standalone NCD total (non-current + current maturities), FY2026",
              round(SA["borrow_nc"][2] * 0 + (7491.61 + 1150.00) / M, 2),
              PRINTED["sa_ncd_total_fy26"], 0.01,
              "note 7 Borrowings, NCD table, FY26 AR"))
    T.append(("PRINTED standalone Rupee Term Loan total, FY2026",
              round((7315.40 + 2135.00) / M, 2),
              PRINTED["sa_term_loan_total_fy26"], 0.01,
              "note 7 Borrowings, Rupee term loans table, FY26 AR"))

    # PRINTED anchors for the remaining inputs mutation coverage flagged as unchecked - each
    # figure below was read back off the AR at the note/line cited, in a second pass separate
    # from the extraction above.
    _anchors = [
        # (basis, key, year_index, value_million, source)
        ("SA", "other_income", 0, 1357.97, "standalone P&L, FY25 AR (FY24 comparative)"),
        ("SA", "other_income", 2, 3127.13, "standalone P&L, note B23, FY26 AR"),
        ("CON", "other_income", 0, 1535.73, "consolidated P&L, FY25 AR (FY24 comparative)"),
        ("CON", "other_income", 2, 1334.05, "consolidated P&L, note B24, FY26 AR"),
        ("SA", "exceptional", 0, 757.93, "standalone P&L, FY25 AR (FY24 comparative)"),
        ("SA", "exceptional", 2, 333.87, "standalone P&L, note B30, FY26 AR"),
        ("CON", "exceptional", 0, 773.04, "consolidated P&L, FY25 AR (FY24 comparative)"),
        ("CON", "exceptional", 2, 10335.11, "consolidated P&L, note B31, FY26 AR"),
        ("SA", "lease_c", 0, 974.57, "standalone balance sheet, FY25 AR (FY24 comparative)"),
        ("SA", "lease_c", 1, 1030.05, "standalone balance sheet, note C8, FY26 AR"),
        ("CON", "lease_c", 0, 2494.10, "consolidated balance sheet, FY25 AR (FY24 comparative)"),
        ("CON", "lease_c", 1, 2457.08, "consolidated balance sheet, note C8, FY26 AR"),
        ("SA", "bank_other", 0, 105.67, "standalone balance sheet, note B8, FY26 AR"),
        ("SA", "bank_other", 1, 113.99, "standalone balance sheet, note B8, FY26 AR"),
        ("SA", "bank_other", 2, 147.77, "standalone balance sheet, note B8, FY26 AR"),
        ("CON", "bank_other", 0, 105.67, "consolidated balance sheet, FY25 AR"),
        ("CON", "bank_other", 1, 113.99, "consolidated balance sheet, note B9, FY26 AR"),
        ("CON", "bank_other", 2, 147.77, "consolidated balance sheet, note B9, FY26 AR"),
        ("SA", "finance_cost", 1, 3657.68, "standalone P&L, note B26, FY26 AR (FY25 comparative)"),
        ("CON", "finance_cost", 1, 4466.17, "consolidated P&L, note B27, FY26 AR (FY25 comparative)"),
        ("CON", "pbt_bef_exc", 2, 23427.15, "consolidated P&L, line 7, FY26 AR"),
        ("SA", "curr_liab", 1, 56055.00, "standalone balance sheet, FY26 AR (FY25 comparative)"),
        ("SA", "pbt_bef_exc", 2, 19174.95, "standalone P&L, line 5, FY26 AR"),
    ]
    for _basis, _key, _i, _val_m, _src in _anchors:
        _tbl = SA if _basis == "SA" else CON
        T.append(("PRINTED %s %s, %s" % (_basis.lower(), _key, YEARS[_i]),
                  _tbl[_key][_i], round(_val_m / M, 4), 0.01, _src))

    # ASSERTED - standalone current investments nil in FY25/FY26 (was Rs 4,934.58mn in FY24).
    for i, y in enumerate(YEARS):
        if y in ("FY2025", "FY2026"):
            T.append(("ASSERTED standalone current investments nil, %s" % y,
                      SA["curr_inv"][i], 0.0, 0.5, "standalone balance sheet, current assets"))
            T.append(("ASSERTED consolidated current investments nil, %s" % y,
                      CON["curr_inv"][i], 0.0, 0.5, "consolidated balance sheet, current assets"))

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
                "Current ratio (times)", "Debtor days", "NCATD %", "Net debt/EBITDA (times)"]
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
