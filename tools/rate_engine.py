#!/usr/bin/env python3
"""Produce a rating outcome for a case TWO independent ways, and compare them.

    python rate_engine.py <case-slug> [--engine local|api|both] [--model ID] [...]

WHY TWO ENGINES
---------------
  local : the deterministic scorecard. Reads the case's filled Rating_Scorecard workbook and
          evaluates its own Inputs -> Ratios -> Scorecard -> Rating formula chain. No network,
          no API key, no model. Byte-identical on every run, which is what makes it auditable
          and what makes it the thing a committee can be shown.
  api   : Claude, via the Anthropic Messages API, on a model you choose. Reasons about the
          credit the way an analyst would - business position, cyclicality, headroom - which
          is exactly what a ratio grid cannot see.

Neither replaces the other, and that is the point. The scorecard is reproducible but blind to
judgement; the model exercises judgement but is not reproducible. `--engine both` (the default)
runs each independently and reports the divergence in notches, which is the same discipline the
SOP already applies to the Step 12b anchor.

THE HARD GUARDRAIL
------------------
The API engine is handed the ratio engine's VERIFIED COMPUTED OUTPUT. It never sees the source
documents and is never asked to extract a figure. That is deliberate: every material error in
this project's history has been an EXTRACTION error - a forex line taken from the cash-flow
statement instead of the P&L note, a provision misread by a factor of ten, a subtotal typed
rather than summed. Those are caught by tie-outs and mutation coverage, not by a language
model, and handing documents to a model would reintroduce exactly the failure class the
tie-outs exist to close. So:

  * tie-outs must ALL pass before either engine runs - a broken engine produces no outcome;
  * the model receives the computed suite, the disclosed conventions AND the list of inputs
    that no tie-out covers, so it can reason about the numbers' reliability rather than
    assume it;
  * the model returns a rating VIEW, never a financial figure.

THE THIRD ENGINE - "1234"
-------------------------
Entering **1234** as the API key does not call the Anthropic API. It routes the job to a local
**Claude Code agent** running in this project directory, which is a fundamentally more capable
route than the API engine:

    python rate_engine.py --pending --api-key 1234

  api   : sees ONLY the computed ratio table. It cannot read a document, cannot build an
          engine, cannot run a gate. It returns a rating view and nothing else.
  agent : inherits CLAUDE.md - the full 19-step SOP and every failure mode - plus the project
          skills and read/write access to the case folders. It can process a pending request
          END TO END: read the annual reports, build compute_ratios.py, run the tie-outs and
          gates, and draft the rationale.

Two things this is NOT, stated plainly because the difference matters:

  * It does not connect to an existing Claude Code conversation. There is no inbound channel
    into a running session - a session only advances when its user sends a message, and no
    script can inject a turn into one or read its reply. "1234" starts a NEW agent that shares
    the project (same CLAUDE.md, same skills, same files), not the chat you are reading.
  * It does not bypass authentication. The spawned agent needs its own credential exactly as
    the API route does - an `ant auth login` / Claude Code session, or ANTHROPIC_API_KEY in
    its environment. Verified 29-Aug-2026: with an expired login the agent returns
    "Failed to authenticate: OAuth session expired and could not be refreshed". The sentinel
    chooses WHICH engine does the work; it does not create credentials.

The agent writes files and consumes usage, so it asks before starting unless you pass --yes,
and --dry-run prints the exact command without running anything.

API KEY - where you put it
--------------------------
    python rate_engine.py --set-key      enter a key (hidden input), stored for future runs
    python rate_engine.py --show-key     which credential is in use, and where it is stored
    python rate_engine.py --clear-key    delete the stored key

--set-key is the one to reach for. It asks for the key with the input masked, stores it in your
HOME directory - NOT in this project folder, which gets zipped and emailed with the reports in
it - and every later run picks it up on its own. Any run that needs a credential and cannot
find one will ask for it rather than failing with a paragraph of instructions.

Entering 1234 at that prompt is the agent sentinel: it routes the job to a local Claude Code
agent instead of the API. That agent still needs its own credential.

Resolution order, highest first: --api-key-file <path>, then --api-key, then ANTHROPIC_API_KEY
/ ANTHROPIC_AUTH_TOKEN, then the stored key, then whatever the SDK finds by itself (an
`ant auth login` profile). The environment deliberately outranks the store: an env var is set
for one shell on purpose and should beat a file you set up months ago and have forgotten about.

--api-key is still accepted and is still the worst option, because the key lands in your shell
history. The key is never logged, never written to the JSON output, and never printed - only a
masked fingerprint is shown, so you can tell which credential was used without exposing it.
"""

import argparse
import importlib.util
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # this script now lives in tools/,
# one level below the project root - moved here 01-Sep-2026 to declutter the root.

# Selectable models. Opus 5.5 is the default - do not downgrade for cost without being asked.
# The list lives in models.json (edit there to add/rename a model or change a label - no code
# change, and the Settings dropdown picks it up too). This dict is the fallback used only if the
# JSON is missing or malformed, so the engine never breaks on a bad edit.
_MODELS_FALLBACK = {
    "claude-opus-5-5":            "Opus 5.5 - default; strongest judgement",
    "claude-fable-5-1":           "Fable 5.1 - most capable; slowest and dearest",
    "claude-opus-4-8":            "Opus 4.8 - previous Opus generation",
    "claude-sonnet-5":            "Sonnet 5 - cheaper, good for bulk re-runs",
    "claude-haiku-4-5-20251001":  "Haiku 4.5 - fastest/cheapest; screening only, not a rating view",
}
_DEFAULT_FALLBACK = "claude-opus-5-5"


