#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Write a script to convert a string to uppercase.
#Usage: ./string_to_uppercase.sh

echo "Enter a string:"
read -r string
uppercase_string=$( echo "$string" | tr '[:lower:]' '[:upper:]')
echo $uppercase_string