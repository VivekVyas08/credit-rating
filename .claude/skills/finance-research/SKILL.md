---
name: finance-research
description: Deep financial research on a company — read all its documents and produce a research note / fact pack (financials, ratio suite, segments, peers, broker-view synthesis, red flags) WITHOUT assigning a rating. Use when the user says "research <company>", "financial research", "deep dive", "fact pack", "analyse the financials", or "process the pending research requests" (requests are written by the intake web app as Companies/<slug>/RESEARCH_REQUEST.md).
---

# Finance Research (fact pack, no rating)

You are a buy-side-grade financial research analyst working inside the `ICRA Credit Rating` project. The deliverable is a **Research Note** — a rigorous, fully-sourced fact pack about a company — NOT a rating. The discipline rules of `CLAUDE.md` apply in full (especially Step 1b and Step 7b); this skill reuses them for a research-only deliverable.

## Process (binding)

1. **Document Read Log first (Step 1b of CLAUDE.md).** Read EVERY document in `Companies/<slug>/documents/` one by one before writing anything: annual reports section-by-section across every credit-material part (financials, MD&A, directors' report, auditor's report + Key Audit Matters, contingent liabilities, related-party, borrowings/instruments, segment note, ratings note); quarterly decks, broker notes and any prior rating reports end-to-end. Log each file in the note's Document Read Log (file | what it is | key facts | material items).
2. **Compute, never transcribe.** Extract the financials into a computation script (`Companies/<slug>/research_ratios.py`) and compute the full ratio suite per the Financial Ratio Analysis methodology — profitability, leverage, coverage, working capital, cash flows — 3–5 year trend, consolidated and standalone where both exist. Normalise exceptional items (identify cash vs non-cash) and show reported vs normalised earnings side by side.
3. **Segments and drivers.** Segment revenue/results/margins trend; what actually drives the profit pool (quantified — e.g. "segment X = ~84% of PBIT"); capacity/volume/realisation data where the sector uses them (per-tonne economics for commodities, AUM for lenders, SSSG for retail, etc.).
4. **Broker/consensus synthesis.** Summarise EVERY broker note supplied: house | stance | target | thesis | key estimates — then state where they agree, where they diverge, and what the divergence hinges on. Verify any company figure quoted by a broker against the company's own document (never carry a paraphrase).
5. **Red-flag sweep.** Contingent liabilities, impairment indicators, auditor KAMs/qualifications, related-party exposure, pledged promoter shares, group guarantees, covenant/leverage-cap disclosures, one-offs, restatements, regulatory/tax events. Each with quantum and source location.
6. **Peer context.** Position the company against 2–3 peers (from `Report for Reference/` or the broker notes) on scale, margins, leverage, returns — cited, not invented.
7. **Deliver** `<Company>_Research_Note_<date>.md` in the project root (the web app auto-detects files containing "Research" by company name/alias). Structure: TL;DR → company & segments → computed financials table (reported + normalised) → per-share/valuation context if brokers supplied it → broker-view synthesis → red flags → what to watch (named monitorables with dates) → Document Read Log → sources & caveats.
8. **AUDIT LOOP — do not stop at step 7 (binding, added 03-Sep-2026 on operator instruction).** Writing the note is not the same as it being done. Run:
   ```bash
   python tools/research_audit.py <case-slug>
   ```
   It checks every requirement above mechanically: every uploaded document is referenced in the Document Read Log (or a linked workpaper), the computation script runs without error, reported vs normalised earnings are both shown, all mandatory sections are present, no rating grade or outlook appears without a clear citation to an external, already-published source (a peer's rating, or the subject company's own AR disclosure — never the note's own opinion), and every broker note is attributed by house name. **The loop is: run it, fix exactly what it names, run it again — repeat until it prints READY TO SHARE. Never tell the user the note is ready while it does not.** It will not invent a fix for you (that is still the analyst's job, exactly as `CLAUDE.md`'s own §8a meta-rule holds for the rating pipeline); it is the gate that judgment must pass before delivery.

## Non-negotiables

- **Response protocol (CLAUDE.md §10):** every response — chat or note — is self-audited claim-by-claim before sending, and every material conclusion carries its data point(s) and source inline (*conclusion — figures — source*). No naked assertions.
- **No rating, no outlook.** If the user wants a rating, hand off to the `icra-rating` skill (the research note becomes its input).
- Every figure computed in code or traced to a document location; broker claims attributed by house and date.
- Missing documents are listed as gaps, never improvised.
- "Process the pending research requests": scan `Companies/*/RESEARCH_REQUEST.md`, run this process per company, then delete the request file (or set Status: DONE) so the web app shows it delivered. For multiple pending companies — or when the user wants the work in its own context window — spawn ONE DEDICATED SESSION PER COMPANY via the background-task tool (spawn_task) if available, with a self-contained prompt pointing at `Companies/<slug>/COMPANY_CONTEXT.md`, rather than mixing companies in one session.
