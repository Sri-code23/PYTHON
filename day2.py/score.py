#score =-2 is decided by seeing the number used for a condition
#here elif uses this condition
score=-2
while (0>score) or (score>100):
    score=int(input("enter your score out of 100 \n dont include '%' symbol:"))
    if (score>=70) and (score<=100):
        name=input("enter your name:")
        department=input("enter your department:")
        location=input("enter yor location:")
        print("you are eligible")
    elif (score<0) or (score>100):
        print("enter a valid number")
     #determining the value of the score as -1 to send it again to the while loop
        score=-2
        #if the score satisfies the elif condition
        #the score value will be assume as -2(any number)
        #the number should be same as the value used for while condition
    else:
        print("you are not eligible")