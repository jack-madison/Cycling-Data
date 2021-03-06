#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create an empty dataframe to append the daily counts to
CHICAGO_weatherdata = pd.DataFrame(columns=['date', 'Snow', 'Precipitation_per_day(mm)', 'Average_daily_tempeture(F)','Maximum_daily_tempeture(F)','Minimum_daily_tempeture(F)'])
 
#Import each dataset and then resample and append to an aggregate dataset
url = "https://www.ncei.noaa.gov/orders/cdo/2650999.csv"
df = pd.read_csv(url)
df = df[['DATE'] + ['SNOW'] + ['PRCP'] + ['TAVG']+['TMAX']+['TMIN']]
df.reset_index(drop=True, inplace=True)
df.columns = ['date', 'Snow', 'Precipitation_per_day(mm)', 'Average_daily_tempeture(F)','Maximum_daily_tempeture(F)','Minimum_daily_tempeture(F)']
CHICAGO_weatherdata1=CHICAGO_weatherdata.append(df, ignore_index = True)
CHICAGO_weatherdata1['Average_daily_tempeture(C)'] = (CHICAGO_weatherdata1['Average_daily_tempeture(F)'] -30)*5/9 
CHICAGO_weatherdata1['Maximum_daily_tempeture(C)'] = (CHICAGO_weatherdata1['Maximum_daily_tempeture(F)'] -30)*5/9 
CHICAGO_weatherdata1['Average_daily_tempeture(F)'] = (CHICAGO_weatherdata1['Minimum_daily_tempeture(F)'] +CHICAGO_weatherdata1['Maximum_daily_tempeture(F)'])/2
CHICAGO_weatherdata1['Minimum_daily_tempeture(C)'] = (CHICAGO_weatherdata1['Minimum_daily_tempeture(F)'] -30)*5/9 
CHICAGO_weatherdata1


#Export the daily counts as a csv
CHICAGO_weatherdata1.to_csv('./chicago_il/weather_data/chicago_daily_weather_data.csv', index = False)
