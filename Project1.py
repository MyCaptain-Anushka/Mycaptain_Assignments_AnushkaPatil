# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:39:51 2023

@author: anush
"""
#Project 1 : Basic school adminstration tool

import csv


def write_into_csv(info_list):
    with open ('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name" ,"Age","Contact Number","E-mail"])
            
        writer.writerow(info_list)

if __name__ == '__main__':
         condition = True 
         student_num = 1



while(condition):
    student_info = input("Enter student information in the following format (Name Age Contact_Number E-mail):")
    print("Entered information :" + student_info)
    
    #split
    student_info_list = student_info.split(' ')
    print("\n Entered split up information is - \nName: {}\nAge: {}\nContact number: {}\nE-mail: {}" 
    .format(student_info_list[0] ,student_info_list[1] ,student_info_list[2] ,student_info_list[3]))
    
    choice_check = input(" Is entered information correct ? (yes/no):")
    
    if choice_check== "yes":
        write_into_csv(student_info_list)

    condition_check=input("Enter (yes/no) if you want to enter information for another student:")
    if condition_check =="yes":
        condition = True
    elif condition_check=="no":
        condition= False