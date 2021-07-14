#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create a list of the dataset names
names = ['indego2020Q1', 'indego2020Q2', 'indego2020Q3', 'indego2020Q4',
'indego2021Q1', 'indego2021Q2']

#Create an empty dataframe to append the daily counts to
philadelphia_bikeshare = pd.DataFrame(columns=['date', 'ride_count'])

#Import each dataset and then resample and append to an aggregate dataset
for x in names:
    df = pd.read_csv("./philadelphia_pa/bike_share/system_data/" + str(x) + ".csv")
    df['ride_count'] = 1
    df['date_i'] = pd.to_datetime(df['start_time'])
    df = df.resample('D', on = 'date_i').sum()
    df['date'] = df.index
    df = df[['date'] + ['ride_count']]
    df.reset_index(drop=True, inplace=True)
    x
    philadelphia_bikeshare = philadelphia_bikeshare.append(df, ignore_index = True)
print("Done!")

#Export the daily counts as a csv
philadelphia_bikeshare.to_csv("./philadelphia_pa/bike_share/philadelphia_daily_bikeshare.csv", index = False)