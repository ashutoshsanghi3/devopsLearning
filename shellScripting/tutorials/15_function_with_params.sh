#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Learning function with parameter
#Usage: ./function_with_params.sh

function sum {
    local total=$(( $1 + $2 ))
	echo $total
}
sum 5 8
echo "<<<<<<<<<<<"
result1=$(sum 5 8)
result2=$(sum 10 4)
result=$(sum $result1 $result2)
echo "The result is $result"


