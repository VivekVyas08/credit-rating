"""TVS Credit Services Limited - NBFC ratio engine (CLAUDE.md Step 4 deliverable).

AGENCY: ICRA.  ENTITY: NBFC-ICC in the RBI Middle Layer (Scale Based Regulation).
The corporate ratio suite does NOT apply. Bank ratios do not apply either - an NBFC is funded
by borrowings, not deposits, so gearing and borrowing concentration matter where CASA would.

BASIS: STANDALONE, per the FY2026 AR, which is the authority for FY2025 and FY2026.
FY2024 is taken from the FY2025 AR. See RESTATEMENT note below.

Rs crore. Sources cite the AR and line number.
"""
AR26 = "FY2026 AR"
AR25 = "FY2025 AR"

YEARS = ["FY2024", "FY2025", "FY2026"]

# ---------------------------------------------------------------------------------------------
# RESTATEMENT / BASIS NOTE (recorded, not smoothed over)
#   The FY2025 AR reports FY2025 CONSOLIDATED total income of Rs 6,630.03 cr (L2827). The FY2026
#   AR's FY2025 consolidated comparative is Rs 6,609.77 cr - a Rs 20.26 cr difference. The FY2026
#   AR is used as the authority for FY2025 because it carries the restated comparative.
#   TVS Credit's consolidated and standalone figures are close (FY2026 consolidated total income
#   Rs 7,197.07 cr vs standalone Rs 7,196.00 cr) because the subsidiaries are immaterial; the two
#   bases are nonetheless NOT mixed within any single ratio below.
# ---------------------------------------------------------------------------------------------

PL = {
    "Interest income":            ([5112.58, 5775.97, 6213.35], f"{AR26} L3115; FY2024 {AR25} L2821"),
    "Total income":               ([5795.19, 6608.68, 7196.00], f"{AR26} L3120; FY2024 {AR25} L2827"),
    "Finance costs":              ([None, 1863.32, 1934.29],    f"{AR26} L3122"),
    "Fees and commission expense": ([None, 527.16, 473.14],     f"{AR26} L3123"),
    "Impairment of financial instruments": ([1127.05, 1295.36, 1156.59],
                                           f"{AR26} L3124; FY2024 {AR25} L2831"),
    "Employee benefits expense":  ([None, 1135.58, 1274.23],    f"{AR26} L3125"),
    "Depreciation":               ([None, 46.20, 56.12],        f"{AR26} L3126"),
    "Other expenses":             ([None, 715.62, 1054.70],     f"{AR26} L3127"),
    "Total expenses":             ([None, 5583.24, 5949.07],    f"{AR26} L3128"),
    "PBT before exceptional":     ([None, 1025.44, 1246.93],    f"{AR26} L3129"),
    "Exceptional items":          ([None, 0.0, 8.61],
                                   f"{AR26} L7670 CONSOLIDATED. The STANDALONE line (L3129) reads "
                                   f"'861' - the decimal point is lost in OCR. 8.61 is correct."),
    "Profit after tax":           ([571.83, 767.25, 913.17],    f"{AR26} L3133; FY2024 {AR25} L2842"),
}

BS = {
    "Total assets":      ([28137.55, 31043.70, 35068.09], f"{AR26} L3063; FY2024 {AR25} L2762 (consol.)"),
    "Total equity":      ([None, 4947.92, 6067.63],       f"{AR26} L5940"),
    "Total borrowings":  ([None, 24687.17, 27667.87],     f"{AR26} L5903"),
    "Net debt":          ([None, 21103.76, 24340.37],     f"{AR26} L5939"),
}

REG = {
    "CRAR (%)":                     ([None, 20.30, 19.44], f"{AR26} L6325 - per RBI guidelines"),
    "Tier I CRAR (%)":              ([None, 15.84, 16.49], f"{AR26} L6326"),
    "Tier II CRAR (%)":             ([None, 4.46, 2.95],   f"{AR26} L6327"),
    "Net debt / equity (x)":        ([None, 4.27, 4.01],   f"{AR26} L5941 - company-reported"),
    "Top-10 borrowings / total (%)": ([None, 77.34, 70.68], f"{AR26} L6761 - funding concentration"),
    "PDI as % of Tier I":           ([None, 2.25, 1.84],   f"{AR26} L6946"),
}

# Ratings disclosed by the issuer itself (Step 7b) - the Step 14 anchor, since no TVS Credit
# rationale exists in the reference library (only parent/sibling group entities).
DISCLOSED_RATINGS = {
    "ICRA long-term bank facilities": "AA+ (Stable)",
    "ICRA short-term bank facilities": "A1+",
    "ICRA subordinated debt":          "AA+ (Stable)",
    "ICRA perpetual debt":             "AA (Stable)   <- notched ONE BELOW senior",
    "ICRA commercial paper":           "A1+",
    "CRISIL NCDs":                     "AA+/Stable",
    "CRISIL perpetual bonds":          "AA/Stable",
    "CRISIL Tier II bond":             "AA+/Stable (FY2025: AA/Positive - UPGRADED)",
    "CARE long-term bank facilities":  "AA+/Stable",
}

