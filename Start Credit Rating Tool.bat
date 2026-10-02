@echo off
rem ============================================================
rem   Credit Rating Tool - Windows launcher
rem   Double-click this file to start the web app, then open
rem   http://localhost:5050 in your browser. Ctrl+C here stops it.
rem ============================================================
cd /d "%~dp0"

echo Checking dependencies (first run may take a few minutes)...
python -m pip install --quiet --prefer-binary ^
    --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu ^
    -r requirements.txt

echo.
echo Starting Credit Rating Tool - opening http://localhost:5050
echo Keep this window open. Press Ctrl+C to stop.
start "" http://localhost:5050
python "webapp\app.py"

echo.
echo Server stopped. Press any key to close.
pause >nul
