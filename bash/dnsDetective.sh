#!/bin/bash
for url in  $(cat $2);
do
host  $url.$1 | grep "has address"
done
