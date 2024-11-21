#instance method 
class clss():
#variable used directly inside the class is called class variable
    school="sjms"
#if self is used ,this method is called instance method
    def __init__(self,a,b):
        self.name=a
        self.roll=b
    def nameroll(self):
        print("name:",self.name)
        print("roll:",self.roll)
    @classmethod 
#this helps to avoid using the class argument in line 18
    def change(cls):
#changing the lass variable school, from "sjms" to "aeri"
        cls.school="aeri"
        print("went to college")
    @staticmethod 
#by using static method ,we dont  need mention self as argument       
    def attendance():
        print("present")
room=clss("sri","12")
room.nameroll()
clss.change()
room.attendance()