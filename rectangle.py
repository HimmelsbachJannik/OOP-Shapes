from shape import Shape

class Rectangle(Shape):
 
    def __init__(self, width:float=1.0, length:float=1.0, color:str='red', filled:bool=True): 
        self.width = width
        self.length = length
        self.setColor(color)
        self.setFilled(filled)

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
        return f'Rectangle color: {self.getColor()}, Rectangle filled: {self.isFilled()}, ' \
            f'Rectangle width: {self.width}, Rectangle length: {self.length}'

    

'''Manual Test Cases'''

'''QPK-52 Test Case'''

# rectangle = Rectangle()
# print(rectangle)
