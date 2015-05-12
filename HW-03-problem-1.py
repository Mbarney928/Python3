# Developer Notes
print("Author: Maegan Barney")
print("2/11/2015")
print("CSC110 - HW3, problem - 1")
print("")

# Download the attached file called “Fastest_Walker_Speed.py”. Test the program by running it using the Python IDLE. 
# This simple algorithm does the following:
#     [i] asks the user to enter the number of walkers
#     [ii] asks for the distance and time for a each walker
#     [iii] computes the speed for each walker
#     [iv] finds the speed of the fastest walker. 

# Modify this algorithm so that it finds the speed of the slowest walker. 
# ------------------------------------------------------------------------------------------------------------


# Get the number of walkers in the group
num_walkers = float(input("How many walkers in your group? "))

# Get the first distance and time
dist = float(input("Enter the distance: "))
time = float(input("Enter the time: "))

# Compute the speed
speed = dist/time

# Intialize counter for loop
i = 1

# Initialize the value for the highest speed
slow_speed = speed

# Loop through to compute speeds and find the highest
while i < num_walkers:
    # Get the distance and time for the next walker
    dist = float(input("Enter the distance: "))
    time = float(input("Enter the time: "))

    # Compute the speed for the next walker
    speed = dist/time

    # Test to see if this speed is higher than the max speed so far
    if speed < slow_speed:
        slow_speed = speed

    # Increment counter
    i = i + 1

# Print the highest speed
print("The slowest speed in the walking group is: ",slow_speed)
