'''
   Mostly data set does not contain any duplicate rows. However it is always important to make sure there is no duplicate rows before present in the data set.
   This sections discuss append and inplace operations available in panda

'''
import pandas as pd

data = pd.read_csv('data/zoo.csv')
print("Rows and columns of input data", data.shape)

'''
   Appending the data to create duplicate data
'''

new_data = data.append(data)
print("Rows and columns of appended data", new_data.shape)

'''
  Drop teh duplicate from new data using drop_duplicate method
'''

new_data = new_data.drop_duplicates()
print("Rows and columns of data after removing duplicate", new_data.shape)

'''
   Inplace argument for avoiding assignments 
'''
new_data = new_data.append(new_data)
print("Rows and columns of appended data", new_data.shape)
new_data.drop_duplicates(inplace=True)
print("Removing duplicate using inplace and drop_duplicates method", new_data.shape)
