# Grep landmark patterns — Indian annual reports (md-converted), quarterlies, broker notes

Use with `grep -niE "<pattern>" <file>` to build the section map. Patterns are battle-tested on ITC and JSW Steel ARs (pymupdf4llm-converted); extend per company and log new landmarks back into this file (Step 19).

## Financial statements
| Target | Pattern |
|---|---|
| Statements (both bases) | `^#+.*(Standalone\|Consolidated).*(Balance Sheet\|Statement of Profit\|Cash Flow)` |
| Fallback (caps headings) | `CONSOLIDATED BALANCE SHEET\|CONSOLIDATED STATEMENT OF PROFIT` |
| Equity/net-worth block | `Other Equity\|Non-controlling interests\|Total equity` |
| Borrowings lines | `Borrowings\|Lease liabilities\|Acceptances` |

## Instruments (Step 7b — Annexure I)
| Target | Pattern |
|---|---|
| Debt ISINs | `INE[0-9A-Z]{9,10}` |
| NCD schedule/notes | `Non.?Convertible Debenture\|ISIN\|redeemable in\|bullet payment\|call option` |
| CP status (issued/outstanding, often "nil") | `Commercial Paper` |
| Rating disclosures (all CRAs, rated structure) | `ICRA\|CRISIL\|CARE Rating\|India Ratings\|IND AA\|A1\+` |
| Coupon rows | `[0-9]\.[0-9]{2}% (secured\|unsecured)? ?NCD` |

## Sweep sections (Step 8)
| Target | Pattern |
|---|---|
| Key Audit Matters / EoM | `Key Audit Matter\|Emphasis of Matter\|Material Uncertainty` |
| Contingent liabilities | `Contingent liabilit\|claims against the (Company\|Group) not acknowledged` |
| Capital commitments | `Capital (and other )?commitment\|estimated amount of contracts` |
| Related parties | `Related Party\|Form AOC-2\|arm.s length` |
| Exceptional items | `Exceptional item` |
| Guarantees | `corporate guarantee\|financial guarantee\|guarantees and collaterals` |
| Pledged shares | `pledge` |
| Leverage caps / net debt | `Net Debt\|net gearing\|leverage\|ND/EBITDA` |
| Segment note | `Segment Revenue\|Segment Results\|Operating Segments\|reportable segment` |
| Subsidiaries/JV list (Annexure II) | `subsidiar(y\|ies).{0,30}(joint venture\|associate)\|AOC-1` |
| Auditor & opinion | `INDEPENDENT AUDITOR\|unmodified\|qualified opinion` |
| Demergers/slump sales/one-offs | `demerger\|slump sale\|discontinued operation\|business transfer` |

## Sector-flavour landmarks
- **FMCG/consumer:** `excise duty` (ICRA OI is NET of excise — reconcile margins), `GST`, `market share`
- **Steel/commodities:** `per tonne\|/t \|EBITDA/t`, `capacity utilisation`, `captive`, `safeguard\|anti.?dumping\|Minimum Import Price`, `coking coal\|iron ore`
- **Banks:** `GNPA\|NNPA\|CET-?1\|CRAR\|CASA\|LCR\|slippage\|provision coverage`
- **NBFC:** `AUM\|Stage 3\|gearing\|RoMA\|credit cost`

## Small files (read END-TO-END, no map needed)
Quarterly decks (~5–8k words): summary slide first (net debt, leverage, guidance, corporate developments) — but still read whole deck.
Broker notes (~3–6k words): stance/TP, estimate tables, conference-call takeaways, capex/assumption tables — read whole note; VERIFY any company figure quoted against the company's own document before use.

---

## ⚠️ PICTURE-TEXT / CHART BLOCKS — the highest-risk extraction surface

Anything inside `<!-- Start of picture text --> … <!-- End of picture text -->` is **OCR of a
chart or infographic, with the layout destroyed**. Values and their labels arrive as two
separate runs, and **the value rows are in chart-stacking order while the legend is listed
bottom-up or top-down depending on the chart** — they are NOT positionally aligned.

**Never read a mix/share/segment percentage straight out of a picture-text block.**

| Trap | Pattern to find it | Mandatory handling |
|---|---|---|
| Stacked bar/column mix (segment, geography, product) | `SECTOR MIX\|PRODUCT MIX\|GEOGRAPHY MIX\|Revenue mix` | Map values→labels by **count and order**, then CORROBORATE against a second source before use |
| Series with N value-runs and N legend entries | `(\d+%<br>){3,}` followed by label list | Count the runs; if runs ≠ labels, the block is unreliable — mark TBC |
| Waterfall / bridge charts | `Net Debt\|bridge\|Gross Block` inside picture text | Prefer the AR's own narrative or table statement of the same figure |

**The free validator: A MIX MUST SUM TO 100%.** Always add the extracted shares up. A segment/geography/
product mix totalling 95% or 104% is **a mis-read, not "rounding in the source"** — treating a failed
sum as rounding is how a one-row mis-alignment survives review. Sum first, then trust.

**Worked failure (Happy Forgings, 11-Aug-2026 — caused a wrong figure to reach a delivered report):**
```
SECTOR MIX<br>14% 13% 16%<br>11% 10% 11%<br>32% 32% 32%<br>6% 6% 8%<br>37% 39% 33%<br>
FY2026 Q12026 Q12027<br>Industrials<br>Off-Highway<br>Farm Equipment<br>Passenger Vehicles<br>Commercial Vehicles
```
5 value-runs, 5 legend entries, **in the same order**: Industrials=14/13/16 … CV=**37**/39/33.
The report shipped CV=32% (the Farm row) — the row was mis-aligned by one. The company's own
broker note said "CV – 33% (39%)" for Q1FY27, which matches the 37/**39**/**33** run exactly and
would have caught it in one grep.

## The corroboration rule (binding — traced ≠ verified)

A figure being **traceable to a document is not the same as being verified.** Before any figure
enters a workpaper or report, ask: *does this number appear in a second document in this case
folder?* If yes, **grep for it and reconcile.** Cross-source corroboration is mandatory for:

| Figure class | Typical second source |
|---|---|
| Segment / geography / product mix % | broker notes (they restate the mix in clean text), MD&A narrative |
| Revenue, EBITDA, margin, PAT | quarterly deck trend table vs AR P&L vs broker results table |
| Debt, net debt, cash | AR borrowings note vs deck balance-sheet slide vs broker BS |
| Capacity, utilisation, volumes | deck capacity slide vs MD&A vs broker operational section |
| Order book, capex guidance | both broker notes (they quote the same management call) |

Where two sources disagree: **the company's own audited/filed document wins**, the divergence is
stated in the workpaper, and the broker figure is never silently preferred. Where a picture-text
block is the ONLY source for a figure, it is marked **"to be confirmed by issuer"** — never shipped
as a clean fact.

## Trend, not snapshot (Step 1b synthesis requirement)

The section map finds *sections*; it does not by itself find *trends*. For every business-mix,
capacity, margin and leverage metric, extract the **longest time series available**, not just the
latest column — the multi-year direction is frequently the rating driver, while the latest snapshot
is merely a data point. Decks carry these under:
`transformation\|journey\|CAGR\|FY2[0-9] ?(to|-|–) ?FY2[0-9]\|Historical Financial Performance\|Business Evolution`

*(Happy Forgings: the rising industrial-segment share was visible across the documents and was the
FIRST strength driver in the agency's own published rationale; the delivered report captured only
the single-year snapshot and never elevated the trend to a driver.)*
