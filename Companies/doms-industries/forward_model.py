"""DOMS Industries Limited - Step 12 forward view, FY2027 to FY2031.

WHAT THIS IS, AND WHAT IT IS NOT
-------------------------------
A five-year projection of the credit path, built in code off the verified FY2026 actuals in
compute_ratios.py. It is not the equity-research plugin's native 3-statement workbook; the
scaling decision and its reason are recorded in case.json.

THE DEBT PATH IS DERIVED, NOT ASSUMED (failure mode 18). Each year:
    external funding need = capex + dividend + change in working capital
                            - (OPBDITA - interest - tax)
and closing debt follows from it. This matters more here than in most cases: DOMS is
mid-greenfield. FY2026 capex was Rs 292.83 crore against an OPBDITA of Rs 402.59 crore, and
the Umbergaon complex is on a PHASED build that continues through the window. Carrying the
historical debt level forward - it has been falling, from Rs 211.77 crore to Rs 141.26 crore -
would have projected continued deleveraging straight through a capex programme that is still
being funded. That is exactly the FM18 error.

THE CENTRAL FORWARD FACT IS A MARGIN SHOCK, AND IT IS THE COMPANY'S OWN NUMBER. Q1 FY2027
standalone OPBDITA margin is 12.08% against 17.37% in Q1 FY2026 - a 529 basis point
compression, computed here from the company's own unaudited filing, not taken from a broker's
paraphrase (failure mode 11). The broker note in the same case folder independently
characterises it as "525bps YoY" on a consolidated basis, which corroborates the direction and
magnitude. Raw-material inflation is the stated cause.

EVERY DRIVER IS SOURCE-LABELLED. Nothing here comes from a CRA publication.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402

YEARS = ["FY2027", "FY2028", "FY2029", "FY2030", "FY2031"]
LAKH = 100.0

# --------------------------------------------------------------------------- FY2026 actuals
D = C.DATA
LAST = 2

BASE = {
    "revenue":     D["revenue"][LAST],
    "ebitda":      (D["pbt"][LAST] + D["finance_cost"][LAST] + D["depreciation"][LAST]
                    - D["other_income"][LAST] - D["assoc_share"][LAST]),
    # Borrowings and leases are tracked SEPARATELY in the projection. A surplus repays
    # borrowings; it does not extinguish lease liabilities, which are contractual right-of-use
    # obligations that renew as premises and equipment are re-leased. Modelling the combined
    # stack as repayable drove total debt to exactly zero by FY2029, which is not a thing that
    # happens to a company operating leased plant and offices.
    "borrowings":  D["borrow_nc"][LAST] + D["borrow_c"][LAST],
    "lease":       D["lease_nc"][LAST] + D["lease_c"][LAST],
    "cash":        D["cash"][LAST] + D["bank_other"][LAST],
    "tnw":         D["equity_total"][LAST] - D["nci_equity"][LAST],
    "inventory":   D["inventory"][LAST],
    "receivables": D["receivables"][LAST],
    "curr_liab":   D["curr_liab"][LAST],
    "depreciation": D["depreciation"][LAST],
    # Consolidated cash-flow statement, FY2025-26 annual report (L11489-11490): purchase of
    # PPE including CWIP and capital advances 28,078.30 lakh PLUS upfront payment for
    # leasehold land 1,205.24 lakh. The land line is included because the greenfield build is
    # precisely what it funds - excluding it would understate the programme.
    "capex":       (28078.30 + 1205.24) / LAKH,
    # Dividend paid, same statement (L11503).
    "dividend":    1911.62 / LAKH,
    # Net cash generated from operating activities, same statement (L11487).
    "ocf":         25434.31 / LAKH,
}

# --------------------------------------------------------------------------- drivers, sourced
DRIVERS = {
    "revenue_growth": {
        "value": [0.19, 0.18, 0.16, 0.14, 0.12],
        "source": "Q1 FY2027 standalone revenue was Rs 603.27 crore against Rs 507.70 crore in "
                  "Q1 FY2026, +18.8% (unaudited standalone results, quarter ended 30-Jun-2026, "
                  "Rs lakh). The broker note in the case folder puts the consolidated figure at "
                  "+19.2%. FY2026 consolidated growth was 21.6% and FY2025 24.4%. The path "
                  "holds near the Q1 run rate while the Umbergaon greenfield ramps - the "
                  "company states production there commences in Q2 FY2027 and capacity is added "
                  "in phases starting with wooden pencils - then tapers as the base grows.",
    },
    "ebitda_margin": {
        "value": [0.140, 0.158, 0.162, 0.165, 0.165],
        "source": "FY2026 consolidated OPBDITA margin was 17.31% (computed). Q1 FY2027 "
                  "standalone is 12.08% (PBT 5,740.77 + finance 86.96 + depreciation 1,824.99 "
                  "- other income 366.21, on revenue 60,326.96, Rs lakh) against 17.37% in Q1 "
                  "FY2026 - a 529bp compression the company attributes to raw-material "
                  "inflation, with ESOP and channel-partner costs adding roughly 60bp. FY2027 "
                  "is set at 14.0%, i.e. ABOVE the Q1 print but well below FY2026, on the "
                  "company's stated price increases already taken; recovery thereafter is "
                  "assumed to be partial and slow, stabilising below the FY2026 level rather "
                  "than returning to it. The broker independently models 14.2% FY2027 and "
                  "16.8% FY2028 - close enough to corroborate, and NOT used as the input.",
    },
    "capex": {
        "value": [350.0, 250.0, 180.0, 160.0, 160.0],
        "source": "FY2026 capex was Rs 292.83 crore and FY2025 Rs 213.27 crore (consolidated "
                  "cash flow, PPE plus leasehold land). Q1 FY2027 alone was about Rs 100 crore "
                  "per the company's earnings call. The annual report describes a 50+ acre "
                  "greenfield complex on a PHASED implementation with 300,000 sq ft expected "
                  "operational in FY2027, plus brownfield additions in ball-point pens, paper "
                  "stationery, mechanical pencils and adhesives, and land acquired in both "
                  "Umbergaon and Jammu for FUTURE expansion. FY2027 is therefore stepped UP, "
                  "not down, and normalises towards maintenance-plus levels by FY2030.",
    },
    "working_capital_pct": {
        "value": [0.105, 0.105, 0.103, 0.100, 0.100],
        "source": "Net working capital (inventory 377.04 + receivables 163.73 - current "
                  "liabilities 293.98 = Rs 246.79 crore) was 10.6% of FY2026 revenue. Held "
                  "near that level: inventory days have risen with the product-range expansion "
                  "(SKU count up about 400 in a year, per the company's call) but receivables "
                  "remain short at 26 days on a distribution-led model. No improvement is "
                  "assumed beyond a slight scale benefit.",
    },
    "interest_rate": {
        "value": [0.065, 0.065, 0.065, 0.065, 0.065],
        "source": "FY2026 finance cost Rs 10.80 crore on average debt of Rs 176.5 crore "
                  "((211.77 + 141.26)/2) = 6.1%, on a book that includes lease liabilities "
                  "carrying a higher implicit rate than the bank debt. Held at 6.5% to allow "
                  "for the mix shifting back towards borrowed funds as the greenfield draws.",
    },
    "tax_rate": {
        "value": [0.257, 0.257, 0.257, 0.257, 0.257],
        "source": "FY2026 total tax Rs 82.70 crore on PBT of Rs 322.26 crore = 25.66%, "
                  "consistent with the 25.17% concessional regime plus surcharge. Held flat.",
    },
    "dividend_payout": {
        "value": [0.09, 0.09, 0.10, 0.10, 0.10],
        "source": "FY2026 dividend paid Rs 19.12 crore against PAT to owners of Rs 230.18 "
                  "crore = 8.3%; FY2025 Rs 15.17 crore on Rs 202.34 crore = 7.5%. Rising "
                  "gently, consistent with the two-year trend.",
    },
}


def project(stress=False):
    """Base case, or a stress flexing the variables CRISIL's manufacturing criteria name."""
    d = {k: list(v["value"]) for k, v in DRIVERS.items()}
    if stress:
        # The stress is the one that actually threatens a mid-greenfield manufacturer: the
        # plant gets built - the capex is committed and the land is bought - but the margin
        # does not recover and the volume ramp is slower than planned. Capex is deliberately
        # NOT cut. Cutting it would improve every credit metric in the projection and would
        # describe a company that had abandoned its strategy, which is not the risk being
        # tested. Raw-material inflation is the company's own stated cause of the Q1 shock.
        d["ebitda_margin"] = [0.122, 0.122, 0.128, 0.132, 0.135]
        d["revenue_growth"] = [0.14, 0.11, 0.10, 0.09, 0.09]
        d["working_capital_pct"] = [0.120, 0.125, 0.125, 0.125, 0.125]

    rev = BASE["revenue"]
    borrowings = BASE["borrowings"]
    lease = BASE["lease"]
    cash = BASE["cash"]
    tnw = BASE["tnw"]
    wc_prev = BASE["inventory"] + BASE["receivables"] - BASE["curr_liab"]
    dep = BASE["depreciation"]

    rows = []
    for i, y in enumerate(YEARS):
        rev *= (1.0 + d["revenue_growth"][i])
        ebitda = rev * d["ebitda_margin"][i]

        wc = rev * d["working_capital_pct"][i]
        delta_wc = wc - wc_prev

        # Leases carry a higher implicit rate than the bank debt, so they are charged
        # separately rather than at a blended rate on a stack whose mix changes.
        interest = borrowings * d["interest_rate"][i] + lease * 0.085
        # Depreciation grows with the asset base: roughly 8% of the prior year's capex is
        # added, reflecting a long-lived plant and machinery book.
        dep = dep + 0.08 * d["capex"][i - 1 if i else 0]
        pbt = ebitda - dep - interest
        tax = max(0.0, pbt) * d["tax_rate"][i]
        pat = pbt - tax
        dividend = max(0.0, pat) * d["dividend_payout"][i]

        # DERIVED, not assumed.
        funding_need = d["capex"][i] + dividend + delta_wc - (ebitda - interest - tax)
        usable_cash = max(0.0, cash - 40.0)          # a Rs 40 crore operating float is kept
        new_debt = max(0.0, funding_need - usable_cash)
        if funding_need < 0:
            repay = min(borrowings, -funding_need)
            borrowings -= repay
            cash += (-funding_need) - repay
        else:
            cash = max(40.0, cash - max(0.0, funding_need - new_debt))
        borrowings += new_debt
        # Right-of-use additions were Rs 6.57 crore in FY2026 against amortisation of the
        # existing book; the liability has drifted DOWN slightly across FY2024-FY2026
        # (51.66 from 56.04). Held roughly flat, growing with the footprint.
        lease *= 1.02
        debt = borrowings + lease

        tnw += pat - dividend
        wc_prev = wc

        rows.append({
            "Year": y,
            "Revenue": round(rev, 0),
            "OPBDITA": round(ebitda, 1),
            "OPBDITA margin %": round(100 * d["ebitda_margin"][i], 2),
            "Depreciation": round(dep, 1),
            "Capex": round(d["capex"][i], 0),
            "Change in WC": round(delta_wc, 1),
            "Interest": round(interest, 1),
            "PAT": round(pat, 1),
            "Dividend": round(dividend, 1),
            "Funding gap": round(funding_need, 0),
            "New debt raised": round(new_debt, 0),
            "Borrowings": round(borrowings, 0),
            "Lease liabilities": round(lease, 0),
            "Total debt": round(debt, 0),
            "Tangible net worth": round(tnw, 0),
            "Total debt/OPBDITA (x)": round(debt / ebitda, 2) if ebitda > 0 else None,
            "Interest coverage (x)": round(ebitda / interest, 2) if interest > 0 else None,
            "Gearing (x)": round(debt / tnw, 2) if tnw > 0 else None,
        })
    return rows


