# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:38:00 2021

@author: Bryan
"""

class department:
    def __init__(self, name, number, description, identification):

        self.name = name
        self.number = number
        self.description = description
        self.identification = identification

    def Name(self, name):
        self.name = name


    def Number(self, number):
        self.number = number


    def Description(self, description):
        self.description = description


    def Identification(self, identification):
        self.identification = identification


