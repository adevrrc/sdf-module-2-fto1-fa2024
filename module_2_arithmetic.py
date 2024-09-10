# Syntax
# operand operator operand
print(1 + 1)
print(12 % 10)

age = 26

print(age + 5)

print(age)

brothers_age = age - 9

print(brothers_age)

brothers_age = brothers_age + 1

print(brothers_age)

# 18
brothers_age += 1 #19
brothers_age -= 1 #18

print(brothers_age)

# Type Conversion
number_of_cookies = input("How many cookies did you eat today? ")

print(type(number_of_cookies))

number_of_cookies = int(number_of_cookies)

print(type(number_of_cookies))

number_of_cookies += 10

print(number_of_cookies)

# Addition operator
# numeric_operand + numeric_operand

# String concatenation operator
# operand + operand (at least one operand is a string)

first_name = "Damien"
last_name = "Altenburg"

full_name = first_name + " " + last_name
print(full_name)
