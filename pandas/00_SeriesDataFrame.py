'''
   Indexed data which can be created from list and arrays.
   pandas package is available via import pandas.
'''
import pandas as pd

data = pd.Series([1, 2, 3, 4,5]) # Series from list

print("Series data is \n{}".format(data))

'''
 Series can be accessed using index.
'''

print("Display series data at index 3 is {} ".format(data[3]))

print("Display series data from  index 2 to 4 using : operator is  \n{} ".format(data[2:5]))

'''
 Pandas series index can be explictly define using index argument
'''

print("Creating Series with explicit index\n")
data = pd.Series([1, 2, 3, 4, 5], index=["zero", "one", "two", "three", "four"])
print(data)
'''
 Pandas Data Frame is a collections of pandas Series.
'''
data = pd.DataFrame([1, 2, 3, 4,5]) #  One dimensional Data Frame
print("One dimensional Data frame\n{}".format(data))

data = pd.DataFrame([1, 2, 3, 4,5], index=["zero", "one", "two", "three", "four"]) #  One dimensional Data Frame
print("One dimensional Data frame with explicit Index\n{}".format(data))

data = pd.DataFrame([[1, 2, 3, 4, 5], [11, 12, 13, 14, 15]]) #  Two dimensional Data Frame
print("Two dimensional Data frame\n{}".format(data))
