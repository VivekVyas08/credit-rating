"""Step 12b - fill the native Rating_Scorecard template for Indus Towers Limited (CRISIL).

Historicals are read from compute_ratios.py (never retyped). Projections are COPIED, not
linked, from forward_model.py, which builds revenue from co-locations x revenue per
co-location and derives the funding path from it.

TWO DECISIONS ARE LOAD-BEARING AND ARE STATED HERE RATHER THAN BURIED.

1. EARNINGS ARE FED IN NORMALISED, NOT REPORTED. Reported EBITDA carries net WRITE-BACKS of
   allowances for doubtful receivables - Rs 5,077.1 crore in FY2025 and Rs 256.0 crore in
   FY2026 - sitting inside other expenses. They are the Vodafone Idea recovery. Feeding the
   reported series in would tell the scorecard that FY2026 EBITDA FELL 12.9% when underlying
   EBITDA GREW 12.9%, and would hand it an FY2025 margin of 70.3% that the business never
   earned. PAT is normalised on the same basis, net of tax at the effective rate.

2. TOTAL DEBT INCLUDES LEASE LIABILITIES, WHICH ON THIS ISSUER MEANS THE SCORECARD IS ALMOST
   ENTIRELY MEASURING GROUND LEASES. At FY2026, borrowings were Rs 920.9 crore and lease
   liabilities Rs 20,206.0 crore - leases are 95.6% of adjusted debt. That is the correct
   CRISIL convention and it is not adjusted away here. But it means the gearing and
   debt/EBITDA cells describe a contractual, revenue-matched obligation rather than borrowed
   money, and the anchor should be read with that in mind. The workpaper note records both
   bases.
"""

import os
import shutil
import sys

from openpyxl import load_workbook

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compute_ratios as C                                              # noqa: E402
import forward_model as F                                               # noqa: E402

SRC = "../../Rating_Scorecard.xlsx"
DST = "Rating_Scorecard_Indus Towers Limited.xlsx"
HIST = ["FY2024", "FY2025", "FY2026"]
MN = C.MN

# Consolidated cash-flow statements, in Rs million as reported.
#   FY2026 and FY2025: FY2026 integrated report (L15346).
#   FY2024: FY2023-24 annual report (L12752).
CAPEX_CASHFLOW = {"FY2024": 89529.0 / MN, "FY2025": 67840.0 / MN, "FY2026": 86258.0 / MN}
# No dividend was paid in any of the three years. FY2025 returned Rs 2,640.0 crore to
# shareholders by BUYBACK instead (payment for buyback of equity shares, 26,400 million).
# The buyback is entered in the dividend row because the row's analytical purpose is
# discretionary shareholder distribution, and recording nil for a year in which Rs 2,640
# crore left the company would misstate the cash available for debt service.
DIVIDEND = {"FY2024": 0.0, "FY2025": 26400.0 / MN, "FY2026": 0.0}

