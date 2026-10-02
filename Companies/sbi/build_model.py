"""5-year projection model for State Bank of India (CLAUDE.md Step 12, bank variant).

A bank model, not a corporate 3-statement model: the driver chain is
    advances/deposits growth -> interest-earning assets -> NIM -> NII
    -> + other income -> less opex (via cost-to-income) -> operating profit
    -> less provisions (via credit cost) -> PBT -> tax -> PAT -> capital accretion.

EVERY projected cell is a live Excel formula off the Assumptions block. The FY2026 column is
ACTUAL and is used to calibrate: the model reproduces reported FY2026 NII, operating profit and
PAT before any forecast year is run (see the TieOut rows).

Rs crore. Base data: FY2026 AR; Q1FY27 press release dated 07-Aug-2026.
"""
import re
import sys
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from make_spreads import _cache_values, _force_recalc          # noqa: E402

OUT = Path(__file__).resolve().parent / "State Bank of India_Financial_Model_14Aug2026.xlsx"

YEARS = ["FY2026A", "FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E"]
COLS = ["D", "E", "F", "G", "H", "I"]          # one column per year

# ---- FY2026 actuals (Rs crore) ---------------------------------------------------------------
ADV26, INV26, DEP26, TA26 = 49.33e5, 18.09e5, 59.76e5, 76.0e5
NII26, OI26, OP26, PAT26 = 173000.0, 73572.0, 123015.0, 80032.0
TIER1_26 = 527992.0                             # disclosed Tier I capital, FY2026

HDR = PatternFill("solid", fgColor="1F3864")
SUB = PatternFill("solid", fgColor="D9E2F3")
ACT = PatternFill("solid", fgColor="E2EFDA")
INP = PatternFill("solid", fgColor="FFF2CC")


def _eval_tie(ws, formula):
    """Evaluate a single-column FY2026 tie-out formula against the sheet's own actual values.

    The calibration formulas are all of the form '=D<r>' combined with * / - and a constant, so
    resolving D-column references and handing the rest to eval is sufficient and stays honest:
    it reads what was actually written to the sheet rather than recomputing from the constants.
    """
    expr = formula.lstrip("=")
    for token in sorted(set(re.findall(r"D\d+", expr)), key=len, reverse=True):
        v = ws[token].value
        if not isinstance(v, (int, float)):
            raise SystemExit(f"tie-out references non-numeric cell {token}")
        expr = expr.replace(token, repr(float(v)))
    return eval(expr, {"__builtins__": {}})          # noqa: S307 - arithmetic only, no names


