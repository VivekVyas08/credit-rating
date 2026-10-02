"""Aptus Value Housing Finance India Limited - CareEdge HFC ratio suite.

AGENCY: CareEdge.  ENTITY: affordable housing finance company.
BASIS: CONSOLIDATED - Aptus Value Housing Finance India Limited + Aptus Finance India Private
Limited (AFIPL, its wholly-owned NBFC subsidiary). CareEdge takes the consolidated approach and
so does this file. The AR carries BOTH bases and they differ materially:
    standalone total assets Rs 9,553.31 cr   vs   consolidated Rs 13,047.66 cr
    standalone total income Rs 1,564.15 cr   vs   consolidated Rs 2,245.48 cr
Never splice the two.

CONVENTIONS - financial-sector, per CareEdge/BROKING_CONVENTIONS.md (the financial-sector paper,
not the corporate one; the two TNW definitions DIFFER - failure mode 32):
    TNW = total equity - intangible assets - deferred tax assets
Verified by reproduction against the CareEdge press release of 02-Jul-2026, which is the test:
a definition that will not reproduce the agency's published figure is WRONG.

METRIC SET taken from the HFC peer, PNB Housing Finance Limited (03-Jul-2026), NOT from the
auto-picked top peer - that was Jana Small Finance Bank, a BANK, and the third hit was HFCL
Limited, a telecom cable maker matching on the token 'hfc'. Failure mode 33.

RATED AMOUNTS: CareEdge press release 02-Jul-2026, already in the reference library and
extracted BEFORE drafting per failure mode 29. Line integrity verified below.
All figures Rs CRORE. Statements are in Rs lakhs; converted once at extraction.
"""
YEARS = ["FY2025", "FY2026"]
AR = "FY2026 annual report - CONSOLIDATED statements"
PR = "CareEdge press release 02-Jul-2026"

# ---- RATED FACILITIES - sanctioned limits, not drawn debt (failure mode 31) --------------------
RATED = {
    "Long-term bank facilities": dict(amount=2100.00, rating="CARE AA; Stable", action="Reaffirmed",
        lines={"Fund-based LT term loan (maturity Feb-2034)": 2058.75,
               "Fund-based LT working capital limits": 30.00,
               "Non-fund-based LT bank guarantee": 11.25}),
    "Non-convertible debentures": dict(amount=1145.00, rating="CARE AA; Stable", action="Reaffirmed",
        lines={"NCD II  INE852O07113 8.75% 23-06-2028": 45.00,
               "NCD III INE852O07139 8.75% 19-09-2029": 240.00,
               "NCD IV  INE852O07147 8.75% 30-12-2029": 200.00,
               "NCD V   INE852O07154/62 8.75% Mar/Apr-2030": 280.00,
               "NCD VI  INE852O07170 8.75% 23-05-2030": 80.00,
               "NCD VII INE852O07188/96 + proposed 7.85-7.95%": 300.00}),
}

# ---- CONSOLIDATED P&L (Rs crore) ---------------------------------------------------------------
PL = {
    "Interest income":              [1669.58, 1943.80],
    "Fees and commission income":   [56.85, 58.65],
    "Net gain on fair value changes": [7.67, 17.36],
    "Net gain on derecognition (assignment)": [16.31, 172.44],
    "Total income":                 [1798.40, 2245.48],
    "Finance costs":                [540.51, 648.45],
    "Impairment on financial instruments": [28.32, 61.51],
    "Total expenses":               [823.56, 1034.33],
    "Profit before tax":            [974.84, 1211.16],
    "Profit after tax":             [751.25, 942.94],
}

# ---- TANGIBLE NET WORTH build-up (failure mode 32) ---------------------------------------------
NW = {
    "Total equity (consolidated)":  [4316.65, 5060.04],
    "less: intangible assets":      [1.01, 1.22],
    "less: deferred tax assets":    [22.06, 0.15],
}
TNW_PUBLISHED = 5059.0          # CareEdge, as on 31-03-2026

