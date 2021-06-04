import pandas as pd

class df ():
    
    def __init__(self):
        print(__name__)  # dfFunctions
    
    def frame_from_csv (self):
        frame = pd.read_csv('anastasia.csv')  # it creates an extra column on the left, which is like an index
        print (frame)
        print(__name__)  # dfFunctions
        return frame
        
    def printDfData (self, frame):  
        print ('Shape\n', frame.shape) #shape
        print ('col', frame.columns)
        print ( 'indexes', frame.index.values)
        
    
    def print_loc (self, frame):
#        mylist = ['Name','City']
#        print ( frame.loc[:,mylist])  # refer to dataframe by row indexes and column name
# 
        print ( frame.loc[1:5,['Name','Salary']])
        
        print(frame.loc[[1,7],['Name','Salary']])
#        
        print(frame.loc[1:7,'Name':'Salary'])   # slice by index and column names
#
        print(frame.loc[1,'Name':'Salary'])
#        
        df = frame.loc[1:4,'Name']
        print (df)

        
    def print_iloc (self, frame):
        print ( frame.iloc[:,:])
        df = frame.iloc[0:3,0:3] # refer to dataframe by position
        print (df)
    
    def create_xlsx(self, frame):
        frame.to_excel('anastasia.xlsx')
        frame.to_csv('ana.csv')
   
    def frame_from_xlsx(self):
        print ( 'Excel data ------------')
        frame = pd.read_excel('anastasia.xlsx')  # it creates an extra column on the left, which is like an index
        print (frame)
        return frame
    
    def getstats(self, frame):
        print ('Maximum Salary: ', frame['Salary'].max())
        print ('Minimum Salary: ', frame['Salary'].min())
        print ('Average Salary: ', frame['Salary'].mean())   
        print ('Sum of Salary : ', frame['Salary'].sum())          
        print ('Ranking the salaries\n', frame['Salary'].rank())

    def groupby_sum(self, frame):
        g1 = frame.groupby(["City"]).sum()
        print('\nSum all the number columns, by City -------------- \n',g1)
        
        g1 = frame.groupby(["Job Title"]).sum()
        print('\nSum all the number columns, by Job Title --------------\n',g1)
        
        g1 = frame.groupby(["Job Title"]).sum()
        print('\nSum all the number columns, by Job Title , show only the Salary --------------\n',g1.loc[:,['Salary']])

    def groupby_count(self,frame):
        g1 = frame.groupby(["City"]).size().reset_index(name='Number of people per city')
        print('\nCount rows, by City -------------- \n',g1)

    def query(self,frame):        
        df4 = frame.query('Age == 50')  # == != > < >= <=
        print ( 'Age 50 ------------\n', df4 )
        
        df4 = frame.query('Name == "Emily"')
        print ('Name Emily ------------\n', df4 )
        
        df4 = frame.query('City == "California"')
        print ( 'City California ------------\n', df4 )
#   
        df4 = frame.query('Age>21 or Salary<7000')    # or and 
        print ( 'Age>21 or Salary < 7000------------\n',df4 )
        
    def sort_frame(self, frame):
#        df4 = frame.query('City == "California"')
        df4 = frame.loc[:,['Salary','Name']]
        print ( df4 )
        
        dfSorted = df4.sort_index(axis=1)
        print ('df sorted on 1 index, i.e. by the names of the COLUMNS\n', dfSorted)
        
        dfSorted = df4.sort_index(axis=0)
        print ('df sorted on 0 index, i.e. by ROW\n', dfSorted)
        
    def unique(self, frame):
        print ('Unique names' , frame["Name"].unique() ) # returns a numpy array: frame["Job Title"].unique()
        print ('Unique Job Titles' , frame["Job Title"].unique() )
        print ('Unique Cities' , frame["City"].unique() )
    
    def convertToList(self, frame):
        mykeys = list ( frame.keys() ) 
        mylist = frame.values.tolist()   # frame to List
        
        df = pd.DataFrame (mylist,columns=mykeys)
        
        print ( df )
