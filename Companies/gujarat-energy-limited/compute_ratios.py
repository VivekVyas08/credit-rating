"""Gujarat Energy Limited (formerly Gujarat Gas Limited) - CareEdge ratio suite.

AGENCY: CareEdge.  ENTITY: city gas distribution, now an integrated energy company. State-owned.
Methodology: CGD Companies (Mar 2025) primary; Wholesale Trading (Mar 2025) for the gas-trading
segment; Infrastructure Sector (Mar 2025) and Consolidation & Combined Approach (Mar 2025).

*** TWO BASES - NEVER MIX THEM (failure mode 26; the NABKISAN lesson) ***
The GSPC Group Composite Scheme of Arrangement took effect 01-May-2026:
  IN  : gas trading, E&P assets, wind power generation, investments
  OUT : gas transmission, demerged into GSPL Transmission Limited (separate listing underway)
  Gujarat Gas Limited was renamed Gujarat Energy Limited. CIN L40200GJ2012SGC069118 unchanged.

  BASIS A - MERGED ENTITY, from the Q4 FY2026 press release (30-May-2026, the NEWEST document).
            FY2026 AND the FY2025 comparative are BOTH on the merged basis -> like-for-like.
  BASIS B - GUJARAT GAS STANDALONE, from the annual reports (FY2023-FY2025), PRE-scheme.

  PROOF the bases differ: FY2025 total income is Rs 17,394.94 cr on Basis B and Rs 27,718 cr on
  Basis A - a Rs 10,323 cr gap, being the incoming trading/E&P/wind businesses. Splicing the two
  would manufacture ~59% of revenue growth that did not happen.

Rs CRORE throughout (both sources report in Rs crore).
  BASIS A : press-release-4th-qtr-and-year-ended-march-2026.md
  BASIS B : 13th_Annual_Report_2024-25_2.md - BS L5790-5850, P&L L5855-5890
"""

# ---- BASIS A: merged entity (the rated entity) ----------------------------------------------
A_YEARS = ["FY2025", "FY2026"]
PR = "Q4 FY2026 press release, 30-May-2026 (merged basis)"
MERGED = {
    "Revenue from operations": ([27718, 24198], PR),
    "EBITDA":                  ([3677, 3772],   PR),
    "Profit after tax":        ([None, 2299],   PR + " - FY2025 PAT not given on merged basis"),
    "Net worth":               ([None, 18517],  PR + " - as on 31-03-2026"),
    "EPS (Rs)":                ([None, 24.50],  PR),
    "Dividend per share (Rs)": ([None, 8.90],   PR + " - 445% of Rs 2 face value; highest ever"),
}
Q4 = {"Revenue": (6560, 5976), "EBITDA": (799, 943), "PAT": (None, 521)}   # Q4FY25, Q4FY26

# ---- Sales volumes, mmscmd - THE CGD sector-defining metric (failure mode 21) ----------------
VOLUMES = {                       # [Q4 FY2026, FY2025-26]
    # Lists, not tuples, so tools/tieout_mutation.py can perturb them and prove the three
    # volume tie-outs below actually cover them. As tuples they were immutable and the
    # harness reported them as uncovered when in fact they were checked.
    "CGD segment (A)":       [8.88, 8.69],
    "  Industrial":          [4.19, 4.29],
    "  CNG":                 [3.60, 3.43],
    "  PNG - domestic":      [0.91, 0.82],
    "  PNG - commercial":    [0.17, 0.16],
    "Gas trading segment (B)": [4.63, 4.94],
    "TOTAL (A+B)":           [13.51, 13.63],
}
OPERATIONAL = [
    ("CNG volume, Q4", "3.60 mmscmd vs 3.22 in Q4 FY2025 - highest ever, +12% YoY"),
    ("CNG stations", "839 total; 14 added in FY2026, of which 7 under FDODO"),
    ("PNG domestic", "24.18 lakh households; 35,400+ added in Q4 FY2026"),
    ("LPG substitution", "2,835 societies / 4.86 lakh households fully PNG-connected by May 2026"),
    ("Morbi ceramic cluster", "gas-consuming units 83 -> 675; consumption 0.36 -> 7.8 MMSCMD"),
]

