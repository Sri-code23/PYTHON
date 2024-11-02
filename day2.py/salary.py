loan=-100 #the -1 can replaced with anythig
while (loan<0):
  
  salary=int(input("enter your salary:"))
  age=int(input("enter your age:"))
  
  if (salary>=20000) or (age<=25):
     loan_amount=float(input("enter the required loan amount:"))
     if (loan_amount<=50000):
        print("you are eligible for loan")
     else:
        print("maximum loan amount is upto 50000")
        loan=-100
  else:
     print("you are eligible")
