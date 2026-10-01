#!/usr/bin/env python3
"""Tests for rate_engine.py's API path - the parts a dummy key cannot reach.

    python test_rate_engine.py

A fake API key exercises transport, authentication and error handling against the real
endpoint, and that is worth doing - it is a genuine live test. But a rejected key can never
exercise the SUCCESS path: request acceptance, response parsing, schema conformance, the
divergence arithmetic, or the failure branches that only occur after a 200. Those are covered
here by stubbing the SDK client, so every line downstream of a successful call is executed.

What each test proves is stated in its own docstring. Nothing here contacts the network.
"""

import json
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # this script now lives in tools/,
# one level below the project root - moved here 01-Sep-2026 to declutter the root.
sys.path.insert(0, str(ROOT))
import rate_engine as RE                                                  # noqa: E402

def _pick_case():
    """Any case with an engine - preferring the worked example.

    This used to hard-code one company's slug, which tied the test suite to one private case
    folder and made it fail anywhere that folder does not exist. The suite is about
    rate_engine's plumbing, not about any particular issuer, so it should run against whatever
    case is to hand.
    """
    import os
    override = os.environ.get("TEST_CASE_SLUG")
    if override:
        return override
    base = ROOT / "Companies"
    names = sorted(d.name for d in base.iterdir()
                   if (d / "compute_ratios.py").exists()) if base.is_dir() else []
    for preferred in ("example-manufacturing-co",):
        if preferred in names:
            return preferred
    # Not just any engine: rate_engine drives compute() and tieouts(), so the case must expose
    # the contract. Picking the first folder alphabetically found one that does not, and the
    # suite failed with a refactor instruction instead of a test result.
    for n in names:
        src = (base / n / "compute_ratios.py").read_text(encoding="utf-8", errors="replace")
        if "def compute(" in src and "def tieouts(" in src:
            return n
    raise SystemExit("no case under %s exposes compute() and tieouts() - the API-path tests "
                     "need one contract-conforming engine to exercise" % base)


SLUG = _pick_case()
_failures = []


def check(cond, label):
    print("   %-5s %s" % ("ok" if cond else "FAIL", label))
    if not cond:
        _failures.append(label)


# --------------------------------------------------------------------- SDK stubs
class _Block:
    def __init__(self, text):
        self.type, self.text = "text", text


class _Usage:
    input_tokens, output_tokens = 4321, 876


class _Resp:
    def __init__(self, text, stop_reason="end_turn", stop_details=None):
        self.content = [_Block(text)] if text is not None else []
        self.stop_reason = stop_reason
        self.stop_details = stop_details
        self.usage = _Usage()
        self._request_id = "req_test_0001"


VALID = {
    "long_term_grade": "AA+",
    "outlook": "Stable",
    "short_term_grade": "A1+",
    "key_strengths": ["Largest domestic stainless producer; PBILDT/tonne rising to ~21,640",
                      "Gearing held in a 0.36-0.46x band through a near-doubling of net block"],
    "key_weaknesses": ["Nickel and chrome price exposure the issuer does not control",
                       "Capex still in flight; earnings contribution behind the spend"],
    "principal_monitorable": "Commissioning the added melt capacity into utilisation",
    "reasoning": "PBILDT margin 12.94% on TOI of 42,954.66; interest coverage 9.79x.",
    "confidence": "high",
    "data_limitations_considered": "Acceptances not separately disclosed, so gearing is "
                                   "unadjusted and understates CareEdge's own measure.",
}


def _client_returning(resp_or_exc):
    class _Messages:
        def create(self, **kw):
            _Messages.last_kwargs = kw
            if isinstance(resp_or_exc, Exception):
                raise resp_or_exc
            return resp_or_exc

    class _Client:
        def __init__(self, *a, **k):
            self.messages = _Messages()
    return _Client, _Messages


def _patched(resp_or_exc, fn):
    """Run fn() with anthropic.Anthropic replaced, restoring it afterwards."""
    import anthropic
    real = anthropic.Anthropic
    Client, Messages = _client_returning(resp_or_exc)
    anthropic.Anthropic = Client
    try:
        return fn(), Messages
    finally:
        anthropic.Anthropic = real


