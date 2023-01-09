@ECHO OFF
echo %time% ^>^>^> [INFO] Attempting Installation > install.log
START /B /wait  pip install -r requirements.txt >> install.log
echo %time% ^>^>^> [INFO] Installation Done >> install.log
echo %time% ^>^>^> [INFO] Starting GUI > log.log
START /B /wait .\FEA_G\main.py >> log.log
echo %time% ^>^>^> [INFO] GUI Closed >> log.log
