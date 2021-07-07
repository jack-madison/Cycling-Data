#Import the required packages
import pandas as pd
import json
import requests
import numpy as np
from datetime import datetime

#Specify the Google Drive link keys for each of the monthly CSV files
google_drive_keys = [
"19GwTAEThIpzc1C12QYiEvu-P39SQqjaF", "17k7nMOUdVTZykAUP6nZHylKf-_a7nJR-", "17pmWJ-yJUT66A09lrMax01_bnEycwAco",
"17lpYIixTOcdZ7-SgoXrr4vdeSnYp_xgQ", "17gUSmxTJXWPjbB-l7HDK1FzlvULTqXNf", "1h7tvRaMkqOVZY0xvOcIU1TXb36qe8Hbu", 
"1UZ77Xx6H0xsDUQ6z2ZEkFotC71xedtt-", "13tTHQY4-bMBwSgnG-L48XC6R_xQf389G", "13clYhYD4xvh-RX_e7-pX3xF1LheT40SZ",
"1UYA5dLM_1Hkc3RQGnrGpu-GXJ70JZLm6", "1femdPsRctZchjDgsGy2Q4akNOn_PmKVO", "1pMh7Wp-dYz8M8xAbfRWOVeMzqwMVyZTJ",
"1hffELgzEuCWd_-nqsdQbU6B3YEQYB8KY", "1IMwLZfnUkaUMimEi-hp4X68uuke99Ym0", "1feKIQOmOLgNlQWDkqdD0P9LlZopp_c6U",
"1MCUVg0LJMOJJmvY2PeP91gSmJL3HXobS", "1JxpJlpllThBmdbMxYXhBEDnckPtNUkXd", "1F5fPg4JEpYXbI3dX1gv7he88gv3CXIfa",
"1DXPDzxt5HKkOV5e7B2veQ0PMVtih44LJ", "19aqDJksVY87l1yavpQWbA5UNkwzrBVtE", "17-W2UMCgjXopvJUPZ-eWhEOxtjs73ZhW",
"16b7RpWOj_O-tYfZM23KJlMyj9c0kqMXA", "16RsSrz42HlNWr7O0G5axxXS6wYMi48Ys", "1620iRVKfAPs0pzmpfupEPcStQ61vAZmQ",
"1oRpGt22rjkvZrC7cIhDnQdf-dojfkMOm", "1Fl2DVuNMMWFMo8a3EHilfxck0KJH0Cu5", "1Egm1hWCTUFIKIDQDK4pScnpQbjpfRJof",
"1Adg34DeBYIlOd_mxSDUeinPEkhJFkTkX", "17dCNNei6gUNDtzeFIMKfJ8xaWSYTxki2", "123RFp09U95pD7EkUl1alkuAEqQnhX7bJ"
]

vancouver_bikeshare = pd.DataFrame(columns=['date', 'count', 'total_distance', 'total_duration'])

for x in google_drive_keys:
    print(x)
    url = 'https://drive.google.com/uc?id=' + str(x) 
    df = pd.read_csv(url)
    df['count'] = 1
    df['date_i'] = pd.to_datetime(df['Departure'])
    df = df.resample('D', on = 'date_i').sum()
    df['date'] = df.index
    df = df[['date'] + ['count'] + ['Covered distance (m)'] + ['Duration (sec.)']]
    df.reset_index(drop=True, inplace=True)
    df.columns = ['date', 'count', 'total_distance', 'total_duration']
    vancouver_bikeshare = vancouver_bikeshare.append(df, ignore_index = True)

print("Done")

vancouver_bikeshare['average_distance'] = vancouver_bikeshare['total_distance'] / vancouver_bikeshare['count']
vancouver_bikeshare['average_duration'] = vancouver_bikeshare['total_duration'] / vancouver_bikeshare['count']