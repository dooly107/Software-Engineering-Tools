#! /usr/bin/env python3.4

import sys
import os

def getCircuitNumber(projectID):
    with open('projects.txt','r') as myProjects:
        l = myProjects.readlines()
        lenlines = len(l)
        circuitarrray = []
        for i in range(2,lenlines):
            lines = l[i].split()
            if (projectID == lines[1]):
                circuitarrray.append(lines[0])
    if circuitarrray == []:
        return "0"
    else:
        return circuitarrray


def getStudentIDwithCircuit(circuitarray):
    listarr = len(circuitarray)
    filename = []
    listID = []
    for i in range(listarr):
        filename = "Circuits/circuit_"+circuitarray[i]+".txt"
        with open(filename,'r') as myFile:
            lines = myFile.readlines()
            IDs = lines[1].split(",")
            countIDs = len(IDs)
            for k in range(countIDs):
                IDs[k] = IDs[k].replace(" ","").replace('\n','')
                listID.append(IDs[k])
    return listID

def getStudentID(studentName):
    name = studentName.split(",")
    lastname = name[0]
    firstname = name[1].replace(" ","")
    studentID = str()
    with open('students.txt', 'r') as myStudent:
        lines = myStudent.readlines()
        numlines = len(lines)
        for i in range(2,numlines):
            linestring = lines[i].replace(" ","").replace("|",",").split(",")
            if (lastname == linestring[0] and firstname == linestring[1]):
                studentID = linestring[2].strip()
    return studentID

def getStudentInvolvedProject(studentID):
    listfiles = os.listdir('Circuits')
    countfiles = len(listfiles)
    projectcircuit = []
    for j in range(countfiles):
        with open(("Circuits/"+listfiles[j]),'r') as myCircuits:
            line = myCircuits.readlines()
            IDs = line[1].split(",")
            listIDs = len(IDs)
            for k in range(listIDs):
                IDs[k] = IDs[k].replace(" ","").replace('\n','')
                if studentID == IDs[k]:
                    projectcircuit.append(listfiles[j][8:13])
    return projectcircuit

def getComponentCountByProject(projectID):
    projID = str(projectID)
    filename = "circuit_"+projID+".txt"
    filedir = "Circuits/"+filename
    resistor = 0
    inductor = 0
    transistor = 0
    capacitor = 0
    if os.access(filedir, os.R_OK):
        with open(filedir,'r') as myFile:
            line = myFile.readlines()
            component = line[4]
            stringlist = component.split(",")
            listlen = len(stringlist)
            for i in range(listlen):
                stringlist[i] = stringlist[i].replace(" ","")
                if stringlist[i][0] == "R":
                    resistor = resistor + 1
                if stringlist[i][0] == "L":
                    inductor = inductor + 1
                if stringlist[i][0] == "C":
                    capacitor = capacitor + 1
                if stringlist[i][0] == "T":
                    transistor = transistor + 1
        result = (resistor, inductor, capacitor, transistor)
        return result
    else:
        return None

def getComponentCountByStudent(studentName):
    name = studentName.split(",")
    lastname = name[0]
    firstname = name[1].replace(" ","")
    studentID = "0"
    resistor = 0
    capacitor = 0
    transistor = 0
    inductor = 0
    with open('students.txt', 'r') as myStudent:
        lines = myStudent.readlines()
        numlines = len(lines)
        for i in range(2,numlines):
            linestring = lines[i].replace(" ","").replace("|",",").split(",")
            if (lastname == linestring[0] and firstname == linestring[1]):
                studentID = linestring[2].strip()
        if (studentID == "0"):
            return None
    listfiles = os.listdir('Circuits')
    countfiles = len(listfiles)
    for j in range(countfiles):
        with open(("Circuits/"+listfiles[j]),'r') as myCircuits:
            line = myCircuits.readlines()
            IDs = line[1].split(",")
            listIDs = len(IDs)
            for k in range(listIDs):
                IDs[k] = IDs[k].replace(" ","").replace('\n','').strip()
                if studentID.strip() == IDs[k]:
                    components = line[4].split(",")
                    listcomponents = len(components)
                    for l in range(listcomponents):
                        components[l] = components[l].replace('\n','').strip()
                        if components[l][0] == "R":
                            resistor = resistor + 1
                        if components[l][0] == "L":
                            inductor = inductor + 1
                        if components[l][0] == "C":
                            capacitor = capacitor + 1
                        if components[l][0] == "T":
                            transistor = transistor + 1
    result = (resistor, inductor, capacitor, transistor)
    return result


