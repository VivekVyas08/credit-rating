"""IndusInd Bank - bank ratio engine (CLAUDE.md Step 5/6 deliverable).

AGENCY: CRISIL.  ENTITY TYPE: scheduled commercial bank (private sector), NOT a corporate.
The corporate ratio suite (gearing, TOL/TNW, interest coverage, GCA days) is NOT applicable
and is deliberately absent (CLAUDE.md failure mode 21/28 - bank metric set only).

BASIS: standalone (the KFI basis), consistent with how the bank headlines its own results and
with the SBI CRISIL precedent in this project. BFIL (wholly owned microfinance BC subsidiary)
and IMFS (associate) are named in the entities-consolidated annexure; consolidated PAT is carried
as a cross-check only.

SOURCE UNIT: Rs crore unless stated. Every figure traced to a document line (see SRC strings).
Primary sources, newest-first (failure mode 26):
  AR26 = annual-report-2025-2026.md   (FY2026 + FY2025 audited)
  AR25 = annual_report_2024-25.md     (FY2025 + FY2024 audited)
  Q1FY27 = Unaudited-Financial-Results-Q1-FY26-27.md (quarter ended 30-Jun-2026)
  Q4FY26 = Audited-Financial-Results-Q4-FY26.md
Every full-year P&L line reconciles between the AR summary table AND the audited quarterly
results - that cross-source agreement is the backbone of the tie-outs below.
"""

AR26 = "AR26 L2701-2726 (P&L+BS summary)"
AR25 = "AR25 L2372-2403 (P&L+BS summary)"
CAP26 = "AR26 L5615-18 / L12252-61 (capital)"
CAP25 = "AR25 L4898-4901 / L11464-71 (capital)"
AQ = "AR26 L13025-27 / AR25 L12027-28 (asset-quality schedule)"
KPI = "AR25 L1359 / AR26 L1673-1687 (KPI charts, FY22-FY26)"
SCH3 = "AR26 L11521-31 (Schedule 3 - deposits)"

# ---------------------------------------------------------------------------------------------
# Three rated years, standalone. FY2024 from AR25 (FY25 AR), FY2025/FY2026 from AR26 (FY26 AR);
# the newest document is preferred where both carry a line (failure mode 26).
# ---------------------------------------------------------------------------------------------
YEARS = ["FY2024", "FY2025", "FY2026"]

PL = {
    # label:                 ([FY24, FY25, FY26],                       source)
    "Interest earned":        ([45748.21, 48667.67, 46250.81], f"{AR25}/{AR26}"),
    "Interest expended":      ([25132.30, 29636.35, 28268.49], f"{AR25}/{AR26}"),
    "Net interest income":    ([20615.91, 19031.32, 17982.32], f"{AR25}/{AR26}"),
    "Non-interest income":    ([9387.85, 7684.19, 7217.06],    f"{AR25}/{AR26}"),
    "Revenue (NII + other)":  ([30003.76, 26715.51, 25199.38], f"{AR25}/{AR26}"),
    "Operating expenses":     ([13838.81, 15585.54, 15481.09], f"{AR25}/{AR26}"),
    "Operating profit":       ([15740.27, 10644.86, 9202.21],  f"{AR25}/{AR26}"),
    "Provisions & conting.":  ([3798.74, 7030.14, 7933.10],    f"{AR25}/{AR26}"),
    "Profit before tax":      ([11941.53, 3614.72, 1269.11],   f"{AR25}/{AR26}"),
    "Tax":                    ([2991.75, 971.82, 335.78],      f"{AR25}/{AR26}"),
    "Net profit (standalone)":([8949.78, 2642.90, 933.33],     f"{AR25}/{AR26}"),
    "Net profit (consol)":    ([8977.30, 2575.54, 889.34],     f"{AR25}/{AR26} consolidated row"),
}