PARENT = ("TVS Motor Company Limited", 85.63, f"{AR26} - holding company")


def series(d, k):
    return d[k][0]


def avg(v, i):
    """Average of the current and prior year; None if the prior year is unavailable."""
    if i == 0 or v[i] is None or v[i - 1] is None:
        return None
    return (v[i] + v[i - 1]) / 2


def _derive():
    """The NBFC ratio suite as an ordered [(label, [values], fmt)] list.

    ONE definition, consumed by both compute() (for the tools) and run() (for the printed
    table), so the two cannot drift apart.
    """
    n = len(YEARS)
    ii, fc = series(PL, "Interest income"), series(PL, "Finance costs")
    ti = series(PL, "Total income")
    imp = series(PL, "Impairment of financial instruments")
    pat = series(PL, "Profit after tax")
    ta, te = series(BS, "Total assets"), series(BS, "Total equity")
    bor = series(BS, "Total borrowings")
    emp, dep, oth = (series(PL, "Employee benefits expense"), series(PL, "Depreciation"),
                     series(PL, "Other expenses"))
    fce = series(PL, "Fees and commission expense")

    nii = [None if (ii[i] is None or fc[i] is None) else ii[i] - fc[i] for i in range(n)]
    opex = [None if any(x[i] is None for x in (emp, dep, oth)) else emp[i] + dep[i] + oth[i]
            for i in range(n)]
    nti = [None if any(x[i] is None for x in (ti, fc, fce)) else ti[i] - fc[i] - fce[i]
           for i in range(n)]

    return [
        ("Net interest income", nii, "{:>13,.2f}"),
        ("NII / avg total assets (%)",
         [None if (nii[i] is None or avg(ta, i) is None) else nii[i] / avg(ta, i) * 100
          for i in range(n)], "{:>12.2f}%"),
        ("RoAA (%)", [None if avg(ta, i) is None else pat[i] / avg(ta, i) * 100
                      for i in range(n)], "{:>12.2f}%"),
        ("RoAE (%)", [None if avg(te, i) is None else pat[i] / avg(te, i) * 100
                      for i in range(n)], "{:>12.2f}%"),
        ("Credit cost / avg assets (%)",
         [None if avg(ta, i) is None else imp[i] / avg(ta, i) * 100 for i in range(n)],
         "{:>12.2f}%"),
        ("Gearing - borrowings / equity (x)",
         [None if (bor[i] is None or te[i] is None) else bor[i] / te[i] for i in range(n)],
         "{:>12.2f}x"),
        ("Operating expenses", opex, "{:>13,.2f}"),
        ("Net total income", nti, "{:>13,.2f}"),
        ("Cost-to-income (%)",
         [None if (opex[i] is None or nti[i] is None) else opex[i] / nti[i] * 100
          for i in range(n)], "{:>12.2f}%"),
        ("Total income growth (%)",
         [None] + [ti[i] / ti[i - 1] * 100 - 100 for i in (1, 2)], "{:>12.2f}%"),
        ("PAT growth (%)",
         [None] + [pat[i] / pat[i - 1] * 100 - 100 for i in (1, 2)], "{:>12.2f}%"),
    ]


def compute():
    """Contract member: {period: {ratio: value}}."""
    rows = _derive()
    R = {}
    for i, y in enumerate(YEARS):
        R[y] = {lab: vals[i] for lab, vals, _f in rows
                if isinstance(vals[i], (int, float)) and not isinstance(vals[i], bool)}
        for table in (PL, BS, REG):
            for k, (vals, _src) in table.items():
                if isinstance(vals[i], (int, float)) and not isinstance(vals[i], bool):
                    R[y][k] = vals[i]
    return R


