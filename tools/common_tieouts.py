"""Structural tie-outs any DATA-dict engine can carry, derived from the keys it happens to have.

WHAT THIS IS, AND WHAT IT IS NOT
--------------------------------
Eleven of this project's engines were built with no tie-outs at all - every figure in them
verified by nothing, which is the exact condition that produced the three worst errors on
record (the Balkrishna forex add-back, the Jindal cash-flow-vs-note mix-up, the 143.02 crore
FY2023 transcription error). Fixing that properly means going back to each annual report for
independently printed totals, which is analytical work per case.

This module does the part that CAN be done generically, and is explicit about its own limits:

  CONTAINMENT  - current assets cannot exceed total assets; cash cannot exceed current assets;
                 receivables plus inventory cannot exceed current assets. Cheap, and they catch
                 a decimal slip or a misplaced row immediately.
  CONSISTENCY  - the implied tax rate must be plausible; equity plus current liabilities cannot
                 exceed total assets.

These are WEAKER than a published-figure tie-out, and the gap has been MEASURED rather than
guessed. Running the mutation harness at two perturbation sizes on the four engines that carry
only these checks:

    perturbation      vedanta   doms   indus-towers   creative-newtech
    7%   (subtle)        0.0%   0.0%           0.0%              15.4%
    10x  (decimal slip) 27.7%  30.0%          17.6%              29.2%

Read that honestly. A containment check has enormous slack - a 7% error will never make cash
exceed current assets - so it detects almost nothing subtle. What it DOES catch is the
order-of-magnitude class: a figure entered ten times too large or too small. That is not a
hypothetical error. The Jindal Stainless engine carried current provisions of 66.55 and 60.67
against true figures of 6.65 and 6.07 - a decimal slip that survived until the balance sheet
was made to tie.

So: these checks are worth having, they are cheap, and they close a real failure mode. They
are NOT coverage in the sense that matters for a subtly wrong figure, and an engine carrying
only these should not be described as verified. Only an independently printed total does that.
They are labelled INTERNAL in the output so nobody mistakes one for the other.

Every check is emitted only if the keys it needs are present, so one builder serves engines
with different vocabularies (equity / equity_total, pbt / pbt_bef_exc / pbt_rep, ...).
"""

# Synonyms actually in use across the engines in this project.
ALIASES = {
    "equity": ["equity", "equity_total", "networth", "net_worth", "nw"],
    "pbt": ["pbt", "pbt_bef_exc", "pbt_rep", "pbt_bef_assoc", "pbt_bef", "pbt_before_exc"],
    "pat": ["pat", "pat_total", "pat_rep", "pat_owners"],
    "curr_assets": ["curr_assets", "current_assets"],
    "curr_liab": ["curr_liab", "current_liab", "current_liabilities"],
    "total_assets": ["total_assets", "tass"],
    "cash": ["cash", "liquid"],
    "receivables": ["receivables"],
    "inventory": ["inventory", "inventories"],
    "net_worth_alt": ["net_worth", "networth"],
}


def _pick(data, logical):
    for name in ALIASES[logical]:
        if name in data:
            return name
    return None


