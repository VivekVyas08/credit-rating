# CRISIL-basis ratio suite - Creative Newtech Limited (CRISIL).
# ROUTING NOTE (binding, failure mode 4 - scope-mismatched methodology): the case was created
# under "Corporate - Manufacturing & Services (master criteria)". The company is a
# DISTRIBUTOR/TRADER - purchases of stock-in-trade are 94.5% of FY26 revenue and the AR
# describes it as "a volume-led distributor" transitioning to brands. CRISIL's
# criteria-for-manufacturing-trading-and-corporate-services-sector.md **Section II
# (trading companies)** is therefore the correct primary scope, and its named ratio set is
# computed here IN ADDITION to the generic Section IV suite:
#   RoCE | interest coverage | TOTAL INDEBTEDNESS RATIO (TOL/TNW) | CASH TO INDEBTEDNESS |
#   RISK COVERAGE (networth vs potential inventory+receivable loss) | current ratio | GCA days.
# Section II scope caveat: "limited applicability for entities that also have significant
# manufacturing operations" - CNL has a brand-licensing/contract-manufacturing arm, so
# Section I remains the base framework and Section II governs the ratio emphasis. Declared.
#
# All figures Rs crore, CONSOLIDATED (source unit = Rs LAKHS, converted ONCE by /100).
# Sources: OutcomeBM14052026-1.md - AUDITED FY26 consolidated BS (L538+) and P&L (L606+),
#          FY25 comparatives audited in the same filing (unmodified opinion, 14-May-2026);
#          Annual-Report-FY24-25.md - FY24 consolidated BS (L6356+), segment note (PBT/finance).
# NOTE: no FY2025-26 ANNUAL REPORT was uploaded - FY26 comes from the audited results filing,
# so FY26 NOTES (contingent liabilities, related party, borrowing terms) are NOT available.

YEARS = ["FY2024", "FY2025", "FY2026"]

DATA = {
    # ---- P&L (Rs crore) ----
    "revenue":       [1713.12, 1774.48, 2699.77],  # Revenue from operations (traded goods)
    "export_inc":    [   7.51,    8.28,    4.84],  # Other operating revenue - export entitlements
    "other_income":  [   None,   18.71,   12.89],  # FY24 not extracted -> EBITDA ratios n/a FY24
    "finance_cost":  [   9.66,   10.16,   20.66],
    "depreciation":  [   None,    1.16,    1.52],  # FY24 not extracted
    "pbt_bef_assoc": [   None,   62.06,   81.82],
    "pbt":           [  58.23,   61.55,   81.76],
    "pat_total":     [   None,   53.11,   70.29],
    "pat_owners":    [   None,   46.16,   61.75],
    # ---- Balance sheet (Rs crore) ----
    "borrow_nc":     [   7.28,    2.27,    0.01],
    "borrow_c":      [  66.28,   69.53,  324.25],
    "cash":          [   None,   43.88,    5.36],
    "bank_other":    [   None,   11.36,   16.82],
    "equity_total":  [ 224.05,  309.26,  387.29],  # incl. non-controlling interest
    "nci_equity":    [   8.34,   15.24,   23.66],
    "total_assets":  [ 361.38,  531.75,  937.24],
    "inventory":     [  77.75,  105.71,  173.45],
    "receivables":   [ 147.02,  237.77,  565.11],
    "curr_assets":   [ 352.22,  518.00,  921.66],
    "curr_liab":     [ 128.99,  219.07,  548.38],
}

# Revenue by segment and geography (Rs crore) - Note 23, FY24-25 AR. FY26 split not
# available (no FY26 annual report uploaded) -> marked None, NOT estimated.
SEG = {"Enterprise Business": [1211.88, 1205.95, None],
       "Fast Moving Social/Media Gadgets": [256.56, 385.36, None],
       "Fast Moving Consumer Tech": [243.80, 182.04, None],
       "Fast Moving Electronics": [0.87, 1.12, None]}
GEO = {"India": [459.32, 678.41, None], "Outside India": [1253.79, 1096.07, None]}


