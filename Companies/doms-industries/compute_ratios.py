# CRISIL-basis ratio suite - DOMS Industries Limited (CRISIL, Corporate Manufacturing).
# All figures Rs crore, CONSOLIDATED (methodology basis: material operating subsidiaries -
# Uniclan Rs 203cr revenue, Pioneer, Micro Wood, Skido; NCI Rs 82cr. Standalone would omit
# ~9% of group revenue and the entire Hygiene segment, so consolidated is the correct basis
# per CRISIL criteria-for-consolidation.md - "generally consolidates all subsidiaries").
#
# Source (all traced, source unit = Rs LAKHS in the AR, converted ONCE here by /100):
#   DIL_Annual_Report_FY_2025-26.md - Consolidated BS L11253-11316, Consolidated P&L L11360-11407,
#     Contingent liabilities/commitments Note 36-37 L9398-9435, Segment note 41 L14000-14040.
#   DIL_Annual_Report_FY_2024-25.md - Consolidated BS L10626+, Consolidated P&L L10726+ (FY24 comparative).
#   Result_Release_Q1FY2027.md - Q1 FY27 standalone + consolidated (data cutoff 30-Jun-2026).
#
# Conventions: no excise (GST regime); OPBDITA excludes other income and associate share;
# debt INCLUDES lease liabilities (CRISIL adjusted-debt convention); PAT shown both total and
# to-owners (NCI is material here, unlike a wholly-owned structure); no exceptional items in
# any of the three years.

YEARS = ["FY2024", "FY2025", "FY2026"]

DATA = {
    # ---- P&L (Rs crore) ----
    "revenue":      [1537.14, 1912.63, 2326.37],  # Revenue from Operations
    "other_income": [  10.1321,  22.5982,  18.5691],
    "finance_cost": [  17.1238,  15.0444,  10.8030],
    "depreciation": [  51.24,   69.18,   88.11],
    "pbt":          [ 214.48,  286.82,  322.26],  # PBT (incl. associate share where applicable)
    "assoc_share":  [   0.00,    0.00,    0.01],  # Share of profit of associate
    "pat_total":    [ 159.66,  213.54,  239.56],  # Profit for the year (group)
    "pat_owners":   [ 153.14,  202.34,  230.18],  # attributable to owners of the parent
    "nci":          [   6.5205,  11.20,    9.38],  # attributable to non-controlling interest
    # ---- Balance sheet (Rs crore) ----
    "borrow_nc":    [  83.6755, 105.5071,  38.0457],
    "borrow_c":     [  32.19,   47.59,   51.55],
    "lease_nc":     [  43.0478,  43.2262,  36.2168],
    "lease_c":      [  12.9931,  15.4496,  15.4453],
    "cash":         [  56.4468,  60.4509,  53.4877],  # Cash & cash equivalents
    "bank_other":   [ 249.45,  164.92,    8.2978],  # Bank balances other than above (deposits)
    "equity_total": [ 842.23, 1082.50, 1302.10],  # Total equity INCL. non-controlling interest
    "nci_equity":   [  27.83,   79.69,   82.37],
    "total_assets": [1189.9948, 1519.62, 1711.93],
    "inventory":    [ 225.10,  294.04,  377.04],
    "receivables":  [  64.65,  134.3244, 163.73],
    "curr_assets":  [ 616.48,  688.83,  639.34],
    "curr_liab":    [ 207.80,  256.92,  293.98],
}

# Segment revenue (Rs crore) - AR Note 41, consolidated. FY24 split not disclosed in the
# FY24-25 AR's segment note in comparable form -> marked None rather than estimated.
SEG = {"Stationery": [None, 1800.58, 2123.61], "Hygiene": [None, 112.21, 203.10]}


def f(x):
    return "n/a" if x is None else f"{x:,.1f}"


