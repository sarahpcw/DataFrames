import pandas as pd
import numpy as np
#getting information about a dataframe

df = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns = ['one','two','three'])
print(df)
df=df.reindex(['a','b','c','d','e']) 
print(df)

# refer to invidual values by index using iloc
print('1,1',df.iloc[1,1])


x = df.shape
print ('the shape is : (in rows and columns) ', x)
print ('the number of rows : ', x[0])
print ('the shape is : ', x[1])

print ('col')
print ('col', df.columns)

rows = x[0]
cols = x[1]
print ('print the top row (row 0) , all the columns')
print('0:1,0:1\n',df.iloc[0:1,0:cols])

print ('the number of values in the df : ', df.size)

print ('the row headings index.values are: ', df.index.values)

print ('the row headings are : ', df.index)

print ( np.random.choice(df.index.values, 1))  # get 1 randomg values from the row headings
print ( np.random.choice(df.index.values, 2))  # get 2 randomg values from the row headings
print ( np.random.choice(df.index.values, 3))  # get 3 randomg values from the row headings

print ('Subframe')
#get 2 random values
rows = np.random.choice(df.index.values, 1)
subFrame = df.loc[rows]  

#
for index,row in df.iterrows():
    print("{0} has name: {1}".format(index,row["one"]))
#    print ( index, row )  # rubbish , you should format
    print("{0} has name: {1} {2} {3}".format(index,row["one"],row["two"] ,row["three"] )) 
    
#
#
#sort a dataframe by columns
#dfSorted = df.sort_index(axis=1)
#print ('df sorted on 1 index, i.e. by columns')
#print (dfSorted)

#print ('2:1')
#print(df.isnull())

print (df)
df3 = df [  ( np.isnan(df['one'] ) ) ].sample(frac=1)
print('0:1,0:1\n',df3.iloc[:,:])   # print all the nan's 
df = df.drop(df3.index)
print (df)

#print (df)
#df3 = df [  ( np.isnan(df['one']) ) ].sample(frac=1)
#print('0:1,0:1\n',df3.iloc[:,:])   # print all the nan's 
#df = df.drop(df3.index)
#print (df)
# 			 
    
#print (np.nan in np.array(x) )		#     False  can't see the nan in a array
#print (np.nan in np.array(x).tolist() )	#     False can't see the nan in a list
#print ('position of the nan value', np.argwhere(np.isnan(x)))  #1 -- this method show the index of the nan
#x = [[1,np.nan],[1,np.nan]]
#print ('position of the nan value \n', np.argwhere(np.isnan(x)))  #1


