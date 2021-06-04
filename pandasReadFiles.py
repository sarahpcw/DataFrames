import pandas as pd
import numpy as np

playersDF = pd.read_excel('C:\\Users\\u\\.spyder-py3\\DataD1\\Data TradeClients.xlsx')
#playersDF.sample(200).to_csv('MBPlayerSalaries200Sample22.csv')  ### outputs a csv file
# Data TradeClients.xlsx
# \MLBPlayerSalaries.xlsx
print ('msg 4 Sample 10    ================ > ')
print (playersDF.sample(10))


print ('msg 1 INdex Values ================ > ') 
print (playersDF.index.values)
print (playersDF.columns.values)
print (playersDF.iloc[0:2,:])
print ('number of rows', len(playersDF.index))
print ( playersDF.iloc[:,:].count() ) ## count rows of every solumn
count_row = playersDF.shape[0]  # gives number of row count
print ( count_row)

r, c = playersDF.shape
total_rows=len(playersDF.axes[0])
total_cols=len(playersDF.axes[1])
print ( r , c , total_rows , total_cols )

count = 0
for row in playersDF.iterrows():  # returns every row as a tuple with 2 elements , a rownumber and the row as a series
    print(row)
#    print ( '---', len(row),  type(row[1]),  row[1] )  # row 1 is a series
#    print ( '---', row[1]['Player'] , row[1]['Salary'] )
##    print (b)
    count += 1
    if count > 10:
        break
    
    
print ('msg 2 get the column headings ============ > ')
print ('msg 3 row 1 all columns =========== > ' ,playersDF.iloc[0:1,0:])
print ('0:1,0:1\n',playersDF.iloc[0:1,0:4])
count_col = playersDF.shape[1]  # gives number of col count
print ( count_col)
#for in in range in playersDF:
#    print (row)


df = pd.read_csv('C:\\Users\\u\\.spyder-py3\\DataD1\\MBPlayerSalaries200Sample2.csv')
#print ('msg 1 ') 
#print (df.index.values)
#print ('msg 2')
#print('0:1,0:1\n',df.iloc[0:1,0:4])
#print ('msg 3')
#print('0:1,0:1\n',df.iloc[0:1,3:])

##     			     True 
#
#df1 = pd.DataFrame(
#        {'name': ['Anastasia', np.nan, np.nan ],
#         'city': ['California', 'Los Angeles', np.nan]
#         })
# 
#print (df1)

print ( 'description ')
x = playersDF.describe() 
print (x)