#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create a list of the dataset names
names = ['divvy2020Q1', 'divvy202004', 'divvy202005', 'divvy202006', 'divvy202007',
'divvy202008', 'divvy202009', 'divvy202010', 'divvy202011', 'divvy202012',
'divvy202101', 'divvy202102', 'divvy202103', 'divvy202104', 'divvy202105']

#Create an empty dataframe to append the daily counts to
chicago_bikeshare = pd.DataFrame(columns=['date', 'ride_count'])

#Import each dataset and then resample and append to an aggregate dataset
for x in names:
    df = pd.read_csv("./chicago_il/system_data/" + str(x) + ".csv")
    df['ride_count'] = 1
    df['date_i'] = pd.to_datetime(df['started_at'])
    df = df.resample('D', on = 'date_i').sum()
    df['date'] = df.index
    df = df[['date'] + ['ride_count']]
    df.reset_index(drop=True, inplace=True)
    x
    chicago_bikeshare  = chicago_bikeshare .append(df, ignore_index = True)
print("Done!")

#Export the daily counts as a csv
chicago_bikeshare .to_csv("./chicago_il/chicago_daily_bikeshare.csv", index=False)