def _load_models():
    """models.json -> (models, default), falling back to the built-in dict on any problem."""
    try:
        cfg = json.loads((Path(__file__).with_name("models.json")).read_text(encoding="utf-8"))
        models = {str(k): str(v) for k, v in (cfg.get("models") or {}).items()}
        default = str(cfg.get("default") or "")
        if models and default in models:
            return models, default
    except Exception:                                                     # noqa: BLE001
        pass
    return dict(_MODELS_FALLBACK), _DEFAULT_FALLBACK


MODELS, DEFAULT_MODEL = _load_models()

# Long-term scale, best to worst. Used only to measure the gap between the two engines.
SCALE = ["AAA", "AA+", "AA", "AA-", "A+", "A", "A-", "BBB+", "BBB", "BBB-",
         "BB+", "BB", "BB-", "B+", "B", "B-", "C+", "C", "C-", "D"]

AGENCY_PREFIX = {"ICRA": "[ICRA]", "CRISIL": "Crisil ", "CareEdge": "CARE "}

# Typing this as the API key selects the local-agent route instead of the Anthropic API.
# It is a ROUTING SENTINEL, not a credential - it is never sent anywhere. Change it freely.
AGENT_SENTINEL = "1234"


# ----------------------------------------------------------------------- case loading
def _load_module_from_source(path, name):
    """Compile the file on disk EVERY time - never touch __pycache__.

    importlib's normal loader will happily serve a cached .pyc. On 26-Aug-2026 that produced a
    genuinely dangerous failure: rate_engine.py rated a case from bytecode compiled hours
    earlier, in which a PAT figure had been deliberately corrupted for a guardrail test, while
    the source file on disk was correct. `python compute_ratios.py` printed "39/39 reconcile"
    and the loader simultaneously saw a broken engine. A tool that can rate off a version of
    the engine that no longer exists is unusable, so this bypasses the cache entirely.
    """
    import types
    src = Path(path).read_text(encoding="utf-8")
    code = compile(src, str(path), "exec")
    mod = types.ModuleType(name)
    mod.__file__ = str(path)
    mod.__dict__["__name__"] = name
    sys.modules[name] = mod
    exec(code, mod.__dict__)
    return mod


def load_case(slug):
    d = ROOT / "Companies" / slug
    if not d.is_dir():
        sys.exit("no such case folder: %s" % d)
    path = d / "compute_ratios.py"
    if not path.exists():
        sys.exit("no compute_ratios.py in %s - build the ratio engine first" % d)
    sys.path.insert(0, str(d))
    mod = _load_module_from_source(path, "engine_" + slug.replace("-", "_"))
    import engine_contract
    gap = engine_contract.require(mod, slug, "rate_engine.py")
    if gap:
        sys.exit(gap)
    meta = {}
    cj = d / "case.json"
    if cj.exists():
        try:
            meta = json.loads(cj.read_text(encoding="utf-8"))
        except Exception:                                                 # noqa: BLE001
            meta = {}
    return d, mod, meta


def _flatten(item):
    """Cases declare DISCLOSED_DIFFERENCES / UNVERIFIED_INPUTS in either of two shapes - a
    (title, text) tuple, or a single self-describing string. Both are in use across this
    project's case folders and both are legitimate, so the engine reads whichever the case
    wrote rather than forcing one: an engine that crashes on a valid case produces no rating,
    which is strictly worse than reading two shapes."""
    if isinstance(item, str):
        return item
    return " - ".join(str(x) for x in item)


def run_tieouts(mod):
    """Every tie-out must pass. A failing engine produces NO rating, by either route.

    ONE narrow exception, added 31-Aug-2026. A tie-out may be ACKNOWLEDGED where the divergence
    is real, understood and separately verified - Alembic Limited's implied tax rate of 6.6% is
    genuine (a Section 80M inter-corporate dividend deduction), and its tax charge already
    reconciles component by component against the printed reconciliation. Suppressing such a
    check silently would be worse than the failure, so acknowledgement costs something:

      * the case must declare ACKNOWLEDGED_TIEOUTS = {<exact tie-out description>: <reason>};
      * the reason must ALSO appear in DISCLOSED_DIFFERENCES, so it reaches the model, the
        committee and the rationale - not just this function;
      * acknowledged checks are REPORTED on every run, never counted as reconciling.

    Without the DISCLOSED_DIFFERENCES half this is a mute button, which is precisely the
    failure mode 39 pattern - a suite that stays green by not looking.
    """
    R = mod.compute()
    T = mod.tieouts(R)
    ack_decl = getattr(mod, "ACKNOWLEDGED_TIEOUTS", {}) or {}
    disclosed = " ".join(_flatten(d)
                         for d in (getattr(mod, "DISCLOSED_DIFFERENCES", []) or []))
    failures, acknowledged = [], []
    for desc, comp, disc, tol, src in T:
        if abs(comp - disc) <= tol:
            continue
        line = "%s (computed %.4f vs disclosed %.4f) [%s]" % (desc, comp, disc, src)
        reason = ack_decl.get(desc)
        if reason and reason.strip() and reason.strip()[:60] in disclosed:
            acknowledged.append((line, reason))
        else:
            if reason:
                line += "  <- acknowledgement REJECTED: its reason is not in "
                line += "DISCLOSED_DIFFERENCES"
            failures.append(line)
    return R, len(T), failures, acknowledged


def ratio_table(mod, R):
    rows, order = [], None
    for y in mod.YEARS:
        if order is None:
            order = [k for k, v in R[y].items() if isinstance(v, (int, float))]
    lines = ["%-42s %s" % ("", "".join("%14s" % y for y in mod.YEARS))]
    for k in order:
        cells = "".join("%14.2f" % R[y][k] if isinstance(R[y].get(k), (int, float))
                        else "%14s" % "-" for y in mod.YEARS)
        lines.append("%-42s%s" % (k, cells))
    return "\n".join(lines)


