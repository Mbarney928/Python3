# Developer Notes
# print("Maegan Barney")
# print("CSC110 - Homework 01")
# print("1/26/2015")

print("")
# .1

print("1.")
a = 5
b = 2
c = 3

z = ((2 * a - 3* b)/8) + (42 / (a**2 - b**2)) * (((2/a)+(c/6))/b)
# print(z)
print("The value of z when printed is:",z)

print("")
# .2
print("2.")
#  Company’s sales in dollars for Month and Year
companySales = input("Enter the value of the company’s sales in dollars in August 2013: ")
#  Input from the user for the sales value for August 2013.
saleValue = float(companySales)
#  Compute the sales tax based on 6% of the sale
salesValue = saleValue * 6 /100
# Print the resulting sales tax
print("The sales tax is ${}".format(salesValue),"for August 2013")
