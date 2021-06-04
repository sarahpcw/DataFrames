# join a 2 dataframes
import pandas as pd
import numpy as np


mydict = {
'Name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'City': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
'Salary': [2000, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
'Year': [1,2,3,4,5,6,7,8,9,0],
'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
'Age':[21,21,31,21,31,46,21,38,49,31]

}


frame = pd.DataFrame(mydict, index=[0,1,2,3,4,5,6,7,8,9]) # to join 2 dataframes : first name sure indexes are the same
print ( frame)

x = frame.loc[:,'Salary':'Salary'] # get my slice
z = x * 2     # create my new values
print ( z)

z = pd.DataFrame(z, index=[0,1,2,3,4,5,6,7,8,9])#   first name sure indexes are the same

z = z.rename(columns={'Salary': 'NewCol'}) # rename the column name , because join does not allow the overlap in columns
print ( z )
#
#print ('--------') 
y = frame.join( z , how = 'outer')
print ( y)
#
#mylist = [1,2]
#print (max(mylist))
#print (min(mylist))
##print (count(mylist))
#print (max(mylist))
#print (max(mylist))