#!/usr/bin/env python3
"""Generate a rationale DRAFT from the verified ratio engine. No Claude, no key, no network.

    python build_rationale.py <case-slug> [--out PATH] [--agency ICRA|CRISIL|CareEdge]

WHAT THIS IS FOR
----------------
The ratio engine, the tie-outs, the mutation harness and the delivery gate are all
provider-independent - anyone with Python can run them. The rationale was the one deliverable
that needed a language model, which meant a user without Claude got verified numbers and no
document to put them in. This closes that gap as far as it can honestly be closed.

It fills in everything that is DERIVABLE:
  * every figure, from the engine, after its tie-outs have passed;
  * the key-financial-indicators table, in the agency's own row order and naming;
  * the computation-basis note, from the engine's DISCLOSED_DIFFERENCES;
  * the inputs no tie-out covers, from UNVERIFIED_INPUTS;
  * every mandatory section header for the agency, so the structural gate is satisfied.

It does NOT write the analysis, and it does not pretend to. Every judgement - why this rating,
which strengths, which risks, what the outlook rests on - is emitted as an explicit

    [ANALYST: ...]

placeholder saying precisely what is needed and which figures bear on it. A draft with
placeholders left in it CANNOT pass the delivery gate: `check_sections.py` fails any report
still containing them. The generator therefore hands over a fully-numbered skeleton and makes
it impossible to ship the skeleton by mistake.

WHAT IT CANNOT DO
-----------------
Populate `compute_ratios.py` for a new company. Extraction - reading an annual report and
deciding which line belongs where - is the judgement-heavy half of this work, and it is the
half a template cannot reach. This tool verifies and formats; a human or a model still has to
read the documents.
"""

import argparse
import json
import sys
import types
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # this script now lives in tools/,
# one level below the project root - moved here 01-Sep-2026 to declutter the root.
PH = "[ANALYST: %s]"


def load_engine(slug):
    """Compile from source every time - never a cached .pyc (see rate_engine.py)."""
    path = ROOT / "Companies" / slug / "compute_ratios.py"
    if not path.exists():
        sys.exit("no compute_ratios.py for %r - build the ratio engine first" % slug)
    sys.path.insert(0, str(path.parent))
    mod = types.ModuleType("gen_engine_" + slug.replace("-", "_"))
    mod.__file__ = str(path)
    sys.modules[mod.__name__] = mod
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), mod.__dict__)
    import engine_contract
    gap = engine_contract.require(mod, slug, "build_rationale.py")
    if gap:
        sys.exit(gap)
    return mod


def load_meta(slug):
    f = ROOT / "Companies" / slug / "case.json"
    if not f.exists():
        return {}
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except Exception:                                                     # noqa: BLE001
        return {}


def check_tieouts(mod):
    R = mod.compute()
    T = mod.tieouts(R)
    bad = [d for d, c, dd, tol, _ in T if abs(c - dd) > tol]
    return R, len(T), bad


def fmt(v):
    if not isinstance(v, (int, float)):
        return "-"
    return "%,.2f".replace("%,", "{:,").format(v) if False else "{:,.2f}".format(v)


def ki_table(mod, R, agency):
    """The agency's key-financial-indicators table, rendered from whatever the engine computes.

    Row names are NOT hard-coded: ICRA's engine yields OPBDITA rows and CareEdge's yields
    PBILDT rows, and inventing a name the engine does not produce is how a template starts
    lying. Whatever compute() returns is what gets printed.
    """
    import engine_contract
    avail = engine_contract.periods(mod, R)
    if not avail:
        raise SystemExit("the engine's compute() returned no period listed in YEARS")
    years = avail[-3:] if len(avail) > 3 else avail
    keys = [k for k, v in R[years[-1]].items() if isinstance(v, (int, float))]
    head = "| %s (%s) | %s |" % (
        "Particulars", "Rs. crore unless stated", " | ".join(years))
    sep = "|---" * (len(years) + 1) + "|"
    rows = [head, sep]
    for k in keys:
        cells = " | ".join(fmt(R[y].get(k)) for y in years)
        rows.append("| %s | %s |" % (k, cells))
    return "\n".join(rows)