# ---- BASIS B: Gujarat Gas standalone, pre-scheme ---------------------------------------------
B_YEARS = ["FY2024", "FY2025"]
AR = "FY2024-25 annual report (Gujarat Gas standalone, PRE-scheme)"
STANDALONE = {
    "Revenue from operations": ([16292.97, 17184.97], AR + " P&L L~5859"),
    "Other income":            ([107.75, 209.97],     AR + " P&L L~5860"),
    "Total income":            ([16400.72, 17394.94], AR + " P&L L5858"),
    "Excise duty":             ([602.78, 698.02],     AR + " P&L - shown as an EXPENSE"),
    "Finance costs":           ([29.31, 32.49],       AR + " P&L L~5866"),
    "Depreciation":            ([474.30, 510.64],     AR + " P&L L~5867"),
    "Profit before tax":       ([1536.21, 1546.60],   AR + " P&L L~5872"),
    "Profit after tax":        ([1142.77, 1145.51],   AR + " P&L L~5878"),
    "Borrowings - non-current": ([0.0, 0.0],          AR + " BS L~5815 - NIL"),
    "Borrowings - current":    ([0.0, 0.0],           AR + " BS L~5823 - NIL"),
    "Lease liabilities - NC":  ([117.77, 115.16],     AR + " BS L~5816"),
    "Cash & equivalents":      ([915.98, 326.86],     AR + " BS L~5803"),
    "Other bank balances":     ([10.14, 32.54],       AR + " BS L~5804"),
    "Total equity":            ([7689.26, 8453.65],   AR + " BS L~5813"),
    "Total assets":            ([11658.35, 12615.12], AR + " BS L~5810"),
    "Trade receivables":       ([1029.84, 1023.97],   AR + " BS L~5802"),
    "Inventories":             ([58.67, 61.86],       AR + " BS L~5799"),
    "Deferred tax liability":  ([910.75, 958.88],     AR + " BS L~5818"),
}

# ---- Ratings disclosed by the issuer (Step 7b -> Step 14 anchor) -----------------------------
DISCLOSED = [
    ("India Ratings", "Bank loan facilities", "IND AAA/Stable / IND A1+", "27-08-2024"),
    ("CARE Ratings",  "Bank loan facilities", "CARE AAA; Stable / CARE A1+", "09-09-2024"),
    ("CRISIL Ratings", "Bank loan facilities", "CRISIL AAA/Watch Developing", "10-09-2024"),
    ("CRISIL Ratings", "Bank loan facilities", "CRISIL AAA/Stable (reaffirmed)", "09-12-2024"),
]


# The contract needs ONE period list. These two bases are deliberately NOT spliced (see the
# module docstring): the merged entity and pre-scheme Gujarat Gas standalone are different
# reporting entities, and R5 forbids mixing bases in one row. So the basis is carried IN THE
# PERIOD LABEL - every downstream tool then shows it rather than silently blending the two.
YEARS = ["FY2024 (standalone)", "FY2025 (standalone)", "FY2025 (merged)", "FY2026 (merged)"]


def _derive_standalone():
    """Basis B ratio suite as [(label, [v_FY2024, v_FY2025], fmt)] - Gujarat Gas standalone."""
    s = {k: v[0] for k, v in STANDALONE.items()}
    n = len(B_YEARS)
    pbildt = [s["Profit before tax"][i] + s["Finance costs"][i] + s["Depreciation"][i]
              - s["Other income"][i] for i in range(n)]
    net = [s["Revenue from operations"][i] - s["Excise duty"][i] for i in range(n)]
    debt = [s["Borrowings - non-current"][i] + s["Borrowings - current"][i]
            + s["Lease liabilities - NC"][i] for i in range(n)]
    cash = [s["Cash & equivalents"][i] + s["Other bank balances"][i] for i in range(n)]
    return [
        ("PBILDT", pbildt, "{:>14,.2f}"),
        ("PBILDT margin on gross revenue (%)",
         [pbildt[i] / s["Revenue from operations"][i] * 100 for i in range(n)], "{:>13.2f}%"),
        ("Revenue NET of excise", net, "{:>14,.2f}"),
        ("PBILDT margin net of excise (%)",
         [pbildt[i] / net[i] * 100 for i in range(n)], "{:>13.2f}%"),
        ("Adjusted debt (leases only)", debt, "{:>14,.2f}"),
        ("Overall gearing (x)",
         [debt[i] / s["Total equity"][i] for i in range(n)], "{:>13.3f}x"),
        ("Net debt / (net cash)", [debt[i] - cash[i] for i in range(n)], "{:>14,.2f}"),
        ("Interest coverage (x)",
         [pbildt[i] / s["Finance costs"][i] for i in range(n)], "{:>13.1f}x"),
        ("TOL / TNW (x)",
         [(s["Total assets"][i] - s["Total equity"][i]) / s["Total equity"][i]
          for i in range(n)], "{:>13.2f}x"),
    ]


