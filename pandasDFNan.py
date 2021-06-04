import pandas as pd
import numpy as np
mydict = {'name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']}

df1 = pd.DataFrame(mydict)
print (df1)
#List unique values in the df['name'] column
print (df1.name.unique())
