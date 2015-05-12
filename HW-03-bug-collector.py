# Developer Notes
print("Author: Maegan Barney")
print("2/11/2015")
print("CSC110 - HW3, problem - 2")
print("")

# A bug collector collects bugs every day for seven days. 
# Write a program in Python that keeps a running total of the number of bugs collected during the seven days. 
# The program should ask for the number of bugs collected each day, and when the loop is finished, the program 
# should display the total number of bugs collected in the week.
# ------------------------------------------------------------------------------------------------------------

# Initialize an accumulator variable.
totalBugs = 0
i = 0

while(i < 7):
    # Ask the user to enter the number of bugs collected for each of the 7 days.
    bugsCollectedToday = int(input("How many bugs were collected on day " + str(i+1) + "? "))
    # Get the total of bugs collected for the entire week.
    totalBugs = totalBugs + bugsCollectedToday
    i = i + 1
    
# Display the total bugs collected within the week.
print("")
print(str(totalBugs) + " bugs were collected this week")
