#!/usr/bin/env python3

# Lists/arrays are much the same thing
# Tuples are a read-only list

# NB - they are 0-indexed, i.e. first item is at index/offset 0

simple = ["a", "b", "c"]
print("Iterate:")
for item in simple:
    print(f"{item}")

print("Iterate with index/offset:")
for offset, item in enumerate(simple):
    print(f"{offset}: {item}")

simple.append("d")
simple.insert(2, "x")
print("Iterate after adding items:")
for item in simple:
    print(f"{item}")

print(f"simple contains {len(simple)} items")
print(f"simple at offset 2 contains {simple[2]}")

print(f"simple sorted: {sorted(simple)}")

# Slices (possibly not in the school syllabus)
print(f"A slice from item 1 to item 2 inclusive: {simple[1:3]}")
print(f"All items from 2 to the end: {simple[2:]}")
print(f"Every 2nd item: {simple[::2]}")
print(f"simple reversed: {simple[::-1]}")
