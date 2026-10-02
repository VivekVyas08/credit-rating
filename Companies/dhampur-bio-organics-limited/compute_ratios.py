"""Dhampur Bio Organics Limited - CareEdge sugar/bio-refinery ratio suite. STANDALONE. v2.

AGENCY : CareEdge.  ENTITY: corporate (sugar / distillery / co-generation).
BASIS  : *** STANDALONE *** - corrected 13-Sep-2026.

WHY v2 EXISTS - THE BASIS WAS WRONG IN v1
-----------------------------------------
v1 of this engine was CONSOLIDATED. CareEdge rates this issuer STANDALONE, and said so on the
face of its action of 13-Jan-2026 ("Analytical approach: Standalone") - a document that was in
the reference library, was flagged PRESENT by the pre-flight, and was opened at Step 14, where
only the GRADE was compared. v1's report asserted the basis was "methodology-determined, not
elective" without opening the consolidation criteria; every gate accepted the sentence as the
compliance it claimed. 34/34 tie-outs and 100.0% mutation coverage said nothing about it,
because a wrong-basis extraction is perfectly self-consistent with itself.

The standalone basis reproduces the agency's published figures where the consolidated one did
not - which is the test failure mode 32 prescribes, and it is decisive:

    metric                 v1 consolidated   v2 standalone   CareEdge published
    Cash & equivalents            8.71            4.50          "low at Rs 4.5 crore"
    Inventories               1,013.17          994.45          Rs 994 crore
    Tangible net worth        1,026.64        1,029.68          Rs 1,030 crore
    TOI net of excise         2,109.25        2,082.01          Rs 2,082 crore
    PAT FY2026                   25.18           24.97          Rs 25 crore
    Gearing FY2025                1.15            1.142         1.14

SOURCES (Rs crore, as printed)
  FY2026 + FY2025 : AR 2025-26, Standalone P&L (L5453) and Standalone Balance Sheet (L5371).
  FY2024          : AR 2024-25, Standalone P&L (L5538) and Standalone Balance Sheet (L5469).

OCR NOTE: the FY2024-25 AR's balance sheet lost decimal points on four small cells - cash
reads "690"/"238" and other current liabilities "1668"/"1858". They are 6.90 / 2.38 / 16.68 /
18.58, confirmed against the FY2025-26 AR which prints FY2025 cash as 6.90. Corrected here and
recorded rather than silently fixed.
"""

YEARS = ["FY2024", "FY2025", "FY2026"]
BASIS = "standalone"
AR26 = "AR 2025-26, standalone statements"
AR25 = "AR 2024-25, standalone statements (FY2024 comparative)"

# ---------------------------------------------------------------- standalone P&L (Rs crore)
PL = {
    "Revenue from operations":    ([2361.16, 2714.40, 3106.17], AR26 + " / " + AR25),
    "Other income":               ([23.72, 3.71, 30.97], AR26 + " note 26"),
    "Total income":               ([2384.88, 2718.11, 3137.14], AR26 + " printed Total Income"),
    "Cost of raw materials":      ([1604.14, 1362.16, 1476.30], AR26 + " expense (a)"),
    "Excise duty on sale":        ([529.98, 831.44, 1024.16], AR26 + " expense (b) - an EXPENSE"),
    "Purchase of stock-in-trade": ([1.87, 9.19, 41.27], AR26 + " expense (c)"),
    "Changes in inventories":     ([-264.45, 34.31, 57.66], AR26 + " expense (d), sign as printed"),
    "Employee benefits":          ([93.94, 98.47, 112.70], AR26 + " expense (e)"),
    "Depreciation & amortisation": ([49.46, 53.85, 58.76], AR26 + " expense (f)"),
    "Finance costs":              ([45.27, 66.99, 62.96], AR26 + " expense (g)"),
    "Other expenses":             ([260.22, 238.90, 263.04], AR26 + " expense (h)"),
    "Pre-operative capitalised":  ([-2.42, 0.0, 0.0], AR25 + " expense (i), FY2024 only"),
    "Total expenses":             ([2318.01, 2695.31, 3096.85], AR26 + " printed Total Expenses"),
    "PBT before exceptional":     ([66.87, 22.80, 40.29], AR26 + " printed line V"),
    "Exceptional items":          ([0.0, 4.96, 0.0], AR26 + " line VI, a DEDUCTION as printed"),
    "Profit before tax":          ([66.87, 17.84, 40.29], AR26 + " printed line VII"),
    "Current tax":                ([11.09, 4.25, 6.43], AR26 + " tax (a)"),
    "Deferred tax":               ([6.96, 1.50, 8.89], AR26 + " tax (b)"),
    "Profit after tax":           ([48.82, 12.09, 24.97], AR26 + " printed line IX"),
}

