'''
   Values in data set fileds can be null/empty. Based on situation we have to either remove such fields, replace null values with non null values.
'''
import pandas as pd
import numpy as np
data = pd.read_csv('data/zoo.csv')

'''
 use isnull method to get nulls in each column of data set. isnull return a DataFrame where each cell is either True or False depending on that cell's null status
'''
print(" Display all empty fields in the data set if its present", data.isnull())

'''
To count the number of nulls in each column we use an aggregate function for summing
'''
print(" Display aggregated null fields in the data set", data.isnull().sum())

'''
 There is no Missing values in our data set. hence we are creating empty fields by using replace method. replace is using on column field.
'''
data['aquatic'] = data['aquatic'].replace({1: np.nan})
print(" After adding NaN, Display aggregated null fields in the data set", data.isnull().sum())

'''
Data Analysts face the dilemma of dropping or imputing null values. 
Take this decision requires intimate knowledge of your data and its context. 
Overall, removing null data is only suggested if you have a small amount of missing data.
'''
new_data = data.dropna()
print("Droping NA values using dropna() method\n", new_data.isnull().sum())

'''
 dropna removes the rows by default. But if there are many columns which provide valuable data and we need to remove only colums, then we can use axis=1 
'''
print("Data with NA values before applying dropna on cloumn", data.isnull().sum())
new_data = data.dropna(axis=1)
print("Droping NA values using dropna() method\n", new_data.isnull().sum())
