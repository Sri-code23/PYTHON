class calculator():
    def __init__(self,a,b):
       self.num1=a
       self.num2=b
    def add(self):
       print("addition")
       print("sum:",self.num1 + self.num2)
    def sub(self):
       print("subtraction")
       print("diff:",self.num1 - self.num2)
    def mul(self):
       print("multiplication")
       print("product:",self.num1 *self.num2)
    def div(self):
       print("division:")
       print("division:",self.num1 / self.num2)
inpu=calculator(20,4)
inpu.add()
inpu.sub()
inpu.mul()
inpu.div()