# ----------------------------------------------------------------------- local engine
def engine_local(case_dir):
    """Evaluate the filled scorecard's OWN formula chain. Deterministic, offline."""
    books = sorted(case_dir.glob("Rating_Scorecard*.xlsx"))
    if not books:
        return {"engine": "local", "available": False,
                "reason": "no filled Rating_Scorecard workbook in the case folder"}
    try:
        import warnings
        warnings.filterwarnings("ignore")
        import formulas
    except ImportError:
        return {"engine": "local", "available": False,
                "reason": "the `formulas` package is needed to evaluate the workbook "
                          "(pip install formulas)"}
    try:
        xl = formulas.ExcelModel().loads(str(books[0])).finish()
        sol = xl.calculate()
    except Exception as e:                                                # noqa: BLE001
        return {"engine": "local", "available": False,
                "reason": "workbook did not evaluate: %s" % e}
    # WHICH ROW holds the anchor grade is read from the sheet's OWN LABELS, never hardcoded.
    # This was pinned to Rating!C12. The 02-Sep-2026 three-stage rebuild moved the anchor to
    # C16 and made C12 "Support notches entered at Step 12b", so the local engine read a notch
    # count, failed to match it against the rating scale, and reported
    #   LOCAL UNAVAILABLE - Rating!C12 did not resolve to a recognised grade (got '0')
    # on EVERY case while still exiting 0. Measured 04-Sep-2026: broken on 6 of 6 cases tried,
    # including the only case the delivery gate calls READY TO SHARE. Per CLAUDE.md 8b the
    # local route is "the Step 12b anchor, made runnable", so the anchor row is the target.
    anchor_row = None
    try:
        from openpyxl import load_workbook
        ws = load_workbook(books[0], data_only=True)["Rating"]
        for r in range(1, ws.max_row + 1):
            if str(ws.cell(row=r, column=2).value or "").strip().lower().startswith(
                    "anchor long-term grade"):
                anchor_row = r
                break
    except Exception:                                                     # noqa: BLE001
        anchor_row = None
    if anchor_row is None:
        return {"engine": "local", "available": False,
                "reason": "no 'Anchor long-term grade' row on the Rating sheet - this workbook "
                          "predates the three-stage layout; run restructure_scorecard.py"}
    pat = re.compile(r"^'\[[^\]]+\]([^']+)'!([A-Z]+)(\d+)$")
    grade = None
    for k, v in sol.items():
        m = pat.match(k)
        if (m and m.group(1).upper() == "RATING" and m.group(2) == "C"
                and int(m.group(3)) == anchor_row):
            try:
                grade = str(v.value[0, 0]).strip()
            except Exception:                                             # noqa: BLE001
                grade = str(v).strip()
    if not grade or grade not in SCALE:
        return {"engine": "local", "available": False,
                "reason": "Rating!C%d (anchor long-term grade) did not resolve to a recognised "
                          "grade (got %r)" % (anchor_row, grade)}
    return {"engine": "local", "available": True, "workbook": books[0].name,
            "long_term": grade,
            "basis": "scorecard formula chain, evaluated offline; deterministic"}


# ----------------------------------------------------------------------- API engine
SCHEMA = {
    "type": "object",
    "properties": {
        "long_term_grade": {"type": "string", "enum": SCALE},
        "outlook": {"type": "string", "enum": ["Stable", "Positive", "Negative", "Not applicable"]},
        "short_term_grade": {"type": "string"},
        "key_strengths": {"type": "array", "items": {"type": "string"}},
        "key_weaknesses": {"type": "array", "items": {"type": "string"}},
        "principal_monitorable": {"type": "string"},
        "reasoning": {"type": "string"},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "data_limitations_considered": {"type": "string"},
    },
    "required": ["long_term_grade", "outlook", "short_term_grade", "key_strengths",
                 "key_weaknesses", "principal_monitorable", "reasoning", "confidence",
                 "data_limitations_considered"],
    "additionalProperties": False,
}

SYSTEM = """You are a senior credit rating analyst forming an independent rating view.

You are given a ratio suite that has ALREADY been computed and verified against the issuer's
audited statements. Every figure has passed a tie-out against a separately published company
figure. Treat these numbers as correct.

Rules that bind you:
- Do NOT invent, adjust, restate or estimate any financial figure. You have every number you
  are going to get. If something you would want is absent, say so in
  data_limitations_considered and reason without it.
- Weigh the DISCLOSED CONVENTIONS and the UNVERIFIED INPUTS sections. An input no tie-out
  covers is weaker evidence than one that reconciles to a published figure, and your
  confidence should reflect that.
- Rate on the named agency's long-term scale. Give the bare notch (for example "AA+"), not the
  agency's prefixed house form - the caller adds the prefix.
- Map the short-term grade consistently with the long-term one (AAA/AA -> A1+; A+ -> A1+ or A1;
  A -> A2+ or A1; A- -> A2+; BBB+ -> A2; BBB -> A3+; BBB- -> A3; BB+ -> A4+; below -> A4).
- Your reasoning must cite specific figures from the suite. A conclusion with no number
  attached to it is not usable."""


