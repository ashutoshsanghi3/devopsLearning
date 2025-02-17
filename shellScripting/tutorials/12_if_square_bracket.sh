#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Doing if condition for if file exists
#Usage: ./if_square_bracket.sh

#1st time
file=$1
if [ -f $file ]; then
	echo "File exists $file"
else
	echo "File doesn't exists"
fi

#2nd time
file=$1
if [ -f "$file" ]; then
	echo "File exists $file"
else
	echo "File doesn't exists"
fi

#3rd time
file=$1
if [[ -f $file ]]; then
	echo "File exists $file"
else
	echo "File doesn't exists"
fi