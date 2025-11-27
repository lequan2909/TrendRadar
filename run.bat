@echo off
chcp 65001 >nul

REM Kiểm tra venv
if not exist venv (
    echo ❌ Virtual environment chưa được tạo!
    echo Chạy: setup-venv.bat để tạo venv
    pause
    exit /b 1
)

REM Kích hoạt venv
call venv\Scripts\activate.bat

REM Load .env nếu có python-dotenv
python -c "import dotenv" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Loading .env file...
)

REM Chạy TrendRadar
echo.
echo ========================================
echo 🚀 TrendRadar đang chạy...
echo ========================================
echo.
python main.py

REM Tự động deactivate khi thoát
deactivate
