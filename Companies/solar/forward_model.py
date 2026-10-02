"""Solar Industries India Limited - Step 12 forward view, FY2027 to FY2031.

A focused five-year projection off the verified FY2026 actuals in compute_ratios.py. For a
diversified explosives + defence manufacturer with a ~Rs 21,300 crore order book, low leverage
and strong coverage, the variables that move the credit are (a) revenue conversion of the order
book and the defence ramp, (b) the operating margin, and (c) the capex-driven funding need -
the borrowing path is DERIVED from capex less internal accrual (failure mode 18), not assumed.
Every driver is source-labelled; nothing here comes from a CRA publication.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402

YEARS = ["FY2027", "FY2028", "FY2029", "FY2030", "FY2031"]

DRIVERS = {
    "revenue_growth": {
        "value": [0.22, 0.20, 0.18, 0.15, 0.13],
        "source": "Revenue grew 30.5% in FY2026 to Rs 9,837.74 crore; the order book stood at "
                  "~Rs 21,300 crore (about 2.2x FY2026 revenue) and defence revenue nearly "
                  "doubled to Rs 2,634 crore (+94%). Growth tapered from the low-20s as the "
                  "base builds, on the assumption the defence ramp and order-book execution "
                  "sustain but do not repeat the FY2026 step every year.",
    },
    "opbdit_margin": {
        "value": [0.265, 0.265, 0.270, 0.270, 0.270],
        "source": "ICRA-convention OPBDIT/OI was 22.6%, 26.1% and 26.7% over FY2024-FY2026 "
                  "(computed). Held around 26.5-27% as the higher-margin defence mix builds "
                  "against input-cost and competitive pressure in the base explosives business.",
    },
    "capex": {
        "value": [1600.0, 1500.0, 1400.0, 1300.0, 1200.0],
        "source": "FY2026 capex was ~Rs 1,556 crore (company disclosure; gross block Rs 5,479 "
                  "crore). A sizeable multi-year capex programme for explosives capacity and "
                  "defence facilities; stepped down gradually as the current cycle completes.",
    },
    "finance_cost_pct_debt": {
        "value": [0.085, 0.085, 0.085, 0.085, 0.085],
        "source": "FY2026 finance cost of Rs 133.97 crore on ~Rs 1,524 crore of debt is ~8.8%; "
                  "held at 8.5% on the drawn balance.",
    },
    "tax_rate": {
        "value": [0.265, 0.265, 0.265, 0.265, 0.265],
        "source": "Effective tax ~26.6% in FY2026 (628.58 / 2365.22). Held at 26.5%.",
    },
    "dividend_payout": {
        "value": [0.20, 0.20, 0.20, 0.20, 0.20],
        "source": "Consistent modest payout; the company retains to fund capex and the defence "
                  "expansion.",
    },
}


def project(stress=False):
    d = {k: list(v["value"]) for k, v in DRIVERS.items()}
    if stress:
        # The Chemicals methodology names demand cyclicality, input-cost volatility and capex
        # execution as the drivers. The stress flexes exactly those: growth halves, margin gives
        # back the FY2026 gain, capex holds (committed) - the classic manufacturer stress where a
        # demand slowdown meets a committed capex programme.
        d["revenue_growth"] = [0.10, 0.06, 0.06, 0.05, 0.05]
        d["opbdit_margin"] = [0.235, 0.225, 0.225, 0.225, 0.225]

    rev = C.CON["revenue"][2]
    debt = C._debt(C.CON, 2)
    tnw = C._tnw(C.CON, 2)
    cash = C._liquid(C.CON, 2)
    rows = []
    for i, y in enumerate(YEARS):
        rev *= (1.0 + d["revenue_growth"][i])
        opbdit = rev * d["opbdit_margin"][i]
        interest = debt * d["finance_cost_pct_debt"][i]
        dep = C.CON["depreciation"][2] * (1.0 + 0.10 * (i + 1))   # depreciation grows with capex
        pbt = opbdit - interest - dep
        tax = max(0.0, pbt) * d["tax_rate"][i]
        pat = pbt - tax
        div = max(0.0, pat) * d["dividend_payout"][i]

        # Funding gap: capex - (PAT + depreciation - dividend) = external funding need.
        internal = pat + dep - div
        gap = d["capex"][i] - internal
        new_debt = max(0.0, gap)
        if gap < 0:                                   # surplus repays debt / builds cash
            repay = min(debt * 0.15, -gap * 0.5)
            debt = max(0.0, debt - repay)
            cash += (-gap) - repay
        else:
            debt += new_debt
        tnw += pat - div

        rows.append({
            "Year": y,
            "Revenue": round(rev, 0),
            "OPBDIT": round(opbdit, 0),
            "OPBDIT margin %": round(100 * d["opbdit_margin"][i], 1),
            "Capex": round(d["capex"][i], 0),
            "New debt raised": round(new_debt, 0),
            "Total debt": round(debt, 0),
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
        print("=" * 92)
        print("%s - Solar Industries India Limited, consolidated, Rs crore" % label)
        print("-" * 92)
        print("%-24s%s" % ("", "".join("%12s" % r["Year"] for r in rows)))
        for k in keys:
            print("%-24s%s" % (k, "".join(
                "%12s" % ("-" if r[k] is None else "{:,}".format(r[k])) for r in rows)))
        print()
    print("Even in the stress case leverage stays well inside 1x debt/OPBDIT and coverage above")
    print("10x - the low starting leverage, strong margins and the order-book/defence pipeline")
    print("are what make this a resilient, high-investment-grade profile.")


if __name__ == "__main__":
    main()
