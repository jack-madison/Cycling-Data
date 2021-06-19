#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime
from sodapy import Socrata

#Specify the Socrata client
client = Socrata("data.cityofnewyork.us", None)

#Get the counter device information from the API
counter_results = client.get("smn3-rzf9", limit=1000)
counters = pd.DataFrame.from_records(counter_results)

#Remove unnessisary columns from the counter dataframe and organize the columns
counters = counters[['site', 'name', 'latitude', 'longitude', 'installationdate']]

#Get the count data from the API
count_results = client.get("uczf-rk3c", limit=100000000)
count = pd.DataFrame.from_records(count_results)

#Remove unnessisary columns from the counts dataframe
count = count[['site', 'date', 'counts']]

#Merge the two dataframes together
count = count.merge(counters, how='left', on='site')

#Set the counts data to be a numeric and the date to datetime
count['counts'] = pd.to_numeric(count['counts'])
count['date'] = pd.to_datetime(count['date'])

#Create a pivot table with dates as the rows and devices as the columns
count_pivot = pd.pivot_table(count, values='counts', index='date', columns='site')

#Resample the dataset to show hourly counts, then unstack the data and re-merge the counter info
count_hourly = count_pivot.resample('H').apply(lambda x: np.sum(x.values))
count_hourly_stack = pd.DataFrame(count_hourly.stack())
count_hourly_stack.reset_index(inplace=True)
count_hourly_stack.columns = ['date', 'site', 'count']
hourly_count_data = count_hourly_stack.merge(counters, how='left', on='site')

#Resample the dataset to show daily counts, then unstack the data and re-merge the counter info
count_daily = count_pivot.resample('D').apply(lambda x: np.sum(x.values))
count_daily_stack = pd.DataFrame(count_daily.stack())
count_daily_stack.reset_index(inplace=True)
count_daily_stack.columns = ['date', 'site', 'count']
daily_count_data = count_daily_stack.merge(counters, how='left', on='site')

#First change the date and install date to datetime then remove any datapoints that occur before the installation date
hourly_count_data['date'] = pd.to_datetime(hourly_count_data['date'])
hourly_count_data['installationdate'] = pd.to_datetime(hourly_count_data['installationdate'])
daily_count_data['date'] = pd.to_datetime(daily_count_data['date'])
daily_count_data['installationdate'] = pd.to_datetime(daily_count_data['installationdate'])
hourly_count_data = hourly_count_data[hourly_count_data['date'] >= hourly_count_data['installationdate']]
daily_count_data = daily_count_data[daily_count_data['date'] >= daily_count_data['installationdate']]

#Export the two dataframes as CSV files
hourly_count_data.to_csv('./nyc_hourly_bike_counts.csv')
daily_count_data.to_csv('./nyc_daily_bike_counts.csv')