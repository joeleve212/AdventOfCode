#!/bin/bash

numLimitedLines=$(grep -o "[0-9].*[0-9]" ./day1Input.txt)
for line in $numLimitedLines; do
    firstNum=$(grep -o "^." $line)
    lastNum=$(grep -o ".$" $line)
    echo $firstNum$lastNum












