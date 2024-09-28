import pandas as pd

#reading in the raw data
raw_data_df = pd.read_csv('data_raw/raw_frailty_in_female.csv')

#checking for any missing data
print(raw_data_df.isna().sum())

#writing the clean data to the new file 
raw_data_df.to_csv('data_clean/clean_frailty_data.csv', index = False)
print("clean data stored to the file")

