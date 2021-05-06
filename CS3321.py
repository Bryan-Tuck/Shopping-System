##########################
# CS3321 Shopping Project
# By 
# UHD 
###########################

import numpy as np

class search:

    def __init__(self, keyword, prodInfo, deptInfo, newSearch):
        
        self.keyword = keyword
        self.prodInfo = prodInfo
        self.deptInfo = deptInfo
        self.newSearch = newSearch
                      
    def readFileName(file):
        file_object  = open("filename", "mode") 
        if (file is valid(file)):
            return file_object
        else:
            return FileNotFoundError

    def stringPrint(self, prodInfo, deptInfo):
        if isinstance(self, prodInfo):
            print(prodInfo)
        else:
            print(deptInfo)
                       
    def newSearch(filename, search_path):
        result = []
        for result(search_path)
            if filename in file:
                result.append(search)
                return result  

    def searchKeyword(list, keyword):
        for i in range(len(list)):
            if list[i] == keyword:
                return True
            return False

    def searchProdInfo(list, prodInfo):
        for i in range(len(list)):
            if list[i] == prodInfo:
                return True
            return False
        
    def searchDeptInfo(list, deptInfo):
        for i in range(len(list)):
            if list[i] == deptInfo:
                return True
            return False            
         
    def getKeyword(self, keyword):
        if isinstance(keyword, str):
            keyword = [keyword]
        self.keyword = list(keyword)
        return keyword
        

    def getProdInfo(self, prodInfo):
        if isinstance(prodInfo, str):
            prodInfo = [prodInfo]
            self.prodInfo = list(prodInfo)
            return prodInfo
            
                        
    def getDeptInfo(self, deptInfo):
        if isinstance(deptInfo):
            deptInfo = [deptInfo]
            self.deptInfo = list(deptInfo)
            return deptInfo

