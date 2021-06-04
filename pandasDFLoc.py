import pandas as pd
import numpy as np

rowIndexes = pd.date_range('20170101',periods=4) #generates 4 dates
colHeadings= list('XYZW')
numbers = np.random.randn(4,4)  # 4x4 grid of random numbers
print (numbers)

df = pd.DataFrame(numbers, index=rowIndexes, columns=colHeadings)
print (df)

#Using loc
print (df.loc['2017-01-02','X'],df.loc['2017-01-02','Y'],df.loc['2017-01-02','W'])
print ('Max',np.max(rowIndexes))
maxD = np.max(rowIndexes)
print ('Max Date col X', df.loc[maxD,'X'])
print ('Max Date col X', df.loc[maxD,'X':'Z'])
print ('Max Date all Cols', df.loc[maxD,:])
print ('Max Date all Cols', df.loc[maxD])

minD = np.min(rowIndexes)
print (df.loc[minD,'X'])
print (df.loc[minD,:])   #row for minimdate date, all the columns
print (df.loc[minD:maxD,'X'])   #row all the dates, only col X
print (df.loc[:,'X'])
print (df.loc[:,:])

#Using iloc
m = 0
n = 3
print(df.iloc[1,1])
print(df.iloc[:,:])
print(df.iloc[0:1,0:1])
print(df.iloc[m:n,:])



