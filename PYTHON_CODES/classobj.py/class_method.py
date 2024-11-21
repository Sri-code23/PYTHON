
class student:
    count=0
    name="sri"
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        student.count+=1
    def get_info(self):
        print(f" name:{self.name}")
        
      
    @classmethod              #this class meythod has access to the class variables like count inthe program 
    def get_count(cls):       #in class method we use cls instead of self
        print(f"total count: {cls.count}")
        print(f"name: {cls.name}")

st1=student("sri","A")
st2=student("den","C")
st3=student("mark","B")


student.get_count()