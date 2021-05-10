# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:54:23 2021

@author: zacha
"""

import Department 
import Transaction


def main():
    
    
    #Testing Department class with inputs
    deptname = input("Enter Department Name: ")
    deptnum = input("Enter Department Number: ")
    descr = input("Enter Description: ")
    deptid = input("Enter Department ID: ")
    
    
    #Testing transaction class with inputs
    tprice = input("Enter Total Price: ")
    payinf = input("Enter Payment Info: ")
    cust = input("Enter Customer: ")
    ccnum = input("Enter CC Number: ")
    ccexp = input("Enter CC Expiration Date: ")
    
    dept = Department.department(deptname,deptnum,descr,deptid)
    tran = Transaction.transaction(tprice,payinf,cust,ccnum,ccexp)
    
    print("Data entered: ")
    print("Description: ", dept.get_description())
    print("Department ID: ", dept.get_department_id())
    print("Customer: ", tran.get_customer())
    print("CC Number: ", tran.get_cc_number())
    
    
main()