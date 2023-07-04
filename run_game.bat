@echo off

REM Check for updates
git pull
REM Chceck pyton version
python --version
REM Install/upgarde pip
python -m ensurepip --upgrade
REM Install required libraries
pip install -r requirements.txt

pause

REM Run game
python menu.py
