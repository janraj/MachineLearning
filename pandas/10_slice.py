'''
 Data frame can be sliced into different chunks for better analytics
'''
import pandas as pd
data = pd.read_csv('data/zoo.csv')
print("We can slice using column name and square bracket {}".format(data['milk']))

print("\n Type of slice based on column become Series in data frames {}".format(type(data['milk'])))

print("\n We can slice the same such a way we can get Data frame type as well using list of column names")
print("\n Type of slice based on column with list become  DataFrame  {}".format(type(data[['milk']])))

print("\n Get dat by rows using loc and iloc method")
print("\n loc method locate row by name and iloc locate the row by index")
data.set_index("animal_name", inplace=True)
print("data ", data)
print("locate row 2 using iloc method \n {}".format(data.iloc[1]))
print("locate row swan using loc method \n {}".format(data.loc["swan"]))


print("locate row 2 to 5 using iloc method and python slice technique : \n {}".format(data.iloc[1:5]))
print("locate row swan to wasp using loc method and python slice technique :\n {}".format(data.loc["swan":"wasp"]))

