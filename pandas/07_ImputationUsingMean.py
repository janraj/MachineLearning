'''
  Here we use mean  imputation technique to fill the data.
  Imputation is a conventional feature engineering technique used to keep valuable data that have null values.

  There may be instances where dropping every row with a null value removes too big a chunk from your dataset, so instead we can impute that null with another value, usually the mean or the median of that column.
 
'''
import pandas as pd
data = pd.read_excel('data/All_IPL_Match_Scores_raw.xlsx')

print("Check how many fields have empty values using isnull mehod", data.isnull().sum())

Bat_Second_15_ov_Req_RR = data['Bat_Second_15_ov_Req_RR']
print("Filtered column data for Bat_Second_15_ov_Req_RR {}".format(Bat_Second_15_ov_Req_RR.head()))
print("Number of empty fields present in Bat Second_15_ove_Ref_RR column {}".format(Bat_Second_15_ov_Req_RR.isnull().sum()))


print("Impute missing value of Bat_Second_15_ov_Req_RR using mean")

Bat_Second_15_ov_Req_RR_mean = Bat_Second_15_ov_Req_RR.mean()
print("Mean values we got is {}".format(Bat_Second_15_ov_Req_RR_mean))


print("With this mean fill the null using nullna")
Bat_Second_15_ov_Req_RR.fillna(Bat_Second_15_ov_Req_RR_mean, inplace=True)
print("Check how many fields have empty values after fillna operation using mean {}".format(Bat_Second_15_ov_Req_RR.isnull().sum()))
