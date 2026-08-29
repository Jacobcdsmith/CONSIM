#!/bin/bash
#
# Build script for CONSIM executable
# Creates a standalone executable for the consciousness simulation
#

set -e  # Exit on any error

echo "🧠 Building CONSIM Standalone Executable..."
echo "=========================================="

# Check if we're in the right directory
if [ ! -f "consim_launcher.py" ]; then
    echo "❌ Error: Must run from CONSIM project root directory"
    echo "   Looking for consim_launcher.py"
    exit 1
fi

# Check if PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "📦 Installing PyInstaller..."
    pip install pyinstaller
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ __pycache__/ src/__pycache__/

# Build the executable
echo "🔨 Building executable with PyInstaller..."
pyinstaller consim.spec --clean --noconfirm

# Check if build was successful
if [ -f "dist/CONSIM" ] || [ -f "dist/CONSIM.exe" ]; then
    echo "✅ Build successful!"
    echo ""
    echo "📁 Executable location:"
    ls -la dist/
    echo ""
    echo "🚀 To run the executable:"
    if [ -f "dist/CONSIM.exe" ]; then
        echo "   ./dist/CONSIM.exe"
        echo "   Or double-click dist/CONSIM.exe"
    else
        echo "   ./dist/CONSIM"
        echo "   Or: chmod +x dist/CONSIM && ./dist/CONSIM"
    fi
    echo ""
    echo "💡 Command line options:"
    echo "   --no-browser    Don't auto-open browser"
    echo "   --port=8080     Use custom port (default: 8000)"
    echo ""
    echo "🌐 The simulation will be available at http://localhost:8000"
else
    echo "❌ Build failed - executable not found in dist/"
    exit 1
fi