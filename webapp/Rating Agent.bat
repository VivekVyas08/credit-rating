@echo off
REM ---- Rating Agent - web app launcher ----
REM Double-click this file to start the intake dashboard, then open
REM http://127.0.0.1:5050 in your browser.

cd /d "%~dp0"

echo Checking dependencies...
python -m pip install --quiet -r requirements.txt

echo.
echo ============================================================
echo   Rating Agent - starting
echo   Open this in your browser:  http://127.0.0.1:5050
echo   Keep this window open. Press Ctrl+C here to stop.
echo ============================================================
echo.

REM Open the browser automatically after a short delay
start "" http://127.0.0.1:5050

python app.py

echo.
echo Server stopped. Press any key to close this window.
pause >nul
