"""
Description: This script demonstrates data types in python.
Author: Damien Altenburg
Date: 9/9/2024
Usage: python module_2_data_types.py
"""
# Invoking Function Syntax
# function_name(argument, argument, etc)
print('Hello World', "Damien", "is super cool.")

#print(*objects, sep=' ', end='\n', file=None, flush=False)
print("Hello World", "Damien", "is super cool.", sep=',')

# Declare variable syntax
# variable_identifier = a_value
student_full_name = "Damien Altenburg"

# redefining the variable
student_full_name = "Bruce Lee"

# Java
# String studentFullName;

age = 26

current_salary = 45238.89

is_employed = True

print("Hello my name is", student_full_name)

# Variables must be declared before you can use them
#print(this_word_doesnt_exist)

# Constants
NUMBER_OF_MONTHS_IN_A_YEAR = 12

# Java
# final int NUMBER_OF_MONTHS_IN_A_YEAR = 12;

# 5%
FEDERAL_TAX_RATE = 0.05

# input Function
# Syntax: input(prompt)
username = input("What is your name? ")

#print("Your name is", username)

print(type(username))

age = input("What is your age? ")

print(type(age))

print(f"Your name is {username} and your age is {age}.")

PI = 3.14159

print(f"Value of pi: {PI:.2f}")

#26
#00026
age = 26
print(type(age))
print(f"Your age is {age:05}")
