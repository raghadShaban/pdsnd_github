import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def greet_user():
    """Greet the user at the start of the program."""
    print('Hello! Let\'s explore some US bikeshare data!')

def display_elapsed_time(start_time):
    """Prints the time elapsed since start_time."""
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    greet_user()

    # TODO: get user input for city (chicago, new york city, washington)
    city = 'chicago'  # placeholder

    # TODO: get user input for month (all, january, february, ... , june)
    month = 'all'  # placeholder

    # TODO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 'all'  # placeholder

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
    # NOTE: Data loading not implemented yet; placeholder empty DataFrame
    df = pd.DataFrame()
    
    # TODO: Implement filtering by month and day
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\n--- Calculating The Most Frequent Times of Travel ---\n')
    start_time = time.time()

    # TODO: display the most common month
    # TODO: display the most common day of week
    # TODO: display the most common start hour

    display_elapsed_time(start_time)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\n--- Calculating The Most Popular Stations and Trip ---\n')
    start_time = time.time()

    # TODO: display most commonly used start station
    # TODO: display most commonly used end station
    # TODO: display most frequent combination of start station and end station trip

    display_elapsed_time(start_time)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\n--- Calculating Trip Duration Stats ---\n')
    start_time = time.time()

    # TODO: display total travel time
    # TODO: display mean travel time

    display_elapsed_time(start_time)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\n--- Calculating User Stats ---\n')
    start_time = time.time()

    # TODO: Display counts of user types
    # TODO: Display counts of gender
    # TODO: Display earliest, most recent, and most common year of birth

    display_elapsed_time(start_time)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
