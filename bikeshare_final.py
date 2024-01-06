import time
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    def get_city():
        while True:
            city = input("Please enter the name of the city (Chicago, New York City, Washington): ").lower()
            if city in ['chicago', 'new york city', 'washington']:
                return city
            else:
                    print("Invalid input. Please try again.")
    # Call the function to get the city from the user
    city = get_city()
    print("You selected:",city)

    # TO DO: get user input for month (all, january, february, ... , june)
    def get_month():
        while True:
            month = input("Please enter the name of the month (all, January, February, ..., June): ").lower()
            if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                return month
            else:
                print("Invalid input. Please try again.")
    # Call the function to get the month from the user
    month = get_month()
    print("You selected:",month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    def get_day():
        while True:
            day = input("Please enter the name of the day of week (all, monday, tuesday, ... sunday) ").lower()
            if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']:
                return day
            else:
                print("Invalid input. Please try again.")
    # Call the function to get the day from the user
    day = get_day()
    print("You selected:",day)
    print('-'*40)
    return city,month,day

def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
        """
  # Retrieve the CSV file name from User input
    filename = CITY_DATA[city]   
  # Load the data into a DataFrame
    df = pd.read_csv(filename) 
  # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

  # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    #print(df['month'])
    df['day'] = df['Start Time'].dt.day_name()
    #print(df['day'])

  # Apply filters based on month and day
    if month != 'all':
     months = ['january','february','march','april','may','june']
     month = months.index(month)+1
    # Filter by month
     df = df[df['month'] == month]
    
    # Filter by day
    if day != 'all':
     df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is:", common_month)

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print("The most common day of the week is:", common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common start hour is:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_strt_station = df['Start Station'].mode()[0]
    print(common_strt_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = df['Start Station'].str.cat(df['End Station']).mode()[0]
    print(common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    # TO DO Additionally: display actual longest and shortest travel time
    max_travel_time = df['Trip Duration'].max()
    min_travel_time = df['Trip Duration'].min()
    # TO DO Additionally: display the histogram for travel time
    x = df['Trip Duration']/60
    print(x)
    bins=100
    plt.hist(x,bins,color="red", edgecolor="black")
    plt.axis('tight')
    plt.xlabel('Trip Duration[min]')
    plt.ylabel('Frequency')
    plt.title('The distribution for trip duraiton time')
    print("The histogram will be showed by 5 seconds")

    plt.show(block=False)
    plt.pause(5)
    plt.close('all')

    print("Total travel time: {} minutes".format(round(total_travel_time/60)))
    print("Mean travel time: {} minutes".format(round(mean_travel_time/60)))
    print("Longest travel time: {} minutes".format(round(max_travel_time/60)))
    print("Shortest travel time: {} minutes".format(round(min_travel_time/60)))    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    # Consider Error and Exceptions
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try :
       user_type_counts = df['User Type'].value_counts()
       print("User Type Counts:\n", user_type_counts)
    except :
       print("No data avairable this date")

    # TO DO: Display counts of gender
    try :
       gender_counts = df['Gender'].value_counts()
       print("\nGender Counts:\n", gender_counts)       
    except :
       print("No data avairable this date")

    # TO DO Additionally : Display counts of user types for each gender
    try:
       user_type_gender_counts = df.groupby(['Gender', 'User Type']).size()
       print("\nUser Type Counts for Each Gender:\n", user_type_gender_counts)
    except:
       print("No data available for this date")

    # TO DO: Display earliest, most recent, and most common year of birth
    try :
       earliest_birth_year = df['Birth Year'].min()
       print("\nEarliest Birth Year:", round(earliest_birth_year))
    except :
       print("No data avairable this date")

    try : 
       most_recent_birth_year = df['Birth Year'].max()
       print("Most Recent Birth Year:", round(most_recent_birth_year))
    except :
       print("No data avairable this date")

    try :    
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("Most Common Birth Year:", round(most_common_birth_year))
    except :
       print("No data avairable this date")
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data (df):
    """Raw data is displayed upon request by the user. Raw data will be displayed by 5 rows each in a press"""
    print('You can check the row data if "enter" press, or "no" to skip')
    i = 0
    while (input()!= 'no'):
     i = i+5
     print(df.head(i))
     print('You can check additional 5-row data if "enter" press, or "no" to skip')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city,month,day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
