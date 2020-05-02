# Adding additional comment line for Version Control project.

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). Normalise input to lowercase.
    city = input("Enter the name of the city to analyze (type chicago, new york city or washington only): ").lower()

    # check if the city value is valid and repeat asking using while loop until input is valid
    while city not in ('chicago', 'new york city', 'washington'):
        city = input("Please enter only chicago, new york city or washington): ").lower()

    # get user input for month (all, january, february, ... , june). Normalise input to lowercase
    month = input("Enter the name of the month to filter by, or \"all\" to apply no month filter: ").lower()

    # check if the month  value is valid and repeat asking using while loop until input is valid
    while month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        month = input("Please enter valid month name: ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday). Normalise input to lowercase
    day = input("Enter the name of the day of week to filter by, or \"all\" to apply no day filter: ").lower()

    # check if the day  value is valid and repeat asking using while loop until input is valid
    while day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        day = input("Please enter valid day name: ").lower()

    # this print is used throughout and provides a border between each set of outputs.
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    # extract day of week from Start Time to create new columns. Solution derived from Udacity mentor help section as noted in readme.txt
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # extract hour from Start Time to create new column to use in time_stats() method
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: {}".format(df['month'].mode()[0]))

    # display the most common day of week
    print("The most common day is: {}".format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print("The most common hour is: {}".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station is: {}".format(df['Start Station'].mode()[0]))
    # display most commonly used end station
    print("The most common end station is: {}".format(df['End Station'].mode()[0]))

    # Using groupby to get frequent combination of start station and end station trip. Solution found from Udacity Mentor Help as documented in readme.txt
    # display most frequent combination of start station and end station trip
    print("The most common start and end station combination is: \n {}".format(df.groupby(['Start Station','End Station']).size().nlargest(1)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is: {} seconds".format( df['Trip Duration'].sum() ) )

    # display mean travel time
    print("MEAN Travel time is: {} seconds".format( df['Trip Duration'].mean() ) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User type count is: \n \n{}".format( df['User Type'].value_counts() ) )
    print()

    # Display counts of gender
    print("Gender count is: \n \n{}".format( df['Gender'].value_counts() ) )
    print()

    # Display earliest, most recent, and most common year of birth
    print("Earliest birth year is: {}".format( int( df['Birth Year'].min() ) ) )
    print()

    print("Most recent birth year is: {}".format( int( df['Birth Year'].max() ) ) )
    print()

    print("Most common birth year is: {}".format( int( df['Birth Year'].mode()[0] ) ) )
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        #request user for input to see first 5 rows of raw data
        raw_data = input('\nWould you like to see the first 5 rows of raw data? Enter yes or no: ').lower()
        print()

        #continue asking user if they want to see next 5 rows until user input != yes
        while raw_data == 'yes':
            print( df.iloc[0:5,:] ) #print first/next 5 rows
            df = df.iloc[5:,:]      #slice out the 5 rows printed above so next 5 can be printed. DataFrame gets smaller for efficiency and error won't occur when end is reached.
            raw_data = input('\nWould you like to see the next 5 rows? Enter yes or no: ').lower()
            print()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
