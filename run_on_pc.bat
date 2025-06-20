@echo off
echo === Autonomous Underwater Robot - PC Development Mode ===
echo.
echo Starting the web application in development mode...
echo This will use mock hardware components for testing.
echo.

cd /d "%~dp0"

echo Activating virtual environment...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo Virtual environment not found. Please run setup.sh first.
    pause
    exit /b 1
)

echo Starting Flask backend server...
start "Flask Backend" cmd /k "cd rpi && python app.py"

echo Waiting for Flask server to start...
timeout /t 5 /nobreak >nul

echo Starting React frontend server...
cd web-dashboard
start "React Frontend" cmd /k "npm start"

echo.
echo Both servers are starting...
echo - Flask backend: http://localhost:5000
echo - React frontend: http://localhost:3000
echo.
echo Press any key to exit...
pause >nul
