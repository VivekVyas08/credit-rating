# CareEdge guidance audit — 20 August 2026

**Scope.** Everything governing CareEdge output: `AGENCIES.md`, the CareEdge-relevant failure modes in `CLAUDE.md`, the 73-file `CareEdge/Methodology/` corpus, the 805-report `CareEdge/Report for Reference/` library, and the two mechanical gates (`preflight.py`, `check_sections.py`). Triggered by the HDFC Securities rationale, which was wrong on four structural points against CareEdge's press release of the same date.

**Method.** Empirical, not by inspection. Where a rule exists, I tested whether it *fires*.

---

## 1. The finding that matters

**Two CareEdge broking rationales were already in the reference library, published six weeks before my report, each containing every convention I got wrong. I opened neither.**

| | `Anand Rathi Share and Stock Brokers Limited_06 Jul 2026.md` | `Angel One Limited_03 Jul 2026.md` |
|---|---|---|
| Tangible net worth | ✓ | ✓ |
| Loan book (Margin Trading Facility) | ✓ | ✓ |
| Overall gearing* | ✓ | ✓ |
| Cost-to-income | ✓ | ✓ |
| Return on net worth (RONW) | ✓ | ✓ |
| Footnote `*including non-fund-based limits utilised` | ✓ | ✓ |
| Rating table stating a **limit** | ✓ (CP ₹200.00 crore) | ✓ |

Anand Rathi's Brief Financials table is row-for-row the template HDFC Securities needed:

```
|Total income|683|845|934|
|Profit after tax (PAT)|79|104|132|
|Tangible net worth (TNW)|385|495|1,342|
|Loan book (Margin Trading Facility)|617|686|1,102|
|Overall gearing* (x)|3.19|2.59|1.07|
|Cost-to-income (%)|79.99%|79.79%|76.69%|
|Return on net worth (RONW) (%)|24.80%|23.57%|14.35%|
A: Audited;  *including non-fund-based limits utilised
```

That single footnote — `*including non-fund-based limits utilised` — **is** CareEdge's gearing definition, the one whose absence produced 4.20x against a published 4.64x. **All four of failure modes 31–34 would have been prevented by opening either file.**

This is not a knowledge gap. It is a *lookup* that no step required.

---

## 2. Why the existing rule did not prevent it

`AGENCIES.md` item 3 already said:

> *Learn that agency's format from its own reference reports … Do NOT assume the format from memory.*

The rule existed, named the right files, and did not fire. Two reasons:

1. **It was scoped to "format".** Read naturally, that means section order and headings — which my report got *right*. The peer report also carries the row set, the ratio definitions and the amount convention, and nothing in the rule said so. A rule that is followed and still permits the error is mis-scoped, not merely ignored.
2. **It was prose.** No step, gate or script required a peer to be opened, and nothing recorded whether one had been.

This is the 13-Aug guidance audit's conclusion recurring exactly: *the deficiency is enforcement architecture, not content.*

---

## 3. Why a peer lookup is load-bearing for CareEdge specifically

CareEdge does not have one Brief Financials template. Of 631 reference reports carrying the table:

| Row-set family | Reports | of which 2025+ |
|---|---|---|
| **Corporate** (PBILDT-based) | 520 | 369 |
| **Financial-sector** (TNW-based) | 49 | 49 |
| **Bank** (NIM/GNPA-based) | 19 | 19 |
| Other / bespoke | 43 | 31 |

The row set **forks by entity type**, and the fork is precisely what a from-memory draft cannot know. Note the financial-sector family: **49 reports, every one from 2025 or later** — a recent, consistent, fully-represented template that I had in full and did not consult.

It also explains why failure mode 28 misfired. FM28 ("don't use another sector's metric set") was learned on an NBFC where cost-to-income was wrong. Generalised to broking it produced a *written justification* for omitting the right metrics. The question "is cost-to-income a broking metric?" is not answerable by reasoning from an adjacent sector — only by opening a CareEdge broking report, where it is row 6.

---

## 4. What changed

### 4.1 New mechanical check — `preflight.py` probe **[1b] PEER REPORTS — SAME AGENCY, SAME SECTOR**

Runs before any drafting. Matches the case's sector against the agency's reference library and prints, for the top three peers, **their Brief Financials row labels and their ratio footnotes**. On HDFC Securities it now emits:

```
[1b] PEER REPORTS - CAREEDGE, SAME SECTOR  (failure modes 32/33)
    * Anand Rathi Share and Stock Brokers Limited_06 Jul 2026.md   (score 12.2 on broking)
        Brief Financials rows THIS AGENCY USES IN THIS SECTOR:
          - Total income
          - Profit after tax (PAT)
          - Tangible net worth (TNW)
          - Loan book (Margin Trading Facility)
          - Overall gearing* (x)
          - Cost-to-income (%)
          - Return on net worth (RONW) (%)
        ratio footnote: *including non-fund-based limits utilised
    *** These rows are the REQUIRED set, and the footnotes are the agency's
        RATIO DEFINITIONS. Reproduce them. ***
```

