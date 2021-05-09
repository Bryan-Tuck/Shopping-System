# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:39:59 2021

@author: Bryan
"""

class Transaction:
    
    #Constructor
    def __init__(self, transaction_name, total_price, payment_info, cc_number, cc_expdate):
 
        self.__total_price = total_price
        self.__payment_info = payment_info
        self.__customer = transaction_name
        self.__cc_number = cc_number
        self.__cc_expdate = cc_expdate
 
    ##Setters and Getters begin
    def set_total_price (self, total_price):
        self.__total_price = total_price      
    
    def set_payment_info (self, payment_info):
        self.__paymentinfo = payment_info
        
    def set_customer (self, transaction_name):
        self.__transaction_name = transaction_name

    def set_cc_number (self, cc_number):
        self.__cc_number = cc_number 
        
    def set_ccexpdate (self, cc_expdate):
        self.__cc_expdate = cc_expdate
        
    def get_total_price (self):
        return self.total_price  
        
    def get_payment_info (self):
        return self.payment_info
           
    def get_transaction_name (self):
        return self.__transaction_name
            
    def get_cc_number (self):
        return self.__ccnumber    

    def get_cc_expdate (self):
        return self.__cc_expdate
    ##Setters and Getters end
  
 
                                      