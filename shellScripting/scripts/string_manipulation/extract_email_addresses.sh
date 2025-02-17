#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Write a script to extract email addresses from a text file.
#Usage: ./extract_email_addresses.sh

input_file="script5.txt"
emails=$(grep -oE '\b[A-Za-z0-9+-._%]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' "$input_file")
echo "$emails"