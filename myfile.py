from datetime import datetime
import calendar 
  
def findDay(date): 
    day = datetime.strptime(date, '%B %d, %Y').weekday() 
    return (calendar.day_name[day]) 
  
# Driver program 
date = 'July 26, 2016'
# date = '31 12 2020'
print(findDay(date)) 

