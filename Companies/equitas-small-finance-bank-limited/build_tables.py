# -*- coding: utf-8 -*-
"""Render the workpaper's numeric tables from compute_ratios.py (R6) -> _tables.md."""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("cr", os.path.join(HERE, "compute_ratios.py"))
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)
R, Y = cr.compute(), cr.YEARS
T = cr.tieouts(R)


def fmt(x):
    return "-" if x is None else "{:,.2f}".format(x)


keys = []
for y in Y:
    keys += [k for k in R[y] if k not in keys]
out = ["**A. CareEdge financial-sector ratio suite - standalone (Rs crore / %)**", "",
       "| Metric | " + " | ".join(Y) + " |", "|---|" + "---:|" * len(Y)]
out += ["| %s | %s |" % (k, " | ".join(fmt(R[y].get(k)) for y in Y)) for k in keys]
npass = sum(1 for t in T if abs(t[1] - t[2]) <= t[3])
out += ["", "**B. Tie-out register (%d/%d reconcile)**" % (npass, len(T)), "",
        "| # | Check | Computed | Disclosed | Tol | Result | Source |", "|---|---|---:|---:|---:|---|---|"]
out += ["| %d | %s | %s | %s | %s | %s | %s |" % (i, d, fmt(c), fmt(x), fmt(t), "PASS" if abs(c - x) <= t else
        "**FAIL**", s) for i, (d, c, x, t, s) in enumerate(T, 1)]
open(os.path.join(HERE, "_tables.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("wrote _tables.md: %d metrics, %d/%d tie-outs" % (len(keys), npass, len(T)))
