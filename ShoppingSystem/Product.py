# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:39:43 2021

@author: Bryan
"""
class product:
    
    #Constructor
    def __init__(self, product_name, product_brand, product_id, product_price, product_country):
        self.product_name = product_name
        self.product_brand = product_brand
        self.product_id = product_id
        self.product_price = product_price
        self.product_country = product_country
 

    ##Setters and Getters begin
    def set_product_name(self, product_name):
        self.product_name  = product_name
        
    def set_product_Brand (self, product_brand):
        self.product_brand = product_brand

    def set_product_id (self, product_id):
        self.product_id = product_id   

    def set_product_Price (self, product_price):
        self.product_price = product_price
 
    def set_product_country (self, product_country):
        self.product_country = product_country
        
    def get_product_name(self):
        return self.product_name    
        
    def get_product_brand (self):
        return self.product_brand   
        
    def get_product_id (self):
        return self.product_id   
    
    #Tax is automatically includedat 0.6
    def get_product_price(self):
        return self.product_price        
        
    def get_product_country (self):
        return self.product_country
    ##Setters and Getters end