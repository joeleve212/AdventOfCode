import re

fileName="C:\\Users\\joele\\Documents\\GHrepos\\AdventOfCode\\2025\\inputDay2.txt"

global dialNum 
dialNum = 50
decoyNum=0
global password
password=0 #increment this as many times as dialNum hits decoyNum

def rotate(dist):
    global dialNum
    global password
    if dialNum == 0:
        startedZero=1
    else:
        startedZero=0
    dialNum = dialNum + dist
    while dialNum < 0: #this is a while in case of rotations larger than 100
        dialNum = 100 + dialNum
        if not startedZero: #prevent increment when starting rotation at zero
            password = password + 1
        else:
            startedZero=0 #don't skip more than one increment
    if dialNum > 99:
        password = password + int(dialNum/100)
        dialNum = dialNum % 100
    elif dialNum == decoyNum:
        password = password + 1


def dayOne():
    with open(fileName) as inFile:
        for line in inFile:
            changeNum=int(re.sub('[^0-9]','',line))
            if line.__contains__("L"):
                #negative
                changeNum= changeNum * -1
            rotate(changeNum)
            print(re.sub('\n','',line) + " new location: " + str(dialNum) + " current pass: " +  str(password))

    print("End loop, password " + str(password))

def findEndChar(subStrStart, subStrLen):
    return ((2*subStrLen) + subStrStart)

def isNumValid(number):
    isValid=True
    numStr=str(number)
    subLen=1 #starting length of substring
    subStart=0 #starting char of substring
    endCompare=findEndChar(subStart, subLen)
    while isValid and (endCompare <= len(numStr)):
        compStart=subStart+subLen
        # print("start compare with ranges [" + str(subStart) + "," + str(subStart+subLen) + "] [" + str(compStart) + "," + str(compStart+subLen) + "]"
        #       + "substrings: " + numStr[subStart:subStart+subLen] + " and " + numStr[compStart:compStart+subLen])
        #loop through checks
        if numStr[subStart:subStart+subLen] == numStr[compStart:compStart+subLen]:
            print("Found match: " + numStr[subStart:subStart+subLen] + " and " + numStr[compStart:compStart+subLen])
            isValid=False
        #update subStart and subLen for next loop
        if findEndChar(subStart, subLen+1) > len(numStr):
            if findEndChar(subStart+1, 1) > len(numStr):
                # print("Done with comparisons")
                endCompare = len(numStr) + 1 #this will exit loop
            else:
                subStart = subStart + 1
                subLen = 1
                endCompare=findEndChar(subStart, subLen)
        else:
            subLen = subLen + 1
            endCompare=findEndChar(subStart, subLen) #this is the index (+1) of last char used in next comparison
        
    return isValid #This will be 1 if valid, 0 if not valid

def dayTwo():
    inFile = open(fileName)
    fileStr = inFile.read()
    ranges = fileStr.split(',')
    invalidTotal = 0 #this will be our end goal
    for r in ranges:
        r = re.sub('\n','',r) #prevent EOF/newline from being included in range string
        borders=r.split('-')
        print("start: " + borders[0] + " end: " + borders[1])
        for value in range(int(borders[0]), int(borders[1]) + 1):
            if not isNumValid(value):
                invalidTotal = invalidTotal + value
                print("Found invalid number " + str(value))
    print("Final total: " + str(invalidTotal))



##Main portion of program
dayTwo()
