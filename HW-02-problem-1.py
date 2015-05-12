# Developer Notes
print("Author: Maegan Barney")
print("Due: 2/03/2015")
print("CSC110 - Homework 2 - Programming in Python ")
print("")
print("===============================================")
# Algorithm 1
#  
# 1- Display (“Enter integer value for redButton (1 or 0)”)
# 2- redButton ß Input from user
# 3- Display (“Enter integer value for blueButton (1 or 0)”)
# 4- blueButton ß Input from user
# 5- If redButton ≥ 2 or redButton < 0
#        Display(“Wrong Input for redButton”)
# 6- else If blueButton ≥ 2 or blueButton < 0
#        Display(“Wrong Input for blueButton”)
# 6- else If redButton == 1 and blueButton == 1:
#        Display(“Switch On Machine 1”)
# 6- else if redButton == 0 and blueButton == 0:
#        Display(“All Machines are Off”)
# 7- else:
#        Display(“Switch On Machine 2”)  
# 7- Halt //exit 

redButton = int(input("Enter integer value for redButton (1 or 0) "))
print("You entered ", redButton, "for the red Button.")

blueButton = int(input("Enter integer value for blueButton (1 or 0) "))
print("You entered ", blueButton, "for the blue Button.")

if redButton >= 2 or redButton < 0:
    print("Wrong input for redButton")
elif blueButton >= 2 or blueButton < 0:
    print("Wrong input for blueButton")
elif redButton == 1 and blueButton == 1:
    print("===================")
    print("Switch On Machine 1")
elif redButton == 0 and blueButton == 0:
    print("=====================")
    print("All Machines are Off")
else:
    print("=====================")
    print("Switch On Machine 2")  
exit
 
