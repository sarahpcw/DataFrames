import pandas as pd
import numpy   as np
# as values : integers, float, string, list, tuple
mydict = {
'Name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'City':  ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
'Salary': [2000, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
'Age':[21,21,31,24,35,46,27,38,49,50]
}

print ( 'Length', len(mydict['Name']) ) 
print ( 'Length', len(mydict['City']) ) 
print ( 'Length', len(mydict['Salary']) ) 
print ( 'Length', len(mydict['Age']) ) 
print ( 'Length', len(mydict['Job Title']) ) 
##
dictKeys = mydict.keys()
print ('Keys', dictKeys)

##
for  key, val  in mydict.items():
    print (key,"==>", val)

frame = pd.DataFrame(mydict)
print (frame)
##shape
print (frame.shape) #shape
#
print ('col', frame.columns)
print ( 'indexes', frame.index.values)
#
#value = 'The Wolf of Wallstreet'
#print ( value[0], value[4:8])   # with string, lists and tuples , simply slice

print(frame.loc[1:7,'Name':'Salary'])  # slice by index and column names

print(frame.loc[1,'Name':'Salary'])

print(frame.loc[1:4,'Name'])

print(frame.loc[[1,7],'Name':'Salary'])

print(frame.loc[[1,7],['Name','Salary']])


# slice by position # Selecting Elements In A Series
print(frame.iloc[3])

print(frame.iloc[1:4,:]) 
 
print(frame.iloc[:,1:2]) 
 
print(frame.iloc[1,1]) 

 



