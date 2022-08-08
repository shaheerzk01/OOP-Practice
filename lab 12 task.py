#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:48:34 2022

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
    
    def get_cnic(self):
        return self.__CNIC
    
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
    Employee_register = []
    A = 0
    while A!=5:
        A = eval(input("Add employee(1) \n show employee details(2) \n terminate employee(3) \n show employee register(4) \n to exit application(5)"))
        
        def add_employee(k):
            if k == 1:
                x = int(input("weekly salary of employee : "))
                y = str(input("name : "))
                z = str(input("CNIC : "))  
                c = SalariedEmployee(x,y,z)
            elif k == 0:
                r = int(input("enter wage : "))
                s = int(input("enter hours : "))   
                t = str(input("name : "))
                u = str(input("CNIC : "))
                c = HourlyEmployee(r,s,t,u)
            Employee_register.append(c)
            
        def employee_details(cnic):
            for i in Employee_register:
                if cnic == i.get_cnic():
                    print(i.get_details())
                else:
                    print("not in the register")
                    
        def terminate_employee(cnic):
            for i in Employee_register:
                if cnic == i.get_cnic():
                    Employee_register.remove(i)
                else:
                    print("not in the register")
                    
        def display_emloyee_register():
            for i in  Employee_register:
                employee_details(i.get_cnic())
                    
                    
        if A == 1:
            k = eval(input("enter type of employee : for salaried press 1 and for hourly press 0 : "))
            add_employee(k)
            
        elif A == 2:
            cnic = input("Enter CNIC number : ")
            employee_details(cnic)
            
        elif A == 3: 
            cnic = eval(input("Enter CNIC number : "))
            terminate_employee(cnic)
            
        elif A == 4:
            display_emloyee_register()
            
        elif A == 5:
            break
main()
            
        
        
        
    