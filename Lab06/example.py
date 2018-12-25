#! /usr/bin/env python3.4
import re
import sys

def example():
    x = r"[0-9]+(?P<foo>\.[0-9]+)"
    m = re.search(x,"Hello 56.43 World")
    if m:
        gp = m.groupdict()
        print(gp["foo"])
    else:
        print("Wrong")
    y = "1249 kim1403@PURDUE.edu 12912"
    pattern = r"([\w.-]+)@([\w.-]+)"
    if re.match(pattern,y,re.I):
        print("Starts with Pattern")
    elif re.search(pattern,y,re.I):
        print("Has this pattern")
    else:
        print("No found pattern")

    A = [1,2,2,3,5,6]
    D = map(lambda x: x == 5,A)
    for i in D:
        print(i)

def make_incrementer(n):
    return lambda x: x+n

def find(filename):
    with open(filename,'r') as myFile:
        lines = myFile.readlines()
        for i in lines:
            ID = re.search(r"\{?\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\}?",i)
            if ID:
                print(ID.group())
            else:
                print("No ID")


if __name__ == "__main__":
    example()
    INC = make_incrementer(1)
    INC2 = make_incrementer(2)
    print(INC(3))
    print(INC2(4))
    find("Employees.txt")