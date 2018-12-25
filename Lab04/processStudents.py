#! /usr/bin/env python3.4

import sys
import os

def getRegistration():
    listfiles = os.listdir('Classes')
    result = {}
    for i in range(len(listfiles)):
        with open('Classes/'+listfiles[i],'r') as myFile:
            line = myFile.readlines()
            for j in range(len(line)):
                name = line[j].strip()
                if name not in result:
                    A = []
                    A.append(listfiles[i][0:6])
                    result[name] = A
                else:
                    result[name].append(listfiles[i][0:6])
    for n in result:
        print(n,result[n])
    return result

def getCommonClasses(studentName1, studentName2):
    setstudents = getRegistration()
    result = []
    if studentName1 in setstudents:
        class1 = setstudents[studentName1]
    if studentName2 in setstudents:
        class2 = setstudents[studentName2]
    for i in range(len(class1)):
        if class1[i] in class2:
            result.append(class1[i])
    print(set(result))
    return (set(result))



if __name__ == "__main__":
    getRegistration()
    getCommonClasses("Zenaida Blaisdell","Neomi Flournoy")