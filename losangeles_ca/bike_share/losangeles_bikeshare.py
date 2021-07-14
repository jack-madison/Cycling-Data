#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create a list of the dataset names
names = ['metrobikeshare2020Q1', 'metrobikeshare2020Q2', 'metrobikeshare2020Q3', 'metrobikeshare2020Q4', 'metrobikeshare2021Q1',
'metrobikeshare2021Q2']

#Create an empty dataframe to append the daily counts to
la_bikeshare = pd.DataFrame(columns=['date', 'ride_count'])

#Import each dataset and then resample and append to an aggregate dataset
for x in names:
    df = pd.read_csv("./losangeles_ca/system_data/" + str(x) + ".csv")
    df['ride_count'] = 1
    df['date_i'] = pd.to_datetime(df['start_time'])
    df = df.resample('D', on = 'date_i').sum()
    df['date'] = df.index
    df = df[['date'] + ['ride_count']]
    df.reset_index(drop=True, inplace=True)
    x
    la_bikeshare = la_bikeshare.append(df, ignore_index = True)
print("Done!")

#Export the daily counts as a csv
la_bikeshare.to_csv('./losangeles_ca/la_daily_bikeshare.csv', index = False)