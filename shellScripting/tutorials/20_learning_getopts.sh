#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Learning date
#Usage: ./learning_getopts.sh -a hello -b world

while getopts :a:b: flag; do
    case $flag in
        a) ab=$OPTARG;;
        b) bc=$OPTARG;;
        ?) echo "i don't understand this value"
    esac
        
done
    echo "first value $ab, second value $bc"