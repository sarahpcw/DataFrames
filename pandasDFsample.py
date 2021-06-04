# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 20:21:00 2019

@author: u
"""

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5,5),index=['a','b','c','d','e'],columns = ['one','two','three','4','5'])
#print(df1)

#dropping a rows
df2 = df.drop('e')  # to drop a row, you need to have the row index
print ('df2')
print (df2) 
print (df2.index)
 

print ('msg 3')
df2 = df.sample(2) # 2 randomly selected  rows
df3 = df.sample(frac=0.4) #percentage
print (df2)
print (df3)