def _api(resp_or_exc):
    d, mod, meta = RE.load_case(SLUG)
    R, n, failures, _ack = RE.run_tieouts(mod)
    assert not failures, "the real engine must reconcile before these tests mean anything"
    return _patched(resp_or_exc,
                    lambda: RE.engine_api(SLUG, mod, R, meta, n,
                                          RE.DEFAULT_MODEL, "high", "sk-ant-fake"))


# --------------------------------------------------------------------- tests
def test_success():
    """A 200 with schema-valid JSON parses into a complete rating view."""
    print("\n[1] success path")
    out, Messages = _api(_Resp(json.dumps(VALID)))
    check(out.get("available") is True, "result marked available")
    check(out.get("long_term_grade") == "AA+", "grade parsed (AA+)")
    check(out.get("outlook") == "Stable", "outlook parsed")
    check(out.get("model") == RE.DEFAULT_MODEL, "model recorded")
    check(out.get("usage", {}).get("input_tokens") == 4321, "token usage recorded")
    check(out.get("request_id") == "req_test_0001", "request id captured for support")
    for k in RE.SCHEMA["required"]:
        if k not in out:
            check(False, "required field carried through: %s" % k)
            return
    check(True, "all %d required schema fields present" % len(RE.SCHEMA["required"]))


def test_request_shape():
    """The request sends the documented parameters, and NO source documents."""
    print("\n[2] request shape")
    _out, Messages = _api(_Resp(json.dumps(VALID)))
    kw = Messages.last_kwargs
    check(kw["model"] == RE.DEFAULT_MODEL, "model passed through")
    check(kw["thinking"] == {"type": "adaptive"}, "adaptive thinking (not budget_tokens)")
    check(kw["output_config"]["effort"] == "high", "effort inside output_config")
    fmt = kw["output_config"]["format"]
    check(fmt["type"] == "json_schema", "structured output via output_config.format")
    check(fmt["schema"]["additionalProperties"] is False,
          "schema closed (additionalProperties false)")
    check("max_tokens" in kw and kw["max_tokens"] >= 4096, "max_tokens set generously")
    prompt = kw["messages"][0]["content"]
    check("VERIFIED RATIO SUITE" in prompt, "verified ratio suite is sent")
    check("UNVERIFIED INPUTS" in prompt or "NO TIE-OUT COVERS" in prompt,
          "unverified-input list is sent so the model can weigh evidence quality")
    check("DISCLOSED CONVENTIONS" in prompt, "disclosed conventions are sent")
    # The guardrail: no raw document text may reach the model.
    leaked = [m for m in ("Integrated Report", "NOTES TO CONSOLIDATED",
                          "Walker Chandiok", "annual report of the Company") if m in prompt]
    check(not leaked, "NO source-document text in the prompt (leaked: %s)" % leaked)


def test_refusal():
    """stop_reason 'refusal' is handled before .content is read."""
    print("\n[3] refusal")
    details = types.SimpleNamespace(category="cyber", explanation="x")
    out, _ = _api(_Resp(None, stop_reason="refusal", stop_details=details))
    check(out.get("available") is False, "marked unavailable")
    check("declined" in out.get("reason", ""), "reason explains the decline")
    check("cyber" in out.get("reason", ""), "refusal category surfaced")


def test_bad_json():
    """A 200 whose text is not JSON fails cleanly instead of raising."""
    print("\n[4] malformed response")
    out, _ = _api(_Resp("this is not json"))
    check(out.get("available") is False, "marked unavailable")
    check("not JSON" in out.get("reason", ""), "reason names the parse failure")


def test_api_errors():
    """Each SDK exception maps to a clean message, never a traceback."""
    print("\n[5] API error mapping")
    import anthropic, httpx
    req = httpx.Request("POST", "https://api.anthropic.com/v1/messages")

    def status(cls, code, body):
        resp = httpx.Response(code, request=req, json=body)
        try:
            return cls("boom", response=resp, body=body)
        except TypeError:
            return cls(response=resp, body=body)

    cases = [
        (status(anthropic.AuthenticationError, 401, {"error": {"message": "bad key"}}),
         "authentication failed"),
        (status(anthropic.NotFoundError, 404, {"error": {"message": "no model"}}),
         "not found"),
        (status(anthropic.PermissionDeniedError, 403, {"error": {"message": "nope"}}),
         "lacks permission"),
        (anthropic.APIConnectionError(request=req), "network error"),
    ]
    for exc, expect in cases:
        out, _ = _api(exc)
        ok = out.get("available") is False and expect in out.get("reason", "")
        check(ok, "%s -> %r" % (type(exc).__name__, out.get("reason", "")[:52]))


