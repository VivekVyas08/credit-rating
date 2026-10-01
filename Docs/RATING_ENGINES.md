# Three ways to get a rating outcome

`rate_engine.py` produces a rating outcome by two independent routes and reports the gap
between them. Both remain available; neither replaces the other.

```bash
python tools/rate_engine.py <case-slug>                    # both engines (default)
python tools/rate_engine.py <case-slug> --engine local     # deterministic only, no key needed
python tools/rate_engine.py <case-slug> --engine api       # model only
python tools/rate_engine.py <case-slug> --engine ollama     # OFFLINE model view (local model + scorecard)
python tools/rate_engine.py <case-slug> --engine ollama --ollama-model qwen2.5:14b
python tools/rate_engine.py --list-models                  # API models + locally-pulled Ollama models
```

| | **local** | **api** |
|---|---|---|
| What it is | the filled `Rating_Scorecard` workbook, evaluated offline through its own Inputs → Ratios → Scorecard → Rating formula chain | Claude, via the Anthropic Messages API, on a model you select |
| Needs a key | no | yes |
| Reproducible | byte-identical every run | no — a judgement, not a computation |
| Sees | ratios only | ratios, disclosed conventions, and which inputs are unverified |
| Good at | auditability; the thing you show a committee | business position, cyclicality, headroom — what a ratio grid cannot see |
| Blind to | everything qualitative | nothing it is told, but it is told only what the engine computed |

Divergence between the two is a **finding to resolve, not a number to average**. The scorecard
is a zero-biased screening band documented to under-rate the AA+/AAA range; the model weighs
factors the grid has no column for. Read both.

## The third route: `1234`

Entering **1234** as the API key does not call the Anthropic API. It hands the job to a local
**Claude Code agent** running in this project directory:

```bash
python tools/rate_engine.py --pending --api-key 1234            # work the request queue
python tools/rate_engine.py --pending --api-key 1234 --dry-run  # show the command, run nothing
python tools/rate_engine.py <slug> --engine agent --yes         # review one case, no prompt
```

Why this is worth having: the **api** engine sees only the computed ratio table — it cannot
read a document, build an engine, or run a gate. The **agent** inherits CLAUDE.md (the 19-step
SOP and every failure mode), the project skills, and read/write access to the case folders, so
it can process a pending request *end to end*.

### Two things it is not

**It does not connect to an existing Claude Code conversation.** There is no inbound channel
into a running session — a session only advances when its user sends a message, and no script
can inject a turn into one or read its reply. `1234` starts a *new* agent that shares the
project (same CLAUDE.md, same skills, same files), not the chat you are reading.

**It does not bypass authentication.** The spawned agent needs its own credential exactly as
the API route does. Verified 29-Aug-2026: with an expired login it returns
`Failed to authenticate: OAuth session expired and could not be refreshed`. The sentinel
chooses *which engine does the work*; it does not create credentials.

`1234` is a routing sentinel, not a secret — it is never transmitted anywhere. The constant
`AGENT_SENTINEL` at the top of `rate_engine.py` changes it. Because the agent writes files and
consumes usage, it asks before starting unless you pass `--yes`, and `--dry-run` prints the
exact command and prompt without running anything.

## The hard guardrail

**The API engine never sees the source documents.** It receives the ratio engine's verified
computed output and is never asked to extract a figure.

This is deliberate. Every material error in this project's history has been an *extraction*
error — a forex line taken from the cash-flow statement instead of the P&L note, a provision
misread by a factor of ten, a subtotal typed rather than summed. Those are caught by tie-outs
and mutation coverage. Handing documents to a language model would reintroduce precisely the
failure class the tie-outs exist to close, and would do it in the one place no tie-out can
reach. So the division of labour is strict:

- **the engine establishes what is true** — and must fully reconcile before anything runs;
- **the model decides what it means.**

Concretely:

1. **Tie-outs must all pass first.** If any fails, the tool aborts with exit 1 and produces no
   outcome by either route. A rating computed off a failing engine is worse than no rating.
2. The model is given the computed suite, the `DISCLOSED_DIFFERENCES`, **and** the
   `UNVERIFIED_INPUTS` list, so it can weigh how well-evidenced each number is instead of
   assuming they are all equally solid.
3. The response is schema-constrained (`output_config.format`) to a rating *view* — grade,
   outlook, strengths, weaknesses, monitorable, confidence. It cannot return a financial figure.

## Supplying the key

In order of preference:

```bash
python tools/rate_engine.py --set-key      # enter it once, hidden input, stored for later runs
python tools/rate_engine.py --show-key     # which credential is in use, and where it lives
python tools/rate_engine.py --clear-key    # delete it
```

