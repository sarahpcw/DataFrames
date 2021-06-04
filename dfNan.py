# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:12:47 2021

@author: u
"""


import pandas as pd
import numpy as np
frame = pd.DataFrame({'Name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                                'City': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
                                'Salary': [2000, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
                                'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
                                'Age':[21,21,31,24,35,46,27,38,49,50]
})


# drop rows by index
frame = frame.drop([0, 1])
print (frame)

frame = frame.drop(index = 9)
print (frame)

# nans  Detecting Nan Examples
# detecting missing values:
print(frame['Job Title'])
print(frame['Job Title'].isnull())    #prints col 1 - suppresses values gives false for a value and true for a Nan
print(frame.isnull()) 	       #prints all - suppresses values gives false for a value and true for a Nan

#isna
print('isna')
print(frame.isna()) #Indicate missing values.
#nonta
print('not na')
print(frame.notna())  #Indicate existing (non-missing) values. (reverse of the above)
#fillna
print('fill na')
print( frame.fillna(5) ) #Replace missing values.


#dropna
print('drop the missing values')
print (frame.dropna()) #Drop missing values.

df = pd.DataFrame(  {"name": ['Alfred', 'Batman'        , 'Catwoman'],
                      "toy": [np.nan,   'Batmobile'     , 'Bullwhip'],
                     "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT]})

frame = pd.DataFrame({'Name': [ np.nan, np.nan,  np.nan,'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                                'City': [ np.nan,  np.nan, 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
                                'Salary': [ np.nan, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
                                'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
                                'Age':[21,21,31,24,35,46,27,38,49,50]
})
print(frame)


print ('rows with nan  are dropped ' )
print ( frame.dropna()  )  #Drop the rows where at least one element is missing.

print ('columns with nan  are dropped ' )
print ( frame.dropna(axis='columns') )   #Drop the columns where at least one element is missing.

print ('only rows with ALL nans  are dropped ' )
print ( frame.dropna(how='all')   ) # Drop the rows where all elements are missing.

print ('keep rows with thresh non-nans. rows with thresh is the number of Non-Nans that I am looking for ' )
print (  frame.dropna(thresh=4)  )   #Keep only the rows with at least 2 non-NA values.
#
print  ('drop rows if there is a non in Salary or Job Title' )
print (  frame.dropna(subset=['Salary', 'Job Title'])  ) # Define in which columns to look for missing values.
#
 



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



#String Functions
import pandas as pd

frame = pd.DataFrame({'Name': [ np.nan, np.nan,  np.nan,' James Brown', ' Emily Black', 'Michael Green', 'Matthew Pink', 'Laura Mustard', 'Kevin White', 'Jonas Scarlet'],
                                'City': [ np.nan,  np.nan, 'Californya', 'Calyfornia', 'Califournia', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
                                'Salary': [ np.nan, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
                                'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
                                'Age':[21,21,31,24,35,46,27,38,49,50]
})
print(frame)
 
print ( 'count of a in every name')
print (frame['Name'].str.count('a'))# print the count of a in every name
print ( 'replace j with $')
print ( frame['Name'].str.replace('J','$') )
print ( 'replace y with i')
print ( frame['City'].str.replace('y','i') )
print ( 'replace ou with o')
print ( frame['City'].str.replace('ou','o') )
print ( frame['City'].str.contains('Los') ) # returns a  true /false
print ( len(frame['City']))
print ( frame['City'].str.upper() )
print ( frame['City'].str.lower() )

# concatenates the whole column into one string
print (frame['City'].str.cat(sep=';' )) 
#Californya;Calyfornia;Califournia;Los Angeles;Los Angeles;Georgia;Georgia;Los Angeles


print ("After Stripping:")
f1 = (frame['Name'].str.strip()) # removes training and leading spaces
f1 = f1.str.split(' ')
f2 = f1.str.slice(0,1)
print (f2)



"""
Sr.No	Function & Description
1	lower()   Converts strings in the Series/Index to lower case.
2	upper()   Converts strings in the Series/Index to upper case.
3	len()   Computes String length().
4	strip()   Helps strip whitespace(including newline) from each string in the Series/index from both the sides.
5	split(' ')  Splits each string with the given pattern.
6	cat(sep=' ')  Concatenates the series/index elements with given separator.
8	contains(pattern)   Returns a Boolean value True for each element if the substring contains in the element, else False.
9	replace(a,b)   Replaces the value a with the value b.
10	repeat(value)   Repeats each element with specified number of times.
11	count(pattern)   Returns count of appearance of pattern in each element.
12	startswith(pattern)   Returns true if the element in the Series/Index starts with the pattern.
13	endswith(pattern)   Returns true if the element in the Series/Index ends with the pattern.
14	find(pattern)   Returns the first position of the first occurrence of the pattern.
15	findall(pattern)   Returns a list of all occurrence of the pattern.
16	Swapcase   Swaps the case lower/upper.
17	islower()   Checks whether all characters in each string in the Series/Index in lower case or not. Returns Boolean
18	isupper()   Checks whether all characters in each string in the Series/Index in upper case or not. Returns Boolean.
19	isnumeric()   Checks whether all characters in each string in the Series/Index are numeric. Returns Boolean.
"""























