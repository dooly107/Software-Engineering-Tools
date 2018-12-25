#! /usr/bin/env python3.4
import sys
from enum import Enum
from random import randint

class Level(Enum):
    freshman = 1
    sophomore = 2
    junior = 3
    senior = 4
    def __str__(self):
        return self.name


class Student:
    def __init__(self,ID,firstname,lastname,level):
        self.ID = ID
        self.firstname = firstname
        self.lastname = lastname
        self.level = level
        if level.lower() in Level.__members__:
            self.level = Level.__getattr__(level.lower())
        else:
            raise TypeError("The argument must be an instance of the 'Level' Enum")

    def __str__(self):
        return self.ID+", "+self.firstname+" "+self.lastname+", "+str(self.level).title()

class Circuit:
    def __init__(self,ID,resistors,capacitors,inductors,transistors):
        self.ID = ID
        for res in resistors:
            if res[0] != "R":
                raise ValueError("The resistors' list contain invalid components.")
        for cap in capacitors:
            if cap[0] != "C":
                raise ValueError("The capacitors' list contain invalid components.")
        for ind in inductors:
            if ind[0] != "L":
                raise ValueError("The inductors' list contain invalid components.")
        for trans in transistors:
            if trans[0] != "T":
                raise ValueError("The transistors' list contain invalid components.")
        self.resistors = resistors
        self.capacitors = capacitors
        self.inductors = inductors
        self.transistors = transistors

    def __str__(self):
        res_count = str('%02d' % len(self.resistors))
        cap_count = str('%02d' % len(self.capacitors))
        ind_count = str('%02d' % len(self.inductors))
        trans_count = str('%02d' % len(self.transistors))
        return self.ID+": (R = "+res_count+", C = "+cap_count+", L = "+ind_count+", T = "+trans_count+")"

    def getDetails(self):
        res_set = self.resistors
        cap_set = self.capacitors
        ind_set = self.inductors
        trans_set = self.transistors
        res_set.sort()
        cap_set.sort()
        ind_set.sort()
        trans_set.sort()
        final_set = []
        for i in res_set:
            final_set.append(i)
        for j in cap_set:
            final_set.append(j)
        for k in ind_set:
            final_set.append(k)
        for l in trans_set:
            final_set.append(l)
        set_string = ", ".join(str(element) for element in final_set)
        return self.ID+": "+set_string

    def __contains__(self, component):
        if type(component) != type(str()):
            raise TypeError("The component in question should be in type of 'string'.")
        if component[0] == "R" or component[0] == "C" or component[0] == "L" or component[0] == "T":
            if component in self.resistors:
                return True
            elif component in self.capacitors:
                return True
            elif component in self.inductors:
                return True
            elif component in self.transistors:
                return True
            else:
                return False
        else:
            raise ValueError("The component in question does not start with 'R' or 'C' or 'L' or 'T'.")

    def typeofcomponent(self, component):
        if type(component) == type(str()):
            a = 1
        elif type(component) == type(self):
            a = 2
        else:
            a = 3
        return a

    def __add__(self, component):
        a = self.typeofcomponent(component)
        if a == 3:
            raise TypeError("The component in question should be in type of 'string' or class 'Circuit'.")
        elif a == 1:
            if component[0] == "R":
                if component in self.resistors:
                    pass
                else:
                    self.resistors.append(component)
            elif component[0] == "C":
                if component in self.capacitors:
                    pass
                else:
                    self.capacitors.append(component)
            elif component[0] == "L":
                if component in self.inductors:
                    pass
                else:
                    self.inductors.append(component)
            elif component[0] == "T":
                if component in self.transistors:
                    pass
                else:
                    self.transistors.append(component)
            else:
                raise ValueError("The component in question does not start with 'R' or 'C' or 'L' or 'T'.")
            return self
        elif a == 2:
            ID = str(randint(0,99999)).zfill(5)
            resistors = self.resistors
            capacitors = self.capacitors
            inductors = self.inductors
            transistors = self.transistors
            for res in component.resistors:
                if res not in resistors:
                    resistors.append(res)
            for cap in component.capacitors:
                if cap not in capacitors:
                    capacitors.append(cap)
            for ind in component.inductors:
                if ind not in inductors:
                    inductors.append(ind)
            for trans in component.transistors:
                if trans not in transistors:
                    transistors.append(trans)
            resistors.sort()
            capacitors.sort()
            inductors.sort()
            transistors.sort()
            new_circuit = Circuit(ID,resistors,capacitors,inductors,transistors)
            return new_circuit

    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, component):
        if type(component) != type(str()):
            raise TypeError("The component in question should be in type of 'string'.")
        if component[0] == "R":
            if component not in self.resistors:
                pass
            else:
                self.resistors.remove(component)
        elif component[0] == "C":
            if component not in self.capacitors:
                pass
            else:
                self.capacitors.remove(component)
        elif component[0] == "L":
            if component not in self.inductors:
                pass
            else:
                self.inductors.remove(component)
        elif component[0] == "T":
            if component not in self.transistors:
                pass
            else:
                self.transistors.remove(component)
        else:
            raise ValueError("The component in question does not start with 'R' or 'C' or 'L' or 'T'.")
        return self



