import time
import pandas as pd
import numpy as np
from tabulate import tabulate

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york": "new_york_city.csv",
    "washington": "washington.csv",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (int) month - number of the month to filter by, or zero to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("-" * 40)
    print("Hello! Let's explore some US bikeshare data!")

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = handle_input_city_by_number()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = handle_input_month_by_number()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = handle_input_day_by_number()
    
    print('-'*40)
    return (city, month, day)
    
def handle_input_city_by_number():
    """
    validate input city number and prevent users from entering wrong data
    
    Returns:
        (str) city - name of the city
    """
    CITY_NUM_DATA = {
        "1": "chicago",
        "2": "new york",
        "3": "washington",
    }
            
    city_num = input(
            "\nPlease input number to select city: 1-Chicago, 2-New York, 3-Washington: \n")
    while city_num not in CITY_NUM_DATA:
        print('Please try again! Number must be 1, 2 or 3')
        city_num = input(
            "\nPlease input number to select city: 1-Chicago, 2-New York, 3-Washington: \n")
            
    return CITY_NUM_DATA[city_num]

def handle_input_month_by_number():
    """
    validate input month number and prevent users from entering wrong data
    
    Returns:
        (int) month - month number
    """
    MONTH_DATA = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
    }
            
    month = input(
            "\nPlease input number to select month: 0-all, 1-january, 2-february, 3-march, 4-april, 5-may, 6-jun: \n")
    while month not in MONTH_DATA:
        print('Please try again! Number must be between 0 and 6')
        month = input(
            "\nPlease input number to select month: 0-all, 1-january, 2-february, 3-march, 4-april, 5-may, 6-jun: \n")
            
    return MONTH_DATA[month]

def handle_input_day_by_number():
    """
    validate input day number and prevent users from entering wrong data
    
    Returns:
        (str) day - name of the day
    """
    DAY_DATA = {
        "0": "all",
        "1": "monday",
        "2": "tuesday",
        "3": "wednesday",
        "4": "thursday",
        "5": "friday",
        "6": "saturday",
        "7": "sunday",
    }
            
    day = input(
            "\nPlease input number to select day: 0-all, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday, 7-Sunday: \n")
    while day not in DAY_DATA:
        print('Please try again! Number must be between 0 and 7')
        day = input(
            "\nPlease input number to select day: 0-all, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday, 7-Sunday: \n")
            
    return DAY_DATA[day]
            

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

    # read data file with specified city into DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column from string to datetime data type
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # add new month column by extracting Start Time for easier query by month
    df["month"] = df["Start Time"].dt.month
    
    # add new day_of_week column by extracting Start Time for easier query by day of week
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    # Filter data with the month user entered
    if month != 0:
        df = df[df["month"] == month]

    # Filter data with the day user entered
    if day != "all":
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print("-" * 40)
    print("\nCalculating The Most Frequent Times of Travel...\n")

    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print("The most common month: ", common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df["day_of_week"].mode()[0]
    print("The most common day of week: ", common_day_of_week)

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_start_hour = df["hour"].mode()[0]

    print("The most common start hour: ", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_used_start_station = df["Start Station"].mode()[0]
    print("The most commonly used start station: ", commonly_used_start_station)

    # TO DO: display most commonly used end station
    commonly_used_end_station = df["End Station"].mode()[0]
    print("The most commonly used end station: ", commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station_trip = (df["Start Station"] + " AND " + df["End Station"]).mode()[0]
    print("The most frequent combination of start station and end station trip: ", start_end_station_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean travel time", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df["User Type"].value_counts() 
    print("\nCounts of user types: \n", counts_of_user_types)

    # TO DO: Display counts of gender
    if city != "washington":
        counts_of_gender = df["Gender"].value_counts()
        print("\nCounts of gender: \n", counts_of_gender)
    else:
        print("Can not display counts of gender because there is no Gender column in washington file")

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != "washington":
        earliest_year_of_birth = int(df["Birth Year"].max())
        print("\nErliest year of birth:", earliest_year_of_birth)

        most_recent_year_of_birth = int(df["Birth Year"].min())
        print("Most recent year of birth: ", most_recent_year_of_birth)

        most_common_year_of_birth = int(df["Birth Year"].mode()[0])
        print("Most common year of birth: ", most_common_year_of_birth)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print("-" * 40)
    else:
        print("Can not display earliest, most recent, and most common year of birth because there is no Birth Year column in washington file")

def view_data(df):
    """ 
    Display raw data with 5 rows of individual trip data
    """
    
    viewData = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    
    #TO DO: Display raw data to view 5 rows of individual trip data
    pd.set_option("display.max_columns",200)

    start_loc = 0
    while viewData == "yes":
        #print(df.iloc[start_loc:start_loc + 5])
        print(tabulate(df.iloc[np.arange(0+start_loc,5+start_loc)], headers ="keys"))
        start_loc += 5
        viewData = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        
        # Change this function because washington.csv file don't contain Gender and Birth Year column
        user_stats(df, city)
        
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
