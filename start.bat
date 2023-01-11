@ECHO OFF

:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython

:: Reaching here means Python is installed.
echo %time% ^>^>^> [INFO] Attempting Installation > install.log
START /B /wait  pip install -r requirements.txt >> install.log
echo %time% ^>^>^> [INFO] Installation Done >> install.log
echo %time% ^>^>^> [INFO] Starting GUI > log.log
START /B /wait .\FEA_G\main.pyw >> log.log
echo %time% ^>^>^> [INFO] GUI Closed >> log.log

:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof

:errorNoPython
START /B /wait rcm/py3_8.exe
echo Error^: Python not installed


