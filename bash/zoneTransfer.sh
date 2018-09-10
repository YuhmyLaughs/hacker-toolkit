#!/bin/bash
#lets transfer some zones..
echo "TCP - 53 port is open ? great : crap"
echo "Crafted by verasnt"
for server in $(host -t ns $1 | cut -d " " -f4);
do
host -l $1 $server;
done
