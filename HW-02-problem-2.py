# Developer Notes
print("Author: Maegan Barney")
print("Due: 2/03/2015")
print("CSC110 - Homework 2/ problem 2 - Programming in Python")
print("")
print("===============================================")

from builtins import input

# Problem 2:
# Write a Python program that does the following:
# ·  The program prompts the user to input two float numbers: number1 and number2
# ·  If the two numbers are positive print their sum
# ·  If the two numbers are negative print their product
# ·  If one of the numbers is a zero print “Error”
# ·  Otherwise, print the result of the following: (number1 – number2)/2


num1 = float(input("Please enter a number (number 1): "))
num2 = float(input("Please enter a number (number 2): "))

if(num1 > 0 and num2 > 0):
    sum = num1 + num2
    print("===============================================")
    print("Sum: ",sum)
elif num1 < 0 and num2 < 0:
    product = num1 - num2
    print("===============================================")
    print("product: ",product)
elif num1 == 0 or num2 ==0:
    print("===============================================")
    print("Error")
else:
    result = (num1-num2)/2
    print("===============================================")
    print(result)
