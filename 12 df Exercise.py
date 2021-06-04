"""
Trade clients
-------------
# what is the largest index value
# how many columns are in the dataframe
# what are the column names

how many rows has one nan column
how many rows has two nan column
how many rows has 3  nan column
drop where thhe row has 3 nan columns

# what is the average company size  ??? no such column
# what is the sum of the registration fees
# what is the max registration fee paid
# what is the most recent registration date
# what are the unique values in the area column
# what are the unique values in the type column
# what are the unique values in the company column
# how many companies are in the area London
# how many companies are not in the area london
# print the all the rows and the Company and Area columns
# what is the average, sum, min and max values in the company registration fee column
#Index(['ID', 'Type', 'Company Size', 'Company Registration Date',
#       'Company TurnOver', 'Company', 'Address1', 'Address2', 'Address3',
#       'Address4', 'Postcode', 'Area', 'Title', 'First Name', 'Surname',
#       'Position', 'Telephone', 'Fax', 'Mobile', 'Email'],
#      dtype='object')


encoding example:
with open("df_info.txt", "w",
          encoding="utf-8") as f: 
    
@@@@@@@
read all three spreadsheets 
create a frame ffrom the df for every area, save each to a sheet in a new excel file

"""
import pandas as pd
import numpy as np
frame = pd.read_csv('C:\\Users\\u\\.spyder-py3\\ManchesterFeb\\TradeClients.csv',encoding="ISO-8859-1")  # it does not create the extra column on the left 

frame.to_csv('C:\\Users\\u\\.spyder-py3\\3W-Webinar\\TC.csv')

# how many row and columns
print (frame.shape)
print (frame.iloc[0:1,:])
frame = frame.drop([0])  # drop row with the index of 0

frame.to_excel('C:\\Users\\u\\.spyder-py3\\3W-Webinar\\TC.xlsx')
#read the excel file , it returns a dataframe
frame = pd.read_excel('C:\\Users\\u\\.spyder-py3\\3W-Webinar\\TC.xlsx')  # it does not create the extra column on the left 
print (frame.shape)

# how many row and columsn
print (frame.shape)
print (frame.dtypes)
# what is the largest index value
print ('Max',(frame.index.values.max()))  #largest index value

# how many columns
print ('col', len( frame.columns))

# what are the column names
print ( frame.columns)
# what is the average company size
print(frame.fillna(0) ) #Replace missing values.
print ('Company Size: ', frame['Company Size'].mean())

# what is the sum of the Company Turover
print ('Company TurnOver: ', frame['Company TurnOver'].sum())

# what is the sum of the max Company Turover
print ('Max Company TurnOver: ', frame['Company TurnOver'].max())

# what is the most recent registration date
print ('Max Company Registration Date: ', frame['Company Registration Date'].max())
###### !!!!!! convert julian date to datetime()

# what are the unique values in the area column
print ('Unique Area' , frame["Area"].unique() )

# what are the unique values in the type column
print ('Unique Type' , frame["Type"].unique() )

# what are the unique values in the company column
print ('Unique Company' , frame["Company"].unique() )

# how may companies are in the area London
print ('Unique Companies in Frame' , len (frame["Company"].unique() ))
allcompanies = len (frame["Company"].unique() )
df4 = frame.query('Area == "London"')
print ('Unique Companies in the London Only Area' , len(df4["Company"].unique()) )
londoncompanies = len(df4["Company"].unique()) 
print ( 'Unique Companies not in London ' , allcompanies - londoncompanies)

g1 = df4.groupby(["Area"]).size().reset_index(name='Number of people in London')
print (g1)


# print the all the rows and the Company and Area columns
print(frame.loc[:,['Company','Area']])
# what is the average, sum, min and max values in the Company TurnOver column
print ( frame['Company TurnOver'].max() ) 
print ( frame['Company TurnOver'].min() )
print ( frame['Company TurnOver'].sum() )
print ( frame['Company TurnOver'].mean())


#how many rows has one nan column
print (frame.shape)
thres = frame.shape[1] - 3
print (  frame.dropna(thresh=thres).shape[0]  )   #Keep only the rows with at least 2 non-NA values.

print (  frame.dropna(thresh=thres).iloc[0:10,19:]  )

#how many rows has two nan column
#how many rows has 3  nan column
#drop where thhe row has 3 nan columns

print ('rows with nan  are dropped ' )
print ( frame.dropna()  )  #Drop the rows where at least one element is missing.

print ('columns with nan  are dropped ' )
print ( frame.dropna(axis='columns') )   #Drop the columns where at least one element is missing.

print ('only rows with ALL nans  are dropped ' )
print ( frame.dropna(how='all')   ) # Drop the rows where all elements are missing.

print ('keep rows with thresh non-nans. rows with thresh is the number of Non-Nans that I am looking for ' )
print (  frame.dropna(thresh=4)  )   #Keep only the rows with at least 2 non-NA values.
#
print  ('drop rows if there is a non in Salary or Job Title' )
print (  frame.dropna(subset=['Salary', 'Job Title'])  ) # Define in which columns to look for missing values.
#
 




