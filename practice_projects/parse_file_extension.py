"""
Description: The script parses a file extension from a file path.
Author: Damien Altenburg
Date: 2024-9-17
Usage: python parse_file_extensions.py
"""
filename = input("Enter a filename: ")

dot_index = filename.index('.')

file_extension_start_index = dot_index + 1

file_extension = filename[file_extension_start_index:]

print(f"File extension: {file_extension}")
