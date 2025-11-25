#1
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is zero.")
else:
    print("Invalid input.")

#2
grade = int(input("Enter your grade: "))
if grade >= 70 and grade <= 100:
    print("1st")
elif grade >= 60 and grade <= 69:
    print("2.1")
elif grade >= 50 and grade <= 59:
    print("2.2")
elif grade >= 40 and grade <= 49:
    print("3rd")
elif grade >= 0 and grade <= 39:
    print("Fail")
else:
    print("Invalid grade.")

#3
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#4
age = int(input("Enter your age: "))
if age >=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#5
number = int(input("Enter a number: "))
if number % 5 == 0 and number % 11 == 0:
    print("True")
else:
    print("False")

#6
electr = int(input("Enter unit: "))
if electr >= 0 and electr <=100:
    print("Bill amount is: £", electr * 0.5)
elif electr <=200 and electr >100:
    print("Bill amount is: £", electr * 0.75)
elif electr <=300 and electr >200:
    print("Bill amount is: £", electr * 1.20)
elif electr >300:
    print("Bill amount is: £", electr * 1.50)
else:
    print("Invalid input.")

#7
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero.")
else:
    print("Invalid operation.")

#8
month = int(input("Enter month number (1-12): "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    print("28 or 29 days")
else:
    print("Invalid month number.")