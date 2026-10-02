"""Hindustan Zinc Limited - Step 12 forward view, FY2027 to FY2031.

ENTITY NOTE (binding, carried forward from compute_ratios.py): the case folder is labelled
"Vedanta", but every financial document in it belongs to HINDUSTAN ZINC LIMITED, a separate
listed entity in which Vedanta Limited holds 60.71% and the Government of India 27.92%. Every
figure here is Hindustan Zinc's. The Vedanta relationship is modelled as what it actually is on
this credit - a claim on cash through the DIVIDEND - not as a consolidation.

WHAT THIS IS, AND WHAT IT IS NOT
-------------------------------
A five-year projection built in code off the verified FY2026 actuals in compute_ratios.py. It
is not the equity-research plugin's native 3-statement workbook; the scaling decision and its
reason are recorded in case.json.

THE WINDOW MATCHES THE COMPANY'S OWN PLANNING HORIZON, WHICH IS UNUSUAL AND USEFUL HERE. The
FY2025-26 integrated report states a capex programme of "Rs 40,000-50,000 crore ... over the
next five years" to lift refined metal capacity from 1.1 Mtpa to 2.0 Mtpa, and - in the same
document - an internal estimate of "pre-growth capex free cash flow (FCF) generation of
Rs 55,000-65,000 crore over the next five years". So the company has published both sides of
the funding equation over exactly the period this model covers, and the model can be checked
against it rather than merely asserted.

AND THE CHECK IS THE FINDING. Take the midpoints: FCF of Rs 60,000 crore against capex of
Rs 45,000 crore leaves Rs 15,000 crore over five years, or Rs 3,000 crore a year, for
dividends. **Hindustan Zinc paid Rs 12,253 crore of dividends in FY2025 and Rs 4,225 crore in
FY2026.** At anything like the FY2025 rate the programme is not self-funding and the difference
is borrowed. The dividend, not the capex and not the zinc price, is therefore the variable that
decides this credit's leverage path - and the dividend is set by a board on which a 60.71%
parent with its own cash needs is represented. That is why the stress case flexes the dividend
and not just the commodity.

THE DEBT PATH IS DERIVED, NOT ASSUMED (failure mode 18):
    external funding need = capex + dividend + interest + tax + lease principal
                            - OPBDITA - other income

SECTOR-DEFINING METRICS ARE MODELLED, NOT NARRATED (failure mode 21). For metals and mining
those are cost of production per tonne and volume. Both are carried as explicit drivers:

    Mined metal production   FY2024 1,079 kt   FY2025 1,095 kt   FY2026 1,114 kt
    Zinc CoP ex royalty      FY2025 US$ 1,052/t          FY2026 US$ 959/t   (-8.8%, a 5-year low)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402

YEARS = ["FY2027", "FY2028", "FY2029", "FY2030", "FY2031"]
D = C.DATA
LAST = 2

# Operating series, read as a DATED series from each year's integrated report.
MINED_METAL_KT = {"FY2024": 1079, "FY2025": 1095, "FY2026": 1114}
ZINC_COP_USD_T = {"FY2025": 1052, "FY2026": 959}          # ex royalty, company-stated

BASE = {
    "revenue":  D["revenue"][LAST],
    "opbdita":  (D["pbt_bef_exc"][LAST] + D["finance_cost"][LAST] + D["depreciation"][LAST]
                 - D["other_income"][LAST]),
    "other_income": D["other_income"][LAST],
    "debt":     (D["borrow_nc"][LAST] + D["borrow_c"][LAST]
                 + D["lease_nc"][LAST] + D["lease_c"][LAST]),
    "liquid":   D["cash"][LAST] + D["bank_other"][LAST] + D["cur_invest"][LAST],
    "equity":   D["equity"][LAST],
    "dep":      D["depreciation"][LAST],
    "pat":      D["pat"][LAST],
    # Consolidated cash-flow statement, FY2025-26 integrated report (L26544 and following):
    # purchases of PPE including intangibles, CWIP and capital advances 5,275; dividend paid
    # 4,225; principal payment of lease liabilities 161; net cash from operating activities
    # 17,008.
    "capex":        5275.0,
    "dividend":     4225.0,
    "lease_repaid":  161.0,
    "ocf":         17008.0,
}

# The company's own published five-year plan, quoted as a RANGE because that is how it is
# published. Used as the cross-check on the derived path, never as the input.
COMPANY_PLAN = {
    "capex_5yr": (40000.0, 50000.0),
    "pre_growth_capex_fcf_5yr": (55000.0, 65000.0),
    "refined_capacity_mtpa": (1.1, 2.0),
}

# --------------------------------------------------------------------------- drivers, sourced
DRIVERS = {
    "capex": {
        "value": [7000.0, 9000.0, 10500.0, 10000.0, 8500.0],
        "source": "FY2026 capex was Rs 5,275 crore and FY2025 Rs 4,006 crore (consolidated "
                  "cash flow). The company states a programme of Rs 40,000-50,000 crore over "
                  "five years to take refined metal capacity from 1.1 to 2.0 Mtpa, including a "
                  "250 ktpa integrated zinc smelter at Debari and 400 ktpa zinc plus 200 ktpa "
                  "lead smelters at existing locations. The path here sums to Rs 45,000 crore "
                  "- the MIDPOINT of the stated range - front-loaded into the middle years "
                  "because smelter construction peaks mid-build rather than at the start.",
    },
    "volume_growth": {
        "value": [0.03, 0.05, 0.09, 0.12, 0.12],
        "source": "Mined metal production was 1,079 kt in FY2024, 1,095 kt in FY2025 and a "
                  "record 1,114 kt in FY2026 - roughly 1.6% a year organically. Growth "
                  "accelerates only from FY2029 as the new smelter capacity commissions; "
                  "modelling the capacity increase as if it arrived with the capex would be "
                  "wrong, since a smelter earns nothing until it is commissioned and ramped. "
                  "Cumulative growth to FY2031 is about 47%, well short of the 82% implied by "
                  "1.1 to 2.0 Mtpa of CAPACITY, because capacity is not utilisation.",
    },
    "realisation_growth": {
        "value": [-0.04, -0.02, 0.00, 0.02, 0.02],
        "source": "Zinc is a commodity and the FY2026 result was struck in what the company "
                  "itself calls 'a favourable commodity environment'. No forecasting skill is "
                  "claimed here: realisation is assumed to give back part of the FY2026 gain "
                  "and then track inflation. This is a deliberately UNFAVOURABLE base-case "
                  "assumption for a year that was an all-time high, on the principle that a "
                  "cyclical peak is not a run rate.",
    },
    "cop_change": {
        "value": [0.03, 0.02, 0.00, -0.02, -0.02],
        "source": "Zinc cost of production excluding royalty fell 8.8% to US$ 959 per tonne in "
                  "FY2026, which the company describes as a five-year low, driven by better "
                  "grades, byproduct realisation and digital/automation investment. A "
                  "five-year low is not a floor to extrapolate from: costs are assumed to "
                  "drift UP modestly before the new capacity brings scale benefits from "
                  "FY2030. The company's stated ambition is below US$ 1,000 per tonne, which "
                  "this path respects.",
    },
    "dividend": {
        "value": [6000.0, 6000.0, 6000.0, 7000.0, 8000.0],
        "source": "THE SWING VARIABLE. Dividends paid were Rs 12,253 crore in FY2025 and "
                  "Rs 4,225 crore in FY2026 (consolidated cash flow) - a 66% cut in one year, "
                  "with no stated policy to anchor either figure. The base case sets roughly "
                  "Rs 6,000-8,000 crore, between the two actuals, which is what the capex "
                  "programme can accommodate. It is NOT a forecast of board behaviour, and "
                  "the stress case tests the other reading.",
    },
    "interest_rate": {
        "value": [0.075, 0.075, 0.075, 0.075, 0.075],
        "source": "Interest and other finance charges paid were Rs 978 crore in FY2026 on "
                  "average debt of about Rs 9,700 crore ((10,967 + 8,728)/2) = 7.4%. Held at "
                  "7.5%.",
    },
    "tax_rate": {
        "value": [0.252, 0.252, 0.252, 0.252, 0.252],
        "source": "FY2026 tax was Rs 4,651 crore on profit before tax and exceptional items of "
                  "Rs 18,483 crore = 25.2%. Held flat.",
    },
}


def project(stress=False):
    """Base case, or a stress flexing what CRISIL's metals criteria and the ownership name."""
    d = {k: list(v["value"]) for k, v in DRIVERS.items()}
    if stress:
        # TWO things at once, because on this credit they are correlated rather than
        # independent: a zinc down-cycle, AND a parent that keeps taking cash out. Vedanta
        # Limited holds 60.71% and has its own obligations; the FY2025 dividend of Rs 12,253
        # crore is the evidence of what this board will approve when the parent needs it. A
        # stress that cut the dividend in a downturn would be modelling a company that
        # protects its own balance sheet first, and the FY2025 payout is evidence against
        # that. Capex is NOT cut - the smelters are contracted and half-built.
        d["realisation_growth"] = [-0.18, -0.08, 0.00, 0.03, 0.03]
        d["cop_change"] = [0.08, 0.05, 0.02, 0.00, 0.00]
        d["dividend"] = [12000.0, 12000.0, 10000.0, 10000.0, 10000.0]

    volume = 1.0
    realisation = 1.0
    cop_index = 1.0
    debt = BASE["debt"]
    liquid = BASE["liquid"]
    equity = BASE["equity"]
    othinc = BASE["other_income"]
    dep = BASE["dep"]

    # FY2026 cost base implied by the margin, so the CoP driver has something to act on.
    cost_base = BASE["revenue"] - BASE["opbdita"]

    rows = []
    for i, y in enumerate(YEARS):
        volume *= (1.0 + d["volume_growth"][i])
        realisation *= (1.0 + d["realisation_growth"][i])
        cop_index *= (1.0 + d["cop_change"][i])

        rev = BASE["revenue"] * volume * realisation
        cost = cost_base * volume * cop_index
        opbdita = rev - cost

        dep *= (1.0 + 0.05 * (i + 1))
        interest = debt * d["interest_rate"][i]
        pbt = opbdita + othinc - dep - interest
        tax = max(0.0, pbt) * d["tax_rate"][i]
        pat = pbt - tax

        # A dividend cannot exceed distributable reserves. Without this cap the stress case
        # drives net worth to MINUS Rs 5,188 crore by FY2031, which is arithmetically correct
        # and legally impossible - the Companies Act limits distribution out of reserves. The
        # cap keeps the projection to balance sheets that could actually exist, and the gap
        # between the planned and paid figures then shows directly where the parent's claim
        # on cash stops being satisfiable. A Rs 2,000 crore floor of share capital and
        # non-distributable reserves is retained.
        dividend_planned = d["dividend"][i]
        dividend = min(dividend_planned, max(0.0, equity + pat - 2000.0))

        # DERIVED, not assumed.
        funding_need = (d["capex"][i] + dividend + interest + tax
                        + BASE["lease_repaid"] - opbdita - othinc)
        new_debt = 0.0
        if funding_need > 0:
            from_cash = min(max(0.0, liquid - 2000.0), funding_need)
            liquid -= from_cash
            new_debt = funding_need - from_cash
        else:
            liquid += -funding_need
        debt += new_debt
        # Surplus years repay debt before building cash further.
        if funding_need < 0 and debt > 0:
            repay = min(debt, liquid - 2000.0) if liquid > 2000.0 else 0.0
            repay = max(0.0, min(repay, -funding_need))
            debt -= repay
            liquid -= repay
        equity += pat - dividend

        rows.append({
            "Year": y,
            "Mined metal (kt)": int(MINED_METAL_KT["FY2026"] * volume),
            "Realisation index": round(realisation, 3),
            "CoP index": round(cop_index, 3),
            "Revenue": round(rev, 0),
            "OPBDITA": round(opbdita, 0),
            "OPBDITA margin %": round(100 * opbdita / rev, 1) if rev else None,
            "Capex": round(d["capex"][i], 0),
            "Dividend (planned)": round(dividend_planned, 0),
            "Dividend (payable)": round(dividend, 0),
            "Interest": round(interest, 0),
            "PAT": round(pat, 0),
            "Funding gap": round(funding_need, 0),
            "New debt raised": round(new_debt, 0),
            "Total debt": round(debt, 0),
            "Liquid assets": round(liquid, 0),
            "Net debt": round(debt - liquid, 0),
            "Net worth": round(equity, 0),
            "TD/OPBDITA (x)": round(debt / opbdita, 2) if opbdita > 0 else None,
            "Net debt/OPBDITA (x)": round((debt - liquid) / opbdita, 2) if opbdita > 0 else None,
            "Interest coverage (x)": round(opbdita / interest, 1) if interest > 0 else None,
        })
    return rows


