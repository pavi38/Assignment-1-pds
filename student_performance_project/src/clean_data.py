import pandas as pd

#reading the raw data file into pandas frame
raw_df = pd.read_csv('data_raw/raw_StudentsPerformance.csv')

#looking for the missing data
print(raw_df.isna().sum())

#checking the size of the database
print(raw_df.shape)

#adding a new col with mean score in all 3 catagories of test
raw_df['avg score'] = raw_df[['math score', 'reading score', 'writing score']].mean(axis=1)

#writing the data to the file
raw_df.to_csv('data_clean/clean_StudentPerformance.csv', index= False)