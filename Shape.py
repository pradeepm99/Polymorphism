import math


class Shape:

    def calculate_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.set_length(length)
        self.set_width(width)
        Shape.__init__(self)

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def calculate_area(self):
        area = self.get_length() * self.get_width()
        return area

class Circle(Shape):

    def __init__(self, radius):
        self.set_radius(radius)
        Shape.__init__(self)

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def calculate_area(self):
        area = math.pi * self.get_radius() ** 2
        return area


rect1 = Rectangle(3, 4)
print(rect1.calculate_area())

circle1 = Circle(5)
print(circle1.calculate_area())