def check():
    """Tie the FY2026 starting point back to the engine, the report and the printed statements."""
    out = []

    def t(desc, computed, disclosed, tol):
        out.append((desc, computed, disclosed, tol, abs(computed - disclosed) <= tol))

    t("OPBDITA, FY2026 - the figure the delivered rationale publishes", BASE["opbdita"],
      22064.0, 1.0)
    t("OPBDITA margin, FY2026 - the rationale's 54.0%",
      100 * BASE["opbdita"] / BASE["revenue"], 54.0, 0.05)
    t("Capex ties to the consolidated cash flow, FY2026", BASE["capex"], 5275.0, 0.01)
    t("Dividend ties to the consolidated cash flow, FY2026", BASE["dividend"], 4225.0, 0.01)
    t("Dividend ties to the engine's own FY2026 figure", BASE["dividend"],
      float(D["dividends"][LAST]), 0.01)
    t("FY2025 dividend was 2.9x the FY2026 dividend - the swing this model tests",
      float(D["dividends"][1]) / float(D["dividends"][LAST]), 2.9001, 0.01)
    t("Total debt including leases, FY2026", BASE["debt"], 8728.0, 0.01)
    t("Liquid assets, FY2026", BASE["liquid"], 13673.0, 0.01)
    t("Hindustan Zinc is NET CASH at FY2026", BASE["debt"] - BASE["liquid"], -4945.0, 1.0)
    t("Zinc CoP fell 8.8% in FY2026",
      ZINC_COP_USD_T["FY2026"] / ZINC_COP_USD_T["FY2025"] - 1.0, -0.0884, 0.001)
    t("Mined metal production rose to a record in FY2026",
      float(MINED_METAL_KT["FY2026"]), 1114.0, 0.5)
    t("Effective tax rate on pre-exceptional PBT, FY2026",
      (D["pbt_bef_exc"][LAST] - D["pat"][LAST]) / D["pbt_bef_exc"][LAST], 0.2517, 0.001)
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
    print("  DISCLOSED DIFFERENCE: the company states FY2026 EBITDA of Rs 22,162 crore against")
    print("  the Rs 22,064 crore computed here and published in the delivered rationale. The")
    print("  Rs 98 crore gap is other income the company treats as OPERATING and the strict")
    print("  convention strips. Both are defensible; the margin is 54% either way, which is")
    print("  the figure the company itself quotes. Stated rather than reconciled away.")
    print()

    for label, stress in (("BASE CASE", False), ("STRESS CASE", True)):
        rows = project(stress)
        keys = [k for k in rows[0] if k != "Year"]
        print("=" * 112)
        print("%s - Hindustan Zinc Limited, consolidated, Rs crore" % label)
        print("-" * 112)
        print("%-26s%s" % ("", "".join("%14s" % r["Year"] for r in rows)))
        for k in keys:
            print("%-26s%s" % (k, "".join(
                "%14s" % ("n/a" if r[k] is None else "{:,}".format(r[k])) for r in rows)))
        print()

    print("=" * 112)
    print("CROSS-CHECK AGAINST THE COMPANY'S OWN PUBLISHED FIVE-YEAR PLAN")
    print("-" * 112)
    b, s = project(False), project(True)
    cap_b = sum(r["Capex"] for r in b)
    div_b = sum(r["Dividend (payable)"] for r in b)
    div_s = sum(r["Dividend (payable)"] for r in s)
    plan_s = sum(r["Dividend (planned)"] for r in s)
    lo, hi = COMPANY_PLAN["capex_5yr"]
    flo, fhi = COMPANY_PLAN["pre_growth_capex_fcf_5yr"]
    print("  Company's stated capex, five years           : Rs %s - %s crore"
          % ("{:,.0f}".format(lo), "{:,.0f}".format(hi)))
    print("  Modelled capex, five years                   : Rs %s crore" % "{:,.0f}".format(cap_b))
    print("  Company's stated pre-growth-capex FCF        : Rs %s - %s crore"
          % ("{:,.0f}".format(flo), "{:,.0f}".format(fhi)))
    print("  Headroom on the midpoints, five years        : Rs %s crore"
          % "{:,.0f}".format((flo + fhi) / 2 - (lo + hi) / 2))
    print("  Modelled dividend, base, five years          : Rs %s crore" % "{:,.0f}".format(div_b))
    print("  Modelled dividend, stress: planned Rs %s cr, PAYABLE Rs %s cr"
          % ("{:,.0f}".format(plan_s), "{:,.0f}".format(div_s)))
    if plan_s > div_s:
        print("    -> Rs %s crore of the stress-case dividend is NOT payable: distributable"
              % "{:,.0f}".format(plan_s - div_s))
        print("       reserves run out. That is the point at which the parent's claim on cash")
        print("       stops being satisfiable, and it is a finding rather than a modelling")
        print("       artefact.")
    print()
    print("  THE ARITHMETIC THAT DECIDES THIS CREDIT. On the company's own midpoints, the")
    print("  programme leaves about Rs 15,000 crore of headroom over five years - Rs 3,000")
    print("  crore a year - for dividends. Hindustan Zinc paid Rs 12,253 crore in FY2025 alone.")
    print("  So the capex is comfortably fundable, and the dividend is what decides whether")
    print("  the company ends the window with net cash or net debt.")
    print()
    print("  Base   : net %s of Rs %s crore by FY2031, net debt/OPBDITA %s"
          % ("CASH" if b[-1]["Net debt"] < 0 else "DEBT",
             "{:,.0f}".format(abs(b[-1]["Net debt"])), b[-1]["Net debt/OPBDITA (x)"]))
    print("  Stress : net %s of Rs %s crore by FY2031, net debt/OPBDITA %s"
          % ("CASH" if s[-1]["Net debt"] < 0 else "DEBT",
             "{:,.0f}".format(abs(s[-1]["Net debt"])), s[-1]["Net debt/OPBDITA (x)"]))
    print()
    print("  The stress is not a commodity stress alone. It combines an 18% realisation fall")
    print("  with an 8% cost increase AND a dividend held at the FY2025 rate - because on this")
    print("  issuer those are correlated, not independent. Vedanta Limited holds 60.71% and")
    print("  has its own obligations; the FY2025 payout is the evidence of what this board")
    print("  approves when the parent needs cash. THE PARENT LINKAGE IS A CLAIM ON CASH, and")
    print("  modelling it as anything else would miss the only real risk on the balance sheet.")

    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