def test_divergence():
    """Notch arithmetic: the number a committee is shown must be right."""
    print("\n[6] divergence arithmetic")
    check(RE.notch_gap("AA", "AA") == 0, "same grade -> 0 notches")
    check(RE.notch_gap("AA", "AA+") == -1, "model one notch stronger -> -1")
    check(RE.notch_gap("AA", "AA-") == 1, "model one notch weaker -> +1")
    check(RE.notch_gap("AAA", "BBB") == 8, "AAA vs BBB -> 8 notches")
    check(RE.notch_gap("AA", "nonsense") is None, "unknown grade -> None, not a crash")


def test_key_handling():
    """The key is masked, and never appears in the JSON payload."""
    print("\n[7] credential hygiene")
    fake = "sk-ant-api03-" + "Z" * 80 + "END1"
    fp = RE.fingerprint(fake)
    check(fake not in fp, "fingerprint does not contain the key")
    check(fp.startswith("sk-ant-") and fp.endswith("(%d chars)" % len(fake)),
          "fingerprint shows prefix/suffix and length only: %s" % fp)
    check(RE.fingerprint(None) == "n/a", "no key -> 'n/a'")
    out, _ = _api(_Resp(json.dumps(VALID)))
    check("sk-ant" not in json.dumps(out), "no key material in the result payload")


