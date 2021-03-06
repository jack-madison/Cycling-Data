#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create an empty dataframe to append the daily counts to
BOSTON_weatherdata = pd.DataFrame(columns=['date', 'Snow', 'Precipitation_per_day(F)', 'Average_daily_tempeture(F)','Maximum_daily_tempeture(F)','Minimum_daily_tempeture(F)'])
 
#Import each dataset and then resample and append to an aggregate dataset
url = "https://www.ncei.noaa.gov/orders/cdo/2648769.csv"
df = pd.read_csv(url)
df = df[['DATE'] + ['SNOW'] + ['PRCP'] + ['TAVG']+['TMAX']+['TMIN']]
df.reset_index(drop=True, inplace=True)
df.columns = ['date', 'Snow', 'Precipitation_per_day(F)', 'Average_daily_tempeture(F)','Maximum_daily_tempeture(F)','Minimum_daily_tempeture(F)']
BOSTON_weatherdata=BOSTON_weatherdata.append(df, ignore_index = True)
BOSTON_weatherdata['Average_daily_tempeture(C)'] = (BOSTON_weatherdata['Average_daily_tempeture(F)'] -30)*5/9 
BOSTON_weatherdata['Maximum_daily_tempeture(C)'] = (BOSTON_weatherdata['Maximum_daily_tempeture(F)'] -30)*5/9 
BOSTON_weatherdata['Minimum_daily_tempeture(C)'] = (BOSTON_weatherdata['Minimum_daily_tempeture(F)'] -30)*5/9 
 
#Export the daily counts as a csv
BOSTON_weatherdata.to_csv('./boston_ma/weather_data/boston_daily_weather_data.csv', index = False)
