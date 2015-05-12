# Developer Notes
print("Author: Maegan Barney")
print("2/21/2015")
print("CSC110 HW #4 - Problem #1")
print("")

# Directions:
# Write a Python program that would 
# generate a list that contains all odd 
# numbers between 100 and 500 except 227 and 355. 
# -------------------------------------------------------------------------------------------

# Start with an empty list
myList = []
# Initial variable 'number' with starting value
number = 100
# While number is less than 500, continue to loop.
while (number < 500):
    # Check to see if number is odd.
    if( number %2 != 0):
        # Add Element to list
        myList = myList + [number]
        # Check for these two numbers, and remove the first occurrence when found in list.
        if(number == 227 or number == 355):
            myList.remove(number)
        else:
            number = number + 1
    number = number + 1
# Print the list
print(myList)