`--set-key` is the normal way in. It prompts with the input masked and writes the key to your
**home directory**, not to this project folder — the folder travels (the rating reports in it
are the deliverable), and a credential that travels with the deliverable is a credential that
leaks. On Windows the file is protected by your user profile's NTFS permissions rather than the
`0600` mode the code requests, and `--set-key` says so when it stores one.

A run that needs a credential and finds none will **ask** for it, rather than failing with
instructions. Entering `1234` at that prompt selects the agent route instead of the API.

Other ways in, in resolution order (highest first):

```bash
python tools/rate_engine.py <slug> --api-key-file ~/.anthropic_key   # good: scriptable
export ANTHROPIC_API_KEY=...                                   # good: per-shell, outranks the store
python tools/rate_engine.py <slug> --api-key ...                     # worst: lands in shell history
```

The key is never printed, never logged, and never written to `--json` output — only a masked
fingerprint (`sk-ant-…abcd (108 chars)`) so you can tell which credential was used. Common key
filenames are in `.gitignore`. With no credential at all the tool still runs the local engine
and reports the API engine as unavailable with instructions.

## Model selection

The API model list lives in `tools/models.json` (edit there to add/rename a model or change a
label - the CLI `--model` and the web Settings dropdown both read it; current default
`claude-opus-5-5`). `--effort low|medium|high|xhigh|max` (default `high`) trades cost against
depth. Haiku is listed for screening runs and bulk re-checks; it is not a model to take a
rating view from. `python tools/rate_engine.py --list-models` prints the live list.

## Offline model view (`--engine ollama`)

