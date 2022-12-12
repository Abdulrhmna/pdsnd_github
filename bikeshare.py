import time
import pandas as pd
import numpy as np


def get_filters():
     """
    Asking user to select city and month.
    
    Returns:
        (str) Selected_city - name of the city to analyze which entered by user
        (str) month - name of the month to filter by, or "all" to apply no month filter
     """
<<<<<<< HEAD
#d3
=======
>>>>>>> documentation

     list_of_cites ='w','c','n' #To control the input
     List_of_month= '1','2','3','4','5','6','7','8','9','10','12','11','all'#To control the input
     selected_city='' 
     month=''
     days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all' ]


     while True:
        selected_city = str(input('which city you ask about (c=chicago , w= washington , n = new_york): ').lower())
        if selected_city in list_of_cites:#check  if the entered city is okay
              break  
        else:
            print('Please Check The Avilable City...')
            #print('which city you ask about (c=chicago , w= washington , n = new_york): ')



     while True:
        month = str(input('Kindly enter the number of month Or ALL for all monthes: ').lower())
        if month in List_of_month:#check  if the entered month is okay
              break
        else:
            print('Please Check The Avilable City...')
            #print('Kindly enter the number of month Or ALL for all monthes: ')

     while True:
        day = str(input( 'Kindly enter the name of day (tuesday, thursday) Or ALL for all days: ').lower())
        if day in days:#check  if the entered month is okay
              break
        else:
            print('Please Check The Avilable City...')       
       

     return selected_city,month,day


def load_data(cities,months,day):
    """
    Preparing the data based on the entered value.

    inputs:
        (str) cities - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
    Returns:
        (DataFrame) my_new_data - data after aplling the entered filters
    """ 

    List_Of_Cities_DATA = {"c": "chicago.csv", "w": "washington.csv", "n": "new_york_city.csv"}#the files working on it
    my_data = pd.read_csv(".//"+List_Of_Cities_DATA[cities])
    my_new_data=None
    my_data['Start Time'] = pd.to_datetime(my_data['Start Time'])#transfered the type to time
    my_data['End Time'] = pd.to_datetime(my_data['End Time'])#transfered the type to time
    my_data['new_dou'] = (my_data['End Time'] - my_data['Start Time']).dt.total_seconds().astype(int)#finding the correct duration, becasue there are some "Trip Duration" have wrong value
    my_data['full_trip'] = 'Start: '+my_data['Start Station']+', End: '+my_data['Start Station']#finding full path
    my_data['month'] = my_data['Start Time'].dt.month
    my_data['day_of_week1'] = my_data['Start Time'].dt.strftime('%A')
    if months == 'all':#filter the Data freambeased on the entered month
        my_new_data=my_data
    else:
        my_new_data=my_data[my_data['month']==int(months)]
        

    if day == 'all':#filter the Data freambeased on the entered day
        my_new_data=my_data
    else:
        my_new_data=my_data[my_data['day_of_week1'] ==day.title()]
        
    return my_new_data


def popular_times(data,month):

      if month=='all':#finding the common month if the user enter "all"
          data['month'] = data['Start Time'].dt.month
          print('most common month is : '+str(data['month'].mode()[0]))
      else:
          print('There are no common month because your selected one month!!')
      data['day_of_week'] = data['Start Time'].dt.strftime('%A')#extract name if day in new colomn
      
      data['hour'] = data['Start Time'].dt.hour#extract hours in new colomn
    


      print('most common hour of day: '+str(data['hour'].mode()[0]))
      print('most common day of week: '+str(data['day_of_week'].mode()[0]))
   

def user_stats(data,city):

     if city =='w':
        print('User info:')
        print('count of each user type:')
        print(data['User Type'].value_counts(ascending=False))
        print('There is no gender information n W')
     else:
        print('User info:')
        print('count of each user type:')
        print(data['User Type'].value_counts(ascending=False))
        print(data['Gender'].value_counts(ascending=False))

def station_stats(data):
     """
      Solving #2 Popular stations and trip
      inputs:
        (DataFrame) Data - data after aplling the entered filters

     """
     print('-'*40) 
     print('#2 Popular stations and trip')
     print('most common start station: '+str(data['Start Station'].mode()[0]))
     print('most common end station: '+str(data['End Station'].mode()[0]))
     print('most common trip from start to end: '+str(data['full_trip'].mode()[0]))
     print('-'*40)

def trip_duration_stats(data):
    """
      Solving #3 Trip duration
      inputs:
        (DataFrame) Data - data after aplling the entered filters
    """
    Time_in_sec = data['new_dou'].sum().astype(int)
    Time_in_sec = data['new_dou'].sum().astype(int)
    day = Time_in_sec // (24 * 3600)
    hour = Time_in_sec // 3600
    minutes = Time_in_sec // 60

    print('-'*40)
    print('#3 Trip duration')
    print('total travel time in Day: '+str(day)+', in Hours: '+str(hour)+', in Minutes: ' +str(minutes)+', Sec: '+str(Time_in_sec))
    print('average travel time: '+str(round(data['new_dou'].mean())))
    print('-'*40)

def user_stats(data,city):
     """
      Solving #4 User info
      inputs:
        (DataFrame) Data - data after aplling the entered filters
     """
     if city =='w':
        print('User info:')
        print('count of each user type:')
        print(data['User Type'].value_counts(ascending=False))
        print('There is no gender and Birth Year information in this city W')
     else:
        print('User info:')
        print('count of each user type:')
        print(data['User Type'].value_counts(ascending=False))
        print(data['Gender'].value_counts(ascending=False))
        print('earliest year of birth '+str(round(data['Birth Year']).min().astype(int)))
        print('most recent year of birth '+str(round(data['Birth Year']).max().astype(int)))
        print('most common year of birth '+str(round(data['Birth Year']).mode()[0].astype(int)))
        



def main():

    
    while True:
        
        S_City,S_Month,S_day= get_filters()
        Final_Data=load_data(S_City,S_Month,S_day)
        popular_times(Final_Data,S_Month)
        station_stats(Final_Data)
        trip_duration_stats(Final_Data)
        user_stats(Final_Data,S_City)
        counter=0
        while True:
             if Final_Data.index.max()>counter:
                 view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no')
                 if view_data=='yes':
                    newcount=counter+5
                    print(Final_Data.iloc[counter: newcount] )
                    counter=+5
                 elif view_data=='no':
                    break
                 else: 
                    print('the entered value suold yes or no!!')
             else:
                break
             counter=+5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