**Matching is IDF-weighted**, which took three iterations to get right and is worth recording:

- *Raw token counts* ranked an **asset manager** top for a city-gas case, because "scheme" and "distribution" appear dozens of times there in an unrelated sense.
- *Distinct-token counts* ranked **Hindware Home Innovation** top for the same case.
- A **4-character minimum silently dropped "gas"** — the single most discriminating word available. Lowering it to 3 is the same lesson as the earlier name-token fix that had made SBI unsearchable.

With rarity weighting the results are correct across every live case:

| Case | Top peer found |
|---|---|
| HDFC Securities (broking) | Anand Rathi, Angel One |
| Gujarat Energy (city gas) | **Gujarat Gas Limited** — the same-issuer report, i.e. this probe also catches failure mode 29 |
| Riba Textiles | Riba's own report, Himatsingka Seide, Sutlej Textiles |
| NABKISAN (NBFC) | 360 One Wam, Bajaj Finance |

### 4.2 `AGENCIES.md` item 3 rewritten
From "learn the format" to a binding instruction naming the three things a peer answers — row set, ratio definitions (in the footnotes), and whether the header table states limits — and pointing at probe [1b].

### 4.3 `CareEdge/BROKING_CONVENTIONS.md`
Every CareEdge broking convention, verified to the rupee against the published figures: TNW build-up, gearing including non-fund-based, RONW on average TNW, ROTA, cost-to-income, the required row set, MTF framing, unencumbered-cash rule, and the mandatory regulatory section.

### 4.4 Five new gate probes (`check_sections.py`)
Rating table states limits not outstandings · no-outlook claim not contradicted · financial-sector net-worth basis stated · broking metric set complete · broking liquidity uses unencumbered cash.

All five were verified to **fire on the wrong version and pass on the corrected one**. Two false positives surfaced during testing and were fixed: JSW Steel (states a limit and merely annotates nil outstanding — correct behaviour) and the string "Financial Sector" matching a *criteria-document name* on a sugar and an FMCG report.

---

## 5. Enforcement position after this audit

| | Count |
|---|---|
| Named failure modes in `CLAUDE.md` | 37 |
| Carrying a mechanical check | **9** |
| Probes in `check_sections.py` | 16 |
| Probe sections in `preflight.py` | 4 |

9 of 37 is 24%, against 3 of 24 (12.5%) at the 13-Aug audit. The meaningful figure is different: **the last six failure modes added (29–34) are all mechanically enforced, six out of six.** The §8a meta-rule is holding for new material. The unenforced remainder is a **legacy backlog of modes 1–28**, written before that rule existed. Three of those have now been retro-fitted — see §9.

**That backlog is the honest residual risk of this audit.** I have not retro-fitted checks to 28 older modes, and I am not going to claim the CareEdge path is now safe because five new probes exist.

---

## 6. What this audit does *not* fix

Stated plainly, because an audit that only lists wins is not an audit.

1. ~~The peer probe surfaces but does not verify.~~ **Closed during this audit.** Probe [1b] now writes `peer_rows.json` into the case folder, and `check_sections.py` reads it back from the report's own directory and fails the report if the agency's row set is absent (matching each label on its stem *or* its parenthetical, so "Loan book (MTF)" satisfies "Loan book (Margin Trading Facility)"). Verified end-to-end: the corrected HSL rationale **passes**; the superseded v1 **fails**, naming exactly `Loan book (Margin Trading Facility); Overall gearing* (x); Cost-to-income (%)` and citing the peer it came from.
2. **Peer quality varies by sector, and the new check inherits that.** Running it across delivered work found real gaps — Gujarat Energy is missing CareEdge's `Total operating income` row (it says "revenue from operations"), and NABKISAN is missing `PAT`, `Tangible net worth`, `Overall gearing` and `RONW`. But NABKISAN's peer matched on the single token "nbfc" and resolved to a *bank* report, so part of that finding is peer-match imprecision rather than a defect in the rationale. **The check is only as good as the peer it selected — read the peer name before acting on a failure.** Broking, city gas and textiles match well. NABKISAN matches only on "nbfc" and returns generic NBFC names rather than an agri-lending peer. Where `case.json`'s `sector` string is vague, the probe degrades quietly — it prints *a* peer, not necessarily *the* peer.
3. **A rated limit still cannot be derived from issuer documents.** Probe [1b] finds a same-issuer or peer rationale when one exists; where none does, the amount is genuinely unavailable and must be marked "to be confirmed by issuer" — never substituted with an outstanding. That is now failure mode 31, but it is a rule, not a check.
4. **Wrong inferences — now partly caught, by a different mechanism.** Added after this audit: a **peer-norm check**. Probe [1b] measures what the agency actually *rates* in the sector (**9 of 14 CareEdge broking peers carry a long-term rating**) and persists it; the gate then fails any report that assigns no long-term rating without saying why. This does not evaluate reasoning — it detects that a *conclusion is unusual for the sector* and demands a justification, which catches novel errors nobody anticipated. Verified: v1-as-delivered (banner stripped) now fails six checks including this one; v2 passes; no false positives across the other delivered reports.

   Two traps found while building it, both of which would have made the check useless while looking like it worked: the peer cache is lower-cased, so a case-sensitive rating regex reported **0 of 14 against a true 9 of 15** — a check that always reads zero looks like evidence of conformity; and the "justified" pattern initially accepted the phrase *"no outlook is assigned"*, which on HSL **was the error, restated** — it would have waved through the very report it exists to catch.

