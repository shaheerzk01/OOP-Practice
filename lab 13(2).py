#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:49:08 2022

@author: macbook
"""

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distance(self, point):
        return (((point.getX() - self.getX()))**2 + (point.getY() - self.getY())**2)**(1/2)
    
class Quadrilateral:
    def __init__(self,a, b, c, d):
        self.__vertex1 = a
        self.__vertex2 = b
        self.__vertex3 = c
        self.__vertex4 = d
        
    def __str__(self):
        V1 = ("V1: {},{}".format(self.__vertex1.getX(),self.__vertex1.getY()))
        V2 = ("V2: {},{}".format(self.__vertex2.getX(),self.__vertex2.getY()))
        V3 = ("V3: {},{}".format(self.__vertex3.getX(),self.__vertex3.getY()))
        V4 = ("V4: {},{}".format(self.__vertex4.getX(),self.__vertex4.getY()))
        return [V1, V2,V3,V4]
    
    
    def getPerimeter(self):
        d1 = (self.__vertex1.distance(self.__vertex2))
        d2 = (self.__vertex2.distance(self.__vertex3))
        d3 = (self.__vertex3.distance(self.__vertex4))
        d4 = (self.__vertex4.distance(self.__vertex1))
        p = d1 + d2 + d3 + d4
        return ("Perimeter: {}".format(p))
    
    def isSquare(self):
        d1 = (self.__vertex1.distance(self.__vertex2))
        d2 = (self.__vertex2.distance(self.__vertex3))
        d3 = (self.__vertex3.distance(self.__vertex4))
        d4 = (self.__vertex4.distance(self.__vertex1))
        if d1 == d2 == d3 ==d4:
            return True
        else:
            return False
        
def main():
    a = int(input("value of X: "))
    b = int(input("value of Y: "))
    c = int(input("value of X: "))
    d = int(input("value of Y: "))
    e = int(input("value of X: "))
    f = int(input("value of Y: "))
    g = int(input("value of X: "))
    h = int(input("value of Y: "))
    point1 = Point(a,b)
    point2 = Point(c,d)
    point3 = Point(e,f)
    point4 = Point(g,h)
    quad = Quadrilateral(point1,point2, point3, point4)
    i = quad.__str__()
    j = quad.getPerimeter()
    k = quad.isSquare()
    print(i,j,k)
main()