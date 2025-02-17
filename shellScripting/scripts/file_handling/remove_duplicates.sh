#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Write a script to append text to a file.
#Usage: ./display_10_lines.sh

echo "enter file name"
read -r file
fileName="$file"
sort "$fileName" | uniq > "$fileName.temp"
mv "$fileName.temp" "$fileName"
echo "Duplicates removed from $fileName"