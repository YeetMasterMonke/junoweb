@echo off
cd /d "%~dp0"
echo Starting Blog Server...
echo Make sure Flask is installed: pip install flask
echo.
echo Opening blog editor in browser...
timeout /t 2 /nobreak
start http://127.0.0.1:5000/blog-admin.html
python server.py
pause
