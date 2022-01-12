from abc import ABC, abstractmethod
from dataclasses import dataclass

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




'''Manual Tests'''

# a = Square(side=2.0, color='blue')

# print(a.setSide(2.0))
# print(a.setColor('blue'))
# print(a)