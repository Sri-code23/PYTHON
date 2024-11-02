class person():
    def __init__(self,name):
        self.name=name
        print("name:",self.name)
class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
        print("grade:",self.grade)
        print("name:",self.name)
obj=student("sri","a")
        