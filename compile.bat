@echo off
:: Closed caption compiler - place in tf/resource
:: i-ghost
if not exist steam.bat (echo Fatal: steam.bat required in PATH or current directory. & exit /b 1) else (call steam)
set VPROJECT=%_steamdir%\steamapps\%_steamuser%\team fortress 2\tf
set bin=%sourcesdk%\bin\orangebox\bin\captioncompiler.exe
del /F /S /Q log.txt
for /f %%a in ('dir /b closecaption_*.txt') do (echo Compiling Captions for %%a... & %bin% "%%~fa" >>log.txt)
:: Create backups in the (highly unlikely) event that Valve update the caption files.
echo Creating backups...
if not exist .\backup md .\backup
xcopy closecaption_*.txt .\backup\ /Y /Q >nul
xcopy closecaption_*.dat .\backup\ /Y /Q >nul
echo Done.
exit /b 0