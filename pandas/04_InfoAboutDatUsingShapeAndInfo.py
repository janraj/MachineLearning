'''
   We have converted data into data frame,
   We learned reading data using different read_xxx functions
   We have learned viewing data using head and tail command.
   here we learn how to get info, size etc of the data frame. 

'''
import pandas as pd
data = pd.read_csv('data/zoo.csv')

print("Information about data using info method: Info gives number of rows and columns, number of non null values, type of data etc.")
print(data.info())

print("Size of  data using shape : This out put just a tuple rows and column  ")
print(data.shape)

