from shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius:float=1.0, color:str='red', filled:bool=True): 
        self.radius = radius
        self.setColor(color)
        self.setFilled(filled)

    def getRadius(self):
        return self.radius

    def setRadius(self, radius:float):
        self.radius = radius

    def getPerimeter(self):
        return math.pi * 2 * self.radius
    
    def getArea(self):
        return math.pi * (self.radius**2)

    def __str__(self):
        return f'Circle color: {self.getColor()}, Circle filled: {self.isFilled()}, radius: {self.radius}'
    