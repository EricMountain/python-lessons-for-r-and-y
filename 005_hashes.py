#!/usr/bin/env python3

# Maps, dictionaries, hash tables, hash maps, associative arrays, lookup tables
# are different names for the same thing

# In Python there are a few different implementations with special properties, 
# but the basic one is the `dict` type

# An empty dict
empty = dict()
print(f"Empty: {empty!r}")

# Another way of starting off empty
empty = {}
print(f"Also empty: {empty!r}")

# Maps map keys to values
simple = {"a": 1, "c": 3, "b": 2}
print(f"Simple map: {simple!r} with {len(simple)} entries")

# Iterating over the keys:
print("Iteration over keys:")
for key in simple:
    print(f"{key} -> {simple[key]}")

# Add a mapping
simple["d"] = 4

# Iterating over items (keys and values at the same time):
print("Iteration over items:")
for key, value in simple.items():
    print(f"{key} -> {value}")

# The reason that works is that items returns a list of (key, value) tuples:
print(f"simple.items(): {simple.items()!r}")

# There is no sorting nor guarantee that keys are kept in the order they are inserted
# (there's actually a type that guarantees the latter: collections.OrderedDict)

# So if you want to sort, then for instance:
print("Iterating over sorted keys:")
for key in sorted(simple.keys()):
    print(f"{key} -> {simple[key]}")

# Dereferencing a key that doesn't exist will cause an error:
try:
    print(f"{simple['e']}")
except KeyError:
    print("There's no 'e' in our simple map")

# We can check if a key is present
if "e" not in simple:
    print("There's no 'e' in our simple map (no exception this time)")

# Maps can be more complicated
complex = {
    ("Rachel", "M"): {
        "age": 99,
        "likes": ["lots", "of", "things"]
    },
    ("Yelena", "M"): {
        "age": 96,
        "likes": ["other", "things"]
    }
}

print(f"complex = {complex!r}")