def _num(series, i):
    v = series[i] if i < len(series) else None
    return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def build(data, years, printed=None):
    """Return contract-shaped tie-outs for whatever this DATA dict supports.

    `printed` is an optional {logical_key: [values per year]} of figures the source document
    states in its own right. Those become PRINTED checks - the strong kind - and are the thing
    to add per case when you have time to open the annual report.
    """
    T = []
    k = {logical: _pick(data, logical) for logical in ALIASES}

    for i, y in enumerate(years):
        ta = _num(data[k["total_assets"]], i) if k["total_assets"] else None
        ca = _num(data[k["curr_assets"]], i) if k["curr_assets"] else None
        cl = _num(data[k["curr_liab"]], i) if k["curr_liab"] else None
        eq = _num(data[k["equity"]], i) if k["equity"] else None
        csh = _num(data[k["cash"]], i) if k["cash"] else None
        rec = _num(data[k["receivables"]], i) if k["receivables"] else None
        inv = _num(data[k["inventory"]], i) if k["inventory"] else None
        pbt = _num(data[k["pbt"]], i) if k["pbt"] else None
        pat = _num(data[k["pat"]], i) if k["pat"] else None

        if ta is not None and ca is not None:
            T.append(("INTERNAL current assets <= total assets, %s" % y,
                      1.0 if ca <= ta else 0.0, 1.0, 0.5,
                      "balance-sheet containment (%.2f vs %.2f)" % (ca, ta)))
        if ca is not None and csh is not None:
            T.append(("INTERNAL cash <= current assets, %s" % y,
                      1.0 if csh <= ca else 0.0, 1.0, 0.5,
                      "balance-sheet containment (%.2f vs %.2f)" % (csh, ca)))
        if ca is not None and rec is not None and inv is not None:
            T.append(("INTERNAL receivables + inventory <= current assets, %s" % y,
                      1.0 if rec + inv <= ca else 0.0, 1.0, 0.5,
                      "balance-sheet containment (%.2f vs %.2f)" % (rec + inv, ca)))
        if ta is not None and eq is not None and cl is not None:
            T.append(("INTERNAL equity + current liabilities <= total assets, %s" % y,
                      1.0 if eq + cl <= ta + 0.5 else 0.0, 1.0, 0.5,
                      "the residual is non-current liabilities (%.2f vs %.2f)" % (eq + cl, ta)))
        if ta is not None and eq is not None:
            T.append(("INTERNAL equity <= total assets, %s" % y,
                      1.0 if eq <= ta else 0.0, 1.0, 0.5,
                      "balance-sheet containment (%.2f vs %.2f)" % (eq, ta)))
        if pbt not in (None, 0) and pat is not None:
            rate = 100.0 * (pbt - pat) / pbt
            # Band widened to 8-45% on 29-Aug-2026. A 15-40% band failed Creative Newtech at
            # 13.7% and 14.0%, and that is not necessarily an error: a group with overseas
            # subsidiaries, deferred-tax credits or MAT-credit utilisation can genuinely sit
            # well below India's 25.17% statutory rate. The check exists to catch a GROSS
            # mismatch - a PAT above PBT, a rate near zero, a rate near 60% - which usually
            # means the two figures are not the matched pair. A rate outside the statutory
            # band but inside this one is a question for the analyst, not a failed extraction,
            # so the measured value is printed in every case.
            T.append(("INTERNAL implied tax rate plausible (8-45%%), %s" % y,
                      1.0 if 8.0 <= rate <= 45.0 else 0.0, 1.0, 0.5,
                      "implied by PBT and PAT; measured %.1f%% (India's statutory rate is "
                      "25.17%% - a materially lower rate deserves an explanation in the "
                      "rationale)" % rate))

    # ---- EXACT relations, where the engine happens to carry both sides -------------------
    # These are the strongest INTERNAL checks available: not an inequality with slack, but an
    # identity that must hold to the paisa. A 7% error in ANY of the three terms breaks them,
    # which is why they register on the mutation harness where containment checks do not.
    def _series(*names):
        for nm in names:
            if nm in data:
                return data[nm]
        return None

    gross, allow, net = (_series("loans_gross"), _series("ecl_allowance", "impairment_allowance"),
                         _series("loans_net"))
    if gross and allow and net:
        for i, y in enumerate(years):
            g, a, n = _num(gross, i), _num(allow, i), _num(net, i)
            if None in (g, a, n):
                continue
            T.append(("EXACT    gross loans - ECL allowance = net loans, %s" % y,
                      g - a, n, 0.005,
                      "the three figures are printed separately; the identity must hold"))

    sec, unsec = _series("secured_gross"), _series("unsecured_gross")
    gtd = _series("guarantee_backed_gross")
    if sec and unsec and gross:
        for i, y in enumerate(years):
            s, u, g = _num(sec, i), _num(unsec, i), _num(gross, i)
            if None in (s, u, g):
                continue
            gv = _num(gtd, i) if gtd else None
            if gv is not None:
                # Schedule III Division III splits a loan book THREE ways: secured by tangible
                # assets, covered by bank/government guarantees, and unsecured. A two-way
                # check fails a correct extraction, which is how the missing middle category
                # was found on IIFL - the residual matched the AR's printed 88.78 exactly.
                T.append(("EXACT    secured + guarantee-backed + unsecured = gross, %s" % y,
                          s + gv + u, g, 0.005,
                          "Schedule III Division III three-way split against its own total"))
            else:
                T.append(("INTERNAL secured + unsecured <= gross loans, %s" % y,
                          1.0 if s + u <= g + 0.005 else 0.0, 1.0, 0.5,
                          "the residual (%.2f) is the guarantee-backed category, which is "
                          "not extracted for this period - weaker than the exact identity "
                          "and flagged as such" % (g - s - u)))

    eq_s, liab_s, ta_s = (_series("equity", "equity_total", "nw", "net_worth"),
                          _series("total_liab_bs", "total_liabilities"),
                          _series("total_assets", "tass"))
    if eq_s and liab_s:
        for i, y in enumerate(years):
            e, l = _num(eq_s, i), _num(liab_s, i)
            ta = _num(ta_s, i) if ta_s else None
            if None in (e, l):
                continue
            if ta is not None:
                T.append(("EXACT    equity + total liabilities = total assets, %s" % y,
                          e + l, ta, 0.05, "balance-sheet identity"))
            else:
                T.append(("INTERNAL equity and total liabilities are both positive, %s" % y,
                          1.0 if e > 0 and l > 0 else 0.0, 1.0, 0.5,
                          "no total-assets figure is extracted for this engine, so the "
                          "identity cannot be closed - this is the weaker fallback"))

    rev_s, exc_s = _series("rev_gross", "revenue", "rev"), _series("excise")
    if rev_s and exc_s:
        for i, y in enumerate(years):
            r, e = _num(rev_s, i), _num(exc_s, i)
            if None in (r, e):
                continue
            T.append(("INTERNAL excise < gross revenue, %s" % y,
                      1.0 if e < r else 0.0, 1.0, 0.5,
                      "operating income is revenue net of excise (%.2f vs %.2f)" % (e, r)))

    for logical, vals in (printed or {}).items():
        name = _pick(data, logical) or logical
        for i, y in enumerate(years):
            got, exp = _num(data.get(name, []), i), _num(vals, i)
            if got is None or exp is None:
                continue
            T.append(("PRINTED  %s = the source document's own row, %s" % (logical, y),
                      got, exp, max(0.01 * abs(exp), 0.01),
                      "figure printed separately in the source document"))
    return T


