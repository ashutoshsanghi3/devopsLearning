#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: For conditions
#Usage: ./for2.sh

for i in 1 2 3 4 5
do
	echo "$i"
done

echo "<<<<<<<<<<<<"

for i in {1..5};
do
	echo "$i"
done

echo "<<<<<<<<<<<<"

for i in $(seq 1 5);
do
	echo "$i"
done

echo "<<<<<<<<<<<<"

for ((i=1; i<=10;i++));
do
	echo "$i"
done

