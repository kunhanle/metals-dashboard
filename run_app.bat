@echo off
echo Starting Stock-Metal Correlation Tool...

:: Start Backend
start "Backend Server" cmd /k "cd backend && python app.py"

:: Start Frontend
start "Frontend Client" cmd /k "cd frontend && npm run dev"

:: Wait a moment for servers to spin up then open browser
timeout /t 5
start http://localhost:8030

echo.
echo Application started!
echo Backend: http://localhost:5000
echo Frontend: http://localhost:8030
echo.
pause
