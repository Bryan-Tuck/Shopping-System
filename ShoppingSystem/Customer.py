# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:40:08 2021

@author: Bryan
"""



class Customer:
    def __init__(self, first_name, last_name, street, city, zip_address):
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.city = city
        self.zip_address = zip_address        
        self.customer_data = []
     
       
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def add_customer(self, Customer):
        self.customer_data.append(Customer)
        
        
                                 
           
cust_1 = Customer('Steve', 'Jobs', '10912 Golden Drive', 'Houston', 77044)
customer.add_customer(Customer)


print(cust_1.fullname())



