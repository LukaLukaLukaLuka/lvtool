@echo off
if "%~1"=="" (
    echo Usage: touch filename
    exit /b
)
echo. > "%~1"
