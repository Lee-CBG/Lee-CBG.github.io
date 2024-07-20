#!/bin/bash

# Ensure this script is run from the directory where it resides
cd "$(dirname "$0")"

function show_menu() {
    echo "Select the component you want to modify:"
    echo "1. Teams"
    echo "2. News"
    echo "3. Research"
    echo "4. Publications"
    echo "5. Exit"
    echo -n "Enter your choice [1-5]: "
    read choice
    return $choice
}

function execute_script() {
    script_path="scripts"
    case $1 in
        1)
            echo "Modifying Teams..."
            python $script_path/teams.py --add
            ;;
        2)
            echo "Modifying News..."
            python $script_path/news.py
            ;;
        3)
            echo "Modifying Research..."
            python $script_path/research.py
            ;;
        4)
            echo "Modifying Publications..."
            cd scripts
            python bibtex2html.py example.bib template.html output.html
            python publications.py
            cd ../.
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
