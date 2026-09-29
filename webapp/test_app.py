"""Smoke tests for the intake web app - the routes must render and a case must round-trip.

No framework (ponytail): plain asserts via the Flask test client, one file, run it directly.
It catches exactly the class of regression that an edit to app.py can introduce silently - a
route that now 500s, a template f-string that breaks, a renamed helper - which nothing else in
this project would notice, since every existing test lives under tools/ and none imports app.py.

    python webapp/test_app.py        # from the project root
    python test_app.py               # from webapp/
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import app as A                                                            # noqa: E402

client = A.app.test_client()
_fails = []


def check(cond, label):
    print(("  ok   " if cond else "*FAIL* ") + label)
    if not cond:
        _fails.append(label)


def url(endpoint, **kw):
    with A.app.test_request_context():
        return A.url_for(endpoint, **kw)


def get_ok(path, label):
    r = client.get(path)
    check(r.status_code == 200, "%s -> 200 (got %d)" % (label, r.status_code))
    return r


def main():
    print("\n[1] static pages render")
    get_ok(url("agency_picker"), "GET /")
    get_ok(url("settings"), "GET /settings")
    get_ok(url("library"), "GET /library")
    get_ok(url("library_search") + "?q=titan", "GET /library/search")
    get_ok(url("process_flow"), "GET /process")

    print("\n[2] every agency dashboard renders")
    for agency in A.AGENCIES:
        get_ok(url("agency_dashboard", agency=agency), "GET dashboard %s" % agency)

    print("\n[3] case create -> view -> audit -> delete round-trip")
    name = "ZZ Smoke Test Co"
    slug = A.slugify(name)
    case_dir = A.CASES_DIR / slug
    if case_dir.exists():                       # leftover from a failed prior run
        shutil.rmtree(case_dir, ignore_errors=True)
    try:
        r = client.post(url("create"),
                        data={"name": name, "agency": "ICRA", "sector": "", "basis": "standalone"},
                        follow_redirects=True)
        check(r.status_code == 200, "POST /create -> 200")
        check(case_dir.is_dir(), "case folder created on disk")
        check((case_dir / "case.json").is_file(), "case.json written")

        check(get_ok(url("company", slug=slug), "GET company page").status_code == 200,
              "company page renders")

        r = client.post(url("run_audit", slug=slug), follow_redirects=True)
        check(r.status_code == 200, "POST audit -> 200")
        audit = A.load_case(slug).get("audit")
        check(isinstance(audit, dict) and "ready" in audit, "audit verdict cached in case.json")
        check(audit and audit.get("ready") is False,
              "bare case is NOT ready (no rationale/workpaper yet)")

        r = client.post(url("delete_case", slug=slug), follow_redirects=True)
        check(r.status_code == 200, "POST delete_case -> 200")
        check(not case_dir.exists(), "case folder removed on delete")
    finally:
        if case_dir.exists():
            shutil.rmtree(case_dir, ignore_errors=True)

    print("\n%s  (%d check(s) failed)" % ("ALL PASS" if not _fails else "FAILURES", len(_fails)))
    return 1 if _fails else 0


if __name__ == "__main__":
    sys.exit(main())
