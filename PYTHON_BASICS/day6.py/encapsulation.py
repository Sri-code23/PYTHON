#encapsulation
#makin the object inaccessible by using __
class company():
    def companyname(self):
        self.__companyname="google"
ob=company()
print(ob.__companyname)