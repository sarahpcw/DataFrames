import pandas as pd
mydict = {
'Name'  : ['Anastasia', 'Katherine', 'James'],
'City'  : ['California', 'Los Angeles',  'Boston'],
'Year'  : [1991, 1992 , 2005],
}
frame = pd.DataFrame(mydict, index=[0,1,2]) # to join 2 dataframes : first name sure indexes are the same
print ( frame )

salary    = [2000, 3000, 44000] # create a dataframe from the list and join to main dataframe
z = pd.DataFrame(salary, index=[0,1,2], columns=['Salary'])#   first name sure indexes are the same
print (z)


frame  = frame.join( z , how = 'outer')
print ( frame )

job_title = ['Manager','Director','Sales Person'] # create a dataframe from the list and join to main dataframe
z = pd.DataFrame(salary, index=[0,1,2], columns=['JobTitle'])#   first name sure indexes are the same
frame = frame.join( z , how = 'outer')
print (frame )

Age = [21,26,31] # create a dataframe from the list and join to main dataframe
z = pd.DataFrame(salary, index=[0,1,2], columns=['Age'])#   first name sure indexes are the same
frame = frame.join( z , how = 'outer')
print ( frame )