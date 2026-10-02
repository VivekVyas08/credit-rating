"""Indus Towers Limited - Step 12 forward view, FY2027 to FY2031.

WHAT THIS IS, AND WHAT IT IS NOT
-------------------------------
A five-year projection of the credit path, built in code off the verified FY2026 actuals in
compute_ratios.py. It is not the equity-research plugin's native 3-statement workbook; the
scaling decision and its reason are recorded in case.json.

THE MODEL IS DRIVEN BY CO-LOCATIONS, NOT BY A REVENUE GROWTH PERCENTAGE. A tower company earns
rent per tenancy, so revenue is built as (co-locations x revenue per co-location) and the
TENANCY RATIO falls out of the tower and co-location paths rather than being assumed. This is
the sector's defining metric (failure mode 21) and its direction is a finding in its own right:

    FY2024   219,736 towers   368,588 co-locations   tenancy 1.677
    FY2025   249,305 towers   405,435 co-locations   tenancy 1.626
    FY2026   264,514 towers   428,014 co-locations   tenancy 1.618

Tenancy has FALLEN in each of the last two years because towers were added faster than tenants
were found for them - FY2025 includes 12,606 towers and co-locations acquired from Bharti
Airtel. A single-year snapshot would have shown "industry-leading tenancy of 1.6x" and missed
that the trend is downward (failure mode 16).

THE DEBT PATH IS DERIVED, NOT ASSUMED (failure mode 18):
    external funding need = capex + lease principal repaid + interest + tax + buyback
                            - normalised EBITDA
Borrowings and LEASE liabilities are tracked separately, and this is not a presentational
nicety on this issuer: at FY2026 borrowings were Rs 920.9 crore against lease liabilities of
Rs 20,206.0 crore. Ground leases ARE the liability structure of a tower company. Reporting a
single "total debt" number without that split would misdescribe the balance sheet.

EARNINGS ARE NORMALISED THROUGHOUT. Reported EBITDA contains net WRITE-BACKS of allowances for
doubtful receivables - Rs 5,077.1 crore in FY2025 and Rs 256.0 crore in FY2026 - which are the
Vodafone Idea recovery running back through other expenses. On reported figures FY2026 EBITDA
FELL 12.9%; normalised, it GREW 12.9%. The projection is built on the normalised base.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402

YEARS = ["FY2027", "FY2028", "FY2029", "FY2030", "FY2031"]
MN = C.MN                                                # Rs million -> Rs crore
D = C.D
LAST = 2

# --------------------------------------------------------------------- operating series
# Towers and co-locations as reported in each year's annual report. Read as a DATED SERIES
# rather than a latest value (failure mode 30), which is how the tenancy decline became
# visible at all.
TOWERS = {"FY2024": 219736, "FY2025": 249305, "FY2026": 264514}
COLOCATIONS = {"FY2024": 368588, "FY2025": 405435, "FY2026": 428014}

BASE = {
    "revenue":     D["revenue"][LAST] / MN,
    # Reported EBITDA plus the write-back line. The write-back is stored NEGATIVE (a credit),
    # so adding it removes the credit and leaves the underlying figure.
    "ebitda":      (D["ebitda_rep"][LAST] + D["writeback"][LAST]) / MN,
    "borrowings":  D["borrowings"][LAST] / MN,
    "leases":      D["leases"][LAST] / MN,
    "cash":        (D["cash"][LAST] + D["bank_other"][LAST] + D["cur_invest"][LAST]) / MN,
    "equity":      D["equity"][LAST] / MN,
    "receivables": D["receivables"][LAST] / MN,
    "dep":         D["dep"][LAST] / MN,
    "towers":      TOWERS["FY2026"],
    "colocations": COLOCATIONS["FY2026"],
    # Consolidated cash-flow statement, FY2026 integrated report (L15346 / L19380):
    # purchase of PPE, intangibles and CWIP 86,258 million.
    "capex":       86258.0 / MN,
    # Repayment of principal portion of lease liabilities, same statement.
    "lease_repaid": 25131.0 / MN,
    "interest_paid": 17076.0 / MN,
}
BASE["rev_per_colo"] = BASE["revenue"] / BASE["colocations"] * 1e7      # Rs per co-location

# --------------------------------------------------------------------------- drivers, sourced
DRIVERS = {
    "tower_adds": {
        "value": [16000, 15000, 14000, 13000, 12000],
        "source": "Net macro-tower additions were 15,209 in FY2026 (from 249,305 to 264,514) "
                  "and 29,569 in FY2025, of which about 12.6 thousand were the Bharti Airtel "
                  "acquisition rather than organic build. The organic FY2025 run rate is "
                  "therefore roughly 17,000. Held near the FY2026 organic level and tapering, "
                  "since the network build for the current 4G/5G cycle is well advanced.",
    },
    "colocation_adds": {
        "value": [24000, 24000, 23000, 22000, 21000],
        "source": "Net co-location additions were 22,579 in FY2026 and 36,847 in FY2025 (the "
                  "latter including the Airtel portfolio). Set slightly ABOVE the FY2026 pace "
                  "so that tenancy stabilises rather than continuing to fall - which is an "
                  "assumption, and a favourable one. It is the driver the stress case reverses.",
    },
    "rev_per_colo_growth": {
        "value": [0.005, 0.010, 0.010, 0.015, 0.015],
        "source": "Revenue per co-location was Rs 7.59 lakh in FY2026 (Rs 32,493.1 crore over "
                  "428,014 co-locations) against Rs 7.43 lakh in FY2025 - up 2.2%. Master "
                  "service agreements are long-tenure with contracted escalations, but the "
                  "customer base is three operators and pricing pressure is structural, so "
                  "near-flat is assumed in the early years, improving as 5G loading raises "
                  "the revenue per tenancy.",
    },
    "ebitda_margin": {
        "value": [0.560, 0.565, 0.565, 0.570, 0.570],
        "source": "Normalised OPBDITA margin was 55.99% in FY2026 (Rs 18,196.6 crore on "
                  "Rs 32,493.1 crore) against 53.49% in FY2025 and 52.64% in FY2024 - rising "
                  "as the acquired portfolio is absorbed and energy pass-through normalises. "
                  "Held near the FY2026 level with a slow improvement; the operating leverage "
                  "in a tower business accrues to co-locations added on EXISTING towers, which "
                  "is why the co-location path and the margin path are linked.",
    },
    "capex": {
        "value": [8000.0, 7500.0, 7000.0, 6500.0, 6500.0],
        "source": "Capex was Rs 8,952.9 crore in FY2024, Rs 6,784.0 crore in FY2025 and "
                  "Rs 8,625.8 crore in FY2026 (consolidated cash flow, purchase of PPE, "
                  "intangibles and CWIP). Tapering with the tower-addition path, since the "
                  "great majority of it is the towers themselves.",
    },
    "interest_rate": {
        "value": [0.085, 0.085, 0.085, 0.085, 0.085],
        "source": "Interest paid was Rs 1,707.6 crore in FY2026 on borrowings of Rs 920.9 "
                  "crore and lease liabilities of Rs 20,206.0 crore - i.e. the charge is "
                  "overwhelmingly the lease unwind, not bank interest. Applied to the lease "
                  "book at 8.5%, which reproduces the FY2026 charge within tolerance, and to "
                  "borrowings at the same rate.",
    },
    "tax_rate": {
        "value": [0.256, 0.256, 0.256, 0.256, 0.256],
        "source": "FY2026 tax was Rs 2,452.9 crore on reported PBT of Rs 9,597.8 crore = "
                  "25.56%, consistent with the concessional regime. Held flat.",
    },
}


def project(stress=False):
    """Base case, or a stress flexing what CRISIL's telecom-infrastructure criteria name."""
    d = {k: list(v["value"]) for k, v in DRIVERS.items()}
    if stress:
        # The named risks for a tower company are tenant concentration and tenancy dilution.
        # The stress is therefore a TENANCY stress: towers keep being built on contract while
        # co-location additions collapse, and revenue per co-location falls as the operators
        # press on renewal pricing. Capex is NOT cut - the build is contracted.
        d["colocation_adds"] = [8000, 6000, 5000, 5000, 5000]
        d["rev_per_colo_growth"] = [-0.030, -0.030, -0.020, -0.010, 0.0]
        d["ebitda_margin"] = [0.535, 0.525, 0.520, 0.520, 0.520]

    towers = BASE["towers"]
    colos = BASE["colocations"]
    rpc = BASE["rev_per_colo"]
    borrowings = BASE["borrowings"]
    leases = BASE["leases"]
    cash = BASE["cash"]
    equity = BASE["equity"]

    rows = []
    for i, y in enumerate(YEARS):
        towers += d["tower_adds"][i]
        colos += d["colocation_adds"][i]
        rpc *= (1.0 + d["rev_per_colo_growth"][i])
        rev = colos * rpc / 1e7
        ebitda = rev * d["ebitda_margin"][i]

        interest = (borrowings + leases) * d["interest_rate"][i]
        dep = BASE["dep"] * (1.0 + 0.06 * (i + 1))
        pbt = ebitda - dep - interest
        tax = max(0.0, pbt) * d["tax_rate"][i]
        pat = pbt - tax

        # Lease principal repaid grows with the ground-lease book; new towers add new leases.
        lease_repaid = BASE["lease_repaid"] * (1.0 + 0.05 * (i + 1))
        lease_added = d["tower_adds"][i] * 0.155        # Rs crore of new lease per tower added

        funding_need = (d["capex"][i] + lease_repaid + interest + tax) - ebitda
        usable_cash = max(0.0, cash - 1000.0)
        new_debt = max(0.0, funding_need - usable_cash)
        if funding_need < 0:
            repay = min(borrowings, -funding_need)
            borrowings -= repay
            cash += (-funding_need) - repay
        else:
            cash = max(1000.0, cash - max(0.0, funding_need - new_debt))
        borrowings += new_debt
        leases = leases - lease_repaid + lease_added + interest * (leases / (leases + borrowings
                                                                            + 1e-9))
        equity += pat
        debt = borrowings + leases

        rows.append({
            "Year": y,
            "Towers": int(towers),
            "Co-locations": int(colos),
            "Tenancy ratio (x)": round(colos / towers, 3),
            "Revenue": round(rev, 0),
            "OPBDITA (normalised)": round(ebitda, 0),
            "OPBDITA margin %": round(100 * d["ebitda_margin"][i], 1),
            "Capex": round(d["capex"][i], 0),
            "Lease principal repaid": round(lease_repaid, 0),
            "Interest": round(interest, 0),
            "PAT": round(pat, 0),
            "Funding gap": round(funding_need, 0),
            "New borrowing raised": round(new_debt, 0),
            "Borrowings": round(borrowings, 0),
            "Lease liabilities": round(leases, 0),
            "Total debt (incl. leases)": round(debt, 0),
            "Net worth": round(equity, 0),
            "TD/OPBDITA (x)": round(debt / ebitda, 2) if ebitda > 0 else None,
            "Borrowings/OPBDITA (x)": round(borrowings / ebitda, 2) if ebitda > 0 else None,
            "Interest coverage (x)": round(ebitda / interest, 2) if interest > 0 else None,
        })
    return rows


