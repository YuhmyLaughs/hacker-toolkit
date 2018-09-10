#!/bin/bash
for ip in $(seq 1 254);
do
host $1.$ip | grep -v $2
done
