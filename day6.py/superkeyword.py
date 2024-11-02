#super() keyword
class a():
    def __init__(self):#if function is not called init wilbe called as default
        print("A")
    def display(self):
        print("a")
class b():
    def __init__(self):
        print("B")
    def disp(self):
        print("b")
class c(a):
    def __init__(self):
        #by using super() the constructor(__init__) will be called from inherited class
        super().__init__()#if function is not called init wilbe called as default
        print("C")
    def disp(self):
        print("c")  
name=c()
