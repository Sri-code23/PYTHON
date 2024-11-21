#mini calculator
a=float(input("number-1:"))
b=float(input("number-2:"))
print("type the operation code  \n for addition==type 1 \n for subtraction==type 2 \n for multiplication==type 3 \n for division==type 4" )
code=float(input("enter the code:"))
if (code==1):
    print("the sum is:",a+b)
elif (code==2):
    print("the diff is:",a-b)
elif (code==3):
    print("the product is:",a*b)
elif (code==4):
    print("the remainder is :",int(a%b))
else:
    print("invalid code \n please enter a valid code")



