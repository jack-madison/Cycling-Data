#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create a list of the dataset names
names = ['bluebikes202001', 'bluebikes202002', 'bluebikes202003', 'bluebikes202004', 'bluebikes202005',
'bluebikes202006', 'bluebikes202007', 'bluebikes202008', 'bluebikes202009', 'bluebikes202010',
'bluebikes202011', 'bluebikes202012', 'bluebikes202101', 'bluebikes202102', 'bluebikes202103',
'bluebikes202104', 'bluebikes202105']

#Create an empty dataframe to append the daily counts to
bostonbikeshare = pd.DataFrame(columns=['date', 'ride_count'])

#Import each dataset and then resample and append to an aggregate dataset
for x in names:
    df = pd.read_csv("./boston_ma/system_data/" + str(x) + ".csv")
    df['ride_count'] = 1
    df['date_i'] = pd.to_datetime(df['starttime'])
    df = df.resample('D', on = 'date_i').sum()
    df['date'] = df.index
    df = df[['date'] + ['ride_count']]
    df.reset_index(drop=True, inplace=True)
    x
    bostonbikeshare = bostonbikeshare.append(df, ignore_index = True)
print("Done!")

#Export the daily counts as a csv
bostonbikeshare.to_csv('./boston_ma/boston_daily_bikeshare.csv', index = False)