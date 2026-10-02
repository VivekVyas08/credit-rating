"""Step 12b - fill the Rating_Scorecard template for ITC Limited, ONCE PER AGENCY.

This case is the reason the single-agency scorecard rule exists in a visible form: ITC was
rated by all three agencies out of one case folder - ICRA on 09-Jul-2026, CareEdge and CRISIL
on 11-Jul-2026 - so ONE workbook cannot serve. This script writes THREE, each carrying only
its own agency's scale, bands and operating-profit convention, which Step 12c then enforces.

THE CONVENTION QUESTION, ANSWERED HONESTLY RATHER THAN DECORATIVELY.
The three agencies define operating profit differently:
  * ICRA     OPBDIT  = PBT + finance cost + depreciation LESS other income, unconditionally.
  * CareEdge PBILDT  = total operating income less operating expenses; interest, dividend and
                       rental income are EXCLUDED from TOI even when recurring, and gross
                       sales are taken net of indirect taxes.
  * CRISIL   EBITDA  = PBDIT, which RETAINS recurring non-operating income rather than
                       stripping it.

On ITC those definitions have real money between them: other income is Rs 2,425.80 crore.
Stripped, operating profit is Rs 27,317.91 crore and the margin 34.64%; retained, it would be
Rs 29,743.71 crore and the margin 37.71% - a 307 basis point spread.

**All three workbooks are nevertheless fed Rs 27,317.91 crore, and that is deliberate.** All
three DELIVERED rationales state that figure: ICRA publishes OPBDIT/OI of 34.6%, CareEdge
publishes PBILDT of 27,318, and CRISIL publishes interest coverage of 321 times, which on
finance costs of Rs 85.17 crore implies 27,318 and not 29,744. A scorecard that contradicted
its own rationale would be precisely the defect failure mode 40 records. The CRISIL
sensitivity is therefore REPORTED here as a disclosed difference rather than silently applied
- and it is a narrow point in any case, since ITC's other income is treasury return on surplus
cash rather than income from operations, which is the reading under which CRISIL would strip
it too.

ONE FURTHER MECHANICAL POINT. The engine holds only FY2025 and FY2026. The template's three
year columns are C, D and E, and the scorecard's financial score and hard caps read COLUMN E
as the latest year. The two available years are therefore written to D and E - never to C and
D, which would silently feed the composite a year-old balance sheet.
"""

import os
import shutil
import sys

from openpyxl import load_workbook

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402
import forward_model as F                                               # noqa: E402

SRC = "../../Rating_Scorecard.xlsx"
HIST = ["FY2025", "FY2026"]
FIRST_COL = 4                       # column D - so FY2026 lands in column E, the latest slot

AGENCIES = [
    ("ICRA",     "Rating_Scorecard_ITC Limited_ICRA.xlsx",     "09-Jul-2026"),
    ("CRISIL",   "Rating_Scorecard_ITC Limited_CRISIL.xlsx",   "11-Jul-2026"),
    ("CareEdge", "Rating_Scorecard_ITC Limited_CareEdge.xlsx", "11-Jul-2026"),
]

# Consolidated Statement of Cash Flows, FY2025-26 Report and Accounts (L11657, L11659).
CAPEX_CASHFLOW = {"FY2025": 2278.70, "FY2026": 2182.89}
DIVIDEND = {"FY2025": 17782.22, "FY2026": 18271.44}

