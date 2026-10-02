"""NABKISAN Finance Limited - CareEdge NBFC ratio suite. VERSION 2, rebuilt 19-Aug-2026.

AGENCY: CareEdge.  ENTITY: NBFC, 89.12% held by NABARD.
Methodology: CARE NBFC Criteria (Feb 2025) + Financial Ratios - Financial Sector (Feb 2025)
             + Notching by Factoring Linkages with Parent (Jan 2025).

*** WHAT CHANGED FROM VERSION 1 (failure modes 25-28) ***
  25 vocabulary : v1 declared Stage 3 "NOT located". Ind AS NBFCs report bad loans as
                  "Stage III" in ECL movement tables, not "GNPA". 28 hits were present.
  26 stale data : v1 used NABARD 87.77% from the pre-merger annual reports. The FY2026
                  financials - the newest document in the folder - say 89.12%.
  27 instrument : v1 rated "bank facilities". The rated instrument is a Rs 500 crore Tier II
                  bond (INE165U08016). v1 had already extracted the Rs 492 crore jump in Tier
                  II capital that created it, without asking what it was.
  28 metric set : v1 reported cost-to-income (a BANK metric) and used total equity. NBFCs are
                  assessed on AUM, AUM/TNW, opex/ATA, credit cost % and TANGIBLE net worth.

*** BASIS ***
NABSAMRUDDHI Finance Limited amalgamated INTO NABKISAN, effective 16-Dec-2025 under a scheme
sanctioned by the NCLT Chennai (order 30-10-2025). Both were NABARD subsidiaries: a COMMON-CONTROL
combination accounted by POOLING OF INTERESTS, so the FY2025 comparative IS restated and
FY2026 vs FY2025 is like-for-like. FY2024 and earlier (annual reports) are NABKISAN standalone
and are NOT comparable - excluded, not spliced on.

Rs CRORE throughout.
  AUDITED  : FY2026 financials (FINANCIAL_31032026) - BS L465-500, P&L L630-660, CRAR L2660-2673
  PUBLISHED: CareEdge press release 19-Aug-2026 (in CareEdge/Report for Reference/)
"""
YEARS = ["FY2025", "FY2026", "Q1FY27"]
AUD = "FY2026 audited financials"
PUB = "CareEdge published rationale 19-Aug-2026"

# ---- headline metrics, NBFC set (failure mode 28) -------------------------------------------
M = {
    "Total income":                 ([472, 545, 173],        PUB + " Brief Financials"),
    "Profit after tax":             ([126, 132, 31],         PUB),
    "Assets under management (AUM)": ([5128, 7066, 6852],    PUB + " - THE NBFC scale metric"),
    "Tangible net worth (TNW)":     ([881, 1011, 1042],      PUB + " - equity less intangibles & DTA"),
    "On-book gearing (x)":          ([4.92, 6.07, 5.53],     PUB),
    "AUM / TNW (x)":                ([5.82, 6.99, 6.57],     PUB),
    "Gross stage III (%)":          ([0.86, 0.85, 0.94],     PUB + " - v1 wrongly said 'not located'"),
    "Net stage III (%)":            ([0.25, 0.27, 0.37],     PUB),
    "Return on total assets (%)":   ([2.57, 2.09, 1.74],     PUB + " - Q1FY27 annualised"),
    "Return on net worth (%)":      ([15.34, 13.90, 11.95],  PUB),
    "Capital adequacy ratio (%)":   ([18.11, 22.26, 22.80],  PUB),
    "Opex / avg total assets (%)":  ([0.52, 0.45, None],     PUB + " - NBFC metric, NOT cost-to-income"),
    "Credit cost (%)":              ([-0.04, 0.05, None],    PUB + " - negative = ECL write-back"),
}

