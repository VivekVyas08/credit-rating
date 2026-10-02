"""Step 12b - fill the native Rating_Scorecard template for Vodafone Idea Limited.

Historicals are read from compute_ratios.py (never retyped). Projections are COPIED, not
linked, from forward_model.py, which derives the debt path from the funding gap.

ONE NORMALISATION DECISION IS LOAD-BEARING AND IS STATED HERE RATHER THAN BURIED. The
scorecard's PAT cell feeds the PAT margin and gross cash accruals. Vodafone Idea's REPORTED
FY2026 consolidated PAT is +Rs 34,552 crore, produced entirely by a Rs 58,607 crore exceptional
credit from the derecognition of an AGR liability. Feeding that in would tell the scorecard the
company earned Rs 56,660 crore of gross cash accruals in a year it lost Rs 24,059 crore before
exceptional items. The NORMALISED figure - loss before exceptional items and tax, which equals
loss before tax here because the tax charge is nil - is used in all three years.
"""

import os
import shutil
import sys

from openpyxl import load_workbook

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402
import forward_model as F                                               # noqa: E402

SRC = "../../Rating_Scorecard.xlsx"
DST = "Rating_Scorecard_Vodafone Idea Limited.xlsx"
HIST = ["FY2024", "FY2025", "FY2026"]

# Cash paid towards PPE and intangible assets, consolidated cash-flow statement. Used rather
# than the Directors' Report capex figure because it is available on one consistent basis for
# all three years - and because the SERIES is the finding: Rs 1,614 crore in FY2024 against
# Rs 10,979 crore in FY2026. The company could not invest while the AGR overhang persisted.
CAPEX_CASHFLOW = {"FY2024": 1613.9, "FY2025": 10004.0, "FY2026": 10979.0}

# The company has not paid a dividend since FY2015-16 (Directors' Report, FY2025-26).
DIVIDEND = {"FY2024": 0.0, "FY2025": 0.0, "FY2026": 0.0}

