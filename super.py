#super()= funtion used to give acess to the methord of a parent class.
#           returns a temporary object of a parent class when used 

class Rectangle:
    def __init__(self , x , y):
        self.x =x 
        self.y = y

class Square(Rectangle):
    def __init__(self , x , y):
       super().__init__(x,y)
    def area (self):
        return self.x*self.y 

class Cube(Rectangle):
    def __init__(self , x, y ,z):
        super().__init__(x,y) 
        self.z = z
    def volume(self):
        return self.x*self.y*self.z
    
square = Square(3,3)
cube = Cube(3,3,3) 
print (square.area())
print (cube.volume())