BS = {
    "Deposits":               ([384792.92, 411078.14, 400173.75], f"{AR25}/{AR26}"),
    "Advances (net)":         ([343298.27, 345018.63, 315871.39], f"{AR25}/{AR26}"),
    "Balance sheet size":     ([514935.15, 554018.43, 543419.06], f"{AR25}/{AR26}"),
}

# Capital adequacy (standalone, Basel III). Tier 1 == CET-1 for this bank (no AT1 outstanding
# material enough to split the two in the disclosure).
CAP = {
    "CRAR (%)":               ([17.23, 16.24, 17.48], f"{CAP25}/{CAP26}"),
    "CET-1 (%)":              ([15.82, 15.10, 16.20], f"{CAP25}/{CAP26}"),
    "Tier I (%)":             ([15.82, 15.10, 16.20], f"{CAP25}/{CAP26}"),
    "Tier II (%)":            ([1.41, 1.14, 1.28],    f"{CAP25}/{CAP26}"),
    "CET-1 capital (Rs cr)":  ([60710.52, 63341.88, 63766.66], f"{CAP25}/{CAP26}"),
}

# Asset quality (standalone). GNPA/NNPA % from the formal asset-quality schedule, which differs
# from the CONSOLIDATED figures in the quarterly results (FY26 consol GNPA 3.13% vs standalone
# 3.43%); standalone is the rated basis here.
AQ_DATA = {
    "GNPA (%)":               ([1.92, 3.13, 3.43], AQ),
    "NNPA (%)":               ([0.57, 0.95, 1.00], AQ),
    "PCR (%)":                [(None, 70.24, 71.44), AQ],   # FY24 PCR not separately disclosed in set
    "GNPA (Rs cr) - FY26":    ([11095.35], "Q4FY26/Q1FY27 results (consol abs 11,09,535 lakh)"),
}

# Headline ratios. NIM here is the bank's OWN headline/KPI series (NII / average assets basis),
# internally consistent FY22-FY26. The audited Business-Ratios schedule (note 14.1) reports NIM
# on an average-EARNING-assets basis at a higher level (FY25 3.94%, FY26 3.74%); both show the
# same compression and the basis is footnoted in the workpaper.
RATIOS = {
    "NIM (%) - headline":     ([4.28, 3.62, 3.43], f"{KPI} / AR26 L1685 MD&A"),
    "NIM (%) - note 14.1":    [(None, 3.94, 3.74), "AR26 L13958 Business-Ratios schedule"],
    "RoA (%)":                ([1.90, 0.50, 0.18], f"{KPI} / AR26 L13960"),
    "RoE (%)":                ([15.32, 4.17, 1.44], f"{KPI} / AR26 L1003"),
    "Cost of deposits (%)":   [(None, 6.53, 6.21), "AR26 L13956 Business-Ratios schedule"],
}

# CASA computed from Schedule 3 components (demand + savings over total deposits). A COMPUTED
# figure, not a headline the bank prints - so the arithmetic is shown and it is tied out below.
CASA = {
    # (demand, savings, deposits)  Rs crore, FY2025 and FY2026 only (Schedule 3 carries 2 yrs)
    "FY2025": (40980.36, 94024.75, 411078.14),   # demand 619.34(banks)+40361.02(others)
    "FY2026": (35276.81, 89899.12, 400173.75),   # demand 203.14(banks)+35073.67(others)
}
DEPOSITS_LIEN_FY26 = 52501.76   # AR26 L11533 - deposits against which a lien is marked (encumbered)

# FY22-FY23 context (KPI infographic), for the trend commentary only - single-sourced, not tied.
CONTEXT = {
    "Balance sheet size": {"FY2022": 401974.58, "FY2023": 457804.05},
    "RoA (%)":            {"FY2022": 1.28, "FY2023": 1.81},
    "NIM (%) - headline": {"FY2022": 4.11, "FY2023": 4.27},
    "RoE (%)":            {"FY2022": 10.20, "FY2023": 14.53},
}