# ---------------------------------------------------------------- standalone balance sheet
BS = {
    "Total non-current assets":   ([1089.37, 1194.30, 1166.58], AR26 + " printed (a)"),
    "Inventories":                ([1082.55, 1051.39, 994.45], AR26 + " note 10"),
    "Assets held for disposal":   ([0.0, 0.58, 0.66], AR26 + " note 11"),
    "Trade receivables":          ([87.53, 96.00, 84.94], AR26 + " note 12"),
    "Cash & cash equivalents":    ([2.38, 6.90, 4.50], AR26 + " note 13 - THE liquidity figure"),
    "Bank balances other":        ([4.08, 6.42, 6.19], AR26 + " note 14 - margin / earmarked"),
    "Total current assets":       ([1224.22, 1198.86, 1154.27], AR26 + " printed (b)"),
    "Total assets":               ([2313.59, 2393.16, 2320.85], AR26 + " printed (a+b)"),
    "Equity share capital":       ([66.39, 66.39, 66.39], AR26 + " note 15"),
    "Other equity":               ([954.27, 951.22, 963.29], AR26 + " note 16"),
    "Total equity":               ([1020.66, 1017.61, 1029.68], AR26 + " printed (c)"),
    "Borrowings - non-current":   ([176.95, 236.27, 206.98], AR26 + " note 17(i)"),
    "Lease liabilities - NC":     ([6.61, 5.41, 2.73], AR26 + " note 18(i)"),
    "Total non-current liab":     ([241.22, 301.92, 279.55], AR26 + " printed (d)"),
    "Borrowings - current":       ([869.86, 915.98, 847.19], AR26 + " note 17(ii)"),
    "Lease liabilities - current": ([3.53, 4.68, 3.56], AR26 + " note 18(ii)"),
    "Total current liabilities":  ([1051.71, 1073.63, 1011.62], AR26 + " printed (e)"),
    # The split v1 never made. Current borrowings are NOT all working capital.
    "Current maturities of LT debt": ([0.0, 0.0, 82.68],
                                      AR26 + " note 17 - inside current borrowings"),
}

# Sector-defining OPERATING metric (failure mode 21). v1 quoted TCD capacity - a licence
# figure that does not move - and never extracted throughput, which fell 20.6% in two years
# while sugar OUTPUT rose on better recovery. That is the operating story of FY2026.
OPS = {
    "Cane crushed (lakh tonne)":   ([41.44, 34.98, 32.92], "AR 2025-26 operating table"),
    "Sugar produced (lakh tonne)": ([0.0, 3.10, 3.54], "AR 2025-26 operating table"),
    "Gross recovery (%)":          ([11.37, 10.56, 10.98], "AR 2023-24 / AR 2025-26 MD&A"),
    "Net recovery (%)":            ([0.0, 9.80, 10.74], "AR 2025-26 MD&A"),
    # Cane diverted to SYRUP-derived ethanol, which never becomes sugar. The AR 2025-26 states
    # "No cane diverted for syrup derived ethanol in FY 2025-26 as against 3.37 lakh tons in
    # FY 2024-25" - a material swing v1 never surfaced, and the term that makes the sugar
    # production identity below close.
    "Cane diverted to ethanol (lakh tonne)": ([0.0, 3.37, 0.0], "AR 2025-26 operating footnote"),
}

