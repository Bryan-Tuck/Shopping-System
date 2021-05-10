# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:54:23 2021

@author: zacha
"""

import Department 
import Product


def main():
    
    
    #Testing Department class with inputs
    deptname = input("Enter Department Name: ")
    deptnum = input("Enter Department Number: ")
    descr = input("Enter Description: ")
    deptid = input("Enter Department ID: ")
    
    
    #Testing Product class with inputs
    prodname = input("Enter Product Name: ")
    prodbra = input("Enter Product Brand: ")
    prodid = input("Enter Product ID: ")
    prodpri = input("Enter Product Price: ")
    prodcou = input("Enter Product Country: ")
    
    
    
    dept = Department.department(deptname,deptnum,descr,deptid)
    prod = Product.product(prodname,prodbra,prodid,prodpri,prodcou)
    
    print("Data entered: ")
    print("Department number: ", dept.get_department_number())
    print("Description: ", dept.get_description())
    print("Product ID: ", prod.get_product_id())
    print("Product Price: ", prod.get_product_price())
    
    
main()