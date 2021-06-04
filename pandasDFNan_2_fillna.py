import pandas as pd
import numpy as np

df = pd.DataFrame(  {"name": ['Alfred', 'Batman'        , 'Catwoman'],
                      "toy": [np.nan,   'Batmobile'     , 'Bullwhip'],
                     "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT]})

print ('rows with nan  are dropped ' )
print ( df.dropna()  )  #Drop the rows where at least one element is missing.

print ('columns with nan  are dropped ' )
print ( df.dropna(axis='columns') )   #Drop the columns where at least one element is missing.

print ('only rows with ALL nans  are dropped ' )
print ( df.dropna(how='all')   ) # Drop the rows where all elements are missing.

print ('keep rows with thresh non-nans. rows with thresh is the number of Non-Nans that I am looking for ' )
print (  df.dropna(thresh=2)  )   #Keep only the rows with at least 2 non-NA values.
#
print  ('drop rows if there is a nan in name or born' )
print (  df.dropna(subset=['name', 'born'])  ) # Define in which columns to look for missing values.
#
print  ('rows with nan  are dropped ' )
print  ( df.dropna(inplace=True) ) # Keep the DataFrame with valid entries in the same variable.
 
print('fill na')
print( df.fillna(5) ) #Replace missing values.

print('fill na')
print( df.fillna('Rubbish') )  #Replace missing values.
