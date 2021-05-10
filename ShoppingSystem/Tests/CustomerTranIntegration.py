# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:54:22 2021

@author: zacha
"""

import Customer 
import Transaction


def main():
    
    
    #Testing Customer class with inputs
    nam = input("Enter Name: ")
    stre = input("Enter Street: ")
    cit = input("Enter City: ")
    zipc = input("Enter Zip Code: ")
    
    #Testing transaction class with inputs
    tprice = input("Enter Total Price: ")
    payinf = input("Enter Payment Info: ")
    cust = input("Enter Customer: ")
    ccnum = input("Enter CC Number: ")
    ccexp = input("Enter CC Expiration Date: ")
    
    custo = Customer.Customer(nam,stre,cit,zipc)
    tran = Transaction.transaction(tprice,payinf,cust,ccnum,ccexp)
    
    print("Data entered: ")
    print("City name: ", custo.get_city())
    print("Zip Code: ", custo.get_zip_code())
    print("Total price: ", tran.get_total_price())
    print("Payment info: ", tran.get_payment_info())
    
    
main()