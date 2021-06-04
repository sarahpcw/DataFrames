#TradeClients.xlsx
#C:\Users\u\Documents\My Tableau Repository\Datasources\
# create all variables

import openpyxl
wb = openpyxl.load_workbook('C:\\Users\\u\\Documents\\My Tableau Repository\\Datasources\\TradeClients.xlsx')
ws = wb['Clients']
data_rows = []
#for row in ws['A1':'T1000']:
count_row_ss=0
for row in ws:
    count_row_ss = count_row_ss + 1
    data_cols = []
    for cell in row:
        data_cols.append(cell.value)
    if 'Wholesaler' in data_cols:
        data_rows.append(data_cols)
    
print (data_rows[0:5])    
count = 0
for row in data_rows:
    count = count + 1
    print(row[0:3])
    
print ('Count of Wholesalers', count)
print ('Count of Wholesalers', len(data_rows))
print ('Row Count in Spreadsheet', count_row_ss)
print ('Number of columns', len(data_cols))

ws = wb['Products']
data_rows = []
count_row_ss=0
for row in ws:
    count_row_ss = count_row_ss + 1
    data_cols = []
    for cell in row:
        data_cols.append(cell.value)
    data_rows.append(data_cols)
print (data_rows[0:5])    
count = 0
for row in data_rows:
    count = count + 1
    print(row[0:3])
print ('Count of products', count)
print ('Count of products', len(data_rows))
print ('Row Count in Spreadsheet', count_row_ss)
print ('Number of columns', len(data_cols))
print (type(ws))

ws = wb['Sheet1']
data_rows = []
count_row_ss=0
for row in ws:
    count_row_ss = count_row_ss + 1
    data_cols = []
    for cell in row:
        data_cols.append(cell.value)
    data_rows.append(data_cols)
print (data_rows[0:5])    
count = 0
for row in data_rows:
    count = count + 1
    print(row[0:])
print ('Count of products', count)
print ('Count of products', len(data_rows))
print ('Row Count in Spreadsheet', count_row_ss)
print ('Number of columns', len(data_cols))
print (type(ws))