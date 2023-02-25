from unittest import main

class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
    def __str__(self):
        string = type(self).__name__
        valueVariableString = "(width={}, height={})".format(self.width, self.height)
        return (type(self).__name__) + valueVariableString

    def set_height(self, height):
        self.height = height
    def set_width(self, width):
        self.width = width


    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return (self.width + self.height)*2
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        picture = ""
        if(self.height > 50 or self.width > 50):
            return "Too big for picture."
        else:
            for heightLine in range(self.height):
                for widthColumn in range(self.width):
                    picture+= "*"
                picture += "\n"
            return picture
    def get_amount_inside(self, anotherShape):
        fitHeight = self.height/anotherShape.height
        fitWidth = self.width/anotherShape.width
        return int(fitHeight * fitWidth)


        

class Square(Rectangle):
    def __init__ (self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return (type(self).__name__+"(side=" + str(self.width) + ")")

    def set_side(self, side):
        self.width = side
        self.height = side

rect = Rectangle(3, 6)