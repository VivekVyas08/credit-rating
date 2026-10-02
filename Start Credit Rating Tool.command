#!/bin/bash
# ============================================================
#   Credit Rating Tool - macOS / Linux launcher
#   Double-click (macOS) or run this file to start the web app,
#   then open http://localhost:5050 in your browser. Ctrl+C stops it.
#
#   First time on a Mac: if double-click is blocked, right-click ->
#   Open, or run once:  chmod +x "Start Credit Rating Tool.command"
# ============================================================
cd "$(dirname "$0")" || exit 1

# Prefer python3; fall back to python.
PY=python3
command -v "$PY" >/dev/null 2>&1 || PY=python
if ! command -v "$PY" >/dev/null 2>&1; then
    echo "Python 3 is not installed. Install it from https://www.python.org/downloads/ and start this again."
    read -r -p "Press Enter to close." _
    exit 1
fi

# A private environment: Homebrew/system Python refuses a plain 'pip install' (PEP 668).
if [ ! -x .venv/bin/python ]; then
    echo "Creating a private Python environment in .venv (first run only)..."
    "$PY" -m venv .venv || { echo "Could not create .venv - is the python venv module installed?"; exit 1; }
fi
VPY=.venv/bin/python

echo "Checking dependencies (first run may take a few minutes)..."
# The offline runtime is installed separately so that, if it cannot be built on this machine,
# everything else still installs and the tool still starts (Online mode works without it).
grep -v -i '^llama-cpp-python' requirements.txt > .venv/requirements-core.txt
"$VPY" -m pip install --quiet --prefer-binary -r .venv/requirements-core.txt \
    || echo "WARNING: some packages failed to install - the tool may not start."
"$VPY" -m pip install --quiet --prefer-binary \
    --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu llama-cpp-python \
    || echo "NOTE: the offline model runtime (llama-cpp-python) did not install. On a Mac run 'xcode-select --install' and start this again. Online mode still works."

echo
echo "Starting Credit Rating Tool - opening http://localhost:5050"
echo "Keep this window open. Press Ctrl+C to stop."
# open the browser after a short delay (macOS 'open', else Linux 'xdg-open')
( sleep 3; (open http://localhost:5050 2>/dev/null || xdg-open http://localhost:5050 2>/dev/null) ) &

"$VPY" webapp/app.py
