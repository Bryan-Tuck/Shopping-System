# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:38:40 2021

@author: Bryan
"""

import Transaction

def main():
    
    #Testing transaction class with inputs
    tname = input("Enter transaction name: ")
    tprice = input("Enter Total Price: ")
    payinf = input("Enter Payment Info: ")
    cust = input("Enter Customer: ")
    ccnum = input("Enter CC Number: ")
    ccexp = input("Enter CC Expiration Date: ")
    
    tran = Transaction.transaction(tname,tprice,payinf,cust,ccnum,ccexp)
    #Displaying data entered
    print("Data entered: ")
    print("Transaction Name: ", tran.get_transaction_name())
    print("Total price: ", tran.get_total_price())
    print("Payment info: ", tran.get_payment_info())
    print("Customer: ", tran.get_customer())
    print("CC Number: ", tran.get_cc_number())
    print("CC Expiration Date: ", tran.get_cc_expdate())
        
    
main()