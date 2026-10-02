"""Step 12b - fill the native Rating_Scorecard template for HINDUSTAN ZINC LIMITED (CRISIL).

ENTITY NOTE (binding): the case folder is labelled "Vedanta". The rated entity, and every
figure here, is HINDUSTAN ZINC LIMITED - a separate listed company in which Vedanta Limited
holds 60.71% and the Government of India 27.92%. The workbook is named for the rated entity.

Historicals are read from compute_ratios.py (never retyped). Projections are COPIED, not
linked, from forward_model.py, which derives the debt path from the funding gap.

TWO DECISIONS ARE LOAD-BEARING AND ARE STATED HERE RATHER THAN BURIED.

1. THE PARENT LINKAGE IS ENTERED AS ZERO NOTCHES, AND ON THIS ISSUER THAT IS NOT THE NEUTRAL
   READING - IT IS THE FAVOURABLE ONE. The scorecard's support cell exists to notch a
   subsidiary UP towards a stronger parent. Hindustan Zinc's parent is not stronger: Vedanta
   Limited is a leveraged holding company whose call on this balance sheet runs through the
   DIVIDEND, and the evidence of that call is Rs 12,253 crore paid in FY2025 against
   Rs 4,225 crore in FY2026. The honest entry would be a negative notch. Zero is used because
   the drag is already modelled where it actually bites - in the forward model's stress case,
   which holds the dividend at the FY2025 rate and turns a Rs 25,704 crore net cash position
   into Rs 34,506 crore of net debt. Recording it twice would double-count it.

2. OPERATIONAL BUYERS' AND SUPPLIERS' CREDIT IS EXCLUDED FROM DEBT. The engine carries it
   separately and reports both ways (Rs 105 crore at FY2026, down from Rs 569 crore). It is
   trade financing on operational purchases, and at 1.2% of debt it changes nothing here - but
   the toggle is named rather than silently chosen.
"""

import os
import shutil
import sys

from openpyxl import load_workbook

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402
import forward_model as F                                               # noqa: E402

SRC = "../../Rating_Scorecard.xlsx"
DST = "Rating_Scorecard_Hindustan Zinc Limited.xlsx"
HIST = ["FY2024", "FY2025", "FY2026"]

# Consolidated cash-flow statement, FY2025-26 integrated report. FY2024 was not extracted -
# left None, not estimated.
CAPEX_CASHFLOW = {"FY2024": None, "FY2025": 4006.0, "FY2026": 5275.0}

