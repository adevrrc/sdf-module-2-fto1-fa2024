# Define a variable as a set
scores = set() # empty set
scores = {34, 22, 80, 70, 66}

print(type(scores))
print(scores)

# Cannot access elements of a set using an index or key
#print(scores[0]) # error

# Functions
print(len(scores))

# Add an element to the set
scores.add(55)
print(scores)

# Remove the element with specific value
scores.remove(55)
print(scores)

# Like remove, but doesn't generate an exception when the value doesn't exist
scores.discard(80)
scores.discard(1)

previous_scores = {11, 22, 33, 44, 55, 66}

# Returns a set contain all the elements within both sets
all_scores = scores.union(previous_scores)

print(all_scores)

# Returns a set with elements different from those in the argument
different_scores = scores.difference(previous_scores)

print(different_scores)

# Returns a set with elements that are common with those in the argument
common_scores = scores.intersection(previous_scores)

print(common_scores)

# Other methods
# clear()
# copy()
# pop()
