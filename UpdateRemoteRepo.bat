# BAt File for Remote Updates to Repo
# by: Mick Shannon
# Date: 11/11/2022
# Function: Perform a commit
# Script: UpdateRemoteRepo.bat
clear
@echo off
git status
echo.
echo '**************************************************'
echo "Performing an add for all files in this directory"
echo '**************************************************'
echo.
git add .
git status

echo *** press [ctrl][c] to exit or any key to continue ***
pause

:: set variables to local

SETLOCAL
echo.
set /p NAME=Enter the name of the project, then press [return]

git commit -m "%NAME%"
git status
echo '**************************************************'
echo 'Pushing to GITHUB repository'
git push -u origin master
echo '**************************************************'
echo 'Done!