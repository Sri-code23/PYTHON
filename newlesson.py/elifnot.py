#elif not
age=input("enter our age \n (enter 'f' to exit):")
while not (str(age)=="f"):
    if(int(age)==0):
     print("enter properly")
     age=int(input("enter our age :"))
    elif(int(age)>=18):
        print(f"you are eligible")
        break
else:
    print("exited succesfully")
    
    