5. **What still is not caught.** The root HDFC error — reasoning from drawn debt to the rated universe — was not a lookup failure but a logic failure. Probe [1b] would have caught its *consequences* (missing rows, wrong definitions). No regex catches the reasoning itself.
5. **`preflight.py` now costs 5–8 seconds per run** (up from under 1s) because it reads 805 reference files. Acceptable for a once-per-case gate; worth caching if the library grows much further.

---

## 7. Verification

- `python preflight.py --selftest` → passes (7 word-boundary + 4 token-derivation cases).
- Probe [1b] returns correct peers on all four live cases tested; every case in `Companies/` still runs.
- `python check_sections.py` across the corpus → 12 pass, 2 pre-existing mandatory-section failures, unchanged by this work; failure modes 31–34 now fire nowhere except where genuinely warranted.
- The rebuilt HDFC Securities rationale passes the gate with all quality probes clean, and its engine reproduces **17 of 17** CareEdge published figures.


---

## 8. Addendum — two defects found *by* this audit

Recorded because an audit that introduces bugs silently is worse than none.

1. **The peer probe was inert for every ICRA case.** It built its reference path as `ROOT/<agency>/Report for Reference`, but ICRA's library sits at the *root*, not under an `ICRA/` folder — and `AGENCY_DIRS` at the top of `preflight.py` already held the correct mapping. It appeared to work because CRISIL and CareEdge happen to match the constructed shape. Now uses `AGENCY_DIRS`.
2. **The row extractor only knew CareEdge's table name.** CRISIL and ICRA call it *Key Financial Indicators*, so the check was silently doing nothing for them. Now matches all three, and filters header/basis cells (`Standalone`, `FY2024`, stray `<br>` markup) that were leaking in as if they were metrics.

Both were found by running the probe across all 19 cases rather than only the one that prompted the audit.


---

## 9. Legacy backlog — first three retro-fitted

The backlog was triaged on two criteria: *has it actually recurred*, and *is it mechanically decidable*. Three qualified; the rest are recorded honestly below as not yet tractable.

**FM12 / FM23 — Annexure I lines must sum to their total.** The strongest of the three, because an invented or mis-split facility line is invisible to every other check: the prose reads correctly and only the arithmetic is wrong. I verified this by hand for HDFC Securities (13,860.00 + 6,140.00 = 20,000.00; 2,250.00 + 750.00 = 3,000.00), and hand-arithmetic is exactly what should not be manual. The probe walks the annexure and compares every row labelled *total* against the component rows beneath it.

Tested in **both** directions, because a check that never fires is worse than none:

| Input | Result |
|---|---|
| Correct report | no breaks — and **6 rows were genuinely parsed**, so it is checking, not skipping |
| One line altered 13,860.00 → 12,860.00 | caught: *"total rated" states 20,000.00 but its 2 lines sum to 19,000.00* |
| Total altered 3,000.00 → 3,500.00 | caught: *"states 3,500.00 but its 2 lines sum to 3,000.00* |

FM23 needs no separate probe — a header total overstating the facilities beneath it is the same arithmetic break seen from the other end.

**FM14 — a CRA-published amount must carry that publication's date.** This directly guards condition (2) of the five-condition amendment, on which every CareEdge rated amount now depends. An undated CRA table cannot be distinguished from a stale one. Passes the dated HSL v2, fails the same report with its dates stripped, and stays silent on reports that cite no CRA publication at all.

Neither probe produces a false positive anywhere in the corpus; totals remain 12 pass / 2 pre-existing mandatory-section failures.

### Not retro-fitted, and why

| Mode | Why it resists a mechanical check |
|---|---|
| FM3 carried ratios, FM16 snapshot-instead-of-trend, FM22 resolving-vs-live risk | Require judgement about what the *right* analysis was, not a decidable property of the text |
| FM7 number drift during writing | Decidable in principle by diffing the report against the workbook, but the mapping from prose figures to workbook cells is fuzzy; a naive version would flag every legitimately quoted peer or published figure |
| FM1, FM11, FM15 provenance of a figure | The text does not record where a number came from, so nothing in the artefact can be checked. Fixable only by changing what the workpaper stores, not by adding a probe |
| FM5, FM6, FM9 omissions and unread documents | Absence of something never specified; the closest existing proxy is the section gate |

That leaves the honest position: **9 of 37 enforced, the six most recent all enforced, three legacy modes retro-fitted, and roughly a dozen that are genuinely judgement-bound rather than merely unbuilt.**
