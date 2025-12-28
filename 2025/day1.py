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

def dayTwo():
    #TODO: add content
    inFile = open(fileName)
    fileStr = inFile.read()
    ranges = fileStr.split(',')
    for r in ranges:
        r = re.sub('\n','',r) #prevent EOF/newline from being included in range string
        print("[" + r + "]")

##Main portion of program
dayTwo()
