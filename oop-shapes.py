from abc import ABC, abstractmethod
from dataclasses import dataclass
import math

@dataclass
class Shape(ABC):
    _color: str = 'red'
    _filled: bool = True

    def getColor(self):
        return self._color
    
    def setColor(self, color:str):
        self._color = color

    def isFilled(self):
        return self._filled

    def setFilled(self, filled:bool):
        self._filled = filled
    
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getPerimeter(self):
        pass

    def __str__(self):
        return f'Shape color: {self._color}, Shape filled: {self._filled}'


@dataclass
class Circle(Shape):
    radius: float = 1.0

    def getRadius(self):
        return self.radius

    def setRadius(self, radius:float):
        self.radius = radius

    def getPerimeter(self):
        return math.pi * 2 * self.radius
    
    def getArea(self):
        return math.pi * (self.radius**2)

    def __str__(self):
        return f'Circle color: {self._color}, Circle filled: {self._filled}, radius: {self.radius}'
    

@dataclass
class Rectangle(Shape):
    width: float = 1.0
    length: float = 1.0

    def getWidth(self):
        return self.width
    
    def setWidth(self, width:float):
        self.width = width
    
    def getLength(self):
        return self.length

    def setLength(self, length:float):
        self.length = length
    
    def getArea(self):
        return self.width * self.length
    
    def getPerimeter(self):
        return 2 * self.width + 2 * self.length
    
    def __str__(self):
        return f'Rectangle color: {self._color}, Rectangle filled: {self._filled}, ' \
            f'Rectangle width: {self.width}, Rectangle length: {self.length}'


@dataclass
class Square(Rectangle):
    # side: float = 1.0
    # width: float = 1.0
    # length: float = 1.0
    # color: str

    def __init__(self, side=1.0, color='red', filled=True): 
        self.setSide(side)
        self.setColor(color)
        self.setFilled(filled)

        # if (width or length): 
            
            # if (color and filled): 
            #     self.width=width 
            #     self.length=width 
            #     self._color = color
            #     self.setFilled(filled)
            # else: 
            #     self.width=width 
            #     self.length=width

    def getSide(self):
        return self.width
    
    def setSide(self, side):
        self.width = side
        self.length = side

    def setWidth(self, side):
        self.setSide(side)

    def setLength(self,side):
        self.setSide(side)
    
    def getArea(self):
        return self.width ** 2
    
    def getPerimeter(self):
        return self.width * 4
    
    def __str__(self):
        return f'Square color: {self.getColor()}, Square filled: {self._filled}, ' \
            f'width: {self.width}, length: {self.width}'



'''Manual Tests'''

a = Square(side=2.0, color='blue')

# print(a.setSide(2.0))
# print(a.setColor('blue'))
print(a)