QUALITATIVE = {
    "business": (4, "Third of three private operators, with 192.8 million subscribers across "
                    "all 22 service areas and 8,030.4 MHz of spectrum of which 8,012.8 MHz is "
                    "liberalised. Scored 4 rather than 3 because the subscriber base FELL from "
                    "198.2 million to 192.8 million over the five quarters to Q4 FY2026 and "
                    "VLR subscribers from 175.3 million to 169.3 million - the company is "
                    "losing share to two better-capitalised competitors. Not a 5, because "
                    "customer ARPU rose 8.3% to Rs 190, 4G/5G subscribers grew to 128.9 "
                    "million, and monthly additions turned positive from February 2026."),
    "management": (4, "The FY2026 audit opinion is UNMODIFIED and carries no material "
                      "uncertainty relating to going concern - the FY2025 report did carry "
                      "one, so this is a change, not a steady state. Held at 4 rather than 3 "
                      "because net worth remains negative at Rs (35,758) crore, the company "
                      "has not paid a dividend since FY2015-16, and the Rs 45,000 crore capex "
                      "programme depends on Rs 25,000 crore of term debt the annual report "
                      "states is still under discussion with lenders."),
    "support": (0, "ZERO NOTCHES ARE ENTERED HERE DELIBERATELY, and this is the single most "
                   "important input on the sheet. The scorecard applies a notch mechanically "
                   "to a standalone score; on this issuer the support is so large and so "
                   "structural that it cannot be represented that way without producing a "
                   "number that looks derived rather than judged. The support case is made in "
                   "full in the rating view and the workpaper instead. Entering 0 keeps the "
                   "ANCHOR honestly standalone, so the divergence between it and the rating "
                   "view is visible and has to be argued - which is what the anchor is for."),
    "liquidity": ("Adequate",
                  "Sources over twelve months: unencumbered cash and equivalents of Rs 2,106 "
                  "crore plus fixed deposits of 3-12 months of Rs 1,502 crore = Rs 3,608 "
                  "crore, the company's own stated basis; FY2026 net cash from operations of "
                  "Rs 19,411 crore; contracted CLAM inflow of Rs 2,307 crore over the next "
                  "twelve months; and an Aditya Birla Group equity commitment of Rs 4,730 "
                  "crore. Claims: bank repayment of Rs 726 crore, deferred payment obligation "
                  "instalments of Rs 7,076 crore as scheduled by March 2027, and spectrum "
                  "usage charges of Rs 124 crore. Note what is EXCLUDED: Rs 3,625 crore of "
                  "'bank balance other than cash', of which only Rs 1,502 crore is disclosed "
                  "as fixed deposits - the residual sits against Rs 7,534 crore of "
                  "non-fund-based facilities and is not shown to be unencumbered. Adequate "
                  "rather than Strong because the Rs 25,000 crore of term debt for the capex "
                  "programme is not committed; Adequate rather than Stretched because "
                  "operating cash flow covers the scheduled claims 2.5 times over."),
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

    ws["C4"] = "Vodafone Idea Limited"
    ws["C5"] = "ICRA"
    ws["C6"] = "Telecom"
    ws["C7"] = "01-Sep-2026"

    rows = {
        12: lambda y: R[y]["Operating income"],
        13: lambda y: R[y]["OPBDIT"],
        14: lambda y: C.CON["depreciation"][I[y]] + C.CON["amortisation"][I[y]],
        15: lambda y: C.CON["finance_cost"][I[y]],
        16: lambda y: C.CON["pbt_bef_exc"][I[y]],          # NORMALISED - see the module docstring
        17: lambda y: R[y]["Total debt"],
        18: lambda y: C.CON["cash"][I[y]] + C.CON["curr_inv"][I[y]],
        19: lambda y: R[y]["Tangible net worth"],
        20: lambda y: C.CON["total_assets"][I[y]] - C.CON["equity"][I[y]],
        21: lambda y: C.CON["curr_assets"][I[y]],
        22: lambda y: C.CON["curr_liab"][I[y]],
        23: lambda y: CAPEX_CASHFLOW[y],
        24: lambda y: DIVIDEND[y],
    }
    for r, fn in rows.items():
        for j, y in enumerate(HIST):
            ws.cell(row=r, column=3 + j, value=round(fn(y), 2))

    fy26_rev = R["FY2026"]["Operating income"]
    proj = {
        "revenue_growth": (round(base[0]["Operating income"] / fy26_rev - 1, 4),
                           round(base[1]["Operating income"] / base[0]["Operating income"] - 1, 4)),
        "ebitda_margin": (base[0]["OPBDIT margin %"] / 100.0, base[1]["OPBDIT margin %"] / 100.0),
        "capex": (base[0]["Capex"], base[1]["Capex"]),
        "net_new_debt": (base[0]["New debt raised"], base[1]["New debt raised"]),
        "interest_rate": (0.095, 0.095),
        # Nil - the company carries enormous unabsorbed losses and recognises no deferred tax
        # asset; the FY2026 tax charge was Rs 4 crore net on a consolidated basis.
        "tax_rate": (0.0, 0.0),
        "dividend_payout": (0.0, 0.0),
    }
    for r, key in [(29, "revenue_growth"), (30, "ebitda_margin"), (31, "capex"),
                   (32, "net_new_debt"), (33, "interest_rate"), (34, "tax_rate"),
                   (35, "dividend_payout")]:
        for j in range(2):
            ws.cell(row=r, column=3 + j, value=proj[key][j])

    ws["C39"] = None                                   # no override; Telecom sector base = 3
    ws["C40"] = QUALITATIVE["business"][0]
    ws["C41"] = QUALITATIVE["management"][0]
    ws["C42"] = QUALITATIVE["support"][0]
    ws["C43"] = QUALITATIVE["liquidity"][0]
    ws["C44"] = QUALITATIVE["outlook"][0]

    # ---------------------------------------------- hard caps STAY ON for this issuer (C67)
    # Unlike Godrej Properties - where the coverage cap fired on an accounting artefact - Vi's
    # capped metric is REAL. Net worth is negative by Rs 35,758 crore on the audited
    # consolidated balance sheet. The cap is doing exactly what it was written to do, and
    # disapplying it would be dishonest. The gap to the assigned rating is a SUPPORT case, and
    # it is argued in Stage 2 below where a reader can see and challenge it.
    ws["C67"] = "Y"
    ws["D67"] = ""

    # ------------------------------------------------------------- committee overlay (Stage 2)
    # This is where the support case now lives. The module docstring above records why the
    # Step 12b support notch was deliberately left at ZERO: a single notch cannot carry an
    # intervention of this scale without looking derived rather than judged. Stage 2 is the
    # right home for it - itemised, justified, and visible on the face of the workbook.
    # Anchor B- (index 15) - 9 notches = index 6 = A-.
    OVERLAY = {
        60: (0, "No sector-metric adjustment. The capped metric - negative net worth of "
                "Rs 35,758 crore - is REAL and audited, not an artefact of a sector accounting "
                "convention. The hard cap is left ON (Inputs!C67 = 'Y') precisely for that "
                "reason. Contrast Godrej Properties, where the capped metric was an artefact of "
                "project-completion accounting and the cap was properly disapplied."),
        61: (2, "+2 for franchise scale the financial composite cannot see. Vi operates in ALL "
                "22 service areas with 192.8 million subscribers and 8,030.4 MHz of spectrum, "
                "of which 8,012.8 MHz is liberalised - one of only three private national "
                "operators in a market with structural barriers to entry. The composite reads "
                "a loss-making P&L and a negative balance sheet; it cannot see a national "
                "spectrum and subscriber franchise that would take a decade and a licence "
                "regime to replicate."),
        62: (7, "+7 for GOVERNMENT SUPPORT - the dominant factor in this rating and the entire "
                "reason it is not a distressed grade. The Government of India holds ~49% of the "
                "equity following the AGR dues-to-equity conversion, making it the single "
                "largest shareholder. It has intervened THREE times in three years: the 2021 "
                "reform package moratorium, the 2023 conversion of interest dues to equity, and "
                "the FY2026 AGR reassessment. The company is systemically important as the "
                "third private operator in a market the Government has repeatedly stated it "
                "wants to keep from becoming a duopoly. Sized at +7 rather than higher because "
                "the support is demonstrated and repeated but NOT contractual - there is no "
                "guarantee, and each intervention has required a fresh policy decision."),
        63: (0, "No peer-benchmarking adjustment beyond the factors above."),
        64: (0, "None."),
    }
    for row, (notches, why) in OVERLAY.items():
        ws.cell(row=row, column=3, value=notches)
        ws.cell(row=row, column=4, value=why)

    wb.save(DST)
    print("wrote %s" % DST)
    print("\nHistoricals fed in (consolidated, Rs crore, PAT NORMALISED before exceptionals):")
    for y in HIST:
        print("  %-8s OI %9s  OPBDIT %8s  PAT(norm) %9s  Debt %9s  TNW %9s"
              % (y, "{:,.0f}".format(R[y]["Operating income"]),
                 "{:,.0f}".format(R[y]["OPBDIT"]),
                 "{:,.0f}".format(C.CON["pbt_bef_exc"][I[y]]),
                 "{:,.0f}".format(R[y]["Total debt"]),
                 "{:,.0f}".format(R[y]["Tangible net worth"])))
    print("\nProjections copied from forward_model.py (base case):")
    for k, v in proj.items():
        print("  %-18s %s" % (k, v))
    print("\nQualitative scores and their justification:")
    for k in ("business", "management", "support", "liquidity"):
        v, why = QUALITATIVE[k]
        print("\n  %s = %s\n    %s" % (k, v, why))


if __name__ == "__main__":
    main()
