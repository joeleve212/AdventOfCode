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

rMax=$1
gMax=$2
bMax=$3

while IFS= read -r line; do
    debug "$line"
    gameID=$(echo $line | grep -o "Game.*:" | sed 's/:\| \|Game//g' )
    numPulls=$(($(echo $line | grep -o ";" | wc -l) + 1))
    for i in $(seq 1 $numPulls); do
        invalidFlag="0"
        thisPull=$(echo $line | grep -o ":.*" | sed 's/://g' | cut -d";" -f$i)
        debug "pull $i had $thisPull"
        numColors=$(($(echo $thisPull | grep -o "," | wc -l)+1))
        for j in $(seq 1 $numColors); do
            countColor=$(echo $thisPull | cut -d"," -f$j)
            thisColor=$(echo $countColor | cut -d" " -f2)
            thisNumber=$(echo $countColor | cut -d" " -f1)
            if [[ $thisColor == "red" ]]; then
                if [ $thisNumber -gt $rMax ]; then
                    debug "Not possible, too many red"
                    invalidFlag="1"
                    break;
                fi
            elif [[ $thisColor == "green" ]]; then
                if [ $thisNumber -gt $gMax ]; then
                    debug "Not possible, too many green"
                    invalidFlag="1"
                    break;
                fi
            elif [[ $thisColor == "blue" ]]; then
                if [ $thisNumber -gt $bMax ]; then
                    debug "Not possible, too many blue"
                    invalidFlag="1"
                    break;
                fi
            else
                debug "Invalid color $thisColor"
            fi
        done
        if [[ $invalidFlag == "1" ]]; then
            debug "Skipping rest of this game"
            break;
        fi
    done
    if [[ $invalidFlag == "0" ]]; then
        IDtotal=$(($IDtotal + $gameID))
        debug "This game valid, total now $IDtotal"
    fi
done < $inputFile


