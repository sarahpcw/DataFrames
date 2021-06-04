# -*- coding: utf-8 -*-
"""
Baseball players - total summ of salary 
and average salary per team
"""
import pandas as pd
import numpy as np

mydict = {
'Name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'City': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
'Salary': [2000, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000],
'Year': [2020, 2019, 2018,2020, 2019, 2018,2020, 2019, 2018,2020],
'newCol':[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],
'Job Title':['Manager','Director','Sales Person','Manager','Director', np.nan,np.nan,np.nan,np.nan,np.nan],
'Age':[21,21,31,21,31,46,21,38,49,31]
}

frame = pd.DataFrame(mydict)
print ( frame)



# = (a1-c1)/d1