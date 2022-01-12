from shape import Shape
from dataclasses import dataclass
import math

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
