@echo off
REM RDP Configurator Launch Script
REM Encoding: UTF-8

setlocal enabledelayedexpansion
chcp 65001 > nul

cd /d "%~dp0"

if not exist venv (
    cls
    echo Creating virtual environment...
    python -m venv venv
)

cls
echo ====================================================
echo   RDP Configurator
echo ====================================================
echo.
call venv\Scripts\activate.bat
python main.py

pause