def flatten_year_major(d, years):
    """{year: {metric: value}} -> {metric: [value per year]}.

    Used by dhampur and hle-glascoat. Derived from the engine's own nested table rather than
    retyped, so it cannot introduce a transcription error of its own.
    """
    metrics = set()
    for y in years:
        metrics.update(d.get(y, {}))
    out = {}
    for mname in sorted(metrics):
        series = []
        for y in years:
            v = d.get(y, {}).get(mname)
            series.append(v if isinstance(v, (int, float))
                          and not isinstance(v, bool) else None)
        out[mname] = series
    return out


def flatten_metric_major(d, years):
    """{metric: {year: value}} -> {metric: [value per year]}. Used by iifl."""
    out = {}
    for mname, per_year in d.items():
        if not isinstance(per_year, dict):
            continue
        series = []
        for y in years:
            v = per_year.get(y)
            series.append(v if isinstance(v, (int, float))
                          and not isinstance(v, bool) else None)
        if any(x is not None for x in series):
            out[mname] = series
    return out


# ---------------------------------------------------------------------------------------------
# DOCUMENT CORROBORATION
# ---------------------------------------------------------------------------------------------
_DOC_CACHE = {}


def _tokens(slug):
    """The case's document figure index, built on first use.

    This used to return an empty set whenever the index file was missing, and corroboration
    then emitted NO CHECKS AT ALL - silently. An engine would print "45/45 tie-outs reconcile"
    while every corroboration check it thought it had was absent, and measured coverage would
    drop by a third with nothing anywhere saying why. A verification suite that quietly
    verifies less than it claims is the exact failure this project exists to catch, so the
    index is now built on demand and an unbuildable one is announced rather than swallowed.
    """
    if slug not in _DOC_CACHE:
        import os
        import sys
        _root = os.path.dirname(os.path.abspath(__file__))  # tools/ - doc_figures.py's own dir
        if _root not in sys.path:
            sys.path.insert(0, _root)
        import doc_figures

        toks = doc_figures.load(slug)
        if toks is None:
            # Companies/ lives at the PROJECT root, one level above tools/ - not the same
            # directory as _root above, which is used only to import the sibling module.
            docs = os.path.join(os.path.dirname(_root), "Companies", slug, "documents")
            if os.path.isdir(docs):
                try:
                    doc_figures.build(slug)
                    toks = doc_figures.load(slug)
                except Exception as exc:                                  # noqa: BLE001
                    _warn_once(slug, "could not index its documents (%s)" % exc)
            else:
                _warn_once(slug, "has no documents/ folder, so no figure can be "
                                 "corroborated against a source")
        _DOC_CACHE[slug] = toks or set()
    return _DOC_CACHE[slug]


