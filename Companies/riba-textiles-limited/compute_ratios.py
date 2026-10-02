"""Riba Textiles Limited - CareEdge ratio suite (CLAUDE.md Step 4 deliverable).

AGENCY: CareEdge.  ENTITY: cotton / home-textile manufacturer (terry towels), STANDALONE.
Methodology: CareEdge Rating Methodology - Cotton Textile Manufacturing (Dec 2024), with the
Manufacturing Companies criteria (Mar 2025) as the master frame.

SOURCE UNIT IS Rs LAKHS in the annual reports; converted ONCE here to Rs CRORE by /100.
  FY2025, FY2024 : AR FY2024-25 (998.md) - BS L3020-3070, P&L L3090-3125
  FY2023         : AR FY2023-24 (973.md) comparative column - P&L L3164-3182, BS L3110-3131

CareEdge earnings measure is PBILDT (profit before interest, LEASE RENTALS, depreciation and tax).
No lease liabilities appear on the balance sheet in any year, so PBILDT = PBDIT here; the absence
is recorded rather than assumed - see LEASE_NOTE.
"""
L = 100.0                      # lakhs -> crore

YEARS = ["FY2023", "FY2024", "FY2025"]

LEASE_NOTE = ("No lease liability line appears on the balance sheet in FY2023, FY2024 or FY2025, "
              "and no right-of-use asset is separately disclosed. PBILDT therefore equals PBDIT. "
              "If material operating leases exist off-balance-sheet, CareEdge's lease add-back "
              "would raise PBILDT and improve coverage - to be confirmed by the issuer.")

# ---- P&L (Rs lakhs as reported) -----------------------------------------------------------
PL = {
    "Revenue from operations": ([None, 24689.43, 29585.89], "998 L~3095; FY23 not separately extracted"),
    "Other income":            ([None, 31.23, 26.73],       "998 L~3096"),
    "Total income":            ([24282.97, 24720.66, 29612.62], "973 L3164; 998 L~3097"),
    "Depreciation":            ([446.66, 479.18, 547.38],   "973 L3170; 998 L~3109"),
    "Finance cost":            ([449.38, 464.89, 588.57],   "973 L3171; 998 L~3110"),
    "Total expenses":          ([None, 23660.38, 28496.40], "998 L~3117"),
    "Profit before tax":       ([974.08, 1060.28, 1116.22], "973 L3177; 998 L~3120"),
    "Profit after tax":        ([740.25, 791.77, 849.96],   "973 L3182; 998 L3121"),
}

# ---- Balance sheet (Rs lakhs as reported) -------------------------------------------------
BS = {
    "Borrowings - non-current": ([2611.53, 2537.90, 2573.58], "973 L3120; 998 L3060"),
    "Borrowings - current":     ([3468.10, 4230.22, 3564.93], "973 L3124; 998 L3064"),
    "Equity share capital":     ([965.29, 965.29, 965.29],    "973 L3113; 998 L~3053"),
    "Reserves & surplus":       ([7182.62, 7974.38, 8824.35], "973 L3115; 998 L~3054"),
    "Total assets":             ([16420.83, 17908.18, 18144.64], "973 L3110; 998 L3067"),
    "Inventories":              ([None, 2567.85, 2516.15],   "998 L3042"),
    "Trade receivables":        ([None, 4158.75, 3621.70],   "998 L3044"),
    "Cash & cash equivalents":  ([None, 470.29, 247.37],     "998 L~3046"),
    "Other bank balances":      ([None, 6.73, 6.73],         "998 L~3047"),
    "Current assets":           ([None, 8262.61, 7589.18],   "998 L~3050"),
    "Current liabilities":      ([None, 6198.93, 5491.49],   "998 L3068"),
    "Deferred tax liability":   ([None, 231.68, 289.94],     "998 L~3061"),
}

