# Declare variable as a list; the list is empty
temperatures = []

print(type(temperatures))

# Redefine variable with populated list
temperatures = [23.4, 36.1, 24.5, 20.8, 15.6]

print(temperatures)

# List with different data types
employee_information = ["A123", 55024.23, 595, True]

print(employee_information)

# List of lists
employee_data = [
  ["B234", 34595.65, 323, False], employee_information
]

print(employee_data)

# Retrieve the value of an element
print(temperatures[2])

# Redefine the value of an element
temperatures[4] = 0
print(temperatures)

# Get the number of elements in the list
number_of_elements = len(temperatures)

# Append to a list
temperatures.append(24.5)

print(temperatures)

# Insert data in a list
temperatures.insert(3, 14.6)

print(temperatures)

# Remove an element (first occurrence)
temperatures.remove(24.5)

print(temperatures)

# Remove the last element
last_temperatures = temperatures.pop()

print(temperatures)
print(last_temperatures)

# Get index of a value
index = temperatures.index(14.6)

print(index)

print(number_of_elements)

# Sort the elements
# **NOTE**: this only works when all elements are the same type
temperatures.sort()

print(temperatures)

# Reverse the order of elements
temperatures.reverse()

print(temperatures)
