"""
Description: The script formats a telephone number.
Author: Damien Altenburg
Date: 2024-9-17
Usage: python format_telephone_number.py
"""
telephone_number = input("Enter telephone digits: ")

area_code = telephone_number[0:3]
prefix = telephone_number[3:6]
line_number = telephone_number[6:]

print(f"({area_code}) {prefix}-{line_number}")