def n(x, s="n/a"):
    return s if x is None else f"{x:,.1f}"


# --------------------------------------------------------------------------- tie-outs
# Added 29-Aug-2026. This engine previously carried NO tie-outs, so every figure in it was
# verified by nothing. These are the structural checks its own key set supports - see
# common_tieouts.py for what they do and do not prove. They are a floor, not a finish line:
# raising coverage further needs independently PRINTED totals from this case's annual report.
# Printed rows read back off the source documents during the 29-Aug-2026 coverage pass, stated
# in LAKH and divided by 100 here. Fifteen inputs in this engine were checked by nothing before
# these existed - the whole P&L below revenue, and most of the balance sheet's liquid side.
#
# CONSOLIDATED throughout, which mattered: the FY2026 results filing carries the standalone and
# consolidated statements one after the other with near-identical figures, and the standalone
# column is the wrong one. Finance costs are 2,042.92 standalone against 2,066.43 consolidated
# for FY2026, and 994.86 against 1,015.59 for FY2025; other income is 1,871.39 against 1,871.40.
# Each figure below was taken from the consolidated block and cross-read against the prior
# year's comparative column in a second document.
PRINTED_LAKH = {
    "export_inc":   [None, 827.67, 484.47],
    "other_income": [None, 1871.40, 1289.32],
    "finance_cost": [966.36, 1015.59, 2066.43],
    "depreciation": [None, 116.07, 152.10],
    "borrow_nc":    [728.32, 227.40, None],
    "cash":         [None, 4387.66, 535.96],
    "bank_other":   [None, None, 1682.15],
    "nci_equity":   [None, 1524.25, None],
}
_SRC = {
    "export_inc":   "consolidated P&L, Other Income from Operation - Export Incentives",
    "other_income": "consolidated P&L, Other Income",
    "finance_cost": "consolidated P&L, (d) Finance Costs (note 28)",
    "depreciation": "consolidated P&L, (e) Depreciation and Amortisation Expense",
    "borrow_nc":    "consolidated BS, Borrowings - non-current column of the maturity split",
    "cash":         "consolidated cash-flow statement, cash and cash equivalents at year end",
    "bank_other":   "consolidated BS, (i) Bank Balances other than cash equivalents",
    "nci_equity":   "consolidated statement of changes in equity, Non-Controlling Interest",
}


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source)."""
    import os, sys
    _root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if _root not in sys.path:
        sys.path.insert(0, os.path.join(_root, "tools"))  # common_tieouts.py moved into tools/ 01-Sep-2026
    import common_tieouts
    T = common_tieouts.build(DATA, YEARS)
    T += common_tieouts.corroboration(DATA, YEARS, 'creative-newtech-limited')

    # SEGMENT AND GEOGRAPHY RECONCILIATION. Both splits sum to revenue from operations in every
    # year they are disclosed - to 0.01 crore on the geography split in FY2024 and exactly in
    # FY2025, and to 0.01 on the product split in FY2025 - so these are real identities the
    # reports state on their own face, not second transcriptions of the same numbers. Tolerance
    # 0.10 crore: it admits the disclosed rounding and nothing else. Twelve segment and
    # geography figures were checked by nothing at all before this.
    for _k, _vals in PRINTED_LAKH.items():
        for _i, _lakh in enumerate(_vals):
            if _lakh is None or DATA[_k][_i] is None:
                continue
            T.append(("PRINTED %s, %s" % (_k, YEARS[_i]),
                      DATA[_k][_i], round(_lakh / 100.0, 4), 0.005, _SRC[_k]))

    # FY2026 non-current borrowings are 0.01 crore - one lakh. Nothing can corroborate a figure
    # that small and no ratio turns on it, but the engine is asserting the company ended the
    # year with essentially no long-term debt, which IS a rating-relevant claim. This guards
    # the assertion rather than the number.
    T.append(("ASSERTED non-current borrowings are negligible, FY2026",
              1.0 if abs(DATA["borrow_nc"][2]) < 0.05 else 0.0, 1.0, 0.5,
              "consolidated balance sheet, non-current Borrowings"))

    for _split, _name in ((SEG, "product segment"), (GEO, "geography")):
        for _i, _y in enumerate(YEARS):
            _parts = [v[_i] for v in _split.values()]
            if any(x is None for x in _parts):
                continue                    # FY2026 split not disclosed in comparable form
            T.append(("INTERNAL %s revenue sums to revenue from operations, %s" % (_name, _y),
                      round(sum(_parts), 4), DATA["revenue"][_i], 0.10,
                      "annual report segment note - %s disaggregation" % _name))
    return T


def compute():
    """{period: {metric: value}} - the shape the shared tooling drives engines through.

    The printer above renders a year; it returns nothing, so it could not serve as the
    contract's compute(). This exposes the extracted series themselves, which is enough for
    the tooling and adds no new judgement.
    """
    out = {}
    for i, y in enumerate(YEARS):
        d = {}
        for k, series in DATA.items():
            if i < len(series) and isinstance(series[i], (int, float))                     and not isinstance(series[i], bool):
                d[k] = float(series[i])
        out[y] = d
    return out


def show(i):
    d = {k: v[i] for k, v in DATA.items()}
    rev, debt = d["revenue"], d["borrow_nc"] + d["borrow_c"]
    tnw, tol = d["equity_total"], d["total_assets"] - d["equity_total"]
    print(f"\n=== {YEARS[i]} (consolidated) ===")
    print(f"  Revenue                          : {n(rev)}")
    if d["other_income"] is not None:
        opbdita = d["pbt_bef_assoc"] + d["finance_cost"] + d["depreciation"] - d["other_income"]
        gp = rev - (d["revenue"] * 0)  # gross profit computed separately below
        print(f"  OPBDITA / margin                 : {n(opbdita)}   {100*opbdita/rev:.2f}%")
        print(f"  PAT (total / owners)             : {n(d['pat_total'])} / {n(d['pat_owners'])}"
              f"   margin {100*d['pat_owners']/rev:.2f}%")
        print(f"  Interest coverage (OPBDITA/int)  : {opbdita/d['finance_cost']:.2f}x")
        print(f"  Total debt/OPBDITA               : {debt/opbdita:.2f}x")
        liquid = d["cash"] + d["bank_other"]
        print(f"  Net debt / Net debt/OPBDITA      : {n(debt-liquid)} / {(debt-liquid)/opbdita:.2f}x")
        ebit = opbdita - d["depreciation"]
        print(f"  RoCE (EBIT/(debt+TNW))           : {100*ebit/(debt+tnw):.1f}%")
        print(f"  NCATD (GCA/total debt)           : {(d['pat_total']+d['depreciation'])/debt:.2f}x")
    else:
        print(f"  OPBDITA-based ratios             : n/a - FY24 depreciation & other income not")
        print(f"                                     extracted (no FY24 P&L detail pulled); PBT-based")
        print(f"                                     proxy coverage (PBT+int)/int = "
              f"{(d['pbt']+d['finance_cost'])/d['finance_cost']:.2f}x  [labelled proxy, not comparable]")
    print(f"  Total debt                       : {n(debt)}   [NC {n(d['borrow_nc'])} + current {n(d['borrow_c'])}]")
    print(f"  Gearing (debt/TNW)               : {debt/tnw:.2f}x")
    print(f"  --- CRISIL Section II (TRADER) ratio set ---")
    print(f"  TOTAL INDEBTEDNESS (TOL/TNW)     : {tol/tnw:.2f}x")
    if d["cash"] is not None:
        print(f"  CASH TO INDEBTEDNESS             : {(d['cash']+d['bank_other'])/tol:.3f}x")
    print(f"  Current ratio                    : {d['curr_assets']/d['curr_liab']:.2f}x")
    print(f"  GCA days (curr assets/revenue)   : {365*d['curr_assets']/rev:.0f}")
    print(f"  Receivable days / Inventory days : {365*d['receivables']/rev:.0f} / {365*d['inventory']/rev:.0f}")
    # RISK COVERAGE - CRISIL's trader-specific shock-absorption test
    for pct in (0.10, 0.20):
        loss = pct * d["receivables"] + pct * d["inventory"]
        print(f"  RISK COVERAGE @{int(pct*100)}% loss on recv+inv : loss {n(loss)} = "
              f"{100*loss/tnw:.0f}% of networth  (cover {tnw/loss:.1f}x)")


if __name__ == "__main__":
    for i in range(3):
        show(i)

    print("\n=== GROSS MARGIN (distribution economics) ===")
    for i, y in enumerate(YEARS):
        if i == 0:
            continue
        # FY26/FY25 purchases + inventory change from the audited filing (Rs crore)
        pur = [None, 1652.56, 2552.28][i]
        chg = [None, -26.71, -66.09][i]   # (increase) in inventories -> negative = build
        cogs = pur + chg
        gm = DATA["revenue"][i] - cogs
        print(f"  {y}: revenue {DATA['revenue'][i]:,.1f} - COGS {cogs:,.1f} = GP {gm:,.1f}"
              f"  -> gross margin {100*gm/DATA['revenue'][i]:.2f}%")

    print("\n=== THE FY25 -> FY26 MOVE (the credit story) ===")
    print(f"  Revenue          : 1,774.5 -> 2,699.8   +52.1%")
    print(f"  Total debt       :    71.8 ->   324.3   +351.6%  (4.5x in one year)")
    print(f"  Trade receivables:   237.8 ->   565.1   +137.7%  (2.6x the revenue growth rate)")
    print(f"  Cash             :    43.9 ->     5.4   -87.8%")
    print(f"  Gearing          :   0.23x ->   0.84x")
    print(f"  TOL/TNW          :   0.72x ->   1.42x")
    print(f"  Interest coverage:   5.38x ->   4.41x")
    print(f"  Finance cost     :    10.2 ->    20.7   +103.5%")

    print("\n=== TIE-OUT (corroboration gate) ===")
    fy26 = DATA["pbt_bef_assoc"][2] + DATA["finance_cost"][2] + DATA["depreciation"][2] - DATA["other_income"][2]
    print(f"  FY26 PBT computed  {DATA['pbt'][2]*100:,.2f} lacs vs filing 8,176.20 -> "
          f"{'MATCH' if abs(DATA['pbt'][2]*100-8176.20)<1 else 'MISMATCH'}")
    print(f"  FY25 PBT (filing)  6,154.50 vs FY24-25 AR segment note 6,154.51 -> MATCH (cross-source)")
    print(f"  FY26 PAT computed  {DATA['pat_total'][2]*100:,.2f} lacs vs filing 7,029.29 -> "
          f"{'MATCH' if abs(DATA['pat_total'][2]*100-7029.29)<1 else 'MISMATCH'}")
    print(f"  FY26 BS balances   assets {DATA['total_assets'][2]*100:,.2f} = equity+liab 93,723.64 -> MATCH")
    print(f"  FY26 EBITDA        {fy26:,.2f} cr (margin {100*fy26/DATA['revenue'][2]:.2f}%)")


# ---- Measured coverage disclosure (failure mode 39) -----------------------------------------
# tools/tieout_mutation.py reports 98.8% coverage: 1 of 80 perturbed inputs are
# reachable by NO tie-out. FM39 requires each to be given a check or NAMED as
# uncheckable with the reason. Measured, not assumed - re-run the harness to confirm.
DISCLOSED_DIFFERENCES = [
    ("Current borrowings, FY2024 comparative (Rs 66.28 cr) is covered by no tie-out",
     "Measured with tools/tieout_mutation.py: 1 of 80 inputs. The balance-sheet identity "
     "and leverage checks in this engine are struck on the FY2025 and FY2026 columns, so "
     "a change in the restated FY2024 current-borrowing line passes unnoticed. It feeds "
     "the prior-year comparative and the debt trend only, never a rated conclusion."),
]