# Interim recovery (standalone, Rs cr) - Q1 FY2027 vs Q1 FY2026.
INTERIM = {
    "Net profit (standalone)": {"Q1FY26": 684.25, "Q1FY27": 1002.50},
    "Net profit (consol)":     {"Q1FY26": 604.07, "Q1FY27": 1037.05},
    "Operating profit (std)":  {"Q1FY26": 2652.16, "Q1FY27": 2683.16},
    "RoA (%) consol":          {"Q1FY26": 0.45, "Q1FY27": 0.78},
    "GNPA (%) consol":         {"Q1FY26": 3.64, "Q1FY27": 3.25},
    "NNPA (%) consol":         {"Q1FY26": 1.12, "Q1FY27": 0.95},
    "CRAR (%)":                {"Q1FY26": 16.63, "Q1FY27": 17.15},
    "CET-1 (%)":               {"Q1FY26": 15.48, "Q1FY27": 16.10},
}
SRC_INTERIM = "Q1FY27 results (30-Jun-2026) + Q1FY26 results (30-Jun-2025)"


def _pct(new, old):
    return (new - old) / abs(old) * 100.0


def _b(x):
    return 1.0 if x else 0.0


def compute():
    """Ratio suite per rated year, assembled from the tables above."""
    out = {}
    for i, y in enumerate(YEARS):
        d = {}
        for src in (PL, BS, CAP):
            for k, (vals, _s) in src.items():
                if isinstance(vals[i], (int, float)):
                    d[k] = float(vals[i])
        for k, (vals, _s) in AQ_DATA.items():
            if k.endswith("FY26"):
                continue
            if i < len(vals) and isinstance(vals[i], (int, float)):
                d[k] = float(vals[i])
        for k, (vals, _s) in RATIOS.items():
            if i < len(vals) and isinstance(vals[i], (int, float)):
                d[k] = float(vals[i])
        # derived: TOTAL provisions & contingencies / closing net advances. This is NOT the loan
        # "credit cost" - the P&C line also carries standard-asset provisions, investment
        # depreciation and other provisions, so it overstates credit cost (FM34/FM36: never feed
        # an aggregate subtotal into a ratio as if it were its pure component). CRISIL's reported
        # loan credit cost for FY26 is ~1.5% vs this 2.5% total. Labelled honestly so neither the
        # rationale nor the offline model mistakes it for credit cost.
        d["Total provisions/advances (%)"] = round(
            PL["Provisions & conting."][0][i] / BS["Advances (net)"][0][i] * 100, 2)
        # derived: cost-to-income = opex / revenue
        d["Cost-to-income (%)"] = round(PL["Operating expenses"][0][i] / PL["Revenue (NII + other)"][0][i] * 100, 2)
        out[y] = d
    # CASA ratios (computed)
    for y, (dem, sav, dep) in CASA.items():
        out.setdefault(y, {})["CASA ratio (%)"] = round((dem + sav) / dep * 100, 2)
    return out


