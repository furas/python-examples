# Two methods to get new date
#  1. after 90 days
#  2. after 3 months
 
#---------------------------------------------------------------
# 1. after 90 days
#---------------------------------------------------------------
 
import datetime
 
range_90_days = datetime.timedelta(days=90)
 
date1 = datetime.datetime.strptime('09.10.2016', "%d.%m.%Y")
date2 = date1 + range_90_days
date3 = date2 + range_90_days
date4 = date3 + range_90_days
 
print(date1.strftime("%d.%m.%Y"))
print(date2.strftime("%d.%m.%Y"))
print(date3.strftime("%d.%m.%Y"))
print(date4.strftime("%d.%m.%Y"))
print('-----')
 
# dates have different day because month has 28/29, 30 or 31 days
# 09.10.2016
# 07.01.2017
# 07.04.2017
# 06.07.2017
 
#---------------------------------------------------------------
# 2. after 3 months
#---------------------------------------------------------------
 
import datetime
 
date1 = datetime.datetime.strptime('09.10.2016', "%d.%m.%Y")
 
year = date1.year
month = date1.month
month += 3
if month > 12:
    month -= 12
    year += 1
 
date2 = date1.replace(month=month, year=year)
 
year = date2.year
month = date2.month
month += 3
if month > 12:
    month -= 12
    year += 1
 
date3 = date2.replace(month=month, year=year)
 
year = date3.year
month = date3.month
month += 3
if month > 12:
    month -= 12
    year += 1
 
date4 = date3.replace(month=month, year=year)
 
print(date1.strftime("%d.%m.%Y"))
print(date2.strftime("%d.%m.%Y"))
print(date3.strftime("%d.%m.%Y"))
print(date4.strftime("%d.%m.%Y"))
print('-----')
 
# dates have the same day
# 09.10.2016
# 09.01.2017
# 09.04.2017
# 09.07.2017
