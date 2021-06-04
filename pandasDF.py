import pandas as pd
import numpy as np
 
 
s = pd.Series([0,1,2,3,4,5]) 
print(s)

#reshape  arrays
x = np.arange(0,20,1)
print(x)
x = np.arange(20).reshape(4,5)				#numbers 0  to 19 in 4 rows and 5 cols
print(x)
rowIndexes = pd.date_range('20170101',periods=4)
print ( rowIndexes)  #generates 4 dates




colHeadings= list('XYZW')
numbers = np.random.randn(4,4)  # 4x4 grid of random numbers
print (numbers)

df = pd.DataFrame(numbers, index=rowIndexes, columns=colHeadings)
print (df)


df['J'] = df['X'].apply(lambda x: 999 if x > 0 else 888)
#df['new column name'] = df['column name'].apply(lambda x: 'true value' if x  condition else 'false value')

dfSorted = df.sort_index(axis=0)
print ('df sorted on 0 index, i.e. by rows')
print (dfSorted)

dfSorted = df.sort_index(axis=1)
print ('df sorted on 1 index, i.e. by columns')
print (dfSorted)


