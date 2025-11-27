import time
import pandas as pd
import numpy as np

# Dictionary to map city names to CSV files
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def print_separator():
    """Print a separator line for readability."""
    print('-'*40)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")

    # Get user input for city
    while True:
        city = input("Enter city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city. Please choose from chicago, new york city, or washington.")

    # Get user input for month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Enter month (January-June) or 'all': ").lower()
        if month in months:
            break
        else:
            print("Invalid month. Please choose a valid month or 'all'.")

    # Get user input for day
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        day = input("Enter day of week (e.g., Monday) or 'all': ").lower()
        if day in days:
            break
        else:
            print("Invalid day. Please choose a valid day or 'all'.")

    print_separator()
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    try:
        df = pd.read_csv(CITY_DATA[city])
    except FileNotFoundError:
        print(f"CSV file for {city} not found. Using empty DataFrame.")
        df = pd.DataFrame()  # empty DataFrame if file not found

    # Convert 'Start Time' to datetime
    if not df.empty:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month_name().str.lower()
        df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
        df['start_hour'] = df['Start Time'].dt.hour

        # Filter by month
        if month != 'all':
            df = df[df['month'] == month]

        # Filter by day
        if day != 'all':
            df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    if not df.empty:
        print(f"Most common month: {df['month'].mode()[0]}")
        print(f"Most common day of week: {df['day_of_week'].mode()[0]}")
        print(f"Most common start hour: {df['start_hour'].mode()[0]}")
    else:
        print("No data to display.")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print_separator()

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    if not df.empty:
        print(f"Most common start station: {df['Start Station'].mode()[0]}")
        print(f"Most common end station: {df['End Station'].mode()[0]}")
        combo = df.groupby(['Start Station','End Station']).size().idxmax()
        print(f"Most frequent combination of start and end station: {combo[0]} -> {combo[1]}")
    else:
        print("No data to display.")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print_separator()

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    if not df.empty:
        print(f"Total travel time: {df['Trip Duration'].sum()} seconds")
        print(f"Mean travel time: {df['Trip Duration'].mean():.2f} seconds")
    else:
        print("No data to display.")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print_separator()

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print("\nCalculating User Stats...\n")
    start_time = time.time()

    if not df.empty:
        print("Counts of user types:")
        print(df['User Type'].value_counts())

        if 'Gender' in df.columns:
            print("\nCounts of gender:")
            print(df['Gender'].value_counts())
        else:
            print("\nGender data not available.")

        if 'Birth Year' in df.columns:
            print("\nBirth year stats:")
            print(f"Earliest: {int(df['Birth Year'].min())}")
            print(f"Most recent: {int(df['Birth Year'].max())}")
            print(f"Most common: {int(df['Birth Year'].mode()[0])}")
        else:
            print("\nBirth year data not available.")
    else:
        print("No data to display.")

    print(f"\nThis took {time.time() - start_time:.2f} seconds.")
    print_separator()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
