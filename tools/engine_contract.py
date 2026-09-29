"""The interface a ratio engine must expose for the shared tools to work on it.

`rate_engine.py`, `tieout_mutation.py` and `build_rationale.py` all drive a case's
`compute_ratios.py` through the same small contract:

    YEARS      : list of period labels, oldest first
    compute()  : -> {period: {ratio_name: value}}
    tieouts(R) : -> [(description, computed, disclosed, tolerance, source), ...]

Optional, used when present:

    DISCLOSED_DIFFERENCES : [(title, text), ...]
    UNVERIFIED_INPUTS     : {(table, key, period), ...}

AUDITED 29-Aug-2026: of 21 engines in this project, only THREE meet the full contract
(balkrishna-industries-ltd, jindal-stainless, repco-home-finance-limited). Six expose
`compute()` but no `tieouts()`; twelve predate the contract entirely and are written as
top-level scripts around a `run()` function.

Before this module existed the three tools crashed on those 18 cases with a raw
`AttributeError: module 'engine_sbi' has no attribute 'compute'` - a traceback that tells the
user nothing about what is wrong or what to do. A tool that cannot support a case must say so
in one clear sentence; crashing is not a failure mode, it is an absence of one.
"""

REQUIRED = ("YEARS", "compute", "tieouts")


def missing(mod):
    """Which contract members this engine lacks."""
    out = []
    for name in REQUIRED:
        obj = getattr(mod, name, None)
        if obj is None:
            out.append(name)
        elif name != "YEARS" and not callable(obj):
            out.append(name + " (present but not callable)")
    return out


def describe(mod):
    """What the engine DOES expose, so the message is useful rather than just negative."""
    have = [n for n in dir(mod) if not n.startswith("_") and callable(getattr(mod, n, None))]
    return sorted(have)[:12]


def require(mod, slug, tool):
    """Return None if the engine is usable, else a ready-to-print explanation."""
    gaps = missing(mod)
    if not gaps:
        return None
    return (
        "%s cannot run on '%s': its compute_ratios.py does not expose %s.\n"
        "\n"
        "  This tool drives every engine through one small contract:\n"
        "      YEARS       list of periods, oldest first\n"
        "      compute()   -> {period: {ratio: value}}\n"
        "      tieouts(R)  -> [(description, computed, disclosed, tolerance, source), ...]\n"
        "\n"
        "  That engine defines: %s\n"
        "\n"
        "  Most engines in this project predate the contract and are written as top-level\n"
        "  scripts. They still RUN correctly on their own (`python compute_ratios.py`);\n"
        "  they just cannot be driven programmatically. To use this tool on the case,\n"
        "  refactor its engine to expose compute() and tieouts() - see\n"
        "  Companies/jindal-stainless/compute_ratios.py as the reference shape."
        % (tool, slug, ", ".join(gaps), ", ".join(describe(mod)) or "(nothing callable)")
    )


def periods(mod, R):
    """Periods that BOTH YEARS declares and compute() actually returns, in YEARS order.

    Repco Home Finance declares YEARS = [FY2023, FY2024, FY2025, FY2026, Q1FY2027] while its
    own compute() returns no FY2026 entry. Any tool that trusts YEARS and indexes into
    compute()'s result therefore dies with `KeyError: 'FY2026'` - which is how
    build_rationale.py crashed on 29-Aug-2026, on a case that otherwise met the contract.

    The intersection is the honest answer: report on the periods that actually have numbers,
    and let the caller surface the discrepancy rather than pretend it is not there.
    """
    have = set(R)
    return [y for y in getattr(mod, "YEARS", []) if y in have]


def period_gap(mod, R):
    """Periods YEARS claims that compute() does not produce, if any."""
    have = set(R)
    return [y for y in getattr(mod, "YEARS", []) if y not in have]
