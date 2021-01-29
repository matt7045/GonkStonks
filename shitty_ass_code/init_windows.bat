echo.off
python -V > "version.txt"
set /p version=<version.txt
IF NOT "%version:~0,8%"=="Python 3" (
    echo Installing Python 3
    IF "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    bitsadmin /transfer myDownloadJob /download /priority FOREGROUND https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe %CD%/py_installer39.exe
    py_installer39.exe
    ) ELSE (
    bitsadmin /transfer myDownloadJob /download /priority FOREGROUND https://www.python.org/ftp/python/3.9.1/python-3.9.1.exe %CD%/py_installer39.exe
    py_installer39.exe
    )
    del py_installer39.exe
    start pip_stuff.bat
    del version.txt
    echo {} > cache.json
) ELSE (
    echo Python already installed.
    del version.txt
    echo {} > cache.json
    echo Starting Gonk Stonks! Good Luck!

    python main.py
    )