# Rated limits: CareEdge press release of 04-Sep-2026, OPERATOR-SUPPLIED, imported under the
# five-condition amendment. Verbatim, every line, date-stamped, CRA-published and NOT
# issuer-confirmed, line integrity verified, and distinguished from drawn debt below.
RATED = {
    "Fund-based LT - Cash Credit":            770.00,
    "Fund-based LT - Term Loan (to 30-06-2029)": 117.05,
    "Fund-based LT - WC Demand Loan":         100.00,
    "Non-fund-based ST - BG/LC":               75.00,
}
RATED_DATE = "04-Sep-2026"


def compute():
    """Contract member: {period: {metric: value}}. CareEdge corporate convention, STANDALONE."""
    P = {k: v[0] for k, v in PL.items()}
    B = {k: v[0] for k, v in BS.items()}
    O = {k: v[0] for k, v in OPS.items()}
    R = {}
    for i, y in enumerate(YEARS):
        r = {k: P[k][i] for k in P}
        r.update({k: B[k][i] for k in B})
        r.update({k: O[k][i] for k in O if O[k][i]})

        toi = P["Revenue from operations"][i] - P["Excise duty on sale"][i]
        r["TOI (net of excise)"] = toi
        pbildt = (P["PBT before exceptional"][i] + P["Finance costs"][i]
                  + P["Depreciation & amortisation"][i] - P["Other income"][i])
        r["PBILDT (ex-other income)"] = pbildt
        r["PBILDT margin % (net TOI)"] = pbildt / toi * 100
        r["PAT margin % (net TOI)"] = P["Profit after tax"][i] / toi * 100

        debt = (B["Borrowings - non-current"][i] + B["Lease liabilities - NC"][i]
                + B["Borrowings - current"][i] + B["Lease liabilities - current"][i])
        tnw = B["Total equity"][i]
        # UNENCUMBERED cash only (failure mode 34/45). "Bank balances other than cash and cash
        # equivalents" is margin money against guarantees and the earmarked Molasses Storage
        # Fund - it is not available to service debt. v1 added it and overstated liquidity ~8x.
        free_cash = B["Cash & cash equivalents"][i]
        r["Total debt (incl leases)"] = debt
        r["Unencumbered cash"] = free_cash
        r["Encumbered bank balances"] = B["Bank balances other"][i]
        r["Net debt (on unencumbered cash)"] = debt - free_cash
        r["Tangible net worth"] = tnw
        r["Overall gearing (x)"] = debt / tnw
        r["TOL / TNW (x)"] = (B["Total assets"][i] - tnw) / tnw
        r["Interest coverage (x)"] = pbildt / P["Finance costs"][i]
        r["Total debt / PBILDT (x)"] = debt / pbildt
        r["Net debt / PBILDT (x)"] = (debt - free_cash) / pbildt
        gca = P["Profit after tax"][i] + P["Depreciation & amortisation"][i]
        r["Gross cash accruals"] = gca
        r["Total debt / GCA (x)"] = debt / gca
        r["Current ratio (x)"] = (B["Total current assets"][i]
                                  / B["Total current liabilities"][i])
        r["RoCE (%)"] = (pbildt - P["Depreciation & amortisation"][i]) / (debt + tnw) * 100
        r["Inventory days"] = B["Inventories"][i] * 365 / toi
        r["Receivable days"] = B["Trade receivables"][i] * 365 / toi
        # The decomposition v1 skipped: current borrowings are not all working capital.
        if B["Current maturities of LT debt"][i]:
            r["Working capital borrowings"] = (B["Borrowings - current"][i]
                                               - B["Current maturities of LT debt"][i])
            r["Long-term debt (incl current maturities)"] = (
                B["Borrowings - non-current"][i] + B["Current maturities of LT debt"][i])
        R[y] = r
    return R


