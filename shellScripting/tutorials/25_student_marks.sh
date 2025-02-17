#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Learning regular expression
#Usage: ./student_marks.sh

echo "enter marks of maths,physics,chemistry"
read -r maths physics chemistry
# echo "$maths"
if [[ $maths -lt 30 || $physics -lt 30 || $chemistry -lt 30 ]]; then
    echo "Fail"
else
    avg=$(( (maths+physics+chemistry)/3 ))
    echo "Avg is $avg"
    if [ $avg -gt 80 ]; then    
        echo "Distinction"
    elif [ $avg -gt 60 ]; then
        echo "Very good"
    elif [ $avg -gt 45 ]; then
        echo "Good"
    else
        echo "Passed"
    fi
fi

