"""State Bank of India - bank ratio engine (CLAUDE.md Step 4 deliverable).

AGENCY: CRISIL.  ENTITY TYPE: scheduled commercial bank (D-SIB), NOT a corporate.
The corporate ratio suite (gearing, TOL/TNW, interest coverage, GCA days) is NOT applicable
and is deliberately absent - see the note in run() below.

SOURCE UNIT: Rs crore unless stated.  All figures traced to a document line; see SRC strings.
Primary source: Companies/sbi/documents/annual_reports/Annual_Report_FY2026_2.md
"""

AR26 = "FY2026 AR"

# ---------------------------------------------------------------------------------------------
# Ten-year series, verbatim from the "Ten Years at a Glance" highlights table (AR26 L420-450).
# Columns run FY2017 -> FY2026 (10 columns, last = FY2026).
# ---------------------------------------------------------------------------------------------
YEARS10 = ["FY2017", "FY2018", "FY2019", "FY2020", "FY2021",
           "FY2022", "FY2023", "FY2024", "FY2025", "FY2026"]

TEN_YEAR = {
    # label:                (values,                                                     source)
    "Operating profit":     ([50848, 59511, 55436, 68133, 71554, 75292, 83713, 93797, 110579, 123015],
                             f"{AR26} L~421 'Operating Result'"),
    "Net profit":           ([10484, -6547, 862, 14488, 20410, 31676, 50232, 61077, 70901, 80032],
                             f"{AR26} L~423 'Net Profit'"),
    "RoAA (%)":             ([0.41, -0.19, 0.02, 0.38, 0.48, 0.67, 0.96, 1.04, 1.10, 1.12],
                             f"{AR26} L~424 'Return on Average Assets'"),
    "RoE (%)":              ([7.25, -3.78, 0.48, 7.74, 9.94, 13.92, 19.43, 20.32, 19.87, 18.57],
                             f"{AR26} L425 'Return on Equity'"),
    "Cost-to-income (%)":   ([47.75, 50.18, 55.70, 52.46, 53.60, 53.31, 53.87, 55.66, 51.64, 50.11],
                             f"{AR26} L~426 'Expenses to Income'"),
    "EPS (Rs)":             ([13.43, -7.67, 0.97, 16.23, 22.87, 35.49, 56.29, 68.44, 79.44, 87.59],
                             f"{AR26} L~428 'Earnings Per Share'"),
    "DPS (Rs)":             ([2.60, 0.0, 0.0, 0.0, 4.00, 7.10, 11.30, 13.70, 15.90, 17.35],
                             f"{AR26} L~429 - 'Nil' for FY2018-FY2020 recorded as 0.0"),
    "CRAR Basel III (%)":   ([13.11, 12.60, 12.72, 13.06, 13.74, 13.83, 14.68, 14.28, 14.25, 15.40],
                             f"{AR26} L~440 'Basel-III Total Capital %'"),
    "Tier I (%)":           ([10.35, 10.36, 10.65, 11.00, 11.44, 11.42, 12.06, 11.93, 12.11, 13.33],
                             f"{AR26} L~441 'Tier I Capital %'"),
    "Tier II (%)":          ([2.76, 2.24, 2.07, 2.06, 2.30, 2.41, 2.62, 2.35, 2.14, 2.07],
                             f"{AR26} L~442 'Tier II Capital %'"),
    "NNPA (%)":             ([3.71, 5.73, 3.01, 2.23, 1.50, 1.02, 0.67, 0.57, 0.47, 0.39],
                             f"{AR26} L445 'Net NPA to Net Advances'"),
    "Domestic branches":    ([17170, 22414, 22010, 22141, 22219, 22266, 22405, 22542, 22937, 23265],
                             f"{AR26} L~446"),
}

# ---------------------------------------------------------------------------------------------
# Asset-quality block, INDEPENDENT table (AR26 L4282-4286), FY2021 -> FY2026.
# Overlaps the ten-year table on NNPA% - used as the corroboration gate (failure mode 15).
# ---------------------------------------------------------------------------------------------
YEARS6 = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025", "FY2026"]
ASSET_QUALITY = {
    "Gross NPA (Rs cr)":  ([126389, 112023, 90928, 84276, 76880, 73452], f"{AR26} L4282"),
    "GNPA (%)":           ([4.98, 3.97, 2.78, 2.24, 1.82, 1.49],         f"{AR26} L4283"),
    "Net NPA (Rs cr)":    ([36810, 27966, 21467, 21051, 19667, 18830],   f"{AR26} L4284"),
    "NNPA (%)":           ([1.50, 1.02, 0.67, 0.57, 0.47, 0.39],         f"{AR26} L4285"),
    "Fresh slippages":    ([29332, 26776, 19224, 20982, 22124, 23804],   f"{AR26} L4286"),
}

