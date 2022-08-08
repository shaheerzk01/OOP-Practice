#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:29:29 2022

@author: macbook
"""
from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self, name, CNIC, basicSalary):
        self.__name  = name
        self.__CNIC = CNIC
        self.__basicSalary = basicSalary
        
    def get_name(self):
        return self.__name
    
    def get_CNIC(self):
        return self.__CNIC
    
    def get_basicSalary(self):
        return self.__basicSalary
    
    def set_basicSalary(self, new_salary):
        if isinstance(new_salary, float):
            self.__basicSalary = new_salary
        else:
            print("invalid")
            
    @abstractmethod
    def monthly_earnings(self):
        pass
    
class Manager(Employee):
    def __init__(self, department, house_allowance, name, CNIC, basicSalary):
        super(). __init__(name, CNIC, basicSalary)
        self.__department = department
        self.__house_allowance = house_allowance
        
    def get_department(self):
        return self.__department
    
    def get_house_allowance(self):
        return self.__house_allowance
    
    def set_department(self, new_department):
        if isinstance(new_department, str):
            self.__department = new_department
        else:
            print("invalid")
            
    def set_house_allowance(self, new_house_allowance):
        if isinstance(new_house_allowance, float):
            self.__house_allowance = new_house_allowance
        else:
            print("invalid")
            
    def monthly_earnings(self):
        return super().get_basicSalary() + self.__house_allowance
    
class Developer(Employee):
    def __init__(self, technology, name, CNIC, basicSalary):
        super(). __init__(name, CNIC, basicSalary)
        self.__technology = technology
        
    def get_technology(self):
        return self.__technology
    
    def set_technology(self, new_technology):
        if isinstance(new_technology, str):
            self.__technolgy = new_technology
        else:
            print("invalid")
            
    def monthly_earnings(self):
        return super().get_basicSalary
    
class CEO(Employee):
    def __init__(self, medical_allowance, name, CNIC, basicSalary):
        super(). __init__(name, CNIC, basicSalary)
        self.__medical_allowance = medical_allowance
        
    def get_medical_allowance(self):
        return self.__medical_allowance
    
    def set_mediacl_allowance(self, new_medical_allowance):
        if isinstance(new_medical_allowance, float):
            self.__medical_allowance = new_medical_allowance
        else:
            print("invalid")
            
    def monthly_earnings(self):
        return super().get_basicSalary() + self.__medical_allowance
    
def main():
    E1 = Manager(a, b, c, d, e)
    E2 = Developer(q, r, s, t)
    E3 = CEO(i, j , k, l)
    print(E1.monthly_earnings())
    print(E2.monthly_earnings())
    print(E3.monthly_earnings())
    E1.set_basicSalary(e*0.1)
    E2.set_basicSalary(t*0.07)
    E3.set_basicSalary(l*0.05)
    print(E1.monthly_earnings())
    print(E2.monthly_earnings())
    print(E3.monthly_earnings())
a = str(input("Department of first employee 1 : "))
b = float(input("House allowance of employee 1 : "))
c = str(input("Name of employee 1 :"))
d = int(input("CNIC number or employee 1 : "))
e = float(input("Basic salary of employee 1 : "))
q = str(input("Technology of employee 2 : "))
r = str(input("Name of employee 2 :"))
s = int(input("CNIC number or employee 2 : "))
t = float(input("Basic salary of employee 2 : "))
i = float(input("Medical allowance of employee 3 : "))
j = str(input("Name of employee 3 :"))
k = int(input("CNIC number or employee 3 : "))
l = float(input("Basic salary of employee 3 : "))
main()
    
    
        
            
    


    
        