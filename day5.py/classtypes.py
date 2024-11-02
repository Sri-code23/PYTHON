#class variable type
class calci():
    a=10 #adding a common variable inside a class
    def __init__(self,b):
       self.num2=b
    def add(self):
       print("addition")
       print("sum:",self.a+self.num2)
    def sub(self):
       print("subtraction")
       print("diff:",self.a - self.num2)
    def mul(self):
       print("multiplication")
       print("product:",self.a*self.num2)
    def div(self):
       print("division:")
       print("division:",self.a/ self.num2)
inpu=calci(4)
inpu.a=40
inpu.add()
inpu.sub()
inpu.mul()
inpu.div()
