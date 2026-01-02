import re

fileName="C:\\Users\\joele\\Documents\\GHrepos\\AdventOfCode\\2025\\inputDay3.txt"

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

def isNumValid(number):
    isValid=True
    numStr=str(number)
    
    for strLen in range(1,int(len(numStr)/2)+1):
        if (len(numStr) % strLen) == 0: #skip if we can't evenly divide string
            print("Start strLen "+str(strLen))
            startIdx = 0
            midIdx=startIdx + strLen
            endIdx=midIdx + strLen
            foundMatch = True #haven't actually looked for match, we just need to enter loop
            while (foundMatch == True) and (endIdx <= len(numStr)): #each time entering this loop is one check 
                if numStr[startIdx:midIdx] == numStr[midIdx:endIdx]:
                    print("Match with "+numStr[startIdx:midIdx]+" and "+numStr[midIdx:endIdx])
                    foundMatch = True #redundant, but here for clarity
                    startIdx = startIdx + strLen
                    midIdx=startIdx + strLen
                    endIdx=midIdx + strLen
                    print("New:: start "+str(startIdx)+" mid "+str(midIdx)+" end "+str(endIdx))
                else:
                    print("No match"+numStr)
                    foundMatch = False  #one time through this else will exit loop
            if foundMatch:
                print("Found invalid number " + numStr )
                print("end: "+str(endIdx)+" mid: "+str(midIdx))
                if numStr == "252511":
                    exit()
                isValid=False     
       
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
                # print("Found invalid number " + str(value))
    print("Final total: " + str(invalidTotal))

totalDigits=12

def findNextDig(string,startIdx,digNum):
    if digNum == totalDigits: #this means we are searching for a 13th char
        print("Invalid digNum search")
        return -1
    highVal=0
    #TODO: figure if this loop is doing subtracts properly
    for charIdx in range(startIdx,len(string) - (totalDigits-digNum-1)): #minus so we leave chars for later digs
        thisDig=int(string[charIdx])
        if thisDig > highVal:
            digIdx=charIdx
            highVal=thisDig
    #return search Idx and digit
    return [ highVal, digIdx + 1 ]

def dayThree():
    sum=0
    with open(fileName) as inFile:
        digits = [] #this will be the final digits we want
        for line in inFile:
            line = re.sub('\n','',line)

            searchIdx=0 #start here to avoid having first loop run different
            for charNum in range(totalDigits):
                result = findNextDig(line, searchIdx, charNum)
                digits.append(result[0])
                searchIdx=result[1]

            thisVal=0
            for idx in range(totalDigits):
                print("Curr num: "+str(idx))
                thisVal=thisVal + (digits[idx] * pow(10, totalDigits - idx - 1))
            print("Max value: "+str(thisVal))
            exit()
            sum=sum+thisVal
    print("Final total: "+str(sum))

##Main portion of program
dayThree()
