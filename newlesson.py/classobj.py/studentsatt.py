class register:
    def __init__(self,name,age,dep,grade):
        self.name=name
        self.age=age
        self.dep=dep
        self.grade=grade
    def attendance(self,name):
        print(f"{name} is present today")
    def performance(self,name):
        print(f" {name} performs well")
