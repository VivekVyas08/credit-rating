"""HDFC Securities Limited - CareEdge broking ratio suite (CLAUDE.md Step 4 deliverable).

AGENCY: CareEdge.  ENTITY: retail broking company, 94.01% held by HDFC Bank Limited.
Methodology: CareEdge Broking Criteria (Dec 2025) + Financial Ratios - Financial Sector (Feb 2025)
             + Notching by Factoring Linkages with Parent (Jan 2025) + Short Term Instruments.

*** THE DEBT PICTURE IS THE STORY - and it is stated in FULL (failure mode 29 discipline) ***
The debt is disclosed by TYPE and TENOR in the company's own balance sheet, so the long-term /
short-term split below is EVIDENCED, not estimated:
  SHORT TERM : commercial paper, tenor 7-180 days (FY2026) / 28-182 days (FY2025)
  SECURED    : loan, disclosed separately as "Borrowings (other than debt securities)"
Total debt nearly DOUBLED while profit FELL 17.3%. That combination is the credit question.

SOURCE UNIT is Rs LAKHS in the financial statements and Rs CRORE in the highlights table.
Everything below is Rs CRORE, converted ONCE at extraction.
  AR26 = HSL Annual Report FY2026 (dated 04-08-2026) - the NEWEST document (failure mode 26)
         highlights L1080-1096; balance sheet L3049-3052; borrowings notes L4660-4700
"""
YEARS = ["FY2025", "FY2026"]
AR26 = "FY2026 annual report (04-08-2026)"

# ---- P&L, Rs crore as printed in the highlights table -----------------------------------------
PL = {
    "Total income":              ([3264.8, 3110.2], AR26 + " highlights L1092"),
    "Total expenses (ex dep'n)": ([1699.1, 1790.3], AR26 + " highlights"),
    "Profit before depreciation": ([1565.7, 1319.8], AR26 + " highlights"),
    "Depreciation & amortisation": ([69.6, 82.8],   AR26 + " highlights"),
    "Profit before tax":         ([1496.1, 1237.1], AR26 + " highlights"),
    "Tax":                       ([371.1, 307.1],   AR26 + " highlights"),
    "Profit after tax":          ([1125.0, 929.9],  AR26 + " highlights"),
    "Dividend (interim + final)": ([898.3, 740.1],  AR26 + " highlights - appropriation"),
}

# ---- DEBT, split by type and tenor. Lakhs / 100 -> crore --------------------------------------
DEBT = {
    "Commercial paper (at amortised cost)": ([7677.51, 12827.38], AR26 + " note L4669"),
    "Interest accrued on CP":              ([64.01, 103.96],     AR26 + " note L4670"),
    "Debt securities - TOTAL (SHORT TERM)": ([7741.52, 12931.33], AR26 + " BS L3049"),
    "Borrowings other than debt securities (secured loan)":
                                            ([202.25, 2182.55],  AR26 + " BS L3050, note L4695"),
    "Lease liabilities":                   ([85.63, 80.80],      AR26 + " BS L3051"),
}
CP_TENOR = {"FY2025": "28 - 182 days, 7.43% - 8.05%", "FY2026": "07 - 180 days, 6.15% - 8.05%"}

# ---- MATURITY LADDER - the definitive LONG TERM / SHORT TERM split ----------------------------
# AR26 contractual maturity table L6405-6417. EVERY rupee of borrowing sits in "Less than 1 year".
# LONG-TERM DEBT IS NIL. This is stated by the issuer, not inferred.
MATURITY_FY26 = {           # Rs crore: (<1yr, 1-2yr, 2-3yr, >3yr)
    "Debt securities (CP)":                  (12931.33, 0.0, 0.0, 0.0),
    "Borrowings other than debt securities": (2182.55, 0.0, 0.0, 0.0),
    "Lease liabilities (undiscounted)":      (24.83, 22.27, 15.43, 41.73),
}
LT_DEBT_FY26 = 0.0          # NIL - evidenced by the maturity table, not assumed

BS = {
    "Total debt (borrowings incl. debt securities)": ([7943.77, 15113.88], AR26 + " L6630"),
    "Total equity":                                  ([3348.59, 3595.92],  AR26 + " L6633"),
}

