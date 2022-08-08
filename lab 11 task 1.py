#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:49:12 2022

@author: macbook
"""

from abc import ABC,abstractmethod
class Employee(ABC):
    
    def __init__(self, name, CNIC):
        self.__name = name
        self.__CNIC = CNIC
        
    @abstractmethod
    def monthly_earnings(self):
        pass
    
    def get_details(self):
        return self.__name, "and", self.__CNIC
    
class SalariedEmployee(Employee):
    def __init__(self, weeklySalary, name, CNIC):
        super(). __init__(name, CNIC)
        self.__weeklySalary = weeklySalary

    def monthly_earnings(self):
        return 4 * self.__weeklySalary
    
    def get_details(self):
        return super().get_details(), "and", self.monthly_earnings()
    
class HourlyEmployee(Employee):
    def __init__(self, wage, hours, name, CNIC):
        super(). __init__(name, CNIC)
        self.__wage = wage
        self.__hours = hours
        
    def monthly_earnings(self):
        if self.__hours > 40:
            a = (self.__hours - 40)*1.5
            b = a * self.__wage
            c = b + (self.__wage * 40)
            return c
        else:
            return self.__wage * self.__hours
        
    def get_details(self):
        return super().get_details(), "and", self.monthly_earnings()
    
def main():
    E1 = SalariedEmployee(x, y, z)
    E2 = SalariedEmployee(r, s, t)
    E3 = HourlyEmployee(e, f, g, h)
    print(E1.monthly_earnings())
    print(E1.get_details())
    print(E2.monthly_earnings())
    print(E2.get_details())
    print(E3.monthly_earnings())
    print(E3.get_details())
x = int(input("Weekly salary of employee 1 : "))
y = str(input("Name of employee 1 : "))
z = int(input("CNIC number of employee 1 : "))
r = int(input("Weekly salary of employee 2 : "))
s = str(input("Name of employee 2 : "))
t = int(input("CNIC number of employee 2 : "))
e = float(input("wage of employee 3 : "))
f = float(input("Total hours of employee 3 :"))
g = str(input("Name of employee 3 : "))
h = int(input("CNIC number of employee 3 : "))
main()