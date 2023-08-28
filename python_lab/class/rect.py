#Q: Compute area of rectangle for given length and breadth using class

class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        print("Area of rectangle =",self.length * self.breadth)

object=rectangle(10,4)
object.area()
