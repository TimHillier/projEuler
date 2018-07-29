import calendar
year = 1900
month = 1
sundays = 0

for y in range(1,101):
    for m in range(1,13):
        if(calendar.weekday(year+y,m,1) == 1):
            sundays +=1
print(sundays)
