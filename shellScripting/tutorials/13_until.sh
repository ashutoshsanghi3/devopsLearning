#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Until
#Usage: ./until.sh

echo -e "Please enter the IP address to ping\c"
read -r ip
until ping $ip
do
	echo "host in $ip is down"
	sleep 1
done
echo "host in $ip is up"