QUALITATIVE = {
    "business": (2, "The largest telecom tower company in India: 264,514 macro towers and "
                    "428,014 co-locations across 22 circles at FY2026, plus 14,044 lean "
                    "co-locations, on master service agreements of long tenure. Scale, "
                    "national footprint and contracted revenue are all top-decile. Scored 2 "
                    "rather than 1 for two evidenced reasons. First, CUSTOMER CONCENTRATION "
                    "is structural and irreducible - Indian telecom has three private "
                    "operators and one state-owned, and Bharti Airtel is both the largest "
                    "customer and a promoter. Second, the TENANCY RATIO, which is the metric "
                    "this sector lives by, has fallen in each of the last two years: 1.677, "
                    "then 1.626, then 1.618, because towers were added faster than tenants "
                    "were found for them. A snapshot would read 'industry-leading 1.6x'; the "
                    "series reads as dilution."),
    "management": (2, "Unmodified audit opinion. The specific test this management passes is "
                      "the one that matters on this credit: the Vodafone Idea receivable. "
                      "Provisions taken against it have been WRITTEN BACK across FY2025 and "
                      "FY2026 as dues were cleared, receivable days compressed from 82 to 58 "
                      "to 55, and the company disclosed the write-backs transparently inside "
                      "other expenses rather than presenting them as operating improvement. "
                      "Capital discipline is evidenced too - borrowings reduced from Rs "
                      "4,311.8 crore to Rs 920.9 crore over two years while spending more than "
                      "Rs 8,000 crore a year on capex and returning Rs 2,640 crore by buyback. "
                      "Scored 2 rather than 1 because there is no stated distribution policy: "
                      "three years produced a buyback, nothing, and nothing."),
    "support": (0, "ZERO NOTCHES, DELIBERATELY, and the reason is a finding rather than an "
                   "omission. Bharti Airtel is a promoter and the largest customer, so a "
                   "support notch is arguable. It is not applied, because the evidence points "
                   "the other way: the standalone profile has strengthened to the point where "
                   "support is not what carries the rating. Borrowings are down 79% in two "
                   "years, normalised EBITDA grew 12.9%, and the receivable that was the "
                   "central weakness has been recovered rather than provided against. A "
                   "subsidiary outgrowing its support notch is an upgrade signal, not a "
                   "neutral fact (failure mode 22). Entering zero keeps the anchor standalone "
                   "and makes that argument visible instead of absorbing it into a notch."),
    "liquidity": ("Superior",
                  "The descriptor is the CONCLUSION of the arithmetic, not an adjective. "
                  "Sources over twelve months: normalised OPBDITA of Rs 18,196.6 crore, cash "
                  "and equivalents of Rs 47.3 crore, other bank balances of Rs 1,505.0 crore "
                  "and current investments of Rs 4,305.2 crore - Rs 5,857.5 crore of liquid "
                  "resources. Claims: total borrowings of Rs 920.9 crore (the WHOLE book, not "
                  "just the current portion), lease principal repayments of about Rs 2,639 "
                  "crore, and interest of roughly Rs 1,796 crore. Liquid resources alone cover "
                  "all borrowings 6.4 times; operating profit covers borrowings, lease "
                  "principal and interest together 3.3 times. Superior rather than Strong "
                  "because the forward model shows the funding gap NEGATIVE in every year of "
                  "both the base and the stress case - the company does not need external "
                  "funding even while spending Rs 8,000 crore a year of capex and even if "
                  "tenancy falls to 1.37x."),
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
    D = C.D
    I = {y: i for i, y in enumerate(C.YEARS)}
    base = F.project(False)

    ws["C4"] = "Indus Towers Limited"
    ws["C5"] = "CRISIL"
    ws["C6"] = "Telecom"
    ws["C7"] = "13-Aug-2026"

    def ebitda_norm(y):
        i = I[y]
        return (D["ebitda_rep"][i] + D["writeback"][i]) / MN

    def pat_norm(y):
        """Reported PAT less the write-back, net of tax at the year's effective rate.

        The write-back is a pre-tax credit sitting in other expenses, so removing it from PAT
        requires removing only its after-tax share - otherwise FY2025 normalised PAT would be
        understated by the tax that was never paid on it.
        """
        i = I[y]
        eff = (D["pbt_rep"][i] - D["pat_rep"][i]) / D["pbt_rep"][i]
        return (D["pat_rep"][i] + D["writeback"][i] * (1.0 - eff)) / MN

    rows = {
        12: lambda y: D["revenue"][I[y]] / MN,
        13: ebitda_norm,
        14: lambda y: D["dep"][I[y]] / MN,
        15: lambda y: D["fin_cost"][I[y]] / MN,
        16: pat_norm,
        17: lambda y: (D["borrowings"][I[y]] + D["leases"][I[y]]) / MN,
        18: lambda y: (D["cash"][I[y]] + D["bank_other"][I[y]] + D["cur_invest"][I[y]]) / MN,
        19: lambda y: D["equity"][I[y]] / MN,
        20: lambda y: (D["total_assets"][I[y]] - D["equity"][I[y]]) / MN,
        # The engine does not carry a current-asset / current-liability split for this issuer.
        # Left EMPTY rather than approximated - the current ratio is not a meaningful metric
        # for a tower company in any case, since its receivables are the whole question and
        # its liabilities are overwhelmingly long-dated ground leases.
        21: lambda y: None,
        22: lambda y: None,
        23: lambda y: CAPEX_CASHFLOW[y],
        24: lambda y: DIVIDEND[y],
    }
    for r, fn in rows.items():
        for j, y in enumerate(HIST):
            v = fn(y)
            ws.cell(row=r, column=3 + j, value=None if v is None else round(v, 2))

    fy26_rev = D["revenue"][2] / MN
    proj = {
        "revenue_growth": (round(base[0]["Revenue"] / fy26_rev - 1, 4),
                           round(base[1]["Revenue"] / base[0]["Revenue"] - 1, 4)),
        "ebitda_margin": (base[0]["OPBDITA margin %"] / 100.0,
                          base[1]["OPBDITA margin %"] / 100.0),
        "capex": (base[0]["Capex"], base[1]["Capex"]),
        "net_new_debt": (base[0]["New borrowing raised"], base[1]["New borrowing raised"]),
        "interest_rate": (0.085, 0.085),
        "tax_rate": (0.256, 0.256),
        # No distribution is assumed. The company paid no dividend in any of the three
        # historical years and returned capital once, by buyback. Assuming a payout would be
        # an invention; see the forward model's closing note.
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

    wb.save(DST)
    print("wrote %s" % DST)
    print("\nHistoricals fed in (consolidated, Rs crore, EBITDA and PAT NORMALISED):")
    for y in HIST:
        print("  %-8s Rev %9s  OPBDITA %9s (rep %9s)  PAT %8s (rep %8s)  Debt %9s"
              % (y, "{:,.0f}".format(rows[12](y)), "{:,.0f}".format(ebitda_norm(y)),
                 "{:,.0f}".format(C.D["ebitda_rep"][I[y]] / MN),
                 "{:,.0f}".format(pat_norm(y)),
                 "{:,.0f}".format(C.D["pat_rep"][I[y]] / MN),
                 "{:,.0f}".format(rows[17](y))))
    print("\n  Tenancy ratio series (the sector's defining metric):")
    for y in HIST:
        print("    %-8s %7s towers  %7s co-locations  tenancy %.3f"
              % (y, "{:,}".format(F.TOWERS[y]), "{:,}".format(F.COLOCATIONS[y]),
                 F.COLOCATIONS[y] / F.TOWERS[y]))
    print("\nProjections copied from forward_model.py (base case, FY2027 / FY2028):")
    for k, v in proj.items():
        print("  %-18s %s" % (k, v))
    print("\nQualitative scores and their justification:")
    for k in ("business", "management", "support", "liquidity"):
        v, why = QUALITATIVE[k]
        print("\n  %s = %s\n    %s" % (k, v, why))


if __name__ == "__main__":
    main()
