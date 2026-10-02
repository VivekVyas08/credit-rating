@echo off
rem ============================================================
rem   Credit Rating Tool - Windows launcher
rem   Double-click this file to start the web app, then open
rem   http://localhost:5050 in your browser. Ctrl+C here stops it.
rem ============================================================
cd /d "%~dp0"

where python >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Install it from https://www.python.org/downloads/ ^(tick "Add python.exe to PATH"^) and start this again.
    pause
    exit /b 1
)

echo Checking dependencies (first run may take a few minutes)...
rem The offline runtime is installed separately so that, if it cannot be installed on this
rem machine, everything else still installs and the tool still starts (Online mode works without it).
findstr /v /i /b "llama-cpp-python" requirements.txt > "%TEMP%\credit-rating-core.txt"
python -m pip install --quiet --prefer-binary -r "%TEMP%\credit-rating-core.txt"
if errorlevel 1 echo WARNING: some packages failed to install - the tool may not start.
python -m pip install --quiet --prefer-binary --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu llama-cpp-python
if errorlevel 1 echo NOTE: the offline model runtime ^(llama-cpp-python^) did not install. Online mode still works.

echo.
echo Starting Credit Rating Tool - opening http://localhost:5050
echo Keep this window open. Press Ctrl+C to stop.
start "" http://localhost:5050
python "webapp\app.py"

echo.
echo Server stopped. Press any key to close.
pause >nul