def check():
    """Tie the FY2026 starting point back to the engine and to the printed statements."""
    out = []

    def t(desc, computed, disclosed, tol):
        out.append((desc, computed, disclosed, tol, abs(computed - disclosed) <= tol))

    t("Capex ties to the consolidated cash flow, FY2026", BASE["capex"], 86258.0 / MN, 0.01)
    t("Lease principal repaid ties to the cash flow, FY2026",
      BASE["lease_repaid"], 25131.0 / MN, 0.01)
    t("Closing cash ties to the cash flow, FY2026", D["cash"][LAST] / MN, 473.0 / MN, 0.01)
    t("Normalised OPBDITA removes the FY2026 write-back",
      BASE["ebitda"], (184526.0 - 2560.0) / MN, 0.01)
    t("Normalised OPBDITA grew 12.9% in FY2026, against a REPORTED 12.9% fall",
      BASE["ebitda"] / ((D["ebitda_rep"][1] + D["writeback"][1]) / MN) - 1.0, 0.129, 0.002)
    t("Reported OPBDITA did fall 12.9% - the number the normalisation exists to correct",
      D["ebitda_rep"][LAST] / D["ebitda_rep"][1] - 1.0, -0.129, 0.002)
    t("FY2026 tenancy ratio", COLOCATIONS["FY2026"] / TOWERS["FY2026"], 1.618, 0.001)
    t("FY2025 tenancy ratio", COLOCATIONS["FY2025"] / TOWERS["FY2025"], 1.626, 0.001)
    t("FY2024 tenancy ratio", COLOCATIONS["FY2024"] / TOWERS["FY2024"], 1.677, 0.001)
    t("Interest rate reproduces the FY2026 interest paid",
      (BASE["borrowings"] + BASE["leases"]) * 0.085, BASE["interest_paid"], 150.0)
    t("Effective tax rate, FY2026",
      (D["pbt_rep"][LAST] - D["pat_rep"][LAST]) / D["pbt_rep"][LAST], 0.2556, 0.001)
    t("Leases dominate the debt stack, FY2026",
      BASE["leases"] / (BASE["leases"] + BASE["borrowings"]), 0.9564, 0.001)
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    print("=" * 112)
    print("OPENING-BALANCE TIE-OUT (a forward model inherits every error in its starting point)")
    print("-" * 112)
    res = check()
    for desc, comp, disc, tol, ok in res:
        print("  %-66s %12.4f vs %12.4f  %s" % (desc[:66], comp, disc, "OK" if ok else "FAIL"))
    bad = [r for r in res if not r[4]]
    print("  %d of %d opening-balance checks reconcile" % (len(res) - len(bad), len(res)))
    print()

    for label, stress in (("BASE CASE", False), ("STRESS CASE", True)):
        rows = project(stress)
        keys = [k for k in rows[0] if k != "Year"]
        print("=" * 112)
        print("%s - Indus Towers Limited, consolidated, Rs crore" % label)
        print("-" * 112)
        print("%-28s%s" % ("", "".join("%14s" % r["Year"] for r in rows)))
        for k in keys:
            print("%-28s%s" % (k, "".join(
                "%14s" % ("n/a" if r[k] is None else "{:,}".format(r[k])) for r in rows)))
        print()

    print("=" * 112)
    print("WHAT THE ARITHMETIC SAYS")
    print("-" * 112)
    b, s = project(False), project(True)
    print("  Base   : tenancy %.3fx by FY2031, borrowings Rs %s cr, borrowings/OPBDITA %.2fx,"
          % (b[-1]["Tenancy ratio (x)"], "{:,.0f}".format(b[-1]["Borrowings"]),
             b[-1]["Borrowings/OPBDITA (x)"]))
    print("           total debt incl. leases Rs %s cr, TD/OPBDITA %.2fx"
          % ("{:,.0f}".format(b[-1]["Total debt (incl. leases)"]), b[-1]["TD/OPBDITA (x)"]))
    print("  Stress : tenancy %.3fx by FY2031, borrowings Rs %s cr, borrowings/OPBDITA %.2fx,"
          % (s[-1]["Tenancy ratio (x)"], "{:,.0f}".format(s[-1]["Borrowings"]),
             s[-1]["Borrowings/OPBDITA (x)"]))
    print("           total debt incl. leases Rs %s cr, TD/OPBDITA %.2fx"
          % ("{:,.0f}".format(s[-1]["Total debt (incl. leases)"]), s[-1]["TD/OPBDITA (x)"]))
    print()
    print("  THE STRUCTURAL POINT. Borrowings fell from Rs 4,311.8 crore to Rs 2,262.4 crore to")
    print("  Rs 920.9 crore across FY2024-FY2026 while the company also bought back Rs 2,640")
    print("  crore of equity in FY2025 and paid no dividend. This is a business that generates")
    print("  more cash than it needs even while spending Rs 8,000+ crore a year on capex. The")
    print("  leverage that remains is the GROUND-LEASE book, which is contractual, matched to")
    print("  the revenue it supports, and does not behave like borrowed money.")
    print()
    print("  WHAT THIS MODEL DELIBERATELY DOES NOT ASSUME: a distribution policy. The surplus")
    print("  above simply accumulates, which is NOT a forecast that it will. The company paid")
    print("  no dividend in FY2024, FY2025 or FY2026 and instead bought back Rs 2,640 crore of")
    print("  equity in FY2025 - three years, two different answers, and no stated policy. Any")
    print("  payout assumption would be invented, so none is made, and the cash and net-worth")
    print("  lines should be read as a RESIDUAL rather than as a projected balance sheet. The")
    print("  credit conclusion is unaffected: a distribution large enough to matter would still")
    print("  leave the funding gap negative in every year of both cases.")
    print()
    print("  THE RISK IS NOT LEVERAGE, IT IS TENANCY. The ratio has fallen two years running")
    print("  (1.677 -> 1.626 -> 1.618) because towers were added faster than tenants. The")
    print("  stress case asks what happens if that continues and pricing turns: even then")
    print("  borrowings stay modest against OPBDITA. The exposure is to the EARNINGS level,")
    print("  through a three-customer market, not to the capital structure.")

    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
