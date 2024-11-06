# Programmers:  Donovan, Cameron
# Course:  CS151, Professor Zee
# Due Date: Oct 30, 2024
# Programming Assignment:  lab 7
# Problem Statement:
# Data In: width, length, flooring type
# Data Out: cost for each room, overall cost
# Credits: basic area formula
# Display the purpose of the program

# Purpose:  enter floor input
# Parameters: none
# Return: floor_type
def floor_input():
    # input for floor type and error checking
    floor_type = input("Please enter the type of floor you would like to use: ")
    floor_type = floor_type.lower().strip()
    while floor_type != "carpet" and floor_type != "hardwood" and floor_type != "tile":
        floor_type = input("Please enter the type of floor you would like to use: ")
        floor_type = floor_type.lower().strip()

    #type of floor and price
    if floor_type == "carpet":
        floor_type = float(1.39)
    elif floor_type == "hardwood":
        floor_type = float(3.99)
    elif floor_type == "tile":
        floor_type = float(4.99)
    return floor_type

# Purpose:  finds the area of the room
# Parameters: none
# Return: area
def dimension_input():
    #
    length = input("Please enter the length of your room in feet to the nearest foot: ")
    while not length.isdigit():
        length = input("Please enter the length of your room in feet to the nearest foot: ")
    length = int(length)

    #
    width = input("Please enter the width of your room in feet to the nearest foot: ")
    while not width.isdigit():
        width = input("Please enter the width of your room in feet to the nearest foot: ")
    width = int(width)

    #
    area = length * width
    return area

# Purpose:  cost of the room
# Parameters: none
# Return: room cost
def room_cost():
    room_area = dimension_input()
    floor_material = floor_input()
    room_cost = floor_material * room_area
    return room_cost

# Purpose:  main function, calls other functions
# Parameters: none
# Return: none
def main():
    #output request for information and call functions
    print('In this program you can calculate the cost it would be to pay for each room and also all of them in total\n'
          'given the dimensions and floor material of your 5 rooms')
    print('Please input your information for your first room')
    room1 = room_cost()
    print('Please input your information for your second room')
    room2 = room_cost()
    print('Please input your information for your third room')
    room3 = room_cost()
    print('Please input your information for your fourth room')
    room4 = room_cost()
    print('Please input your information for your fifth room')
    room5 = room_cost()
    total_cost = room1 + room2 + room3 + room4 + room5

    #output individual room cost and total room cost
    print('Your first room costs $', room1)
    print('Your second room costs $', room2)
    print('Your third room costs $', room3)
    print('Your fourth room costs $', room4)
    print('Your fifth room costs $', room5)
    print('Your total is $', total_cost)
    print('Thank you for using our program! Have a nice day!')

# call main function
main()
