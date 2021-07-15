#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create an empty dataframe to append the daily counts to
SAN_FRANCISCO_weatherdata = pd.DataFrame(columns=['date', 'Snow', 'Precipitation_per_day(F)', 'Average_daily_tempeture(F)','Maximum_daily_tempeture(F)','Minimum_daily_tempeture(F)'])

#Import each dataset and then resample and append to an aggregate dataset
url = "https://www.ncei.noaa.gov/orders/cdo/2649313.csv"
df = pd.read_csv(url)
df
df = df[['DATE'] + ['PRCP'] +['TMAX']+['TMIN']]
df.reset_index(drop=True, inplace=True)
df.columns = ['date', 'Average_daily_tempeture(F)','Maximum_daily_tempeture(F)','Minimum_daily_tempeture(F)']
SAN_FRANCISCO_weatherdata=SAN_FRANCISCO_weatherdata.append(df, ignore_index = True)

SAN_FRANCISCO_weatherdata['Maximum_daily_tempeture(C)'] = (SAN_FRANCISCO_weatherdata['Maximum_daily_tempeture(F)'] -30)*5/9
SAN_FRANCISCO_weatherdata['Minimum_daily_tempeture(C)'] = (SAN_FRANCISCO_weatherdata['Minimum_daily_tempeture(F)'] -30)*5/9
SAN_FRANCISCO_weatherdata['Average_daily_tempeture(F)'] = (SAN_FRANCISCO_weatherdata['Minimum_daily_tempeture(F)'] +SAN_FRANCISCO_weatherdata['Maximum_daily_tempeture(F)'])/2
SAN_FRANCISCO_weatherdata['Average_daily_tempeture(C)'] = (SAN_FRANCISCO_weatherdata['Average_daily_tempeture(F)'] -30)*5/9
SAN_FRANCISCO_weatherdata 

#Export the daily counts as a csv
SAN_FRANCISCO_weatherdata.to_csv('./bayarea_ca/weather_data/bayarea_daily_weather_data.csv', index = False)

