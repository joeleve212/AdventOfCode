#!/bin/bash

total=0
numLimitedLines=$(grep -o "[0-9].*" ./day1Input.txt)


for line in $numLimitedLines; do
    line=$(echo $line | grep -o ".*[0-9]")
    # echo $line               #only for debug
    firstNum=$(echo $line | grep -o "^.")
    lastNum=$(echo $line | grep -o ".$")
    # echo $firstsNum$lastNum  #only for debug
    total=$(($total + $firstNum$lastNum ))
done

echo $total