def disclosed_block(mod):
    items = getattr(mod, "DISCLOSED_DIFFERENCES", [])
    if not items:
        return "None recorded by the ratio engine."
    return "\n\n".join("**%s** — %s" % (t, x) for t, x in items)


def unverified_block(mod):
    items = sorted(getattr(mod, "UNVERIFIED_INPUTS", set()))
    if not items:
        return ("Every input in the engine is covered by at least one tie-out "
                "(verified by `python tieout_mutation.py`).")
    listing = ", ".join("%s (%s)" % (k, y) for _t, k, y in items)
    return ("The following inputs are verified by **no** tie-out and are therefore weaker "
            "evidence than the rest of the suite: %s. Reproduce with "
            "`python tieout_mutation.py <slug>`." % listing)


# --------------------------------------------------------------------------- templates
def icra_doc(ctx):
    return """{date_line}

**{name}: {ph_headline}**

## Summary of rating action

| Instrument* | Previous rated amount (Rs. crore) | Current rated amount (Rs. crore) | Rating action |
|---|---|---|---|
| {ph_instrument_row} |
| **Total** | | **{ph_total}** | |

*Instrument details are provided in Annexure I. Rated amounts are sanctioned/rated LIMITS, a
different measure from drawn debt. {ph_amount_source}

## Rationale

{ph_rationale}

{ph_outlook_para}

## Key rating drivers and their description

### Credit strengths

{ph_strengths}

### Credit challenges

{ph_challenges}

## Environmental and social risks

**Environmental considerations** – {ph_environmental}

**Social considerations** – {ph_social}

## Liquidity position: {ph_liquidity_descriptor}

**Sources and claims (figures from the ratio engine; the DESCRIPTOR is the conclusion of this
arithmetic, never an adjective chosen first):**

{ph_liquidity_arithmetic}

## Rating sensitivities

**Positive factors** – {ph_positive}

**Negative factors** – {ph_negative}

## Analytical approach

| Analytical approach | Comments |
|---|---|
| Applicable rating methodologies | {methodologies} |
| Parent/Group support | {ph_support} |
| Consolidation/Standalone | {basis}. {ph_basis_reason} |

## About the company

{ph_about}

## Key financial indicators (audited)

{ki}

Source: company annual reports; every ratio computed in `compute_ratios.py`, with all
{n_tieouts} tie-outs reconciling.

**Computation basis, stated rather than implied.** {ph_normalisation}

**Disclosed conventions and differences.**

{disclosed}

**Verification coverage.** {unverified}

## Status of non-cooperation with previous CRA: {ph_noncoop}

## Any other information

{ph_other}

## Rating history for past three years

{ph_history}

## Complexity level of the rated instruments

| Instrument | Complexity indicator |
|---|---|
| {ph_complexity} |

## Annexure I: Instrument details

| ISIN | Instrument name | Date of issuance | Coupon rate | Maturity | Amount rated (Rs. crore) | Current rating and outlook |
|---|---|---|---|---|---|---|
| {ph_annexure} |

## Annexure II: List of entities considered for consolidated analysis

{ph_entities}

---

*Disclaimer: prepared as an analytical exercise from the issuer's published documents applying
{agency}'s methodology framework. NOT an official {agency} publication. Data cut-off:
{ph_cutoff}.*
"""


