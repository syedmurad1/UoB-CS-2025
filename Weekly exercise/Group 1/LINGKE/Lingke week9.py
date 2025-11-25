#1
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is zero.")
else:
    print("Invalid input. Please enter a valid number.")

#2
grade = int(input("Enter your grade (0-100): "))
if grade >= 70:
    print("1st")
elif 60 <= grade <= 69:
    print("2:1")
elif 50 <= grade <= 59:
    print("2:2")
elif 40 <= grade <= 49:
    print("3rd")
elif 0 <= grade <= 39:
    print("F")
else:
    print("Invalid grade. Please enter a number between 0 and 100.")

#3
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#4
age = int(input("Enter your age: "))
if age < 18:
    print("You cannot vote.")
elif 18 <= age :
    print("You can vote.")
else:
    print("Invalid age. Please enter a valid number.")

#5
number = int(input("Enter a number: "))
if number % 5 == 0 and number % 11 == 0:
    print("The number is divisible by both 5 and 11.")
elif number % 5 == 0:
    print("The number is divisible by 5.")
elif number % 11 == 0:
    print("The number is divisible by 11.")
else:
    print("The number is not divisible by either 5 or 11.")
    
#6
units = int(input("Enter the number of units consumed: "))
if units <= 100:
    bill = units * 0.50
elif 200 <= units <= 200:
    units= units - 100
    bill = (0.50 * 100) + (units * 0.75)
elif 200 <= units <= 300:
    units= units - 200
    bill = (0.50 * 100) + (0.75 * 100) + (units * 1.20)
else:
    units= units - 300
    bill = (0.50 * 100) + (0.75 * 100) + (1.20 * 100) + (units * 1.50)
print(f"Your electricity bill is: Rs. {bill}")

#7
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == '+':
    result = num_1 + num_2
    print(f"The result is: {result}")
elif operation == '-':
    result = num_1 - num_2
    print(f"The result is: {result}")
elif operation == '*':
    result = num_1 * num_2
    print(f"The result is: {result}")
elif operation == '/':
    if num_2 != 0:
        result = num_1 / num_2
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")

#8
month = (input("Enter month : "))
if month in ['April', 'June', 'September', 'November']:
    print(f"{month} has 30 days.")
elif month in ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
    print(f"{month} has 31 days.")
elif month == 'February':
    year = int(input("Enter year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{month} has 29 days.")
    else:
        print(f"{month} has 28 days.")
else:
    print("Invalid month name.")