import pandas as pd
import numpy as np

mydict = {
'Name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'City': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
'Salary': [2000, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
'Age':[21,21,31,24,35,46,27,38,49,50]
}
frame = pd.DataFrame(mydict)
 
#create a excel file from the dataframe
myfile = open('C:\\Users\\u\\.spyder-py3\\Stu_LondonFeb25\\anastasia.csv','w' )
myfile.close()

frame.to_excel('C:\\Users\\u\\.spyder-py3\\3W-Webinar\\anastasia.xlsx')
#read the excel file , it returns a dataframe
excel_dataframe = pd.read_excel('C:\\Users\\u\\.spyder-py3\\3W-Webinar\\anastasia.xlsx')  # it does not create the extra column on the left 

##inspect the dataframe
print (excel_dataframe)
print ('Shape\n', excel_dataframe.shape) #shape
print ('Column Names: \n', excel_dataframe.columns)
print ('Indexes: \n', excel_dataframe.index.values)

print ( frame.loc[:,['Name','City']])

mylist = ['Name','City']
print ( frame.loc[:,mylist])

excel_dataframe.to_csv('anastasia.csv')
csv_dataframe = pd.read_csv('anastasia.csv')  # it creates an extra column on the left, which is like an index
frame.to_excel('C:\\Users\\u\\.spyder-py3\\3W-Webinar\\anastasia.xlsx')

##inspect the dataframe
#print (csv_dataframe)
#print ('Shape\n', csv_dataframe.shape) #shape
#print ('Column Names: \n', csv_dataframe.columns)
#print ('Indexes: \n', csv_dataframe.index.values)