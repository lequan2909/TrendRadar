@echo off
chcp 65001 >nul
echo ========================================
echo Setup TrendRadar - Python Virtual Environment
echo ========================================
echo.

REM Kiểm tra Python
echo [1/5] Kiểm tra Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Lỗi: Python chưa được cài đặt
    echo Vui lòng cài Python từ: https://www.python.org/downloads/
    pause
    exit /b 1
)

python --version
echo ✅ Python đã cài đặt
echo.

REM Tạo virtual environment
echo [2/5] Tạo virtual environment...
if exist venv (
    echo ⚠️  Thư mục venv đã tồn tại, bạn có muốn xóa và tạo lại không?
    choice /C YN /M "Xóa và tạo lại venv (Y/N)"
    if errorlevel 2 goto skip_create
    
    echo Đang xóa venv cũ...
    rmdir /s /q venv
)

python -m venv venv
if %errorlevel% neq 0 (
    echo ❌ Lỗi: Không thể tạo virtual environment
    pause
    exit /b 1
)

echo ✅ Virtual environment đã được tạo
echo.

:skip_create

REM Activate venv
echo [3/5] Kích hoạt virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ❌ Lỗi: Không thể kích hoạt virtual environment
    pause
    exit /b 1
)

echo ✅ Virtual environment đã được kích hoạt
echo.

REM Upgrade pip
echo [4/5] Nâng cấp pip...
python -m pip install --upgrade pip
echo ✅ pip đã được nâng cấp
echo.

REM Cài đặt dependencies
echo [5/5] Cài đặt dependencies từ requirements.txt...
if not exist requirements.txt (
    echo ❌ Lỗi: Không tìm thấy file requirements.txt
    pause
    exit /b 1
)

pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Lỗi: Không thể cài đặt dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies đã được cài đặt
echo.

echo ========================================
echo ✅ Setup hoàn tất!
echo ========================================
echo.
echo Để sử dụng TrendRadar:
echo 1. Kích hoạt venv: venv\Scripts\activate.bat
echo 2. Chạy: python main.py
echo.
echo Để thoát venv: deactivate
echo.
pause
