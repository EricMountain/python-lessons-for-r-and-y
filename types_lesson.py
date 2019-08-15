#!/usr/bin/env python

import math

print("a string (of characters)")
print(345)
print("a string, a number", 345, "another string")

a=1
b=2.1
c="hello"
d=[a, b, c]

print(f"slightly special string. a = {a}") # Note the *f*

print(f"a = {a} is of type {type(a)}")
print(f"b = {b} is of type {type(b)}")
print(f"c = {c} is of type {type(c)}")
print(f"d = {d} is of type {type(d)}")
print(f"d[2] = {d[2]} is of type {type(d[2])}")

print(f"a+a = {a+a}, is of type {type(a+a)}")
print(f"a+b = {a+b}, is of type {type(a+b)}")

e="world"
print(f"c+e = {c+e}, is of type {type(e)}")


# Now classes and objects...

class Shape:
    def __init__(self, name: str, colour: str):
        self.name = name
        self.colour = colour

    def __str__(self):
        return f"{self.name} is {self.colour}"

shape1 = Shape("polygon", "green")
shape2 = Shape("blabla", "blue")

print(shape1)
print(shape2)

class Rectangle(Shape):
    def __init__(self, name: str, colour: str, length: float, width: float):
        super().__init__(name, colour)
        self.length = length
        self.width = width

    def perimeter(self):
        return self.length * 2 + self.width * 2

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"{super().__str__()}, has perimeter {self.perimeter()} and has area {self.area()}"

print(Rectangle("rectangle", "red", 4, 5))

class Circle(Shape):
    def __init__(self, name: str, colour: str, radius: float):
        super().__init__(name, colour)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius * self.radius

    # def __str__(self):
    #     return f"{super().__str__()}, has perimeter {self.perimeter()} and has area {self.area()}"

c = Circle("disc", "yellow", 5)
area = c.area()
perimeter = c.perimeter()
print(f"{c}, and is of type {type(c)} and has area {area} and perimeter {perimeter}")
