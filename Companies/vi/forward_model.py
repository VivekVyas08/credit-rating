"""Vodafone Idea Limited - Step 12 forward view, FY2027 to FY2031.

WHAT THIS IS, AND WHAT IT IS NOT
-------------------------------
This is a five-year projection of the credit path, built in code off the verified FY2026
actuals in compute_ratios.py. It is NOT the equity-research plugin's native 3-statement
workbook. The scaling decision and its reason are recorded in case.json; in short, the three
things that decide this rating are the capex funding gap, the AGR repayment cliff in FY2036,
and whether promoter and Government support continues - and a full P&L/BS/CF template would
add presentation, not analysis, on top of the funding-gap arithmetic below.

THE DEBT PATH IS DERIVED, NOT ASSUMED (failure mode 18). Each year:
    external funding need = capex + interest paid + scheduled repayment - operating cash flow
and the closing debt follows from it. The company's own stated funding plan is used as the
cross-check, not as the input.

EVERY DRIVER IS SOURCE-LABELLED. Nothing here comes from a CRA publication.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402

YEARS = ["FY2027", "FY2028", "FY2029", "FY2030", "FY2031"]

# --------------------------------------------------------------------------- drivers, sourced
DRIVERS = {
    "arpu_growth": {
        "value": [0.08, 0.07, 0.06, 0.05, 0.05],
        "source": "Customer ARPU rose 8.3% year on year in Q4 FY2026 (Rs 190 from Rs 175) - "
                  "Q4 FY2026 results presentation. Held near that rate in FY2027 and tapered, "
                  "because the FY2026 gain came substantially from subscriber upgrades to "
                  "4G/5G rather than from headline tariff, and the upgrade pool shrinks as the "
                  "4G/5G share rises past two-thirds.",
    },
    "subscriber_growth": {
        "value": [-0.01, 0.00, 0.01, 0.01, 0.01],
        "source": "The base fell from 198.2 million to 192.8 million over the five quarters to "
                  "Q4 FY2026, but the company states monthly additions turned POSITIVE from "
                  "February 2026 (Q4 FY2026 presentation). One more year of mild decline is "
                  "assumed before stabilisation - the deceleration is evidenced, the turn is "
                  "not yet a trend.",
    },
    "ebitda_margin": {
        "value": [0.435, 0.445, 0.455, 0.460, 0.465],
        "source": "OPBDIT/OI was 40.15%, 41.60% and 42.35% over FY2024-FY2026 (computed), with "
                  "the quarterly margin reaching 43.1% in Q4 FY2026. Telecom carries high "
                  "operating leverage, so incremental ARPU drops through; the ramp is capped "
                  "below 47% because network opex rises with the 5G rollout.",
    },
    "capex": {
        "value": [15000.0, 15000.0, 15000.0, 9000.0, 9000.0],
        "source": "The company states a Rs 45,000 crore programme over FY2027-FY2029 "
                  "(Chairman's statement, FY2025-26 annual report) - taken at Rs 15,000 crore "
                  "a year - reverting thereafter towards the FY2026 actual of Rs 8,217 crore "
                  "consolidated plus bandwidth.",
    },
    "interest_rate": {
        "value": [0.095, 0.095, 0.095, 0.095, 0.095],
        "source": "Applied to the bank and market debt only. The deferred payment obligation "
                  "carries its own DoT-set discount unwind, modelled separately below.",
    },
    "dpo_repayment": {
        "value": [7076.0, 8000.0, 9000.0, 10000.0, 11000.0],
        "source": "FY2027 is the company's own stated figure - 'instalments payable, as "
                  "scheduled, by March 2027 is Rs 7,076 crore' (standalone note 5). Later "
                  "years step up as the spectrum moratorium fully unwinds. The AGR component "
                  "is separate and negligible until FY2036 (see AGR_SCHEDULE).",
    },
    "agr_payment": {
        "value": [124.0, 124.0, 124.0, 124.0, 124.0],
        "source": "Spectrum usage charges of Rs 609 crore in six annual instalments of Rs 124 "
                  "crore between March 2026 and March 2031 (standalone note 3). The AGR "
                  "principal itself is not payable until FY2032.",
    },
}

# The repayment profile the DoT set. This is why the FY2026 reassessment was a rating event and
# not an accounting one - and why the cliff sits outside the projection window entirely.
AGR_SCHEDULE = {
    "FY2032-FY2035": "minimum Rs 100 crore a year",
    "FY2036-FY2041": "Rs 10,608 crore a year, six instalments",
    "cumulative first 10 years": C.AGR_FIRST_10Y_CUMULATIVE,
    "total finalised": C.AGR["dues_finalised_by_committee"],
}


def project(stress=False):
    """Run the base case, or a stress case flexing the variables the methodology names."""
    d = {k: list(v["value"]) for k, v in DRIVERS.items()}
    if stress:
        # The Telecom Services methodology names ARPU movement, subscriber quality and capex
        # as the business drivers, and leverage/coverage as the financial ones. The stress
        # flexes exactly those: no ARPU growth beyond FY2027, continued subscriber decline,
        # margin held flat, and the full capex programme still spent - which is the realistic
        # bad case, since deferring the capex is what caused the subscriber loss to begin with.
        d["arpu_growth"] = [0.04, 0.01, 0.00, 0.00, 0.00]
        d["subscriber_growth"] = [-0.03, -0.03, -0.02, -0.02, -0.02]
        d["ebitda_margin"] = [0.425, 0.425, 0.425, 0.425, 0.425]

    rev = C.CON["revenue"][2]
    subs = C.OPS["Subscriber base (mn)"][4]
    bank_debt = C.CON["bank_lt"][2] + C.CON["bank_st"][2]
    dpo = C.CON["dpo_nc"][2] + C.CON["dpo_c"][2]
    lease = C.CON["lease_nc"][2] + C.CON["lease_c"][2]
    cash = C.COMPANY_STATED["consol_cash_and_equiv"] + C.COMPANY_STATED["consol_fd_3to12m"]

    rows = []
    for i, y in enumerate(YEARS):
        subs *= (1.0 + d["subscriber_growth"][i])
        rev *= (1.0 + d["arpu_growth"][i]) * (1.0 + d["subscriber_growth"][i])
        ebitda = rev * d["ebitda_margin"][i]

        interest_bank = bank_debt * d["interest_rate"][i]
        # The DPO unwinds at the DoT discount rate; approximated by the FY2026 effective rate
        # implied by the finance-cost line net of the bank and lease components.
        interest_dpo = dpo * 0.08
        interest_lease = lease * 0.09
        interest = interest_bank + interest_dpo + interest_lease

        repay = d["dpo_repayment"][i] + d["agr_payment"][i]
        lease_payment = lease * 0.16                       # roughly the FY2026 cash lease outflow

        # Cash available before financing. Tax is nil - unabsorbed losses (see the engine's
        # disclosed differences), so no tax line is modelled.
        ocf = ebitda - interest_bank - interest_lease - lease_payment
        funding_need = d["capex"][i] + repay - ocf

        # DERIVED, not assumed: the gap is met by new bank/market debt, and only what is
        # actually needed is raised.
        new_debt = max(0.0, funding_need - max(0.0, cash - 2000.0))
        cash = max(2000.0, cash - max(0.0, funding_need - new_debt))
        bank_debt += new_debt
        dpo = max(0.0, dpo - d["dpo_repayment"][i] + interest_dpo)
        lease = lease * 1.02

        total_debt = bank_debt + dpo + lease
        rows.append({
            "Year": y,
            "Subscribers (mn)": round(subs, 1),
            "Operating income": round(rev, 0),
            "OPBDIT": round(ebitda, 0),
            "OPBDIT margin %": round(100 * d["ebitda_margin"][i], 1),
            "Capex": round(d["capex"][i], 0),
            "Interest": round(interest, 0),
            "Scheduled repayment": round(repay, 0),
            "Funding gap": round(funding_need, 0),
            "New debt raised": round(new_debt, 0),
            "Bank and market debt": round(bank_debt, 0),
            "Total debt": round(total_debt, 0),
            "Total debt/OPBDIT (x)": round(total_debt / ebitda, 2),
            "Interest coverage (x)": round(ebitda / interest, 2),
        })
    return rows


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    for label, stress in (("BASE CASE", False), ("STRESS CASE", True)):
        rows = project(stress)
        keys = [k for k in rows[0] if k != "Year"]
        print("=" * 100)
        print("%s - Vodafone Idea Limited, consolidated, Rs crore" % label)
        print("-" * 100)
        print("%-30s%s" % ("", "".join("%12s" % r["Year"] for r in rows)))
        for k in keys:
            print("%-30s%s" % (k, "".join("%12s" % "{:,}".format(r[k]) for r in rows)))
        print()

    print("=" * 100)
    print("THE VARIABLE THE WINDOW DOES NOT REACH")
    print("-" * 100)
    for k, v in AGR_SCHEDULE.items():
        print("  %-28s %s" % (k, v))
    print("\n  The AGR principal of Rs 64,046 crore is almost entirely payable FY2036-FY2041,")
    print("  at Rs 10,608 crore a year. Cumulative payment in the first TEN years is Rs 1,144")
    print("  crore. That is the single largest fact about this credit: the obligation has not")
    print("  been forgiven, it has been moved beyond any reasonable forecasting horizon, and")
    print("  the company must build the earnings power to meet it in the meantime.")

    print("\n" + "=" * 100)
    print("CROSS-CHECK AGAINST THE COMPANY'S OWN STATED FUNDING PLAN")
    print("-" * 100)
    base = project(False)
    raised = sum(r["New debt raised"] for r in base[:3])
    print("  Model-derived new debt, FY2027-FY2029        : Rs %s crore" % "{:,.0f}".format(raised))
    print("  Company's stated capex programme, FY2027-29  : Rs 45,000 crore")
    print("  Company's stated cash and FDs at 31-Mar-2026 : Rs %s crore"
          % "{:,.0f}".format(C.COMPANY_STATED["consol_cash_and_equiv"]
                             + C.COMPANY_STATED["consol_fd_3to12m"]))
    print("  CLAM inflow contracted over next 12 months   : Rs 2,307 crore (standalone note,")
    print("                                                 FY2025-26 annual report)")
    print("  ABG equity commitment                        : Rs 4,730 crore (US$500 million)")
    print("\n  The gap between the derived funding need and the equity and CLAM inflows is what")
    print("  the company must raise as term debt. It has NOT yet been raised: the annual report")
    print("  states discussions with lenders are continuing. That is the central execution risk")
    print("  and it is a named monitorable, not an assumption.")


if __name__ == "__main__":
    main()