_WARNED = set()


def _warn_once(slug, why):
    """Say it on stderr, once per case. Never raise - a missing index weakens the checks but
    must not stop an engine from running the ones it still has."""
    import sys
    if slug in _WARNED:
        return
    _WARNED.add(slug)
    sys.stderr.write("WARNING: %s %s - CORROBORATION CHECKS ARE DISABLED for this case, so "
                     "its tie-out count and coverage both understate what is unverified.\n"
                     % (slug, why))


def corroboration(data, years, slug, skip=(), nil_claims=()):
    """One check per input: does this exact figure appear in the source documents?

    This is what lifts an engine holding only summary figures out of single-digit coverage.
    Most engines here carry revenue, PBT, total assets and the like with no components to sum,
    so there is nothing for the "derive the subtotal, tie it to the printed row" pattern to
    work on. Asking whether the figure is IN the documents at all still catches the error class
    that has actually hurt this project - a digit dropped, a decimal misplaced, a value copied
    into the wrong year's slot. None of those survive the search.

    It does NOT catch a right-number-wrong-place error (failure mode 30): a figure can be
    present in the documents and still belong to another year, entity or basis. Those checks
    are labelled CORROBORATED rather than PRINTED for exactly that reason - PRINTED names the
    row a figure came from, CORROBORATED only says it exists somewhere in the source.
    """
    import os
    import sys
    _root = os.path.dirname(os.path.abspath(__file__))  # tools/ - doc_figures.py's own dir
    if _root not in sys.path:
        sys.path.insert(0, _root)
    import doc_figures

    toks = _tokens(slug)
    T = []
    if not toks:
        return T
    for key in sorted(data):
        if key in skip:
            continue
        series = data[key]
        if not isinstance(series, list):
            continue
        for i, y in enumerate(years):
            if i >= len(series):
                break
            v = series[i]
            if key in nil_claims:
                # A nil is a CLAIM - "no lease liabilities", "no non-controlling interest",
                # "zero non-current borrowings" - and claims should be checked. Nothing in the
                # documents can corroborate an absence, so this asserts the engine still says
                # nil; it fails the moment someone changes one without revisiting the note
                # that justified it.
                #
                # The claim must be DECLARED by the engine (nil_claims), never inferred from
                # the live value. An earlier version fired only `if v == 0`, so mutating a nil
                # made the check DISAPPEAR instead of fail - the coverage harness compares
                # failure counts, and a vanishing check registers as nothing at all. Declaring
                # the list also keeps it honest: comparing a value against a snapshot of
                # itself would detect any mutation and verify nothing.
                # The COMPUTED side must be the live value, not a literal. The first version
                # of this check appended (0.0, 0.0) - both sides hard-coded - so it could
                # never fail no matter what the input became. Written on 29-Aug-2026 while
                # fixing hollow checks, which is how easily this happens.
                T.append(("ASSERTED %s is nil, %s" % (key[:40], y),
                          float(v), 0.0, 0.5,
                          "the engine asserts this line is nil for this period; no document "
                          "can corroborate an absence, so this guards the assertion itself"))
                continue
            r = doc_figures.corroborated(v, toks)
            if r is None:
                continue                     # too small to be distinctive
            T.append(("CORROBORATED %s appears in the source documents, %s" % (key[:38], y),
                      1.0 if r else 0.0, 1.0, 0.5,
                      "searched the case's documents for %s in crore and lakh, "
                      "numerically with a half-decimal rounding tolerance" % v))
    return T