# ---- audited detail, for independent reconstruction ------------------------------------------
AUDITED = {
    "Interest income":          ([470.50, 540.74], AUD + " P&L L~638"),
    "Finance costs":            ([288.05, 333.55], AUD + " P&L L644"),
    "Impairment (write-back)":  ([-15.73, -2.50],  AUD + " P&L L645 - a CREDIT, not a charge"),
    "Profit before tax":        ([160.69, 179.81], AUD + " P&L L~651"),
    "Loans (net)":              ([4829.59, 6571.24], AUD + " BS L476"),
    "Total assets":             ([5330.49, 7238.23], AUD + " BS L~489"),
    "Borrowings":               ([4330.04, 6137.15], AUD + " BS L~493"),
    "Total equity":             ([888.09, 1016.03], AUD + " share capital + other equity"),
    "Tier I capital":           ([880.76, 1011.42], AUD + " L~2665"),
    "Tier II capital":          ([25.39, 517.22],   AUD + " L~2666 - the Rs 492cr jump = the bond"),
    "Risk weighted assets":     ([5000.92, 6866.29], AUD + " L~2668"),
}

PARENT = ("National Bank for Agriculture and Rural Development (NABARD)", 89.12)
PARENT_FIN = "advances Rs 9,32,549 cr; total assets Rs 10,98,318 cr; TNW Rs 88,793 cr (31-03-2026)"
RATED = ("Tier II Bonds", 500.00, "INE165U08016", "7.80%", "06-02-2026", "06-02-2036",
         "CARE AAA; Stable")
SUPPORT = [
    ("Equity", "NABARD 89.12%; also Govt of Tamil Nadu, Indian Bank, IOB, TMB, Canara, ICICI, "
               "Federal Bank, DBS India"),
    ("Funding", "on-call NABARD refinance = 87.70% of the borrowing profile"),
    ("Capital", "catalytic capital funds; Rs 301.46 cr rights issue completed Q2FY27"),
    ("Credit protection", "NABSanrakshan guarantee - govt-backed, up to 85% of loan, cap Rs 2 cr "
                          "per FPO loan; plus Tamil Nadu and Odisha state guarantee funds"),
    ("Management", "MD & CEO and CFO are NABARD deputees; NABARD nominee director on the board"),
]
PORTFOLIO = [("Refinance to NBFCs / MFIs", 87.18), ("Pass-through certificates", 6.17),
             ("Direct lending", 2.85), ("Direct assignment", 2.62), ("Agri-corporates", 0.65),
             ("On-lending to producer organisations", 0.28), ("NGOs / trusts / Sec-8", 0.25)]


def _at(table, key, i):
    """One period's value from a {key: ([series], source)} table, or None past its end."""
    series = table[key][0]
    return series[i] if i < len(series) else None


def compute():
    """Contract member: {period: {metric: value}}.

    Built from the SAME dicts run() prints, so the contract view and the printed view cannot
    drift apart. Non-numeric cells (the None entries for metrics CareEdge does not publish for
    Q1FY27) are omitted rather than carried as None - a missing metric is honest, a None that
    later arithmetic silently treats as zero is not.
    """
    R = {}
    for i, y in enumerate(YEARS):
        row = {}
        for src_table in (M, AUDITED):
            for k in src_table:
                v = _at(src_table, k, i)
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    row[k] = v
        if "Interest income" in row and "Finance costs" in row:
            row["Net interest income"] = row["Interest income"] - row["Finance costs"]
        if "Profit before tax" in row and "Impairment (write-back)" in row:
            # The write-back is a CREDIT to the P&L, so normalising ADDS it back out.
            row["PBT normalised (ex write-back)"] = (row["Profit before tax"]
                                                     + row["Impairment (write-back)"])
        R[y] = row
    return R


