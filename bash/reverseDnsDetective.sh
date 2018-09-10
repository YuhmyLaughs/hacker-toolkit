#!/bin/bash
echo "One IP to rule them all..."
echo "usage: ./reverseDnsDetective <127.0.0> <1 - start><254-end>  <pattern to avoid if needed>"
echo "Crafted by verasnt"
for ip in $(seq $2 $3);
do
#uncomment the grep part in order to avoid some  useless results
host $1.$ip #| grep -v $4
done
