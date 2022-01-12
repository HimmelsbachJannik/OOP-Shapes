from shape import Shape
from dataclasses import dataclass
import math

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
    