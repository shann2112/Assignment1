# BAt File for Remote Updates to Repo
# by: Mick Shannon
# Date: 11/11/2022
# Function: Perform a commit
# Script: UpdateRemoteRepo.bat

clear
@echo off
echo.
echo '**************************************************'
echo "Performing an add for all files in this directory"
echo '**************************************************'
echo.
git status
echo *** press [ctrl][c] to exit or any key to continue ***
pause
echo.
set /p NAME=Enter the name of the project, then press [return]

echo '**************************************************'
echo 'Pushing to GITHUB repository'

:: git remote add origin https://github.com/shann2112/Assignment1
git add .
git commit -m "%NAME%"
git push origin main

echo '**************************************************'
echo 'Done!