#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create a list of the dataset names
names = ['capitalbikeshare202001', 'capitalbikeshare202002', 'capitalbikeshare202003', 'capitalbikeshare202004', 'capitalbikeshare202005',
'capitalbikeshare202006', 'capitalbikeshare202007', 'capitalbikeshare202008', 'capitalbikeshare202009', 'capitalbikeshare202010',
'capitalbikeshare202011', 'capitalbikeshare202012', 'capitalbikeshare202101', 'capitalbikeshare202102', 'capitalbikeshare202103',
'capitalbikeshare202104', 'capitalbikeshare202105']

#Create an empty dataframe to append the daily counts to
washington_bikeshare = pd.DataFrame(columns=['date', 'ride_count'])

#Import each dataset and then resample and append to an aggregate dataset
for x in names:
    try:
        df = pd.read_csv("./washington_dc/system_data/" + str(x) + ".csv")
        df['ride_count'] = 1
        df['date_i'] = pd.to_datetime(df['Start date'])
        df = df.resample('D', on = 'date_i').sum()
        df['date'] = df.index
        df = df[['date'] + ['ride_count']]
        df.reset_index(drop=True, inplace=True)
        x
        washington_bikeshare = washington_bikeshare.append(df, ignore_index = True)
    except:
        df = pd.read_csv("./washington_dc/system_data/" + str(x) + ".csv")
        df['ride_count'] = 1
        df['date_i'] = pd.to_datetime(df['started_at'])
        df = df.resample('D', on = 'date_i').sum()
        df['date'] = df.index
        df = df[['date'] + ['ride_count']]
        df.reset_index(drop=True, inplace=True)
        x
        washington_bikeshare = washington_bikeshare.append(df, ignore_index = True)
print("Done!")

#Export the daily counts as a csv
washington_bikeshare.to_csv("./washington_dc/washington_daily_bikeshare.csv", index = False)