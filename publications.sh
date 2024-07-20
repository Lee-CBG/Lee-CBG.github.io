#!/bin/bash

BIB_FILE="example.bib"

function add_entry() {
    echo "$1" >> $BIB_FILE
    echo "Entry added."
}

function remove_entry() {
    grep -v "$1" $BIB_FILE > temp.bib && mv temp.bib $BIB_FILE
    echo "Entry removed."
}

function list_entries() {
    cat $BIB_FILE
}

function update_entry() {
    remove_entry "$2"
    add_entry "$1"
    echo "Entry updated."
}

echo "BibTeX Manager"
echo "1. Add entry"
echo "2. Remove entry"
echo "3. List entries"
echo "4. Update entry"
read -p "Select an option: " option
read -p "Enter BibTeX entry (escape any internal double quotes): " entry

case $option in
    1) add_entry "$entry" ;;
    2) remove_entry "$entry" ;;
    3) list_entries ;;
    4) read -p "Enter old BibTeX entry for replacement: " old_entry
       update_entry "$entry" "$old_entry" ;;
    *) echo "Invalid option selected." ;;
esac
