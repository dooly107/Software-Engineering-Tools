#! /usr/bin/env python3.4
import sys
import os
from simpleVector import Vector

def loadVectors(filename):
    with open(filename, 'r') as myFile:
        lines = myFile.readlines()
        result = []
        for i in lines:
            try:
                coordinates = Vector(i)
            except:
                result.append(None)
            else:
                result.append(coordinates)
        return result

if __name__ == "__main__":
    print(loadVectors("values.txt"))