# ---- Broking sector metrics (failure mode 21 / 28 - the RIGHT metric set) ---------------------
# CORRECTED 20-Aug-2026. The first pass mis-attributed these by YEAR: it read "34% / Rs 1.7 Tr"
# (an FY2025 annual report figure), "1.09 million clients" (an FY2024 figure) and branch counts
# in the WRONG DIRECTION, reporting a shrinking network as expansion. Each metric below is now
# tied to the report it came from. Failure mode 26: read the NEWEST document first.
BROKING = [
    ("Average daily turnover", "UP 82% to Rs 3 trillion (Rs 1.6 trillion at 31-Mar-2025) "
                               "- FY2026 AR highlights"),
    ("Derivative volumes", "up 83% YoY; derivatives market share up 1.7x; retail equity "
                           "delivery market share retained - FY2026 AR"),
    ("Brokerage and fee income", "Rs 1,516 crore - 48.7% of total income of Rs 3,110.2 cr"),
    ("Active customers", "1 million+ accessing services digitally - FY2026 AR"),
    ("Branch network - CONTRACTING", "184 branches / 139 cities (31-Mar-2024) -> 134 / 106 "
                                     "(31-Mar-2025) -> 128 / 100+ (31-Mar-2026). Down 30% in "
                                     "two years - deliberate consolidation toward digital"),
]
PARENT = ("HDFC Bank Limited", 94.01)
SUBSIDIARY = "HDFC Securities IFSC Limited (HSIL) - wholly owned"


