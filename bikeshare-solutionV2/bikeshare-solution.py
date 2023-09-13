import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


months = ['january','febuary','march','april','may','june']

days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

cities = ['washington','new york city','chicago']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
      
    
    while True:
        city = input('\n new york city, chicago or washington choose a city to filter?\n')
        if city in cities:
                break
    else:
        print('please enter a valid city.')
                


    

    while True:
        month = input('\nplease choose a month to filter from january, febuary, march, april, may, june\n')
        if month in months:
            break
    else:
        print('please enter a valid month.')


  

    while True:
        day = input('\nplease choose a day to filter from sunday, monday, tuesday, wednesday, thursday, friday, saturday\n')
        if day in days:
            break
    else:
        print('please enter a valid day.')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
   


    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    
    df = df[df['month'] == month]
    
    if day != 'all':
    
        df = df[df['day_of_week'] == day.title()]

    return df
    




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nBeep..Boop..Beep..Boop calculating most frequent times of travel..Beep..Beep\n')
         
    start_time = time.time()

    
    common_month = df['month'].mode()[0]
    print('most common month:', common_month)



    
    common_day = df['day_of_week'].mode()[0]
    print ('most common day:', common_day)


    
    
    common_hour = df['hour'].mode()[0]
    print('most common hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)






def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start_station = df['Start Station'].mode()

    print ("\nmost common start station:\n", common_start_station)

    # display most commonly used end station

    common_end_station = df['End Station'].mode()

    print ("\nmost common end station:\n", common_end_station)


    # display most frequent combination of start station and end station trip

    combined_station = df.groupby(['Start Station', 'End Station']).count()
    
    print ('\nmost common combined station is:', common_start_station, 'and', common_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    int_total_travel_time = int(float(total_travel_time/3600))

    print('Total travel time:', int_total_travel_time, 'hours')


    # display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    int_mean_travel_time = int(float(mean_travel_time/60))

    print('mean travel time:', int_mean_travel_time, 'minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print ('\nCounts of user types:\n', df['User Type'].value_counts())


    # Display counts of gender

    try:
        print ('\nnumbers of gender:\n'), df['Gender'].value_counts()
        
    except KeyError:
        print ('\nthis database has no gender information.')
        


    # Display earliest, most recent, and most common year of birth
    try:
        
        earlist_birth = df['Birth Year'].min()
        int_earlist_birth = int(float(earlist_birth))

        print('\nThe earlist birth year is\n', int_earlist_birth)
    
    except KeyError:
        print ('\nthis database earlist birth information.')
        
    try:

        recent_birth = df['Birth Year'].max()
        int_recent_birth = int(float(recent_birth))
        
        print ('\nThe most recent birth year is\n', int_recent_birth)
    
    except KeyError:
        print ('\nthis database has no recent birth information.')
        
    try:
        common_birth = df['Birth Year'].mean()
        int_common_birth = int(float(common_birth))
        print ('\nThe most common birth year is\n', int_common_birth)
            
    except KeyError:
        ('\nthis database has no common birth information.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def display_raw_data(df):
    
    data_display = input ('would you like to take a look at the first 5 rows of data? yes / no ?').lower()
    start_loc = 0
    pd.set_option('display.max_columns',None)
    
    while True:
        if data_display == 'no':
            break
        print (df[start_loc:start_loc+5])
        data_display = input('would you like to see the next 5 rows? yes / no ?').lower()
        start_loc += 5
    
    
    
    
    
    
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()