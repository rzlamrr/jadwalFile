#!/bin/bash

git config --global user.email "rzlamrr.dvst@protonmail.com"
git config --global user.name "rzlamrr"

pip3 install requests

for var in "$@":
do
    python3 fetch.py $var && git add $var && git commit -m "Import schedule for $var" &
    pids[${var}]=$!
done

for pid in ${pids[*]}
do
    wait $pid
done

