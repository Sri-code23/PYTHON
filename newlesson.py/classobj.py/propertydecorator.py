#property

#getter- to get 
#setter- to set
#deleter - to delete
from turtle import width


class size:
    def circle(self,name,width,height):
        self._name=name
        self._width=width
        self._height=height
    
    @property
    def name(self):                             #we can edit the argument name by using property decorator
        return f"{self._name} $$ "
    
    @property                                           #getter
    def width(self):                                    
        return f"{self._width:.2f}"
    
    @property
    def height(self):
        return f"{self._height:.2f}"
 
    @width.setter                                                     #setter
    def width(self,new_width):          
        if new_width>0:
            self._width=new_width
        else: 
           print( f" width cant be zero"  )

    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._height=new_height
        else: 
           print( f" height cant be zero"  )         

    @width.deleter                                                   #deleter
    def width(self):
        del self._width
        print(f"width has been deleted")



shape=size()
shape.circle("sri",3,4)

#shape.width=9      #@width.setter
del shape.width      #deleting the width


#print(shape.width)
print(shape.height) 
print(shape.name)       