def getParticipationByStudent(studentName):
    studentID = getStudentID(studentName)
    if studentID == "0":
        return None
    projectlist = getStudentInvolvedProject(studentID)
    lenprojectlist = len(projectlist)
    result = []
    with open('projects.txt','r') as myProjects:
        lines = myProjects.readlines()
        lenlines = len(lines)
        for j in range(lenprojectlist):
            for i in range(2,lenlines):
                proj = lines[i].split()
                listlinelen = len(proj)
                for k in range(listlinelen):
                    proj[k] = proj[k].replace(" ","").replace('\n','')
                if projectlist[j] == proj[0]:
                    result.append(proj[1])
    result_set = set(result)
    return result_set



def getParticipationByProject(projectID):
    circuitarr = getCircuitNumber(projectID)
    if circuitarr == "0":
        return None
    IDarr = getStudentIDwithCircuit(circuitarr)
    lenIDarr = len(IDarr)
    result = []
    with open('students.txt','r') as myNames:
        lines = myNames.readlines()
        lenlines = len(lines)
        for i in range(2,lenlines):
            linestring = lines[i].replace(" ","").replace("|",",").split(",")
            for j in range(lenIDarr):
                if (IDarr[j] == linestring[2].strip()):
                    result.append(linestring[0]+", "+linestring[1])
    wodup = set(result)
    return wodup

#step 5
def getfilenamesbycomponent(component):
    listfiles = os.listdir('Circuits')
    countfiles = len(listfiles)
    result = []
    lencomponent = len(component)
    for j in range(countfiles):
        with open(("Circuits/"+listfiles[j]),'r') as myCircuits:
            line = myCircuits.readlines()
            compline = line[4].split(",")
            listcomposition = len(compline)
            for i in range(listcomposition):
                for k in range(lencomponent):
                    if (compline[i].strip() == component[k]):
                        result.append(listfiles[j][8:13]+str(k))
    return result


def getProjectByComponent(component):
    lencomponent = len(component)
    circuits = getfilenamesbycomponent(component)
    if circuits == []:
        return None
    lencircuits = len(circuits)
    result = {}
    A = []
    with open('projects.txt','r') as myProj:
        lines = myProj.readlines()
        lenlines = len(lines)
        for j in range(2,lenlines):
            strline = lines[j].split()
            for i in range(lencircuits):
                if circuits[i][0:5] == strline[0]:
                    if component[int(circuits[i][5])] in result:
                        result[component[int(circuits[i][5])]].append(strline[1])
                    else:
                        A = [strline[1]]
                        result[component[int(circuits[i][5])]] = A
    for key in result.keys():
        makeset = set(result[key])
        result[key] = makeset
    return result


def getStudentByComponent(components):
    lencompgiven = len(components)
    listfiles = os.listdir('Circuits')
    countfiles = len(listfiles)
    listIDS = []
    result = {}
    A = []
    for i in range(countfiles):
        with open("Circuits/"+listfiles[i],'r') as myFiles:
            line = myFiles.readlines()
            IDline = line[1].split(",")
            lenIDline = len(IDline)
            for s in range(lenIDline):
                IDline[s] = IDline[s].replace('\n',"").strip()
            compline = line[4].split(",")
            lencompfile = len(compline)
            for j in range(lencompgiven):
                for k in range(lencompfile):
                    if (components[j].strip() == compline[k].strip()):
                        for b in range(lenIDline):
                            listIDS.append(IDline[b]+str(j))
    lenlistIDS = len(listIDS)
    with open('students.txt','r') as myStudents:
        lines = myStudents.readlines()
        lenlines = len(lines)
        for a in range(2,lenlines):
            strline = lines[a].replace(" ","").replace("|",",").split(",")
            for b in range(lenlistIDS):
                if strline[2].strip() == listIDS[b][0:11].strip():
                    if components[int(listIDS[b][11])] in result:
                        result[components[int(listIDS[b][11])]].append(strline[0] + ", " + strline[1])
                    else:
                        A = [strline[0]+", "+strline[1]]
                        result[components[int(listIDS[b][11])]] = A
    for key in result.keys():
        makeset = set(result[key])
        result[key] = makeset
    return result

