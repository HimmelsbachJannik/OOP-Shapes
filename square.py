from rectangle import Rectangle
class Square(Rectangle):

    def __init__(self, side:float=1.0, color:str='red', filled:bool=True): 
        self.setSide(side)
        self.setColor(color)
        self.setFilled(filled)

    def getSide(self):
        return self.width
    
    def setSide(self, side:float):
        self.width = side
        self.length = side

    def setWidth(self, side:float):
        self.setSide(side)

    def setLength(self,side:float):
        self.setSide(side)
    
    def getArea(self):
        return self.width ** 2
    
    def getPerimeter(self):
        return self.width * 4
    
    def __str__(self):
        return f'Square color: {self.getColor()}, Square filled: {self.isFilled()}, ' \
            f'width: {self.width}, length: {self.width}'