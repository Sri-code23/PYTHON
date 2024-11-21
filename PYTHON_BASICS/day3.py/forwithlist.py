#get 5 inputs and print its sum and average
a=[]
for i in range(5):
    num=int(input("enter number"+str(i+1)+":"))
    a.append(num)
print("the given nos:")
sum=0
for j in a:
    sum=sum+j
print("sum of the numbers is:",sum)
average=sum/5
print("average :",average)