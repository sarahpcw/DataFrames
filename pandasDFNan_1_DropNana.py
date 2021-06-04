import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns = ['one','two','three'])
df=df.reindex(['a','b','c','d','e']) 
print(df)
print (df.isnull())

print('isna')
print (df.isna()) #Indicate missing values.

print('not na')
print (df.notna())  #Indicate existing (non-missing) values. (reverse of the above)

print('fill na')
print( df.fillna(5) ) #Replace missing values with 5

print('fill na')
print( df.fillna('Rubbish') )  #Replace missing values with Rubbish

print('drop the missing values')
print (df.dropna()) #Drop missing values.

print('drop row if the index in nan')
df=df.reindex(['a','b','c',np.NAN,'e']) 
print (df)
print ( df.index.dropna() ) #Drop missing indices. you will again have to reindex the frame