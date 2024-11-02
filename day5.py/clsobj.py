class maths:
    def add(self):
      print("addition")
      print("sum:",a+b)

    def sub(self):
      print("subtraction")
      print("diff:",a-b)

    def mul(self):
      print("multiplication")
      print("product:",a*b)

    def div(self):
      print("division:")
      print("division:",a/b)
calci = maths() #to link class with object called (calci)
a=int(input("enter a :"))
b=int(input("enter b:"))
calci.add() #to call the function called add() from class