#!/bin/bash

DEBUG=1
inputFile="./day2Input.txt"
editedInput="./day2_edit.txt"
IDtotal=0

debug(){
    if [ $DEBUG == 1 ]; then
        echo $1
    fi
}

while IFS= read -r line; do
    debug "$line"
    gameID=$(echo $line | grep -o "Game.*:" | sed 's/:\| \|Game//g' )
    numPulls=$(($(echo $line | grep -o ";" | wc -l) + 1))
    for i in $(seq 1 $numPulls); do
        thisPull=$(echo $line | cut -d=";" -f1)
        debug "pull $i had $thisPull"
    done
done < $inputFile