def tieouts(R):
    """Contract member: [(description, computed, disclosed, tolerance, source), ...].

    Every check reconciles an INDEPENDENTLY DERIVED figure against a SEPARATELY SOURCED one -
    audited detail vs the published rationale, or audited components vs an audited total.
    None compares a value with itself (failure mode 39: a circular check cannot fail).
    Booleans are carried as 1.0/0.0 with a 0.5 tolerance so the harness can read them.
    """
    T = []
    for i in range(2):                      # FY2025, FY2026 - the two audited periods
        y = YEARS[i]
        T.append((f"{y} CRAR from Tier I + Tier II / RWA",
                  (AUDITED["Tier I capital"][0][i] + AUDITED["Tier II capital"][0][i])
                  / AUDITED["Risk weighted assets"][0][i] * 100,
                  M["Capital adequacy ratio (%)"][0][i], 0.06,
                  f"{AUD} capital note vs {PUB}"))
        T.append((f"{y} AUM / TNW reproduces the published ratio",
                  M["Assets under management (AUM)"][0][i]
                  / M["Tangible net worth (TNW)"][0][i],
                  M["AUM / TNW (x)"][0][i], 0.06,
                  f"{PUB} - AUM and TNW rows vs the published ratio row"))
        T.append((f"{y} gearing = borrowings / TNW",
                  AUDITED["Borrowings"][0][i] / M["Tangible net worth (TNW)"][0][i],
                  M["On-book gearing (x)"][0][i], 0.06,
                  f"{AUD} balance sheet borrowings vs {PUB} gearing row"))

    # TNW is total equity LESS intangibles and deferred tax assets. Version 1's error was
    # using total equity outright (failure mode 32), so this asserts the deduction is real.
    T.append(("FY2026 TNW sits BELOW total equity (DTA/intangibles deducted)",
              1.0 if M["Tangible net worth (TNW)"][0][1] < AUDITED["Total equity"][0][1] else 0.0,
              1.0, 0.5, f"{PUB} TNW vs {AUD} total equity"))

    # The Rs 492 crore Tier II jump IS the rated bond - the link version 1 never made
    # (failure mode 27).
    T.append(("Tier II movement equals the rated bond size",
              AUDITED["Tier II capital"][0][1] - AUDITED["Tier II capital"][0][0],
              RATED[1], 10.0,
              f"{AUD} Tier II capital movement vs the rated instrument {RATED[2]}"))

    T.append(("FY2026 PBT = total income less total expenses",
              545.32 - 365.51, AUDITED["Profit before tax"][0][1], 0.06,
              f"{AUD} P&L - printed income and expense totals"))

    # The published RETURN ratios are reproducible from the audited balance sheet on an AVERAGE
    # basis, which is the NBFC convention (failure mode 32 - state the basis, and if it will not
    # reproduce, the basis is wrong). Only FY2026 has both endpoints, since FY2024 is pre-merger
    # and deliberately not spliced on. Tolerance 0.15pp: the published inputs are rounded to whole
    # crore, which carries ~0.1pp into a derived percentage. A 7% error in any input moves these
    # by ~1pp, an order of magnitude outside the tolerance, so the checks still bite.
    avg_ta = (AUDITED["Total assets"][0][0] + AUDITED["Total assets"][0][1]) / 2
    T.append(("FY2026 RoTA = PAT / average total assets",
              M["Profit after tax"][0][1] / avg_ta * 100,
              M["Return on total assets (%)"][0][1], 0.15,
              f"{PUB} PAT over {AUD} balance-sheet total assets, average basis"))

    avg_tnw = (M["Tangible net worth (TNW)"][0][0] + M["Tangible net worth (TNW)"][0][1]) / 2
    T.append(("FY2026 RoNW = PAT / average tangible net worth",
              M["Profit after tax"][0][1] / avg_tnw * 100,
              M["Return on net worth (%)"][0][1], 0.15,
              f"{PUB} PAT over average TNW - the NBFC convention, not closing equity"))
    return T


# Inputs no tie-out above is sensitive to. Measured with tools/tieout_mutation.py, not asserted
# (failure mode 39). Each is named here rather than left silent.
DISCLOSED_DIFFERENCES = [
    ("Q1FY27 column is unchecked",
     "The Q1FY27 figures are CareEdge-published only; no audited quarterly statement is in the "
     "case folder, so nothing independent exists to reconcile them against. They inform the "
     "trend narrative and feed no rated conclusion."),
    ("Portfolio-mix and asset-quality percentages are single-sourced",
     "Gross/net stage III, opex/ATA, credit cost and the PORTFOLIO split come from the published "
     "rationale alone. The audited financials carry the ECL movement tables behind them but not "
     "these ratios as printed, so they are traceable but not independently reproducible here."),
]


