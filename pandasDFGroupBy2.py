# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:08:15 2019

@author: u
"""

import pandas as pd
import numpy as np

df = pd.read_excel('MLBPlayerSalaries.xlsx')
df = pd.read_csv('MBPlayerSalaries200Sample2.csv')
 
print ('msg 1')
print('1,1',df.iloc[1,1])
print ('msg 2')
print('0:1,0:1\n',df.iloc[0:1,0:5])
print ( df.head())
print ( df.columns )
#Index(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1', 'Year', 'Player',
#       'Salary', 'Position', 'Team'],

 
g1 = df.groupby(["Player"]).size().reset_index(name='Number per player')
print (g1)

g1 = df.groupby(["Team"]).size().reset_index(name='Number per team')
print (g1)

g1 = df.groupby(["Year"]).size().reset_index(name='Number per year')
print (g1)


print ( '-- g1 = df.groupby(["Year"]).sum()  --' )  # sums all the number columns
g1 = df.groupby(["Year"]).sum() 
print (g1)


grouped = ( df.groupby(['Year']).agg({ "Salary":np.sum} ) )  # sums specified number columns
print(grouped)
g1 = df.groupby(['Year']).agg({ "Salary":np.mean} )
print (g1)

