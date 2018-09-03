#!/bin/bash
if [ "$1" == "" ]
then
echo "You shall not pass."
echo "We need a access.log from your apache server..."
echo "You MUST run: $0 <apache's logfile>"
else
cat $1 | cut -d" " -f1 |sort|uniq -c|sort -unr
fi
