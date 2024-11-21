class laptop:
    def spec(self): #self takes the object name as input
       ram=""
       processor=""
       print("ram:",self.ram)
    def display(self):
       quality=""
       print("diplay:",self.quality)
hp=laptop()
hp.ram="16gb"
hp.spec()
dell=laptop()
dell.quality="8k"
dell.display()