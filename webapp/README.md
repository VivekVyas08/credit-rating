# Credit Rating — Web App

Document intake, ISIN checklist and output viewer for the Credit Rating project.

## Start

Double-click **`Start Credit Rating Tool.bat`** in the project root
(`Credit Rating\`), then open http://localhost:5050 — the browser
opens automatically. Keep the black console window open while using the
app; press Ctrl+C in it (or close it) to stop.

Manual start (any terminal):

```
cd webapp
python app.py
```

## Requirements

Python 3 with `flask` and `markdown` (`pip install -r requirements.txt`).

## What it does

1. **Rating cases** — one per company, stored in `Companies\<company>\`.
2. **Required-document checklist** — upload annual reports (3+ yrs),
   quarterly results, term sheets, sector assumptions, etc. Uploads start
   automatically on file selection; ticks turn green when a slot is complete.
3. **ISIN checklist** — add any number of instruments (comma-separated ISINs
   supported); tick each once its term sheet is uploaded.
4. **Get the output** — copy the generated kickoff prompt into a Claude
   session on this project, or click "Request rating" and later tell Claude
   to "process the pending rating requests".
5. **Output viewer** — generated rationales and workpapers are auto-detected
   and rendered in the browser.

## Settings — API key and model

The web app had no way to supply a credential: `rate_engine.py` took one from the command line
or an environment variable, neither of which a browser can reach. The **Settings** tab (top nav)
now holds both.

**API key.** A masked field; the key is never sent back to the page, only a masked fingerprint
(`sk-ant-...zzzz (46 chars)`). It is written to your **home folder**, deliberately not into this
project folder — the folder gets zipped and emailed with the rating reports in it, and a
credential that travels with the deliverable is a credential that leaks. Enter `1234` instead of
a key to route work to a local Claude Code agent rather than the API.

On Windows the file is protected by your user profile's NTFS permissions rather than the `0600`
mode the code requests; the app says so when it stores one rather than implying protection that
is not there.

**Model.** Sets the default model for API runs. It is read by `rate_engine.py` at startup, so
choosing it here changes what an actual run uses; an explicit `--model` on the command line
still wins. (The first version of this dropdown wrote a preference file that nothing read.)

The same store backs the command line, so a key set in either place works in both:

```bash
python rate_engine.py --show-key     # which credential is in use, and where it lives
python rate_engine.py --set-key      # set one from a terminal instead
python rate_engine.py --clear-key
```

**Settings does not start a rating.** An API or agent run spends money, and that belongs where
you can see the output — run it from a terminal in the project root.

### If Settings is missing after an update

The app does not auto-reload. Stop the running server (Ctrl+C in its window, or close it) and
start it again with `Rating Agent.bat`.
