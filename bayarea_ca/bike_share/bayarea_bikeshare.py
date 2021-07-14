#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create a list of the dataset names
names = ["baywheels202001", "baywheels202002", "baywheels202003", "baywheels202004", "baywheels202005",
"baywheels202006", "baywheels202007", "baywheels202008", "baywheels202009", "baywheels202010",
"baywheels202011", "baywheels202012", "baywheels202101", "baywheels202102", "baywheels202103",
"baywheels202104", "baywheels202105"]

#Create an empty dataframe to append the daily counts to
bayarea_bikeshare = pd.DataFrame(columns=['date', 'ride_count'])

#Import each dataset and then resample and append to an aggregate dataset
for x in names:
    try:
        df = pd.read_csv("./bayarea_ca/system_data/" + str(x) + ".csv")
        df['ride_count'] = 1
        df['date_i'] = pd.to_datetime(df['start_time'])
        df = df.resample('D', on = 'date_i').sum()
        df['date'] = df.index
        df = df[['date'] + ['ride_count']]
        df.reset_index(drop=True, inplace=True)
        bayarea_bikeshare = bayarea_bikeshare.append(df, ignore_index = True)
    except:
        df = pd.read_csv("./bayarea_ca/system_data/" + str(x) + ".csv")
        df['ride_count'] = 1
        df['date_i'] = pd.to_datetime(df['started_at'])
        df = df.resample('D', on = 'date_i').sum()
        df['date'] = df.index
        df = df[['date'] + ['ride_count']]
        df.reset_index(drop=True, inplace=True)
        bayarea_bikeshare = bayarea_bikeshare.append(df, ignore_index = True)
    x
print("Done!")

#Export the daily counts as a csv
bayarea_bikeshare.to_csv('./bayarea_ca/bayarea_daily_bikeshare.csv', index = False)