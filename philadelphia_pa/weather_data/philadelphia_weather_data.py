#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Create an empty dataframe to append the daily counts to
PHILADELPHIA_weatherdata = pd.DataFrame(columns=['date', 'Snow', 'Precipitation_per_day(mm)', 'Average_daily_tempeture(F)','Maximum_daily_tempeture(F)','Minimum_daily_tempeture(F)'])
 
#Import each dataset and then resample and append to an aggregate dataset
url = "https://www.ncei.noaa.gov/orders/cdo/2651221.csv"
df = pd.read_csv(url)
df = df[['DATE'] + ['SNOW'] + ['PRCP'] + ['TAVG']+['TMAX']+['TMIN']]
df.reset_index(drop=True, inplace=True)
df.columns = ['date', 'Snow', 'Precipitation_per_day(mm)', 'Average_daily_tempeture(F)','Maximum_daily_tempeture(F)','Minimum_daily_tempeture(F)']
PHILADELPHIA_weatherdata= PHILADELPHIA_weatherdata.append(df, ignore_index = True)
PHILADELPHIA_weatherdata['Maximum_daily_tempeture(C)'] = (PHILADELPHIA_weatherdata['Maximum_daily_tempeture(F)'] -30)*5/9 
PHILADELPHIA_weatherdata['Minimum_daily_tempeture(C)'] = (PHILADELPHIA_weatherdata['Minimum_daily_tempeture(F)'] -30)*5/9 
PHILADELPHIA_weatherdata['Average_daily_tempeture(C)'] = (PHILADELPHIA_weatherdata['Average_daily_tempeture(F)'] -30)*5/9 
PHILADELPHIA_weatherdata

#Export the daily counts as a csv
PHILADELPHIA_weatherdata.to_csv('./philadelphia_pa/weather_data/philadelphia_daily_weather_data.csv', index = False)
