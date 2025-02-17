#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Learning date
#Usage: ./date_command.sh

#This is one way to get the value
command="date +%H"
newcommand="`eval $command`"

#This is another way
#newcommand = $(date +%H)

res=$(( newcommand + 4 ))
if [ $res -le 12 ]; then
    echo "Good morning"
elif [ $res -le 16 ]; then
    echo "Good afternoon"
elif [ $res -le 20 ]; then   
    echo "Good evening"
else
    echo "Good night"
fi