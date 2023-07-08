@echo off

REM Chceck pyton version
python --version
REM Check for updates
git pull
REM Install/upgarde pip
python -m ensurepip --upgrade
REM Install required libraries
pip install -r Assets/requirements.txt

pause

REM Run game
python menu.py
