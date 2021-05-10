# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:54:24 2021

@author: zacha
"""

import Product 
import Transaction


def main():
    
    
    #Testing Product class with inputs
    prodname = input("Enter Product Name: ")
    prodbra = input("Enter Product Brand: ")
    prodid = input("Enter Product ID: ")
    prodpri = input("Enter Product Price: ")
    prodcou = input("Enter Product Country: ")
    
    #Testing transaction class with inputs
    tprice = input("Enter Total Price: ")
    payinf = input("Enter Payment Info: ")
    cust = input("Enter Customer: ")
    ccnum = input("Enter CC Number: ")
    ccexp = input("Enter CC Expiration Date: ")
    
    prod = Product.product(prodname,prodbra,prodid,prodpri,prodcou)
    tran = Transaction.transaction(tprice,payinf,cust,ccnum,ccexp)
    
    print("Data entered: ")
    print("Product Price: ", prod.get_product_price())
    print("Product Country: ", prod.get_product_country())
    print("CC Number: ", tran.get_cc_number())
    print("CC Expiration Date: ", tran.get_cc_expdate())
    
    
main()