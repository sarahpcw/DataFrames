# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:45:11 2020

@author: u
"""

import pandas as pd
class df ():
    
    def DfExtract (self):
        frame = pd.read_csv('anastasia.csv')  # it creates an extra column on the left, which is like an index
        print (frame)
        return frame
        
    def printDfData (self, frame):  
        print ('Shape\n', frame.shape) #shape
        print ('col', frame.columns)
        print ( 'indexes', frame.index.values)
        
    
    def printCols (self, frame):
        mylist = ['Name','City']
        print ( frame.loc[:,mylist])
        print ( frame.loc[:,['Name','City']])
        