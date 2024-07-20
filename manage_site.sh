#!/bin/bash

# Function to display the menu and get a choice
function show_menu() {
    echo "Select the component you want to modify:"
    echo "1. Teams"
    echo "2. News"
    echo "3. Research"
    echo "4. Publications"
    echo "5. Exit"
    echo "Enter your choice [1-5]: "
    read choice
    return $choice
}

# Function to execute the Python script based on the user's choice
function execute_script() {
    script_path="scripts"
    case $1 in
        1)
            echo "Modifying Teams..."
            python3 $script_path/teams.py
            ;;
        2)
            echo "Modifying News..."
            python3 $script_path/news.py
            ;;
        3)
            echo "Modifying Research..."
            python3 $script_path/research.py
            ;;
        4)
            echo "Modifying Publications..."
            python3 $script_path/publications.py
            ;;
        5)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please select a valid option."
            return 1
            ;;
    esac
    return 0
}

# Function to handle Git operations
function git_operations() {
    read -p "Do you want to push these changes to the repository? (y/n): " answer
    if [[ $answer = "y" || $answer = "Y" ]]
    then
        echo "Running build command before pushing changes. Uno Momento!"
        bundle exec jekyll build
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
    script_status=$?
    if [[ $script_status -eq 0 && $choice -ne 5 ]]
    then
        git_operations
    fi
done
