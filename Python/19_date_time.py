# import datetime
# print (dir(datetime))

from datetime  import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hr = now.hour
mn = now.minute
sc = now.second

print(day,month,year,hr,mn,sc)