# ---- Ratings disclosed by the issuer (Step 7b -> the Step 14 anchor) -----------------------
DISCLOSED = [
    ("FY2023 AR", "16 May 2022", "CRISIL BBB / Negative / A3+", "Rs 76.5 cr bank facilities"),
    ("FY2024 AR", "03 May 2023", "CRISIL BBB / Negative (long term)", "Rs 76.5 cr bank facilities"),
    ("FY2025 AR", "04 Jul 2025", "CRISIL BBB / Stable (long term)", "Rs 94 cr bank facilities"),
]

# ---- The company's OWN disclosed ratios, for tie-out --------------------------------------
# Indexed BY YEAR, not by position. In both ARs the FIRST numeric column is the CURRENT year
# (header reads "31.03.2024 | 31.03.2023 | DEVIATION"). Reading it the other way round made
# four tie-outs fail on the first run - the error was in the mapping, not the data.
#   FY2024 AR (973.md) L2745-2762 : FY2024 | FY2023
#   FY2025 AR (998.md) L2620-2631 : FY2025 | FY2024
OWN = {
    "Current ratio":      {"FY2023": 1.35, "FY2024": 1.33, "FY2025": 1.38},
    "Debt-equity (LT)":   {"FY2023": 0.32, "FY2024": 0.28, "FY2025": 0.26},
    "DSCR":               {"FY2023": 1.16, "FY2024": 1.52, "FY2025": 1.47},
    "Operating margin %": {"FY2023": 16.23, "FY2024": 16.63, "FY2025": 12.56},
    "RoCE %":             {"FY2024": 13.03, "FY2025": 13.47},
}


def g(d, k, i):
    v = d[k][0][i]
    return None if v is None else v / L


def _derive():
    """The CareEdge-convention ratio suite as an ordered [(label, [values], fmt)] list.

    ONE definition, consumed by both compute() (which transposes it for the tools) and run()
    (which prints it). Deriving it twice is how a printed table and a gate result drift apart.
    Rs crore throughout; None where FY2023 lacks the underlying line.
    """
    n = len(YEARS)
    pbt = [g(PL, "Profit before tax", i) for i in range(n)]
    fin = [g(PL, "Finance cost", i) for i in range(n)]
    dep = [g(PL, "Depreciation", i) for i in range(n)]
    oi = [g(PL, "Other income", i) for i in range(n)]
    rev = [g(PL, "Revenue from operations", i) for i in range(n)]
    ti = [g(PL, "Total income", i) for i in range(n)]
    pat = [g(PL, "Profit after tax", i) for i in range(n)]
    eq = [g(BS, "Equity share capital", i) + g(BS, "Reserves & surplus", i) for i in range(n)]
    debt = [g(BS, "Borrowings - non-current", i) + g(BS, "Borrowings - current", i)
            for i in range(n)]
    ta = [g(BS, "Total assets", i) for i in range(n)]
    ca = [g(BS, "Current assets", i) for i in range(n)]
    cl = [g(BS, "Current liabilities", i) for i in range(n)]
    cash = [None if g(BS, "Cash & cash equivalents", i) is None
            else g(BS, "Cash & cash equivalents", i) + g(BS, "Other bank balances", i)
            for i in range(n)]

    # PBILDT: PBT + finance + depreciation - other income (no lease rentals - see LEASE_NOTE)
    pbildt = [pbt[i] + fin[i] + dep[i] - (oi[i] or 0.0) for i in range(n)]
    # FY2023 has no separate revenue line -> margin taken on total income, flagged in DISCLOSED_DIFFERENCES
    base = [ti[0], rev[1], rev[2]]
    ce = [debt[i] + eq[i] for i in range(n)]
    rcv = [g(BS, "Trade receivables", i) for i in range(n)]
    inv = [g(BS, "Inventories", i) for i in range(n)]

    return [
        ("PBILDT", pbildt, "{:>13,.2f}"),
        ("PBILDT margin (%)", [pbildt[i] / base[i] * 100 for i in range(n)], "{:>12.2f}%"),
        ("PAT margin (%)", [pat[i] / base[i] * 100 for i in range(n)], "{:>12.2f}%"),
        ("Total debt", debt, "{:>13,.2f}"),
        ("Net debt", [None if cash[i] is None else debt[i] - cash[i] for i in range(n)],
         "{:>13,.2f}"),
        ("Tangible net worth", eq, "{:>13,.2f}"),
        ("Overall gearing (x)", [debt[i] / eq[i] for i in range(n)], "{:>12.2f}x"),
        ("Net overall gearing (x)",
         [None if cash[i] is None else (debt[i] - cash[i]) / eq[i] for i in range(n)],
         "{:>12.2f}x"),
        ("TOL / TNW (x)", [(ta[i] - eq[i]) / eq[i] for i in range(n)], "{:>12.2f}x"),
        ("Interest coverage (x)", [pbildt[i] / fin[i] for i in range(n)], "{:>12.2f}x"),
        ("Total debt / PBILDT (x)", [debt[i] / pbildt[i] for i in range(n)], "{:>12.2f}x"),
        ("Current ratio (x)",
         [None if ca[i] is None else ca[i] / cl[i] for i in range(n)], "{:>12.2f}x"),
        ("RoCE (%)", [(pbildt[i] - dep[i]) / ce[i] * 100 for i in range(n)], "{:>12.2f}%"),
        ("Receivable days",
         [None if rcv[i] is None else rcv[i] * 365 / base[i] for i in range(n)], "{:>13.0f}"),
        ("Inventory days",
         [None if inv[i] is None else inv[i] * 365 / base[i] for i in range(n)], "{:>13.0f}"),
    ]


