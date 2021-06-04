from dfFunctions import df
class runDf(df):
    
    a = df()  # create an object
    print(__name__)
    frame = a.frame_from_csv()
    
    a.convertToList(frame)
#    print ( frame )
#    
#    a.printDfData(frame)       # get general information about the dataframe
#
#    a.print_loc(frame)         # slice and prince data from the dataframe using loc (col and index names)
# 
#    a.print_iloc(frame)        # slice and prince data from the dataframe using iloc (position)
#   
#    a.create_xlsx(frame)       # write dataframe to excel
#   
#    frame = a.frame_from_xlsx()# read an excel file into a dataframe
#    
#    a.getstats(frame)      # Sum, min, max, average and count 
#   
#    a.groupby_sum(frame)   # group records, eg records per city
#   
#    a.groupby_count(frame) # count how many rows are in a grouping
#    
#    a.query(frame)         # filter records by value
#    
#    a.sort_frame(frame)    # sort by column name or index
#    
#    a.unique(frame)        # get unique records in a column
    
    
    
    