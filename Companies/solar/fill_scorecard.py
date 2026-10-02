"""Step 12b - fill the native Rating_Scorecard template for Solar Industries India Limited.

Historicals from compute_ratios.py; projections copied (never linked) from forward_model.py.
Stage 1 (anchor) only is filled here; Stage 2/3 are set at Step 17c by the committee.

No hard-cap disapplication is needed: interest coverage is 19.6x (FY2026) and net worth is
strongly positive. Business risk is a STRENGTH (explosives market leadership, defence ramp,
order book, scale), so the business-risk gate (failure mode 53) does not bind - it is checked.
"""

import os
import shutil
import sys

from openpyxl import load_workbook

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402
import forward_model as F                                               # noqa: E402

SRC = "../../Rating_Scorecard.xlsx"
DST = "Rating_Scorecard_Solar Industries India Limited.xlsx"
HIST = ["FY2024", "FY2025", "FY2026"]

# Cash capex (purchase of PPE/intangibles) - company-disclosed ~Rs 1,556 cr FY2026; FY2024/25
# from the cash-flow investing block are approximated by the gross-block change and left None
# where not cleanly extracted (used only as a scorecard input, not a ratio).
CAPEX = {"FY2024": None, "FY2025": None, "FY2026": 1556.0}
DIVIDEND = {"FY2024": None, "FY2025": None, "FY2026": 145.0}   # ~20% payout, financing block

QUALITATIVE = {
    "business": (2, "Market leader in industrial explosives and initiating systems in India with "
                    "a fast-scaling defence business (revenue nearly doubled to Rs 2,634 crore, "
                    "+94% in FY2026), a ~Rs 21,300 crore order book, presence in 40+ countries "
                    "and 90+ manufacturing facilities, and consolidated revenue of Rs 9,838 "
                    "crore (+30.5%). Scored 2 for scale, diversification (mining/infra/defence, "
                    "domestic and export) and market position; not 1 because the base explosives "
                    "business is exposed to demand cyclicality, input-cost volatility and "
                    "competition, and the defence order book is at an early ramp."),
    "management": (2, "Long-established promoter-managed group (promoter holding 95.11%) with a "
                      "professional senior team, an UNMODIFIED audit opinion on both standalone "
                      "and consolidated FY2026 statements (joint auditors Gandhi Rathi & Co and "
                      "S R B C & Co LLP), a consistent dividend record and disciplined capital "
                      "allocation. Held at 2 given the concentrated promoter holding and the "
                      "execution demands of a large simultaneous capex and defence build-out."),
    "support": (0, "NOT APPLICABLE as a support notch. Solar is a promoter-owned listed group "
                   "with no rated parent whose credit could be notched onto it, and no external "
                   "guarantee or cash-support undertaking. The rating rests on the standalone/"
                   "consolidated profile; no parent/group uplift or drag applies (failure mode "
                   "56 checked - there is no weaker parent to drag it)."),
    "liquidity": ("Strong",
                  "Cash, bank balances and current investments of Rs 584.14 crore as on "
                  "March 31, 2026, FY2026 operating cash generation well in excess of the "
                  "Rs 133.97 crore interest bill (coverage 19.6x), and modest debt of "
                  "Rs 1,524.02 crore (gearing 0.24x, TD/OPBDIT 0.58x) against strong internal "
                  "accruals that fully fund the capex programme in the base case (no new debt "
                  "drawn over FY2027-FY2031). Strong rather than Superior because a sizeable "
                  "multi-year capex and defence build-out consumes much of the free cash flow "
                  "and working capital is expanding with the defence ramp."),
    "outlook": ("Stable", "See the rating view in the workpaper."),
}


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    shutil.copyfile(SRC, DST)
    wb = load_workbook(DST)
    ws = wb["Inputs"]
    R = C.compute()
    I = {y: i for i, y in enumerate(C.YEARS)}
    base = F.project(False)

    ws["C4"] = "Solar Industries India Limited"
    ws["C5"] = "ICRA"
    ws["C6"] = "Chemicals / Agrochemicals"   # nearest of the 22 scorecard sectors to explosives
    ws["C7"] = "22-Sep-2026"

    rows = {
        12: lambda y: R[y]["Operating income"],
        13: lambda y: R[y]["OPBDIT"],
        14: lambda y: C.CON["depreciation"][I[y]],
        15: lambda y: C.CON["finance_cost"][I[y]],
        16: lambda y: C.CON["pat"][I[y]],
        17: lambda y: R[y]["Total debt"],
        18: lambda y: C._liquid(C.CON, I[y]),
        19: lambda y: R[y]["Tangible net worth (owners)"],
        20: lambda y: C.CON["total_liab"][I[y]],
        21: lambda y: C.CON["curr_assets"][I[y]],
        22: lambda y: C.CON["curr_liab"][I[y]],
        23: lambda y: CAPEX[y],
        24: lambda y: DIVIDEND[y],
    }
    for r, fn in rows.items():
        for j, y in enumerate(HIST):
            v = fn(y)
            if v is not None:
                ws.cell(row=r, column=3 + j, value=round(v, 2))

    fy26_rev = R["FY2026"]["Operating income"]
    proj = {
        "revenue_growth": (round(base[0]["Revenue"] / fy26_rev - 1, 4),
                           round(base[1]["Revenue"] / base[0]["Revenue"] - 1, 4)),
        "ebitda_margin": (base[0]["OPBDIT margin %"] / 100.0, base[1]["OPBDIT margin %"] / 100.0),
        "capex": (base[0]["Capex"], base[1]["Capex"]),
        "net_new_debt": (base[0]["New debt raised"], base[1]["New debt raised"]),
        "interest_rate": (0.085, 0.085),
        "tax_rate": (0.265, 0.265),
        "dividend_payout": (0.20, 0.20),
    }
    for r, key in [(29, "revenue_growth"), (30, "ebitda_margin"), (31, "capex"),
                   (32, "net_new_debt"), (33, "interest_rate"), (34, "tax_rate"),
                   (35, "dividend_payout")]:
        for j in range(2):
            ws.cell(row=r, column=3 + j, value=proj[key][j])

    ws["C39"] = None
    ws["C40"] = QUALITATIVE["business"][0]
    ws["C41"] = QUALITATIVE["management"][0]
    ws["C42"] = QUALITATIVE["support"][0]
    ws["C43"] = QUALITATIVE["liquidity"][0]
    ws["C44"] = QUALITATIVE["outlook"][0]

    wb.save(DST)
    print("wrote %s" % DST)
    for y in HIST:
        print("  %-8s OI %9s  OPBDIT %8s  PAT %8s  Debt %8s  TNW %8s" % (
            y, "{:,.0f}".format(R[y]["Operating income"]), "{:,.0f}".format(R[y]["OPBDIT"]),
            "{:,.0f}".format(R[y]["PAT (incl NCI)"]), "{:,.0f}".format(R[y]["Total debt"]),
            "{:,.0f}".format(R[y]["Tangible net worth (owners)"])))
    for k in ("business", "management", "support", "liquidity"):
        print("  %-11s %s" % (k, QUALITATIVE[k][0]))


if __name__ == "__main__":
    main()
