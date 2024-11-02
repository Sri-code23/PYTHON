#inheritance and polymorpism
class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=20
        b=30
        print(l*b)
obj=rectangle()
obj.area()