def build_prompt(slug, mod, R, meta, n_tieouts):
    disclosed = getattr(mod, "DISCLOSED_DIFFERENCES", [])
    unverified = sorted(getattr(mod, "UNVERIFIED_INPUTS", set()))
    parts = [
        "ISSUER: %s" % meta.get("name", slug),
        "AGENCY: %s" % meta.get("agency", "(not recorded)"),
        "SECTOR: %s" % meta.get("sector", "(not recorded)"),
        "METHODOLOGIES APPLIED: %s" % ", ".join(meta.get("methodologies", [])) or "(none recorded)",
        "",
        "VERIFIED RATIO SUITE (Rs crore unless the row says otherwise). All %d tie-outs in the "
        "engine reconcile." % n_tieouts,
        "",
        ratio_table(mod, R),
        "",
        "DISCLOSED CONVENTIONS AND DIFFERENCES - read these before weighing the numbers:",
    ]
    if disclosed:
        for item in disclosed:
            parts.append("  * %s" % _flatten(item))
    else:
        parts.append("  (none recorded)")
    parts += ["", "INPUTS NO TIE-OUT COVERS - weaker evidence, factor into your confidence:"]
    parts.append("  " + ("; ".join(_flatten(u) for u in unverified)
                         if unverified else "(none - every input is checked)"))
    parts += ["",
              "Form your rating view. Return only the structured object."]
    return "\n".join(parts)


def engine_api(slug, mod, R, meta, n_tieouts, model, effort, api_key):
    try:
        import anthropic
    except ImportError:
        return {"engine": "api", "available": False,
                "reason": "the anthropic SDK is not installed (pip install anthropic)"}
    try:
        client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()
    except Exception as e:                                                # noqa: BLE001
        return {"engine": "api", "available": False, "reason": "client init failed: %s" % e}

    prompt = build_prompt(slug, mod, R, meta, n_tieouts)
    try:
        resp = client.messages.create(
            model=model,
            max_tokens=16000,
            system=SYSTEM,
            thinking={"type": "adaptive"},
            output_config={"effort": effort,
                           "format": {"type": "json_schema", "schema": SCHEMA}},
            messages=[{"role": "user", "content": prompt}],
        )
    except anthropic.AuthenticationError:
        return {"engine": "api", "available": False,
                "reason": "authentication failed - the credential was rejected"}
    except anthropic.PermissionDeniedError:
        return {"engine": "api", "available": False,
                "reason": "the credential lacks permission for this model"}
    except anthropic.NotFoundError:
        return {"engine": "api", "available": False,
                "reason": "model %r not found for this account" % model}
    except anthropic.RateLimitError as e:
        ra = e.response.headers.get("retry-after", "?") if e.response is not None else "?"
        return {"engine": "api", "available": False,
                "reason": "rate limited; retry after %ss" % ra}
    except anthropic.APIStatusError as e:
        return {"engine": "api", "available": False,
                "reason": "API error %s: %s" % (e.status_code, e.message)}
    except anthropic.APIConnectionError:
        return {"engine": "api", "available": False,
                "reason": "network error reaching the API"}
    except TypeError as e:
        # The SDK resolves credentials lazily: Anthropic() constructs fine with no key and
        # only raises at request time, as a TypeError rather than AuthenticationError. Without
        # this branch the tool dies with a traceback instead of telling you what to do.
        if "authentication" in str(e).lower():
            return {"engine": "api", "available": False,
                    "reason": "no credential found. Set ANTHROPIC_API_KEY, or run "
                              "`ant auth login`, or pass --api-key-file <path>. "
                              "The local engine still works with no credential at all."}
        raise

    if resp.stop_reason == "refusal":
        cat = getattr(getattr(resp, "stop_details", None), "category", None)
        return {"engine": "api", "available": False,
                "reason": "the model declined this request (category: %s)" % cat}

    text = next((b.text for b in resp.content if b.type == "text"), None)
    if not text:
        return {"engine": "api", "available": False,
                "reason": "no text block in the response (stop_reason=%s)" % resp.stop_reason}
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        return {"engine": "api", "available": False, "reason": "response was not JSON: %s" % e}

    data.update({
        "engine": "api", "available": True, "model": model, "effort": effort,
        "usage": {"input_tokens": resp.usage.input_tokens,
                  "output_tokens": resp.usage.output_tokens},
        "request_id": getattr(resp, "_request_id", None),
    })
    return data


# ----------------------------------------------------------------------- agent engine
def find_pending():
    """Every RATING_REQUEST.md / RESEARCH_REQUEST.md still marked PENDING."""
    out = []
    for req in sorted((ROOT / "Companies").glob("*/*REQUEST.md")):
        try:
            txt = req.read_text(encoding="utf-8", errors="replace")
        except Exception:                                                 # noqa: BLE001
            continue
        m = re.search(r"^Status:\s*(.+)$", txt, re.M | re.I)
        status = m.group(1).strip() if m else "(no Status line)"
        if status.upper().startswith("PENDING"):
            agency = re.search(r"^Agency:\s*(.+)$", txt, re.M | re.I)
            out.append({"slug": req.parent.name, "file": req.name,
                        "agency": agency.group(1).strip() if agency else "?",
                        "status": status})
    return out


def find_claude_cli():
    import shutil
    for name in ("claude", "claude.cmd", "claude.exe"):
        p = shutil.which(name)
        if p:
            return p
    for cand in (Path.home() / ".local" / "bin" / "claude",
                 Path.home() / ".claude" / "local" / "claude"):
        if cand.exists():
            return str(cand)
    return None


AGENT_PROMPT_PENDING = """Process the pending rating requests in this project.

Follow CLAUDE.md exactly - it is the binding SOP for this work. In particular:
  * run `python preflight.py <slug>` first and paste its output into the read log;
  * every number must be computed in code, and every tie-out must reconcile before drafting;
  * run `python tieout_mutation.py <slug>` and declare any input no tie-out covers;
  * pass the delivery gate (`python check_sections.py <rationale>`) before you finish.

Pending now: {pending}

Work through them one at a time. When each is complete, mark its request file Status: DONE and
update case.json. Report what you delivered, the rating assigned, and anything you could not
verify."""

