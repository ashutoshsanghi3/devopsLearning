#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Learning while loop and inputing value
#Usage: ./multiplication_while.sh

echo "Please enter the number"
read -r number
echo "multiplication table of $number"
counter=1
while [ $counter -le 10 ]
do
	mult=`expr $number \* $counter`
	echo "$number * $counter = $mult"
	counter=`expr $counter + 1`
done