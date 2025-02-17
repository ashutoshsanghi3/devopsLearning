#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Learning regular expression
#Usage: ./regularexpression.sh

numString="123456789"
if [[ $numString =~ ^1 ]]; then
    echo "$numString starts with 1"
fi

if [[ $numString =~ ^[0.61] ]]; then
    echo "$numString starts with 0, . , 6 or "
fi

if [[ $numString =~ ^1,*8 ]]; then
    echo "$numString starts with 1 and 8"
fi

charString="aFCEf"
if [[ $charString =~ ^[A-Za-z]+$ ]]; then
# The string must consist entirely of one or more alphabetic characters (letters), and nothing else.
    echo "$charString has only alphabetic characters"
fi