#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime
#Create an empty dataframe to append the daily counts to

Los_Angeles_weatherdata = pd.DataFrame(columns=['date', 'Snow', 'Precipitation_per_day(F)', 'Average_daily_tempeture(F)','Maximum_daily_tempeture(F)','Minimum_daily_tempeture(F)'])

#Import each dataset and then resample and append to an aggregate dataset
url = "https://www.ncei.noaa.gov/orders/cdo/2648803.csv"
df = pd.read_csv(url)
df
df = df[['DATE'] + ['PRCP'] + ['TAVG']+['TMAX']+['TMIN']]
df.reset_index(drop=True, inplace=True)
df.columns = ['date', 'Precipitation_per_day(F)', 'Average_daily_tempeture(F)','Maximum_daily_tempeture(F)','Minimum_daily_tempeture(F)']
Los_Angeles_weatherdata=Los_Angeles_weatherdata.append(df, ignore_index = True)

Los_Angeles_weatherdata['Maximum_daily_tempeture(C)'] = (Los_Angeles_weatherdata['Maximum_daily_tempeture(F)'] -30)*5/9 
Los_Angeles_weatherdata['Minimum_daily_tempeture(C)'] = (Los_Angeles_weatherdata['Minimum_daily_tempeture(F)'] -30)*5/9 
Los_Angeles_weatherdata['Average_daily_tempeture(F)'] = (Los_Angeles_weatherdata['Minimum_daily_tempeture(F)'] +Los_Angeles_weatherdata['Maximum_daily_tempeture(F)'])/2
Los_Angeles_weatherdata['Average_daily_tempeture(C)'] = (Los_Angeles_weatherdata['Average_daily_tempeture(F)'] -30)*5/9 
Los_Angeles_weatherdata

#Export the daily counts as a csv
Los_Angeles_weatherdata.to_csv('./losangeles_ca/weather_data/losangeles_daily_weather_data.csv', index = False)


