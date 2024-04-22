import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Cube(Shape):
    def __init__(self, side):
        self.side = side

    def __eq__(self, obj):
        if not isinstance(obj, Cube):
            return False

    def area(self):
        return 6 * math.pow(self.side, 2)

    def perimeter(self):
        return 12 * self.side
