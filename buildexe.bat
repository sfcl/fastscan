@echo off

del /f /s /q .\dist\*

del /f /s /q .\__pycache__\*
python setup.py py2exe

xcopy bin .\dist\bin /s /e /q

copy config.ini .\dist\config.ini