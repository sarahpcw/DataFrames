#Dataframes and Files
#excel file to data frames: pd.read_excel
import pandas as pd
import numpy as np
import openpyxl


wb = openpyxl.load_workbook('C:\\Users\\u\\Documents\\ForFlashDrive\\DB All PCW\\Surjit PPH.xlsx')
ws = wb['Sheet1']
data_rows = []
for row in ws['A3':'D20']:
    data_cols = []
    for cell in row:
            data_cols.append(cell.value)
    data_rows.append(data_cols)
    
    
for each in data_rows: 
    if type(each[0]) != int and  '@' in each[0]:
        print ( each[0])
        
    
df = pd.read_csv('C:\\Users\\u\\.spyder-py3\\3W-Webinar\\MBPlayerSalaries200Sample22.csv')

df.to_excel('C:\\Users\\u\\.spyder-py3\\3W-Webinar\\MBPlayerSalaries200Sample22.xlsx')
df = pd.read_excel('C:\\Users\\u\\.spyder-py3\\3W-Webinar\\MLBPlayerSalaries.xlsx')
print(df.shape)
#df1 = pd.read_excel('MLBPlayerSalaries.xlsx')

#Write / Output to  Specific Sheet Tabs In An Excel File:
pd.read_excel('bla.xlsx',sheet_name='Sheet1')

print ('Example 2 --------------------------')
df1 = pd.read_excel('F:\\2012 London\\Courses\\PYTHON\\Data TradeClients.xlsx', sheet_name='Sheet2')
print(df1.shape)
frame = pd.read_csv('C:\\Users\\u\\.spyder-py3\\ManchesterFeb\\TradeClients.csv',encoding="ISO-8859-1")
print(frame.shape)
print ( 'Column names:      ', frame.columns.values)  # print the column names

print ( df1.iloc[0:10,0:])
print ( 'df1 shape:         ', df1.shape)
print ( 'Column names:      ', df1.columns.values)  # print the column names
print ( 'Index information: ', df1.index)    # print the index information : RangeIndex(start=0, stop=19543, step=1)
print ( '1,1',df1.iloc[1,1])
print ( 'msg 2')
print ( '0:10,0:4\n',df1.iloc[0:5,2:3])
print ( '0:10,3:\n',df1.iloc[0:5,3:])

print ('Unique names' , df1["Area"].unique() )
print ('Unique Type'  , df1["Type"].unique() )

df4 = df1.query('Area == "london" or Area == "London" ')
print ( df4 )
g1 = df4.groupby(["Area"]).sum()
print('\nSum all the number columns, by City -------------- \n',g1.loc[:,['AnnualSubScription']])

print ('Example 3 --------------------------')
workSheets = ['Sheet1', 'Sheet2',  'Sheet3']
cols = ['A:E', 'A,E', 'B,C,D']
mydict = {}
for ws, c in zip(workSheets, cols):
#    df[ws] = pd.read_excel(excelFile, sheetname=ws, parse_cols=c)
#    Below is update for Python 3.6.5 & Pandas 0.23.4:
#    mydict[ws] = pd.read_excel('C:\\Users\\u\\Documents\\ForFlashDrive\\DB All PCW\\Surjit PPH.xlsx', sheet_name=ws, usecols=c)
    mydict[ws] = pd.read_excel('F:\\2012 London\\Courses\\PYTHON\\Data TradeClients.xlsx', sheet_name=ws, usecols=c)
    a = mydict[ws]
#    print ( 'The Shape of',ws,':', a.shape, 'Columns', c)
    print (mydict[ws])
print ('done--------------------------')  
