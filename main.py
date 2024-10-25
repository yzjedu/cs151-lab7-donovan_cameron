# Programmers:  Donovan, Cameron
# Course:  CS151, professor zee
# Due Date: oct 30, 2024
# Programming Assignment:  lab 7
# Problem Statement:
# Data In: width, length, flooring type
# Data Out: cost for each room, overall cost
# Credits:
# Display the purpose of the program

# Purpose:  [what problem does the function solve?]
# Parameters: [list with purpose in the same order they appear in the function header]
# Return: [return value, it's type, and what it represents]
def floor_input():
    floor_type = input("Please enter the type of floor you would like to use: ")
    floor_type = floor_type.lower().strip()
    while floor_type != "carpet" and floor_type != "hardwood" and floor_type != "tile":
        floor_type = input("Please enter the type of floor you would like to use: ")
        floor_type = floor_type.lower().strip()
    if floor_type == "carpet":
        floor_type = float(1.39)
    elif floor_type == "hardwood":
        floor_type = float(3.99)
    elif floor_type == "tile":
        floor_type = float(4.99)
    return floor_type

# Purpose:  [what problem does the function solve?]
# Parameters: [list with purpose in the same order they appear in the function header]
# Return: [return value, it's type, and what it represents]
def dimension_input():
    length = input("Please enter the length of your room in feet to the nearest foot: ")
    while not length.isdigit():
        length = input("Please enter the length of your room in feet to the nearest foot: ")
    length = int(length)

    width = input("Please enter the width of your room in feet to the nearest foot: ")
    while not width.isdigit():
        width = input("Please enter the width of your room in feet to the nearest foot: ")
    width = int(width)
    area = length * width
    return area

print(dimension_input())
