import random

a=int(input("enter the lowest number:"))
b=int(input("enter the highest number:"))
answer=random.randint(a,b)
condn=True
guesses=0
while condn:
    guess=input("guess the number:")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if a<=guess<=b:
            if(guess<answer):
                print("too low")
            elif(guess>answer):
                print("Too high!!")
            else:
                print("the number is correct")
                print(f"number of guesses took is : {guesses}")
                condn=False
    else:
        print("invalid input")
    