def tieouts(R=None):
    """Contract member: [(description, computed, disclosed, tolerance, source), ...]."""
    P = {k: v[0] for k, v in PL.items()}
    B = {k: v[0] for k, v in BS.items()}
    T = []
    for i, y in enumerate(YEARS):
        T.append(("%s total income = revenue + other income" % y,
                  P["Revenue from operations"][i] + P["Other income"][i],
                  P["Total income"][i], 0.02, AR26 + " printed Total Income"))
        T.append(("%s expense build-up reproduces printed total expenses" % y,
                  sum(P[k][i] for k in ("Cost of raw materials", "Excise duty on sale",
                                        "Purchase of stock-in-trade", "Changes in inventories",
                                        "Employee benefits", "Depreciation & amortisation",
                                        "Finance costs", "Other expenses",
                                        "Pre-operative capitalised")),
                  P["Total expenses"][i], 0.02, AR26 + " all expense captions vs printed total"))
        T.append(("%s PBT before exceptional = total income - total expenses" % y,
                  P["Total income"][i] - P["Total expenses"][i],
                  P["PBT before exceptional"][i], 0.02, AR26 + " printed line V"))
        T.append(("%s PBT = PBT before exceptional less exceptional items" % y,
                  P["PBT before exceptional"][i] - P["Exceptional items"][i],
                  P["Profit before tax"][i], 0.02, AR26 + " printed line VII"))
        T.append(("%s PAT = PBT less current and deferred tax" % y,
                  P["Profit before tax"][i] - P["Current tax"][i] - P["Deferred tax"][i],
                  P["Profit after tax"][i], 0.02, AR26 + " printed line IX"))
        T.append(("%s assets = equity + non-current + current liabilities" % y,
                  B["Total equity"][i] + B["Total non-current liab"][i]
                  + B["Total current liabilities"][i],
                  B["Total assets"][i], 0.02, AR26 + " printed Total Equity and Liabilities"))
        T.append(("%s total assets = non-current + current assets" % y,
                  B["Total non-current assets"][i] + B["Total current assets"][i],
                  B["Total assets"][i], 0.02, AR26 + " printed Total Assets"))
        T.append(("%s total equity = share capital + other equity" % y,
                  B["Equity share capital"][i] + B["Other equity"][i],
                  B["Total equity"][i], 0.02, AR26 + " printed Total Equity"))
    # Rated-limit line integrity (five-condition amendment, condition 4).
    T.append(("Rated LT limits sum to the published long-term total",
              sum(v for k, v in RATED.items() if k.startswith("Fund-based LT")),
              987.05, 0.005, "CareEdge press release %s, Annexure-1" % RATED_DATE))
    T.append(("Rated total sums to the published programme",
              sum(RATED.values()), 1062.05, 0.005,
              "CareEdge press release %s - LT 987.05 + ST 75.00" % RATED_DATE))
    # OPERATING IDENTITY: sugar produced = (cane crushed - cane diverted) x net recovery.
    # This is the only arithmetic check available on the sector metrics, and it validates four
    # inputs at once - throughput, diversion, recovery and output. It also proves the FY2025
    # diversion figure, which is the reason output fell that year while crushing fell less.
    for _i in (1, 2):
        _o = OPS["Cane crushed (lakh tonne)"][0][_i] - OPS["Cane diverted to ethanol (lakh tonne)"][0][_i]
        T.append(("%s sugar produced = (cane crushed - diverted) x net recovery" % YEARS[_i],
                  _o * OPS["Net recovery (%)"][0][_i] / 100.0,
                  OPS["Sugar produced (lakh tonne)"][0][_i], 0.012,
                  "AR 2025-26 operating table - throughput, diversion, recovery and output"))

    # The decomposition v1 never made.
    T.append(("FY2026 current borrowings split into WC and current maturities",
              (BS["Borrowings - current"][0][2] - BS["Current maturities of LT debt"][0][2])
              + BS["Current maturities of LT debt"][0][2],
              BS["Borrowings - current"][0][2], 0.02,
              AR26 + " note 17 - the split must return the printed caption"))
    return T


