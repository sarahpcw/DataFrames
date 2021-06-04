# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:55:18 2020

@author: u
"""

import pandas as pd
import numpy as np
mydict = {
'Name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'City': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
'Salary': [2000, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
'Age':[21,21,31,24,35,46,27,38,49,50]
}

print ( mydict['Name'])

frame = pd.DataFrame(mydict)
#create a csv file from the dataframe
frame.to_csv('anastasia.csv') 

#you could read the csv file as a data frame or a a file
#read the csv file , it returns a dataframe
csv_dataframe = pd.read_csv('anastasia.csv')  # it creates an extra column on the left, which is like an index
#inspect the dataframe
print (csv_dataframe)
print ('Shape\n', csv_dataframe.shape) #shape
print ('Column Names: \n', csv_dataframe.columns)
print ('Indexes: \n', csv_dataframe.index.values)
print ('Max',(csv_dataframe.index.values.max()))  #largest index value
print ('Max',(csv_dataframe.index.values.min()))  #largest index value

# Dataframe is a collections of series, every column is a series, not that easy to make a 2d list
# make the dataframe into a 2d list
x = [] 
for index,row in csv_dataframe.iterrows():
    print("%s in %s, %s who is a  %s "  % (index, row["City"].ljust(12), row["Name"].ljust(10) ,row["Job Title"]   ))
    x.append(row.tolist())   #Series.tolist(self)[source]¶
for row in x:
    print (row)

# read the csv file as a file ( many lines of txt data)
filein = open('anastasia.csv','r')
for row in filein:
    print ( row )
filein.close()
 