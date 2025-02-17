#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Learning for loop
#Usage: ./for.sh

fruits=("Apple" "Banana" "Cherry" "Mango")
for fruit in "${fruits[@]}"; do
	echo "I like to eat $fruit"
done

fruits=("Apple" "Banana" "Cherry" "Mango")
for i in "${!fruits[@]}"; do
	echo "fruit ate $i is ${fruits[$i]}"
done

#1st way to print even and odd fruits
fruits=("Apple" "Banana" "Cherry" "Mango")
for i in "${!fruits[@]}"; do
	if [[ $i%2 -eq 0 ]];	then
		echo "I like ${fruits[$i]}"
	else
		echo "I don't like ${fruits[$i]}"
	fi	
done

#2nd way to print even and odd fruits
fruits=("Apple" "Banana" "Cherry" "Mango")
for i in "${!fruits[@]}"; do
	if (( i%2==0 ));	then
		echo "I like ${fruits[$i]}"
	else
		echo "I don't like ${fruits[$i]}"
	fi	
done