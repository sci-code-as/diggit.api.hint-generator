import datetime
import calendar

def find_day(date):
    #day = datetime.datetime.strptime(date, '%d %m %Y')
    weekday = day.weekday()
    return calendar.day_name[weekday]

date = '31 12 2020'
print(find_day(date))