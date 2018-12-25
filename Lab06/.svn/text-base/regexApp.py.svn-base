#! /usr/bin/env python3.4
import sys
import re

def getUrlParts(url):
    result = []
    pattern = re.match(r"http://(?P<BaseAddress>[\w.-]+)/(?P<Controller>[\w.-]+)/(?P<Action>[\w.-]+)\?(?P<QueryString>[\w.-]+)", url)
    result.append(pattern.group("BaseAddress"))
    result.append(pattern.group("Controller"))
    result.append(pattern.group("Action"))
    result_tuple = tuple(result)
    print(result_tuple)
    return result_tuple

def getQueryParameters(url):
    result = []
    find = re.findall(r"[\w.-]+=[\w.-]+",url)
    for i in range(len(find)):
        param = re.search(r"([\w.-]+)=([\w.-]+)",find[i])
        tuple_find = (param.group(1),param.group(2))
        result.append(tuple_find)
    print(result)
    return result

def getSpecial(sentence, letter):
    find = re.findall(r"(\bt\w+|\w+t\b)",sentence,re.IGNORECASE)
    find_illegal = re.findall(r"\bt\w+t\b",sentence,re.IGNORECASE)
    for i in range(len(find_illegal)):
        if find_illegal[i] in find:
            find.remove(find_illegal[i])
    print(find)
    return find

def getRealMAC(sentence):
    find = re.findall(r"[A-Za-z0-9][a-zA-Z0-9]:[a-zA-Z0-9][a-zA-Z0-9]:[a-zA-Z0-9][a-zA-Z0-9]:[a-zA-Z0-9][a-zA-Z0-9]:[a-zA-Z0-9][a-zA-Z0-9]:[a-zA-Z0-9][a-zA-Z0-9]|[A-Za-z0-9][a-zA-Z0-9]-[a-zA-Z0-9][a-zA-Z0-9]-[a-zA-Z0-9][a-zA-Z0-9]-[a-zA-Z0-9][a-zA-Z0-9]-[a-zA-Z0-9][a-zA-Z0-9]-[a-zA-Z0-9][a-zA-Z0-9]", sentence)
    if find != []:
        result = str(find[0])
    else:
        result = []
    print(result)
    return result

def helperDict():
    group_dict = {}
    with open('Employees.txt','r') as myEmployee:
        lines = myEmployee.readlines()
        fullname = ""
        ID = ""
        phone = ""
        state = ""
        for i in range(len(lines)):
            group_result = []
            lines[i] = lines[i].replace('\n',"")
            nameinfo = re.search(r"^([\w.-]+,?\s)([\w.-]+)", lines[i])
            firstname = re.sub(r",","",nameinfo.group(1))
            lastname = nameinfo.group(2)
            fullname = firstname+lastname
            IDinfo = re.search(r"[{]?\w{8}-?\w{4}-?\w{4}-?\w{4}-?\w{12}[}]?", lines[i])
            phoneinfo = re.search(r"[(]?\d{3}[)]?[\s|-]?\d{3}-?\d{4}", lines[i])
            stateinfo = re.search(r"[\w\s*]*$", lines[i])
            if IDinfo == None:
                ID = ""
            else:
                from uuid import UUID
                i = IDinfo.group(0)
                ID = str(UUID(i))
            group_result.append(ID)
            if phoneinfo == None:
                phone = ""
            else:
                num = re.sub(r"\(","",phoneinfo.group(0))
                num = re.sub(r"\)","",num)
                num = re.sub(r"\s","",num)
                num = re.sub(r"\-","",num)
                phone = "("+num[0:3]+") "+num[3:6]+"-"+num[6:10]
            group_result.append(phone)
            if stateinfo.group(0) == "":
                state = ""
            else:
                state = stateinfo.group(0)
            group_result.append(state)
            group_dict[fullname] = group_result
    return group_dict


def getRejectedEntries():
    result = []
    setinfo = helperDict()
    for keys in setinfo:
        flag = 0
        for i in setinfo[keys]:
            if i == "":
                continue
            else:
                flag = 1
        if flag == 0:
            result.append(keys)
    result.sort()
    print(result)
    return result

def getEmployeesWithIDs():
    result = {}
    setinfo = helperDict()
    for keys in setinfo:
        if setinfo[keys][0] != "":
            result[keys] = setinfo[keys][0]
    print(result)
    return result

def getEmployeesWithoutIDs():
    result = []
    setinfo = helperDict()
    for keys in setinfo:
        if setinfo[keys][0] == "":
            result.append(keys)
    result.sort()
    print(result)
    return result

def getEmployeesWithPhones():
    result = {}
    setinfo = helperDict()
    for keys in setinfo:
        if setinfo[keys][1] != "":
            result[keys] = setinfo[keys][1]
    print(result)
    return result

def getEmployeesWithStates():
    result = {}
    setinfo = helperDict()
    for keys in setinfo:
        if setinfo[keys][2] != "":
            result[keys] = setinfo[keys][2]
    print(result)
    return result

def getCompleteEntries():
    result = {}
    setinfo = helperDict()
    for keys in setinfo:
        flag = 0
        for i in setinfo[keys]:
            if i == "":
                flag = 1
            else:
                continue
        if flag == 0:
            tupleset = tuple(setinfo[keys])
            result[keys] = tupleset
    print(result)
    return result

if __name__ == "__main__":
    getUrlParts("http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall")

    getQueryParameters("http://www.google.com/Math/Const?Pi=3&Max_Int=65536&What_Else=Not-Here")

    getSpecial("The TART program runs on Tuesdays and Thursdays, but it does not start until next week.","t")

    getRealMAC("http://www.google.com/Math/Const?Pi=3&Max_Int=65536&What_Else=Not-Here and what is tis thing i dont get a clue. but here we go 58-1C-0A-6E-AE-35.")

    getRejectedEntries()

    getEmployeesWithIDs()

    getEmployeesWithoutIDs()

    getEmployeesWithPhones()

    getEmployeesWithStates()

    getCompleteEntries()