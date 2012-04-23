@echo off
:: Steam helper
:: i-ghost
:: Variables:
:: %_steamdir% = Steam path
:: %_steamuser% = Steam username
:: %_steamvanity% = Steam community name
:: %_steampid% = Steam process ID
:: %_steambin% = Steam binary path
for /F "tokens=2* delims=	 " %%A in ('REG QUERY "HKCU\Software\Valve\Steam" /v SteamPath 2^>nul') do set _steamdir=%%B
:: substitute forward slashes for back slashes
set _steamdir=%_steamdir:/=\%
for /f "tokens=2,3 delims=	 " %%a in ('findstr /C:AutoLoginUser "%_steamdir%\config\SteamAppData.vdf"') do set _steamuser=%%~a
for /F "tokens=2* delims=	 " %%A in ('REG QUERY "HKCU\Software\Valve\Steam" /v LastGameNameUsed 2^>nul') do set _steamvanity=%%B
for /F "tokens=1,2 delims=	 " %%A in ('tasklist /FI "imagename eq Steam.exe" /FI "Status eq running" /NH 2^>nul') do set _steampid=%%B
for /F "tokens=2* delims=	 " %%A in ('REG QUERY "HKCU\Software\Valve\Steam" /v SteamExe 2^>nul') do set _steambin=%%B
exit /b 0