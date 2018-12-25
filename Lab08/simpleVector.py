#! /usr/bin/env python3.4
import sys
import os

class Vector:
    def __init__(self,string):
        values = string.split(" ")
        x = values[0]
        y = values[1]
        self.x = float(x)
        self.y = float(y)