# ---- Balance sheet / book -----------------------------------------------------------------------
BS = {
    "Debt securities":              [1292.29, 1350.49],
    "Borrowings (other than debt securities)": [5554.55, 6523.18],
    "TOTAL DEBT":                   [6846.84, 7873.67],
    "Lease liabilities":            [26.24, 30.10],
    "Loans - on book":              [10630.27, 11929.52],
    "Cash and cash equivalents":    [302.59, 563.32],
    "Bank balances other than above": [121.16, 27.42],
    "Total assets":                 [11243.41, 13047.66],
}
AUM = [10865.0, 13107.0]
AUM_SERIES = [("FY2021", 4068), ("FY2022", 5180), ("FY2023", 6738),
              ("FY2024", 8722), ("FY2025", 10865), ("FY2026", 13107)]
AUM_SPLIT = [("Aptus HFC (housing)", 9306, 71), ("AFIPL (NBFC subsidiary)", 3801, 29)]

# ---- Q1FY2027 (quarter ended 30-Jun-2026), consolidated ----------------------------------------
Q1 = dict(total_income=610.65, pat=260.94, q1fy26_income=530.14, q1fy26_pat=219.25,
          q4fy26_income=593.12, q4fy26_pat=260.95)

# ---- Asset quality and capital -----------------------------------------------------------------
ASSET_QUALITY = {
    "GNPA % - AR, consolidated":    [1.19, 1.52],
    "NNPA % - AR, consolidated":    [0.89, 1.15],
    "Gross stage 3 % - CareEdge published": [1.18, 1.45],
}
CRAR = 71.0                       # vs RBI minimum 15% for HFCs
STANDALONE_AQ = dict(gnpa=1.29, nnpa=0.96, pcr_stage3=25.50, lcr=211.79)
COST_OF_BORROWINGS = [8.6, 8.7, 8.3]      # FY2024, FY2025, FY2026
CORP_GUARANTEE_AFIPL = [459.06, 269.63]   # given by Aptus for AFIPL borrowings
LIQUIDITY = 2061.0                        # Rs cr, per AR


def _tnw():
    """Tangible net worth per CareEdge: equity less intangibles less DTA (failure mode 32)."""
    return [NW["Total equity (consolidated)"][i] - NW["less: intangible assets"][i]
            - NW["less: deferred tax assets"][i] for i in range(len(YEARS))]


def compute():
    """Contract member: {period: {ratio: value}}, CareEdge HFC conventions."""
    n = len(YEARS)
    tnw = _tnw()
    ti, pat, fc = PL["Total income"], PL["Profit after tax"], PL["Finance costs"]
    ii, imp = PL["Interest income"], PL["Impairment on financial instruments"]
    avg_aum = (AUM[0] + AUM[1]) / 2
    R = {}
    for i, y in enumerate(YEARS):
        row = {k: v[i] for k, v in PL.items()}
        row.update({k: v[i] for k, v in BS.items()})
        row.update({k: v[i] for k, v in ASSET_QUALITY.items()})
        row["Tangible net worth"] = tnw[i]
        row["AUM"] = AUM[i]
        row["On-book gearing (x)"] = BS["TOTAL DEBT"][i] / tnw[i]
        row["AUM / tangible net worth (x)"] = AUM[i] / tnw[i]
        row["Net interest income"] = ii[i] - fc[i]
        row["PAT margin (%)"] = pat[i] / ti[i] * 100
        row["Cost-to-income (%)"] = ((PL["Total expenses"][i] - fc[i] - imp[i])
                                     / (ti[i] - fc[i]) * 100)
        row["Capital adequacy CRAR (%)"] = CRAR
        if i == 1:            # average-basis ratios need both endpoints
            row["NIM on average AUM (%)"] = (ii[i] - fc[i]) / avg_aum * 100
            row["Credit cost on avg AUM (%)"] = imp[i] / avg_aum * 100
            row["Return on managed assets ROMA (%)"] = pat[i] / avg_aum * 100
            row["Return on total assets (%)"] = pat[i] / (
                (BS["Total assets"][0] + BS["Total assets"][1]) / 2) * 100
            row["Return on net worth (%)"] = pat[i] / ((tnw[0] + tnw[1]) / 2) * 100
        R[y] = row
    return R


