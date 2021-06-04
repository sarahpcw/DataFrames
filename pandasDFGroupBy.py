# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:05:30 2019

"""
## dups
"""

import pandas as pd
import numpy as np
df1 = pd.DataFrame({'name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
print (df1)
g1 = df1.groupby(["city"]).size().reset_index(name='Number of people')
print(g1)

#Drop duplicated rows based on a column's value
#Permalink
#For example, say you have a movies dataframe with "title" and "synopsis" 
#columns and you want to drop all movies with duplicate titles:
duplicated_titles = df1.duplicated(subset=['name'], keep=False)

# tilde is used to to dataframe subraction!
df2 = df1[~duplicated_titles]
print(df2)
@author: u
"""
import pandas as pd
import numpy as np

mydict = {'name': ['Anastasia',  'Katherine', 'James','Anastasia',  'Katherine', 'James'],
'city': ['California', 'Los Angeles', 'California','California', 'Los Angeles', 'California'], 
'salary':[10,20,30,40,50,60]}

df4 = pd.DataFrame(mydict)
print ("1------------------")
print (df4)

print ("add all salaries------------------")
# add all the salaries
g1 = df4.groupby(["city"]).size().reset_index(name='Number of people')
print(g1)
print ("add all salaries------------------")
df3 =df4.groupby(["city",'name']).size().reset_index(name='Number of people')
print (df3)
print ("add all salaries------------------")
grouped = df4.groupby(df3.name).agg({
    "salary":np.sum
})
print(grouped)

#Verify that the dataframe includes specific values
#Permalink
#This is done using the .isin() method, which returns a boolean dataframe to 
#indicate where the passed values match.
# if the method is passed a simple list, it matches
# those values anywhere in the dataframe 
print ("is in california------------------")
print (g1.isin(['California']))
print ("name starts with A------------------")
# select rows whose name begins with the letter 'A'
print (df4[df4.apply(lambda row: row['name'].startswith('A'),axis=1)])
#Create from list of dicts
#Permalink
#A record is a dict with column names as keys
#Another way to create a dataframe is by using a list of dicts with column names as keys, using from_records().
new_df = pd.DataFrame(columns=['id','name'])

data_dict = [
    {'id':1,'name':"john"},
    {'id':2,'name':"mary"},
    {'id':3,'name':"peter"}
]

# must reassign since the append method does not work in place
new_df = new_df.from_records(data_dict)
print (new_df)

for index,row in df1.iterrows():
    print("{0} has name: {1}".format(index,row["name"]))

