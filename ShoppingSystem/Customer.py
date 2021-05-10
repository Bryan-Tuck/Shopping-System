# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:40:08 2021

@author: Bryan
"""
# import pickle

class Customer:
    
    #Constructor
    def __init__(self, name, street, city, zip_code):
        self.__name = name       
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code
        
        
        
        
    ##Setters and Getters Begin    
    def set_name(self, name):
        self.__name = name        
        
    def set_street(self, street):
        self.__street = street
        
    def set_city(self, city):
        self.__city = city
    
    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code
        
    def get_name(self):
        return self.__name     
        
    def get_street(self):
        return self.__street 
        
    def get_city(self):
        return self.__city 
    
    def get_zip_code(self):
        return self.__zip_code     
    ##Setters and Getters End   

               
               

                
    





