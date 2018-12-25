#! /usr/bin/env python3.4
import sys

class Rectangle:
    def __init__(self,llPoint,urPoint):
        if type(llPoint) != type(tuple()):
            raise TypeError("llPoint is not a form of tuple")
        if type(urPoint) != type(tuple()):
            raise TypeError("urPoint is not a form of tuple")
        if llPoint[0] >= urPoint[0]:
            raise ValueError("Lower-Left point must be less than Upper-Right point.")
        if llPoint[1] >= urPoint[1]:
            raise ValueError("Lower-Left point must be less than Upper-Right point.")
        self.llPoint = llPoint
        self.urPoint = urPoint

    def isSquare(self):
        width = self.urPoint[0]-self.llPoint[0]
        length = self.urPoint[1]-self.llPoint[1]
        if width == length:
            return True
        else:
            return False

    def isPointInside(self,point):
        if point[0] > self.llPoint[0] and point[0] < self.urPoint[0] and point[1] > self.llPoint[1] and point[1] < urPoint[1]:
            return True
        else:
            return False

    def intersectsWith(self,rect):
        if (self.isPointInside(rect.llPoint) == True) and (self.isPointInside(rect.urPoint) == True):
            return True
        else:
            return False

if __name__ == "__main__":
    llPoint = (4,2)
    urPoint = (8,6)
    rectangle = Rectangle(llPoint,urPoint)
    print(rectangle.isSquare())
    print(rectangle.isPointInside((6,3)))
    llPoint2 = (6,4)
    urPoint2 = (7,5)
    int_rectangle = Rectangle(llPoint2,urPoint2)
    print(rectangle.intersectsWith(int_rectangle))
