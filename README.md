### Date created
2 May 2020

### Project Title
Bikeshare data analysis

### Description
Python program which is used to analyse the bikeshare data of either Chicago, New York City, or Washington.
The program asks for various filters for analysis, including: city (data file), month, day.


### Files used
bikeshare_2.py
chicago.csv
new_york_city.csv
washington.csv

### Credits
1. The method load_data(city, month, day) was derived from Udacity Practise Problem 3.

2. The solution to extract the day name in the load_data() method was derived from https://knowledge.udacity.com/questions/132505 as solution from Udacity Practise Solution 3 didn't work due to version difference.
   ie: df['day_of_week'] = df['Start Time'].dt.day_name() 

3. The solution to extract frequent combination of start and end stations in the station_stats() method was derived from:
https://knowledge.udacity.com/questions/74297
   ie: common_stations = df.groupby(['Start Station','End Station']).size().nlargest(1)

4. Udacity Version Control course for training on how to use Git and GitHub
