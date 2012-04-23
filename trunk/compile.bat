@echo off
:: Close caption compiler - place in tf/resource
:: i-ghost
call steam
set VPROJECT=%_steamdir%\steamapps\%_steamuser%\team fortress 2\tf
set bin=%sourcesdk%\bin\orangebox\bin\captioncompiler.exe
for /f %%a in ('dir /b closecaption_*.txt') do (echo compiling %%a... & %bin% -l "%%~fa" >nul)
echo Creating backups...
if not exist .\backup md .\backup
xcopy closecaption_*.txt .\backup\ /Y /Q >nul
xcopy closecaption_*.dat .\backup\ /Y /Q >nul
echo Done.