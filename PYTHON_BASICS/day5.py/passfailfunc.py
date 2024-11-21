def passfail():
    mark=int(input("enter your mark:"))
    if (mark<40):
        print("you failed")
    elif ((mark>=40) and (mark<=100)):
        print("you passed")
passfail()