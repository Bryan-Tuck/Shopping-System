# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:38:00 2021

@author: Bryan
"""

class department:
    def __init__(self, department_name, department_number, description, department_id):

        #Constructors
        self.__department_name = department_name
        self.__department_number = department_number
        self.__description = description
        self.__department_id = department_id
        
    ##Setters and Getters begin   
    def set_department_name(self, department_name):
        self.__department_name = department_name
            
    def set_department_number(self, department_number):
        self.__department_number = department_number
            
    def set_description(self, description):
        self.__description = description
    
    def set_department_id(self, department_id):
        self.__department_id = department_id
        
    def get_department_name(self):
        return self.__department_name
    
    def get_department_number(self):
        return self.__department_number
    
    def get_description(self):
        return self.__description
    
    def get_department_id(self):
        return self.__department_id
    ##Setters and Getters end    

        


