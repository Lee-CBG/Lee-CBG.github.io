#!/bin/bash
#just pull before commiting since there could be mobile updates 
git pull
# Add all changes
git add .

# Commit changes with a provided message
git commit -m "fixing python to python3 for MAC"

# Push changes to the origin's HEAD
git push origin HEAD

read -p "Enter to exit" 