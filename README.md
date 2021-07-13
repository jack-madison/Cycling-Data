# Cycling-Data
This repository contains code to retrieve bike counter and bike share trip data from various cities across North America and Europe. Additionally, CSV files of aggregated counter and trip data will be provided. Currently this repository is a work in progress.

## Bike Share Data
Bike share data is retrived from the individual provider's website in CSV format. Each of the monthly (or quarterly) CSV files contain data on individual trips. The python files aggregates this data into daily trip counts but can easily be modified for different aggregation windows. Below are the links to each city's bike share system data.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Bay Area, CA (Bay Wheels): https://www.lyft.com/bikes/bay-wheels/system-data

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Boston, MA (Blue Bikes): https://www.bluebikes.com/system-data

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Chicago, IL (Divvy Bikes): https://divvy-tripdata.s3.amazonaws.com/index.html

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Los Angeles, CA (Metro Bikeshare): https://bikeshare.metro.net/about/data/

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; New York City, NY (Citi Bike NYC): https://www.citibikenyc.com/system-data

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Philadelphia, PA (Indego): https://www.rideindego.com/about/data/

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Washington, DC (Capital Bikeshare): https://www.capitalbikeshare.com/system-data

More bike share data will be uploaded as it is collected.

## Bike Counter Data
Data for bicycle counters are generally taken from the municipality's website and accessed through an API. The links to each city's bike counter data is listed below.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; New York City, NY: https://data.cityofnewyork.us/Transportation/Bicycle-Counts/uczf-rk3c

More bike counter data will be uploaded as it is collected.

## Weather Data
Weather data is also included in this repository since no analysis of bike ridership is complete without detailed weather data to use as controls. Below are the links to the weather data sources.

No weather data has bee added yet. 

More weather data will be uploaded as it is collected.
