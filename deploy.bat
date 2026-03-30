@echo off
REM --- Windows batch wraper for deployment tool ---
REM --- usage= deploy [args] ---

REM Get the directory of this script
set SCRIPT_DIR=%~dp0

REM Try py3, then py
where python3 >nul 2>nul
if %errorlevel%==0 (
    python3 "%SCRIPT_DIR%deploy.py" %*
    exit /b %errorlevel%
)
where python >nul 2>nul
if %errorlevel%==0 (
    python "%SCRIPT_DIR%deploy.py" %*
    exit /b %errorlevel%
)

echo [✗] not launched & not installed
exit /b 1
