# BAt File for Remote Updates to Repo
# by: Mick Shannon
# Date: 11/11/2022
# Function: Perform a commit
# Script: UpdateRemoteRepo.bat
clear
git status
echo '**************************************************'
echo "Performing an add for all files in this directory"
git add .
git status
echo '**************************************************'
echo 'Enter the commit message:'
read CommitMessage
git commit -m "$CommitMessage"
git status
echo '**************************************************'
echo 'Pushing to GITHUB repository'
git push -u origin master
echo '**************************************************'
echo 'Done!