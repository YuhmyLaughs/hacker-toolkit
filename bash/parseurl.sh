#!/bin/bash
if [ "$1" == "" ]
then
echo "PARSE URL - ONE PARSE TO RULE THEM ALL"
echo "You should run: $0 <EXAMPLE.COM>"
else
wget -O target.html "$1"
grep href= target.html | cut -d "/" -f3 | grep "\.com\|\.org"| cut -d'"' -f1 | sort -u > hosts.txt
#for url in $(cat hosts);do host "$url";done
while read -r i; do
  host $i |grep "has address" 
done < hosts.txt
rm target.html hosts.txt
fi