def tieouts(R):
    """Contract member: [(description, computed, disclosed, tolerance, source), ...].

    The test here is REPRODUCING CareEdge's published figures from the audited components -
    which is the strongest form of tie-out available (failure mode 32: if the definition will
    not reproduce the published number, the definition is wrong). Reads the input tables
    directly so the mutation harness's perturbations are visible.
    """
    n = len(YEARS)
    tnw = _tnw()
    ti, pat = PL["Total income"], PL["Profit after tax"]
    avg_aum = (AUM[0] + AUM[1]) / 2
    CE = "CareEdge published rationale"
    T = [
        ("FY2026 TNW reproduces published 5,059", tnw[1], TNW_PUBLISHED, 1.0,
         f"{CE} tangible net worth vs the AR equity/intangibles/DTA build-up"),
        ("FY2026 total income reproduces published 2,245", ti[1], 2245.0, 1.0,
         f"{CE} Brief Financials vs audited P&L"),
        ("FY2025 total income reproduces published 1,798", ti[0], 1798.0, 1.0,
         f"{CE} Brief Financials vs audited P&L"),
        ("FY2026 PAT reproduces published 943", pat[1], 943.0, 1.0,
         f"{CE} Brief Financials vs audited P&L"),
        ("FY2025 PAT reproduces published 751", pat[0], 751.0, 1.0,
         f"{CE} Brief Financials vs audited P&L"),
        ("FY2026 on-book gearing reproduces published 1.56",
         BS["TOTAL DEBT"][1] / tnw[1], 1.56, 0.02,
         f"{CE} gearing vs audited total debt over derived TNW"),
        ("FY2025 on-book gearing reproduces published 1.60",
         BS["TOTAL DEBT"][0] / tnw[0], 1.60, 0.02,
         f"{CE} gearing vs audited total debt over derived TNW"),
        ("FY2025 AUM/TNW reproduces published 2.53", AUM[0] / tnw[0], 2.53, 0.02,
         f"{CE} AUM/TNW row"),
        ("FY2026 AUM/TNW vs published 2.58", AUM[1] / tnw[1], 2.58, 0.02,
         f"{CE} AUM/TNW row"),
        ("FY2026 ROMA vs the AR's own RoA of 7.9", pat[1] / avg_aum * 100, 7.9, 0.1,
         "FY2025-26 annual report - the company's own stated return on assets"),
        ("FY2026 RONW vs the AR's own RoE of 20.1",
         pat[1] / ((tnw[0] + tnw[1]) / 2) * 100, 20.1, 0.1,
         "FY2025-26 annual report - the company's own stated return on equity"),
        ("LINE INTEGRITY bank facilities = 2,100.00",
         sum(RATED["Long-term bank facilities"]["lines"].values()), 2100.00, 0.02,
         f"{CE} rated-amount table - component lines vs their printed total (failure mode 12)"),
        ("LINE INTEGRITY NCDs = 1,145.00",
         sum(RATED["Non-convertible debentures"]["lines"].values()), 1145.00, 0.02,
         f"{CE} rated-amount table - component lines vs their printed total (failure mode 12)"),
        ("FY2026 total debt = debt securities + other borrowings",
         BS["Debt securities"][1] + BS["Borrowings (other than debt securities)"][1],
         BS["TOTAL DEBT"][1], 0.02, "audited balance sheet - printed total-debt row"),
        ("FY2026 AUM split sums to the AUM",
         float(sum(v for _, v, _ in AUM_SPLIT)), AUM[1], 1.0,
         "AR segment disclosure - HFC and NBFC book split vs consolidated AUM"),
        ("FY2026 PAT = PBT less tax implied",
         PL["Profit before tax"][1] - 268.22, pat[1], 0.02,
         "audited P&L - PBT less the tax charge vs the printed PAT row"),
    ]
    return T


