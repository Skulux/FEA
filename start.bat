@ECHO OFF & setlocal

:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython

goto:program

:errorNoPython
echo WScript.Echo MsgBox("Missing Python Install\nStart Installer?", 4, "Installation") >> %temp%\pyinstaller.vbs
for /f "delims=" %%i in ('cscript //nologo %temp%\pyinstaller.vbs') do set answer=%%i
del %temp%\pyinstaller.vbs
if "%answer%" == "6" goto install
if "%answer%" == "7" goto deny


:install
START /B /wait rcm/py3_8.exe
goto program

:deny
exit


:program
echo %time% ^>^>^> [INFO] Attempting Installation > install.log
START /B /wait  pip install -r requirements.txt >> install.log
echo %time% ^>^>^> [INFO] Installation Done >> install.log
echo %time% ^>^>^> [INFO] Starting GUI > log.log
START /B /wait .\FEA_G\main.pyw >> log.log
echo %time% ^>^>^> [INFO] GUI Closed >> log.log