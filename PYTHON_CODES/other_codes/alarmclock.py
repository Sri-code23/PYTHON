import pygame
import datetime
import time


try:
    def set_alarm(alarm_time):
        print(F"alar is set for {alarm_time} ")
        music_file="newlesson.py\\streets x one of the girl's x lana.mp3"
        is_running=True

        while is_running:
            current_time=datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            time.sleep(1)
            if alarm_time==current_time:

                pygame.mixer.init()               #song equaliser
                pygame.mixer.music.load(music_file) #loading music
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    time.sleep(1)

                print("time's up !!!😑😑")
                is_running=False


    if __name__=="__main__":
        alarm_time=input("enter the alarm time(HH:MM:SS):")
        set_alarm(alarm_time)
        
#

except ModuleNotFoundError:
    print("module is not available")