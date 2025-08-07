@echo off
REM Build script for CONSIM executable (Windows)
REM Creates a standalone executable for the consciousness simulation

echo 🧠 Building CONSIM Standalone Executable...
echo ==========================================

REM Check if we're in the right directory
if not exist "consim_launcher.py" (
    echo ❌ Error: Must run from CONSIM project root directory
    echo    Looking for consim_launcher.py
    pause
    exit /b 1
)

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo 📦 Installing PyInstaller...
    pip install pyinstaller
)

REM Clean previous builds
echo 🧹 Cleaning previous builds...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "__pycache__" rmdir /s /q "__pycache__"
if exist "src\__pycache__" rmdir /s /q "src\__pycache__"

REM Build the executable
echo 🔨 Building executable with PyInstaller...
pyinstaller consim.spec --clean --noconfirm

REM Check if build was successful
if exist "dist\CONSIM.exe" (
    echo ✅ Build successful!
    echo.
    echo 📁 Executable location:
    dir dist\
    echo.
    echo 🚀 To run the executable:
    echo    dist\CONSIM.exe
    echo    Or double-click dist\CONSIM.exe
    echo.
    echo 💡 Command line options:
    echo    --no-browser    Don't auto-open browser
    echo    --port=8080     Use custom port ^(default: 8000^)
    echo.
    echo 🌐 The simulation will be available at http://localhost:8000
) else (
    echo ❌ Build failed - executable not found in dist\
    pause
    exit /b 1
)

pause