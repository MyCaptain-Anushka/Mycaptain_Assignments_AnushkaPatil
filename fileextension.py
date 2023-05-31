# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:52:02 2023

@author: anush
"""
filename = input(" The Filename is : ")
fextns = filename.split(".")
print ("The File extension is : " + repr(fextns[-1]))