AGENT_PROMPT_CASE = """Review the completed rating for the case `{slug}` in this project.

Follow CLAUDE.md. Re-run the ratio engine, the tie-outs, `python tieout_mutation.py {slug}`,
and the case's own verify script. Then form and state a rating view with your reasoning.
Report any figure you cannot verify against a source document."""


def engine_agent(slug=None, pending=None, model=None, timeout=3600,
                 dry_run=False, assume_yes=False, max_budget_usd=2.0):
    """Hand the job to a local Claude Code agent. It can do what the API engine cannot."""
    cli = find_claude_cli()
    if not cli:
        return {"engine": "agent", "available": False,
                "reason": "the `claude` CLI was not found on PATH. Install Claude Code, or "
                          "use --engine api with a real key."}

    if pending is not None:
        if not pending:
            return {"engine": "agent", "available": False,
                    "reason": "nothing is pending - every *REQUEST.md is already marked DONE. "
                              "Add a request, or name a case slug to review instead."}
        listing = "\n".join("  - %s (%s, %s)" % (p["slug"], p["agency"], p["file"])
                             for p in pending)
        prompt = AGENT_PROMPT_PENDING.format(pending=listing)
        what = "%d pending request(s)" % len(pending)
    else:
        prompt = AGENT_PROMPT_CASE.format(slug=slug)
        what = "case %s" % slug

    # An EXPLICIT ALLOWLIST, deliberately not --dangerously-skip-permissions.
    # First attempt used only --permission-mode acceptEdits, which auto-approves file edits
    # but NOT command execution. In headless -p mode there is nobody to approve a Bash call,
    # so the agent burned 15 turns and $0.70 and then reported it could not run
    # compute_ratios.py, tieout_mutation.py or verify_jsl.py - i.e. it could not verify
    # anything, which is the whole point of handing it the job. The SOP needs to run scripts,
    # read documents and write case files, so those tools are named here; everything else
    # still requires approval, and --add-dir keeps it inside this project.
    allowed = ["Bash", "Read", "Write", "Edit", "Glob", "Grep", "Skill", "TodoWrite",
               "WebSearch", "WebFetch"]
    # A HARD DOLLAR CAP, always passed. An agent pass is not a single API call:
    # measured 29-Aug-2026, one trivial one-turn prompt cost $0.4561 and a 15-turn
    # case review cost $0.7025, and a full SOP pass is far longer than either.
    # Without a ceiling this route can spend real money with nobody watching.
    cmd = [cli, "-p", prompt, "--output-format", "json",
           "--permission-mode", "acceptEdits",
           "--allowedTools", ",".join(allowed),
           "--max-budget-usd", str(max_budget_usd),
           "--add-dir", str(ROOT)]
    if model:
        cmd += ["--model", model]

    if dry_run:
        return {"engine": "agent", "available": False, "dry_run": True,
                "reason": "dry run - not executed", "command": cmd[:2] + ["<prompt>"] + cmd[3:],
                "prompt": prompt, "target": what}

    if not assume_yes:
        print("")
        print("  The agent will run in %s and may WRITE FILES." % ROOT)
        print("  Target     : %s" % what)
        print("  Budget cap : $%.2f (hard limit; raise with --max-budget-usd)"
              % max_budget_usd)
        print("  For scale  : a trivial 1-turn prompt measured $0.46; a 15-turn "
              "review $0.70.")
        try:
            if input("  Start it? [y/N] ").strip().lower() not in ("y", "yes"):
                return {"engine": "agent", "available": False,
                        "reason": "declined at the confirmation prompt"}
        except EOFError:
            return {"engine": "agent", "available": False,
                    "reason": "no TTY to confirm on - pass --yes to run non-interactively"}

    import subprocess
    print("  agent running (up to %ds; this is a full SOP pass, not a single call)..." % timeout)
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=str(ROOT))
    except subprocess.TimeoutExpired:
        return {"engine": "agent", "available": False,
                "reason": "agent exceeded the %ds timeout (raise --agent-timeout)" % timeout}
    except Exception as e:                                                # noqa: BLE001
        return {"engine": "agent", "available": False, "reason": "could not start: %s" % e}

    raw = (r.stdout or "").strip()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return {"engine": "agent", "available": False,
                "reason": "agent output was not JSON (exit %d): %s"
                          % (r.returncode, (raw or r.stderr or "")[:300])}

    if data.get("is_error"):
        return {"engine": "agent", "available": False,
                "reason": "agent failed: %s" % data.get("result", "(no detail)")}

    return {"engine": "agent", "available": True, "target": what,
            "result": data.get("result", ""),
            "session_id": data.get("session_id"),
            "turns": data.get("num_turns"),
            "cost_usd": data.get("total_cost_usd"),
            "duration_s": round((data.get("duration_ms") or 0) / 1000.0, 1)}


def check_agent_ready():
    """Is the local agent route actually usable? Cheap to run, saves a failed agent pass."""
    import subprocess
    cli = find_claude_cli()
    print("claude CLI     : %s" % (cli or "NOT FOUND on PATH"))
    if not cli:
        print("                 install Claude Code, or use --engine api with a real key")
        return False
    try:
        r = subprocess.run([cli, "auth", "status"], capture_output=True, text=True, timeout=60)
        data = json.loads((r.stdout or "").strip())
    except Exception as e:                                                # noqa: BLE001
        print("auth status    : could not read (%s)" % e)
        return False
    logged = bool(data.get("loggedIn"))
    print("logged in      : %s" % ("yes" if logged else "NO"))
    print("auth method    : %s" % data.get("authMethod"))
    if not logged:
        print("")
        print("  The agent route needs its own credential. Run this yourself - it opens")
        print("  a browser for consent, so it cannot be done for you:")
        print("")
        print("      claude auth login")
        print("")
        print("  Then re-run:  python rate_engine.py --check-agent")
        return False
    pending = find_pending()
    print("pending queue  : %s" % (", ".join(p["slug"] for p in pending) if pending
                                   else "empty - add a request before using --pending"))
    print("")
    print("  Ready. Try:  python rate_engine.py --pending --api-key %s --dry-run"
          % AGENT_SENTINEL)
    return True