QUALITATIVE = {
    "business": (1, "The dominant position in Indian cigarettes - gross segment revenue of "
                    "Rs 40,601.00 crore in FY2026 - alongside genuinely material non-cigarette "
                    "businesses in Agri, Paperboards and Paper, and FMCG-Others, which between "
                    "them delivered ALL of FY2026's growth while cigarette net revenue was "
                    "flat. Scale, brand portfolio, distribution reach and backward integration "
                    "into leaf tobacco and agri sourcing are each best-in-class. Scored 1 "
                    "because the franchise is not seriously contestable on any horizon this "
                    "rating covers; the risk to it is regulatory and fiscal, not competitive, "
                    "and that risk is captured in the industry score rather than here."),
    "management": (1, "Unmodified audit opinion. The demerger of the hotels business was "
                      "executed and disclosed cleanly, with FY2024 comparatives flagged as "
                      "not like-for-like in the delivered rationales rather than quietly "
                      "restated. Capital allocation is explicit and consistent - roughly 88 "
                      "to 90% of earnings distributed, capex about 12% of OPBDIT, and no "
                      "recourse to borrowing. The company also disclosed the February 2026 "
                      "tax reset and its consequences, including the growth in illicit trade, "
                      "in plain terms rather than presenting the 13.1% gross cigarette revenue "
                      "growth without noting that net revenue was flat."),
    "support": (0, "Not applicable. ITC has no parent and needs no support; it is a net "
                   "creditor to the financial system with Rs 23,759.43 crore of liquid assets "
                   "against Rs 2,399.06 crore of debt including leases."),
    "liquidity": ("Superior",
                  "The descriptor is the CONCLUSION of the arithmetic, not an adjective. "
                  "Sources over twelve months: liquid assets of Rs 23,759.43 crore (cash and "
                  "equivalents Rs 20,750.64 crore, other bank balances Rs 643.46 crore, "
                  "current investments Rs 2,365.33 crore) and FY2026 net cash from operations "
                  "of Rs 18,464.31 crore. Claims: TOTAL debt of Rs 2,399.06 crore including "
                  "lease liabilities - not merely the current portion - capex the forward "
                  "model puts at Rs 2,400 crore, and a dividend of roughly Rs 18,000 crore. "
                  "Liquid assets alone cover total debt 9.9 times. Superior on any reading: "
                  "the only claim of any size is the dividend, which is discretionary, and "
                  "even in the stress case - legal cigarette volumes falling for two "
                  "consecutive years - the company remains in net cash of more than Rs 28,000 "
                  "crore while maintaining the payout."),
    "outlook": ("Stable", "See the rating view in the workpaper."),
}


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    K = C.CONSOLIDATED
    I = {y: i for i, y in enumerate(C.YEARS)}
    base = F.project(False)

    def oi(y):
        i = I[y]
        return K["rev"][i] - K["excise"][i]

    def opbdit(y):
        i = I[y]
        return C.opbdit(K["pbt_bef"][i], K["fin"][i], K["dep"][i], K["othinc"][i], K["jv"][i])

    rows = {
        12: oi,
        13: opbdit,
        14: lambda y: K["dep"][I[y]],
        15: lambda y: K["fin"][I[y]],
        16: lambda y: K["pat"][I[y]],                   # PAT to owners of the parent
        17: lambda y: K["debt"][I[y]],
        18: lambda y: K["liquid"][I[y]],
        19: lambda y: K["nw"][I[y]],
        20: lambda y: K["tass"][I[y]] - K["nw"][I[y]],
        # The engine carries no current-asset / current-liability split for ITC. Left EMPTY
        # rather than approximated.
        21: lambda y: None,
        22: lambda y: None,
        23: lambda y: CAPEX_CASHFLOW[y],
        24: lambda y: DIVIDEND[y],
    }

    fy26_oi = oi("FY2026")
    proj = {
        "revenue_growth": (round(base[0]["Operating income"] / fy26_oi - 1, 4),
                           round(base[1]["Operating income"] / base[0]["Operating income"] - 1,
                                 4)),
        "ebitda_margin": (base[0]["OPBDIT margin %"] / 100.0,
                          base[1]["OPBDIT margin %"] / 100.0),
        "capex": (base[0]["Capex"], base[1]["Capex"]),
        "net_new_debt": (base[0]["New debt raised"], base[1]["New debt raised"]),
        "interest_rate": (0.05, 0.05),
        "tax_rate": (0.279, 0.279),
        "dividend_payout": (0.88, 0.88),
    }

    written = []
    for agency, dst, rating_date in AGENCIES:
        shutil.copyfile(SRC, dst)
        wb = load_workbook(dst)
        ws = wb["Inputs"]

        ws["C4"] = "ITC Limited"
        ws["C5"] = agency
        ws["C6"] = "FMCG / Consumer staples"
        ws["C7"] = rating_date

        # Year headers, so a reader can see that column C is genuinely absent rather than
        # wondering whether a year was dropped.
        ws.cell(row=11, column=3, value="n/a")
        for j, y in enumerate(HIST):
            ws.cell(row=11, column=FIRST_COL + j, value=y)

        for r, fn in rows.items():
            ws.cell(row=r, column=3, value=None)             # column C stays empty
            for j, y in enumerate(HIST):
                v = fn(y)
                ws.cell(row=r, column=FIRST_COL + j,
                        value=None if v is None else round(v, 2))

        for r, key in [(29, "revenue_growth"), (30, "ebitda_margin"), (31, "capex"),
                       (32, "net_new_debt"), (33, "interest_rate"), (34, "tax_rate"),
                       (35, "dividend_payout")]:
            for j in range(2):
                ws.cell(row=r, column=3 + j, value=proj[key][j])

        ws["C39"] = None                     # no override; FMCG sector base = 2
        ws["C40"] = QUALITATIVE["business"][0]
        ws["C41"] = QUALITATIVE["management"][0]
        ws["C42"] = QUALITATIVE["support"][0]
        ws["C43"] = QUALITATIVE["liquidity"][0]
        ws["C44"] = QUALITATIVE["outlook"][0]

        wb.save(dst)
        written.append((agency, dst))
        print("wrote %s   (agency = %s)" % (dst, agency))

    print("\nHistoricals fed to ALL THREE workbooks (consolidated, Rs crore):")
    for y in HIST:
        print("  %-8s OI %9s  OPBDIT %9s  margin %5.2f%%  PAT %9s  Debt %8s  Liquid %9s"
              % (y, "{:,.0f}".format(oi(y)), "{:,.0f}".format(opbdit(y)),
                 100 * opbdit(y) / oi(y), "{:,.0f}".format(K["pat"][I[y]]),
                 "{:,.0f}".format(K["debt"][I[y]]), "{:,.0f}".format(K["liquid"][I[y]])))

    print("\nDISCLOSED CONVENTION DIFFERENCE (reported, not applied - see the module docstring):")
    o = K["othinc"][1]
    print("  Other income, FY2026 consolidated                    : Rs %9s crore"
          % "{:,.2f}".format(o))
    print("  Operating profit STRIPPING it (ICRA / CareEdge basis): Rs %9s crore, margin %.2f%%"
          % ("{:,.2f}".format(opbdit("FY2026")), 100 * opbdit("FY2026") / fy26_oi))
    print("  Operating profit RETAINING it (a strict CRISIL read) : Rs %9s crore, margin %.2f%%"
          % ("{:,.2f}".format(opbdit("FY2026") + o), 100 * (opbdit("FY2026") + o) / fy26_oi))
    print("  Spread                                               : %.0f basis points"
          % (10000.0 * o / fy26_oi))
    print("  All three DELIVERED rationales state the stripped figure - CRISIL's published")
    print("  interest coverage of 321x on finance costs of Rs 85.17 crore implies 27,318, not")
    print("  29,744 - so the stripped figure is fed to all three and the difference is")
    print("  disclosed here rather than silently applied.")

    print("\nProjections copied from forward_model.py (base case, FY2027 / FY2028):")
    for k, v in proj.items():
        print("  %-18s %s" % (k, v))
    print("\nQualitative scores and their justification:")
    for k in ("business", "management", "support", "liquidity"):
        v, why = QUALITATIVE[k]
        print("\n  %s = %s\n    %s" % (k, v, why))


if __name__ == "__main__":
    main()
