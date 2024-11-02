class student:
    year=2024
    numof_students=0
    def __init__(self,name,age):
        self.name=name
        self.age=age  
        student.numof_students+=1   # accessing the class variable and updating the value


student1=student("sri",20)
student2=student("hari",40)
student3=student("dain",23)


print(student.year)

print(student.numof_students)