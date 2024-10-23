# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
- **Name: Main**
- **Parameters:**
- **Return:**
- **Algorithm:**
1. print the purpose
2. call room_cost and set the return to the variable room 1
3. call room_cost and set the return to the variable room 2
4. call room_cost and set the return to the variable room 3
5. call room_cost and set the return to the variable room 4
6. call room_cost and set the return to the variable room 5
7. add room 1, room 2, room 3, room 4, and room5 together and set it to 
total_cost
8. print the rooms 
9. and print the total

   
- **Name: room_cost**
- **Parameters: floor_type, area**
- **Return:**
- **Algorithm:**
1. call dimension_input and set it to room_area
2. call floor_input and set it to floor_cost
3. multiply floor_input by room_area and save it in the 
variable room_cost

- **Name:dimension_input**
- **Parameters:**
- **Return: area**
- **Algorithm:**
1. prompt to input the length and save as length 
2. while the length is not a digit 
   3. prompt to input the length
3. typecast length to an integer
3. prompt to input the width and save as width
4. while the width is not a digit
   1. prompt to input the width
5. typecast width to an integer
6. set area to length * width
7. return area


- **Name: floor_input**
- **Parameters:**
- **Return: floor_type**
- **Algorithm:**
1. Prompt the user to input the floor type and save as floor_type
2. while floor type is not hardwood, carpet, or tile
   1. Prompt the user to input the floor type
3. if floor_type is hardwood
   1. floor_type is set to the float 1.39 
4. Otherwise if the floor_type is carpet
   1. floor_type is set to the float 3.99
5. otherwise if floor_type is tile 
   1. floor_type is set to the float 4.99
6. return floor_type
