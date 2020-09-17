import calendar
import datetime

month, date, year = map(int, input().split(" "))

d = calendar.weekday(year, month, date)
print(calendar.day_name[d].upper())