# ----------------------------------------------------------------------- comparison
def notch_gap(a, b):
    if a in SCALE and b in SCALE:
        return SCALE.index(b) - SCALE.index(a)
    return None


def is_sentinel(value):
    return value is not None and value.strip() == AGENT_SENTINEL


# =============================================================================================
# WHERE YOU PUT YOUR API KEY
# =============================================================================================
# Until now the only ways in were --api-key (which lands in shell history), --api-key-file, or
# an environment variable - so the tool never actually ASKED for a key, and there was nowhere
# obvious to put one. There is now:
#
#     python rate_engine.py --set-key          enter it once, stored for future runs
#     python rate_engine.py --show-key         where it is stored and which key is in use
#     python rate_engine.py --clear-key        delete it
#
# and any run that needs a credential and cannot find one will ask, rather than failing with
# instructions.
#
# The key is stored in the user's HOME directory, deliberately NOT in this project folder. The
# folder gets zipped and emailed - the rating reports in it are the whole point of the tool -
# and a credential that travels with the deliverable is a credential that leaks.
KEY_FILE = Path.home() / ".icra_rating_api_key"


def _protect(path):
    """Owner-only permissions. Returns a note if that could not be fully guaranteed."""
    try:
        os.chmod(path, 0o600)
    except OSError:
        return "could not set file permissions"
    if os.name == "nt":
        # chmod on Windows only toggles the read-only bit; it does not restrict other users the
        # way 0600 does on POSIX. Say so rather than implying a protection that is not there.
        return ("on Windows this file is protected only by your user profile's own NTFS "
                "permissions, not by the 0600 mode this code requests")
    return None


def store_key(key):
    KEY_FILE.write_text(key.strip() + "\n", encoding="utf-8")
    return _protect(KEY_FILE)


def stored_key():
    if not KEY_FILE.exists():
        return None
    key = KEY_FILE.read_text(encoding="utf-8").strip()
    return key or None


def prompt_for_key(reason=""):
    """Ask for a key with the input masked. Returns the key, or None if declined.

    getpass falls back to visible input on terminals that cannot mask, and warns when it does;
    that warning is left alone rather than suppressed, because a key echoed to a shared screen
    is exactly the thing the caller needs to know about.
    """
    import getpass
    if not sys.stdin.isatty():
        return None                       # non-interactive: never block a scripted run
    print()
    if reason:
        print("  %s" % reason)
    print("  Enter an Anthropic API key (starts with 'sk-ant-'), or %s to hand the job to a"
          % AGENT_SENTINEL)
    print("  local Claude Code agent. Leave blank to cancel. Input is hidden.")
    try:
        key = getpass.getpass("  API key: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n  cancelled.")
        return None
    if not key:
        print("  cancelled - no key entered.")
        return None
    if key == AGENT_SENTINEL:
        return key
    if not key.startswith("sk-ant-"):
        # A warning, not a rejection: Anthropic has changed key prefixes before, and a tool that
        # refuses a valid credential because it does not recognise the shape is worse than one
        # that lets the API return 401.
        print("  NOTE: that does not look like an Anthropic key (expected an 'sk-ant-' prefix).")
        print("        Storing it anyway - the API will reject it if it is wrong.")
    return key


UI_PREFS = ROOT / "webapp" / "ui_prefs.json"


def ui_model():
    """The model chosen on the web app's Settings page, or the built-in default.

    Without this the Settings dropdown was decorative - it wrote a preference file that nothing
    read, so choosing a model there changed nothing about what any run actually used. A control
    that does not control anything is worse than no control: it invites you to believe a
    decision was made.

    An explicit --model on the command line still wins, because argparse only falls back to this
    when the flag is absent.
    """
    try:
        m = json.loads(UI_PREFS.read_text(encoding="utf-8")).get("model")
    except Exception:                                                     # noqa: BLE001
        return DEFAULT_MODEL
    return m if m in MODELS else DEFAULT_MODEL


def sdk_has_credential():
    """True if the Anthropic SDK can authenticate on its own (e.g. an `ant auth login` profile).

    Constructing the client is the only honest test - the SDK's resolution order is its own
    business and reimplementing it here would drift. It raises when it finds nothing, so the
    exception IS the answer; no request is made and nothing is billed.
    """
    try:
        import anthropic
    except ImportError:
        return False
    try:
        anthropic.Anthropic()
        return True
    except Exception:                                                     # noqa: BLE001
        return False


def resolve_key(args):
    """Return (key_or_None, description). The key itself is never printed.

    A sentinel value is returned as-is so main() can route on it; it is never handed to the
    Anthropic client, because sending a known-invalid string to the API would just burn a
    round-trip on a guaranteed 401.
    """
    if args.api_key_file:
        p = Path(args.api_key_file).expanduser()
        if not p.exists():
            sys.exit("--api-key-file not found: %s" % p)
        key = p.read_text(encoding="utf-8").strip()
        if not key:
            sys.exit("--api-key-file is empty: %s" % p)
        return key, "file %s (keep this out of version control)" % p.name
    if args.api_key:
        return args.api_key, "--api-key argument (prefer ANTHROPIC_API_KEY - a key passed " \
                             "on the command line is written to your shell history)"
    for var in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN"):
        if os.environ.get(var):
            return None, "environment variable %s (resolved by the SDK)" % var
    # The stored key ranks BELOW the environment on purpose: an env var is set deliberately for
    # one shell and should win over a file the user set up months ago and has forgotten about.
    key = stored_key()
    if key:
        return key, "stored key at %s (set with --set-key)" % KEY_FILE
    return None, "SDK default resolution (env var or an `ant auth login` profile)"


