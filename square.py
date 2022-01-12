from rectangle import Rectangle
from dataclasses import dataclass
import math

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