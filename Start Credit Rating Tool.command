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

echo "Checking dependencies (first run may take a few minutes)..."
"$PY" -m pip install --quiet --prefer-binary \
    --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu \
    -r requirements.txt

echo
echo "Starting Credit Rating Tool - opening http://localhost:5050"
echo "Keep this window open. Press Ctrl+C to stop."
# open the browser after a short delay (macOS 'open', else Linux 'xdg-open')
( sleep 2; (open http://localhost:5050 2>/dev/null || xdg-open http://localhost:5050 2>/dev/null) ) &

"$PY" webapp/app.py
