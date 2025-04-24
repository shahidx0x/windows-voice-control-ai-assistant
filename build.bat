@echo off
setlocal EnableDelayedExpansion

echo Cleaning previous builds...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"

echo Installing requirements...
pip install -r requirements.txt
if !errorlevel! neq 0 (
    echo Failed to install requirements
    pause
    exit /b 1
)

echo Building executable...
pyinstaller --clean ^
    build.spec

if !errorlevel! neq 0 (
    echo Build failed!
    pause
    exit /b 1
) else (
    echo Build completed successfully!
    echo Executable can be found in the dist folder
)

pause