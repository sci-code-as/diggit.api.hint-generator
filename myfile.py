# import datetime
# import calendar 
  
# def findDay(date): 
#     day = datetime.datetime.strptime(date, '%d, %m, %Y').weekday() 
#     return (calendar.day_name[day]) 
  
# # Driver program 

# date = '31, 12, 2020'
# print(findDay(date)) 

import datetime 
import calendar 
  
def findDay(date): 
    day = 2020-12-31 00:00:00
    return (calendar.day_name[day]) 
  
# Driver program 
date = '31 12 2020'
print(findDay(date)) 