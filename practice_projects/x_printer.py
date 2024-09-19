"""
Description: This script prints the letter X to the terminal.
Author: Damien Altenburg
Date: 2024-09-19
Usage: python x_printer.py
"""
#PRINT_CHARACTER = '*'

PRINT_CHARACTER = input("Enter a character: ")

PRINT_LINES = [
    f"{PRINT_CHARACTER}   {PRINT_CHARACTER}",
    f" {PRINT_CHARACTER} {PRINT_CHARACTER}",
    f"  {PRINT_CHARACTER}"
]

print(PRINT_LINES[0])
print(PRINT_LINES[1])
print(PRINT_LINES[2])
print(PRINT_LINES[1])
print(PRINT_LINES[0])

hockey_teams = {
    "winnipeg": "jets"
}

print(f"My favorite hockey team is "
      f"the {hockey_teams["winnipeg"].title()}")

favorite_hockey_team_message = (f"My favorite hockey team is "
                               f"the {hockey_teams["winnipeg"].title()}")

print(favorite_hockey_team_message)