def compute():
    """Contract member: {period: {ratio: value}}, basis carried in the period label."""
    R = {y: {} for y in YEARS}
    for i, y in enumerate(B_YEARS):                       # standalone, Basis B
        key = f"{y} (standalone)"
        for k, (vals, _src) in STANDALONE.items():
            if isinstance(vals[i], (int, float)):
                R[key][k] = vals[i]
        for lab, vals, _f in _derive_standalone():
            R[key][lab] = vals[i]
    for i, y in enumerate(A_YEARS):                       # merged, Basis A
        key = f"{y} (merged)"
        for k, (vals, _src) in MERGED.items():
            if isinstance(vals[i], (int, float)):
                R[key][k] = vals[i]
    return R


def tieouts(R):
    """Contract member: [(description, computed, disclosed, tolerance, source), ...].

    Reads the input tables directly so the mutation harness's perturbations are visible.
    Booleans carried as 1.0/0.0 with a 0.5 tolerance.
    """
    s = {k: v[0] for k, v in STANDALONE.items()}
    T = []
    debt = [s["Borrowings - non-current"][i] + s["Borrowings - current"][i]
            + s["Lease liabilities - NC"][i] for i in range(len(B_YEARS))]
    cash = [s["Cash & equivalents"][i] + s["Other bank balances"][i]
            for i in range(len(B_YEARS))]
    for i in range(len(B_YEARS)):
        y = B_YEARS[i]
        T.append((f"{y} total income = revenue + other income",
                  s["Revenue from operations"][i] + s["Other income"][i],
                  s["Total income"][i], 0.06, AR + " - printed total income row"))
        T.append((f"{y} borrowings are NIL",
                  s["Borrowings - non-current"][i] + s["Borrowings - current"][i],
                  0.0, 0.06, AR + " - both borrowing lines"))
        T.append((f"{y} company is in NET CASH",
                  1.0 if (debt[i] - cash[i]) < 0 else 0.0, 1.0, 0.5,
                  AR + " - lease-only debt against cash and bank balances"))
    # Basis separation - the whole point of the docstring warning.
    T.append(("FY2025 merged revenue EXCEEDS standalone (bases differ)",
              1.0 if MERGED["Revenue from operations"][0][0] > s["Total income"][1] else 0.0,
              1.0, 0.5, f"{PR} against {AR} - a deliberate cross-basis sanity check"))
    T.append(("FY2025 basis gap is ~Rs 10,323 cr",
              MERGED["Revenue from operations"][0][0] - s["Total income"][1],
              10323.06, 0.06, f"{PR} revenue less {AR} total income"))
    # Volume internal consistency - the CGD sector-defining metric (failure mode 21).
    T.append(("FY26 volumes: CGD + trading = total",
              VOLUMES["CGD segment (A)"][1] + VOLUMES["Gas trading segment (B)"][1],
              VOLUMES["TOTAL (A+B)"][1], 0.06, PR + " - segment volume table"))
    T.append(("Q4 volumes: CGD + trading = total",
              VOLUMES["CGD segment (A)"][0] + VOLUMES["Gas trading segment (B)"][0],
              VOLUMES["TOTAL (A+B)"][0], 0.06, PR + " - segment volume table"))
    T.append(("FY26 CGD sub-segments sum to CGD total",
              sum(VOLUMES[k][1] for k in
                  ("  Industrial", "  CNG", "  PNG - domestic", "  PNG - commercial")),
              VOLUMES["CGD segment (A)"][1], 0.06, PR + " - CGD volume breakdown"))
    return T


