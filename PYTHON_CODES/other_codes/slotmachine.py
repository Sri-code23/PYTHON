import random
#from time import sleep
def get_random():
    symbols=['❤','🎈','🎁','🧨','🏈']
    luck=[]
    for _ in range(3):
        luck.append(random.choice(symbols))
    return luck

def print_row(row):
    print("————————————")
    print(" | ".join(row))
    print("————————————")
def payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='❤':
            return bet*2
        if row[0]=='🎈':
            return bet*5
        if row[0]=='🎁':
            return bet*10
        if row[0]=='🧨':
            return bet*20
        if row[0]=='🏈':
            return bet*50
    else:
        return 0
def main():
    balance=100
    print("————————————————————————")
    print("welome to jackpot")
    print("————————————————————————")
    while balance>0:
       bet=input("enter your bet amount:")
       if not bet.isdigit():
          print("enter a valid amount !!")
          continue
       else:
            bet=int(bet)
            if bet<=0:
                print("the bet amount should be atleast one 👻")
                continue
            if bet> balance:
                print("insufficient funds 👻 ")
                continue
       balance-=bet
       print("————————————————————————")
       print(f"your current balance ${balance}")
       print("————————————————————————")
       print("spinning....") 
       #sleep(2)
       row=get_random()
       print_row(row)
       l=payout(row,bet)
       if l>0:
           balance+=l
           print(f"you won 🤑 ${l}")
           print(f"your balance is:${balance}")
           print("————————————————————————")
           i=input("do you want to play again ?? (Y/N): ").upper()
           if not i=='Y':
               print("thank you for playing !!")
               break
           else:
               continue
    else:
        print("————————————————————————")
        print("you don't have enough balance🥺 \n re-run the program ")           
        print("————————————————————————")
if __name__=='__main__':
    main()
