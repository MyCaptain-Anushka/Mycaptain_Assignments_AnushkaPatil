# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:40:19 2023

@author: anush
"""
total_num=int(input("The total no.of input is="))


n1, n2 = 0, 1
num = 0


if total_num <= 0:
   print("Please enter a positive integer")
   
   
elif total_num == 1:
   print("Fibonacci sequence upto",total_num)
   print(n1)
   
   
else:
   print("The Fibonacci sequence is :")
   while num < total_num:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       num += 1