class Project:
    def __init__(self,ID,participants,circuits):
        self.ID = ID
        if participants == []:
            raise ValueError("The participants list passed to the argument is empty.")
        elif circuits == []:
            raise ValueError("The circuits list passed to the argument is empty.")
        else:
            for people in participants:
                if type(people) != Student:
                    raise ValueError("The element in participant list is not a type of 'Student'.")
            for circuit in circuits:
                if type(circuit) != Circuit:
                    raise ValueError("The element in circuit list is not a type of 'Circuit'.")
            self.participants = participants
            self.circuits = circuits

    def __str__(self):
        num_circuits = str(len(self.circuits)).zfill(2)
        num_participants = str(len(self.participants)).zfill(2)
        return self.ID+": "+num_circuits+" Circuits, "+num_participants+" Participants"

    def getdetails(self):
        sort_participant = self.participants
        sort_participant.sort(key = lambda x: x.ID)
        sort_circuit = self.circuits
        sort_circuit.sort(key = lambda y: y.ID)
        arr_participant = []
        arr_circuit = []
        for i in sort_participant:
            string_participant = i.__str__()
            arr_participant.append(string_participant)
        for j in sort_circuit:
            string_circuit = j.__str__()
            arr_circuit.append(string_circuit)
        str_participant_final = "\n".join(str(element) for element in arr_participant)
        str_circuit_final = "\n".join(str(element) for element in arr_circuit)
        return self.ID+"\n\nParticipants:\n"+str_participant_final+"\n\nCircuits:\n"+str_circuit_final

    def gettypecomponent(self,component):
        if type(component) == type(str()):
            a = 1
        elif type(component) == Circuit:
            a = 2
        elif type(component) == Student:
            a = 3
        else:
            a = 4
        return a

    def __contains__(self, component):
        typeofcomponent = self.gettypecomponent(component)
        if typeofcomponent == 4:
            raise TypeError("The component in question should be in type of 'string', class 'Circuit' or class 'Student'.")
        elif typeofcomponent == 1:
            if component[0] == "R" or component[0] == "C" or component[0] == "L" or component[0] == "T":
                for element in self.circuits:
                    if component in element.resistors:
                        return True
                    elif component in element.capacitors:
                        return True
                    elif component in element.inductors:
                        return True
                    elif component in element.transistors:
                        return True
                    else:
                        pass
                return False
            else:
                raise ValueError("The component in question does not start with 'R' or 'C' or 'L' or 'T'.")
        elif typeofcomponent == 2:
            if component in self.circuits:
                return True
            else:
                return False
        elif typeofcomponent == 3:
            if component in self.participants:
                return True
            else:
                return False

    def __add__(self, component):
        typeofcomponent = self.gettypecomponent(component)
        if typeofcomponent == 1 or typeofcomponent == 4:
            raise TypeError("The circuit in question is not an instance of the Circuit class nor Student class.")
        else:
            if typeofcomponent == 2:
                if component in self.circuits:
                    pass
                else:
                    self.circuits.append(component)
            elif typeofcomponent == 3:
                if component in self.participants:
                    pass
                else:
                    self.participants.append(component)
        return self

    def __sub__(self, component):
        typeofcomponent = self.gettypecomponent(component)
        if typeofcomponent == 1 or typeofcomponent == 4:
            raise TypeError("The circuit in question is not an instance of the Circuit class nor Student class.")
        else:
            if typeofcomponent == 2:
                if component not in self.circuits:
                    pass
                else:
                    self.circuits.remove(component)
            elif typeofcomponent == 3:
                if component not in self.participants:
                    pass
                else:
                    self.participants.remove(component)
        return self



