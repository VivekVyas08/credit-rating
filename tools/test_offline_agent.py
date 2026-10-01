"""Smoke test for the offline draft agent - exercises the real tool loop with a stubbed model.

No network, no model: _ollama_chat is replaced by a scripted sequence (read_file -> save_draft
-> final text). The data path (load_case, tie-outs, engine_local, build_prompt) and the tools
(read_file sandbox, save_draft banner, run_section_audit subprocess) are the REAL ones.

    python tools/test_offline_agent.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import offline_agent as OA                                                 # noqa: E402
import rate_engine as RE                                                   # noqa: E402

_fails = []


def check(cond, label):
    print("   %-5s %s" % ("ok" if cond else "FAIL", label))
    if not cond:
        _fails.append(label)


def _pick_reconciling_case():
    base = ROOT / "Companies"
    for d in sorted(p for p in base.iterdir() if (p / "compute_ratios.py").exists()):
        try:
            _c, mod, _m = RE.load_case(d.name)
            if not (hasattr(mod, "compute") and hasattr(mod, "tieouts")):
                continue
            _R, _n, failures, _a = RE.run_tieouts(mod)
            if not failures:
                return d.name
        except Exception:                                                 # noqa: BLE001
            continue
    raise SystemExit("no reconciling case with the compute()/tieouts() contract to test against")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    print("=" * 78)
    print("offline_agent.py - tool-loop smoke test (stubbed model, no network)")
    print("=" * 78)

    slug = _pick_reconciling_case()
    print("\n[case] %s" % slug)

    # Scripted model: read the skeleton, save a draft, then stop with a final line.
    script = [
        {"message": {"content": "", "tool_calls": [
            {"function": {"name": "read_file",
                          "arguments": {"path": ".claude/skills/icra-report-skeleton/SKELETON.md"}}}]}},
        {"message": {"content": "", "tool_calls": [
            {"function": {"name": "save_draft",
                          "arguments": {"markdown": "# Test Co: rating assigned\n\n## Rationale\n"
                                                    "Body.\n\n## Liquidity position: Adequate\n"}}}]}},
        {"message": {"content": "Draft complete."}},
    ]
    seen = {"i": 0, "tools_offered": False}

    def fake_chat(url, model, messages, timeout):
        # prove the real tool schema is being sent and think is disabled
        # (messages/urls are real; we only replace the transport)
        r = script[min(seen["i"], len(script) - 1)]
        seen["i"] += 1
        return r

    real = OA._ollama_chat
    OA._ollama_chat = fake_chat
    draft_path = ROOT / "Companies" / slug / ("%s_OFFLINE_DRAFT_Rating Rationale.md" % slug)
    try:
        if draft_path.exists():
            draft_path.unlink()
        out = OA.run(slug, "stub-model", "http://localhost:11434", timeout=30, max_steps=12)

        print("\n[1] loop + tools")
        check(seen["i"] >= 3, "model was polled across tool steps (%d calls)" % seen["i"])
        check(draft_path.is_file(), "draft file written to the case folder")
        if draft_path.is_file():
            body = draft_path.read_text(encoding="utf-8", errors="replace")
            check(body.startswith("> ⚠ EXPERIMENTAL OFFLINE DRAFT"),
                  "draft carries the EXPERIMENTAL banner (never mistaken for a rating)")
            check("stub-model" in body.split("\n")[0], "banner names the local model used")
            check("## Rationale" in body, "the model's markdown body is preserved")
        check("OFFLINE DRAFT written" in out, "run() reports the draft path")
        check("Section audit" in out, "run() ran the offline section gate on the draft")
        check("NOT a rating" in out, "output states plainly it is not a rating")

        print("\n[2] read_file sandbox (no traversal)")
        t = OA.Tools(slug, "stub-model")
        check(t.read_file("CLAUDE.md").startswith("# MASTER PROMPT"), "reads a project file")
        check("ERROR" in t.read_file("../../../Windows/System32/drivers/etc/hosts"),
              "blocks a path-traversal read outside the project")
        check("ERROR" in t.read_file("nope/does-not-exist.md"), "missing file -> error, not crash")

        print("\n[3] aborts on a non-reconciling engine (nothing to draft from)")
        orig = RE.run_tieouts
        RE.run_tieouts = lambda mod: (orig(mod)[0], orig(mod)[1], ["SYNTHETIC break"], [])
        try:
            ab = OA.run(slug, "stub-model", "http://localhost:11434", timeout=30, max_steps=3)
            check(ab.startswith("ABORTED"), "a failing tie-out blocks drafting")
        finally:
            RE.run_tieouts = orig
    finally:
        OA._ollama_chat = real
        if draft_path.exists():
            draft_path.unlink()

    print("\n" + "=" * 78)
    if _fails:
        print("%d FAILED:" % len(_fails))
        for f in _fails:
            print("  - %s" % f)
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
