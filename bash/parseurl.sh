#!/bin/bash
if [ "$1" == "" ]
then
echo "PARSE URL - ONE PARSE TO RULE THEM ALL"
echo"You should run: $0 <EXAMPLE.COM>"
else
wget $1 >parsed

