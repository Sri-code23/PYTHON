def balance_r(balance):
    print(f"your balance is {balance:.2f} ")
def deposit():
    amount=float(input("enter the amount to be deposited:"))
    if amount<0:
        print("amount cant be less than '0' ")
        return 0
    elif amount>0:
        return amount
def withdraw(balance):
    amount=float(input("enter the amount you need:"))
    is_con=True
    while is_con:
        if amount>balance:
            print("insufficient balance")

            amount=float(input("enter the amount you need: \n (press '0' to cancel )"))
            if int(amount) == 0:
                print("transaction cancelled by the user")
        elif amount<0:
            print("amount cant be zero")
            amount=float(input("enter the amount you need: \n (press '0' to cancel )"))
            if int(amount) == 0:
                print("transaction cancelled by the user")
        elif amount>0:
            return amount                    
def main(): 
    balance=0   
    is_running=True
    while is_running:
        print("************")
        print("my bank")
        print("************")
        print("1- to check balance")
        print("2- to deposit amount ")
        print("3- to withdraw amount")
        print("4- to exit")
        print("************")

        user_inp=input('enter your choice \n (1/2/3/4): ')
        if user_inp == '1':
            balance_r(balance)
            print("************")
        elif user_inp == '2':
            balance=balance+deposit()
            print("*********************")
            print(f"your current balance is {balance:.2f} ")
            print("************")
        elif user_inp == '3':
            balance-= withdraw(balance)
            print(f"your current balance is {balance:.2f} ")
            print("************")

        elif user_inp == '4':
            print("you exited")
            print("************")
            is_running=False
        else:
            print('enter a valid input')                    
if __name__=="__main__":
    main()                