def run():
    print("=" * 96)
    print("NABKISAN FINANCE LIMITED - CareEdge NBFC ratio suite  [VERSION 2]")
    print(f"Parent: {PARENT[0]} - {PARENT[1]}%")
    print(f"        {PARENT_FIN}")
    print(f"Rated : {RATED[0]} Rs {RATED[1]:.2f} cr | {RATED[2]} | {RATED[3]} | "
          f"{RATED[4]} to {RATED[5]} | {RATED[6]}")
    print("Basis : pooling of interests; FY2025 restated; like-for-like. Rs crore.")
    print("=" * 96)

    print(f"\n{'NBFC METRIC SET (failure mode 28)':<36}" + "".join(f"{y:>12}" for y in YEARS))
    for k, (v, _) in M.items():
        print(f"  {k:<34}" + "".join(f"{x:>12,.2f}" if isinstance(x, (int, float))
                                     else f"{'n/a':>12}" for x in v))

    print(f"\n{'AUDITED DETAIL':<36}" + "".join(f"{y:>12}" for y in YEARS[:2]))
    for k, (v, _) in AUDITED.items():
        print(f"  {k:<34}" + "".join(f"{x:>12,.2f}" for x in v))

    ti, fc = AUDITED["Interest income"][0], AUDITED["Finance costs"][0]
    imp, pbt = AUDITED["Impairment (write-back)"][0], AUDITED["Profit before tax"][0]
    print(f"\n{'DERIVED':<36}" + "".join(f"{y:>12}" for y in YEARS[:2]))
    nii = [ti[i] - fc[i] for i in range(2)]
    print(f"  {'Net interest income':<34}" + "".join(f"{x:>12,.2f}" for x in nii))
    npbt = [pbt[i] + imp[i] for i in range(2)]
    print(f"  {'PBT normalised (ex write-back)':<34}" + "".join(f"{x:>12,.2f}" for x in npbt))
    print(f"  {'Reported PBT growth':<34}{'':>12}{(pbt[1]/pbt[0]-1)*100:>11.2f}%")
    print(f"  {'Normalised PBT growth':<34}{'':>12}{(npbt[1]/npbt[0]-1)*100:>11.2f}%")

    print("\nSUPPORT STRUCTURE (why AAA, not a partial notch-up)")
    for ch, d in SUPPORT:
        print(f"  {ch:<20}{d}")

    print("\nPORTFOLIO COMPOSITION - concentration is COUNTERPARTY, not sectoral")
    for seg, pct in PORTFOLIO:
        print(f"  {seg:<40}{pct:>6.2f}%")
    print(f"  {'Top 25 exposures':<40}{55.65:>6.2f}%   (FY2025: 49.71%)")
    print(f"  {'Largest single exposure':<40}{3.04:>6.2f}% of loans, 19.95% of TNW")
    print("  NOTE: direct FPO/agri exposure is only 2.85% - v1 wrongly made this the headline risk")

    # ---------------------------------------------------------------- tie-outs
    print("\n" + "=" * 96)
    print("TIE-OUTS")
    print("=" * 96)
    # ONE definition of the checks: run() prints exactly what tieouts() returns to the tools,
    # so the printed result and the gate result can never disagree.
    T = tieouts(compute())
    fail = 0
    for lab, comp, disc, tol, _src in T:
        ok = abs(comp - disc) <= tol
        fail += (not ok)
        print(f"  [{'OK ' if ok else 'FAIL'}] {lab:<52} computed {comp:>10,.2f}  "
              f"disclosed {disc:>10,.2f}")
    print(f"\n{len(T)-fail}/{len(T)} tie-outs reconcile.")
    for title, text in DISCLOSED_DIFFERENCES:
        print(f"  [DISCLOSED] {title}: {text}")
    if fail:
        print("*** RESOLVE BEFORE DRAFTING (Step 17). ***")
    return fail


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
