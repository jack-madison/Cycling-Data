#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create a list of the dataset names
names = ['niceride201804', 'niceride201805', 'niceride201806', 'niceride201807', 'niceride201808', 'niceride201809', 'niceride201810', 
'niceride201811', 'niceride201904', 'niceride201905', 'niceride201906', 'niceride201907', 'niceride201908', 'niceride201909', 
'niceride201910', 'niceride201911', 'niceride202004', 'niceride202005', 'niceride202006', 'niceride202007', 'niceride202008', 
'niceride202009']

niceride = pd.DataFrame(columns=['date', 'counter'])

for x in names:
    df = pd.read_csv("./Minneapolis/niceride/" + str(x) + ".csv")
    df['counter'] = 1
    df['date_i'] = pd.to_datetime(df['start_time'])
    df = df.resample('D', on = 'date_i').sum()
    df['date'] = df.index
    df = df[['date'] + ['counter']]
    df.reset_index(drop=True, inplace=True)
    x
    niceride = niceride.append(df, ignore_index = True)

print("Done!")

niceride.to_csv('./Minneapolis/minneapolis_bikeshare.csv', index = False)