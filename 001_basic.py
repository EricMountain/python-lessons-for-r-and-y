#!/usr/bin/env python

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