def getComponentsByStudents(students):
    lenstudentsgiven = len(students)
    listIDS = []
    result = {}
    A = []
    with open('students.txt') as myStudents:
        lines = myStudents.readlines()
        countlines = len(lines)
        for i in range(2,countlines):
            linestring = lines[i].replace(" ","").replace("|",",").split(",")
            for j in range(lenstudentsgiven):
                if students[j].strip() == linestring[0].strip()+", "+linestring[1].strip():
                    listIDS.append(linestring[2].strip()+str(j))
    listfiles = os.listdir('Circuits')
    countfiles = len(listfiles)
    lenID = len(listIDS)
    for l in range(countfiles):
        with open('Circuits/'+listfiles[l],'r') as myfiles:
            strline = myfiles.readlines()
            IDline = strline[1].split(",")
            componentline = strline[4].split(",")
            lengthcomponents = len(componentline)
            for d in range(lengthcomponents):
                componentline[d] = componentline[d].replace('\n','').strip()
            idlength = len(IDline)
            for k in range(idlength):
                for m in range(lenID):
                    if IDline[k].strip() == listIDS[m][0:11].strip():
                        if students[int(listIDS[m][11])] in result:
                            for n in range(lengthcomponents):
                                result[students[int(listIDS[m][11])]].append(componentline[n])
                        else:
                            for n in range(lengthcomponents):
                                A.append(componentline[n])
                            result[students[int(listIDS[m][11])]] = A
    for key in result.keys():
        makeset = set(result[key])
        result[key] = makeset
    return result

def getSerialByCircuitID(array):
    arraylen = len(array)
    result = []
    for i in range(arraylen):
        with open("Circuits/circuit_"+array[i]+".txt",'r') as myFiles:
            lines = myFiles.readlines()
            strcomp = lines[4].split(",")
            countcomp = len(strcomp)
            for j in range(countcomp):
                strcomp[j] = strcomp[j].replace('\n',"").strip()
                if strcomp[j] not in result:
                    result.append(strcomp[j])
    return result



def getCommonByProject(projectID1, projectID2):
    array1 = getCircuitNumber(projectID1)
    array2 = getCircuitNumber(projectID2)
    if array1 == [] or array2 == []:
        return None
    comparray1 = getSerialByCircuitID(array1)
    comparray2 = getSerialByCircuitID(array2)
    countcomparray1 = len(comparray1)
    result = []
    for i in range(countcomparray1):
        if comparray1[i] in comparray2:
            result.append(comparray1[i])
    return result


def getCompbyStdID(studentID):
    listfiles = os.listdir('Circuits')
    countfiles = len(listfiles)
    result = []
    for j in range(countfiles):
        with open(("Circuits/"+listfiles[j]),'r') as myCircuits:
            line = myCircuits.readlines()
            IDs = line[1].split(",")
            listIDs = len(IDs)
            strcomps = line[4].split(",")
            for k in range(listIDs):
                IDs[k] = IDs[k].replace(" ","").replace('\n','').strip()
                if studentID == IDs[k]:
                    for l in range(len(strcomps)):
                        strcomps[l] = strcomps[l].replace('\n',"").strip()
                        if strcomps[l] not in result:
                            result.append(strcomps[l])
    return result

