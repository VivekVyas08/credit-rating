# Credit Rating — Web App

The browser side of the Credit Rating tool: cases, documents, instruments, the reference library,
the outputs and the settings. It prepares the work and shows the results; the rating itself is
produced by a Claude Code session on this project (see the main [README](../README.md#how-it-works)).

## Start

Double-click **`Start Credit Rating Tool.bat`** (Windows) or **`Start Credit Rating Tool.command`**
(macOS/Linux) in the project root. The browser opens <http://localhost:5050>. Keep the console window
open while you work; Ctrl+C in it stops the app.

From a terminal, in the project root:

```bash
python webapp/app.py
```

The launchers install everything from the project's `requirements.txt`. `webapp/requirements.txt`
is the web-app-only subset, plus the optional packages for reading scanned PDFs.

## The pages

| Page | What it is for |
|---|---|
| **Cases** | Choose ICRA, CRISIL or CareEdge, then create a case: company name, sector (each agency's own list, with a *Suggest sector* helper) and analytical basis. |
| **Case page** | 1 · documents by checklist slot (uploads convert to Markdown in the background) · 2 · methodology files, pre-selected for the sector · 3 · instruments (ISINs) · 4 · a prompt for a dedicated Claude session · 5 · *Request rating* / *Request research* · 6 · the outputs, opened in the browser · 7 · *Check readiness* (the delivery audit). |
| **Reference Library** | Each agency's methodology papers, published rationales and the shared knowledge base, with search across all three. |
| **Process Flow** | The rating procedure as a flowchart: phases, gates, and where each failure loops back. |
| **Settings** | API key, Claude model, Online/Offline mode, and the code-sync status. |
| **Mode switch** (header) | Online (Claude API, the default) or Offline (the built-in model, under development). It sets which engine a rating view uses. |

Online is the default, so nothing is downloaded on first start. If you switch to Offline and the
model is not on the machine yet, every page shows a setup screen while the model downloads and is
checked against its SHA-256; you can continue in Online mode instead.

## API key

Enter it under **Settings**. The key is never sent back to the page, only a masked fingerprint
(`sk-ant-...zzzz (46 chars)`). It is stored in your **home folder**, not in this project, so it never
travels with the project folder or the repository. Enter `1234` instead of a key to hand runs to a
local Claude Code agent rather than the API. On Windows the file is protected by your user profile's
permissions; on macOS/Linux it is made readable by you only.

The same store backs the command line:

```bash
python tools/rate_engine.py --show-key     # which credential is in use, and where it lives
python tools/rate_engine.py --set-key      # set one from a terminal
python tools/rate_engine.py --clear-key
```

**Settings never starts a rating.** A run can spend money, so it is started where you can see its
output: from Claude Code, or `python tools/rate_engine.py <case>` in a terminal.

## Security

The app listens on this computer only and needs no login there. To serve it to other machines it
requires a password (`python webapp/app.py --set-password`, or `RATING_PASSWORD`); see
[Security](../README.md#security) in the main README for the full list of protections.

## After an update

The app does not reload itself. Stop it (Ctrl+C in its window) and start it again with the launcher.
