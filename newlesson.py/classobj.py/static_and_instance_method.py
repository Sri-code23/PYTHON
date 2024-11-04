class employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def get_info(self):                     #instance method
        return f"{self.name} : {self.position}"
    
     
    @staticmethod                     #static method we can access clas methods without the object name
    def is_valid(position):
        name="srod" 
        positions=["cook","manager","director","watchman"]
        print(f"{name}")
        return position in positions

print(employee.is_valid("cook"))

#
employee1=employee("sri","designer")    #instance method is accessed by first declaring the object name
print(employee1.get_info())