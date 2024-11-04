import datetime

target_time=datetime.datetime(2030,2,23,12,12,23)
current_time=datetime.datetime.now()

if target_time<current_time:
    print("you are late")
else:
    print("you are early")
    