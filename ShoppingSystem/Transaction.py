# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:39:59 2021

@author: Bryan
"""

class Transaction:
    transactionList = []

    def __init__(self, totalprice, paymentinfo, customer, ccnumber, ccexpdate):
 
        self.totalprice = totalprice
        self.paymentinfo = paymentinfo
        self.customer = customer
        self.ccnumber = ccnumber
        self.ccexpdate = ccexpdate
        
    def totalprice(self, totalprice):
        self.totalprice = totalprice()

    def paymentinfo(self, paymentinfo):
        self.paymentinfo = paymentinfo()
        
    def customer(self, customer):
        self.customer = customer()
    
    def ccnumber(self, ccnumber):
        self.ccnumber = ccnumber()
    
    def ccexpdate(self, ccexpdate):
        self.ccexpdate = ccexpdate()
        
 
                                             