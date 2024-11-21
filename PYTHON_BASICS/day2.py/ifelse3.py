#ifelif...else
score=float(input("enter your score:"))
if (score<35):
    print("poor student / fail")
elif (score>35) and (score<70):
    print("average student / good")
elif (score>70) and (score<=100):
    print("good student / excellent")
else:
   print("invalid score")