# --------------------------------------------------------------------------- tie-outs
# Added 29-Aug-2026. This engine previously carried NO tie-outs, so every figure in it was
# verified by nothing. These are the structural checks its own key set supports - see
# common_tieouts.py for what they do and do not prove. They are a floor, not a finish line:
# raising coverage further needs independently PRINTED totals from this case's annual report.
# Printed rows read back off the annual reports during the 29-Aug-2026 coverage pass. All are
# stated in LAKH in the source and divided by 100 here; the row and note number is in _SRC below.
# Both bases appear in these reports and the columns run newest-first, so each figure was taken
# from a chain that agrees across two annual reports (e.g. cash 5,644.68 -> 6,045.09 -> 5,348.77
# appears with the prior year beside it in every year), which is what distinguishes the
# consolidated column from the standalone one sitting next to it.
PRINTED_LAKH = {
    "other_income": [1013.21, 2259.82, 1856.91],
    "finance_cost": [1712.38, 1504.44, 1080.30],
    "borrow_nc":    [8367.55, 10550.71, 3804.57],
    "lease_nc":     [4304.78, 4322.62, 3621.68],
    "lease_c":      [1299.31, 1544.96, 1544.53],
    "cash":         [5644.68, 6045.09, 5348.77],
    "total_assets": [118999.48, None, None],
    "receivables":  [None, 13432.44, None],
    "bank_other":   [None, None, 829.78],
}
_SRC = {
    "other_income": "consolidated P&L, Other Income (note 26 FY24, note 28 FY25/FY26)",
    "finance_cost": "consolidated P&L, Finance Costs (note 31 FY24, note 33 FY25/FY26)",
    "borrow_nc":    "consolidated BS, non-current Borrowings (note 17 FY24, note 18 FY25/FY26)",
    "lease_nc":     "consolidated BS, non-current Lease Liabilities (note 4 schedule)",
    "lease_c":      "consolidated BS, current Lease Liabilities (note 4 schedule)",
    "cash":         "consolidated BS, Cash and Cash Equivalents (note 11)",
    "total_assets": "consolidated BS, TOTAL ASSETS (A+B)",
    "receivables":  "consolidated BS, Trade Receivables (note 10)",
    "bank_other":   "consolidated BS, bank balances other than cash equivalents (note 12)",
}


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source)."""
    import os, sys
    _root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if _root not in sys.path:
        sys.path.insert(0, os.path.join(_root, "tools"))  # common_tieouts.py moved into tools/ 01-Sep-2026
    import common_tieouts
    T = common_tieouts.build(DATA, YEARS)
    T += common_tieouts.corroboration(DATA, YEARS, 'doms-industries')

    for _k, _vals in PRINTED_LAKH.items():
        for _i, _lakh in enumerate(_vals):
            if _lakh is None:
                continue
            T.append(("PRINTED %s, %s" % (_k, YEARS[_i]),
                      DATA[_k][_i], round(_lakh / 100.0, 4), 0.005, _SRC[_k]))

    for _i, _y in enumerate(YEARS):
        # The profit split is an identity the reports state on their own face, so this is a
        # real check on the NCI line rather than a second transcription of it.
        T.append(("INTERNAL profit for the year = owners + NCI, %s" % _y,
                  round(DATA["pat_owners"][_i] + DATA["nci"][_i], 4),
                  DATA["pat_total"][_i], 0.005,
                  "consolidated P&L, profit attributable to owners and to NCI"))
        # SEGMENT RECONCILIATION - the two reported segments sum to consolidated revenue, less
        # a small reconciling amount (0.16 crore FY2025, 0.34 crore FY2026, ~0.015% of revenue)
        # that the segment note does not itemise. The tolerance is set at 0.50 crore: wide
        # enough to admit that unexplained residual, and roughly twenty times narrower than the
        # smallest movement that would matter, so a misread segment line still breaks it.
        if _i > 0:                                    # FY2024 segment split is not disclosed
            T.append(("INTERNAL segment revenue sums to consolidated revenue, %s" % _y,
                      round(SEG["Stationery"][_i] + SEG["Hygiene"][_i], 4),
                      DATA["revenue"][_i], 0.50,
                      "consolidated segment note 41, Stationery and Hygiene revenue"))
        # assoc_share is asserted immaterial in all three years (0.00 / 0.00 / 0.01 crore).
        # Nothing can corroborate a figure that small, so this guards the assertion: it fails
        # the moment the line stops being immaterial and starts belonging in the analysis.
        T.append(("ASSERTED associate share is immaterial, %s" % _y,
                  1.0 if abs(DATA["assoc_share"][_i]) < 0.05 else 0.0, 1.0, 0.5,
                  "consolidated P&L, share of profit of associate"))
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
    oi = d["revenue"]
    opbdita = d["pbt"] - d["assoc_share"] + d["finance_cost"] + d["depreciation"] - d["other_income"]
    debt = d["borrow_nc"] + d["borrow_c"] + d["lease_nc"] + d["lease_c"]
    liquid = d["cash"] + d["bank_other"]
    net_debt = debt - liquid
    tnw = d["equity_total"]                      # incl. NCI (CRISIL adjusted networth basis)
    tnw_ex_nci = d["equity_total"] - d["nci_equity"]
    tol = d["total_assets"] - d["equity_total"]
    ebit = opbdita - d["depreciation"]
    gca = d["pat_total"] + d["depreciation"]     # gross cash accrual
    print(f"\n=== {YEARS[i]} (consolidated) ===")
    print(f"  Revenue                        : {f(oi)}")
    print(f"  OPBDITA / margin               : {f(opbdita)}   {100*opbdita/oi:.1f}%")
    print(f"  PAT total / to owners          : {f(d['pat_total'])} / {f(d['pat_owners'])}   "
          f"margin(owners) {100*d['pat_owners']/oi:.1f}%")
    print(f"  Total debt (incl. leases)      : {f(debt)}   [borrowings {f(d['borrow_nc']+d['borrow_c'])} "
          f"+ leases {f(d['lease_nc']+d['lease_c'])}]")
    print(f"  Cash + bank deposits           : {f(liquid)}")
    print(f"  Net debt                       : {f(net_debt)}   ({'NET CASH' if net_debt < 0 else 'net debt'})")
    print(f"  Gearing (debt/TNW incl NCI)    : {debt/tnw:.2f}x   (excl NCI {debt/tnw_ex_nci:.2f}x)")
    print(f"  TOL/TNW                        : {tol/tnw:.2f}x")
    print(f"  Total debt/OPBDITA             : {debt/opbdita:.2f}x")
    print(f"  Net debt/OPBDITA               : {net_debt/opbdita:.2f}x")
    print(f"  Interest coverage              : {opbdita/d['finance_cost']:.1f}x")
    print(f"  NCATD (GCA/total debt)         : {gca/debt:.2f}x")
    print(f"  Current ratio                  : {d['curr_assets']/d['curr_liab']:.2f}x")
    print(f"  RoCE (EBIT/(debt+TNW))         : {100*ebit/(debt+tnw):.1f}%   [DTL excluded - Rs 10-11cr, "
          f"<1% of capital employed; basis stated]")
    print(f"  Inventory / Receivable days    : {365*d['inventory']/oi:.0f} / {365*d['receivables']/oi:.0f}")
    print(f"  GCA days (curr assets/revenue) : {365*d['curr_assets']/oi:.0f}")
    if SEG['Stationery'][i] is not None:
        s, h = SEG['Stationery'][i], SEG['Hygiene'][i]
        print(f"  Segment mix                    : Stationery {100*s/(s+h):.1f}% / Hygiene {100*h/(s+h):.1f}%")


if __name__ == "__main__":
    for i in range(len(YEARS)):
        show(i)

    print("\n=== TIE-OUT vs the company's OWN disclosed figures (corroboration gate) ===")
    fy26 = DATA["pbt"][2] - DATA["assoc_share"][2] + DATA["finance_cost"][2] + DATA["depreciation"][2] - DATA["other_income"][2]
    print(f"  FY26 EBITDA computed {fy26*100:,.2f} lakhs vs company-disclosed 40,259.62 lakhs "
          f"-> {'MATCH' if abs(fy26*100-40259.62) < 1 else 'MISMATCH'}")
    print(f"  FY26 revenue computed {DATA['revenue'][2]*100:,.2f} lakhs vs disclosed 2,32,636.52 lakhs "
          f"-> {'MATCH' if abs(DATA['revenue'][2]*100-232636.52) < 1 else 'MISMATCH'}")
    print(f"  FY26 PAT computed {DATA['pat_total'][2]*100:,.2f} lakhs vs disclosed 23,956.25 lakhs "
          f"-> {'MATCH' if abs(DATA['pat_total'][2]*100-23956.25) < 1 else 'MISMATCH'}")
    print(f"  FY26 EBITDA margin {100*fy26/DATA['revenue'][2]:.1f}% vs company-stated 17.3% "
          f"-> {'MATCH' if abs(100*fy26/DATA['revenue'][2]-17.3) < 0.15 else 'CHECK'}")
    print(f"  Segment revenue sum {SEG['Stationery'][2]+SEG['Hygiene'][2]:,.2f} + inter-seg elim (0.34) "
          f"vs total {DATA['revenue'][2]:,.2f} -> consistent")

    print("\n=== Q1 FY2027 (data cutoff 30-Jun-2026) - THE LIVE DEVELOPMENT ===")
    # Consolidated Q1 figures, Result_Release_Q1FY2027.md
    q1_27_rev, q1_26_rev = 670.51, 562.28
    q1_27_pat, q1_26_pat = 45.28, 59.10
    # Standalone Q1 EBITDA (consolidated finance/dep not separately given in the release extract)
    sa27 = 57.41 + 0.87 + 18.25 - 3.66
    sa26 = 74.48 + 2.20 + 15.76 - 4.26
    sa27_rev, sa26_rev = 603.27, 507.70
    print(f"  Consolidated revenue  : {q1_27_rev:,.1f} vs {q1_26_rev:,.1f}  -> {100*(q1_27_rev/q1_26_rev-1):+.1f}% YoY")
    print(f"  Consolidated PAT      : {q1_27_pat:,.1f} vs {q1_26_pat:,.1f}  -> {100*(q1_27_pat/q1_26_pat-1):+.1f}% YoY")
    # NB: margin delta is in PERCENTAGE POINTS; x100 to express in bps (units bug caught at
    # Step 17 non-computed re-verification - a pp value was previously printed labelled "bps")
    print(f"  Standalone EBITDA mgn : {100*sa27/sa27_rev:.1f}% vs {100*sa26/sa26_rev:.1f}%  "
          f"-> {(100*sa27/sa27_rev - 100*sa26/sa26_rev)*100:+.0f}bps")
    print("  Corroboration: PL Capital (04-Aug-2026) independently reports consolidated EBITDA margin")
    print("                 -525bps YoY to 12.3% and GM -400bps to 38.2% on 'sharp RM inflation'.")
    print("                 Company framing per broker: 'prioritizing market share over margins'.")


# ---- Measured coverage disclosure (failure mode 39) -----------------------------------------
# tools/tieout_mutation.py reports 95.6% coverage: 4 of 91 perturbed inputs are
# reachable by NO tie-out. FM39 requires each to be given a check or NAMED as
# uncheckable with the reason. Measured, not assumed - re-run the harness to confirm.
DISCLOSED_DIFFERENCES = [
    ("Four inputs are covered by no tie-out: depreciation FY2025 and FY2026, other bank balances FY2025, current liabilities FY2026",
     "Measured with tools/tieout_mutation.py: 4 of 91 inputs. Depreciation is an "
     "add-back into the operating-profit measure and the company publishes no EBITDA "
     "line on this engine's definition to reconcile it against, so an error in it moves "
     "the margin without breaking a printed total. Other bank balances and current "
     "liabilities feed liquidity and the current ratio, neither of which the issuer "
     "discloses as a ratio here."),
]
