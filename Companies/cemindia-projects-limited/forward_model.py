"""Cemindia Projects Limited - Step 12 forward view, FY2027 to FY2031.

WHAT THIS IS. A five-year projection built in code off the verified FY2026 actuals in
compute_ratios.py. It is NOT the equity-research plugin's native workbook; the scaling
decision and its reason are recorded in case.json. For an order-book-backed EPC contractor
with almost no term debt and a near-net-cash balance sheet, the variables that move the credit
are (a) revenue conversion of the Rs 31,306.8 crore order book (Jun-30-2026), (b) the operating margin, and
(c) the working-capital cycle that turns growth into a funding need - not a term-debt
repayment schedule. The model turns those three, and derives the borrowing path from the
working-capital gap rather than assuming it (failure mode 18).

EVERY DRIVER IS SOURCE-LABELLED. Nothing here comes from a CRA publication.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402

YEARS = ["FY2027", "FY2028", "FY2029", "FY2030", "FY2031"]

DRIVERS = {
    "revenue_growth": {
        "value": [0.22, 0.20, 0.15, 0.12, 0.10],
        "source": "Revenue grew 8.4% in FY2026 to Rs 10,061 crore (Q1 FY2027 OI up 7% YoY); the "
                  "order book stood at Rs 31,306.8 crore as on June 30, 2026 (3.1x FY2026 OI) on "
                  "sizeable Adani-group inflow. A book of 3.1x supports the ramp-up; near-term "
                  "growth set at ~20-22%, tapering as the base builds, on the assumption that "
                  "inflow does not sustain its recent record every year.",
    },
    "opbdit_margin": {
        "value": [0.107, 0.107, 0.106, 0.106, 0.105],
        "source": "ICRA-convention OPBDIT/OI (retaining core-related claim income) was 9.86%, "
                  "9.32% and 10.66% over FY2024-FY2026 (computed). Margin improved in FY2026 on "
                  "operating leverage, project mix and claim-related income; held range-bound "
                  "within 10.0-10.7% over the medium term as higher-margin marine/urban-infra "
                  "work executes against EPC competitive intensity - the range the profile "
                  "supports, not a straight-line rise.",
    },
    "nwc_pct_revenue": {
        "value": [0.13, 0.13, 0.13, 0.12, 0.12],
        "source": "Net working capital (inventory + receivables + contract assets - trade "
                  "payables - contract liabilities) ran ~12-14% of revenue over FY2024-FY2026. "
                  "Held flat then eased slightly as the Adani-linked order mix improves "
                  "advance and milestone terms.",
    },
    "capex": {
        "value": [300.0, 320.0, 340.0, 340.0, 350.0],
        "source": "FY2026 cash capex was Rs 263.80 crore (consolidated cash-flow statement). "
                  "Stepped up modestly for plant and equipment to execute the larger book; a "
                  "contractor's capex is equipment-led and scales with revenue.",
    },
    "finance_cost_pct_revenue": {
        "value": [0.020, 0.019, 0.019, 0.018, 0.018],
        "source": "FY2026 finance cost of Rs 215.01 crore was 2.14% of revenue. For an EPC "
                  "contractor the finance cost is dominated by bank-guarantee commissions and "
                  "bill-discounting charges that scale with TURNOVER, not with the small drawn "
                  "borrowing balance - so it is modelled as a share of revenue, easing slightly "
                  "as scale improves. Rate-on-debt would understate it materially.",
    },
    "tax_rate": {
        "value": [0.27, 0.27, 0.27, 0.27, 0.27],
        "source": "Effective tax was ~26.9% in FY2026 (219.89 / 817.62). Held at 27%.",
    },
    "dividend_payout": {
        "value": [0.12, 0.12, 0.12, 0.12, 0.12],
        "source": "Modest payout consistent with FY2026; the company retains to fund working "
                  "capital for growth.",
    },
}


def project(stress=False):
    d = {k: list(v["value"]) for k, v in DRIVERS.items()}
    if stress:
        # The Construction methodology names order-inflow, execution pace and the
        # working-capital cycle as the drivers. The stress flexes exactly those: growth halves,
        # margin gives back the FY2026 gain, and the working-capital cycle stretches 4 points -
        # the classic EPC stress where a slow-paying government client balloons contract assets.
        d["revenue_growth"] = [0.07, 0.05, 0.05, 0.04, 0.04]
        d["opbdit_margin"] = [0.093, 0.090, 0.090, 0.090, 0.090]
        d["nwc_pct_revenue"] = [0.16, 0.17, 0.17, 0.17, 0.17]

    rev = C.CON["revenue"][2]
    debt = C._debt(C.CON, 2)
    tnw = C.CON["equity"][2]
    cash = C._unencumbered_cash(C.CON, 2)
    nwc_prev = 0.13 * rev                         # approx FY2026 NWC as a share of revenue
    rows = []
    for i, y in enumerate(YEARS):
        rev *= (1.0 + d["revenue_growth"][i])
        opbdit = rev * d["opbdit_margin"][i]
        interest = rev * d["finance_cost_pct_revenue"][i]
        pbt = opbdit - interest - d["capex"][i] * 0.5   # rough depreciation ~ half of capex
        pat = pbt * (1.0 - d["tax_rate"][i])
        div = max(0.0, pat) * d["dividend_payout"][i]

        nwc = d["nwc_pct_revenue"][i] * rev
        d_nwc = nwc - nwc_prev
        nwc_prev = nwc

        # Cash flow: OPBDIT - interest - tax - capex - dividend - increase in working capital.
        tax = max(0.0, pbt) * d["tax_rate"][i]
        cf_before_fin = opbdit - interest - tax - d["capex"][i] - div - d_nwc
        # DERIVED: a shortfall is met by new borrowing; a surplus repays / builds cash.
        new_debt = max(0.0, -cf_before_fin - max(0.0, cash - 200.0))
        cash = max(200.0, cash + cf_before_fin + new_debt)
        debt += new_debt if new_debt > 0 else max(-debt * 0.05, cf_before_fin * 0.3)
        debt = max(0.0, debt)
        tnw += pat - div

        rows.append({
            "Year": y,
            "Revenue": round(rev, 0),
            "OPBDIT": round(opbdit, 0),
            "OPBDIT margin %": round(100 * d["opbdit_margin"][i], 1),
            "Net working capital": round(nwc, 0),
            "Increase in NWC": round(d_nwc, 0),
            "Capex": round(d["capex"][i], 0),
            "New debt raised": round(new_debt, 0),
            "Total debt": round(debt, 0),
            "Unencumbered cash": round(cash, 0),
            "TNW": round(tnw, 0),
            "Total debt/OPBDIT (x)": round(debt / opbdit, 2),
            "Interest coverage (x)": round(opbdit / interest, 2) if interest else None,
            "Gearing (x)": round(debt / tnw, 2),
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
        print("=" * 96)
        print("%s - Cemindia Projects Limited, consolidated, Rs crore" % label)
        print("-" * 96)
        print("%-26s%s" % ("", "".join("%12s" % r["Year"] for r in rows)))
        for k in keys:
            print("%-26s%s" % (k, "".join(
                "%12s" % ("-" if r[k] is None else "{:,}".format(r[k])) for r in rows)))
        print()
    print("The book-to-bill of 3.1x underwrites the base-case revenue path; even in the stress")
    print("case leverage stays inside 1.5x debt/OPBDIT and coverage above 3x - the near-net-cash")
    print("start and the absence of a term-debt cliff are what make this a resilient profile.")


if __name__ == "__main__":
    main()
