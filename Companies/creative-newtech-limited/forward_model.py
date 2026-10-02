"""Creative Newtech Limited - Step 12 forward view, FY2027 to FY2031.

WHAT THIS IS, AND WHAT IT IS NOT
-------------------------------
A five-year projection of the credit path, built in code off the verified FY2026 actuals in
compute_ratios.py. It is not the equity-research plugin's native 3-statement workbook; the
scaling decision and its reason are recorded in case.json.

WHY THE MODEL IS SHAPED AROUND WORKING CAPITAL RATHER THAN CAPEX. This is a value-added
DISTRIBUTOR: purchases of stock-in-trade are 94.5% of revenue, and FY2026 capex was Rs 3.30
crore against an OPBDITA of Rs 91.11 crore - capex is a rounding error in the funding
arithmetic. What actually consumes cash here is the receivable and inventory build that
accompanies growth. In FY2026 revenue rose 52.1% and net working capital rose Rs 345.32 crore
(from Rs 208.13 crore to Rs 553.45 crore); debt rose Rs 252.5 crore and cash fell Rs 38.5
crore to fund it. A capex-centred model would have shown almost nothing happening.

THE DEBT PATH IS DERIVED, NOT ASSUMED (failure mode 18). Each year:
    external funding need = change in working capital + capex + dividend
                            - (OPBDITA - interest - tax)
and closing debt follows from it. Nothing is carried forward on the basis of "this issuer has
always borrowed about this much".

EVERY DRIVER IS SOURCE-LABELLED. Nothing here comes from a CRA publication.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402

YEARS = ["FY2027", "FY2028", "FY2029", "FY2030", "FY2031"]

# --------------------------------------------------------------------------- FY2026 actuals
# Every figure below is read from the engine, not retyped. The two balance-sheet lines the
# engine does not hold - trade payables and capex - are stated here with their source and are
# tied out in check() at the foot of this file.
LAKH = 100.0                                    # source unit is Rs lakh; converted ONCE here

BASE = {
    "revenue":     C.DATA["revenue"][2] + C.DATA["export_inc"][2],
    "receivables": C.DATA["receivables"][2],
    "inventory":   C.DATA["inventory"][2],
    # Trade payables = micro-and-small 3,021.95 + other creditors 15,489.48 lakh, consolidated
    # balance sheet, audited FY2026 results filing (OutcomeBM14052026-1.md L583-585).
    "payables":    (3021.95 + 15489.48) / LAKH,
    "debt":        C.DATA["borrow_nc"][2] + C.DATA["borrow_c"][2],
    "cash":        C.DATA["cash"][2] + C.DATA["bank_other"][2],
    "tnw":         C.DATA["equity_total"][2] - C.DATA["nci_equity"][2],
    # Purchase of PPE, intangibles and CWIP 330.04 lakh - consolidated cash flow, same filing.
    "capex":       330.04 / LAKH,
    # Dividend and DDT paid 75.08 lakh - consolidated cash flow, same filing. The Board has
    # recommended Re 0.50 per Rs 10 share for FY2026 (resolution 3), so the outflow continues.
    "dividend":    75.08 / LAKH,
    "depreciation": C.DATA["depreciation"][2],
}
# COGS is purchases of stock-in-trade PLUS the inventory movement - the same construction the
# engine uses for its gross-margin block. It is NOT backed out of EBITDA, which would fold
# employee and other operating expenses into cost of goods and overstate inventory days.
# Purchases 2,55,227.91 lakh, consolidated FY2026 (audited results filing; the same figure
# appears in the FY2026 column of the Q1 FY2027 filing, which is the cross-source check).
# Inventory build 66.09 crore, i.e. the "(increase) in inventories" line.
BASE["cogs"] = 255227.91 / LAKH - 66.09

# --------------------------------------------------------------------------- drivers, sourced
DRIVERS = {
    "revenue_growth": {
        "value": [0.20, 0.15, 0.12, 0.10, 0.10],
        "source": "Q1 FY2027 consolidated revenue was Rs 476.07 crore against Rs 392.96 crore "
                  "in Q1 FY2026, +21.2% year on year (unaudited consolidated results for the "
                  "quarter ended 30-Jun-2026, columns 30-Jun-26 and 30-Jun-25, Rs lakh). "
                  "FY2027 is set just below that print and tapers: the FY2026 growth of 52.1% "
                  "was driven by a step-change in the distribution book that cannot repeat "
                  "annually off a base 2.6 times larger, and the working capital it consumes "
                  "is itself the constraint on how fast the book can grow.",
    },
    "ebitda_margin": {
        "value": [0.036, 0.037, 0.038, 0.038, 0.038],
        "source": "OPBDITA margin was 3.04% in FY2025 and 3.37% in FY2026 (computed). Q1 FY2027 "
                  "prints materially higher at 5.09% (PBT 16.77 + finance 7.63 + depreciation "
                  "0.57 - other income 0.76, on revenue 476.07), against 3.05% in Q1 FY2026. "
                  "That is real year-on-year expansion, but ONE quarter in a business with "
                  "seasonal mix - so the base case takes only a modest step up from the FY2026 "
                  "actual and treats the Q1 print as upside evidence, not as the run rate. If "
                  "it holds, the credit metrics improve faster than modelled here.",
    },
    "receivable_days": {
        "value": [76, 76, 74, 72, 70],
        "source": "Receivable days went 49 -> 76 between FY2025 and FY2026 (computed), the "
                  "single largest adverse movement in the accounts: receivables grew 137.7% "
                  "against revenue growth of 52.1%. The base case assumes NO improvement in "
                  "FY2027-28 and only a slow unwind thereafter - an assumed reversion to the "
                  "FY2025 level would flatter the funding gap on no evidence.",
    },
    "inventory_days": {
        "value": [23, 23, 23, 23, 23],
        "source": "22 days FY2025, 23 days FY2026 (computed on COGS). Stable across both years "
                  "despite the revenue step-change, so held flat.",
    },
    "payable_days": {
        "value": [27, 27, 27, 27, 27],
        "source": "Trade payables Rs 185.11 crore on COGS of Rs 2,486.2 crore = 27 days FY2026, "
                  "against Rs 135.35 crore on Rs 1,625.8 crore = 30 days FY2025 (consolidated "
                  "balance sheets, audited FY2026 results filing). Held at the FY2026 level; "
                  "supplier credit has not lengthened to absorb the receivable stretch, which "
                  "is precisely why the gap fell on the balance sheet.",
    },
    "capex": {
        "value": [5.0, 5.0, 6.0, 6.0, 6.0],
        "source": "FY2026 purchase of PPE, intangibles and CWIP was Rs 3.30 crore and FY2025 "
                  "Rs 2.82 crore (consolidated cash flow). Stepped up modestly for the brand "
                  "licensing and contract-manufacturing arm the annual report describes, but "
                  "this remains an asset-light distributor and capex is not the funding driver.",
    },
    "interest_rate": {
        "value": [0.105, 0.105, 0.105, 0.105, 0.105],
        "source": "FY2026 finance cost Rs 20.66 crore on average debt of Rs 198.0 crore "
                  "((71.80 + 324.25)/2) = 10.4%. Held at 10.5%: the borrowing is almost "
                  "entirely short-term working-capital debt, which reprices.",
    },
    "tax_rate": {
        "value": [0.22, 0.22, 0.22, 0.22, 0.22],
        "source": "FY2026 tax was Rs 11.47 crore on PBT of Rs 81.76 crore, an effective 14.0%, "
                  "which is below the 25.17% concessional regime and not assumed to persist - "
                  "the FY2026 rate reflects period items the FY2026 notes are not available to "
                  "explain (no FY2025-26 annual report was uploaded). 22% is used as a "
                  "deliberately conservative middle, and is flagged as an assumption.",
    },
}


def project(stress=False):
    """Base case, or a stress flexing the variables CRISIL's trading-sector criteria name."""
    d = {k: list(v["value"]) for k, v in DRIVERS.items()}
    if stress:
        # CRISIL's criteria for the trading sector name total indebtedness, cash to
        # indebtedness, RISK COVERAGE (net worth against a loss on receivables and inventory)
        # and GCA days. The stress flexes exactly those: the receivable stretch continues
        # instead of unwinding, and thin distribution margins compress. Growth is NOT cut -
        # for a working-capital-funded distributor, growth is what consumes cash, so cutting
        # it would make the stress case look better on leverage. That is the trap.
        d["receivable_days"] = [88, 92, 92, 92, 92]
        d["ebitda_margin"] = [0.030, 0.028, 0.028, 0.028, 0.028]
        d["interest_rate"] = [0.115, 0.120, 0.120, 0.120, 0.120]

    rev = BASE["revenue"]
    cogs_ratio = BASE["cogs"] / BASE["revenue"]
    debt = BASE["debt"]
    cash = BASE["cash"]
    tnw = BASE["tnw"]
    wc_prev = BASE["receivables"] + BASE["inventory"] - BASE["payables"]

    rows = []
    for i, y in enumerate(YEARS):
        rev *= (1.0 + d["revenue_growth"][i])
        cogs = rev * cogs_ratio
        ebitda = rev * d["ebitda_margin"][i]

        recv = rev * d["receivable_days"][i] / 365.0
        inv = cogs * d["inventory_days"][i] / 365.0
        pay = cogs * d["payable_days"][i] / 365.0
        wc = recv + inv - pay
        delta_wc = wc - wc_prev

        interest = debt * d["interest_rate"][i]
        dep = BASE["depreciation"] * (1.0 + 0.10 * (i + 1))
        pbt = ebitda - dep - interest
        tax = max(0.0, pbt) * d["tax_rate"][i]
        pat = pbt - tax

        # DERIVED, not assumed. Only what the gap actually requires is raised, and cash is
        # drawn down to a Rs 5 crore floor first - the FY2026 closing position was already
        # only Rs 22.18 crore including other bank balances, so there is little to draw on.
        funding_need = delta_wc + d["capex"][i] + BASE["dividend"] - (ebitda - interest - tax)
        usable_cash = max(0.0, cash - 5.0)
        new_debt = max(0.0, funding_need - usable_cash)
        cash = max(5.0, cash - max(0.0, funding_need - new_debt))
        if funding_need < 0:                       # surplus repays debt before it builds cash
            repay = min(debt, -funding_need)
            debt -= repay
            cash += (-funding_need) - repay
        debt += new_debt

        tnw += pat - BASE["dividend"]
        wc_prev = wc

        rows.append({
            "Year": y,
            "Revenue": round(rev, 0),
            "OPBDITA": round(ebitda, 1),
            "OPBDITA margin %": round(100 * d["ebitda_margin"][i], 2),
            "Receivable days": d["receivable_days"][i],
            "Net working capital": round(wc, 0),
            "Change in WC": round(delta_wc, 0),
            "Capex": round(d["capex"][i], 1),
            "Interest": round(interest, 1),
            "PAT": round(pat, 1),
            "Funding gap": round(funding_need, 0),
            "New debt raised": round(new_debt, 0),
            "Total debt": round(debt, 0),
            "Tangible net worth": round(tnw, 0),
            "Total debt/OPBDITA (x)": round(debt / ebitda, 2) if ebitda > 0 else None,
            "Interest coverage (x)": round(ebitda / interest, 2) if interest > 0 else None,
            "Gearing (x)": round(debt / tnw, 2) if tnw > 0 else None,
        })
    return rows


