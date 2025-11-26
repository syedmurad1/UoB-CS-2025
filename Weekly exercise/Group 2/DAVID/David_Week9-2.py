# Write a program that checks whether a given number is positive negative or zero

n = int(input("Enter an integer: "))
if n >= 0:
    if n == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

# Write a program in a list that classifies a student's grade based on the following criteria:
# 70-100: 1st
# 60-69: 2.1
# 50-59: 2.2
# 40-49: 3rd
# 0-39: F

grade = int(input("Enter your grade (0-100): "))
if 70 <= grade <= 100:
    print("1st")
elif 60 <= grade <= 69:
    print("2.1")
elif 50 <= grade <= 59:
    print("2.2")
elif 40 <= grade <= 49:
    print("3rd")
elif 0 <= grade <= 39:
    print("F")
else:
    print("That's not a valid grade!")

# Write a program that checks if a given year is a leap year or not
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Write a program that checks if a person is eligible to vote. A person can vote if their
# age is 18 or older.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Write a program to check if a given number is divisible by both 5 and 11.
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11.")
else:
    print(f"{num} is not divisible by both 5 and 11.")

# Write a program to calculate an electricity bill based on the number of units consumed:
# For the first 100 units, the cost is $0.5 per unit
# For the next 100 units (101-200), the cost is $0.75 per unit
# For the next 100 units (201-300), the cost is $1.20 per unit
# For units above 300, the cost is $1.50 per unit

units = int(input("Enter the number of units consumed: "))
if units <= 100:
    bill = units * 0.5
elif units <= 200:
    bill = (100 * 0.5) + ((units - 100) * 0.75)
elif units <= 300:
    bill = (100 * 0.5) + (100 * 0.75) + ((units - 200) * 1.20)
else:
    bill = (100 * 0.5) + (100 * 0.75) + (100 * 1.20) + ((units - 300) * 1.50)
print(f"Your electricity bill is: ${bill:.2f}")

# Write a program that acts as a simple calculator. It should prompt the user for two numbers
# and an operator (+, -, *, /) and perform the corresponding operation.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero.")
else:
    print("Error! Invalid operator.")

# Write a program that takes a month as input and prints the number of days in that month.
# (Assume February has 28 days)

month = input("Enter the month: ").strip().lower()

month_list = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

if month in month_list:
    if month == "february":
        print("February has 28 days.")
    elif month in ["april", "june", "september", "november"]:
        print(f"{month} has 30 days.")
    else:
        print(f"{month} has 31 days.")
else:
    print("Error! Invalid month name.")

