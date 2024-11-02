class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print(self.name,self.salary)
class manager(employee):
    def __init__(self,name,salary,dep):
        super().__init__(name,salary)
        self.dep=dep
        print(self.name,self.salary,self.dep) 
obj=manager("sri","2000","ece")
        