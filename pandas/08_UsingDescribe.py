'''
   In this section we discuss, how to get a summary of the distribution of continuous variables.
   Understanding which numbers are continuous also comes in handy when thinking about the type of plot to use to represent your data visually.
'''
import pandas as pd
data = pd.read_excel('data/All_IPL_Match_Scores_raw.xlsx')
print("Describe Entire data using describe method {}".format(data.describe()))

'''
 This tell us Venue column has some unique values, and its top value and ts frequency.
'''
print("Describe Row data using describe method for row Venue {}".format(data['Venue'].describe()))

'''
Value counts can tell us frequency of all values in a column
'''
print("frequency of all values in a column Venue using value_counts  {}".format(data['Venue'].value_counts().head(10)))
