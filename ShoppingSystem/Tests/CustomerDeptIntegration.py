# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:54:21 2021

@author: zacha
"""

import Customer 
import Department


def main():
    
    
    #Testing Customer class with inputs
    nam = input("Enter Name: ")
    stre = input("Enter Street: ")
    cit = input("Enter City: ")
    zipc = input("Enter Zip Code: ")
    
    #Testing Department class with inputs
    deptname = input("Enter Department Name: ")
    deptnum = input("Enter Department Number: ")
    descr = input("Enter Description: ")
    deptid = input("Enter Department ID: ")
    
    custo = Customer.Customer(nam,stre,cit,zipc)
    dept = Department.department(deptname,deptnum,descr,deptid)
    
    print("Data entered: ")
    print("Customer name: ", custo.get_name())
    print("Street name: ", custo.get_street())
    print("Department name: ", dept.get_department_name())
    print("Department number: ", dept.get_department_number())
    
    
main()