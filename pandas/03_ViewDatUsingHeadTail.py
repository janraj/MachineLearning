'''
   We have learned how to convert data to Data frame. We have learned how to read data from files using resoective methods. This section discuss how to view the data which we have read/converted.
'''
import pandas as pd
data = pd.read_csv('data/zoo.csv')

'''
 Head method can be used to see the few rows of the data. Default value of head methid is 5, however we can specify how many number of rows we want to display 
'''
print("Display data using head method\n")

print(data.head())

print('Display first 10 data using head')
print(data.head(10))

'''
 tail method can be used for viewing last five rows in use. This method also accept argument number and display based on that given value.
'''


print('Display data using tail method')
print(data.tail())

print('Display last 2 data using tail method')
print(data.tail(2))
