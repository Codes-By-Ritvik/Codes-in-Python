#to perform trigonometric functions

import math

#function for adding
def add(x, y):
    return x + y
#function for subtracting
def subtract(x, y):
    return x - y
#function for multiplication
def multiply(x, y):
    return x * y
#function for division
def divide(x, y):
    return x / y

print("Select operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. tan")

while True:
    #selection of operation
    choice = input("Enter choice (1/2/3/4/5): ")
    #enter the numbers
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
#if, elif, else statement for the entered numbers
        if choice == "1":
            print(num1, "+", num2, "=", num1 + num2,",","Rounded number: ", round(num1 + num2))
        elif choice == "2":
            print(num1, "-", num2, "=", num1 - num2,",","Rounded number: ", round(num1 - num2))
        elif choice == "3":
            print(num1, "x", num2, "=", num1 * num2,",","Rounded number: ", round(num1 * num2))
        elif choice == "4":
            print(num1, "/", num2, "=", num1 / num2,",","Rounded number: ", round(num1 / num2))
        break
    else:
        print("Invalid input.")