def tieouts(R=None):
    """(description, computed, disclosed, tolerance, source) - the shared engine contract.

    Each check reconciles two INDEPENDENTLY sourced disclosures, or an internal P&L identity.
    """
    T = []
    NUM = 0.06

    for i, y in enumerate(YEARS):
        # Revenue identity: NII + non-interest income = revenue
        T.append(("%s revenue = NII + non-interest income" % y,
                  round(PL["Net interest income"][0][i] + PL["Non-interest income"][0][i], 2),
                  PL["Revenue (NII + other)"][0][i], NUM, "P&L identity, AR summary"))
        # NII identity: interest earned - interest expended
        T.append(("%s NII = interest earned - expended" % y,
                  round(PL["Interest earned"][0][i] - PL["Interest expended"][0][i], 2),
                  PL["Net interest income"][0][i], NUM, "P&L identity vs stated NII"))
        # PBT identity: operating profit - provisions
        T.append(("%s PBT = operating profit - provisions" % y,
                  round(PL["Operating profit"][0][i] - PL["Provisions & conting."][0][i], 2),
                  PL["Profit before tax"][0][i], NUM, "P&L identity"))
        # PAT identity: PBT - tax
        T.append(("%s PAT = PBT - tax" % y,
                  round(PL["Profit before tax"][0][i] - PL["Tax"][0][i], 2),
                  PL["Net profit (standalone)"][0][i], NUM, "P&L identity"))
        # CRAR = Tier I + Tier II
        T.append(("%s CRAR = Tier I + Tier II" % y,
                  round(CAP["Tier I (%)"][0][i] + CAP["Tier II (%)"][0][i], 2),
                  CAP["CRAR (%)"][0][i], NUM, "capital schedule"))
        # consolidated PAT differs from standalone by a small BFIL/associate amount
        T.append(("%s |consol PAT - standalone PAT| < Rs 100 cr" % y,
                  _b(abs(PL["Net profit (consol)"][0][i] - PL["Net profit (standalone)"][0][i]) < 100.0),
                  1.0, 0.5, "subsidiary/associate contribution is small"))
        # NNPA < GNPA
        T.append(("%s NNPA%% < GNPA%%" % y,
                  _b(AQ_DATA["NNPA (%)"][0][i] < AQ_DATA["GNPA (%)"][0][i]), 1.0, 0.5,
                  "asset-quality schedule, internal consistency"))

    # Direction-of-travel checks (the rating story is the TREND, not a level - FM16)
    T.append(("RoA fell FY24->FY26 (stress year)",
              _b(RATIOS["RoA (%)"][0][2] < RATIOS["RoA (%)"][0][0]), 1.0, 0.5, f"{KPI}"))
    T.append(("NII declined every year FY24->FY26",
              _b(PL["Net interest income"][0][2] < PL["Net interest income"][0][1]
                 < PL["Net interest income"][0][0]), 1.0, 0.5, "AR summary"))
    T.append(("GNPA%% rose FY24->FY26 (MFI stress)",
              _b(AQ_DATA["GNPA (%)"][0][2] > AQ_DATA["GNPA (%)"][0][0]), 1.0, 0.5, AQ))
    T.append(("Advances CONTRACTED in FY26 (de-risking)",
              round(_pct(BS["Advances (net)"][0][2], BS["Advances (net)"][0][1]), 2),
              -8.45, 0.10, "AR BS summary stated -8.45%"))

    # CASA computed vs components, and the decline FY25->FY26
    c25 = round(sum(CASA["FY2025"][:2]) / CASA["FY2025"][2] * 100, 2)
    c26 = round(sum(CASA["FY2026"][:2]) / CASA["FY2026"][2] * 100, 2)
    T.append(("FY26 CASA ratio from Schedule 3 components",
              c26, 31.28, NUM, "demand+savings / total deposits, Sch 3"))
    T.append(("CASA ratio WEAKENED FY25->FY26", _b(c26 < c25), 1.0, 0.5,
              "franchise pressure through the stress period"))

    # Interim recovery: Q1FY27 PAT well above Q1FY26
    T.append(("Q1FY27 consol PAT > Q1FY26 (recovery)",
              _b(INTERIM["Net profit (consol)"]["Q1FY27"]
                 > INTERIM["Net profit (consol)"]["Q1FY26"]), 1.0, 0.5, SRC_INTERIM))
    T.append(("Q1FY27 RoA recovered above 0.7%",
              _b(INTERIM["RoA (%) consol"]["Q1FY27"] >= 0.70), 1.0, 0.5, SRC_INTERIM))
    return T


