#! /usr/bin/env python3.4
import sys
import os
import re
from moduleTask import isOK, isBounded, loadDataFrom

def loadMultiple(signalNames, folderName, maxCount):
    result = {}
    namelist = signalNames
    namelist.sort()
    for names in namelist:
        okload = ()
        okname = isOK(names)
        if okname == True:
            okload = loadDataFrom(names,folderName)
        if (okname == False) or (okload == ()):
            result[names] = None
        else:
            filename = names+'.txt'
            with open(folderName+'/'+filename) as myFile:
                lines = myFile.readlines()
                float_values = []
                nonfloat_count = 0
                for i in lines:
                    i = i.strip()
                    try:
                        value = float(i)
                    except ValueError:
                        nonfloat_count = nonfloat_count + 1
                    else:
                        float_values.append(value)
                float_values.sort()
                if nonfloat_count <= maxCount:
                    result[names] = float_values
                else:
                    result[names] = []
    return result

def saveData(signalsDictionary,targetFolder,bounds,threshold):
    for keys in signalsDictionary:
        filename = keys+".txt"
        target = targetFolder+"/"+filename
        if signalsDictionary[keys] == []:
            with open(target,'w') as myNewFile:
                pass
        elif signalsDictionary[keys] == None:
            pass
        else:
            with open(target,'w') as myNewFile:
                bound = isBounded(signalsDictionary[keys],bounds,threshold)
                if bound == False:
                    pass
                else:
                    valuelist = []
                    for i in signalsDictionary[keys]:
                        try:
                            value = float(i)
                        except ValueError:
                            pass
                        else:
                            if value < bounds[0] or value > bounds[1]:
                                pass
                            else:
                                value = "%.3f" % i
                                valuelist.append(value)
                    finalstring = '\n'.join(valuelist)
                    myNewFile.write(finalstring)



if __name__ == "__main__":
    dictionary = loadMultiple(["a23-412","NPU-381","AFW-481","CIG-308"],"Signals",7)
    print(dictionary)
    saveData(dictionary,"targetfolder",(-13.7,13.8),14)
    a = 0.182743