def compute():
    """Contract member: {period: {ratio: value}}. Omits cells with no underlying line."""
    rows = _derive()
    R = {}
    for i, y in enumerate(YEARS):
        R[y] = {lab: vals[i] for lab, vals, _f in rows if vals[i] is not None}
        for table in (PL, BS):
            for k in table:
                v = g(table, k, i)
                if v is not None:
                    R[y][k] = v
    return R


def tieouts(R):
    """Contract member: [(description, computed, disclosed, tolerance, source), ...].

    Reads the input tables directly (not R) so every check stays sensitive to the inputs the
    mutation harness perturbs. Each reconciles a DERIVED figure against a SEPARATELY PRINTED
    one - the AR's own arithmetic, or the ratios the company itself discloses - never a value
    against itself (failure mode 39).
    """
    T = []
    n = len(YEARS)
    eq = [g(BS, "Equity share capital", i) + g(BS, "Reserves & surplus", i) for i in range(n)]
    for i in (1, 2):                       # FY2023 lacks the component lines these need
        y = YEARS[i]
        T.append((f"{y} total income = revenue + other income",
                  g(PL, "Revenue from operations", i) + g(PL, "Other income", i),
                  g(PL, "Total income", i), 0.02,
                  "AR statement of profit and loss - printed total income row"))
        T.append((f"{y} PBT = total income - total expenses",
                  g(PL, "Total income", i) - g(PL, "Total expenses", i),
                  g(PL, "Profit before tax", i), 0.02,
                  "AR statement of profit and loss - printed PBT row"))
        T.append((f"{y} current ratio vs company-disclosed",
                  g(BS, "Current assets", i) / g(BS, "Current liabilities", i),
                  OWN["Current ratio"][y], 0.02,
                  "AR key-financial-ratios note, current ratio row"))
        # The company's "Debt Equity Ratio" is LONG-TERM debt / equity, not total debt.
        # Reproducing it on that basis confirms both the extraction AND the convention.
        T.append((f"{y} company 'debt-equity' = LT debt / equity",
                  g(BS, "Borrowings - non-current", i) / eq[i],
                  OWN["Debt-equity (LT)"][y], 0.02,
                  "AR key-financial-ratios note, debt-equity row (long-term basis)"))
    return T