def careedge_doc(ctx):
    return """Press Release

# **{name}**

{date_line}

| **Facilities/Instruments** | **Amount (Rs. crore)** | **Rating** | **Rating Action** |
|---|---|---|---|
| {ph_instrument_row} |
| **Total** | **{ph_total}** | | |

Details of instruments/facilities in Annexure-1. Amounts are sanctioned/rated LIMITS, a
different measure from drawn debt. {ph_amount_source}

## **Rationale and key rating drivers**

{ph_rationale}

## **Rating sensitivities: Factors likely to lead to rating actions**

### **Positive factors**

{ph_positive}

### **Negative factors**

{ph_negative}

## **Analytical approach:** {basis}

{ph_basis_reason}

## **Outlook:** {ph_outlook}

{ph_outlook_para}

## **Key strengths**

{ph_strengths}

## **Key weaknesses**

{ph_challenges}

## **Liquidity: {ph_liquidity_descriptor}**

{ph_liquidity_arithmetic}

## **Environment, social, and governance (ESG) risks**

**Environmental** – {ph_environmental}

**Social** – {ph_social}

**Governance** – {ph_governance}

## **Applicable criteria**

{methodologies}

## **About the company and industry**

{ph_about}

## **Brief Financials (Consolidated)**

{ki}

Source: company annual reports; every ratio computed in `compute_ratios.py`, with all
{n_tieouts} tie-outs reconciling.

**Computation basis, stated rather than implied.** {ph_normalisation}

**Disclosed conventions and differences.**

{disclosed}

**Verification coverage.** {unverified}

## **Status of non-cooperation with previous CRA:** {ph_noncoop}

## **Any other information**

{ph_other}

## **Rating history for last three years**

{ph_history}

## **Annexure-1: Details of instruments/facilities**

| Name of the instrument | Date of issuance | Coupon rate (%) | Maturity date | Size of the issue (Rs. crore) | Rating assigned |
|---|---|---|---|---|---|
| {ph_annexure} |

## **Annexure-2: List of entities consolidated**

{ph_entities}

## **Annexure-3: Complexity level**

| Instrument | Complexity indicator |
|---|---|
| {ph_complexity} |

---

*Disclaimer: prepared as an analytical exercise from the issuer's published documents applying
{agency}'s published methodology framework. NOT an official {agency} publication. Data
cut-off: {ph_cutoff}.*
"""


ASKS = {
    "ph_headline": "the rating action headline, e.g. '[ICRA]AA (Stable); assigned' or "
                   "'Ratings reaffirmed' - the grade is YOUR decision, not this tool's",
    "ph_instrument_row": "one table row per rated facility - instrument, amount, rating, "
                         "action. Use 'To be confirmed by issuer' for any amount not evidenced "
                         "in the issuer's own documents - never reconstruct or split a figure",
    "ph_total": "the total of the rows above, or 'To be confirmed by issuer'. If you state a "
                "number the lines MUST sum to it",
    "ph_amount_source": "if any amount came from a CRA publication, name the agency AND stamp "
                        "its publication date here, and label it CRA-published rather than "
                        "issuer-confirmed",
    "ph_rationale": "the rating narrative. Answer in order: why this rating level (2-3 "
                    "structural anchors, each with its most-defining number from the table "
                    "below); what changed this period; what could go wrong, each risk "
                    "quantified against its buffer; what you expect, with forward ranges and "
                    "named monitorables",
    "ph_outlook": "Stable / Positive / Negative",
    "ph_outlook_para": "the closing outlook paragraph - what the outlook reflects, and what "
                       "would change it",
    "ph_strengths": "2-4 credit strengths. Each needs a bold positioning claim plus its "
                    "consequence, then 3+ verifiable specifics drawn from the figures below. "
                    "A bare adjective is not a driver",
    "ph_challenges": "2-4 credit challenges, each mapping to a negative sensitivity below",
    "ph_environmental": "the issuer's own disclosed environmental data (emissions, intensity, "
                        "targets) and your assessment. If you assert data is absent, record "
                        "the search that proves it",
    "ph_social": "workforce, safety and community data from the issuer's own BRSR/report, and "
                 "your assessment",
    "ph_governance": "audit opinion, board structure, related-party density, and your "
                     "assessment",
    "ph_liquidity_descriptor": "Superior / Strong / Adequate / Stretched / Poor - chosen AFTER "
                               "the arithmetic below, not before",
    "ph_liquidity_arithmetic": "sources (unencumbered cash and equivalents, undrawn lines, "
                               "operating cash flow) against claims (repayments, capex "
                               "commitments, dividends) over ~12 months. Cash is not liquidity "
                               "until shown UNENCUMBERED - check the lien/charge notes",
    "ph_positive": "upgrade triggers, phrased 'on a sustained basis', each with a threshold",
    "ph_negative": "downgrade triggers, symmetric with the challenges above, each with a "
                   "threshold",
    "ph_support": "'Not applicable', or the parent/group support notch with the support "
                  "criterion quoted verbatim",
    "ph_basis_reason": "why this consolidation basis follows from the consolidation criteria",
    "ph_about": "the company: incorporation, promoters and stake, facilities and capacity, "
                "products, scale, and the sector's defining operating metric as a dated SERIES "
                "rather than a snapshot",
    "ph_normalisation": "state the operating-profit formula explicitly and name the treatment "
                        "of forex, exceptional items and any one-off. Take every figure from "
                        "the P&L NOTES, never from the cash-flow reconciliation - they are "
                        "different measures. 'No exceptional item was disclosed' is an absence "
                        "claim, not a treatment",
    "ph_noncoop": "'Not applicable', or the non-cooperation history",
    "ph_other": "auditor opinion, contingent liabilities, related-party direction, and any "
                "scope limitation - each absence claim backed by a recorded search",
    "ph_history": "the rating history table, or a statement that none exists with the search "
                  "that establishes it",
    "ph_complexity": "one row per instrument - name, then Simple / Complex / Highly Complex",
    "ph_annexure": "one row per instrument. Never reconstruct an undisclosed amount; mark it "
                   "'To be confirmed by issuer'",
    "ph_entities": "every consolidated entity by FULL LEGAL NAME with ownership % and method. "
                   "Materiality governs analytical treatment, never whether an entity is named",
    "ph_cutoff": "the date of the most recent document relied on",
}


