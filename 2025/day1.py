import re

fileName="C:\\Users\\joele\\Documents\\GHrepos\\AdventOfCode\\2025\\inputDay1.txt"

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
        if not startedZero:
            password = password + 1
    if dialNum > 99:
        password = password + int(dialNum/100)
        dialNum = dialNum % 100
    elif dialNum == decoyNum:
        password = password + 1



with open(fileName) as inFile:
    for line in inFile:
        changeNum=int(re.sub('[^0-9]','',line))
        if line.__contains__("L"):
            #negative
            changeNum= changeNum * -1
        rotate(changeNum)
        print(re.sub('\n','',line) + " new location: " + str(dialNum) + " current pass: " +  str(password))

print("End loop, password " + str(password))

