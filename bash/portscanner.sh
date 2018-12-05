#!/bin/bash

# ./portscanner host startport stopport
# ./portscanner dummy.com 1 13


host=$1
startport=$2
stopport=$3

#ping check
function pingcheck
{
ping=`ping -c 1 $host | grep bytes | wc -l`
if [ "$ping" -gt 1 ];then
	echo "$host is up";
else
	echo "$host is down, quitting...";
	exit
fi
}

#function to test a port to see if its open
function portcheck
{
for((counter=$startport; counter<=$stopport; counter++))
do
	(echo >/dev/tcp/$host/$counter) > /dev/null 2>&1 && echo "$counter open"
done
}

#running
pingcheck
portcheck