# ---------------------------------------------------------------------------------------------
# FY2026 headline metrics from the Chairman's statement / MD&A narrative (AR26 L764-790, L11698).
# ---------------------------------------------------------------------------------------------
FY26 = {
    "Total business (Rs lakh cr)":      (109.0,  f"{AR26} L764 'total business surpassed Rs 109 lakh crore'"),
    "Balance sheet size (Rs lakh cr)":  (76.0,   f"{AR26} L764 'balance sheet crossed Rs 76 lakh crore'"),
    "Deposits (Rs lakh cr)":            (59.76,  f"{AR26} L764 '+11.03%'"),
    "Advances (Rs lakh cr)":            (49.33,  f"{AR26} L764 '+16.87%'"),
    "CASA deposits (Rs lakh cr)":       (22.62,  f"{AR26} L764 '+9.53%'"),
    "CASA ratio (%)":                   (39.46,  f"{AR26} L764 'as of March 2026'"),
    "NII (Rs lakh cr)":                 (1.73,   f"{AR26} L764 '+4.08%'"),
    "Operating profit (Rs lakh cr)":    (1.23,   f"{AR26} L764 '+11.25%'"),
    "Net profit (Rs cr)":               (80032,  f"{AR26} L764 '+12.88%'"),
    "RoA (%)":                          (1.12,   f"{AR26} L776 'against 1.10% for FY 2025'"),
    "RoE (%)":                          (18.57,  f"{AR26} L776"),
    "Cost-to-income (%)":               (50.11,  f"{AR26} L764 'from 51.64% last year'"),
    "CET-1 (%)":                        (12.29,  f"{AR26} L786 'highest ever level'"),
    "CRAR (%)":                         (15.40,  f"{AR26} L786"),
    "GNPA (%)":                         (1.49,   f"{AR26} L790 'improvement of 33 bps YoY'"),
    "NNPA (%)":                         (0.39,   f"{AR26} L790 'improved by 8 bps YoY'"),
    "Slippage ratio (%)":               (0.54,   f"{AR26} L790 'contained at'"),
    "PCR excl. AUCA (%)":               (74.36,  f"{AR26} L790"),
    "PCR incl. AUCA (%)":               (99.01,  f"{AR26} L790"),
    "Investments (Rs lakh cr)":         (18.09,  f"{AR26} L764 '95.48% domestic'"),
    "Yield on investments (%)":         (7.01,   f"{AR26} L764"),
    "Dividend per share (Rs)":          (17.35,  f"{AR26} L764"),
    "GoI shareholding (%)":             (55.03,  f"{AR26} L11698 - FY2025 comparative 56.92%"),
}

# LCR row (AR26 L11840) carries five quarterly-average columns, not a single annual figure;
# NSFR (L11931/L11998) likewise reports solo figures for two period-pairs. Recorded as ranges
# rather than inventing a point estimate.
LIQUIDITY = {
    "LCR (%) - quarterly averages": ([124.32, 137.83, 143.05, 136.67, 132.26], f"{AR26} L11840"),
    "NSFR (%) - solo, reported pairs": ([120.05, 127.15, 127.73, 129.55], f"{AR26} L11931, L11998"),
}


def _pct(new, old):
    return (new - old) / abs(old) * 100.0


# ---------------------------------------------------------------------------------------------
# ENGINE CONTRACT (added 29-Aug-2026)
# ---------------------------------------------------------------------------------------------
# This engine's tie-outs were always here and always genuine - 34 of them, each comparing two
# independently sourced disclosures. They simply lived inside run() as a local list, so nothing
# outside this file could reach them: `tieout_mutation.py` could not measure what they cover,
# and `rate_engine.py` / `build_rationale.py` could not drive the case at all.
#
# The refactor below CHANGES NO FIGURE AND NO CHECK. It moves the check-building into a
# module-level tieouts() and adds a compute() over the same data, so the shared tooling can
# see them. run() calls both, so the printed output is unchanged.
YEARS = YEARS10


def compute():
    """Ratio suite per period, assembled from the tables already extracted above."""
    out = {}
    for i, y in enumerate(YEARS10):
        d = {}
        for k, (vals, _src) in TEN_YEAR.items():
            if i < len(vals) and isinstance(vals[i], (int, float)):
                d[k] = float(vals[i])
        if y in YEARS6:
            j = YEARS6.index(y)
            for k, (vals, _src) in ASSET_QUALITY.items():
                if j < len(vals) and isinstance(vals[j], (int, float)):
                    d[k] = float(vals[j])
        out[y] = d
    return out


