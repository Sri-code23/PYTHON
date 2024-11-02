#multilevel inheritance
class grandpa():
    def phone(self):
        print("grandpas mobile")
class dad(grandpa):#grandpa cls is linked to dad 
    def money(self):
        print("dads money") 
class son(dad):#dad class is linked to son
    #since grandpa mis linked with dad ,we can also access granpa from son
    def laptop(self):
        print("sons laptop")
ram=son()
ram.phone()                       