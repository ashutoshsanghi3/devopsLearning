#!/bin/bash 
#Not done
#Author: Ashutosh Sanghi
#Purpose: Write a script to check if a string is a palindrome.
#Usage: ./check_if_string_is_palindrome.sh

echo "Enter a string:"
read -r string
size_of_string=${#string}
reverse_string=""
for ((i=0;i<$size_of_string;i++));
do
    reverse_string+=${string[i]}
done

echo $string
echo $reverse_string