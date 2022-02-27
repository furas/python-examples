import datetime

today = datetime.date.today()
birth = datetime.date(1968, 12, 24)

years  = today.year - birth.year
months = today.month - birth.month
days   = today.day - birth.day

print(years, months, days)

age = years
if (months < 0) or (months == 0 and days < 0):
    age -= 1 
    
print('age:', age)



