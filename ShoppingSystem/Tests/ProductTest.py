# -*- coding: utf-8 -*-
"""
Created on Sat May  8 01:30:36 2021

@author: Bryan
"""
import Product


def main():
    
    #Testing Product class with inputs
    prodname = input("Enter Product Name: ")
    prodbra = input("Enter Product Brand: ")
    prodid = input("Enter Product ID: ")
    prodpri = input("Enter Product Price: ")
    prodcou = input("Enter Product Country: ")
    
    prod = Product.product(prodname,prodbra,prodid,prodpri,prodcou)
    #Displaying data entered
    print("Data entered: ")
    print("Product name: ", prod.get_product_name())
    print("Product brand: ", prod.get_product_brand())
    print("Product ID: ", prod.get_product_id())
    print("Product Price: ", prod.get_product_price())
    print("Product Country: ", prod.get_product_country())
    
    
main()