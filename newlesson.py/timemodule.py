import time
#time.sleep(5)
#print("Time up !!")

"""
tim=int(input("start count down: "))
for i in reversed(range(1,tim+1)):
    print(i)
    time.sleep(1)
print("times up!!")
"""

tim=int(input("start count down: "))
for i in range(tim,0,-1):
    print(i)
    time.sleep(1)
print("times up!!") 