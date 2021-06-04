
import pandas as pd
import numpy as np
frame = pd.DataFrame({'Name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'City': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
'Salary': [2000, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
'Age':[21,21,31,24,35,46,27,38,49,50]
})


print (frame)
#shape
print (frame.shape) #shape

print ('col', frame.columns.values)
print ( 'indexes', frame.index.values)

print ( 'description ')
x = frame.describe() 
print (x)

print ('Max',(frame.index.values.max()))  #largest index value
print ('Max',(frame.index.values.min()))  #largest index value




print ( 'iloc\n', frame.iloc[0:5,1:4])  # exclused the end index
print ( 'loc\n', frame.loc[0:5,'City':'Job Title'])  # includes the end index


print ('Maximum Salary: ', frame['Salary'].max())
print ('Minimum Salary: ', frame['Salary'].min())
print ('Average Salary: ', frame['Salary'].mean())
print ('Sum of Salary : ',frame['Salary'].sum())  

print ('Average Age   : ',frame['Age'].mean())  

print ('AllSalary: ', frame['Salary'])
print ('Ranking the salaries\n', frame['Salary'].rank())

print ('AllSalary: \n', frame['Age'])
print ('Ranking the ages\n', frame['Age'].rank())

#group by
g1 = frame.groupby(["City"]).size()
print('\nCount rows, by City -------------- \n',g1)

g1 = frame.groupby(["City"]).size().reset_index(name='Number of people per city')
print('\nCount rows, by City -------------- \n',g1)

g1 = frame.groupby(["City"]).sum()
print('\nSum all the number columns, by City -------------- \n',g1)

g1 = frame.groupby(["Job Title"]).sum()
print('\nSum all the number columns, by Job Title --------------\n',g1)
g1 = frame.groupby(["Job Title"]).sum()
print('\nSum all the number columns, by Job Title , show only the Salary --------------\n',g1.loc[:,['Salary']])

g1 = frame.loc[:,["Job Title","Salary"]]
g1 = g1.groupby(["Job Title"]).sum()
print('\nSum all the number columns, by Job Title , show only the Salary --------------\n',g1)


print('----- Print for every group all the data ( splitting the frame by grouping -----')
g1 = frame.groupby('City') 
for key,item in g1:
    if key == 'California':
        print('Key: ',key,'\n', g1.get_group(key),"\n\n")



g1 = frame.groupby(["Job Title"]).size()
print('\nSum all the number columns, by Job Title --------------\n',g1)
g1 = frame.groupby('Job Title') 
for key,item in g1:
    print('Key: ',key,'\n', g1.get_group(key),"\n\n")


#Using aggregate
grouped = ( frame.groupby(['Name']).agg({  "Salary":np.sum} ) )
print('\n\nAve age and Sum Salary by name\n',  grouped)
print ( '\n\nAverage age adn Average Salary  by city\n',  frame.groupby(['City']).agg({ "Age":np.mean, "Salary":np.mean, } ) )
print ( '\n\nMin age by city\n',  frame.groupby(['City']).agg({ "Age":np.min} ) )
print ( '\n\nMax age by city\n',  frame.groupby(['City']).agg({ "Age":np.max} ) )
print ( '\n\Count age by city\n',  frame.groupby(['City']).agg({ "Age":np.size, "Salary":np.size} ) )

#unique values
print ('Unique names' , frame["Name"].unique() )
print ('Unique Job Titles' , frame["Job Title"].unique() )
print ('Unique Cities' , frame["City"].unique() )

#duplicated values
duplicated_name = frame.duplicated(subset=['Name'], keep=False)
print (duplicated_name)
duplicated_name = frame.duplicated(subset=['Name'], keep='first')
print (duplicated_name)
duplicated_name = frame.duplicated(subset=['Name'], keep='last')
print (duplicated_name)

#Drop duplicated rows based on a column's value
duplicated_titles = frame.duplicated(subset=['Name'], keep=False)   # could be first, last or false
#(keeps the first row where there are duplicates, the last or none), 
print ( duplicated_titles )
 
# tilde is used to to dataframe subraction!
df2 = frame[~duplicated_titles]  # without the duplicated titles : drops the tru
print(df2)



#filtering
df2 = frame [frame['Salary'] < 7000] 
print('\nSalary < 7000 \n', df2.loc[:,['Name','Salary']])

df2 = frame[frame['Salary'] < 7000].head(2)
print('\nSalary < 7000 \n', df2.loc[:,['Name','Salary']])

df2 = frame[frame['Salary'] < 7000].tail(2)
print('\nSalary < 7000 \n', df2.loc[:,['Name','Salary']])

df2 = frame[frame['Salary'] < 7000].sample(frac=.5)
print('\nSalary < 7000 \n', df2.loc[:,['Name','Salary']])

df2 = frame[  (frame['Salary'] > 7000) & (frame['Salary'] < 10000)  ] 
print("\nSalaries between 7k and 10k \n", df2.loc[:,['Name','Salary']])
# like : you have to use containsm startswith or endswith
#df.col_name.str.startswith('abc'), column_name.str.contains("abc")
#Query 
df4 = frame.query('Age>50 or Salary<7000')
print ( df4 )

df4 = frame.query('Age == 50')
print ( df4 )

df4 = frame.query('Name == "Emily"')
print ( df4 )

df4 = frame.query('City == "California"')
print ( df4 )

dfSorted = frame.sort_index(axis=1)
print ('df sorted on 0 index, i.e. by COLUMN\n', dfSorted)

dfSorted = frame.sort_index(axis=0)
print ('df sorted on 0 index, i.e. by ROW\n', dfSorted)

 
# select rows whose name begins with the letter 'A'
print (frame[frame.apply(lambda row: row['Name'].startswith('A'),axis=1)])
print (frame[frame.apply(lambda row: row['Name'].endswith('y'),axis=1)])

#frame.query('Name.str.contains("abc")', engine='python')

a = frame['Name']  # change the column into a seriers and then use the series string functions

a = list(frame['Name'])

for value in a:
    print ( value)

#Verify that the dataframe includes specific values
#Permalink
#This is done using the .isin() method, which returns a boolean dataframe to 
#indicate where the passed values match.
# if the method is passed a simple list, it matches
# those values anywhere in the dataframe 
#print ("is in california------------------")
#print (g1.isin(['California']))
#print ("name starts with A------------------") 























