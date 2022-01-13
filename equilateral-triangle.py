from shape import Shape
import math

class Equilateral_Triangle(Shape):
    def __init__(self, sideLenght:float=1.0, color:str='red', filled:bool=True):
        self.sideLength = sideLenght
        self.setColor(color)
        self.setFilled(filled)
    
    def getSideLength(self):
        return self.sideLength
    
    def setSideLenght(self, sideLenght:float):
        self.sideLength = sideLenght
    
    def getArea(self):
        return (self.sideLength**2) / 4 * math.sqrt(3)

    def getPerimeter(self):
        return self.sideLength * 3
    
    def __str__(self):
        return f'Equilateral Triangle color: {self.getColor()}, Equilateral Triangle filled: {self.isFilled()}, ' \
            f'Side Lenght: {self.sideLength}'
