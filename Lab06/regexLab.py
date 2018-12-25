#! /usr/bin/env python3.4
import sys
import re

def parseXML(xmlNode):
    result = []
    find = re.findall(r'[\w.-]*=\"[\w.-]*\s?[\w.-]*\"',xmlNode)
    for i in range(len(find)):
        gather = []
        param = re.search(r'([\w.-]*)=(\"[\w.-]*\s?[\w.-]*\")',find[i])
        remove = re.sub(r'"',"",param.group(2))
        gather = [param.group(1),remove]
        tupleset = tuple(gather)
        result.append(tupleset)
    result.sort()
    print(result)
    return result

def captureNumbers(sentence):
    result = []
    find = re.findall(r'[-|+]?[\d].[\d]+e[-|+][\d]+|[-|+]?[\d]+.[\d]+|[-|+]?[\d]+',sentence,re.IGNORECASE)
    for i in range(len(find)):
        result.append(find[i])
    print(result)
    return result

if __name__ == "__main__":
    xmlNode = '<person name="Irene Adler" gender="female" age="35" \>'
    parseXML(xmlNode)

    s = "With the electron's charge being -1.6022e-19, some choices you have are -110, -32.0 and +55. Assume that pi equals 3.1415, 'e' equals 2.7 and Na is +6.0221E+023/"
    captureNumbers(s)