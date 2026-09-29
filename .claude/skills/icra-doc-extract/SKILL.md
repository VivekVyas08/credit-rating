---
name: icra-doc-extract
description: Token-efficient extraction from company documents (annual reports, quarterly decks, broker notes) for rating/research work. Use at Step 1b/5/7b/8 of the ICRA SOP — builds a section map with grep, then reads every credit-material section via targeted offset reads instead of paging the whole file. Triggers - "extract from the annual report", "build the section map", "read the documents efficiently".
---

# Document extraction playbook (comprehensive coverage, minimum tokens)

Purpose: satisfy Step 1b's "read every credit-material section" standard at the lowest token cost. This is NOT permission to skip content — it is the method for covering ALL of it efficiently: **locate → read the section → log it**, instead of paging sequentially through 300k-word files.

## Method (binding order)

1. **Size every file first** (`wc -w`) and plan: small files (< ~15k words: quarterly decks, broker notes, prior reports, term sheets) are read **end-to-end**; large files (annual reports) are covered **section-by-section via the map below**.
2. **Build the section map with one grep pass per landmark group** (patterns in `PATTERNS.md` — read it now). Record line numbers.
3. **Read each mapped section** with offset/limit around the hit (statements ±120 lines; notes ±40). Never conclude from a truncated page — if the Read is cut off, continue from the next offset.
4. **Log every file and every section covered** in the workpaper's Document Read Log as you go.
5. **The completeness gate:** the map must cover, for each annual report — both financial statements (standalone + consolidated) · auditor's report + Key Audit Matters + Emphasis of Matter · contingent liabilities & capital commitments · borrowings/NCD/instrument notes + ISINs + CP status + credit-rating note · segment note · related-party note · exceptional items · MD&A / directors' report (credit-relevant parts) · leverage-cap / net-debt disclosures · pledged shareholding · **the subsidiary/JV/associate list with each entity's FULL LEGAL NAME and % holding (grep `AOC-1`, `wholly owned subsidiary`, `subsidiar(y|ies)`)**. A section with no grep hit is confirmed absent by a second, looser pattern before being marked n/a.
   - **Naming is not a materiality question.** An entity that is immaterial in size is still NAMED in the Annexure-II / entities-consolidated table. Deciding "immaterial, skip it" is an analytical-treatment decision; it never licenses omitting the name. *(Happy Forgings: the delivered report said only "subsidiary, immaterial" — `M/s HFL Technologies Private Limited` and a full FORM AOC-1 table were both sitting in the AR, and the agency's own rationale named and consolidated it.)*
6. **The corroboration gate (binding — run BEFORE any figure leaves this skill).** Traceable ≠ verified. For every figure heading into the workpaper, ask whether it appears in a second document in the case folder; if it does, grep it and reconcile. Mandatory for: mix/share percentages · revenue/EBITDA/margin/PAT · debt/net debt/cash · capacity, utilisation, volumes · order book and capex guidance. Company's own audited/filed document wins any disagreement, and the divergence is written down. **Anything whose only source is a `picture text` block is marked "to be confirmed by issuer", never shipped as clean fact** — see the worked failure in `PATTERNS.md`.
7. **Trend, not snapshot.** This method finds sections, not trends. For every business-mix, capacity, margin and leverage metric, pull the **longest time series the documents support** and record the multi-year direction alongside the latest value — the direction is frequently the rating driver while the snapshot is just a data point.

## Why this exists (token economics)

A JSW-sized annual report is ~430k tokens; three of them exceed the context window. Sequential reading is impossible AND unnecessary — the credit-material sections are ~10–15% of the file. The section map covers 100% of what Step 1b requires at roughly a tenth of the tokens, and the grep hits double as source citations for the Response Protocol (CLAUDE.md §10).
