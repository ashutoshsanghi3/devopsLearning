#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Write a script to count the number of words in a given string.
#Usage: ./count_no_of_words.sh


echo "Enter the string:"
read -r str
count=$(echo "$str" | wc -w)
echo "Word count = $count"