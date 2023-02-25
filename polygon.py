from unittest import main

class Rectangle:
    def __init__(self, height, width = 0):
        self.height = height
        if width == 0:
            width = height
        self.width = height

    def get_area(self):
        return self.width * self.height
    def set_width(self, width):
        self.width = width
    def get_perimeter(self):
        return (self.width + self.height)*2
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

        

class Square(Rectangle):
    def set_side(self, value):
        self.width = value
        self.height = value

rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)