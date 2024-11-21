#hybrid inheritance
class dad():#both the sons are linked to the dad class 
    def money(self):
        print("dads money")
class land():
    def land(self):
        print("his land")
class son1(dad,land):#son can accesss both dad and land class
    def phone(self):
        print("son1 phone")
class son2(dad):
    def tab(self):
        print("son2 tab") 
me=son1()
me.money()        
me.land()