def run():
    print("=" * 96)
    print("HDFC SECURITIES LIMITED - CareEdge broking ratio suite")
    print(f"Parent: {PARENT[0]} - {PARENT[1]}%   |   Subsidiary: {SUBSIDIARY}")
    print("All figures Rs CRORE. Rs lakhs in the statements, converted once.")
    print("=" * 96)

    def show(title, d):
        print(f"\n{title:<54}" + "".join(f"{y:>14}" for y in YEARS))
        for k, (v, _) in d.items():
            print(f"  {k:<52}" + "".join(f"{x:>14,.2f}" for x in v))

    show("PROFIT AND LOSS", PL)
    show("DEBT - SPLIT BY TYPE AND TENOR", DEBT)
    for y in YEARS:
        print(f"    CP tenor {y}: {CP_TENOR[y]}")
    print()
    print(f"{'MATURITY LADDER FY2026 - LT/ST SPLIT':<44}" + ''.join(f'{h:>13}' for h in ['<1 year', '1-2 yr', '2-3 yr', '>3 yr']))
    for k, v in MATURITY_FY26.items():
        print(f"  {k:<42}" + "".join(f"{x:>13,.2f}" for x in v))
    print(f"  {'>>> LONG-TERM DEBT':<42}{'':>13}{'N I L':>13}{'N I L':>13}{'N I L':>13}")

    show("BALANCE SHEET", BS)

    ti = PL["Total income"][0]
    pat = PL["Profit after tax"][0]
    pbt = PL["Profit before tax"][0]
    div = PL["Dividend (interim + final)"][0]
    td = BS["Total debt (borrowings incl. debt securities)"][0]
    eq = BS["Total equity"][0]
    cp = DEBT["Debt securities - TOTAL (SHORT TERM)"][0]
    sec = DEBT["Borrowings other than debt securities (secured loan)"][0]

    print(f"\n{'DERIVED':<54}" + "".join(f"{y:>14}" for y in YEARS))

    def e(lab, v, f="{:>14,.2f}"):
        print(f"  {lab:<52}" + "".join(f.format(x) for x in v))

    e("Gearing - total debt / equity (x)  [KEY]", [td[i] / eq[i] for i in range(2)], '{:>13.2f}x')
    e("Short-term debt as % of total debt", [cp[i] / td[i] * 100 for i in range(2)], "{:>13.1f}%")
    e("PAT margin (%)", [pat[i] / ti[i] * 100 for i in range(2)], "{:>13.2f}%")
    e("PBT margin (%)", [pbt[i] / ti[i] * 100 for i in range(2)], "{:>13.2f}%")
    e("Return on equity (%)", [pat[i] / eq[i] * 100 for i in range(2)], "{:>13.2f}%")
    e("Dividend payout (%)", [div[i] / pat[i] * 100 for i in range(2)], "{:>13.1f}%")
    print(f"  {'Total income growth (%)':<52}{'':>14}{(ti[1]/ti[0]-1)*100:>13.2f}%")
    print(f"  {'PAT growth (%)':<52}{'':>14}{(pat[1]/pat[0]-1)*100:>13.2f}%")
    print(f"  {'Total DEBT growth (%)':<52}{'':>14}{(td[1]/td[0]-1)*100:>13.2f}%")
    print(f"  {'Secured loan growth (%)':<52}{'':>14}{(sec[1]/sec[0]-1)*100:>13.2f}%")

    print("\n  --- THE CENTRAL TENSION ---")
    print(f"  Total income {ti[0]:,.1f} -> {ti[1]:,.1f} ({(ti[1]/ti[0]-1)*100:+.1f}%)")
    print(f"  Profit after tax {pat[0]:,.1f} -> {pat[1]:,.1f} ({(pat[1]/pat[0]-1)*100:+.1f}%)")
    print(f"  Total debt {td[0]:,.1f} -> {td[1]:,.1f} ({(td[1]/td[0]-1)*100:+.1f}%)")
    print(f"  Gearing {td[0]/eq[0]:.2f}x -> {td[1]/eq[1]:.2f}x")
    print(f"  Dividend payout {div[1]/pat[1]*100:.0f}% of a FALLING profit, while debt doubled.")
    print("  YIELD COMPRESSION: average daily turnover rose 82% (1.6 -> 3.0 Rs trillion) and")
    print(f"  derivative volumes 83%, yet total income FELL {abs((ti[1]/ti[0]-1)*100):.1f}%.")
    print("  Volume growth is NOT converting to revenue - the defining operating fact of FY2026.")

    print("\nBROKING METRICS (sector-defining)")
    for k, v in BROKING:
        print(f"  {k:<30}{v}")

    print("\n" + "=" * 96)
    print("TIE-OUTS")
    print("=" * 96)
    ck = []
    for i in range(2):
        y = YEARS[i]
        ck.append((f"{y} debt securities = CP + interest accrued",
                   round(cp[i], 2),
                   round(DEBT["Commercial paper (at amortised cost)"][0][i]
                         + DEBT["Interest accrued on CP"][0][i], 2)))
        ck.append((f"{y} total debt = debt securities + secured loan",
                   round(td[i], 2), round(cp[i] + sec[i], 2)))
        ck.append((f"{y} PBT = profit before dep'n - depreciation",
                   round(pbt[i], 2),
                   round(PL["Profit before depreciation"][0][i]
                         - PL["Depreciation & amortisation"][0][i], 2)))
        ck.append((f"{y} PAT = PBT - tax",
                   round(pat[i], 2), round(pbt[i] - PL["Tax"][0][i], 2)))
        ck.append((f"{y} profit before dep'n = income - expenses",
                   round(PL["Profit before depreciation"][0][i], 2),
                   round(ti[i] - PL["Total expenses (ex dep'n)"][0][i], 2)))
    ck.append(("Debt is overwhelmingly SHORT TERM in both years", True,
               all(cp[i] / td[i] > 0.85 for i in range(2))))
    ck.append(("Debt grew while PAT fell", True, td[1] > td[0] and pat[1] < pat[0]))
    ck.append(("FY2026 maturity ladder: borrowings all in <1yr = total debt",
               round(td[1], 2),
               round(MATURITY_FY26["Debt securities (CP)"][0]
                     + MATURITY_FY26["Borrowings other than debt securities"][0], 2)))
    ck.append(("FY2026 LONG-TERM debt is NIL (buckets beyond 1yr are zero)", 0.0,
               round(sum(sum(v[1:]) for k, v in MATURITY_FY26.items() if "Lease" not in k), 2)))

    # TOLERANCE 0.15 = one-and-a-half rounding units. The highlights table is printed to ONE
    # decimal in Rs crore and each line is rounded independently, so FY2026 shows genuine 0.1
    # drift (1,319.8 - 82.8 = 1,237.0 against a printed 1,237.1). That is SOURCE rounding, not a
    # reconciliation failure - the figures are NOT adjusted to force a tie.
    fail = 0
    for lab, exp, act in ck:
        ok = (abs(exp - act) < 0.15) if isinstance(exp, (int, float)) and not isinstance(exp, bool) \
            else (exp == act)
        fail += (not ok)
        print(f"  [{'OK ' if ok else 'FAIL'}] {lab:<54} expected {exp!s:>10} got {act!s:>10}")
    print(f"\n{len(ck)-fail}/{len(ck)} tie-outs reconcile.")
    return fail


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
