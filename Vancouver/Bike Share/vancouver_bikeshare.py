#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

x = "19GwTAEThIpzc1C12QYiEvu-P39SQqjaF"

vancouver_bikeshare = pd.DataFrame(columns=['date', 'count', 'total_distance', 'total_duration'])

url = 'https://drive.google.com/uc?id=' + str(x) 
df = pd.read_csv(url)
df['count'] = 1
df['date_i'] = pd.to_datetime(df['Departure'])
df = df.resample('D', on = 'date_i').sum()
df['date'] = df.index
df = df[['date'] + ['count'] + ['Covered distance (m)'] + ['Duration (sec.)']]
df.reset_index(drop=True, inplace=True)
df.columns = ['date', 'count', 'total_distance', 'total_duration']
vancouver_bikeshare = vancouver_bikeshare.append(df, ignore_index = True)


vancouver_bikeshare['average_distance'] = vancouver_bikeshare['total_distance'] / vancouver_bikeshare['count']
vancouver_bikeshare['average_duration'] = vancouver_bikeshare['total_duration'] / vancouver_bikeshare['count']