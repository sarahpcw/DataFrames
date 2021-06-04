import pandas as pd
import numpy as np
#getting information about a dataframe

df = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns = ['one','two','three'])
print(df)
df=df.reindex(['a','b','c','d','e']) 
print(df)  


dfSorted = df.sort_index(axis=0)
print ('df sorted on 0 index, i.e. by rows')
minIndex = (dfSorted.head(1).index)
print (minIndex[0])   # smallest row index value 
print (dfSorted.tail(1).index) # largest  row index value 

print ('Max',np.max(df.index.values))
print ('min',np.min(df.index.values))
print ('col', df.columns)

rowOne = df.loc[:,'one']
print('max rowONe', np.max(rowOne))

print('max rowONe', np.max(df.loc[:,'one'] ))
maxValue = np.max(df.loc[:,'one'] )

print ('col', df.columns)
cols = df.columns[2]
for i, val in enumerate ( (df.columns) ): 
     print ( 'max values' , i , val, np.max(df.loc[:,val] ) )
     print ( 'min values' , i , val, np.min(df.loc[:,val] ) )
     
for val in  ( (df.columns) ): 
     print ( np.max(df.loc[:,val] ) )