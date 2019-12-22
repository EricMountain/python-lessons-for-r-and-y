#!/usr/bin/env python3

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

# Lists
a = []
print(f"a = {a}")
a.append("something")
a.extend([1, 2, "bob", 10])
print(f"after append and extend, a = {a}")
print(f"2nd element of a = {a[1]}")
print(f"length of a = {len(a)}")

# Loops
for i in range(3):
    print(f"i = {i}")

# Basic Maths
# - Assign
a = 1
# - Increment
a += 1
# - Integer division
b = 10 // 3
print(f"10 // 3 = {b}")
# - Modulo/remainder-of-division (mathematical notation: a | b)
print(f"10 % 3 = {10 % 3}")