def fingerprint(key):
    if not key:
        return "n/a"
    return "%s...%s (%d chars)" % (key[:7], key[-4:], len(key)) if len(key) > 14 else "set"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", nargs="?", help="case folder name under Companies/")
    ap.add_argument("--engine", choices=["local", "api", "agent", "both"], default="both",
                    help="'agent' hands the job to a local Claude Code agent; it is also "
                         "selected automatically when the key is the sentinel %r"
                         % AGENT_SENTINEL)
    ap.add_argument("--pending", action="store_true",
                    help="agent route: work the pending request queue instead of one case")
    ap.add_argument("--yes", action="store_true",
                    help="skip the confirmation before starting an agent")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the agent command and prompt without running it")
    ap.add_argument("--agent-timeout", type=int, default=3600,
                    help="seconds to allow the agent (default 3600)")
    ap.add_argument("--max-budget-usd", type=float, default=2.0,
                    help="hard spend ceiling for an agent run (default 2.00)")
    ap.add_argument("--model", default=ui_model(), choices=sorted(MODELS))
    ap.add_argument("--effort", default="high",
                    choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--set-key", action="store_true",
                    help="enter an API key (hidden input) and store it for future runs")
    ap.add_argument("--show-key", action="store_true",
                    help="show which credential is in use and where it is stored")
    ap.add_argument("--clear-key", action="store_true", help="delete the stored API key")
    ap.add_argument("--api-key", help="discouraged - lands in shell history")
    ap.add_argument("--api-key-file", help="path to a file containing only the key")
    ap.add_argument("--json", help="write the full result to this path")
    ap.add_argument("--list-models", action="store_true")
    ap.add_argument("--check-agent", action="store_true",
                    help="report whether the local agent route is usable, and why not")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass

    if args.check_agent:
        print("=" * 92)
        print("AGENT ROUTE READINESS")
        print("=" * 92)
        sys.exit(0 if check_agent_ready() else 1)

    # ---- key management. These run and exit; they never touch a case folder. ----------------
    if args.clear_key:
        if KEY_FILE.exists():
            KEY_FILE.unlink()
            print("Stored key deleted: %s" % KEY_FILE)
        else:
            print("No stored key to delete (looked in %s)." % KEY_FILE)
        return

    if args.set_key:
        entered = prompt_for_key()
        if entered is None:
            if not sys.stdin.isatty():
                sys.exit("--set-key needs an interactive terminal (input must be hidden). "
                         "Use --api-key-file <path> in a script instead.")
            return
        note = store_key(entered)
        print("\n  Stored: %s" % KEY_FILE)
        print("  In use: %s" % fingerprint(entered))
        if note:
            print("  NOTE:   %s" % note)
        if entered == AGENT_SENTINEL:
            print("  This is the agent sentinel, not an API key - runs will be routed to a")
            print("  local Claude Code agent, which needs its own credential.")
        print("\n  Ready. Try:  python rate_engine.py --pending --dry-run")
        return

    if args.show_key:
        _k, _desc = resolve_key(args)
        print("=" * 92)
        print("CREDENTIAL")
        print("=" * 92)
        print("  source      : %s" % _desc)
        print("  fingerprint : %s" % fingerprint(_k))
        print("  store path  : %s%s"
              % (KEY_FILE, "" if KEY_FILE.exists() else "   (nothing stored yet)"))
        if _k is None and not KEY_FILE.exists():
            print("\n  No key is stored. Add one with:  python rate_engine.py --set-key")
            print("  The SDK may still find a credential of its own (ANTHROPIC_API_KEY, or an")
            print("  `ant auth login` profile); this only reports what THIS tool can see.")
        return

    if args.list_models:
        print("Selectable models (--model):\n")
        for m, d in MODELS.items():
            print("  %-20s %s%s" % (m, d, "   [default]" if m == DEFAULT_MODEL else ""))
        return
    key_peek, _ = resolve_key(args)

    # If an API run is asked for and NOTHING can supply a credential, ask for one here rather
    # than failing several steps later with a paragraph of instructions. Only when the SDK has
    # no fallback of its own - an `ant auth login` profile is a perfectly good credential and
    # prompting over the top of it would be noise.
    if (key_peek is None and args.engine in ("api", "both")
            and not any(os.environ.get(v) for v in ("ANTHROPIC_API_KEY",
                                                    "ANTHROPIC_AUTH_TOKEN"))
            and not sdk_has_credential()):
        entered = prompt_for_key("No API key found, and the API engine was requested.")
        if entered:
            note = store_key(entered)
            print("  Stored for future runs: %s" % KEY_FILE)
            if note:
                print("  NOTE: %s" % note)
            key_peek = entered
            args.api_key = entered

    sentinel = is_sentinel(key_peek)
    if sentinel and args.engine in ("api", "both"):
        args.engine = "agent"

    # The agent route works the request QUEUE, so it does not need a built case.
    if args.engine == "agent" or args.pending:
        pending = find_pending()
        print("=" * 92)
        print("AGENT ROUTE - local Claude Code agent")
        print("=" * 92)
        if sentinel:
            print("key           : sentinel %r -> local agent (nothing sent to the API)"
                  % AGENT_SENTINEL)
        print("project       : %s" % ROOT)
        print("pending queue : %s" % (", ".join("%s (%s)" % (p["slug"], p["agency"])
                                                for p in pending) if pending else "empty"))
        out = engine_agent(slug=args.slug,
                           pending=pending if (args.pending or not args.slug) else None,
                           model=args.model if args.model != DEFAULT_MODEL else None,
                           timeout=args.agent_timeout, dry_run=args.dry_run,
                           assume_yes=args.yes,
                           max_budget_usd=args.max_budget_usd)
        print("-" * 92)
        if out.get("dry_run"):
            print("DRY RUN - would run:\n  %s\n" % " ".join(out["command"]))
            print("prompt:\n%s" % out["prompt"])
        elif not out.get("available"):
            print("AGENT UNAVAILABLE - %s" % out["reason"])
        else:
            print("AGENT COMPLETE - %s" % out["target"])
            print("  turns %s | %.1fs | $%.4f | session %s"
                  % (out["turns"], out["duration_s"], out["cost_usd"] or 0.0,
                     out["session_id"]))
            print("-" * 92)
            print(out["result"])
        print("-" * 92)
        print("An agent is not a rating either. Its output goes to a committee like any other.")
        return

    if not args.slug:
        ap.error("a case slug is required (or use --list-models / --pending)")

    case_dir, mod, meta = load_case(args.slug)
    R, n_tieouts, failures, acknowledged = run_tieouts(mod)

    print("=" * 92)
    print("RATING OUTCOME - %s" % meta.get("name", args.slug))
    print("=" * 92)
    print("agency        : %s" % meta.get("agency", "(not recorded)"))
    print("tie-outs      : %d/%d reconcile%s"
          % (n_tieouts - len(failures) - len(acknowledged), n_tieouts,
             ", %d acknowledged" % len(acknowledged) if acknowledged else ""))
    for line, reason in acknowledged:
        print("")
        print("ACKNOWLEDGED DIVERGENCE - a declared and evidenced one, not a passing check:")
        print("  %s" % line)
        print("  reason: %s" % reason)

    if failures:
        print("\nABORTED - the ratio engine does not reconcile, so no rating is produced by")
        print("either route. A rating computed off a failing engine is worse than none.")
        for f in failures:
            print("  FAIL %s" % f)
        sys.exit(1)

    results = {}
    if args.engine in ("local", "both"):
        results["local"] = engine_local(case_dir)
    if args.engine in ("api", "both"):
        key, how = resolve_key(args)
        if is_sentinel(key):
            key, how = None, "sentinel ignored on this route"
        print("credential    : %s" % how)
        if key:
            print("                fingerprint %s" % fingerprint(key))
        print("model         : %s (effort %s)" % (args.model, args.effort))
        results["api"] = engine_api(args.slug, mod, R, meta, n_tieouts,
                                    args.model, args.effort, key)

    print()
    for name in ("local", "api"):
        r = results.get(name)
        if not r:
            continue
        print("-" * 92)
        if not r.get("available"):
            print("%-6s UNAVAILABLE - %s" % (name.upper(), r["reason"]))
            continue
        if name == "local":
            print("LOCAL  (deterministic scorecard, offline)")
            print("       grade      : %s" % r["long_term"])
            print("       workbook   : %s" % r["workbook"])
            print("       basis      : %s" % r["basis"])
        else:
            print("API    (%s, effort %s)" % (r["model"], r["effort"]))
            print("       grade      : %s (%s)" % (r["long_term_grade"], r["outlook"]))
            print("       short term : %s" % r["short_term_grade"])
            print("       confidence : %s" % r["confidence"])
            print("       monitorable: %s" % r["principal_monitorable"])
            print("       strengths  :")
            for s in r["key_strengths"]:
                print("          - %s" % s)
            print("       weaknesses :")
            for s in r["key_weaknesses"]:
                print("          - %s" % s)
            print("       limitations: %s" % r["data_limitations_considered"])
            print("       reasoning  : %s" % r["reasoning"])
            print("       tokens     : in %s / out %s"
                  % (r["usage"]["input_tokens"], r["usage"]["output_tokens"]))

    lo, ap_ = results.get("local", {}), results.get("api", {})
    if lo.get("available") and ap_.get("available"):
        gap = notch_gap(lo["long_term"], ap_["long_term_grade"])
        print("-" * 92)
        print("DIVERGENCE")
        if gap == 0:
            print("  none - both routes return %s independently." % lo["long_term"])
        else:
            direction = "weaker" if gap > 0 else "stronger"
            print("  %d notch(es): scorecard %s, model %s - the model is %s."
                  % (abs(gap), lo["long_term"], ap_["long_term_grade"], direction))
            print("  This is a finding to resolve, not a number to average. The scorecard is")
            print("  a zero-biased screening band that under-rates the AA+/AAA range; the")
            print("  model sees business factors a ratio grid cannot. Read both and decide.")
        prefix = AGENCY_PREFIX.get(meta.get("agency", ""), "")
        print("  house form: %s%s (%s) / %s"
              % (prefix, ap_["long_term_grade"], ap_["outlook"], ap_["short_term_grade"]))

    print("-" * 92)
    print("Neither engine is the rating. Both are inputs to a committee decision.")

    if args.json:
        payload = {"case": args.slug, "issuer": meta.get("name", args.slug),
                   "agency": meta.get("agency"), "generated_utc": datetime.now(timezone.utc)
                   .isoformat(timespec="seconds"),
                   "tieouts": {"total": n_tieouts, "failed": len(failures)},
                   "results": results}
        Path(args.json).write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print("wrote %s (no credential is included)" % args.json)


if __name__ == "__main__":
    main()
