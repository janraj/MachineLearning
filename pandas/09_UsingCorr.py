'''
correlation method generate the relationship between each continuous variable
'''
import pandas as pd
data = pd.read_excel('data/All_IPL_Match_Scores_raw.xlsx')
print("Display correlation using corr method {}".format(data.corr()))


print("Correlation tables are a numerical representation of the bivariate relationships in the dataset. Positive numbers indicate a positive correlation — one goes up the other goes up — and negative numbers represent an inverse correlation — one goes up the other goes down. 1.0 indicates a perfect correlation.")


'''
Examining bivariate relationships comes in handy when you have an outcome or dependent variable in mind and would like to see the features most correlated to the increase or decrease of the outcome
'''
