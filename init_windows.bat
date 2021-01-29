echo.off
python -V > "version.txt"
set /p version=<version.txt
IF NOT "%version:~0,10%"=="Python 3.9" (
    echo Installing Python 3.9
    IF "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    bitsadmin /transfer myDownloadJob /download /priority normal https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe %CD%/py_installer39.exe
    py_installer39.exe
    ) ELSE (
    bitsadmin /transfer myDownloadJob /download /priority normal https://www.python.org/ftp/python/3.9.1/python-3.9.1.exe %CD%/py_installer39.exe
    py_installer39.exe
    )
    del py_installer39.exe
) ELSE (
    echo Python already installed.
    )
del version.txt
python -m pip install requests
pip install alpaca_trade_api

echo Starting Gonk Stonks! Good Luck!

python main.py
