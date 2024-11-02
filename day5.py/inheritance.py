#inheritance (accessing one or more class functions)
class dad():
    def phone(self):
        print("dads mobile")
class mom():
    def sweet(self):
        print("moms sweet")
class son(mom,dad):#accessing  both dad and moms class
    def laptop (self):
        print("sons laptop")
me=son()
me.sweet()   
me.phone()             