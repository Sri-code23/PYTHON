class Book:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):                              #returns the string 
        return f"{self.name}'s age is {self.age}" 

    def __eq__(self,other):                         #return the boolean(true/false) based on the condition
        return self.name==other.name 
 
    def __lt__(self,other):                         #checks the lower than codition 
        return self.age < other.age

    def __gt__(self,other):                         #checks the greater than codition 
        return self.age > other.age           

    def __add__(self,other):                        #adds the values
        return self.age + other.age   
    
    def __contains__(self,k):                       #checks whether the given key is in class
        return k in self.name 
    
    def __getitem__(self,key):                      #return the item of the given key
        if key == "name":
            return self.name
        elif key == "age":
            return self.age

student1=Book("sri",20)
student2=Book("minu",5)
student3=Book("dravid",35)

#print(student1)                  __str__

#print(student1==student2)        __eq__

#print(student1< student2)        __lt__  

#print(student1 > student2)       __gt__

#print(student1+student3)         __add__

#print("sri" in student2)          __contains__

#print(student1["name"])            __getitem__