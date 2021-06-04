"""
excel_dataframe = pd.read_excel('C:\\Users\\u\\.spyder-py3\\3W-Webinar\\anastasia.xlsx') 
"""
import pandas as pd
import numpy as np

mydict = {
'Name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'City': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
'Salary': [2000, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
'Year': [2020, 2019, 2018,2020, 2019, 2018,2020, 2019, 2018,2020],
'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
'Age':[21,21,31,21,31,46,21,38,49,31]
}

frame = pd.DataFrame(mydict)
print ( frame)

#Query 
 
dfSorted = frame.sort_index(axis=1) 
print ('df sorted on 0 index, i.e. by COLUMN\n', dfSorted)

 
dfSorted = frame.sort_index(axis=0) 
print ('df sorted on 0 index, i.e. by ROW index\n', dfSorted)

