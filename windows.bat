cd %~dp0
echo=
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f >nul 2>nul
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "127.0.0.1:3000" /f >nul 2>nul
.\src\core\mitmdump --listen-host 127.0.0.1 -p 3000 -s ./src/main.py --set termlog_verbosity=error --flow-detail 0