a=float(input("mark1"))
b=float(input("mark2"))
c=float(input("mark3"))
d=float(input("mark4"))
e=float(input("mark5"))
sum=a+b+c+d+e
average=sum/5
print("average=",average)
if (average<35):
    print("need class")
else:
    print("good to go")