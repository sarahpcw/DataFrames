# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:12:39 2019

@author: u
"""

import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
print("Original DataFrame")
print(df)
df =  df.fillna(0)
print("\nNew DataFrame replacing all NaN with 0:")
print(df)

#Drop duplicated rows based on a column's value
#Permalink
#For example, say you have a movies dataframe with "title" and "synopsis" columns and
# you want to drop all movies with duplicate titles:
duplicated_titles = df.duplicated(subset=['name'], keep=False)
print("\nilde is used to to dataframe subraction!")
# tilde is used to to dataframe subraction!
df2 = df[~duplicated_titles]
print (df2)  # both anastasia's are gone