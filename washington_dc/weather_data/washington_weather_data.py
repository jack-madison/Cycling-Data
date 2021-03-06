#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create an empty dataframe to append the daily counts to
Washington_weatherdata = pd.DataFrame(columns=['date', 'Snow', 'Precipitation_per_day(mm)', 'Average_daily_tempeture(F)','Maximum_daily_tempeture(F)','Minimum_daily_tempeture(F)'])
 
#Import each dataset and then resample and append to an aggregate dataset
url = "https://www.ncei.noaa.gov/orders/cdo/2651267.csv"
df = pd.read_csv(url)
df["TAVG"]= df[['TMAX','TMIN']].mean(axis=1)
df = df[['DATE'] + ['SNOW'] + ['PRCP'] + ['TAVG']+['TMAX']+['TMIN']]
df.reset_index(drop=True, inplace=True)
df.columns = ['date', 'Snow', 'Precipitation_per_day(mm)', 'Average_daily_tempeture(F)','Maximum_daily_tempeture(F)','Minimum_daily_tempeture(F)']
Washington_weatherdata= Washington_weatherdata.append(df, ignore_index = True)

Washington_weatherdata['Maximum_daily_tempeture(C)'] = (Washington_weatherdata['Maximum_daily_tempeture(F)'] -30)*5/9 
Washington_weatherdata['Minimum_daily_tempeture(C)'] = (Washington_weatherdata['Minimum_daily_tempeture(F)'] -30)*5/9 
Washington_weatherdata['Average_daily_tempeture(F)'] = (Washington_weatherdata['Minimum_daily_tempeture(F)'] + Washington_weatherdata['Maximum_daily_tempeture(F)'])/2
Washington_weatherdata['Average_daily_tempeture(C)'] = (Washington_weatherdata['Average_daily_tempeture(F)'] -30)*5/9 
Washington_weatherdata

#Export the daily counts as a csv
Washington_weatherdata.to_csv('./washington_dc/weather_data/washington_daily_weather_data.csv', index = False)

