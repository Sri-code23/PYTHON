"""
import time
import datetime
from calendar import isleap
import pygame


def leap_year(year):
    if isleap(year) is True:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

def timer():
    current_time=datetime.datetime.now().strftime("%Y-%m-%D ----- %H:%M:%S")
    print("-----------------------")
    time.sleep(3)
    print(f"current time: {current_time:50}")
    print("-----------------------")
    print("-----------------------")
    print("-----------------------")
    name=str(input("enter your name : "))
    pygame_check(name)

def pygame_check( name):
    alarm_time=input("enter the time in this format( HH:MM:SS) :")
    time_is_up=True

    while time_is_up:
        tim=datetime.datetime.today().strftime("%H:%M:%S")
        print(f"{tim}")
        print("-----------")
        time.sleep(1)

        if (tim == alarm_time):
            print(f"Times up, {name} !! ")
            music_file="python coding//newlesson.py//streets x one of the girl's x lana.mp3"
            time_is_up=False
            pygame.mixer.init()
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play()


if __name__=="__main__":
    #year=int(input("enter the year :"))
    #leap_year(year)
    #timer()

"""



#2d list
"""

a=["sri","dhart","dvvsfrv"]
b=["vry","vsrv","svfvr"]
c=[30,24,15]
lists=[a,b,c]


for list in lists:
    for element in list:
        print(f"{element:^30}",end=" ")
    print()    

"""

#2d listarray

"""
example_array=[(1,2,3),
               (4,5,6),
               (7,8,9)]

for i in range(0,3):
    for j in range(0,3):
        print(f"{example_array[i][j]:^5}",end="__")
        
    
#print(f"{example_array[1][2]}")
#print()
"""

                






