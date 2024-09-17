"""
Slicing Syntax
collection[start:stop:step]

start (inclusive) default 0
stop  (exclusive) default last index
step  default is 1 (optional)

** The slicing syntax works for string, list, and tuple types.
"""

# Slicing Strings
name = "Damien Altenburg"

print(name[2:5])

# Start from index zero
print(name[:5])

# End at the last index
print(name[2:])

# Negative indexes start from the end of the string, -1 represents the last element
print(name[-5:-2])

# Using step
print(name[2:12:3])
print(name[::2])

# Negative step reverses the order of sliced elements
print(name[::-1])
