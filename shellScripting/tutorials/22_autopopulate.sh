#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Learning auto populated
#Usage: ./autopopulate.sh

echo " all arguments concat together $*"
echo " number of arguments $#"
echo " first argument $1"
echo " expands all the command line arguments as seperate words $@"
echo " process id of current process $$"

sleep 400 &
echo "process id of recently backgrounded process $!"
echo "file name of current program $0"