# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:55:57 2023

@author: anush
"""
list1 = [-1,7,6,-13,-23,33,123,-220,15,23,-41]
nos = 0
print("The positive nos. form the list are")
while(nos < len(list1)):
     
    if list1[nos] >= 0:
        print( list1[nos], end = " ")
     
    nos += 1
