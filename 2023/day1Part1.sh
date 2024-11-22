#!/bin/bash

DEBUG=0
total=0
inputFile="./day1Input.txt"
editedInput="./day1_edit.txt"

debug(){
    if [ $DEBUG == 1 ]; then
        echo $1
    fi
}


#pre-processing to replace spelled out numbers:
numStrings="one two three four five six seven eight nine"
cp $inputFile $editedInput

numValue=1
for number in $numStrings; do
    sed -i "s/$number/$number$numValue$number/g" $editedInput
    numValue=$(($numValue + 1))
done

#part 1 solution:
numLimitedLines=$(grep -o "[0-9].*" $editedInput)

for line in $numLimitedLines; do
    line=$(echo $line | grep -o ".*[0-9]")
    debug "line:$line"               #only for debug
    firstNum=$(echo $line | cut -c1-1)
    lastNum=$(echo $line | grep -o ".$")
    debug "first:$firstNum second:$lastNum"  #only for debug
    total=$(($total + $firstNum$lastNum ))
done

echo $total









