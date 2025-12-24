import re

fileName="C:\\Users\\joele\\Documents\\GHrepos\\AdventOfCode\\2025\\inputDay1.txt"

global dialNum 
dialNum = 50
decoyNum=0
password=0 #increment this as many times as dialNum hits decoyNum

def rotate(dist):
    global dialNum
    dialNum = dialNum + dist
    while dialNum < 0: #this is a while in case of rotations larger than 100
        dialNum = 100 + dialNum
    if dialNum > 99:
        dialNum = dialNum % 100



with open(fileName) as inFile:
    for line in inFile:
        # print(line)
        changeNum=int(re.sub('[^0-9]','',line))
        if line.__contains__("L"):
            #negative
            changeNum= changeNum * -1
        rotate(changeNum)
        if dialNum == decoyNum:
            password = password + 1

print("End loop, password " + str(password))