def check():
    """Tie the FY2026 starting point back to the engine and to the printed balance sheet.

    A forward model inherits every error in its opening balances silently, so the opening
    balances are checked rather than assumed. Printed figures are stated in Rs lakh exactly as
    they appear in the filing and divided here, so a mutation of the literal is visible.
    """
    out = []

    def t(desc, computed, disclosed, tol):
        ok = abs(computed - disclosed) <= tol
        out.append((desc, computed, disclosed, tol, ok))

    t("Trade payables = micro/small + other creditors, FY2026",
      BASE["payables"], (3021.95 + 15489.48) / LAKH, 0.01)
    t("Total current liabilities tie to the printed total, FY2026",
      C.DATA["curr_liab"][2], 54838.06 / LAKH, 0.01)
    t("Current borrowings tie to the printed balance sheet, FY2026",
      C.DATA["borrow_c"][2], 32424.88 / LAKH, 0.01)
    t("Balance sheet totals, FY2026", C.DATA["total_assets"][2], 93723.64 / LAKH, 0.01)
    t("Payable days on COGS, FY2026", BASE["payables"] / BASE["cogs"] * 365.0, 27.0, 1.0)
    t("Opening net working capital vs the FY2026 balance sheet",
      BASE["receivables"] + BASE["inventory"] - BASE["payables"], 553.45, 0.5)
    t("Q1 FY2027 revenue growth used in the base case",
      (47607.02 / 39296.40 - 1.0), 0.2115, 0.001)
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
        print("  %-62s %12.2f vs %12.2f  %s" % (desc[:62], comp, disc, "OK" if ok else "FAIL"))
    bad = [r for r in res if not r[4]]
    print("  %d of %d opening-balance checks reconcile" % (len(res) - len(bad), len(res)))
    print()

    for label, stress in (("BASE CASE", False), ("STRESS CASE", True)):
        rows = project(stress)
        keys = [k for k in rows[0] if k != "Year"]
        print("=" * 104)
        print("%s - Creative Newtech Limited, consolidated, Rs crore" % label)
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
    print("  Base   : debt Rs %s cr by FY2031, TD/OPBDITA %.2fx, coverage %.2fx, gearing %.2fx"
          % ("{:,.0f}".format(b[-1]["Total debt"]), b[-1]["Total debt/OPBDITA (x)"],
             b[-1]["Interest coverage (x)"], b[-1]["Gearing (x)"]))
    print("  Stress : debt Rs %s cr by FY2031, TD/OPBDITA %.2fx, coverage %.2fx, gearing %.2fx"
          % ("{:,.0f}".format(s[-1]["Total debt"]), s[-1]["Total debt/OPBDITA (x)"],
             s[-1]["Interest coverage (x)"], s[-1]["Gearing (x)"]))
    print()
    print("  The base case turns self-funding in FY2029: at 12% growth the accruals cover the")
    print("  incremental working capital, the gap turns negative and debt starts repaying. The")
    print("  stress case is not a growth shock - growth is held UNCHANGED - it is a receivable")
    print("  and margin shock, and it is what actually breaks this credit. For a distributor")
    print("  funded on short-term working-capital lines, the danger is not that sales fall; it")
    print("  is that sales are made and not collected.")
    print()
    print("  The FY2026 receivable stretch from 49 to 76 days is therefore the central")
    print("  monitorable, and it is a named negative sensitivity in the rationale.")

    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