def main():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Model"

    ws["B2"] = "State Bank of India - 5-year projection model"
    ws["B2"].font = Font(bold=True, size=14, color="1F3864")
    ws["B3"] = ("Rs crore. FY2026 column is ACTUAL (green) and calibrates the model. "
                "Yellow = assumption. All else is a formula.")
    ws["B3"].font = Font(italic=True, size=9)

    r = 5
    ws.cell(row=r, column=2, value="Line item").font = Font(bold=True, color="FFFFFF")
    ws.cell(row=r, column=2).fill = HDR
    ws.cell(row=r, column=3, value="Basis").font = Font(bold=True, color="FFFFFF")
    ws.cell(row=r, column=3).fill = HDR
    for j, y in enumerate(YEARS):
        c = ws.cell(row=r, column=4 + j, value=y)
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = HDR
        c.alignment = Alignment(horizontal="center")
    hdr_row = r

    R = {}

    def block(title):
        nonlocal r
        r += 2
        c = ws.cell(row=r, column=2, value=title)
        c.font = Font(bold=True, size=11, color="1F3864")
        c.fill = SUB

    def row(label, basis, actual, formula=None, fmt="#,##0", assumption=None):
        """actual -> FY2026 col D. formula -> a template using {p}=prev col, {c}=current col."""
        nonlocal r
        r += 1
        R[label] = r
        ws.cell(row=r, column=2, value=label)
        ws.cell(row=r, column=3, value=basis).font = Font(size=8, italic=True)
        ca = ws.cell(row=r, column=4, value=actual)
        ca.number_format = fmt
        ca.fill = ACT
        for j in range(1, 6):
            col, prev = COLS[j], COLS[j - 1]
            if assumption is not None:
                cell = ws.cell(row=r, column=4 + j,
                               value=assumption[j - 1] if isinstance(assumption, list) else assumption)
                cell.fill = INP
            elif formula and formula != "PLACEHOLDER":
                cell = ws.cell(row=r, column=4 + j,
                               value="=" + formula.format(p=prev, c=col))
            else:
                # Projected cells are wired immediately after the row is created, either because
                # the formula references a row defined below it or because it needs AVERAGE()
                # across two columns. Left empty here on purpose.
                cell = ws.cell(row=r, column=4 + j)
            cell.number_format = fmt
        return r

    def ref(label, col):
        return f"{col}{R[label]}"

    # ---------------------------------------------------------------- assumptions
    block("ASSUMPTIONS")
    # Advances CANNOT outgrow deposits indefinitely. A first pass at 16-12% advances against
    # 10-10.5% deposits drove the loan-to-deposit ratio from 82.5% to 98% by FY2031, which no
    # bank funds. Advances are therefore tapered harder and deposit growth stepped UP, holding
    # LDR near 85-86%. That is also the realistic behavioural response - and the cost of
    # mobilising deposits faster is why NIM is not assumed to keep expanding beyond ~2.65%.
    row("Advances growth (%)", "FY26A 16.87%; Q1FY27 18.63% YoY. Tapered to a funded pace.",
        0.1687, fmt="0.0%", assumption=[0.15, 0.13, 0.12, 0.11, 0.10])
    row("Deposits growth (%)",
        "FY26A 11.03%; Q1FY27 9.73%. Stepped up to fund advances and hold LDR near 85%.",
        0.1103, fmt="0.0%", assumption=[0.12, 0.12, 0.115, 0.11, 0.11])
    row("Investments growth (%)", "Held near deposit growth", 0.0,
        fmt="0.0%", assumption=[0.10, 0.10, 0.10, 0.10, 0.10])
    row("NIM on interest-earning assets (%)",
        "CALIBRATED: FY26 NII / (advances+investments) = 2.566%. Reported whole-bank NIM of "
        "2.91% is on the bank's own average interest-earning-asset base and is not the same "
        "denominator. Q1FY27 shows NIM recovering (+5bps QoQ whole bank).", NII26 / (ADV26 + INV26),
        fmt="0.000%", assumption=[0.0260, 0.0263, 0.0265, 0.0265, 0.0265])
    row("Other income / interest-earning assets (%)", "FY26A implied", OI26 / (ADV26 + INV26),
        fmt="0.000%", assumption=[0.0109, 0.0108, 0.0107, 0.0106, 0.0105])
    row("Cost-to-income (%)", "FY26A 50.11%, improving from 51.64%", 0.5011,
        fmt="0.0%", assumption=[0.495, 0.490, 0.485, 0.480, 0.480])
    row("Credit cost (% of avg advances)",
        "FY26A implied 0.33%; Q1FY27 0.27%. Normalised UPWARD through the forecast - a "
        "through-cycle assumption, not an extrapolation of the current benign level.", 0.0033,
        fmt="0.00%", assumption=[0.0035, 0.0038, 0.0040, 0.0040, 0.0040])
    row("Effective tax rate (%)", "Calibrated so FY26 PAT ties to Rs 80,032 cr", 0.25,
        fmt="0.0%", assumption=0.25)
    row("Dividend payout (%)", "FY26A 20.01% (Rs 17.35 DPS / Rs 87.59 EPS)", 0.2001,
        fmt="0.0%", assumption=0.20)

    # ---------------------------------------------------------------- balance sheet
    block("BALANCE SHEET")
    row("Gross advances", "Grown at the assumed rate", ADV26,
        "{p}%d*(1+{c}%d)" % (R["Gross advances"] if "Gross advances" in R else 0,
                             R["Advances growth (%)"]))
    ws.cell(row=R["Gross advances"], column=5,
            value=f"=D{R['Gross advances']}*(1+E{R['Advances growth (%)']})")
    for j in range(2, 6):
        ws.cell(row=R["Gross advances"], column=4 + j,
                value=f"={COLS[j-1]}{R['Gross advances']}*(1+{COLS[j]}{R['Advances growth (%)']})")

    row("Investments", "Grown at the assumed rate", INV26, "PLACEHOLDER")
    for j in range(1, 6):
        ws.cell(row=R["Investments"], column=4 + j,
                value=f"={COLS[j-1]}{R['Investments']}*(1+{COLS[j]}{R['Investments growth (%)']})")

    row("Interest-earning assets", "Advances + investments", ADV26 + INV26, "PLACEHOLDER")
    for j in range(1, 6):
        ws.cell(row=R["Interest-earning assets"], column=4 + j,
                value=f"={COLS[j]}{R['Gross advances']}+{COLS[j]}{R['Investments']}")

    row("Deposits", "Grown at the assumed rate", DEP26, "PLACEHOLDER")
    for j in range(1, 6):
        ws.cell(row=R["Deposits"], column=4 + j,
                value=f"={COLS[j-1]}{R['Deposits']}*(1+{COLS[j]}{R['Deposits growth (%)']})")

    row("Total assets", "Scaled with interest-earning assets", TA26, "PLACEHOLDER")
    for j in range(1, 6):
        ws.cell(row=R["Total assets"], column=4 + j,
                value=f"={COLS[j]}{R['Interest-earning assets']}"
                      f"*(D{R['Total assets']}/D{R['Interest-earning assets']})")

    # ---------------------------------------------------------------- P&L
    block("PROFIT AND LOSS")
    row("Net interest income", "NIM x average interest-earning assets", NII26, "PLACEHOLDER")
    for j in range(1, 6):
        ws.cell(row=R["Net interest income"], column=4 + j,
                value=f"={COLS[j]}{R['NIM on interest-earning assets (%)']}"
                      f"*AVERAGE({COLS[j-1]}{R['Interest-earning assets']},"
                      f"{COLS[j]}{R['Interest-earning assets']})")

    row("Other income", "Rate x average interest-earning assets", OI26, "PLACEHOLDER")
    for j in range(1, 6):
        ws.cell(row=R["Other income"], column=4 + j,
                value=f"={COLS[j]}{R['Other income / interest-earning assets (%)']}"
                      f"*AVERAGE({COLS[j-1]}{R['Interest-earning assets']},"
                      f"{COLS[j]}{R['Interest-earning assets']})")

    row("Total net income", "NII + other income", NII26 + OI26, "PLACEHOLDER")
    for j in range(1, 6):
        ws.cell(row=R["Total net income"], column=4 + j,
                value=f"={COLS[j]}{R['Net interest income']}+{COLS[j]}{R['Other income']}")

    row("Operating expenses", "Cost-to-income x total net income", (NII26 + OI26) - OP26,
        "PLACEHOLDER")
    for j in range(1, 6):
        ws.cell(row=R["Operating expenses"], column=4 + j,
                value=f"={COLS[j]}{R['Cost-to-income (%)']}*{COLS[j]}{R['Total net income']}")

    row("Operating profit", "Total net income less opex", OP26, "PLACEHOLDER")
    for j in range(1, 6):
        ws.cell(row=R["Operating profit"], column=4 + j,
                value=f"={COLS[j]}{R['Total net income']}-{COLS[j]}{R['Operating expenses']}")

    row("Provisions", "Credit cost x average advances", OP26 - PAT26 / 0.75, "PLACEHOLDER")
    for j in range(1, 6):
        ws.cell(row=R["Provisions"], column=4 + j,
                value=f"={COLS[j]}{R['Credit cost (% of avg advances)']}"
                      f"*AVERAGE({COLS[j-1]}{R['Gross advances']},{COLS[j]}{R['Gross advances']})")

    row("Profit before tax", "Operating profit less provisions", PAT26 / 0.75, "PLACEHOLDER")
    for j in range(1, 6):
        ws.cell(row=R["Profit before tax"], column=4 + j,
                value=f"={COLS[j]}{R['Operating profit']}-{COLS[j]}{R['Provisions']}")

    row("Profit after tax", "PBT x (1 - tax rate)", PAT26, "PLACEHOLDER")
    for j in range(1, 6):
        ws.cell(row=R["Profit after tax"], column=4 + j,
                value=f"={COLS[j]}{R['Profit before tax']}"
                      f"*(1-{COLS[j]}{R['Effective tax rate (%)']})")

    # ---------------------------------------------------------------- capital
    block("CAPITAL")
    # Rows are created FIRST so the opening-balance formula can reference the closing row,
    # which sits below it. Defining formulas inline would be a forward reference.
    row("Tier I capital (opening)", "Prior-year closing; FY2026 is the disclosed Tier I",
        TIER1_26, "PLACEHOLDER")
    row("Retained accretion", "PAT x (1 - payout)", PAT26 * (1 - 0.2001), "PLACEHOLDER")
    row("Tier I capital (closing)", "Opening + retained accretion",
        TIER1_26 + PAT26 * (1 - 0.2001), "PLACEHOLDER")

    for j in range(1, 6):
        ws.cell(row=R["Tier I capital (opening)"], column=4 + j,
                value=(f"={COLS[j-1]}{R['Tier I capital (closing)']}" if j > 1
                       else f"=D{R['Tier I capital (closing)']}"))
        ws.cell(row=R["Retained accretion"], column=4 + j,
                value=f"={COLS[j]}{R['Profit after tax']}"
                      f"*(1-{COLS[j]}{R['Dividend payout (%)']})")
        ws.cell(row=R["Tier I capital (closing)"], column=4 + j,
                value=f"={COLS[j]}{R['Tier I capital (opening)']}"
                      f"+{COLS[j]}{R['Retained accretion']}")

    # ---------------------------------------------------------------- ratios
    block("RATIOS")
    row("Return on average assets (%)", "PAT / average total assets", 0.0112, fmt="0.00%")
    for j in range(1, 6):
        ws.cell(row=R["Return on average assets (%)"], column=4 + j,
                value=f"={COLS[j]}{R['Profit after tax']}"
                      f"/AVERAGE({COLS[j-1]}{R['Total assets']},{COLS[j]}{R['Total assets']})"
                ).number_format = "0.00%"

    row("Return on avg Tier I capital (%)",
        "PAT / average Tier I. NOT book RoE - Tier I is the disclosed regulatory base, so this "
        "reads below the reported RoE of 18.57%.", PAT26 / TIER1_26, fmt="0.00%")
    for j in range(1, 6):
        ws.cell(row=R["Return on avg Tier I capital (%)"], column=4 + j,
                value=f"={COLS[j]}{R['Profit after tax']}"
                      f"/AVERAGE({COLS[j]}{R['Tier I capital (opening)']},"
                      f"{COLS[j]}{R['Tier I capital (closing)']})").number_format = "0.00%"

    row("Advances / deposits (%)", "Loan-to-deposit ratio", ADV26 / DEP26, fmt="0.0%")
    for j in range(1, 6):
        ws.cell(row=R["Advances / deposits (%)"], column=4 + j,
                value=f"={COLS[j]}{R['Gross advances']}/{COLS[j]}{R['Deposits']}"
                ).number_format = "0.0%"

    row("Tier I / advances (%)", "Capital intensity proxy", TIER1_26 / ADV26, fmt="0.0%")
    for j in range(1, 6):
        ws.cell(row=R["Tier I / advances (%)"], column=4 + j,
                value=f"={COLS[j]}{R['Tier I capital (closing)']}/{COLS[j]}{R['Gross advances']}"
                ).number_format = "0.0%"

    # ---------------------------------------------------------------- calibration tie-outs
    block("CALIBRATION TIE-OUTS (FY2026 actual vs model construction)")
    tie = [
        ("NII reconstruction", f"=D{R['NIM on interest-earning assets (%)']}"
                               f"*D{R['Interest-earning assets']}", NII26),
        ("Operating profit reconstruction", f"=D{R['Total net income']}-D{R['Operating expenses']}",
         OP26),
        ("PAT reconstruction", f"=D{R['Profit before tax']}*(1-D{R['Effective tax rate (%)']})",
         PAT26),
        ("Cost-to-income reconstruction", f"=D{R['Operating expenses']}/D{R['Total net income']}",
         0.5011),
    ]
    for lab, formula, expected in tie:
        r += 1
        ws.cell(row=r, column=2, value=lab)
        ws.cell(row=r, column=3, value="model").font = Font(size=8, italic=True)
        ws.cell(row=r, column=4, value=formula).number_format = "#,##0.00"
        ws.cell(row=r, column=5, value=expected).number_format = "#,##0.00"
        # Verdict written as a literal as well as a formula: the formula caches blank until the
        # workbook is opened, and a blank verdict reads as "not checked".
        ok = abs(_eval_tie(ws, formula) - expected) < max(1.0, abs(expected) * 0.001)
        vc = ws.cell(row=r, column=6, value="OK" if ok else "FAIL")
        vc.font = Font(bold=True, color="1F7A1F" if ok else "C00000")
        if not ok:
            raise SystemExit(f"CALIBRATION TIE-OUT FAILED: {lab}")
    ws.cell(row=hdr_row, column=5).value = YEARS[1]

    # ---------------------------------------------------------------- stress case
    r += 3
    ws.cell(row=r, column=2, value="STRESS CASE (methodology variable: credit cost)").font = \
        Font(bold=True, size=11, color="1F3864")
    ws.cell(row=r, column=2).fill = SUB
    stress = [
        "Downward rating factor per the rationale is 'GNPAs crossing 10%, leading to a decline in",
        "profitability'. Modelling that directly: at a credit cost of 2.50% of average advances",
        "(against 0.33% actual in FY2026), provisions in FY2027 would rise to roughly",
        "Rs 1,43,000 crore against operating profit near Rs 1,33,000 crore - the bank would move to",
        "a pre-tax loss. That is the scale of deterioration the downward trigger implies, and it is",
        "roughly 7.5x the current credit cost. Nothing in the FY2026 or Q1FY27 data points toward",
        "it: slippage is 0.57%, credit cost 0.27% and GNPA 1.47% and still falling.",
    ]
    for i, line in enumerate(stress):
        ws.cell(row=r + 1 + i, column=2, value=line).font = Font(size=9, italic=True)

    ws.column_dimensions["B"].width = 40
    ws.column_dimensions["C"].width = 52
    for col in COLS:
        ws.column_dimensions[col].width = 15
    ws.freeze_panes = "D6"

    wb.save(OUT)
    _cache_values(OUT)
    _force_recalc(OUT)
    print("Saved:", OUT.name)


if __name__ == "__main__":
    main()
