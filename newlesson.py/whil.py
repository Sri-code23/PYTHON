#while loop 
name=input("enter your name:")
age=input("enter your age:")
while name=="" or age=="" :
    print(f" name or age cannot be left empty")
    name=input("enter your name:")
    age=input("enter your age:")
else:
    name=str(name)
    age=int(age)
    while len(name)>10:
         print(f"the name should contain only 10 characters")
         name=input("enter your name:")
         break
    if(age<=18):
        print("you are not eligible , because you are a minor")

    else:
        print(f"hello:{name}")
        print(f"your age:{age}")   