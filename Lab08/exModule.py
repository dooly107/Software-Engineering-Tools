#! /usr/bin/env python3.4
import sys
import os

def runNetworkCode(**kwargs):
    for key in kwargs:
        return os.open(kwargs[key],os.O_RDWR)