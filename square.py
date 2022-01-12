from rectangle import Rectangle
class Square(Rectangle):

    def __init__(self, side=1.0, color='red', filled=True): 
        self.setSide(side)
        self.setColor(color)
        self.setFilled(filled)

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
        return f'Square color: {self.getColor()}, Square filled: {self.isFilled()}, ' \
            f'width: {self.width}, length: {self.width}'