QUALITATIVE = {
    "business": (2, "The world's largest integrated zinc producer and the dominant Indian "
                    "primary zinc supplier, with 13.9 Mnt of metal reserves and 50 Mnt of "
                    "resources - decades of mine life - and a zinc cost of production "
                    "excluding royalty of US$ 959 per tonne in FY2026, a five-year low and a "
                    "genuine first-quartile global position. Mined metal production reached a "
                    "record 1,114 kt. Scored 2 rather than 1 for one reason: this is a "
                    "SINGLE-COMMODITY business. Revenue, margin and cash flow all move with "
                    "the zinc price, and the FY2026 result was struck in what the company "
                    "itself calls a favourable commodity environment. Cost leadership "
                    "determines who survives a down-cycle; it does not exempt anyone from it."),
    "management": (3, "Scored 3, and the reason is specific rather than atmospheric. The "
                      "FY2026 consolidated audit report carries an EMPHASIS OF MATTER drawing "
                      "attention to Note 43, 'regarding allegations made during the year by a "
                      "short seller, and ongoing matters for which information has been sought "
                      "by regulators/authorities'. That is an unresolved governance overhang "
                      "at the reporting date and it cannot be scored as though it were absent. "
                      "Operationally the record is strong - record production, a five-year-low "
                      "cost of production, and a published five-year capital plan with both "
                      "sides of the funding equation disclosed. Not a 4, because the opinion "
                      "itself is unmodified and the disclosure is full. Not a 2, because a "
                      "dividend that swung from Rs 12,253 crore to Rs 4,225 crore in one year "
                      "with no stated distribution policy is a capital-allocation question, "
                      "and the majority shareholder's own needs are visible in it."),
    "support": (0, "Zero - see the module docstring. This is the FAVOURABLE entry, not the "
                   "neutral one: the 60.71% parent is a claim on this balance sheet rather "
                   "than a source of support, and the drag is modelled in the forward model's "
                   "stress case instead of being notched here."),
    "liquidity": ("Superior",
                  "The descriptor is the CONCLUSION of the arithmetic, not an adjective. "
                  "Sources over twelve months: liquid assets of Rs 13,673 crore (cash Rs 297 "
                  "crore, other bank balances Rs 22 crore, current investments Rs 13,354 "
                  "crore - the company parks surplus in liquid funds, so excluding them would "
                  "materially misstate the position) and FY2026 net cash from operations of "
                  "Rs 17,008 crore. Claims: TOTAL debt of Rs 8,728 crore including leases - "
                  "the whole book, not the current portion - current maturities within that "
                  "of Rs 3,822 crore, capex the forward model puts at Rs 7,000 crore for "
                  "FY2027, and a dividend of Rs 4,225 crore at the FY2026 rate. Hindustan "
                  "Zinc is NET CASH of Rs 4,945 crore; operating cash flow alone covers total "
                  "debt 1.9 times in a single year. Superior rather than Strong because even "
                  "the full FY2027 claim set - capex, dividend, interest, tax and all current "
                  "maturities - is covered by operating cash flow and liquid assets with room "
                  "to spare. The qualification worth naming: this is Superior standalone "
                  "liquidity attached to a company whose majority shareholder can call on it, "
                  "which is why the dividend is the monitorable rather than the debt."),
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
    D = C.DATA
    I = {y: i for i, y in enumerate(C.YEARS)}
    base = F.project(False)

    ws["C4"] = "Hindustan Zinc Limited"
    ws["C5"] = "CRISIL"
    ws["C6"] = "Iron & Steel / Metals / Mining"
    ws["C7"] = "13-Aug-2026"

    def opbdita(y):
        i = I[y]
        return (D["pbt_bef_exc"][i] + D["finance_cost"][i] + D["depreciation"][i]
                - D["other_income"][i])

    rows = {
        12: lambda y: D["revenue"][I[y]],
        13: opbdita,
        14: lambda y: D["depreciation"][I[y]],
        15: lambda y: D["finance_cost"][I[y]],
        16: lambda y: D["pat"][I[y]],
        # Buyers'/suppliers' credit EXCLUDED - see the module docstring.
        17: lambda y: (D["borrow_nc"][I[y]] + D["borrow_c"][I[y]]
                       + D["lease_nc"][I[y]] + D["lease_c"][I[y]]),
        18: lambda y: D["cash"][I[y]] + D["bank_other"][I[y]] + D["cur_invest"][I[y]],
        19: lambda y: D["equity"][I[y]],
        20: lambda y: D["total_assets"][I[y]] - D["equity"][I[y]],
        21: lambda y: D["curr_assets"][I[y]],
        22: lambda y: D["curr_liab"][I[y]],
        23: lambda y: CAPEX_CASHFLOW[y],
        24: lambda y: D["dividends"][I[y]],
    }
    for r, fn in rows.items():
        for j, y in enumerate(HIST):
            v = fn(y)
            ws.cell(row=r, column=3 + j, value=None if v is None else round(float(v), 2))

    fy26 = D["revenue"][2]
    proj = {
        "revenue_growth": (round(base[0]["Revenue"] / fy26 - 1, 4),
                           round(base[1]["Revenue"] / base[0]["Revenue"] - 1, 4)),
        "ebitda_margin": (base[0]["OPBDITA margin %"] / 100.0,
                          base[1]["OPBDITA margin %"] / 100.0),
        "capex": (base[0]["Capex"], base[1]["Capex"]),
        "net_new_debt": (base[0]["New debt raised"], base[1]["New debt raised"]),
        "interest_rate": (0.075, 0.075),
        "tax_rate": (0.252, 0.252),
        "dividend_payout": (round(base[0]["Dividend (payable)"] / base[0]["PAT"], 4),
                            round(base[1]["Dividend (payable)"] / base[1]["PAT"], 4)),
    }
    for r, key in [(29, "revenue_growth"), (30, "ebitda_margin"), (31, "capex"),
                   (32, "net_new_debt"), (33, "interest_rate"), (34, "tax_rate"),
                   (35, "dividend_payout")]:
        for j in range(2):
            ws.cell(row=r, column=3 + j, value=proj[key][j])

    ws["C39"] = None                # no override; Metals & Mining sector base = 4
    ws["C40"] = QUALITATIVE["business"][0]
    ws["C41"] = QUALITATIVE["management"][0]
    ws["C42"] = QUALITATIVE["support"][0]
    ws["C43"] = QUALITATIVE["liquidity"][0]
    ws["C44"] = QUALITATIVE["outlook"][0]

    wb.save(DST)
    print("wrote %s" % DST)
    print("\nHistoricals fed in (consolidated, Rs crore; debt incl. leases, excl. buyers' credit):")
    for y in HIST:
        cap = CAPEX_CASHFLOW[y]
        div = D["dividends"][I[y]]
        print("  %-8s Rev %8s  OPBDITA %8s (%.1f%%)  PAT %8s  Debt %7s  Liquid %8s  Capex %7s  Div %8s"
              % (y, "{:,.0f}".format(rows[12](y)), "{:,.0f}".format(opbdita(y)),
                 100 * opbdita(y) / rows[12](y), "{:,.0f}".format(rows[16](y)),
                 "{:,.0f}".format(rows[17](y)), "{:,.0f}".format(rows[18](y)),
                 "n/a" if cap is None else "{:,.0f}".format(cap),
                 "n/a" if div is None else "{:,.0f}".format(div)))
    print("\n  Sector-defining metrics (failure mode 21):")
    for y in HIST:
        cop = F.ZINC_COP_USD_T.get(y)
        print("    %-8s mined metal %s kt   zinc CoP ex royalty %s"
              % (y, "{:,}".format(F.MINED_METAL_KT[y]),
                 "US$ %s/t" % cop if cop else "not disclosed in the documents for this year"))
    print("\nProjections copied from forward_model.py (base case, FY2027 / FY2028):")
    for k, v in proj.items():
        print("  %-18s %s" % (k, v))
    print("\nQualitative scores and their justification:")
    for k in ("business", "management", "support", "liquidity"):
        v, why = QUALITATIVE[k]
        print("\n  %s = %s\n    %s" % (k, v, why))


if __name__ == "__main__":
    main()
