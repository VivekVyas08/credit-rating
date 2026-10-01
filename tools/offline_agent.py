"""EXPERIMENTAL offline report drafter: a local Ollama model + the project's skills + tools.

This is NOT the online agent, and its output is NOT a rating. It runs a small tool-using loop
against a LOCAL model under Ollama (granite, qwen3, ... anything tools-capable) so the rating
SKELETON, house style and the VERIFIED computed data become a DRAFT rationale with no key and no
internet. The local model is far below Claude, so this is a SCREENING DRAFT only:

  * the NUMBERS are computed offline by the ratio engine and handed to the model verbatim - it is
    told to use only those, never to invent a figure (the same discipline as the model-view
    engine: every material error this project made was an extraction error);
  * the model writes the PROSE around them and assembles the mandatory sections;
  * the draft is saved with a loud EXPERIMENTAL banner and then run through check_sections.py.

A small local model will miss sections, mis-map the short-term grade and trip the gates. Treat
the result as a starting point a human (or Claude, online) finishes - never as a deliverable.

    python tools/offline_agent.py <case-slug> [--model granite4.2:8b] [--url URL] [--timeout 1200] [--max-steps 12]
"""
import argparse
import json
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import rate_engine as RE                                                   # noqa: E402

SKELETON = ROOT / ".claude" / "skills" / "icra-report-skeleton" / "SKELETON.md"
BANNER = ("> ⚠ EXPERIMENTAL OFFLINE DRAFT — written by a local model (%s) with no key and no "
          "internet. The figures are from the offline ratio engine; the prose is a SCREENING "
          "draft only, NOT a rating and NOT verified. A human or Claude must finish it.\n\n")

SYSTEM = """You draft a credit-rating rationale OFFLINE from already-verified data.

Hard rules:
- Use ONLY the numbers in the VERIFIED DATA block. NEVER invent, adjust or estimate a figure.
- Produce EVERY mandatory section of the SKELETON, in its order and house style.
- Rate on the stated agency's scale; the long-term grade is given to you - do not change it.
- Output ONLY the report in markdown. No tool calls, no preamble, no commentary, no reasoning
  trace - just the finished rationale, starting at its title."""


def _tools():
    f = lambda name, desc, props, req: {                                  # noqa: E731
        "type": "function",
        "function": {"name": name, "description": desc,
                     "parameters": {"type": "object", "properties": props, "required": req}}}
    return [
        f("read_file", "Read a UTF-8 text file under the project root (the report skeleton, a "
                       "conventions file, the case workpaper). Returns the first part of the file.",
          {"path": {"type": "string", "description": "path relative to the project root"}}, ["path"]),
        f("save_draft", "Save the finished draft rationale to the case folder. Call once with the "
                        "complete markdown of the report.",
          {"markdown": {"type": "string", "description": "the full rationale in markdown"}}, ["markdown"]),
        f("run_section_audit", "Run the mandatory section/quality gate on the saved draft and "
                               "return its report so you can fix any missing section.", {}, []),
    ]


class Tools:
    def __init__(self, slug, model):
        self.slug = slug
        self.model = model
        self.case_dir = ROOT / "Companies" / slug
        self.draft_path = None

    def read_file(self, path=""):
        p = (ROOT / path).resolve()
        if not str(p).startswith(str(ROOT)) or not p.is_file():
            return "ERROR: no such file under the project root: %r" % path
        return p.read_text(encoding="utf-8", errors="replace")[:12000]

    def save_draft(self, markdown=""):
        name = "%s_OFFLINE_DRAFT_Rating Rationale.md" % self.slug
        self.draft_path = self.case_dir / name
        self.case_dir.mkdir(parents=True, exist_ok=True)
        self.draft_path.write_text((BANNER % self.model) + (markdown or ""), encoding="utf-8")
        return "Saved draft to %s (%d chars)." % (self.draft_path.name, len(markdown or ""))

    def run_section_audit(self):
        if not self.draft_path or not self.draft_path.is_file():
            return "No draft saved yet. Call save_draft first."
        p = subprocess.run([sys.executable, str(ROOT / "tools" / "check_sections.py"),
                            str(self.draft_path)], cwd=str(ROOT), capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=300)
        out = (p.stdout or "") + (p.stderr or "")
        return out[-2500:] if out.strip() else "check_sections.py produced no output."


