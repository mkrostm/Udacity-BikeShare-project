# -*- coding: utf-8 -*-
"""

@author: Mohamed Kamel 
"""

import time
import datetime
import pandas as pd


CITY_DATA = { 'chicago': 'Data/chicago.csv',
              'new york city': 'Data/new_york_city.csv',
              'washington': 'Data/washington.csv' }
months =['january','february','march','april','may','june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    months_abbreviation ={'jan':'january','feb':'february','mar':'march','apr':'april','may':'may','jun':'june'}
    days_abbreviation ={'sun':'sunday','mon':'monday','tu':'tuesday','wed':'wednesday','thu':'thursday','fri':'friday','sat':'saturday'}
    

    print('\n Hello! Let\'s explore some US bikeshare data!')
    # ask user to choose city
    selected_city = input('\n please select city to show \n \n Type letter a or b or c  \n \n Letter (a) for Chicago \n Letter (b) for New York City \n Letter (c) for Washington  \n\n').lower()
           
    while selected_city not in ['a','b','c'] :
        
        #Showing wrong choice message to the user and ask again type the correct letter
        print('\n Wrong choice \n')
        selected_city = input('\n please select city to show \n \n Type letter a or b or c  \n \n Letter (a) for Chicago \n Letter (b) for New York City \n Letter (c) for Washington  \n\n').lower()
    #
    if selected_city == 'a' :
        city = 'chicago'
        print('Your choice is {}'.format(city))
    elif selected_city == 'b':
        city = 'new york city'
        print('Your choice is {}'.format(city))
    elif selected_city == 'c':
        city = 'washington'
        print('Your choice is {}'.format(city))
    #ask user to choose filter by month ,day , both day and month or no filter and put the result in time_frame var
    time_frame = input('\n Would you like to filter {}\'s data by month, day, both, or not at all? type month or day or both or none: \n'.format(city.title())).lower()
    # if user type wrong filter word, ask him again to type the filter
    while time_frame not in ['month' , 'day' , 'both' , 'none'] :
        print('\n Wrong choice \n')
        time_frame = input('\n\n Would you like to filter {}\'s data by month, day, both, or not at all? \n type month or day or both or none: \n'.format(city.title())).lower()
    # filter by all 6 months
    if time_frame == 'none' :
        month ='all'
        day ='all'
        print('Your choice is all 6 months.')
    # filter by month
    elif time_frame == 'month':
        # ask user to choose month in put it in selected_month var
        selected_month = input('Which month ? \n type jan,feb,mar,apr,may,jun \n').lower()
        # while user type wrong word ask him again to type month
        while selected_month not in months_abbreviation:
            print('\n wrong choice \n')
            selected_month = input('Which month ? \n type jan,feb,mar,apr,may,jun \n').lower()
        # get the month name from months_abbreviation  dict and set day to all
        month = months_abbreviation.get(selected_month)
        day ='all'
        print('Your choice is {}'.format(month))
    # filter by day 
    elif time_frame == 'day':
        # ask user to choose day in put it in selected_day var
        selected_day = input('\n Which day ? \n type sun,mon,tu,wed,thu,fri or sat \n').lower()
        # while user type wrong word ask him again to type day
        while selected_day not in days_abbreviation:
            print('\n wrong choice \n')
            selected_day = input('Which day ? \n type sun,mon,tu,wed,thu,fri or sat \n').lower()
        # get the day name from days_abbreviation  dict and set month to all
        day = days_abbreviation.get(selected_day)
        month= 'all'
        print('Your choice is {}'.format(day))
    # filter by month and day
    elif time_frame == 'both':
        # ask user to choose month in put it in selected_month var
        selected_month = input('Which month ? \n type jan,feb,mar,apr,may,jun \n').lower()
        # while user type wrong word ask him again to type month
        while selected_month not in months_abbreviation:
            print('\n wrong choice \n')
            selected_month = input('Which month ? \n type jan,feb,mar,apr,may,jun \n').lower()
        # get the month name from months_abbreviation  dict and set day to all
        month = months_abbreviation.get(selected_month)
        # ask user to choose day in put it in selected_day var
        selected_day = input('\n Which day ? \n type sun,mon,tu,wed,thu,fri or sat \n').lower()
        # while user type wrong word ask him again to type day
        while selected_day not in days_abbreviation:
            print('\n wrong choice \n')
            selected_day = input('Which day ? \n type sun,mon,tu,wed,thu,fri or sat \n').lower()
        day = days_abbreviation.get(selected_day)
               
    print('Your choice : month: {} , day: {} and city: {}'.format(month,day,city))
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
    df = pd.read_csv(CITY_DATA.get(city))
    # convert start time column to datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # add column month extract form start time column
    df['month'] = df['Start Time'].dt.month
    # add column day_of_week from start time column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # add hour column from start time column
    df['hour'] = df['Start Time'].dt.hour
    # add trip column  from combination of start station and end statinon
    df['Trip']= df['Start Station'] + ' - ' + df['End Station']
    
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]   
    return df
