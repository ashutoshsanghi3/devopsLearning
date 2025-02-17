#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: If batsman score is less than 20,remove him.If greater than equal to 20 but less than 40,
#	player is good.If greater than 40,player is excellent.
#Usage: ./if_batsman.sh

echo "Please enter the batsman score"
read -r score
echo "score is $score"
if [ $score -lt 20 ]; then
	echo "Remove him"
elif [ $score -le 40 ]; then
	echo "Player is good"
else
	echo "Player is excellent"
fi

for i in 1 2 3 4 5
do
	echo "$i"
done

for i in {1..5};
do
	echo "$i"
done

for i in $(seq 1 5);
do
	echo "$i"
done

for (( i=1; i<=10;i++ ));
do
	echo "$i"
done

