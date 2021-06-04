import pandas
wb = pandas.read_excel('C:\\Users\\u\\Documents\\My Tableau Repository\\Datasources\\TradeClients.xlsx', sheet_name='Products')
##inspect the dataframe
#print (wb)
print ('Shape\n', wb.shape) #shape
print ('Column Names: \n', wb.columns)
print ('Indexes-------------: \n', wb.index.values)
print ('Max',(wb.index.values.max()))  #largest index value
print ('Min',(wb.index.values.min()))  #largest index value

print ('Unique names------' )
#print ( wb["product size"].unique() )
unames = wb["product size"].unique()
for each in unames:
    print (each)
unames = wb["Product"].unique()
for each in unames:
    print (each)

print ('Statistics ------' )
print ('Maximum Unit Price: ', wb['Unit Price'].max())
print ('Minimum Unit Price: ', wb['Unit Price'].min())
print ('Average Unit Price: ', wb['Unit Price'].mean())
print ('Sum of Unit Price : ', wb['Unit Price'].sum()) 

print ('Group by product ------' )
print ( wb.groupby(["Product"]).size() )
print ('Sum the Group by product ------' )
print ( wb.groupby(["Product"]).mean() )

print ('Group by unit product size ------' )
print ( wb.groupby(["product size"]).size() )
print ('Average the Group by product size------' )
print ( wb.groupby(["product size"]).mean() )

df4 = wb.query('Product == "TAB"  ')
print ( df4 )

print ('Sum of Unit Price : ', df4['Unit Price'].sum())  
print ('Ranking the Unit Price\n', wb['product size'].rank())

csv_dataframe = pd.read_csv('C:\\Users\\u\\Documents\\My Tableau Repository\\Datasources\\TradeClients.csv')  # it creates an extra column on the left, which is like an index
print ('Shape\n', csv_dataframe.shape) #shape
print ('Column Names: \n', csv_dataframe.columns)