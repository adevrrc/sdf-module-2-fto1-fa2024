# Declare a list
temperatures = []

print(type(temperatures))

print(temperatures)

temperatures = [23.4, 34.5, 45.6, 56.7]

print(temperatures)

# Elements can store values of different types
employee_information = ["A123", 55023.23, 595, True]

# Java
# float[] temperatures;

employee_data = [["B234", 23457.336232, 834, False], employee_information]

print(employee_data)

# Access element syntax
# list_ref[index]
print(f"Employee salary: ${employee_information[1]:,.2f}")

print(f"Employee salary: ${employee_information[1]}")

print(f"Employee salary: ${employee_data[0][1]:,.2f}")

temperatures[3] = 99.99

print(temperatures[3])

#temperatures = 99.99

#print(temperatures)

# Retrieve the number elements
print(len(temperatures))

print(len("Damien Altenburg"))

# Invoke functions of anything
# object_reference.function_identifier(arg-list)
temperatures.append(24.5)
temperatures.insert(3, 14.6)
temperatures.remove(24.5)
last_step_count = temperatures.pop()
index = temperatures.index(14.6)
temperatures.sort()
temperatures.reverse()
