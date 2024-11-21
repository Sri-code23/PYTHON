#count no of even no
a=int(input("enter a num:"))
b=int(input("enter a num:"))
count=0
for i in range(a,b+1):
    if (i%2==0):
        count=count+1
print(count)        