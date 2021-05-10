# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:54:22 2021

@author: zacha
"""

import Customer 
import Product


def main():
    
    
    #Testing Customer class with inputs
    nam = input("Enter Name: ")
    stre = input("Enter Street: ")
    cit = input("Enter City: ")
    zipc = input("Enter Zip Code: ")
    
      #Testing Product class with inputs
    prodname = input("Enter Product Name: ")
    prodbra = input("Enter Product Brand: ")
    prodid = input("Enter Product ID: ")
    prodpri = input("Enter Product Price: ")
    prodcou = input("Enter Product Country: ")
    
    custo = Customer.Customer(nam,stre,cit,zipc)
    prod = Product.product(prodname,prodbra,prodid,prodpri,prodcou)
    
    print("Data entered: ")
    print("Street name: ", custo.get_street())
    print("City name: ", custo.get_city())
    print("Product name: ", prod.get_product_name())
    print("Product brand: ", prod.get_product_brand())
    
    
main()