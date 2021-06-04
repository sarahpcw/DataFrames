# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:21:41 2019

@author: u
"""
import pandas as pd
import numpy as np

df = pd.read_excel('MLBPlayerSalaries.xlsx')
print (df.head(5))
print ('msg 1')

print('1,1',df.iloc[1,1])
print ('msg 2')
print('0:1,0:1\n',df.iloc[0:1,0:5])

#In the most cases we want to take random samples of more rows than one. 
#Thus, in the next Pandas sample example we are going to take random sample of the size of 200.
# We are going to use the parameter n to accomplish this:
print ('msg 3')
print (df.sample(n=200).head(10))


 
#Random Sampling Rows using NumPy Choice
#It’s of course very easy and convenient to use Pandas sample method to take a random sample of rows. 
#Note, however, that it’s possible to use NumPy and random.choice. 
#In the example below we will get the same result as above by using np.random.choice.
#As usual when working with Python modules, we start by importing NumPy. 
#After this is done we will the continue to create an array of indices (rows) and then 
#use Pandas loc method to select the rows based on the random indices:
#import numpy as np

rows = np.random.choice(df.index.values, 200)
print ('msg 4')
print (df.index.values)
df200 = df.loc[rows]
df200.head()

grouped = df.groupby('Player')
print( grouped.apply(lambda x: x.sample(n=2, replace=True)).head())
g1 = df.groupby(["Player"]).size().reset_index(name='Number of games')

#The code above may need some clarification. In the second line, 
#we used Pandas apply method and the anonymous Python function lambda.
# What it will do is run sample on each subset (i.e., for each Player) and take 2 random rows. 
#Note, here we have to use replace=True or else it won’t work.
print ('msg 5')
#df.sample(200, random_state=1111).to_csv('MBPlayerSalaries200Sample2.csv')

df2 = (df[df['Salary'] < 421000].sample(frac=.1).head())
print('0:1,0:1\n',df2.iloc[0:1,0:4])

df3 = df[(df['Salary'] < 421000) & (df['Year'] < 2000)].sample(frac=.1).head()
print('0:1,0:1\n',df3.iloc[0:1,0:4])


#Using Pandas Sample and Remove
#We may want to take a random sample from our dataframe and remove those rows. 
#Maybe we want to create two different dataframes; one with 80% of the rows and one with the 
#remaining 20%. Both of these things can, of course, be done using sample and the drop method. 
#In the code example below we create two new dataframes;
# one with 80% of the rows and one with the remaining 20%.
df1 = df.sample(frac=0.8, random_state=138)
df2 = df.drop(df1.index)
#If we merely want to remove random rows we can use drop and the inplace parameter:
df.drop(df1.index, inplace=True)
df.shape
#Same as: 
df.drop(df.sample(frac=0.8, random_state=138).index, inplace=True)
# Output: (3909, 5)




print (df.index.values)
print ('Row index 58', df.loc[58,'Year'])
print ('Row index 58\n', df.loc[58,'Year':'Salary'])


for index,row in df.iterrows():
    print("{0} has name: {1}".format(index,row["Player"]))
    print ( index, row )
    
