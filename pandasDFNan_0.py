# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:30:10 2019

@author: u
"""

#!nan values
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns = ['one','two','three'])
#print(df1)

# create NaN values in rows b and d
df1=df1.reindex(['a','b','c','d','e']) 


#print (df1)


print ('-1-',np.NaN in df1 )  
#print ('-2-',np.nan in df1 )
#print ('-4-',float(np.nan) in df1 )	
#
print ('-5-',df1.isnull().values.any())
print ('-6-\n', df1.isnull().sum())
#print ( '-7-', df1.notnull())
#print ('-5-',df1.isnull())
#	 
#for index,row in df.iterrows():
#    print("{0} has name: {1}".format(index,row["Player"]))
    