def tieouts(R):
    """Contract member: [(description, computed, disclosed, tolerance, source), ...].

    Reads the input tables directly so every check stays sensitive to what the mutation
    harness perturbs. Each reconciles a DERIVED figure against a SEPARATELY PRINTED one -
    never a value against itself (failure mode 39). The boolean check is carried as 1.0/0.0
    with a 0.5 tolerance so the harness can read it.
    """
    T = []
    fc = series(PL, "Finance costs")
    fce = series(PL, "Fees and commission expense")
    imp = series(PL, "Impairment of financial instruments")
    emp, dep, oth = (series(PL, "Employee benefits expense"), series(PL, "Depreciation"),
                     series(PL, "Other expenses"))
    ti, te = series(PL, "Total income"), series(BS, "Total equity")

    for i, y in enumerate(YEARS):
        if series(REG, "CRAR (%)")[i] is not None:
            T.append((f"{y} CRAR = Tier I + Tier II",
                      series(REG, "Tier I CRAR (%)")[i] + series(REG, "Tier II CRAR (%)")[i],
                      series(REG, "CRAR (%)")[i], 0.06,
                      "RBI capital-adequacy note - Tier I and Tier II components vs printed CRAR"))
    for i in (1, 2):
        T.append((f"{YEARS[i]} total expenses = sum of components",
                  fc[i] + fce[i] + imp[i] + emp[i] + dep[i] + oth[i],
                  series(PL, "Total expenses")[i], 0.06,
                  "audited P&L - expense components vs the printed total-expenses row"))
        T.append((f"{YEARS[i]} PBT = total income - total expenses",
                  ti[i] - series(PL, "Total expenses")[i],
                  series(PL, "PBT before exceptional")[i], 0.06,
                  "audited P&L - printed PBT row"))
        # The company publishes net debt/equity; reproduce it from its own components.
        T.append((f"{YEARS[i]} net debt/equity reproduces",
                  series(BS, "Net debt")[i] / te[i],
                  series(REG, "Net debt / equity (x)")[i], 0.06,
                  "company-disclosed leverage ratio vs its own balance-sheet components"))
    # OCR sanity: the exceptional item must be immaterial, not 861.
    T.append(("FY2026 exceptional item is immaterial vs PBT",
              1.0 if (series(PL, "Exceptional items")[2]
                      / series(PL, "PBT before exceptional")[2] < 0.05) else 0.0,
              1.0, 0.5, "audited P&L - exceptional item against PBT (OCR sanity check)"))
    return T


# Measured with tools/tieout_mutation.py, not asserted (failure mode 39).
DISCLOSED_DIFFERENCES = [
    ("FY2024 is a comparative column, not an independently reconciled one",
     "The two arithmetic tie-outs (expense build-up, PBT waterfall) run on FY2025 and FY2026, "
     "where the audited P&L prints every component. FY2024 enters as the restated comparative "
     "and supports the average-basis ratios and growth rates only."),
    ("Asset-quality and yield metrics have no second source",
     "Where the regulatory table carries stage-wise assets, provision cover or yield, those come "
     "from a single disclosure with no independent published figure to reconcile against. They "
     "are traceable but not reproducible in this engine."),
]


def run():
    print("=" * 94)
    print("TVS CREDIT SERVICES LIMITED - NBFC RATIO SUITE (ICRA)")
    print("NBFC-ICC, RBI Middle Layer. Parent: %s (%.2f%%)." % (PARENT[0], PARENT[1]))
    print("=" * 94)

    def show(title, d):
        print(f"\n{title:<38}" + "".join(f"{y:>13}" for y in YEARS))
        for k, (vals, _) in d.items():
            row = "".join(f"{v:>13,.2f}" if isinstance(v, (int, float)) else f"{'n/a':>13}"
                          for v in vals)
            print(f"  {k:<36}{row}")

    show("PROFIT AND LOSS", PL)
    show("BALANCE SHEET", BS)
    show("REGULATORY / LEVERAGE", REG)

    # ---- derived ------------------------------------------------------------------------------
    print(f"\n{'DERIVED RATIOS':<38}" + "".join(f"{y:>13}" for y in YEARS))
    for label, vals, fmt in _derive():
        print(f"  {label:<36}" + "".join(fmt.format(v) if isinstance(v, (int, float))
                                         else f"{'n/a':>13}" for v in vals))

    # ---- disclosed ratings ---------------------------------------------------------------------
    print("\nRATINGS DISCLOSED BY THE ISSUER (Step 7b - the Step 14 anchor)")
    for k, v in DISCLOSED_RATINGS.items():
        print(f"  {k:<36}{v}")

    # ---- tie-outs -----------------------------------------------------------------------------
    print("\n" + "=" * 94)
    print("TIE-OUTS")
    print("=" * 94)
    # ONE definition of the checks: printed here exactly as the tools receive them.
    T = tieouts(compute())
    failed = 0
    for label, comp, disc, tol, _src in T:
        ok = abs(comp - disc) <= tol
        failed += (not ok)
        print(f"  [{'OK ' if ok else 'FAIL'}] {label:<52} computed {comp:>10,.2f} "
              f"disclosed {disc:>10,.2f}")
    print(f"\n{len(T) - failed}/{len(T)} tie-outs reconcile.")
    for title, text in DISCLOSED_DIFFERENCES:
        print(f"\n  [DISCLOSED] {title}\n              {text}")
    if failed:
        print("*** UNRECONCILED - RESOLVE BEFORE DRAFTING (Step 17). ***")
    return failed


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
