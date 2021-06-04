# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:50:30 2020

@author: u
"""
import pandas as pd
import numpy as np


mydict = {
'Name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'City': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
'Salary': [2000, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
'Year': [2020, 2019, 2018,2020, 2019, 2018,2020, 2019, 2018,2020],
'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
'Age':[21,21,31,21,31,46,21,38,49,31]
}


#for key ,  value in mydict.items(): 
#    if 'Salary' in key:   #    if value and 'Salary' in value.keys(): 
#        print (len(value))
#        for i in range ( len(value)):
#            mydict['Salary'][i] = value[i] * 2
        

mydict['NewCol'] = np.zeros(10)
print (type ( mydict['NewCol'] ) , mydict['NewCol'] )
for i in range ( len(mydict['Salary'])):
    mydict['NewCol'][i] = mydict['Salary'][i] * 2

print ( mydict)        
        
frame = pd.DataFrame(mydict)

mytuple = (1,2,3,4,5,6,7,8,9,0)
x = np.array(mytuple)
print ( type ( x ))

y = np.array(frame['Salary'])
print (type (y))

z = y * x
print ( z)