# Measured with tools/tieout_mutation.py, not asserted (failure mode 39).
DISCLOSED_DIFFERENCES = [
    ("The merged basis carries almost no independent checks",
     "Basis A comes from a single Q4 press release. Only revenue is cross-checked, and then "
     "only against the standalone basis as a DIFFERENCE test that proves the two are not "
     "comparable. EBITDA, PAT, net worth, EPS and DPS on the merged basis have no second "
     "source in the case folder and are traceable but not reproducible."),
    ("Q4 columns are unchecked",
     "The Q4 revenue/EBITDA/PAT figures support the quarterly narrative only; no audited "
     "quarterly statement exists in the folder to reconcile them against."),
    ("Working-capital lines are single-sourced",
     "Trade receivables, inventories and the deferred-tax liability come from the FY2024-25 "
     "balance sheet alone, with no disclosed ratio to reproduce them from."),
]


def run():
    print("=" * 98)
    print("GUJARAT ENERGY LIMITED (formerly Gujarat Gas Limited) - CareEdge suite")
    print("Scheme effective 01-May-2026: trading/E&P/wind IN, gas transmission OUT to GSPL")
    print("Transmission Limited. Rs crore. TWO BASES - see the module docstring.")
    print("=" * 98)

    print(f"\n{'BASIS A - MERGED ENTITY (the rated entity)':<40}" + "".join(f"{y:>14}" for y in A_YEARS))
    for k, (v, _) in MERGED.items():
        print(f"  {k:<38}" + "".join(f"{x:>14,.2f}" if isinstance(x, (int, float))
                                     else f"{'n/a':>14}" for x in v))
    rev, eb = MERGED["Revenue from operations"][0], MERGED["EBITDA"][0]
    print(f"  {'EBITDA margin (%)':<38}" + "".join(f"{eb[i]/rev[i]*100:>13.2f}%" for i in range(2)))
    print(f"  {'Revenue growth (%)':<38}{'':>14}{(rev[1]/rev[0]-1)*100:>13.2f}%")
    print(f"  {'EBITDA growth (%)':<38}{'':>14}{(eb[1]/eb[0]-1)*100:>13.2f}%")
    print("  -> Revenue FELL 12.7% while EBITDA ROSE 2.6%. Margin expanded 232 bps because the")
    print("     low-margin gas-TRADING revenue shrank. Volume, not price, tells the real story.")

    print(f"\n{'SALES VOLUME (mmscmd) - SECTOR-DEFINING METRIC':<40}{'Q4 FY26':>14}{'FY2025-26':>14}")
    for k, (q, f) in VOLUMES.items():
        print(f"  {k:<38}{q:>14,.2f}{f:>14,.2f}")

    print("\nOPERATIONAL")
    for k, v in OPERATIONAL:
        print(f"  {k:<24}{v}")

    print(f"\n{'BASIS B - GUJARAT GAS STANDALONE (pre-scheme)':<40}" + "".join(f"{y:>14}" for y in B_YEARS))
    for k, (v, _) in STANDALONE.items():
        print(f"  {k:<38}" + "".join(f"{x:>14,.2f}" for x in v))

    print(f"\n{'DERIVED (Basis B only)':<40}" + "".join(f"{y:>14}" for y in B_YEARS))
    for label, vals, fmt in _derive_standalone():
        print(f"  {label:<38}" + "".join(fmt.format(v) for v in vals))
    print("  -> BORROWINGS ARE NIL in both years. Adjusted debt is lease liabilities alone, and")
    print("     the company is in NET CASH. This, not any ratio band, is why the rating is AAA.")

    print("\nRATINGS DISCLOSED BY THE ISSUER (Step 7b - the Step 14 anchor)")
    for ag, inst, rtg, dt in DISCLOSED:
        print(f"  {ag:<18}{inst:<24}{rtg:<34}{dt}")

    # ---------------------------------------------------------------- tie-outs
    print("\n" + "=" * 98)
    print("TIE-OUTS")
    print("=" * 98)
    # ONE definition of the checks: printed here exactly as the tools receive them.
    T = tieouts(compute())
    fail = 0
    for lab, comp, disc, tol, _src in T:
        ok = abs(comp - disc) <= tol
        fail += (not ok)
        print(f"  [{'OK ' if ok else 'FAIL'}] {lab:<52} computed {comp:>11,.2f} "
              f"disclosed {disc:>11,.2f}")
    print(f"\n{len(T)-fail}/{len(T)} tie-outs reconcile.")
    for title, text in DISCLOSED_DIFFERENCES:
        print(f"\n  [DISCLOSED] {title}\n              {text}")
    if fail:
        print("*** RESOLVE BEFORE DRAFTING (Step 17). ***")
    return fail


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
