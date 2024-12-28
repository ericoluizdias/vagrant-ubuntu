@echo off
rem Configurar proxy CNHCE

reg add "hkey_current_user\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d 172.25.141.179:8080 /f
reg add "hkey_current_user\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /d 1 /f
reg add "hkey_current_user\Software\Microsoft\Windows\currentVersion\Internet Settings" /v ProxyOverride /d "172.25.136.148;api.valid.com;sso.valid.com;<local>" /f
echo.
echo Servidor Proxy CNHCE configurado. (Testar ADP e demais sistemas)
pause