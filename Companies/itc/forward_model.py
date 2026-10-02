"""ITC Limited - Step 12 forward view, FY2027 to FY2031.

WHAT THIS IS, AND WHAT IT IS NOT
-------------------------------
A five-year projection of the credit path, built in code off the verified FY2026 actuals in
compute_ratios.py. It is not the equity-research plugin's native 3-statement workbook; the
scaling decision and its reason are recorded in case.json.

THE ONE THING THIS MODEL EXISTS TO FLEX: THE FEBRUARY 2026 CIGARETTE TAX RESET, WHICH FY2026
ONLY PARTLY REFLECTS. In the company's own words (Q4 FY2026 press release): the GST rate went
"from 28% of transaction value to 40% of retail sale price along with a steep hike in excise
duties w.e.f 1st February, 2026 upon phasing out of Compensation Cess", producing "an
unprecedented increase in tax incidence on cigarettes". FY2026 therefore contains TWO MONTHS of
the new regime and ten of the old. FY2027 contains twelve.

The FY2026 accounts already show what that does, and the arithmetic is worth stating because
the headline hides it:

    Gross cigarette revenue   FY2025  35,893.57  ->  FY2026  40,601.00   +13.1%
    Excise                    FY2025   6,289.44  ->  FY2026  11,044.93   +75.6%
    NET of excise             FY2025  29,604.13  ->  FY2026  29,556.07    -0.2%

The entire gross growth in the cigarette segment was tax. Net revenue was FLAT. A model built
on gross revenue growth would have projected a healthy business.

WHY THE MODEL IS BUILT ON NET OPERATING INCOME AND NOT ON AN EXCISE FORECAST. It is tempting to
annualise the two months of new-regime excise into an FY2027 number. That would be false
precision: the annual report gives no month-wise split of the excise line, so any such split
would be invented, and the GST component does not pass through reported revenue at all (GST is
collected as agent and netted off, whereas excise is grossed up). The reset reaches ITC's P&L
through VOLUME and MIX - higher retail prices, and the growth in illicit trade the company
explicitly flags - not through a line that can be forecast arithmetically. So net operating
income is the primitive, and the stress case flexes it directly.

THE DEBT PATH IS DERIVED, NOT ASSUMED (failure mode 18) - though on this issuer that is close
to a formality, since ITC holds Rs 23,759.43 crore of liquid assets against Rs 2,399.06 crore
of debt including leases.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402

YEARS = ["FY2027", "FY2028", "FY2029", "FY2030", "FY2031"]
K = C.CONSOLIDATED
LAST = 1                                        # YEARS = ["FY2025", "FY2026"]

# Consolidated segment note 23B, FY2025-26 Report and Accounts (L13487), Rs crore.
CIG_GROSS = {"FY2025": 35893.57, "FY2026": 40601.00}

BASE = {
    "oi":       K["rev"][LAST] - K["excise"][LAST],
    "opbdit":   C.opbdit(K["pbt_bef"][LAST], K["fin"][LAST], K["dep"][LAST],
                         K["othinc"][LAST], K["jv"][LAST]),
    "othinc":   K["othinc"][LAST],
    "debt":     K["debt"][LAST],
    "liquid":   K["liquid"][LAST],
    "nw":       K["nw"][LAST],
    "tass":     K["tass"][LAST],
    "dep":      K["dep"][LAST],
    "fin":      K["fin"][LAST],
    "pat":      K["pat"][LAST],
    # Consolidated Statement of Cash Flows, FY2025-26 Report and Accounts (L11657, L11659):
    # purchase of PPE, intangibles and ROU 2,182.89; dividend paid 18,271.44;
    # net cash from operating activities 18,464.31.
    "capex":    2182.89,
    "dividend": 18271.44,
    "ocf":      18464.31,
}

# --------------------------------------------------------------------------- drivers, sourced
DRIVERS = {
    "oi_growth": {
        "value": [0.040, 0.070, 0.080, 0.080, 0.080],
        "source": "Net operating income grew 4.7% in FY2026 (75,323 to 78,868) while the "
                  "cigarette segment's NET revenue was flat at -0.2% - so the whole of FY2026's "
                  "growth came from the non-cigarette segments (Agri, Paperboards, FMCG-Others). "
                  "FY2027 is set at 4.0%, BELOW the FY2026 rate, because it is the first full "
                  "year of the new tax incidence and the cigarette segment is roughly 37% of "
                  "net operating income; the non-cigarette segments are assumed to keep "
                  "compounding. Recovery thereafter to 7-8% assumes prices are absorbed and "
                  "legal volumes stabilise - which is an assumption, and the one the stress "
                  "case reverses.",
    },
    "opbdit_margin": {
        "value": [0.338, 0.345, 0.350, 0.352, 0.352],
        "source": "OPBDIT/OI was 34.49% in FY2025 and 34.64% in FY2026 (computed; both "
                  "reproduce the figures published in all three delivered rationales). FY2027 "
                  "is set slightly BELOW FY2026 - a tax increase of this size is not fully "
                  "passed through in one year, and the company also reports that consumption "
                  "of high-cost leaf tobacco inventory weighed on margin. Recovery thereafter "
                  "is gradual and does not exceed the historical band by much.",
    },
    "capex": {
        "value": [2400.0, 2600.0, 2800.0, 2900.0, 3000.0],
        "source": "Consolidated capex was Rs 2,278.70 crore in FY2025 and Rs 2,182.89 crore in "
                  "FY2026 (purchase of PPE, intangibles and ROU assets). Stepped up modestly "
                  "in line with the FMCG-Others build-out; ITC is not a capital-intensive "
                  "business at group level - capex is about 12% of OPBDIT.",
    },
    "dividend_payout": {
        "value": [0.88, 0.88, 0.88, 0.88, 0.88],
        "source": "Dividend paid was Rs 17,782.22 crore in FY2025 and Rs 18,271.44 crore in "
                  "FY2026 (consolidated cash flow), against PAT to owners of Rs 19,730.62 "
                  "crore and Rs 20,689.47 crore - payouts of 90.1% and 88.3%. Held at 88%. "
                  "This is the single largest cash outflow in the model, an order of magnitude "
                  "above capex, and it is what keeps the balance sheet from accumulating cash "
                  "without limit.",
    },
    "other_income_growth": {
        "value": [0.02, 0.04, 0.05, 0.05, 0.05],
        "source": "Other income was Rs 2,529.69 crore in FY2025 and Rs 2,425.80 crore in "
                  "FY2026 - treasury return on a liquid portfolio of Rs 23,759.43 crore plus "
                  "dividends from associates and joint ventures. It grows with the portfolio, "
                  "which in turn depends on the payout ratio. Held to low single digits. "
                  "NOTE: this line is stripped from OPBDIT on the ICRA and CareEdge "
                  "conventions and is the point on which a CRISIL EBITDA would differ - see "
                  "fill_scorecard.py, which reports the sensitivity.",
    },
    "tax_rate": {
        "value": [0.279, 0.279, 0.279, 0.279, 0.279],
        "source": "FY2026 consolidated tax was Rs 8,012.70 crore on profit before tax "
                  "including the JV and associate share of Rs 28,702.17 crore = 27.92%. "
                  "Held flat.",
    },
}


def project(stress=False):
    """Base case, or a stress flexing the variable the tax reset actually threatens."""
    d = {k: list(v["value"]) for k, v in DRIVERS.items()}
    if stress:
        # The company's own stated risk, in its own words: the tax incidence drives "rapid
        # growth in illicit cigarette volumes", leaving "a large component of tobacco
        # consumption remaining outside the tax net". The stress is therefore a LEGAL VOLUME
        # stress - net operating income falls in the first two years as legal volumes migrate
        # to illicit trade and price increases fail to hold - with margin compressing because
        # the tax cannot be fully passed on. The dividend is NOT cut, which is deliberate:
        # ITC has paid out roughly 90% of earnings for years, and a stress case that quietly
        # assumes the board conserves cash would flatter the balance sheet on no evidence.
        d["oi_growth"] = [-0.040, -0.020, 0.020, 0.040, 0.050]
        d["opbdit_margin"] = [0.310, 0.305, 0.315, 0.320, 0.325]

    oi = BASE["oi"]
    debt = BASE["debt"]
    liquid = BASE["liquid"]
    nw = BASE["nw"]
    othinc = BASE["othinc"]
    dep = BASE["dep"]

    rows = []
    for i, y in enumerate(YEARS):
        oi *= (1.0 + d["oi_growth"][i])
        opbdit = oi * d["opbdit_margin"][i]
        othinc *= (1.0 + d["other_income_growth"][i])
        dep *= 1.04
        interest = debt * 0.05

        pbt = opbdit + othinc - dep - interest
        tax = max(0.0, pbt) * d["tax_rate"][i]
        pat = pbt - tax
        dividend = max(0.0, pat) * d["dividend_payout"][i]

        # DERIVED, not assumed. On this issuer the gap is met from the liquid portfolio
        # rather than by borrowing, which is itself the finding.
        funding_need = d["capex"][i] + dividend - (opbdit + othinc - interest - tax)
        new_debt = 0.0
        if funding_need > 0 and liquid - funding_need < 2000.0:
            new_debt = funding_need - max(0.0, liquid - 2000.0)
        liquid -= (funding_need - new_debt)
        debt = debt * 0.97 + new_debt          # existing debt amortises; leases roll
        nw += pat - dividend

        rows.append({
            "Year": y,
            "Operating income": round(oi, 0),
            "OPBDIT": round(opbdit, 0),
            "OPBDIT margin %": round(100 * d["opbdit_margin"][i], 2),
            "Other income": round(othinc, 0),
            "PAT": round(pat, 0),
            "Capex": round(d["capex"][i], 0),
            "Dividend": round(dividend, 0),
            "Funding gap": round(funding_need, 0),
            "New debt raised": round(new_debt, 0),
            "Total debt": round(debt, 0),
            "Liquid assets": round(liquid, 0),
            "Net debt": round(debt - liquid, 0),
            "Net worth": round(nw, 0),
            "Total debt/OPBDIT (x)": round(debt / opbdit, 3) if opbdit > 0 else None,
            "Interest coverage (x)": round(opbdit / interest, 0) if interest > 0 else None,
        })
    return rows


def check():
    """Tie the FY2026 starting point back to the engine, the reports and the printed notes."""
    out = []

    def t(desc, computed, disclosed, tol):
        out.append((desc, computed, disclosed, tol, abs(computed - disclosed) <= tol))

    t("Operating income net of excise, FY2026 - as published in all three rationales",
      BASE["oi"], 78868.40, 0.5)
    t("OPBDIT, FY2026 - the figure all three delivered reports state", BASE["opbdit"],
      27317.91, 1.0)
    t("OPBDIT/OI margin, FY2026", 100 * BASE["opbdit"] / BASE["oi"], 34.64, 0.05)
    t("Gross consolidated revenue ties to note 23B total, FY2026", K["rev"][LAST], 89913.33,
      0.01)
    t("Cigarette segment NET of excise was FLAT in FY2026",
      (CIG_GROSS["FY2026"] - K["excise"][LAST]) /
      (CIG_GROSS["FY2025"] - K["excise"][0]) - 1.0, -0.0016, 0.001)
    t("Cigarette segment GROSS grew 13.1% - the number the net figure corrects",
      CIG_GROSS["FY2026"] / CIG_GROSS["FY2025"] - 1.0, 0.1311, 0.001)
    t("Excise rose 75.6% on two months of the new regime",
      K["excise"][LAST] / K["excise"][0] - 1.0, 0.7561, 0.001)
    t("Capex ties to the consolidated cash flow, FY2026", BASE["capex"], 2182.89, 0.01)
    t("Dividend ties to the consolidated cash flow, FY2026", BASE["dividend"], 18271.44, 0.01)
    t("Dividend payout on PAT to owners, FY2026", BASE["dividend"] / BASE["pat"], 0.8831, 0.001)
    t("Effective tax rate incl. JV share, FY2026",
      (K["pbt_bef"][LAST] + K["jv"][LAST] - K["pat_total"][LAST])
      / (K["pbt_bef"][LAST] + K["jv"][LAST]), 0.2792, 0.001)
    t("Liquid assets vastly exceed debt, FY2026", BASE["liquid"] / BASE["debt"], 9.903, 0.01)
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    print("=" * 108)
    print("OPENING-BALANCE TIE-OUT (a forward model inherits every error in its starting point)")
    print("-" * 108)
    res = check()
    for desc, comp, disc, tol, ok in res:
        print("  %-66s %12.4f vs %12.4f  %s" % (desc[:66], comp, disc, "OK" if ok else "FAIL"))
    bad = [r for r in res if not r[4]]
    print("  %d of %d opening-balance checks reconcile" % (len(res) - len(bad), len(res)))
    print()

    for label, stress in (("BASE CASE", False), ("STRESS CASE", True)):
        rows = project(stress)
        keys = [k for k in rows[0] if k != "Year"]
        print("=" * 108)
        print("%s - ITC Limited, consolidated, Rs crore" % label)
        print("-" * 108)
        print("%-26s%s" % ("", "".join("%14s" % r["Year"] for r in rows)))
        for k in keys:
            print("%-26s%s" % (k, "".join(
                "%14s" % ("n/a" if r[k] is None else "{:,}".format(r[k])) for r in rows)))
        print()

    print("=" * 108)
    print("WHAT THE ARITHMETIC SAYS")
    print("-" * 108)
    b, s = project(False), project(True)
    print("  Base   : net CASH of Rs %s crore by FY2031; total debt Rs %s crore"
          % ("{:,.0f}".format(-b[-1]["Net debt"]), "{:,.0f}".format(b[-1]["Total debt"])))
    print("  Stress : net %s of Rs %s crore by FY2031; total debt Rs %s crore"
          % ("CASH" if s[-1]["Net debt"] < 0 else "DEBT",
             "{:,.0f}".format(abs(s[-1]["Net debt"])), "{:,.0f}".format(s[-1]["Total debt"])))
    print()
    print("  The credit conclusion does not move. ITC enters the window with Rs 23,759.43")
    print("  crore of liquid assets against Rs 2,399.06 crore of debt including leases -")
    print("  liquid assets are 9.9 times total debt - and generates Rs 18,464.31 crore of")
    print("  operating cash flow against Rs 2,182.89 crore of capex. Even in the stress, where")
    print("  legal volumes fall for two years and margin compresses more than 350 basis")
    print("  points, the company stays in a substantial net cash position while continuing to")
    print("  pay out 88% of earnings.")
    print()
    print("  THE EXPOSURE IS TO EARNINGS, NOT TO SOLVENCY, and the variable is legal cigarette")
    print("  VOLUME rather than the excise line. FY2026 carried two months of the new tax")
    print("  regime; FY2027 carries twelve. The company itself states the reset is driving")
    print("  'rapid growth in illicit cigarette volumes'. That is the monitorable, and it is")
    print("  a question about the size of the profit pool, not about whether the debt is paid.")

    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
