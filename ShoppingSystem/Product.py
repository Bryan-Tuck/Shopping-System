# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:39:43 2021

@author: Bryan
"""
class product:
    def __init__(self, productName, productBrand, productID, productPrice, productCode, productCountry):
        self.name = productName
        self.brand = productBrand
        self.ID = productID
        self.price = productPrice
        self.code = productCode
        self.country = productCountry
 

 
    def setproductName(self, productName):
        self.productName  = productName
        
    def getproductName(self):
        return self.productName
    
    def setproductBrand (self, productBrand):
        self.productBrand = productBrand
        
    def getproductBrand (self):
        return self.productBrand
    
    def setproductID (self, productID):
        self.productID = productID
        
    def getproductID (self):
        return self.productID
    
    def setproductPrice (self, productPrice):
        self.productPrice = productPrice
        
    def getproductPrice(self):
        return self.productPrice
    
    def setproductCode (self, productCode):
        self.productCode = productCode
        
    def get productCode (self):
        return self.productCode
    
    def setproductCountry (self, productCountry):
        self.productCountry = productCountry
        
    def getproductCountry (self):
        return self.productCountry