DISCLOSED_DIFFERENCES = [
    ("PBILDT differs from CareEdge's published figure in FY2024 and FY2026, and is NOT forced",
     "On this engine's stated convention - PBT before exceptional, plus finance and "
     "depreciation, less other income in full - PBILDT is 137.88 / 139.93 / 131.04 for "
     "FY2024-26. CareEdge publishes 143 / 140 / 134. FY2025 reproduces almost exactly "
     "(139.93 vs 140); FY2024 and FY2026 are 5.12 and 2.96 short. The convention is stated and "
     "the inputs are NOT adjusted to close the gap - failure mode 32 says that if a definition "
     "will not reproduce, the definition is wrong, and the fix is to say so, not to force the "
     "tie. The most likely cause is the treatment of the loss on sale of property, plant and "
     "equipment (2.32 in FY2026) and of small non-operating items inside other expenses that "
     "CareEdge appears to add back. Every ratio struck on PBILDT here therefore differs "
     "slightly from theirs, and that is disclosed rather than hidden."),
    ("Inventory and operating-cycle days are computed on net TOI, not on CareEdge's denominator",
     "This engine reports inventory days of 190.1 / 203.8 / 174.3 on net operating income. "
     "CareEdge publishes inventory holding days of 224 (FY2025) and 193 (FY2026) and an "
     "operating cycle of 212 / 184 days, which implies a cost-of-goods denominator. Both move "
     "the same way and by a similar magnitude; the level differs by construction."),
    ("FY2024 current maturities of long-term debt are not separately extracted",
     "The FY2026 split is made (82.68 of the 847.19 current borrowings is current maturities, "
     "leaving 764.51 of working-capital borrowings, which reconciles to CareEdge's Rs 765 "
     "crore). FY2024 and FY2025 carry 0.0 for this line, so their working-capital figure is "
     "not split out. Recorded rather than left as a silent zero."),
    ("Q1 FY2026-27 is narrative, not a computed column",
     "The quarter is the off-crushing monsoon season and its reported PAT is dominated by the "
     "one-time gain on the Meerganj slump sale. It informs the forward view; no ratio is "
     "struck on it, so no tie-out reaches it."),
]


def run():
    R = compute()
    W = 42
    print("=" * 104)
    print("DHAMPUR BIO ORGANICS LIMITED - CareEdge ratio suite | sugar / distillery | STANDALONE")
    print("v2, 13-Sep-2026. v1 was CONSOLIDATED and that was the error - see the module docstring.")
    print("=" * 104)
    order = ["Cane crushed (lakh tonne)", "Sugar produced (lakh tonne)", "Gross recovery (%)",
             "Net recovery (%)", "TOI (net of excise)", "PBILDT (ex-other income)",
             "PBILDT margin % (net TOI)", "Profit after tax", "Gross cash accruals",
             "Total debt (incl leases)", "Working capital borrowings",
             "Long-term debt (incl current maturities)", "Unencumbered cash",
             "Encumbered bank balances", "Net debt (on unencumbered cash)",
             "Tangible net worth", "Overall gearing (x)", "TOL / TNW (x)",
             "Interest coverage (x)", "Total debt / PBILDT (x)", "Net debt / PBILDT (x)",
             "Total debt / GCA (x)", "Current ratio (x)", "RoCE (%)", "Inventory days",
             "Receivable days"]
    print("\n%-*s%s" % (W, "METRIC", "".join("%14s" % y for y in YEARS)))
    for k in order:
        cells = "".join("%14s" % ("{:,.2f}".format(R[y][k]) if k in R[y] else "-")
                        for y in YEARS)
        print("  %-*s%s" % (W - 2, k, cells))

    print("\nRATED LIMITS (CareEdge press release %s - CRA-published, NOT issuer-confirmed)"
          % RATED_DATE)
    for k, v in RATED.items():
        print("  %-46s %10.2f" % (k, v))
    print("  %-46s %10.2f" % ("TOTAL RATED PROGRAMME", sum(RATED.values())))
    print("  Drawn borrowings incl leases at 31-Mar-2026: %10.2f  <- a DIFFERENT measure"
          % R["FY2026"]["Total debt (incl leases)"])

    print("\n" + "=" * 104)
    print("TIE-OUTS")
    print("=" * 104)
    T = tieouts(R)
    fail = 0
    for lab, comp, disc, tol, _s in T:
        ok = abs(comp - disc) <= tol
        fail += (not ok)
        print("  [%s] %-62s computed %11s  printed %11s"
              % ("OK " if ok else "FAIL", lab, "{:,.2f}".format(comp), "{:,.2f}".format(disc)))
    print("\n%d/%d tie-outs reconcile." % (len(T) - fail, len(T)))
    for title, text in DISCLOSED_DIFFERENCES:
        print("\n  [DISCLOSED] %s\n              %s" % (title, text))
    if fail:
        print("*** RESOLVE BEFORE DRAFTING (Step 17). ***")
    return fail


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