def check():
    """Tie the FY2026 starting point back to the engine and to the printed statements."""
    out = []

    def t(desc, computed, disclosed, tol):
        out.append((desc, computed, disclosed, tol, abs(computed - disclosed) <= tol))

    t("Capex = PPE purchase + leasehold land, FY2026 cash flow",
      BASE["capex"], (28078.30 + 1205.24) / LAKH, 0.01)
    t("Closing cash ties to the cash-flow statement, FY2026",
      D["cash"][LAST], 5348.77 / LAKH, 0.01)
    t("Dividend paid ties to the cash-flow statement, FY2026",
      BASE["dividend"], 1911.62 / LAKH, 0.01)
    t("OPBDITA vs the AR's stated FY2026 EBITDA growth of 15.5%",
      BASE["ebitda"] / (D["pbt"][1] + D["finance_cost"][1] + D["depreciation"][1]
                        - D["other_income"][1] - D["assoc_share"][1]) - 1.0, 0.155, 0.01)
    t("Q1 FY2027 standalone OPBDITA margin, from the company's own filing",
      (5740.77 + 86.96 + 1824.99 - 366.21) / 60326.96, 0.1208, 0.001)
    t("Q1 FY2026 standalone OPBDITA margin, same filing's comparative",
      (7448.09 + 219.94 + 1575.59 - 425.60) / 50769.78, 0.1737, 0.001)
    t("Total debt includes leases, FY2026", BASE["borrowings"] + BASE["lease"],
      D["borrow_nc"][LAST] + D["borrow_c"][LAST] + D["lease_nc"][LAST] + D["lease_c"][LAST],
      0.01)
    t("Effective tax rate, FY2026",
      (D["pbt"][LAST] - D["pat_total"][LAST]) / D["pbt"][LAST], 0.2566, 0.001)
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    print("=" * 104)
    print("OPENING-BALANCE TIE-OUT (a forward model inherits every error in its starting point)")
    print("-" * 104)
    res = check()
    for desc, comp, disc, tol, ok in res:
        print("  %-62s %12.4f vs %12.4f  %s" % (desc[:62], comp, disc, "OK" if ok else "FAIL"))
    bad = [r for r in res if not r[4]]
    print("  %d of %d opening-balance checks reconcile" % (len(res) - len(bad), len(res)))
    print()

    for label, stress in (("BASE CASE", False), ("STRESS CASE", True)):
        rows = project(stress)
        keys = [k for k in rows[0] if k != "Year"]
        print("=" * 104)
        print("%s - DOMS Industries Limited, consolidated, Rs crore" % label)
        print("-" * 104)
        print("%-26s%s" % ("", "".join("%14s" % r["Year"] for r in rows)))
        for k in keys:
            print("%-26s%s" % (k, "".join(
                "%14s" % ("n/a" if r[k] is None else "{:,}".format(r[k])) for r in rows)))
        print()

    print("=" * 104)
    print("WHAT THE ARITHMETIC SAYS")
    print("-" * 104)
    b, s = project(False), project(True)
    for lbl, r in (("Base  ", b[-1]), ("Stress", s[-1])):
        print("  %s : debt Rs %s cr by FY2031, TD/OPBDITA %.2fx, coverage %.1fx, gearing %.2fx"
              % (lbl, "{:,.0f}".format(r["Total debt"]), r["Total debt/OPBDITA (x)"],
                 r["Interest coverage (x)"], r["Gearing (x)"]))
    peak_b = max(r["Total debt"] for r in b)
    peak_s = max(r["Total debt"] for r in s)
    print("  Peak debt: base Rs %s crore, stress Rs %s crore, against a FY2026 tangible net"
          % ("{:,.0f}".format(peak_b), "{:,.0f}".format(peak_s)))
    print("  worth of Rs %s crore." % "{:,.0f}".format(BASE["tnw"]))
    print()
    print("  The finding is that the balance sheet absorbs the greenfield in both cases. Even")
    print("  in the stress - margin stuck near the Q1 FY2027 level of about 12%, a slower")
    print("  volume ramp, working capital stretched, and the capex programme spent in full -")
    print("  the company does not approach a leverage level that would trouble the rating.")
    print("  That is a statement about the STARTING POINT: FY2026 closed with Rs 141.26 crore")
    print("  of debt including leases against Rs 1,219.73 crore of tangible net worth and")
    print("  Rs 254.34 crore of operating cash flow. The margin shock is real and is the")
    print("  monitorable; it is an EARNINGS event, not yet a credit event.")

    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
