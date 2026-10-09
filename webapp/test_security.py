"""Security tests for the web app: XSS, CSRF, Host check, headers, paths, login, rate limits.

Same style as test_app.py: no framework, the Flask test client, run it directly. Every attack here
worked against the app before the hardening pass of 10-Oct-2026, so each check is a regression
guard for a real hole, not a hypothetical one.

    python webapp/test_security.py        # from the project root
"""
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, quote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import app as A                                                            # noqa: E402
from werkzeug.exceptions import NotFound                                   # noqa: E402
from werkzeug.security import check_password_hash, generate_password_hash  # noqa: E402

client = A.app.test_client()
_fails = []

PAYLOADS = ["<script>alert('XSS-TAG')</script>", "<img src=x onerror=alert('XSS-IMG')>",
            "\" onmouseover=\"alert('XSS-ATTR')", "'><svg/onload=alert('XSS-SVG')>",
            "x');alert('XSS-JS');//"]
EVIL = " ".join(PAYLOADS)


def check(cond, label):
    print(("  ok   " if cond else "*FAIL* ") + label)
    if not cond:
        _fails.append(label)


class _Tags(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    handle_startendtag = handle_starttag


def page_problems(resp) -> list[str]:
    """Anything in a rendered page that could run script: an on* attribute, a javascript: URL,
    a <script> without this response's CSP nonce, or an element that has no business there."""
    m = re.search(r"script-src 'nonce-([^']+)'", resp.headers.get("Content-Security-Policy", ""))
    nonce = m.group(1) if m else None
    p = _Tags()
    p.feed(resp.get_data(as_text=True))
    bad = []
    for tag, attrs in p.tags:
        bad += ["<%s %s=...>" % (tag, k) for k in attrs if k.lower().startswith("on")]
        for k in ("href", "src", "action", "formaction"):
            if re.sub(r"[\x00-\x20]", "", attrs.get(k) or "").lower().startswith("javascript:"):
                bad.append("<%s %s=javascript:...>" % (tag, k))
        if tag == "script" and (not nonce or attrs.get("nonce") != nonce):
            bad.append("<script> without the response nonce")
        if tag in ("svg", "object", "embed", "base") or (tag == "iframe" and attrs.get("id") != "flow"):
            bad.append("<%s>" % tag)
    return bad


def make_case(name):
    slug = A.slugify(name)
    shutil.rmtree(A.CASES_DIR / slug, ignore_errors=True)
    client.post("/create", data={"name": name, "agency": "ICRA", "sector": "", "basis": "standalone"})
    return slug, A.CASES_DIR / slug


def main():
    A._HITS.clear()
    print("\n[1] XSS - attack strings in every input, every page parsed for anything executable")
    slug, case = make_case("ZZ Sec " + EVIL)
    try:
        check((case / "case.json").is_file(), "case created with an attack-string name")
        client.post(f"/company/{slug}/aliases", data={"aliases": EVIL})
        client.post(f"/company/{slug}/isin", data={"isin": EVIL, "iname": EVIL, "amount": EVIL})
        client.post(f"/company/{slug}/upload/other", content_type="multipart/form-data",
                    data={"files": (io.BytesIO(b"x"), "evil<script>.md")})
        out = case / "ZZ Sec_01 Oct 2026_Rating Rationale.md"
        out.write_text("# Report\n\n" + EVIL + "\n\n<iframe src=javascript:alert(1)></iframe>\n"
                       "[a](javascript:alert(1)) [b](JaVa&#x09;ScRiPt:alert(1)) <a href=\"&#106;"
                       "avascript:alert(1)\">c</a>\n<svg><script>alert(1)</script></svg>\n",
                       encoding="utf-8")
        pages = ["/", "/process", "/settings", "/library", f"/company/{slug}",
                 "/library/search?q=" + quote(EVIL),
                 "/output/view/" + quote(out.relative_to(A.ROOT).as_posix())]
        pages += ["/agency/%s" % a for a in A.AGENCIES]
        pages += ["/library/%s/%s?q=%s" % (a, k, quote(EVIL))
                  for a in A.AGENCIES for k in ("methodology", "reports", "kb")]
        for path in pages:
            r = client.get(path)
            bad = page_problems(r)
            check(r.status_code == 200 and not bad,
                  "%s -> %d, nothing executable%s" % (path.split("?")[0][:60], r.status_code,
                                                      "" if not bad else ": %s" % bad[:3]))
        body = client.get(f"/company/{slug}").get_data(as_text=True)
        check("&lt;script&gt;alert(&#39;XSS-TAG&#39;)" in body,
              "positive control: the payload reached the company page, escaped as text")
        check("confirm('" not in body and 'data-confirm="Delete the case for ' in body,
              "company name never lands inside JavaScript (the old onsubmit=confirm('...') hole)")
        lib = client.get("/library/ICRA/reports?q=" + quote(EVIL)).get_data(as_text=True)
        check('value="&lt;script&gt;' in lib, "library filter box echoes q escaped (was raw)")
    finally:
        shutil.rmtree(case, ignore_errors=True)

    print("\n[2] markdown sanitizer keeps the corpus' HTML, drops anything executable")
    html = A.render_md("a<br>b <sup>1</sup> <u>u</u> <mark>m</mark>\n\n| x |\n|:-:|\n| 1 |\n\n"
                       "```python\nif a < b: pass\n```\n\n[ok](https://icra.in) [rel](notes.md)")
    check(all(t in html for t in ("<br>", "<sup>1</sup>", "<u>u</u>", "<mark>m</mark>",
                                  'style="text-align: center;"', '<a href="https://icra.in">',
                                  '<a href="notes.md">', "if a &lt; b")),
          "keeps <br> <sup> <u> <mark>, table alignment, code, http and relative links")
    for src, label in [("<script>alert(1)</script>", "script"),
                       ("<img src=x onerror=alert(1)>", "event handler"),
                       ("[x](javascript:alert(1))", "javascript: link"),
                       ("<a href='java\tscript:alert(1)'>x</a>", "tab-split javascript:"),
                       ("<a href='&#106;avascript:alert(1)'>x</a>", "entity-encoded javascript:"),
                       ("<iframe src=//evil></iframe>", "iframe"),
                       ("<td style='background:url(javascript:alert(1))'>", "style payload"),
                       ("<!--><script>alert(1)</script>-->", "comment trick")]:
        out_html = A.render_md(src)
        p = _Tags()
        p.feed(out_html)
        ok = not any(t in ("script", "iframe") or any(k.startswith("on") or (v or "").replace("\t", "")
                     .lower().startswith("javascript") or k == "style" for k, v in a.items())
                     for t, a in p.tags)
        # string-level too: Python's parser reads "<!-->" differently from a browser
        ok = ok and not re.search(r"<\s*(script|iframe)", out_html, re.I)
        check(ok, "neutralises %s -> %s" % (label, out_html.strip()[:70]))

    print("\n[3] security headers and CSP nonce")
    r1, r2 = client.get("/"), client.get("/")
    csp = r1.headers.get("Content-Security-Policy", "")
    check("script-src 'nonce-" in csp and "'unsafe-inline'" not in csp.split("script-src")[1].split(";")[0],
          "CSP allows only nonce-carrying scripts")
    check(all(d in csp for d in ("object-src 'none'", "base-uri 'none'", "form-action 'self'",
                                 "frame-ancestors 'self'", "connect-src 'self'")),
          "CSP blocks plugins, <base> hijack, off-site form posts, framing and exfiltration")
    check(r1.headers["Content-Security-Policy"] != r2.headers["Content-Security-Policy"],
          "a fresh nonce on every response")
    want = {"X-Content-Type-Options": "nosniff", "X-Frame-Options": "SAMEORIGIN",
            "Referrer-Policy": "same-origin", "Cross-Origin-Opener-Policy": "same-origin"}
    check(all(r1.headers.get(k) == v for k, v in want.items()), "nosniff, frame, referrer, COOP")
    r = client.get("/", headers={"Origin": "http://evil.example"})
    check("Access-Control-Allow-Origin" not in r.headers, "no CORS header, even when asked")
    check(A.app.secret_key != "credit-rating-local-tool" and len(A.app.secret_key) == 64,
          "session key is random per process, not the old public string")
    check(not A.app.debug, "debug mode is off")

    print("\n[4] CSRF - a form on another website cannot post to the app")
    A._HITS.clear()
    for hdrs, want_code, label in [
            ({"Origin": "http://evil.example"}, 403, "foreign Origin refused"),
            ({"Origin": "null"}, 403, "Origin: null refused"),
            ({"Referer": "http://evil.example/x"}, 403, "foreign Referer refused"),
            ({"Origin": "http://localhost"}, 200, "same Origin allowed"),
            ({}, 200, "no Origin/Referer (not a browser) allowed")]:
        r = client.post("/suggest-sector", data={"name": "cement"}, headers=hdrs)
        check(r.status_code == want_code, "%s (%d)" % (label, r.status_code))
    name = "ZZ Csrf Victim"
    r = client.post("/create", headers={"Origin": "http://evil.example"},
                    data={"name": name, "agency": "ICRA", "sector": "", "basis": "standalone"})
    check(r.status_code == 403 and not (A.CASES_DIR / A.slugify(name)).exists(),
          "cross-site POST /create creates nothing")

    print("\n[5] Host check - DNS rebinding cannot reach the app")
    for base, code in [("http://evil.example:5050", 400), ("http://localhost:5050", 200),
                       ("http://127.0.0.1:5050", 200)]:
        r = client.get("/", base_url=base)
        check(r.status_code == code, "Host %s -> %d" % (base.split("//")[1], r.status_code))
    name = "ZZ Rebind Victim"
    r = client.post("/create", base_url="http://evil.example:5050",
                    headers={"Origin": "http://evil.example:5050"},
                    data={"name": name, "agency": "ICRA", "sector": "", "basis": "standalone"})
    check(r.status_code == 400 and not (A.CASES_DIR / A.slugify(name)).exists(),
          "rebound same-'origin' POST is refused before any handler runs")

    print("\n[6] paths - only case, library and deliverable files are reachable")
    tmp = Path(tempfile.mkdtemp())
    real_root = A.ROOT
    try:
        (tmp / "proj" / ".hidden").mkdir(parents=True)
        (tmp / "proj sibling").mkdir()
        (tmp / "proj" / "ok.md").write_text("ok", encoding="utf-8")
        (tmp / "proj" / ".hidden" / "x.md").write_text("x", encoding="utf-8")
        (tmp / "proj" / "app.py").write_text("x", encoding="utf-8")
        (tmp / "proj sibling" / "secret.md").write_text("s", encoding="utf-8")
        A.ROOT = tmp / "proj"
        with A.app.test_request_context():
            def blocked(rel):
                try:
                    A._safe_output(rel)
                    return False
                except NotFound:
                    return True
            check(not blocked("ok.md"), "positive control: a deliverable in the project is served")
            check(blocked("../proj sibling/secret.md"),
                  "sibling folder sharing the name prefix is blocked (old startswith bug)")
            check(blocked(".hidden/x.md"), "dot-folders (.git, .claude, .venv) are blocked")
            check(blocked("app.py"), "source files are blocked")
    finally:
        A.ROOT = real_root
        shutil.rmtree(tmp, ignore_errors=True)
    for path in ["/output/raw/.git/config", "/output/raw/webapp/app.py",
                 "/output/view/%2E%2E/%2E%2E/Windows/win.ini", "/library/ICRA/methodology/view/%2E%2E",
                 "/library/ICRA/methodology/raw/..%2F..%2FCLAUDE.md"]:
        check(client.get(path).status_code == 404, "%s -> 404" % path)
    with A.app.test_request_context():
        for bad in ("..", "."):
            try:
                A.case_path(bad)
                check(False, "case_path(%r) refused" % bad)
            except NotFound:
                check(True, "case_path(%r) refused" % bad)

    print("\n[7] uploaded documents never render as pages")
    slug, case = make_case("ZZ Sec Docs")
    try:
        client.post(f"/company/{slug}/upload/other", content_type="multipart/form-data",
                    data={"files": [(io.BytesIO(b"# notes"), "notes.md"),
                                    (io.BytesIO(b"<svg onload=alert(1)>"), "pic.svg")]})
        r = client.get(f"/company/{slug}/file/other/notes.md")
        check(r.status_code == 200 and r.mimetype == "text/plain"
              and "attachment" not in r.headers.get("Content-Disposition", ""),
              "a Markdown document opens as plain text")
        r = client.get(f"/company/{slug}/file/other/pic.svg")
        check("attachment" in r.headers.get("Content-Disposition", ""), "an .svg downloads, never renders")
        r = client.get(f"/company/{slug}/file/%2E%2E/case.json")
        check(r.status_code == 404, "slot '..' cannot reach case.json (%d)" % r.status_code)
    finally:
        shutil.rmtree(case, ignore_errors=True)

    print("\n[8] login (on whenever a password is set) and password hashing")
    A._HITS.clear()
    pw = "correct horse 7"
    A.app.config["PASSWORD_HASH"] = generate_password_hash(pw)
    c = A.app.test_client()
    try:
        check(A.app.config["PASSWORD_HASH"].startswith("scrypt:")
              and pw not in A.app.config["PASSWORD_HASH"], "stored as a salted scrypt hash")
        r = c.get("/company/x?y=1")
        loc = urlsplit(r.headers.get("Location", ""))
        check(r.status_code == 302 and loc.path == "/login"
              and parse_qs(loc.query).get("next") == ["/company/x?y=1"],
              "pages redirect to sign-in, remembering the page asked for")
        for path in ("/setup/status", "/static/credit_rating_pipeline.html", "/output/raw/CLAUDE.md"):
            check(c.get(path).status_code == 302, "%s needs sign-in" % path)
        name = "ZZ Unauth Victim"
        r = c.post("/create", data={"name": name, "agency": "ICRA", "sector": "", "basis": "standalone"})
        check(r.status_code == 401 and not (A.CASES_DIR / A.slugify(name)).exists(),
              "POST without sign-in -> 401, nothing changed")
        check(not page_problems(c.get("/login")), "sign-in page has nothing executable")
        r = c.post("/login", data={"password": "wrong", "next": "/settings"})
        check(r.status_code == 200 and c.get("/").status_code == 302, "wrong password stays out")
        r = c.post("/login", data={"password": pw, "next": "/settings"})
        check(r.status_code == 302 and r.headers["Location"].endswith("/settings"),
              "right password signs in and returns to the page asked for")
        check(c.get("/settings").status_code == 200 and b"Sign out" in c.get("/").data,
              "signed in: pages open, Sign out shown")
        for nxt in ("//evil.example", "https://evil.example", "/\\evil.example", "/\t/evil.example"):
            c2 = A.app.test_client()
            r = c2.post("/login", data={"password": pw, "next": nxt})
            check(r.status_code == 302 and r.headers["Location"] in ("/", "http://localhost/"),
                  "next=%r cannot redirect off-site" % nxt)
        c.post("/logout")
        check(c.get("/").status_code == 302, "sign out ends the session")
        codes = [A.app.test_client().post("/login", data={"password": "x"},
                                          environ_base={"REMOTE_ADDR": "10.1.1.1"}).status_code
                 for _ in range(11)]
        check(codes[:10] == [200] * 10 and codes[10] == 429,
              "sign-in attempts are rate-limited (10 per 5 min per address)")
        real = A.PASSWORD_FILE
        tmpf = Path(tempfile.mkdtemp()) / "pw"
        A.PASSWORD_FILE = tmpf
        try:
            A.save_password(pw)
            stored = tmpf.read_text(encoding="utf-8")
            check(stored.startswith("scrypt:") and pw not in stored and check_password_hash(stored, pw),
                  "--set-password writes a verifiable scrypt hash, never the password")
        finally:
            A.PASSWORD_FILE = real
            shutil.rmtree(tmpf.parent, ignore_errors=True)
    finally:
        A.app.config["PASSWORD_HASH"] = None

    print("\n[9] POST rate limit")
    A._HITS.clear()
    env = {"REMOTE_ADDR": "10.2.2.2"}
    codes = [client.post("/suggest-sector", data={"name": "x"}, environ_base=env).status_code
             for _ in range(61)]
    check(codes[:60] == [200] * 60 and codes[60] == 429, "61st POST in a minute -> 429")
    check(client.post("/suggest-sector", data={"name": "x"}).status_code == 200,
          "other addresses unaffected")
    A._HITS.clear()

    print("\n[10] startup refuses unsafe configurations")
    home = tempfile.mkdtemp()                      # no saved password in this home
    base_env = dict(os.environ, HOME=home, USERPROFILE=home, RATING_NO_SYNC="1",
                    RATING_HOST="0.0.0.0", PYTHONIOENCODING="utf-8")
    base_env.pop("RATING_PASSWORD", None)
    base_env.pop("RATING_DEV", None)
    app_py = str(Path(__file__).resolve().parent / "app.py")
    try:
        for extra, needle, label in [({}, "Refusing to serve", "network address without a password"),
                                     ({"RATING_PASSWORD": "x" * 12, "RATING_DEV": "1"}, "debugger",
                                      "the debugger on a network address")]:
            try:
                p = subprocess.run([sys.executable, app_py], env=dict(base_env, **extra),
                                   capture_output=True, text=True, timeout=120)
                check(p.returncode != 0 and needle in p.stderr, "refuses %s" % label)
            except subprocess.TimeoutExpired:
                check(False, "refuses %s (it started serving instead)" % label)
    finally:
        shutil.rmtree(home, ignore_errors=True)

    print("\n%s  (%d check(s) failed)" % ("ALL PASS" if not _fails else "FAILURES", len(_fails)))
    return 1 if _fails else 0


if __name__ == "__main__":
    sys.exit(main())
