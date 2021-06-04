
import pandas as pd
import numpy as np
df = pd._________(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])


# Use `.index`
df['D'] = df.index

# Print `df`
print(df)

## Check out the weird index of your dataframe
#print(df)
#
## Use `reset_index()` to reset the values. 
#df_reset = df.__________(level=0, drop=True)
#
## Print `df_reset`
#print(df_reset)