# A placeholder that lands inside a markdown table must not contain "|" - it would split the
# row into phantom columns and silently corrupt the table it was meant to help fill.
for _k, _v in ASKS.items():
    assert "|" not in _v, "ASKS[%r] contains a pipe and would break a table row" % _k


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--out")
    ap.add_argument("--agency", choices=["ICRA", "CRISIL", "CareEdge"])
    ap.add_argument("--force", action="store_true",
                    help="write even if the engine's tie-outs do not reconcile")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    mod = load_engine(args.slug)
    meta = load_meta(args.slug)
    agency = args.agency or meta.get("agency") or "ICRA"

    R, n_tieouts, bad = check_tieouts(mod)
    print("tie-outs      : %d/%d reconcile" % (n_tieouts - len(bad), n_tieouts))
    import engine_contract
    gap = engine_contract.period_gap(mod, R)
    if gap:
        print("period gap    : YEARS declares %s but compute() returns no value for it - "
              "those periods are OMITTED from the table below. Fix the engine if they "
              "should be there." % ", ".join(gap))
    if bad and not args.force:
        print("\nREFUSING TO GENERATE - the engine does not reconcile. A formatted document")
        print("built on figures that do not tie is more dangerous than no document, because")
        print("it looks finished. Fix these first, or pass --force knowingly:")
        for b in bad:
            print("  FAIL %s" % b)
        sys.exit(1)

    ctx = {
        "name": meta.get("name", args.slug),
        "agency": agency,
        "date_line": date.today().strftime("%B %d, %Y"),
        "basis": "Consolidated" if "consolidat" in json.dumps(meta).lower() else
                 PH % "Consolidated or Standalone, per the consolidation criteria",
        "methodologies": ("; ".join(meta.get("methodologies", []))
                          or PH % "the applicable methodologies, each with its vintage"),
        "ki": ki_table(mod, R, agency),
        "n_tieouts": n_tieouts,
        "disclosed": disclosed_block(mod),
        "unverified": unverified_block(mod),
    }
    for k, ask in ASKS.items():
        ctx[k] = PH % ask

    template = careedge_doc if agency == "CareEdge" else icra_doc
    doc = template(ctx).format(**ctx)

    out = Path(args.out) if args.out else (
        ROOT / "Companies" / args.slug /
        ("%s_%s_DRAFT_Rating Rationale.md"
         % (ctx["name"], date.today().strftime("%d %b %Y"))))
    out.write_text(doc, encoding="utf-8")

    n_ph = doc.count("[ANALYST:")
    print("agency        : %s" % agency)
    print("wrote         : %s" % out.name)
    print("placeholders  : %d judgement calls left for the analyst" % n_ph)
    print("")
    print("  Every FIGURE is filled from the verified engine. Every JUDGEMENT is marked.")
    print("  The delivery gate will REFUSE this draft while any [ANALYST: ...] remains:")
    print("")
    print('      python check_sections.py "%s"' % out.name)


if __name__ == "__main__":
    main()
