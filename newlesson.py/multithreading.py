#multithreading - to start all the functions at a same time

import threading
import time

def eat(food):
    time.sleep(6)
    print(f"you ate { food}")

def exercise():
    time.sleep(4)
    print(f"you finished exercising ")

def depart():
    time.sleep(2)
    print(f'you went to school')

 # if the function is involved with argumnets  the use args=("noodles",)
chore1=threading.Thread(target=eat,args=("noodles",)) 
chore1.start()
chore2=threading.Thread(target=exercise)
chore2.start()
chore3=threading.Thread(target=depart)
chore3.start()

chore1.join()         #by using join() , the print("you fin....") works after the threading is completed
chore2.join()
chore3.join()
time.sleep(3)
print("you finished your job  ") 