def _ollama_chat(url, model, messages, timeout, tools_on=True):
    payload = {"model": model, "stream": False, "think": False,
               "options": {"temperature": 0, "num_ctx": 16384}, "messages": messages}
    if tools_on:
        payload["tools"] = _tools()
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url + "/api/chat", data=body,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        if e.code == 400 and "think" in detail.lower():          # non-thinking model: drop it
            b2 = json.loads(body); b2.pop("think", None)
            req2 = urllib.request.Request(url + "/api/chat", data=json.dumps(b2).encode("utf-8"),
                                          headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req2, timeout=timeout) as r:
                return json.load(r)
        raise


def run(slug, model, url, timeout):
    # Verified inputs: numbers come from the ratio engine, never from the model.
    d, mod, meta = RE.load_case(slug)
    R, n, failures, _ack = RE.run_tieouts(mod)
    if failures:
        return "ABORTED - the ratio engine does not reconcile, so there is nothing trustworthy to "\
               "draft from:\n  " + "\n  ".join(failures)
    anchor = RE.engine_local(ROOT / "Companies" / slug)
    data_block = RE.build_prompt(slug, mod, R, meta, n)
    anchor_line = ("SCORECARD ANCHOR (deterministic, offline): %s"
                   % anchor.get("long_term", "n/a")) if anchor.get("available") else ""
    skeleton_text = SKELETON.read_text(encoding="utf-8", errors="replace")[:9000]

    # ONE pre-loaded generation, NO tools. A local model cannot orchestrate a tool loop for this
    # (granite4.2:3b emitted tool-call SYNTAX as text and never wrote a word); handing it the
    # skeleton + the verified numbers up front and asking for the report in a single pass is the
    # only thing that reliably yields prose. Python does the saving and the audit.
    user = ("Draft the rating rationale for the issuer below. Output ONLY the report in markdown.\n\n"
            "ISSUER: %s   AGENCY: %s   SECTOR: %s\n\n"
            "VERIFIED DATA (use ONLY these numbers, never invent one):\n%s\n%s\n\n"
            "Follow this mandatory SKELETON section by section:\n\n%s"
            % (meta.get("name", slug), meta.get("agency", "?"), meta.get("sector", "?"),
               anchor_line, data_block, skeleton_text))
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]

    print("  generating the full rationale in one pass (no tools)...")
    try:
        resp = _ollama_chat(url, model, messages, timeout, tools_on=False)
    except Exception as e:                                                # noqa: BLE001
        return "ollama call failed: %s" % e
    md = (resp.get("message") or {}).get("content", "")
    if not md.strip():
        return "NO DRAFT PRODUCED - the model returned no text."

    tools = Tools(slug, model)
    tools.save_draft(md)
    audit = tools.run_section_audit()
    return ("OFFLINE DRAFT written (experimental, screening only):\n  %s\n  (%d chars of prose, "
            "%s eval tokens)\n\n"
            "Section audit (expect gaps from a small local model):\n%s\n\n"
            "This is NOT a rating. Finish it with Claude (online) or by hand."
            % (tools.draft_path, len(md), resp.get("eval_count", "?"), audit[:1500]))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", help="case folder name under Companies/")
    ap.add_argument("--model", default=RE.OLLAMA_DEFAULT_MODEL)
    ap.add_argument("--url", default=RE.OLLAMA_DEFAULT_URL)
    ap.add_argument("--timeout", type=int, default=1800, help="seconds for the generation (default 1800)")
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    print("=" * 92)
    print("OFFLINE DRAFT AGENT - %s  (model %s, offline)" % (a.slug, a.model))
    print("This is a SCREENING DRAFT from a local model, not a rating. Numbers are engine-verified;")
    print("the prose is the local model's and is unverified.")
    print("-" * 92)
    out = run(a.slug, a.model, a.url, a.timeout)
    print("-" * 92)
    print(out)


if __name__ == "__main__":
    main()
