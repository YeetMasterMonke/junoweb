@echo off
cd /d "%~dp0"
echo Starting Blog Server...
echo Make sure Flask is installed: pip install flask
echo.
python server.py
pause
