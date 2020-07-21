#!/usr/bin/env python3

import math

class Shape:
    def __init__(self, colour):
        self.colour = colour

class Rectangle(Shape):
    def __init__(self, colour, width, length):
        super().__init__(colour)
        self.width = width
        self.length = length

    def p(self):
        return self.width * 2 + self.length * 2

class Circle(Shape):
    def __init__(self, colour, radius):
        super().__init__(colour)
        self.radius = radius

    def p(self):
        return self.radius * 2 * math.pi


rect = Rectangle("pink", 100, 10)
print(rect.p())

circle = Circle("green", 50)
print(circle.p())

shapes = [rect, circle]
for shape in shapes:
    print(f"{shape.colour} {shape.p()}")