# Measured with tools/tieout_mutation.py, not asserted (failure mode 39).
DISCLOSED_DIFFERENCES = [
    ("FY2023 column is largely unchecked",
     "The FY2024 AR restates only total income, depreciation, finance cost, PBT, PAT and the "
     "balance-sheet headline for FY2023 - it carries no revenue/other-income split, no current "
     "assets/liabilities and no working-capital lines. The two arithmetic tie-outs therefore "
     "cannot run on FY2023, and its PBILDT margin is struck on TOTAL income rather than revenue. "
     "Stated rather than silently blended."),
    ("Working-capital and cash lines have no independent second source",
     "Inventories, trade receivables, cash and other bank balances come from the FY2025 AR "
     "balance sheet alone. The company discloses no inventory- or receivable-day ratio to "
     "reconcile them against, so receivable/inventory days are traceable but not reproducible."),
    # Stated as a literal, not as `LEASE_NOTE`: delivery_audit.py counts named gaps with
    # ast.literal_eval, so a variable reference here makes the whole list unevaluable and the
    # three gaps below get counted as one.
    ("No lease add-back is possible, so coverage may be overstated",
     "No lease liability line and no right-of-use asset appears on the balance sheet in any of "
     "FY2023, FY2024 or FY2025, so PBILDT equals PBDIT and no CareEdge lease add-back can be "
     "computed. If material operating leases exist off-balance-sheet, the add-back would raise "
     "PBILDT and improve coverage - to be confirmed by the issuer. See LEASE_NOTE."),
]


def run():
    print("=" * 96)
    print("RIBA TEXTILES LIMITED - CareEdge ratio suite | cotton / home textiles | STANDALONE")
    print("All figures Rs CRORE (source Rs lakhs, converted once).")
    print("=" * 96)

    def show(title, d):
        print(f"\n{title:<34}" + "".join(f"{y:>13}" for y in YEARS))
        for k in d:
            row = "".join(f"{g(d,k,i):>13,.2f}" if g(d, k, i) is not None else f"{'n/a':>13}"
                          for i in range(3))
            print(f"  {k:<32}{row}")

    show("PROFIT AND LOSS", PL)
    show("BALANCE SHEET", BS)

    print(f"\n{'DERIVED - CareEdge convention':<34}" + "".join(f"{y:>13}" for y in YEARS))
    for label, vals, fmt in _derive():
        print(f"  {label:<32}" + "".join(fmt.format(v) if v is not None else f"{'n/a':>13}"
                                         for v in vals))

    print("\nRATINGS DISCLOSED BY THE ISSUER  (Step 7b - the Step 14 anchor)")
    for src, dt, rtg, amt in DISCLOSED:
        print(f"  {src:<11}{dt:<14}{rtg:<36}{amt}")
    print("  -> outlook moved Negative -> Stable and rated quantum rose Rs 76.5cr -> Rs 94cr.")
    print("  -> NO Riba rationale exists in any reference library (searched); anchor is the AR.")

    # ---------------------------------------------------------------- tie-outs
    print("\n" + "=" * 96)
    print("TIE-OUTS")
    print("=" * 96)
    # ONE definition of the checks: printed here exactly as the tools receive them.
    T = tieouts(compute())
    failed = 0
    for lab, comp, disc, tol, _src in T:
        ok = abs(comp - disc) <= tol
        failed += (not ok)
        print(f"  [{'OK ' if ok else 'FAIL'}] {lab:<52} computed {comp:>8,.2f} "
              f"disclosed {disc:>8,.2f}")
    print(f"\n{len(T)-failed}/{len(T)} tie-outs reconcile.")
    for title, text in DISCLOSED_DIFFERENCES:
        print(f"\n  [DISCLOSED] {title}\n              {text}")
    return failed


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
