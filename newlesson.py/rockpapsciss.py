import random
option=("rock","paper","scissor")
condn=True
player=None
playa=True
while playa:
    computer=random.choice(option)
    while condn:
        player=input("choose \n (rock/paper/scissor) :").lower()
        print(f"player:{player}")
        print(f"computer:{computer}")
        if player not in option:
            print("invalid input!!")
        elif(player==computer):
            print("its a TIE!!")
            condn=False
        elif(player=="rock") and (computer=="scissor"):        
            print("YOU WIN")
        elif(player=="paper") and (computer=="rock"):        
            print("YOU WIN")
        elif(player=="scissor") and (computer=="paper"):        
            print("YOU WIN")
        else:       
            print("YOU LOSE")
            condn=False
    play_again=input("do you want to play again(yes/no):").lower()
    if(play_again=="yes" or play_again=="no"):
        if (play_again=="yes"):
            condn=True
        else:
            playa=False
    else:
        print("invalid")        
print("THANK YOU FOR PLAYING")            