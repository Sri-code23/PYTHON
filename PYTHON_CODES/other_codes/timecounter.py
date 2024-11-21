import time
n=int(input("enter the timer:"))
for i in range(n,0,-1):
    second=i%60
    minutes=int(i/60)%60
    hours=int(i/3600)
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)
print("times up!!")