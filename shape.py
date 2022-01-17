from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        super().__init__()
        self._color = 'red'
        self._filled = True

    def getColor(self):
        return self._color
    
    def setColor(self, color:str):
        self._color = color

    def isFilled(self):
        return self._filled

    def setFilled(self, filled:bool):
        self._filled = filled
    
    @abstractmethod
    def getArea(self:float):
        pass

    @abstractmethod
    def getPerimeter(self:float):
        pass

    def __str__(self):
        return f'Shape color: {self.getColor()}, Shape filled: {self.isFilled()}'

