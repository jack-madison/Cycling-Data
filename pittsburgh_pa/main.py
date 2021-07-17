import pandas as pd

# Create an empty dataframe to append the daily counts to
PSB_data = pd.DataFrame(
    columns=['Date', 'Snow', 'Precipitation_per_day(mm)', 'Average_daily_tempeture(C)', 'Maximum_daily_tempeture(C)',
             'Minimum_daily_tempeture(C)'])

# Import each dataset and then resample and append to an aggregate dataset
url = "2652903.csv"
df = pd.read_csv(url)
df.reset_index(drop=True, inplace=True)
df.columns = ['Date', 'Precipitation_per_day(mm)', 'Snow', 'Average_daily_tempeture(F)', 'Maximum_daily_tempeture(F)',
              'Minimum_daily_tempeture(F)']

PSB_data=PSB_data.append(df, ignore_index=True)
PSB_data['Average_daily_tempeture(C)'] = round(((PSB_data['Average_daily_tempeture(F)'] -30)*5/9),2)
PSB_data['Maximum_daily_tempeture(C)'] = round(((PSB_data['Maximum_daily_tempeture(F)'] -30)*5/9),2)
PSB_data['Minimum_daily_tempeture(C)'] = round(((PSB_data['Minimum_daily_tempeture(F)'] -30)*5/9),2)

# Export the daily counts as a csv
PSB_data.to_csv('PSB_data.csv', index=False)

print(PSB_data.head())
