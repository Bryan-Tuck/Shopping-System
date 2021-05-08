# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:55:23 2021

@author: Bryan
"""

import Customer 

def main():
    
    
    
    nam = input("Enter Name:")
    stre = input("Enter Street")
    cit = input("Enter City")
    zipc = input("Enter Zip Code")
    
    custo = Customer.Customer(nam,stre,cit,zipc)
    
    print("Data entered: ")
    print("Customer name: ", custo.get_name())
    print("Street name: ", custo.get_street())
    print("City name: ", custo.get_city())
    print("Zip Code: ", custo.get_zip_code())
    
main()
    