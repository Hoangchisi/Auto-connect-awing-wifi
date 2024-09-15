
@echo off

:loop
python C:/Users/Admin/Downloads/Awing-Free-Wifi-Autoconnect-main/awing-autoconnect.py
timeout /t 840 >nul
python C:/Users/Admin/Downloads/Awing-Free-Wifi-Autoconnect-main/awing-autodisconnect.py
goto loop
