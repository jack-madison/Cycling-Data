#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create a list of the dataset names
names = ['citibike202001', 'citibike202002', 'citibike202003', 'citibike202004', 'citibike202005',
'citibike202006', 'citibike202007', 'citibike202008', 'citibike202009', 'citibike202010',
'citibike202011', 'citibike202012', 'citibike202101', 'citibike202102', 'citibike202103',
'citibike202104', 'citibike202105']

#Create an empty dataframe to append the daily counts to
nyc_bikeshare = pd.DataFrame(columns=['date', 'ride_count'])

#Import each dataset and then resample and append to an aggregate dataset
for x in names:
    try:
        df = pd.read_csv("./newyorkcity_ny/bike_share/system_data/" + str(x) + ".csv")
        df['ride_count'] = 1
        df['date_i'] = pd.to_datetime(df['starttime'])
        df = df.resample('D', on = 'date_i').sum()
        df['date'] = df.index
        df = df[['date'] + ['ride_count']]
        df.reset_index(drop=True, inplace=True)
        nyc_bikeshare = nyc_bikeshare.append(df, ignore_index = True)
    except:
        df = pd.read_csv("./newyorkcity_ny/bike_share/system_data/" + str(x) + ".csv")
        df['ride_count'] = 1
        df['date_i'] = pd.to_datetime(df['started_at'])
        df = df.resample('D', on = 'date_i').sum()
        df['date'] = df.index
        df = df[['date'] + ['ride_count']]
        df.reset_index(drop=True, inplace=True)
        nyc_bikeshare = nyc_bikeshare.append(df, ignore_index = True)
print("Done!")

#Export the daily counts as a csv
nyc_bikeshare.to_csv('./newyorkcity_ny/bike_share/nyc_daily_bikeshare.csv', index = False)