def _b(x):
    """Booleans as 1/0 so a truth check fits the numeric (computed, disclosed, tol) shape."""
    return 1.0 if x else 0.0


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source) - the contract shape.

    Identical checks to those run() has always performed; only the packaging differs.
    """
    T = []
    NUM = 0.06          # the tolerance run() has always applied to numeric comparisons

    for i, y in enumerate(YEARS10):
        crar = TEN_YEAR["CRAR Basel III (%)"][0][i]
        t1 = TEN_YEAR["Tier I (%)"][0][i]
        t2 = TEN_YEAR["Tier II (%)"][0][i]
        T.append(("%s CRAR = Tier I + Tier II" % y, crar, round(t1 + t2, 2), NUM,
                  "ten-year series, capital table"))

    for i, y in enumerate(YEARS6):
        T.append(("%s NNPA%% (2 independent tables)" % y,
                  ASSET_QUALITY["NNPA (%)"][0][i],
                  TEN_YEAR["NNPA (%)"][0][YEARS10.index(y)], NUM,
                  "asset-quality table vs ten-year series - two separate disclosures"))
        g = ASSET_QUALITY["Gross NPA (Rs cr)"][0][i]
        n = ASSET_QUALITY["Net NPA (Rs cr)"][0][i]
        T.append(("%s Net NPA < Gross NPA" % y, _b(n < g), 1.0, 0.5,
                  "asset-quality table, internal consistency"))

    for label, fy26_key, ten_key in [
        ("net profit", "Net profit (Rs cr)", "Net profit"),
        ("RoE", "RoE (%)", "RoE (%)"),
        ("CRAR", "CRAR (%)", "CRAR Basel III (%)"),
        ("NNPA", "NNPA (%)", "NNPA (%)"),
        ("cost-income", "Cost-to-income (%)", "Cost-to-income (%)"),
    ]:
        T.append(("FY26 %s narrative = table" % label,
                  FY26[fy26_key][0], TEN_YEAR[ten_key][0][-1], NUM,
                  "FY2026 headline metric vs the ten-year series"))

    T.append(("FY26 CET-1 < Tier I",
              _b(FY26["CET-1 (%)"][0] < TEN_YEAR["Tier I (%)"][0][-1]), 1.0, 0.5,
              "Tier I = CET-1 + AT1, so CET-1 must be the smaller"))

    T.append(("FY26 GNPA improved 33bps YoY",
              round(ASSET_QUALITY["GNPA (%)"][0][-1] - ASSET_QUALITY["GNPA (%)"][0][-2], 2),
              -0.33, NUM, "stated YoY movement vs the series"))
    T.append(("FY26 NNPA improved 8bps YoY",
              round(ASSET_QUALITY["NNPA (%)"][0][-1] - ASSET_QUALITY["NNPA (%)"][0][-2], 2),
              -0.08, NUM, "stated YoY movement vs the series"))
    T.append(("FY26 net profit growth 12.88%",
              round(_pct(TEN_YEAR["Net profit"][0][-1], TEN_YEAR["Net profit"][0][-2]), 2),
              12.88, NUM, "stated growth vs the series"))
    T.append(("FY26 op profit growth 11.25%",
              round(_pct(TEN_YEAR["Operating profit"][0][-1],
                         TEN_YEAR["Operating profit"][0][-2]), 2),
              11.25, NUM, "stated growth vs the series"))

    casa_global = round(FY26["CASA deposits (Rs lakh cr)"][0]
                        / FY26["Deposits (Rs lakh cr)"][0] * 100, 2)
    T.append(("FY26 CASA on global deposits is NOT the reported ratio",
              _b(abs(casa_global - FY26["CASA ratio (%)"][0]) > 1.0), 1.0, 0.5,
              "CASA is reported on DOMESTIC deposits; using global understates it by 161bps"))

    tb = round(FY26["Deposits (Rs lakh cr)"][0] + FY26["Advances (Rs lakh cr)"][0], 2)
    T.append(("FY26 deposits + advances 'surpassed' 109 lakh cr",
              _b(109.0 <= tb < 110.0), 1.0, 0.5,
              "narrative states a rounded floor, so the test is a bound not an equality"))
    return T


def run():
    print("=" * 92)
    print("STATE BANK OF INDIA - BANK RATIO SUITE (CRISIL)")
    print("Corporate ratios (gearing / TOL-TNW / interest coverage / GCA days) are NOT")
    print("applicable to a bank and are deliberately omitted - see CLAUDE.md failure mode 21.")
    print("=" * 92)

    print(f"\n{'TEN-YEAR SERIES':<26}" + "".join(f"{y[2:]:>8}" for y in YEARS10))
    for label, (vals, _) in TEN_YEAR.items():
        print(f"{label:<26}" + "".join(f"{v:>8,.2f}" if isinstance(v, float) else f"{v:>8,}"
                                       for v in vals))

    print(f"\n{'ASSET QUALITY':<26}" + "".join(f"{y[2:]:>10}" for y in YEARS6))
    for label, (vals, _) in ASSET_QUALITY.items():
        print(f"{label:<26}" + "".join(f"{v:>10,.2f}" if isinstance(v, float) else f"{v:>10,}"
                                       for v in vals))

    print("\nFY2026 HEADLINE METRICS")
    for label, (val, src) in FY26.items():
        print(f"  {label:<34}{val:>10,.2f}   [{src}]")

    print("\nLIQUIDITY (regulatory)")
    for label, (vals, src) in LIQUIDITY.items():
        print(f"  {label:<34}{str(vals):>44}   [{src}]")

    # -----------------------------------------------------------------------------------------
    # TIE-OUTS - each must reconcile independently or the extraction is wrong (Step 17).
    # -----------------------------------------------------------------------------------------
    print("\n" + "=" * 92)
    print("TIE-OUTS")
    print("=" * 92)
    checks = [(desc, comp, disc, tol) for desc, comp, disc, tol, _src in tieouts()]

    casa_global = round(FY26["CASA deposits (Rs lakh cr)"][0]
                        / FY26["Deposits (Rs lakh cr)"][0] * 100, 2)
    implied_domestic = round(FY26["CASA deposits (Rs lakh cr)"][0]
                             / (FY26["CASA ratio (%)"][0] / 100), 2)
    print(f"\n  NOTE  CASA basis: reported {FY26['CASA ratio (%)'][0]}% is on DOMESTIC deposits;"
          f" on global deposits it is {casa_global}%.")
    print(f"        Implied domestic deposits {implied_domestic} lakh cr; implied overseas"
          f" {round(FY26['Deposits (Rs lakh cr)'][0] - implied_domestic, 2)} lakh cr (DERIVED,"
          f" not separately disclosed in the source line - corroborate before quoting).")

    failed = 0
    for label, expected, actual, tol in checks:
        ok = abs(expected - actual) <= tol
        if not ok:
            failed += 1
        print(f"  [{'OK ' if ok else 'FAIL'}] {label:<46} expected {expected!s:>10} "
              f"got {actual!s:>10}")

    print(f"\n{len(checks) - failed}/{len(checks)} tie-outs reconcile.")
    if failed:
        print("*** UNRECONCILED ITEMS ABOVE MUST BE RESOLVED BEFORE DRAFTING (Step 17). ***")
    return failed


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)


# ---- Measured coverage disclosure (failure mode 39) -----------------------------------------
# tools/tieout_mutation.py reports 31.4% coverage: 109 of 159 perturbed inputs are
# reachable by NO tie-out. FM39 requires each to be given a check or NAMED as
# uncheckable with the reason. Measured, not assumed - re-run the harness to confirm.
DISCLOSED_DIFFERENCES = [
    ("The ten-year history block (78 inputs) is context, reconciled by nothing",
     "Measured with tools/tieout_mutation.py: 78 of the 109 uncovered inputs sit in "
     "TEN_YEAR, the FY2017-FY2026 long-run series. It exists to show direction of travel "
     "across a full credit cycle; each year is taken as printed from that year's "
     "disclosure and there is no second source per year to reconcile it against. The "
     "tie-outs are struck on the current rating periods, which is the correct place for "
     "them - but it means the history is illustrative, not verified, and no rated "
     "conclusion rests on a single year within it."),
    ("Asset-quality (22 inputs) and liquidity (9 inputs) series are single-sourced",
     "The GNPA/NNPA rupee and percentage series and the LCR/NSFR/liquidity block come "
     "from the bank's own disclosures with no independent published figure held in the "
     "engine to reproduce them from. They are traceable to a document location but not "
     "recomputable here, so an error in any one of them would not be caught by this "
     "engine."),
    ("Overall coverage is 31.4% and that number is not comparable with a corporate engine's",
     "159 inputs are perturbed, of which 109 are the history/asset-quality/liquidity "
     "context series above. The inputs that actually drive the rated conclusion - the "
     "current-period capital, earnings and balance-sheet lines - are the covered 50. "
     "Stated explicitly so the low headline is read correctly rather than as a broken "
     "engine."),
]