The **ollama** engine is the `api` engine's offline twin: the SAME prompt and SCHEMA, sent to a
model running locally under [Ollama](https://ollama.com) instead of the Anthropic API. No key,
no internet, nothing leaves the machine. `--engine ollama` runs it **alongside the local
scorecard**, so an offline run still shows two independent views and their divergence - the
offline equivalent of `--engine both`.

```bash
ollama serve                              # if not already running
ollama pull qwen2.5:14b                   # one-time (several GB); offline thereafter
python tools/rate_engine.py <slug> --engine ollama --ollama-model qwen2.5:14b
```

- `--ollama-model` (or `$OLLAMA_MODEL`) picks the model; `--ollama-url` (or `$OLLAMA_HOST`)
  points at a non-default server. `--list-models` shows which models are pulled.
- Structured output is enforced via Ollama's `format` = the rating SCHEMA, so the reply is the
  same object shape as the API engine's; a model that returns malformed or incomplete JSON is
  reported unavailable rather than shipped.
- The hard guardrail below binds it identically: it is handed the verified computed ratios,
  never the source documents, and the schema admits no financial figure.
- Determinism caveat: `temperature` is 0, but a local model is not byte-reproducible the way the
  scorecard is. Treat its view as judgement, like the API engine's - an input to the committee,
  never the rating itself.

## Example

```
RATING OUTCOME - Jindal Stainless Limited
agency        : CareEdge
tie-outs      : 39/39 reconcile
credential    : environment variable ANTHROPIC_API_KEY (resolved by the SDK)
model         : claude-opus-5 (effort high)

LOCAL  (deterministic scorecard, offline)
       grade      : AA
API    (claude-opus-5, effort high)
       grade      : AA (Stable)
       short term : A1+
       confidence : high

DIVERGENCE
  none - both routes return AA independently.
  house form: CARE AA (Stable) / A1+

Neither engine is the rating. Both are inputs to a committee decision.
```

`--json <path>` writes the whole result, including the model's full reasoning and token usage,
for the workpaper.

## Testing

Two layers, because a fake key can only reach one of them.

**1. Live, with a deliberately invalid key** - exercises key resolution, masking, transport,
and authentication handling against the real endpoint:

```bash
printf 'sk-ant-api03-FAKE-TEST-KEY-NOT-REAL-000...' > /tmp/dummy.key
python tools/rate_engine.py jindal-stainless --engine both --api-key-file /tmp/dummy.key
```

Expected: the local engine still returns its grade, and the API engine reports
`authentication failed - the credential was rejected`. A traceback here is a bug.

**2. Stubbed, for everything a rejected key cannot reach** - request shape, response parsing,
schema conformance, refusal and malformed-response branches, notch arithmetic, key hygiene:

```bash
python tools/test_rate_engine.py        # 33 checks, no network
```

The request-shape test includes the guardrail assertion: it fails if any source-document text
reaches the prompt.

### A bug this testing found

Running the live test surfaced a genuine defect that had nothing to do with the API. Both
`rate_engine.py` and `tieout_mutation.py` loaded the case engine through
`importlib.spec_from_file_location`, which happily serves a cached `.pyc`. The tool reported
`38/39 tie-outs reconcile` from bytecode compiled during an earlier guardrail test, in which a
PAT figure had been deliberately corrupted - while `python compute_ratios.py` on the same file
printed `39/39`. **A rating tool that can run against a version of the engine that no longer
exists is unusable.** Both loaders now compile from source on every call and never consult
`__pycache__`; a control writes a change, confirms the loader sees it immediately, restores,
and confirms again.


---

# Working without Claude at all

Only `rate_engine.py` and its test import `anthropic`. Everything else — `preflight.py`,
`compute_ratios.py`, `build_spreads.py`, `build_model.py`, `fill_scorecard.py`,
`tieout_mutation.py`, `check_sections.py`, `verify_*.py`, `build_rationale.py` — is plain
Python. Verified with both credential variables stripped from the environment: the local
engine returned its grade on 39/39 tie-outs.

| | Tier 1: no Claude | Tier 2: API key | Tier 3: Claude Code |
|---|---|---|---|
| Needs | Python + openpyxl + formulas | + an Anthropic key (cents per rating) | + Claude Code installed |
| Pre-flight document scan | yes | yes | yes |
| Ratio engine + tie-outs | yes | yes | yes |
| Mutation coverage | yes | yes | yes |
| Spreads / model / scorecard | yes | yes | yes |
| Delivery gate | yes | yes | yes |
| Anchor grade | yes | yes | yes |
| **Numbered rationale draft** | **yes**, on engines meeting the contract (see below) | same | same |
| Reasoned rating view | no | yes | yes |
| Extraction + full drafting | no | no | yes |

## Which cases the shared tools can drive

`rate_engine.py`, `tieout_mutation.py` and `build_rationale.py` all drive a case's engine
through one small contract — `YEARS`, `compute()`, `tieouts(R)` (see `engine_contract.py`).

**Audited 29-Aug-2026: only 3 of 21 engines meet it** — `balkrishna-industries-ltd`,
`jindal-stainless`, `repco-home-finance-limited`. Six expose `compute()` but no `tieouts()`;
twelve predate the contract and are written as top-level scripts around a `run()` function.
Those 18 still work perfectly on their own (`python compute_ratios.py`); they just cannot be
driven programmatically.

The tools now **refuse those cases with a one-paragraph explanation** naming what the engine
lacks, what it does expose, and which file to copy as the reference shape. Before the audit
they crashed with a bare `AttributeError`. To bring a case in scope, refactor its engine to
expose `compute()` and `tieouts()`.

## `build_rationale.py` — the Tier 1 draft generator

```bash
python tools/build_rationale.py <case-slug> [--out PATH] [--agency ICRA|CRISIL|CareEdge]
```

Fills everything **derivable** from the verified engine: the full key-financial-indicators
table in the agency's own row naming, the disclosed conventions, the inputs no tie-out covers,
and every mandatory section header so the structural gate is satisfied. Row names are read
from whatever `compute()` returns rather than hard-coded — an ICRA engine yields OPBDITA rows
and a CareEdge engine yields PBILDT rows, and inventing a name the engine does not produce is
how a template starts lying.

Every **judgement** is emitted as an explicit placeholder saying what is needed and which
figures bear on it:

```
[ANALYST: the rating narrative. Answer in order: why this rating level (2-3 structural
anchors, each with its most-defining number from the table below); what changed this
period; what could go wrong, each risk quantified against its buffer; ...]
```

**It refuses to run on a broken engine.** If any tie-out fails, it exits 1 rather than
producing a document — a formatted report built on figures that do not tie is more dangerous
than no report, because it looks finished. `--force` overrides, knowingly.

**The placeholders are binding, not decorative.** `check_sections.py` fails any report still
containing `[ANALYST: ...]`, so the skeleton cannot be shipped by mistake. While a draft is
unfilled the gate reports that one reason only — an unfilled draft otherwise trips half a
dozen probes on the *guidance text inside its own placeholders*, which buries the thing the
author needs to read. Once filled, the placeholder probe releases and the real quality probes
take over: absence claims, liquidity descriptor, rated-amount treatment.

### What it cannot do

Populate `compute_ratios.py` for a new company. Extraction — reading an annual report and
deciding which line belongs where — is the judgement-heavy half of this work and the half a
template cannot reach. For a Tier 1 user this tool is a rigorous assistant, not an analyst:
it verifies, computes and formats; a human still reads the documents.
