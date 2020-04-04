#!/bin/bash

if [ "$#" -ne 2 ]; then
 echo "usage: ./prober.sh <domainlist.txt>"
 exit 1
fi

filename=$1

for sub in $(cat `pwd`/$filename);
do
    if ping -c 1 -q -W 1 "$sub"; then
        echo $sub >> alive.txt
    fi
done

exit 1