import datetime

date=datetime.date(2001,12,23)
today=datetime.date.today()

time=datetime.time(3,40)
now=datetime.datetime.now()

now=now.strftime("day : %H:%M:%S \ntime: %d-%m-%Y ")


#print(date)
#print(today)
#print(time)
print(now)


