'''
  Conditional selection using logical operators
  We have covered how to select columns and rows.
  Here we discuss selection of frame based on multiple conditions
'''
import pandas as pd
data = pd.read_csv('data/zoo.csv')
print("Select all the animals whose name is swan \n{}".format((data["animal_name"] == "swan").head()))
print("Select all the animals whose name is swan with data instead Flase True \n {}".format(data[data["animal_name"] == "swan"]))