class Capstone(Project):
    def __init__(self,ID,participants,circuits):
        Project.__init__(self,ID,participants,circuits)
        for people in self.participants:
            if people.level != Level.senior:
                raise ValueError("One or some or all the people participating in project is not 'Senior'")

    def __add__(self,component):
        Project.__add__(self,component)
        if type(component) == Student:
            if component.level != Level.senior:
                raise ValueError("The participant that has been added to Project is not a 'Senior'.")


if __name__ == "__main__":
    student1 = Student("15487-79431","John","Purdue","Freshman")
    print(str(student1))

    circuit1 = Circuit("99887",["R302.104", "R204.182"], ["C102.493","C402.213"],[],["T492.385"])
    print(str(circuit1))
    print(circuit1.getDetails())
    print("R302.104" in circuit1)

    circuit1 + "R102.394"
    print("R102.394" in circuit1)
    "C495.182" + circuit1
    print("C495.182" in circuit1)
    print(str(circuit1))

    circuit1 - "R302.104"
    print("R302.104" in circuit1)

    circuit2 = Circuit("30241",["R202.154", "R254.122"], ["C702.423","C86.213"],["L148.371"],["T952.385"])

    circuit3 = circuit1 + circuit2
    print(str(circuit3))
    print("L148.371" in circuit3)

    student2 = Student("13423-83612", "Sang", "Kim", "Senior")
    student3 = Student("14483-88272", "Eric", "Kim", "Junior")
    proj1 = Project("38753067-e3a8-4c9e-bbde-cd13165fa21e", [student1,student2,student3], [circuit1,circuit2,circuit3])
    print(str(proj1))
    print(proj1.getdetails())

    print("T952.385" in proj1)
    print(circuit1 in proj1)
    print(student1 in proj1)
    student4 = Student("19273-79431","John","Purdue","Freshman")
    print(student4 in proj1)
    circuit4 = Circuit("78291",["R202.154", "R254.122"], ["C702.423","C86.213"],["L148.371"],["T952.385"])
    print(circuit4 in proj1)

    proj1 + circuit4
    print(circuit4 in proj1)
    proj1 - circuit4
    print(circuit4 in proj1)

    proj1 + student4
    print(student4 in proj1)
    proj1 - student4
    print(student4 in proj1)

    student1 = Student("42813-28174", "Chulwoo", "Park", "Senior")
    student2 = Student("13423-83612", "Sang", "Kim", "Senior")
    student3 = Student("14483-88272", "Eric", "Kim", "Senior")
    proj2 = Capstone("38753067-e3a8-4c9e-bbde-cd13165fa21e", [student1,student2,student3], [circuit1,circuit2,circuit3])
    student4 = Student("19273-79431","John","Purdue","Senior")
    proj2 + student4
    print(str(proj2))