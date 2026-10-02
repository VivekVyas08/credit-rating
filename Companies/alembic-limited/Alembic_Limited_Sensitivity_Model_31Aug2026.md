# Alembic Limited — Sensitivity Model (Step 12, scaled per case.json)

All figures Rs crore, standalone, from `compute_ratios.py`. FY2026 actual is the anchor.

## Why this shape, and not a 3-statement model

Total debt is **Rs 10.64 crore**. OPBDIT is **Rs 87.69 crore**. Interest cover is **55.95 times**
and the company holds **net cash of Rs 81.38 crore**. Run any plausible revenue, margin or capex
path through a three-statement model and the debt-servicing answer does not change, because
there is almost no debt to service. A model whose output cannot vary with its inputs is not a
forward view; it is arithmetic theatre.

The two variables that *can* move this credit are neither revenue nor margin:

## Variable 1 — the market value of the listed portfolio (the dominant one)

The company's own note 6 discloses the aggregate market value of its quoted investments. The
series is the finding:

| FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| 3,156.46 | **5,823.75** | 5,490.20 | **3,885.89** |

Down **33% from the FY2024 peak**, and down 29.2% (Rs 1,604.31 crore) in FY2026 alone. The
holdings are Alembic Pharmaceuticals (28.54%, carried at cost of Rs 86.65 crore in the
standalone accounts) and Paushak (carried at FVOCI, Rs 162.52 crore after a Rs 102.99 crore
markdown in FY2026).

| Scenario | Portfolio value | Cover on total debt | Assessment |
|---|---|---|---|
| Actual FY2026 | 3,885.89 | 365x | Flexibility overwhelming |
| A further 30% fall | ~2,720 | ~256x | **No rating consequence** |
| A further 50% fall | ~1,943 | ~183x | **No rating consequence** |
| A 90% fall | ~389 | ~37x | Still ample against Rs 10.64 cr of debt |

**The honest conclusion is that this variable does not bind at current debt levels**, and saying
so is more useful than a table implying otherwise. It would bind if AL levered materially
against the portfolio — which is the reason "a debt-funded acquisition or land purchase" is a
named surveillance trigger rather than a generic caution.

What the decline *does* affect is net worth (via OCI, Rs 102.99 crore in FY2026) and the
headline optics of financial flexibility. It does not affect cash flow: **dividend income was
Rs 62.95 crore in both FY2025 and FY2026**, essentially unchanged while the portfolio's market
value fell 29%.

## Variable 2 — the electricity-duty litigation (the one that could actually bind)

Principal provided for: **Rs 20.52 crore**. Deposited with the Supreme Court on 26-May-2023:
**Rs 35.00 crore**. Interest: **disclosed as unascertainable and not acknowledged by the
company**.

| Scenario | Cash impact | Assessment |
|---|---|---|
| Appeal succeeds | Rs 35.00 cr deposit refunded; Rs 20.52 cr provision written back | Positive |
| Appeal fails, interest ≈ principal | ~Rs 20 cr beyond the deposit | Absorbed by liquidity (Rs 92.02 cr on hand) |
| Appeal fails, interest at 2-3x the principal | Rs 40-60 cr beyond the deposit | Absorbed, but consumes most of on-hand liquidity |
| Appeal fails, interest materially above that | Not sizeable from the documents | **The genuine unknown** |

**This cannot be modelled further, because the company itself states the interest is not
ascertainable.** Presenting a point estimate would be inventing a figure the issuer declines to
put a number on. The band above is scaled off the one figure the AR does disclose - the
Rs 20.52 crore principal - and is an analyst's illustration, labelled as such, not a forecast.
**The AR gives no origination date for the notice and no High Court history**; those details sit
only in ICRA's published rationale, which supplies no facts to this exercise, so the elapsed
period cannot be used to size the interest either.

## Variable 3 — the real-estate segment (the operating base)

| | FY2025 | FY2026 |
|---|---|---|
| Revenue | 182.14 | 185.35 |
| Segment PBT | 83.90 | **78.59** |
| Implied segment margin | 46.1% | 42.4% |

Revenue is flat-to-up; segment profit fell 6.3%. Since the AR does not disclose project-level
bookings or completion percentages — **searched and confirmed absent** — the movement cannot be
attributed to a specific project with confidence. Base case: broadly stable, with the
observation that a landholder-developer's revenue is inherently lumpy across project
completions and a single year's move is weak evidence of a trend.

## What this does not replace

This is not the full 5-year 3-statement model the SOP names as the default. It is the analyst's
judgement that for an issuer with Rs 10.64 crore of debt and Rs 3,885.89 crore of listed
securities, the variables above capture materially more of the actual rating sensitivity than a
revenue-and-margin projection would. **If AL announces material debt-funded investment, this
must be upgraded to the full workflow** — at that point the portfolio-value variable starts to
bind and a leverage path becomes worth modelling.