def test_key_storage():
    """The --set-key store: round trip, precedence, and that nothing leaks.

    Runs against a TEMPORARY path, never the user's real key file. The real one is left
    untouched even if this test fails part-way - a test that can destroy a credential is not
    worth the coverage it buys.
    """
    import os
    import tempfile
    from pathlib import Path
    print("\n[8] key storage (--set-key / --show-key / --clear-key)")

    real = RE.KEY_FILE
    tmp = Path(tempfile.mkdtemp()) / "test_key"
    RE.KEY_FILE = tmp
    saved_env = {v: os.environ.pop(v, None)
                 for v in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN")}

    class A:
        api_key = None
        api_key_file = None

    try:
        check(RE.stored_key() is None, "no stored key -> None")
        k, d = RE.resolve_key(A())
        check(k is None and "SDK default" in d, "no stored key -> falls through to the SDK")

        FAKE = "sk-ant-api03-STORAGETEST-0000000000000000-zzzz"
        RE.store_key(FAKE)
        check(RE.stored_key() == FAKE, "stored key reads back byte-identical")

        k, d = RE.resolve_key(A())
        check(k == FAKE, "resolve_key returns the stored key")
        check("stored key at" in d, "resolve_key names the store as the source")
        check(FAKE not in d, "the source description does not contain the key")
        check(FAKE not in RE.fingerprint(k), "fingerprint does not contain the key")

        os.environ["ANTHROPIC_API_KEY"] = "sk-ant-from-the-environment"   # publish-scan-ok: fabricated fixture, not a credential
        k, d = RE.resolve_key(A())
        check(k is None and "environment variable" in d,
              "an environment variable outranks the stored key")
        os.environ.pop("ANTHROPIC_API_KEY")

        A.api_key = "sk-ant-explicit-flag"   # publish-scan-ok: fabricated fixture, not a credential
        k, _ = RE.resolve_key(A())
        check(k == "sk-ant-explicit-flag", "--api-key outranks the stored key")   # publish-scan-ok: fabricated fixture, not a credential
        A.api_key = None

        RE.store_key(RE.AGENT_SENTINEL)
        k, _ = RE.resolve_key(A())
        check(RE.is_sentinel(k), "the agent sentinel survives a store/read round trip")

        # POSITIVE CONTROL. Every check above passes when the store works; this proves they can
        # also fail. Without it "stored key reads back byte-identical" would still pass against
        # a store() that wrote nothing and a stored_key() that returned the input.
        tmp.write_text("something-else\n", encoding="utf-8")
        check(RE.stored_key() != RE.AGENT_SENTINEL,
              "control: a changed file IS noticed (these checks can fail)")

        tmp.unlink()
        check(RE.stored_key() is None, "deleting the file clears the stored key")
    finally:
        RE.KEY_FILE = real
        for v, val in saved_env.items():
            if val is not None:
                os.environ[v] = val
        if tmp.exists():
            tmp.unlink()
        check(RE.KEY_FILE == real, "the user's real key file was never touched")


def test_ui_model_pref():
    """The Settings dropdown must actually change what a run uses.

    This exists because the first version of that dropdown wrote a preference file nothing
    read - the control looked like it worked and changed nothing.
    """
    import json as _json
    import tempfile
    from pathlib import Path
    print("\n[9] web-app model preference")

    real = RE.UI_PREFS
    tmp = Path(tempfile.mkdtemp()) / "ui_prefs.json"
    RE.UI_PREFS = tmp
    try:
        check(RE.ui_model() == RE.DEFAULT_MODEL, "no prefs file -> the built-in default")

        other = next(m for m in RE.MODELS if m != RE.DEFAULT_MODEL)
        tmp.write_text(_json.dumps({"model": other}), encoding="utf-8")
        check(RE.ui_model() == other, "a stored choice becomes the default (%s)" % other)

        tmp.write_text(_json.dumps({"model": "not-a-model"}), encoding="utf-8")
        check(RE.ui_model() == RE.DEFAULT_MODEL,
              "an unknown model falls back rather than being passed through")

        tmp.write_text("{ this is not json", encoding="utf-8")
        check(RE.ui_model() == RE.DEFAULT_MODEL, "a corrupt prefs file does not crash a run")
    finally:
        RE.UI_PREFS = real
        if tmp.exists():
            tmp.unlink()
        check(RE.UI_PREFS == real, "the real prefs file was never touched")


# --------------------------------------------------------------------- ollama stubs (offline)
class _FakeHTTP:
    """A urlopen() return value: context-managed, with .read() for json.load()."""
    def __init__(self, payload):
        self._b = json.dumps(payload).encode("utf-8")

    def read(self, *a):
        return self._b

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


OLLAMA_OK = {"message": {"content": json.dumps(VALID)},
             "prompt_eval_count": 1234, "eval_count": 567}


def _ollama(urlopen_impl):
    """Call engine_ollama with urllib.request.urlopen swapped; capture the request sent."""
    import urllib.request
    d, mod, meta = RE.load_case(SLUG)
    R, n, failures, _ack = RE.run_tieouts(mod)
    assert not failures, "the real engine must reconcile before these tests mean anything"
    captured, real = {}, urllib.request.urlopen

    def spy(req, timeout=None):
        captured["req"] = req
        return urlopen_impl(req, timeout)
    urllib.request.urlopen = spy
    try:
        out = RE.engine_ollama(SLUG, mod, R, meta, n, "test-model", url="http://localhost:11434")
    finally:
        urllib.request.urlopen = real
    return out, captured.get("req")


def test_ollama_success():
    """A structured Ollama response parses into a complete, OFFLINE rating view."""
    print("\n[10] ollama success path (offline, stubbed)")
    out, _req = _ollama(lambda r, t: _FakeHTTP(OLLAMA_OK))
    check(out.get("available") is True, "result marked available")
    check(out.get("engine") == "ollama", "engine tagged ollama")
    check(out.get("long_term_grade") == "AA+", "grade parsed (AA+)")
    check(out.get("outlook") == "Stable", "outlook parsed")
    check(out.get("model") == "test-model", "model recorded")
    check(out.get("usage", {}).get("input_tokens") == 1234, "prompt tokens recorded")
    check(out.get("usage", {}).get("output_tokens") == 567, "output tokens recorded")
    for k in RE.SCHEMA["required"]:
        if k not in out:
            check(False, "required field carried through: %s" % k)
            return
    check(True, "all %d required schema fields present" % len(RE.SCHEMA["required"]))


def test_ollama_request_shape():
    """The request hits /api/chat with SCHEMA as the format, and sends NO documents."""
    print("\n[11] ollama request shape")
    _out, req = _ollama(lambda r, t: _FakeHTTP(OLLAMA_OK))
    check(req.full_url.endswith("/api/chat"), "POSTs to /api/chat")
    body = json.loads(req.data.decode("utf-8"))
    check(body["model"] == "test-model", "model in body")
    check(body["stream"] is False, "non-streaming (one JSON response)")
    check(body["format"] == RE.SCHEMA, "SCHEMA passed as the structured-output format")
    check(body["options"]["temperature"] == 0, "temperature 0 for reproducibility")
    check(body.get("think") is False, "thinking disabled (we want the JSON object, not a trace)")
    check([m["role"] for m in body["messages"]] == ["system", "user"], "system + user messages")
    prompt = body["messages"][1]["content"]
    check("VERIFIED RATIO SUITE" in prompt, "verified ratio suite is sent")
    # Same guardrail as the API engine: no raw document text may reach the model.
    leaked = [m for m in ("Integrated Report", "NOTES TO CONSOLIDATED",
                          "Walker Chandiok", "annual report of the Company") if m in prompt]
    check(not leaked, "NO source-document text in the prompt (leaked: %s)" % leaked)


def test_ollama_errors():
    """Model-not-pulled, server-down, bad JSON and missing fields all fail cleanly."""
    print("\n[12] ollama error handling")
    import io
    import urllib.error

    def raise_404(r, t):
        raise urllib.error.HTTPError("http://localhost:11434/api/chat", 404,
                                     "Not Found", {}, io.BytesIO(b"model not found"))
    out, _ = _ollama(raise_404)
    check(out.get("available") is False and "ollama pull" in out.get("reason", ""),
          "model not pulled -> pull instruction")

    def raise_conn(r, t):
        raise urllib.error.URLError("Connection refused")
    out, _ = _ollama(raise_conn)
    check(out.get("available") is False and "Ollama server" in out.get("reason", ""),
          "server down -> points at `ollama serve`")

    out, _ = _ollama(lambda r, t: _FakeHTTP({"message": {"content": "not json"}}))
    check(out.get("available") is False and "not JSON" in out.get("reason", ""),
          "non-JSON content -> clean parse failure")

    partial = {k: v for k, v in VALID.items() if k != "confidence"}
    out, _ = _ollama(lambda r, t: _FakeHTTP({"message": {"content": json.dumps(partial)}}))
    check(out.get("available") is False and "missing required" in out.get("reason", ""),
          "missing required field -> rejected, not shipped")


def test_sdk_credential_detection():
    """sdk_has_credential() reflects a RESOLVED key/token, not just that the client constructed.

    Regression: the old version returned True unconditionally because constructing the SDK client
    succeeds with no key, so the Settings page claimed a credential the run then could not find.
    The client is stubbed so the three cases are deterministic and portable.
    """
    import anthropic
    print("\n[13] sdk credential detection")
    real = anthropic.Anthropic
    try:
        anthropic.Anthropic = lambda *a, **k: types.SimpleNamespace(api_key=None, auth_token=None)
        check(RE.sdk_has_credential() is False,
              "no resolved key/token -> False (the false positive this fixes)")
        anthropic.Anthropic = lambda *a, **k: types.SimpleNamespace(api_key="sk-ant-x", auth_token=None)  # publish-scan-ok: stub
        check(RE.sdk_has_credential() is True, "a resolved api_key -> True")
        anthropic.Anthropic = lambda *a, **k: types.SimpleNamespace(api_key=None, auth_token="tok")
        check(RE.sdk_has_credential() is True, "a resolved auth_token -> True")
    finally:
        anthropic.Anthropic = real


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:                                                     # noqa: BLE001
        pass
    print("=" * 78)
    print("rate_engine.py - API path tests (stubbed SDK; no network)")
    print("=" * 78)
    for fn in (test_success, test_request_shape, test_refusal, test_bad_json,
               test_api_errors, test_divergence, test_key_handling, test_key_storage,
               test_ui_model_pref,
               test_ollama_success, test_ollama_request_shape, test_ollama_errors,
               test_sdk_credential_detection):
        fn()
    print("\n" + "=" * 78)
    if _failures:
        print("%d FAILED:" % len(_failures))
        for f in _failures:
            print("  - %s" % f)
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
