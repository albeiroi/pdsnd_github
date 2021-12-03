import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    city = ''
    month = ''
    day = ''
    cityUserInput= " "
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cityUserInput = input('chicago 1, new york city 2, washington 3').lower()
    while cityUserInput not in CITY_DATA:
        print("That city is not in our menu")
        cityUserInput = input('chicago 1, new york city 2, washington 3')

    if cityUserInput == "chicago":
        city = 'chicago'
    elif cityUserInput == "new york":
        city = 'new york'
    elif cityUserInput == "washington":
        city = 'washington'


    monthUserInput = input('please type a month according to the menu 1 January, 2 February, 3 March, 4 April, 5 May, 6 June').lower()
    while monthUserInput not in months:
        print("we have only months until June, ")
        monthUserInput = input(' so please type months from January to June ')

    if monthUserInput == "january":
        month = 'january'
    elif monthUserInput == "february":
        month = 'february'
    elif monthUserInput == "march":
        month = 'march'
    elif monthUserInput == "april":
        month = 'april'
    elif monthUserInput == "may":
        month = 'may'
    elif monthUserInput == "june":
        month = 'june'


    dayUserInput = input('please type the name of the day 1 Monday, 2 Tuesday, 3 Wednesday, 4 Thursday, 5 friday, 6 saturday, 7 sunday').lower()
    while dayUserInput not in weekdays:
        print("we have only week days")
        dayUserInput = input(' so please type the week day from Monday to Sunday')

    if dayUserInput == "monday":
        day = 'monday'
    elif dayUserInput == "tuesday":
        day = 'tuesday'
    elif dayUserInput == "wednesday":
        day = 'wednesday'
    elif dayUserInput == "thursday":
        day = 'thursday'
    elif dayUserInput == "friday":
        day = 'friday'
    elif dayUserInput == "saturday":
        day = 'saturday'
    elif dayUserInput == "sunday":
        day = 'sunday'




       # option = input ('to continue select 1, to exit select 0')
    print('-'*40)
    return city, month, day

    def load_data(city, month, day):
        """ from column 'Start Time' we extract the information corresponding to month and day of the week, and to be able to cross it with the city"""
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

        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()

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
        """ from the new columns month, day of the week and time we can filter the most common uses of each of the supplied variables"""

        """Displays statistics on the most frequent times of travel."""

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # TO DO: display the most common month
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month from the Start Time column to create an month column
        df['month'] = df['Start Time'].dt.month

        # find the most common month (from 1 to 6)
        popular_month = df['month'].mode()[0]

        print('The most commnon month to travel is : ',popular_month)




        # TO DO: display the most common day of week



        # extract hour from the Start Time column to create an hour column
        df['day'] = df['Start Time'].dt.day

        # find the most common day
        popular_day = df['day'].mode()[0]

        print('The most commnon day to travel is : ',popular_day)



        # TO DO: display the most common start hour


        df['hour'] = df['Start Time'].dt.hour
        #df['hour'] = df['Start Time'].dt.hour

        # find the most popular hour
        popular_hour = df['hour'].mode()

        print('Most Popular Start Hour:', popular_hour)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)



    def station_stats(df):
        """ from the analysis of the variables Start Station and End Station  we can filter and know which are the most used individually and in combination."""

        """Displays statistics on the most popular stations and trip."""

        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # TO DO: display most commonly used start station
        most_common_start_station = df['Start Station'].mode()[0]

        print('The most commonly used start station is: ',most_common_start_station)


        # TO DO: display most commonly used end station
        most_common_end_station = df['End Station'].mode()[0]

        print('The most commonly used end station is: ',most_common_end_station)


        # TO DO: display most frequent combination of start station and end station trip
        most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]

        print("The most frequent combination of used start station and end station is:", most_common_start_end_station[0],'-',most_common_start_end_station[1])


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)



    def trip_duration_stats(df):
        """ from the analysis of the variable Trip Duration we can filter and know what the total time and average is"""

        """Displays statistics on the total and average trip duration."""

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO: display total travel time
        total_travel_time = df['Trip Duration'].sum()
        print("Total travel time :", total_travel_time)


        # TO DO: display mean travel time
        mean_travel_time = df['Trip Duration'].mean()
        print("Mean travel time :", mean_travel_time)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)



    def user_stats(df):
        """ by analyzing the variables User Type, Gender and Birth Year we can extract information about the type of user, gender, date of birth, etc."""

        """Displays statistics on bikeshare users."""

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        user_counts_types = df['User Type'].value_counts()

        print("Counts of user types:\n",user_counts_types)

        try:
            # TO DO: Display counts of gender
            gender_counts = df['Gender'].value_counts()

            print("Counts of gender:\n",gender_counts)


            # TO DO: Display earliest, most recent, and most common year of birth
            birth_year = df['Birth Year']

            # the most common birth year
            most_common_birth_year = df['Birth Year'].mode()[0]
            print("The most common birth year:", most_common_birth_year)

            # the most recent birth year
            most_recent_birth_year = df['Birth Year'].max()
            print("The most recent birth year:", most_recent_birth_year)

            # the most earliest birth year
            most_earliest_birth_year = df['Birth Year'].min()
            print("The most earliest birth year:", most_earliest_birth_year)


            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
        except KeyError:
            print("Sorry,Gender and Birth Year columns are not for this city ")


    def rows(df):
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        keep_asking = True
        while (keep_asking):
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            view_display = input("Do you wish to continue?: yes or no").lower()
            if view_display =="no":
                keep_asking = False

                def main():
                while True:
                    city, month, day = get_filters()
                    df = load_data(city, month, day)

                    time_stats(df)
                    station_stats(df)
                    trip_duration_stats(df)
                    user_stats(df)
                    rows(df)

                    restart = input('\nWould you like to restart? Enter yes or no.\n')
                    if restart.lower() != 'yes':
                        break


            if __name__ == "__main__":
            	main()
            