# Measured with tools/tieout_mutation.py, not asserted (failure mode 39).
DISCLOSED_DIFFERENCES = [
    ("Asset-quality percentages are not independently reproducible",
     "GNPA/NNPA and gross stage 3 are taken as printed from the AR and the CareEdge rationale. "
     "The engine holds no stage-wise gross carrying amounts or provision balances to rebuild "
     "them from, so they are traceable but not reproducible here."),
    ("CRAR, LCR, cost of borrowings and the liquidity buffer are single-sourced",
     "CRAR 71%, the standalone LCR/PCR block, COST_OF_BORROWINGS and LIQUIDITY come from one "
     "disclosure each with no second source in the folder to reconcile against."),
    ("The Q1FY2027 block is unchecked",
     "Q1 income and PAT support the trend narrative only; no audited quarterly statement is in "
     "the case folder."),
    ("The FY2026 tax charge is a single literal",
     "The PAT waterfall uses a tax charge of 268.22 read from the P&L. It is not carried as a "
     "table input, so no mutation can reach it - the check proves the PBT/PAT relationship, "
     "not the tax line itself."),
]


def run():
    w = 52
    print("=" * 104)
    print("APTUS VALUE HOUSING FINANCE INDIA LIMITED - CareEdge HFC suite (CONSOLIDATED)")
    print("=" * 104)

    print("\nRATED FACILITIES - sanctioned LIMITS (failure mode 31).  " + PR)
    tot = 0.0
    for k, v in RATED.items():
        print(f"  {k:<34} Rs {v['amount']:>9,.2f} cr   {v['rating']}   {v['action']}")
        for ln, amt in v["lines"].items():
            print(f"      - {ln:<48} {amt:>9,.2f}")
        tot += v["amount"]
    print(f"  {'TOTAL RATED':<34} Rs {tot:>9,.2f} cr")

    def show(title, d):
        print(f"\n{title:<{w}}" + "".join(f"{y:>14}" for y in YEARS))
        for k, v in d.items():
            print(f"  {k:<{w-2}}" + "".join(f"{x:>14,.2f}" for x in v))

    show("CONSOLIDATED PROFIT AND LOSS", PL)
    show("TANGIBLE NET WORTH build-up (failure mode 32)", NW)
    tnw = [NW["Total equity (consolidated)"][i] - NW["less: intangible assets"][i]
           - NW["less: deferred tax assets"][i] for i in range(2)]
    print(f"  {'= TANGIBLE NET WORTH':<{w-2}}" + "".join(f"{x:>14,.2f}" for x in tnw))
    print(f"  {'  CareEdge published (FY2026)':<{w-2}}{'':>14}{TNW_PUBLISHED:>14,.2f}")
    show("BALANCE SHEET", BS)

    ti, pat, fc = PL["Total income"], PL["Profit after tax"], PL["Finance costs"]
    td, tot_assets = BS["TOTAL DEBT"], BS["Total assets"]

    print(f"\n{'RATIOS - CareEdge HFC conventions':<{w}}" + "".join(f"{y:>14}" for y in YEARS))

    def row(lab, vals, f="{:>14,.2f}"):
        print(f"  {lab:<{w-2}}" + "".join(f.format(v) for v in vals))

    gearing = [td[i] / tnw[i] for i in range(2)]
    aum_tnw = [AUM[i] / tnw[i] for i in range(2)]
    row("On-book gearing (x)  [KEY]", gearing, '{:>13.2f}x')
    row("  CareEdge published", [1.60, 1.56], '{:>13.2f}x')
    row("AUM / tangible net worth (x)", aum_tnw, '{:>13.2f}x')
    row("  CareEdge published", [2.53, 2.58], '{:>13.2f}x')
    row("Net interest income", [PL["Interest income"][i] - fc[i] for i in range(2)])
    row("NIM on average AUM (%)", [None, (PL["Interest income"][1] - fc[1])
                                   / ((AUM[0] + AUM[1]) / 2) * 100][1:] * 2, "{:>13.2f}%")
    row("PAT margin (%)", [pat[i] / ti[i] * 100 for i in range(2)], "{:>13.2f}%")
    row("Cost-to-income (%)", [(PL["Total expenses"][i] - fc[i] - PL["Impairment on financial "
        "instruments"][i]) / (ti[i] - fc[i]) * 100 for i in range(2)], "{:>13.2f}%")
    row("Credit cost on avg AUM (%)", [None, PL["Impairment on financial instruments"][1]
        / ((AUM[0] + AUM[1]) / 2) * 100][1:] * 2, "{:>13.2f}%")
    romaa = pat[1] / ((AUM[0] + AUM[1]) / 2) * 100
    rota = pat[1] / ((tot_assets[0] + tot_assets[1]) / 2) * 100
    ronw = pat[1] / ((tnw[0] + tnw[1]) / 2) * 100
    print(f"  {'Return on managed assets ROMA (%) - FY2026':<{w-2}}{'':>14}{romaa:>13.2f}%")
    print(f"  {'  AR reports RoA':<{w-2}}{'':>14}{7.9:>13.2f}%")
    print(f"  {'Return on total assets (%) - FY2026':<{w-2}}{'':>14}{rota:>13.2f}%")
    print(f"  {'Return on net worth (%) - FY2026':<{w-2}}{'':>14}{ronw:>13.2f}%")
    print(f"  {'  AR reports RoE':<{w-2}}{'':>14}{20.1:>13.2f}%")
    print(f"  {'Capital adequacy CRAR (%)':<{w-2}}{'':>14}{CRAR:>13.2f}%   (RBI min 15%)")

    print(f"\n{'ASSET QUALITY - TWO MEASURES, NOT ONE':<{w}}" + "".join(f"{y:>14}" for y in YEARS))
    for k, v in ASSET_QUALITY.items():
        print(f"  {k:<{w-2}}" + "".join(f"{x:>13.2f}%" for x in v))
    print(f"  Standalone Aptus HFC only: GNPA {STANDALONE_AQ['gnpa']}%, "
          f"NNPA {STANDALONE_AQ['nnpa']}%, PCR {STANDALONE_AQ['pcr_stage3']}%")

    print(f"\n{'AUM - the sector-defining metric':<{w}}")
    print("  " + "  ".join(f"{y}:{v:,}" for y, v in AUM_SERIES))
    print(f"  6-year CAGR ~26%.  FY2026 split: "
          + ", ".join(f"{n} Rs {v:,} cr ({p}%)" for n, v, p in AUM_SPLIT))

    print(f"\n{'Q1FY2027 (quarter ended 30-Jun-2026), consolidated':<{w}}")
    print(f"  Total income {Q1['total_income']:,.2f} vs {Q1['q1fy26_income']:,.2f} "
          f"({Q1['total_income']/Q1['q1fy26_income']-1:+.1%} YoY)")
    print(f"  PAT          {Q1['pat']:,.2f} vs {Q1['q1fy26_pat']:,.2f} "
          f"({Q1['pat']/Q1['q1fy26_pat']-1:+.1%} YoY)")

    # ------------------------------------------------------------------ tie-outs
    print("\n" + "=" * 104)
    print("TIE-OUTS - the test is REPRODUCING CareEdge's published figures")
    print("=" * 104)
    # ONE definition of the checks: printed here exactly as the tools receive them.
    T = tieouts(compute())
    fail = 0
    for lab, comp, disc, tol, _src in T:
        ok = abs(comp - disc) <= tol
        fail += (not ok)
        print(f"  [{'OK ' if ok else 'FAIL'}] {lab:<52} computed {comp:>10,.2f}"
              f"  published {disc:>10,.2f}")
    print(f"\n{len(T)-fail}/{len(T)} reconcile.")
    for title, text in DISCLOSED_DIFFERENCES:
        print(f"\n  [DISCLOSED] {title}\n              {text}")
    return fail


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
