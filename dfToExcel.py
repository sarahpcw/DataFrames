# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:55:18 2020

@author: u
"""

import pandas as pd
import numpy as np
frame = pd.DataFrame({
'Name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'City': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
'Salary': [2000, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
'Age':[21,21,31,24,35,46,27,38,49,50]
})
 
#create a excel file from the dataframe
frame.to_excel('anastasia.xlsx')
#read the excel file , it returns a dataframe
excel_dataframe = pd.read_excel('anastasia.xlsx')  # it does not create the extra column on the left 

#inspect the dataframe
print (excel_dataframe)
print ('Shape\n', excel_dataframe.shape) #shape
print ('Column Names: \n', excel_dataframe.columns)
print ('Indexes: \n', excel_dataframe.index.values)
print ('Max',(excel_dataframe.index.values.max()))  #largest index value
print ('Max',(excel_dataframe.index.values.min()))  #largest index value

print ( frame.loc[:,['Name','City']])

# create a excel file from the dataframe, using sheet names
# extract a subset of records into a dataframe
df4 = frame.query('City == "California"')
print ( df4 )
# write the dataframe to an excel file specifying the sheetname
df4.to_excel('anastasia1.xlsx', sheet_name='Sheet1')
# read the excel file, specified sheetname only, into a dataframe
excel_dataframe = pd.read_excel('anastasia1.xlsx',sheet_name='Sheet1')  # it does not create the extra column on the left 
print (excel_dataframe.shape)


# extract a subset of records into a dataframe
df4 = frame.query('City == "Los Angeles"')
print ( df4 )
# write the dataframe to an excel file specifying the sheetname
df4.to_excel('anastasia1.xlsx', sheet_name='Sheet2')
# read the excel file, specified sheetname only, into a dataframe
excel_dataframe = pd.read_excel('anastasia1.xlsx',sheet_name='Sheet2')  # it does not create the extra column on the left 
print (excel_dataframe.shape)


# extract a subset of records into a dataframe
df4 = frame.query('City == "Georgia"')
print ( df4 )
# write the dataframe to an excel file specifying the sheetname
df4.to_excel('anastasia1.xlsx', sheet_name='Sheet3')
# read the excel file, specified sheetname only, into a dataframe
excel_dataframe = pd.read_excel('anastasia1.xlsx',sheet_name='Sheet3')  # it does not create the extra column on the left 
print (excel_dataframe.shape)