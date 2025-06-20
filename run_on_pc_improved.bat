@echo off
echo === Autonomous Underwater Robot - PC Development Mode ===
echo.
echo Starting the web application in development mode...
echo This will use mock hardware components for testing.
echo.

cd /d "%~dp0"

REM Check for Node.js and npm
where npm >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: npm not found. Please install Node.js and npm first.
    echo Download from: https://nodejs.org/
    echo.
    pause
    exit /b 1
)

echo Node.js version:
node --version
echo npm version:
npm --version
echo.

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
if not exist "node_modules" (
    echo Installing React dependencies...
    call npm install
)
start "React Frontend" cmd /k "npm start"

echo.
echo Both servers are starting...
echo - Flask backend: http://localhost:5000
echo - React frontend: http://localhost:3000
echo.
echo Press any key to exit...
pause >nul
