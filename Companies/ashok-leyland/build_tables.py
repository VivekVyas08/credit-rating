# -*- coding: utf-8 -*-
"""Render the workpaper's numeric tables straight from compute_ratios.py (R6: numbers are COPIED
from the engine, never retyped). Writes _tables.md, which the workpaper embeds verbatim."""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cr", os.path.join(HERE, "compute_ratios.py"))
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)
R = cr.compute()
T = cr.tieouts(R)
Y = cr.YEARS


def fmt(x, dec=2):
    if x is None:
        return "-"
    return "{:,.{d}f}".format(x, d=dec)


def table(title, rows, dec=2):
    out = ["**%s**" % title, "", "| Metric | " + " | ".join(Y) + " |",
           "|---|" + "---:|" * len(Y)]
    for k in rows:
        out.append("| %s | %s |" % (k, " | ".join(fmt(R[y].get(k), dec) for y in Y)))
    return "\n".join(out) + "\n"


parts = []
parts.append(table("A. AL standalone (the rated entity) - ICRA ratio suite (Rs crore)", [
    "Operating income", "Revenue growth (%)", "OPBDITA", "OPBDITA margin (%)", "PBIT (operating)",
    "PBIT margin (%)", "PAT", "PAT margin (%)", "Total debt", "Tangible net worth",
    "Total outside liabilities", "Gearing (x)", "TOL/TNW (x)", "Total debt/OPBDITA (x)",
    "Interest coverage (x)", "DSCR (x)", "RoCE (%)", "NCA (PAT + D&A - dividend)",
    "Free cash and liquid investments", "Net debt (negative = net cash)", "Net debt/OPBDITA (x)",
    "Current ratio (x)", "Debtor days", "Inventory days", "Payable days", "CFO",
    "RCF (CFO - dividend)", "FCF (RCF - capex - repayments)", "Capex/OI (%)",
    "Support to subsidiaries (equity)"]))
parts.append(table("B. METHODOLOGY BASIS - automotive business = consolidated EXCLUDING financial services "
                   "(ICRA 934; HLF assessed separately)", [
    "AUTO CV revenue", "AUTO CV PBIT margin (%)", "AUTO OPBDITA low (CV PBIT + standalone D&A)",
    "AUTO OPBDITA high (CV PBIT + consolidated D&A)", "AUTO total debt",
    "AUTO non-FS subsidiary borrowings", "AUTO debt/OPBDITA at low bound (x)",
    "AUTO interest coverage at low bound (x)", "AUTO net assets (CV segment)",
    "AUTO gearing on CV net assets (x)",
    "ADJ standalone debt + non-FS subsidiary debt / standalone OPBDITA (x)",
    "ADJ net debt incl. non-FS subsidiary debt (negative = net cash)"]))
parts.append(table("C. Reported consolidated incl. Hinduja Leyland Finance (supplementary only)", [
    "CONS operating income", "CONS PAT", "CONS total debt", "CONS TNW (incl. NCI)",
    "CONS TOL/TNW (x)", "CONS total debt/OPBDITA (x)", "CONS FS share of group borrowings (%)"]))
parts.append(table("D. Operating and support series", [
    "Total vehicle volume", "M&HCV market share (%)", "Corporate guarantees for subsidiaries"], dec=1))

npass = sum(1 for t in T if abs(t[1] - t[2]) <= t[3])
lines = ["**E. Tie-out register (%d/%d reconcile)**" % (npass, len(T)), "",
         "| # | Check | Computed | Disclosed | Tol | Result | Source |", "|---|---|---:|---:|---:|---|---|"]
for i, (d, c, x, tol, src) in enumerate(T, 1):
    lines.append("| %d | %s | %s | %s | %s | %s | %s |" % (
        i, d, fmt(c), fmt(x), fmt(tol), "PASS" if abs(c - x) <= tol else "**FAIL**", src))
parts.append("\n".join(lines) + "\n")

open(os.path.join(HERE, "_tables.md"), "w", encoding="utf-8").write("\n".join(parts))
print("wrote _tables.md: %d tie-outs, %d pass" % (len(T), npass))