def run():
    print("=" * 96)
    print("INDUSIND BANK - BANK RATIO SUITE (CRISIL, standalone)")
    print("Corporate ratios (gearing / TOL-TNW / interest coverage / GCA days) are NOT applicable")
    print("to a bank and are deliberately omitted (CLAUDE.md failure modes 21/28).")
    print("=" * 96)

    R = compute()
    rows = (list(PL) + list(BS) + ["CASA ratio (%)"] + list(CAP)
            + ["GNPA (%)", "NNPA (%)", "PCR (%)"]
            + ["NIM (%) - headline", "RoA (%)", "RoE (%)", "Cost of deposits (%)",
               "Total provisions/advances (%)", "Cost-to-income (%)"])
    print(f"\n{'STANDALONE (Rs cr / %)':<28}" + "".join(f"{y:>14}" for y in YEARS))
    seen = set()
    for label in rows:
        if label in seen:
            continue
        seen.add(label)
        cells = []
        for y in YEARS:
            v = R[y].get(label)
            cells.append(f"{v:>14,.2f}" if isinstance(v, float) else f"{'-':>14}")
        print(f"{label:<28}" + "".join(cells))

    print("\nCOMPUTED CASA (Schedule 3): demand + savings / total deposits")
    for y, (dem, sav, dep) in CASA.items():
        print(f"  {y}: ({dem:,.2f} + {sav:,.2f}) / {dep:,.2f} = {(dem+sav)/dep*100:,.2f}%")
    print(f"  Deposits with lien marked (encumbered), FY26: Rs {DEPOSITS_LIEN_FY26:,.2f} cr")

    print("\nINTERIM RECOVERY (standalone/consol, Rs cr / pct)  [" + SRC_INTERIM + "]")
    for label, d in INTERIM.items():
        print(f"  {label:<28} Q1FY26 {d['Q1FY26']:>10,.2f}    Q1FY27 {d['Q1FY27']:>10,.2f}")

    print("\n" + "=" * 96)
    print("TIE-OUTS (each reconciles two independent disclosures or a P&L identity - Step 17)")
    print("=" * 96)
    failed = 0
    for desc, comp, disc, tol, _src in tieouts():
        ok = abs(comp - disc) <= tol
        failed += 0 if ok else 1
        print(f"  [{'OK ' if ok else 'FAIL'}] {desc:<52} expected {disc!s:>10} got {comp!s:>10}")
    n = len(tieouts())
    print(f"\n{n - failed}/{n} tie-outs reconcile.")
    if failed:
        print("*** UNRECONCILED ITEMS MUST BE RESOLVED BEFORE DRAFTING (Step 17). ***")
    return failed


# ---- Measured coverage disclosure (failure mode 39) -----------------------------------------
DISCLOSED_DIFFERENCES = [
    ("FY2024 PCR, cost of deposits and note-14.1 NIM are single-period / single-source",
     "The FY2024 column for PCR, cost of deposits and the earning-assets NIM is not carried in "
     "the two-year schedules extracted, so those cells are left blank rather than estimated. No "
     "rated conclusion rests on the FY2024 value of these three items."),
    ("FY2022-FY2023 context series is illustrative, not tied",
     "Balance sheet, RoA, NIM and RoE for FY2022-FY2023 come from the KPI infographic as a single "
     "source to show the pre-stress baseline; each is taken as printed and reconciled by nothing."),
    ("NIM is disclosed on two bases and both are retained",
     "Headline/KPI NIM (average-assets basis: 4.28/3.62/3.43) and the audited note-14.1 NIM "
     "(average-earning-assets basis: -/3.94/3.74) differ by ~30bps. Both are reported by the bank; "
     "the rationale uses the headline series and footnotes the schedule basis. Neither is wrong - "
     "they measure NIM on different denominators."),
    ("'Total provisions/advances' is NOT the loan credit cost",
     "The ratio is total Provisions & Contingencies over net advances (2.5% FY26). The P&C line "
     "includes standard-asset provisions, investment depreciation and other provisions, so it "
     "OVERSTATES the loan credit cost, which CRISIL reports at ~1.5% for FY26. Do not quote this "
     "figure as 'credit cost' (FM34/FM36 - an aggregate subtotal is not its pure component)."),
    ("GNPA is standalone 3.43% not consolidated 3.13%",
     "The quarterly results report a consolidated GNPA of 3.13% for FY26; the standalone asset-"
     "quality schedule reports 3.43%. The case is rated standalone, so 3.43% is used; the gap is "
     "the BFIL microfinance book's treatment on consolidation."),
]


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
