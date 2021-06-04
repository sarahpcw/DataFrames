import pandas as pd
import numpy as np

dates = pd.date_range('20170101',periods=4) 
print(dates)

s = pd.Series([1,np.nan,5,np.nan,6,8])
print (s)

s = pd.Series(np.random.randn(10))
print (s)
print (s.head(5))
print (s.tail(5))

colHeadings= list('XYZW')
numbers = np.rint(np.random.randn(4,4) ) # 4x4 grid of random numbers
print (numbers)
#MS        month start frequency
dateFrame = pd.date_range('2015-02-24', periods=4, freq='Q')
for date in dateFrame:
     print(date)
     
df = pd.DataFrame(numbers, index=dateFrame, columns=colHeadings)
print (df)

#Alias     Description
#B         business day frequency  
#C         custom business day frequency (experimental)  
#D         calendar day frequency  
#W         weekly frequency  
#M         month end frequency  
#BM        business month end frequency  
#CBM       custom business month end frequency  
#MS        month start frequency  
#BMS       business month start frequency  
#CBMS      custom business month start frequency  
#Q         quarter end frequency  
#BQ        business quarter endfrequency  
#QS        quarter start frequency  
#BQS       business quarter start frequency  
#A         year end frequency  
#BA        business year end frequency  
#AS        year start frequency  
#BAS       business year start frequency  
#BH        business hour frequency  
#H         hourly frequency  
#T, min    minutely frequency  
#S         secondly frequency  
#L, ms     milliseconds  
#U, us     microseconds  
#N         nanoseconds  



