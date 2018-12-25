#! /usr/bin/env python3.4
import sys
import os
import re
from exModule import runNetworkCode

def checkNetwork(**kwargs):
    try:
        runNetworkCode(**kwargs)
    except ConnectionError:
        raise
    except OSError as error:
        errortype = type(error).__name__
        print('An issue encountered during runtime. The name of the error is: '+errortype)
    except:
        return False
    else:
        return True

def isOK(signalName):
    check = re.match('[A-Z][A-Z][A-Z]-\d\d\d',signalName)
    if check:
        return True
    else:
        return False

def loadDataFrom(signalName, folderName):
    check = isOK(signalName)
    if check == False:
        raise ValueError(signalName+" is invalid.")
    else:
        filename = signalName+".txt"
        signalList = os.listdir(folderName)
        if filename not in signalList:
            raise OSError(filename+" is not found in given folder.")
        else:
            with open(folderName+"/"+filename,'r') as myFile:
                floatlist = []
                nonfloat_count = 0
                lines = myFile.readlines()
                for i in lines:
                    i = i.strip()
                    try:
                        value = float(i)
                    except ValueError:
                        nonfloat_count = nonfloat_count + 1
                    else:
                        floatlist.append(value)
                floatlist.sort()
                result = (floatlist,nonfloat_count)
                return result

def isBounded(signalValues, bounds, threshold):
    minimum = 0
    maximum = 0
    outofbound = 0
    if signalValues == []:
        raise ValueError("Signal contains no data")
    else:
        if bounds[0] < bounds[1]:
            minimum = bounds[0]
            maximum = bounds[1]
        else:
            minimum = bounds[1]
            maximum = bounds[0]
        for i in signalValues:
            if i < minimum or i > maximum:
                outofbound = outofbound + 1
            else:
                pass
        if outofbound <= threshold:
            return True
        else:
            return False

if __name__ == "__main__":
    checkNetwork(file="f1.txt")
    print(isOK("AEW-481"))
    a = loadDataFrom("PVL-758","Signals")
    print(a)
    print(isBounded(a[0],(-4.5,4.9),11))