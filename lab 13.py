#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:18:50 2022

@author: macbook
"""

class Book:
    class Author:
        def __init__(self,name, email):
            self.__name = name
            self.__email = email
            
        def __str__(self):
            return ("Name: {}, Email: {}".format(self.__name,self.__email))
            
    def __init__(self,tittle):
        self.__tittle = tittle
        self.__price = 14.5
        
    def __str__(self):
        a = input("name")
        b = input("email")
        r = self.Author(a,b)
        return ("Tittle: {}, Author: {}, Price:{}".format(self.__tittle,r,self.__price))
def main():
    my_book = Book("xyz")
    print(my_book)
main()
        
        
        