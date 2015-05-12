# Developer Notes
print("Author: Maegan Barney")
print("2/11/2015")
print("CSC110 - HW3, problem - 3")
print("")

# Consider an application in which a radar sensor is placed on an overpass on the highway to 
# monitor the speed of the cars going by. Assume that the speeds are collected ahead of time each day. 
# Write a program that reads the speeds into a list and then determines what percentage of the cars are 
# exceeding the speed limit (65 mph). Allow the user to specify how many speeds have been collected so you 
# can know the size of the list. 
# ------------------------------------------------------------------------------------------------------------

# Ask user to specify how many speeds have been collected. 
userInput = int(input("How many speeds are being entered? "))
speedLimit = int(input("What is the speed limit in that area? "))

# Initialize empty list
speeds = []
i = 0

# Begin while loop with user input of collected speeds
while (i < userInput):
    speed = int(input("Enter a speed: "))
    speeds = speeds + [speed]
    i = i + 1

# Determine which speeds are above 65 and count them.
# Put speeders in separate list to later determine average.
i = 0
totalSpeeders = 0
listOfSpeeders = []
while (i < userInput):
    if (speeds[i] > speedLimit):
        totalSpeeders += 1
        listOfSpeeders = listOfSpeeders + [speeds[i]]
    i = i + 1
    
# Calculate percentage of collected daily speeds over 65mph
speedPct = totalSpeeders / userInput
     
# Display the percentage of the cars exceeding the speed limit (65 mph)
print(str(speedPct * 100) + "% of drivers were exceeding the speed limit (65 mph).")
