class teacher:
    def __init__(self,n,moo):
        self.name=n
        self.reg=moo
    def display(self):
        print("name:",self.name) 
        print("reg:",self.reg)
s1=teacher("sri","120")
print(s1.name)
s1.display()
