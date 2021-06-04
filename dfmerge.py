# -*- coding: utf-8 -*-
"""
Merge: Combining 2 dataframes using the values in the first columns, like a cartesian product
Zip: John and London etc
Map: 
Concat
Append
"""
import pandas as pd
#zip combines 2 lists or tuples in a mapped order
a = ("John", "Charles", "Mike")
b = ("London", "Bristol", "Leads")
x = zip(a, b)
print ( x)
for i,j in x:
    print (i,j)


import pandas as pd
df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})

print (df1)
print(df2)
#df1
#    lkey value
#0   foo      1
#1   bar      2
#2   baz      3
#3   foo      5
#df2
#    rkey value
#0   foo      5
#1   bar      6
#2   baz      7
#3   foo      8
#Merge df1 and df2 on the lkey and rkey columns. 
#The value columns have the default suffixes, _x and _y, appended.


df1.merge(df2, left_on='lkey', right_on='rkey')

#  lkey  value_x rkey  value_y
#0  foo        1  foo        5
#1  foo        1  foo        8
#2  foo        5  foo        5
#3  foo        5  foo        8
#4  bar        2  bar        6
#5  baz        3  baz        7


import pandas as pd
import numpy as np

# almost like joining on the 1 2 3 
print ('3 ========== s  >>> ')
s = pd.Series([1,2,3], index=['one','two','three'])
print(s)
print ('3 ========== t  >>> ')
t = pd.Series(['map1','map2','map3'], index=[1,2,3])
print (t)
print ('3 ========== s map t >>> ')
print(s.map(t))

    #3 ========== s  >>> 
    #one      1
    #two      2
    #three    3
    #dtype: int64
    #3 ========== t  >>> 
    #1    map1
    #2    map2
    #3    map3
    #dtype: object
    #3 ========== s map t >>> 
    #one      map1
    #two      map2
    #three    map3
    
    
print('__________________')
s=pd.Series([1,2,3,np.nan])
print(s)

t1=s.map('this is a test string {}'.format,na_action=None) #maps as normal
print(t1)

t2=s.map('this is a test string {}'.format,na_action='ignore') #ignores this valie if the other in a nan
print(t2)










import pandas as pd
#import numpy as np
df1 = pd.DataFrame(
        {
          'Red Sox':['A0','A1','A2'],
          'Kaizer Chiefs':['B0','B1','B2'],
          'Man u':['C0','C1','C2']                
                }, index=[0,1,2])

df2 = pd.DataFrame(
        {
          'Red Sox':['A3','A4','A5'],
          'Kaizer Chiefs':['B3','B4','B5'],
          'Man u':['C3','C4','C5'],
          'Arsenal':['D3','D4','D5']                
                }, index=[3,4,5])

df3 = pd.DataFrame(
        {
          'Red Sox':['A6','A7','A8'],
          'Kaizer Chiefs':['B6','B7','B8'],
          'Man u':['C6','C7','C8'],
          'Arsenal':['D6','D7','D8']                
                }, index=[6,7,8])

frames = [df1,df2,df3]
print(frames)
result = pd.concat(frames)
print(result)



#append  dataframes
print (df1.append(df2))  
 







