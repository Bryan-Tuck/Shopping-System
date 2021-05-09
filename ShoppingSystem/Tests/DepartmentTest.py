# -*- coding: utf-8 -*-
"""
Created on Sat May  8 01:30:25 2021

@author: Bryan
"""
import Department



def main():
        
    #Testing Department class with inputs
    deptname = input("Enter Department Name: ")
    deptnum = input("Enter Department Number: ")
    descr = input("Enter Description: ")
    deptid = input("Enter Department ID: ")
    
    dept = Department.department(deptname,deptnum,descr,deptid)
    #Displaying data entered
    print("Data entered: ")
    print("Department name: ", dept.get_department_name())
    print("Department number: ", dept.get_department_number())
    print("Description: ", dept.get_description())
    print("Department ID: ", dept.get_department_id())
    

main()
