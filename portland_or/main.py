import pandas as pd

# Create an empty dataframe to append the daily counts to
Portland_OR_weatherdata = pd.DataFrame(
    columns=['Date', 'Precipitation_per_day(mm)', 'Snow', 'Average_daily_tempeture(C)', 'Maximum_daily_tempeture(C)',
             'Minimum_daily_tempeture(C)'])

# Import each dataset and then resample and append to an aggregate dataset
url = "2651836.csv"
df = pd.read_csv(url)
df.reset_index(drop=True, inplace=True)
df.columns = ['Date', 'Precipitation_per_day(mm)', 'Snow', 'Average_daily_tempeture(C)', 'Maximum_daily_tempeture(C)',
              'Minimum_daily_tempeture(C)']

Portland_OR_weatherdata = Portland_OR_weatherdata.append(df, ignore_index=True)
Portland_OR_weatherdata['Average_daily_tempeture(F)'] = round(((Portland_OR_weatherdata['Average_daily_tempeture(C)'] * (9/5)) + 32),2)
Portland_OR_weatherdata['Maximum_daily_tempeture(F)'] = round(((Portland_OR_weatherdata['Maximum_daily_tempeture(C)'] * (9/5)) + 32),2)
Portland_OR_weatherdata['Minimum_daily_tempeture(F)'] = round(((Portland_OR_weatherdata['Minimum_daily_tempeture(C)'] * (9/5)) + 32),2)


# Export the daily counts as a csv
Portland_OR_weatherdata.to_csv('./Portland_OR_weatherdata.csv', index=False)
print(Portland_OR_weatherdata.head())
