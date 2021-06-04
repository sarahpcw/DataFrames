import pandas as pd
import numpy   as np
mydict = {
'Name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'City': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
'Salary': [2000, 3000, np.nan, 5000, 6000, 7000, 8000, 9000, 10000, np.nan],
'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
'Age':[21,21,31,24,35,46,27,38,49,50]
}

print ( 'Length', len(mydict['Name']) ) 
print ( 'Length', len(mydict['City']) ) 
print ( 'Length', len(mydict['Salary']) ) 
print ( 'Length', len(mydict['Age']) ) 
#
dictKeys = mydict.keys()
print ('Keys', dictKeys)
#
##
#for  key, val  in mydict.items():
#    print (key,"==>", val)

frame = pd.DataFrame(mydict)
f = frame.loc[:,'Salary']

final = f.fillna(f.mean())
print ( final)

#print('fill na')
#print( f.fillna(5) ) #Replace missing values.
#
#print('fill na')
#print( f.fillna('Rubbish') )  #Replace missing values.
