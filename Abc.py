from abc import ABC, abstractmethod
import math
pi = math.pi
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)


shapes = [Rectangle(5, 3), Circle(4)]


for shape in shapes:
    print(f"The area is {shape.area()}")
