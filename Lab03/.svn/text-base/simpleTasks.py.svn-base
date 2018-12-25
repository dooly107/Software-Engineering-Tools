#! /usr/bin/env python3.4

import sys
import math

def find(pattern):
    with open('sequence.txt', 'r') as myFile:
        content = myFile.read()
        lengthpattern = len(pattern)
        lengthsequence = len(content)
        seqlocation = 0
        whereint = []
        datatype =[]
        for i in range(lengthpattern):
            if pattern[i] == "X":
                datatype.append("char")
            else:
                datatype.append("int")
        for j in range(lengthpattern):
            if datatype[j] == "int":
                whereint.append(j)
        print(whereint)
        lengthwhereint = len(whereint)
        result = []


        for index in range(lengthsequence - lengthpattern):
            good = 0
            bad = 0
            for ind in range(lengthwhereint):
                if content[index + whereint[ind]] == pattern[whereint[ind]] and bad == 0:
                    good = 1
                else:
                    bad = 1
                    good = 0
            if good == 1:
                result.append(content[index: (index + lengthpattern)])
        result.sort()
        return result

def getStreakProduct(sequence, maxSize, product):
    list = []
    lengthsequence = len(sequence)
    result = 1
    for index in range(lengthsequence):
        size = 0
        vallocation = index
        result = 1
        while result < product and vallocation < lengthsequence:
            val = int(sequence[vallocation])
            result = result * val
            vallocation += 1
            size += 1
        if size <= maxSize and result == product:
            list.append(sequence[index:vallocation])
    return list

def writePyramid(filepath, baseSize, count, char):
    with open(filepath, 'w') as myFile:
        row = int((baseSize + 1) / 2)
        space = int((baseSize - 1) / 2)
        numchar = 0
        for rows in range(row):
            for numpy in range(count):
                for cols in range(baseSize):
                    if cols < space or cols > space + numchar:
                        myFile.write(' ')
                    else:
                        myFile.write(char)
                if numpy < count - 1:
                    myFile.write(' ')
            numchar = numchar + 2
            space = space - 1
            myFile.write('\n')

def getStreaks(sequence, letters):
    lengthletters = len(letters)
    lensequence = len(sequence)
    count = 0
    result = []
    upletter = '\0'
    for seq in range(lensequence):
        if upletter == sequence[seq]:
            count = count + 1
        else:
            if count != 0:
                result.append(sequence[seq-count:seq])
                upletter = '\0'
                count = 0
            for let in range(lengthletters):
                if sequence[seq] == letters[let]:
                    count = 1
                    upletter = sequence[seq]
    if count != 0:
        result.append(sequence[seq-count+1:seq+1])
    return result


def findNames(nameList, part, name):
    numelements=len(nameList)
    lcname = name.title()
    findname = []
    if part == "L":
        for element in range(numelements):
            splitname = nameList[element].split(" ",2)
            lastname = splitname[1]
            if lastname == lcname:
                findname.append(nameList[element])
    elif part == "F":
        for element in range(numelements):
            splitname = nameList[element].split(" ",2)
            firstname = splitname[0]
            if firstname == lcname:
                findname.append(nameList[element])
    elif part == "FL":
        for element in range(numelements):
            splitname = nameList[element].split(" ",2)
            if splitname[0] == lcname or splitname[1] == lcname:
                findname.append(nameList[element])
    return findname

def convertToBoolean(num, size):
    if type(num) != int or type(size) != int:
        return []
    binary = bin(num)
    strbinary = str(binary)
    sizestrbinary = len(strbinary)
    sizebinary = sizestrbinary - 2
    result = []
    diff = size - sizebinary
    difflen = diff
    if difflen < 0:
        difflen = 0

    if size > sizebinary:
        sizebinary = size
    for length in range(sizebinary + 2):
        if length > 1:
            if diff > 0:
                ans = False
                result.append(ans)
                diff = diff - 1
            else:
                if strbinary[length-difflen] == "1":
                    ans = True
                    result.append(ans)
                else:
                    ans = False
                    result.append(ans)
    return result

def convertToInteger(boolList):
    sizebinary = len(boolList)
    power = sizebinary - 1
    intval = 0

    for size in range(sizebinary):
        if boolList[size] == True:
            intval += (2 ** power)
            power = power - 1
        else:
            power = power - 1
    return intval


if __name__ == "__main__":
    print(find("897XXXX"))

    print(getStreakProduct("54789654321687984",7,288))

    writePyramid("pyramid1.txt", 13, 6, 'X')

    print(getStreaks("AAASSSSSAPPPSSPPBBCCCSSS","PAZ"))

    print(findNames(["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"], "FL", "JOHNSON"))

    print(convertToBoolean(9, 1))

    print(convertToInteger([False, False, True, False, False, True]))