def getCommonByStudents(studentName1, studentName2):
    result = []
    std1ID = getStudentID(studentName1)
    if std1ID == '\0':
        return None
    std2ID = getStudentID(studentName2)
    if std2ID == '\0':
        return None
    std1comparr = getCompbyStdID(std1ID)
    std2comparr = getCompbyStdID(std2ID)
    for i in range(len(std1comparr)):
        if std1comparr[i] in std2comparr:
            result.append(std1comparr[i])
    return result


def getProjectByCircuit():
    result = {}
    A = []
    with open('projects.txt','r') as myProj:
        lines = myProj.readlines()
        for i in range(2,len(lines)):
            data = lines[i].split()
            if data[0].strip() not in result:
                A = []
                A.append(data[1].strip())
                result[data[0].strip()] = A
            else:
                result[data[0].strip()].append(data[1].strip())
    for key in result.keys():
        result[key].sort()
    return result

def getCircuitByStudent():
    arrNames = []
    arrIDs = []
    result = {}
    A = []
    with open('students.txt','r') as myStud:
        l = myStud.readlines()
        for i in range(2,len(l)):
            strline = l[i].replace("|",",").split(",")
            arrNames.append(strline[0].strip()+", "+strline[1].strip())
            arrIDs.append(strline[2].strip())
    listfiles = os.listdir('Circuits')
    for j in range(len(listfiles)):
        with open("Circuits/"+listfiles[j],'r') as myFiles:
            lines = myFiles.readlines()
            IDline = lines[1].split(",")
            for s in range(len(IDline)):
                IDline[s] = IDline[s].replace('\n','').strip()
            for k in range(len(IDline)):
                for m in range(len(arrIDs)):
                    if arrIDs[m].strip() == IDline[k]:
                        if arrNames[m].strip() in result:
                            result[arrNames[m].strip()].append(listfiles[j][8:13])
                        else:
                            A = []
                            A.append(listfiles[j][8:13])
                            result[arrNames[m].strip()] = A
    for key in result.keys():
        result[key].sort()
    return result


def getCircuitByStudentPartial(studentName):
    name = studentName.split(",")
    firstname = name[1].strip()
    lastname = name[0].strip()
    IDlist = []
    nameList = []
    result = {}
    A = []
    with open('students.txt','r') as myStud:
        l = myStud.readlines()
        for i in range(2,len(l)):
            line = l[i].replace("|",",").split(",")
            if lastname == line[0].strip() or firstname == line[1].strip():
                IDlist.append(line[2].strip())
                nameList.append(line[0].strip()+", "+line[1].strip())
    if IDlist == [] or nameList == []:
        return None
    listfiles = os.listdir('Circuits')
    for j in range(len(listfiles)):
        with open('Circuits/'+listfiles[j],'r') as myFile:
            line = myFile.readlines()
            IDline = line[1].split(",")
            for k in range(len(IDline)):
                for m in range(len(IDlist)):
                    if IDlist[m].strip() == IDline[k].strip():
                        if nameList[m].strip() not in result:
                            A = []
                            A.append(listfiles[j][8:13])
                            result[nameList[m].strip()] = A
                        else:
                            result[nameList[m].strip()].append(listfiles[j][8:13])
    for key in result.keys():
        result[key].sort()
    return result

if __name__ == "__main__":
    print(getComponentCountByProject(10055))

    print(getComponentCountByStudent("Alexander, Carlos"))

    print(getParticipationByStudent("Barnes, Sean"))

    print(getParticipationByProject("83383848-1D69-40D4-A360-817FB22769ED"))

    print(getProjectByComponent(['T71.386','C407.660']))

    print(getStudentByComponent(('T71.386','C407.660')))

    print(getComponentsByStudents(("Adams, Keith", "Bailey, Catherine", "Gonzalez, Kimberly" )))

    print(getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6","96CC6F98-B44B-4FEB-A06B-390432C1F6EA"))

    print(getCommonByStudents("Adams, Keith", "Bailey, Catherine"))

    print(getProjectByCircuit())

    print(getCircuitByStudent())

    print(getCircuitByStudentPartial("Adams, Keith"))