def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    """
    print('-'*60)
    print('|' + ' '*58 + '|' )
    print('|      Calculating The Most Frequent Times of Travel.      |')
    print('|' + ' '*58 + '|' )
    print('|'+'-'*59)

    start_time = time.time()

    # display the most common month
    popular_month= df['month'].mode()[0]
    popular_month= months[popular_month -1] 
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('| Popular start hour is : {}'.format(popular_hour))
    print('| Popular month is : {}'.format(popular_month))
    print('| Popular day of the week is : {}'.format(popular_day))
    print("| \n| This took %s seconds." % (time.time() - start_time))
    print('-'*60)

def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    """
    print('-'*60)
    print('|' + ' '*58 + '|' )
    print('|     Calculating The Most Popular Stations and Trip..     |')
    print('|' + ' '*58 + '|' )
    print('-'*60)
    
    start_time = time.time()

    # display most commonly used start station
    most_commonly_start_station = df['Start Station'].mode()[0]
    print('most commonly used start station : {}'.format(most_commonly_start_station))

    # display most commonly used end station
    most_commonly_end_station = df['End Station'].mode()[0]
    print('most commonly used End station : {}'.format(most_commonly_end_station))

    # display most frequent combination of start station and end station trip
    most_frequent_trip = df['Trip'].mode()[0]
    print('Most common trip from start to end  : {}'.format(most_frequent_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)

def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    """
    print('-'*60)
    print('|' + ' '*58 + '|' )
    print('|               Calculating Trip Duration...               |')
    print('|' + ' '*58 + '|' )
    print('-'*60)
    start_time = time.time()

    # display total travel time
    total__travel_time = df['Trip Duration'].sum()
    print('total travel time in seconds : {}'.format(total__travel_time))
    print('total travel time in Format Days, H:M:S > {}'.format(datetime.timedelta(seconds=float(total__travel_time))))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time in seconds : {}'.format(mean_travel_time))
    print('mean travel time in in Format Days, H:M:S > {}'.format(datetime.timedelta(seconds=float(mean_travel_time))))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """
    Displays statistics on bikeshare users.
    
    """
    print('-'*60)
    print('|' + ' '*58 + '|' )
    print('|                  Calculating User Stats                  |')
    print('|' + ' '*58 + '|' )
    print('-'*60)
    
    start_time = time.time()

    # Display counts of user types
    user_types =df['User Type'].value_counts()
    print('counts of user types  :\n{}'.format(user_types))
    print(' '*25 + '-'*10 +' '*25)

    # if selected city washington show message some state not available
    if city == 'washington' :
        print('Sorry, gender counts,earliest, most recent,\n and most common year of birth  are not available for washington')
    else:
        # Display counts of gender
        count_of_gender = df['Gender'].value_counts()
        print('Gender count  :\n{}'.format(count_of_gender))
        print(' '*25 + '-'*10 +' '*25)
        
        # Display earliest, most recent, and most common year of birth
        earlist_year = df['Birth Year'].min()       
        Most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('Earliest year of birth: {}'.format(int(earlist_year)))
        print('Most recent year  of birth: {}'.format(int(Most_recent_year)))
        print('Most common year of birth: {}'.format(int(most_common_year)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
def display_raw_data(city):
    """ 
    
    prompt the user whether they would like to see the raw data. If the user answers 'yes' 
    print 5 rows of the data at a time, then ask the user if want to see 5 more rows of row data
    Args:
        (str) city - name of the city to show raw data

    """
    display_raw =input('would you like to see raw data ? type yes or no : \n').lower()
    try:
        while display_raw == 'yes':
            for chunk in pd.read_csv(CITY_DATA[city], chunksize = 5):
                print(chunk)
                display_raw = input('Would you like to view more 5 rows? Type "Yes" or "No": \n').lower()
                if display_raw != 'yes':
                    print('Thank you')
                    break
            
    except KeyboardInterrupt:
        print('Thank you For your time')
    
def main():
    while True:
        
        city, month, day = get_filters()        
        load_data(city, month,day)
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
 	main()
