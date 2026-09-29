# Rating review agents

Six project-scoped subagents that **audit a rating case step-by-step, find mistakes, and fix them**, with a head agent that confirms each one actually did its job. They review work already done (a delivered or in-progress case) — they do not replace the rating SOP, they check and correct it. All of them lean on the existing gate scripts (`preflight.py`, `tieout_mutation.py`, `annotate_scorecard.py`, `check_sections.py`, `step14_diff.py`, `delivery_audit.py`) rather than re-inventing the checks.

## The roster

| Agent | Covers (SOP) | Fixes? | Confirms with |
|---|---|---|---|
| `rating-intake` | Ph 1 · Steps 1-4 (pre-flight, docs, routing, peers) | yes | `preflight.py` |
| `rating-ratios` | Ph 2 · Steps 5-9 (extraction, tie-outs, coverage) | yes | `compute_ratios.py` + `tieout_mutation.py` |
| `rating-analysis` | Ph 3 · Steps 10-15 (methodology, liquidity, scorecard, Step-14) | yes | `annotate_scorecard.py` + `step14_diff.py` |
| `rating-draft` | Ph 4 · Steps 16-17a (the rationale) | yes | `check_sections.py` |
| `rating-reviewer` | Ph 5 · Step 17b (independent four-eyes) | no — finds & reports | re-runs every gate |
| `rating-chief` | Step 17c (head — orchestrates + verifies) | routes back | `delivery_audit.py` = READY |

## How to run

**Whole sweep (recommended):** from the main session, ask —
> Run the `rating-chief` sweep on `<slug>`.

The chief dispatches each phase agent in order, re-runs that phase's gate to confirm the fix landed, routes red gates back, then signs off only on `delivery_audit.py` = READY TO SHARE. (Run the chief at the top level: a subagent generally can't spawn its own subagents.)

**A single phase:** dispatch one agent directly, e.g.
> Use `rating-ratios` to review `<slug>`.

## Design notes

- **Phase granularity, not per-step.** One agent per group of steps (a phase) keeps each agent's context focused and avoids duplicating the scripts that already check individual steps.
- **Phase agents auto-fix**, then report what they changed with evidence. The `rating-reviewer` is deliberately read-only, so the four-eyes check stays independent of the agents that did the fixing.
- **"Worked properly" is evidence-based:** a phase is done only when its named script exits clean and its artifact exists — the chief re-runs the gate itself rather than trusting an agent's summary.
- **Model:** each agent inherits the session model. Set `model: opus` in the frontmatter of `rating-analysis`, `rating-reviewer` and `rating-chief` if you want the judgement-heavy roles on a stronger model.
