#!/bin/bash

# Function to display the menu and get a choice
function show_menu() {
    echo "Select the component you want to modify:"
    echo "1. Teams"
    echo "2. News"
    echo "3. Research"
    echo "4. Publications"
    echo "5. Exit"
    read -p "Enter your choice [1-5]: " choice
    return $choice
}

# Function to execute the Python script based on the user's choice
function execute_script() {
    case $1 in
        1)
            echo "Modifying Teams..."
            python3 scripts/teams.py
            ;;
        2)
            echo "Modifying News..."
            python3 scripts/news.py
            ;;
        3)
            echo "Modifying Research..."
            python3 scripts/research.py
            ;;
        4)
            echo "Modifying Publications..."
            python3 scripts/publications.py
            ;;
        5)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice..."
            ;;
    esac
}

# Function to handle Git operations
function git_operations() {
    read -p "Do you want to push these changes to the repository? (y/n): " answer
    if [[ $answer = "y" || $answer = "Y" ]]
    then
        git add .
        read -p "Enter commit message: " commit_message
        git commit -m "$commit_message"
        git push
        echo "Changes pushed to repository."
    else
        echo "Changes not pushed."
    fi
}

# Main program loop
while true
do
    show_menu
    choice=$?
    execute_script $choice
    if [[ $choice -ge 1 && $choice -le 4 ]]
    then
        git_operations
    fi
done
