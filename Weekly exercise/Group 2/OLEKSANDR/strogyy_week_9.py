# Task 1

entered_number = input("Enter number: ")

try:
    if float(entered_number) > 0:
        print("You number is positive")
    elif float(entered_number) < 0:
        print("Your number is negative")
    elif float(entered_number) == 0:
        print("Your number is zero")
    else:
        print("Unknown error...")
except ValueError:
    print("Value Error!")


# Task 2

grade = input("Enter your grade (0-100): ")

try:
    if float(grade) >= 0 and float(grade) < 40:
        print("F")
    elif float(grade) >= 40 and float(grade) < 50:
        print("3rd")
    elif float(grade) >= 50 and float(grade) < 60:
        print("2.2")
    elif float(grade) >= 60 and float(grade) < 70:
        print("2.1")
    elif float(grade) >= 70 and float(grade) <= 100:
        print("1st")
    else:
        print("You need to enter the grade in the range of 0-100")
except ValueError:
    print("Value Error!")


# Task 3

year = input("Enter a year: ")

try:
    if (int(year) % 4 == 0 and int(year) % 100 != 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Value Error!")



# Task 4

user_age = input("Enter your age: ")

try:
    if int(user_age) >= 18:
        print("You can vote.")
    else:
        print("You can't vote.")

except ValueError:
    print("Value Error!")



# Task 5

number = input("Enter a number: ")
try:
    if int(number) % 5 == 0 and int(number) % 11 == 0:
        print("True")
    else:
        print("False")
except ValueError:
    print("Value Error!")



# Task 6

electricity = input("Enter units: ")

try:

    if int(electricity) >= 0 and int(electricity) <=100:
        print("You need to pay: £", int(electricity) * 0.5)
    elif int(electricity) <=200 and int(electricity) >100:
        print("You need to pay: £", int(electricity) * 0.75)
    elif int(electricity) <=300 and int(electricity) >200:
        print("You need to pay: £", int(electricity) * 1.20)
    elif int(electricity) >300:
        print("You need to pay: £", int(electricity) * 1.50)
    else:
        print("Invalid input.")
except ValueError:
    print("Value Error!")



# Task 7

num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")
operation = input("Enter operation (+, -, *, /): ")

try:
    if operation == "+":
        print("Result:", float(num_1) + float(num_2))
    elif operation == "-":
        print("Result:", float(num_1) - float(num_2))
    elif operation == "*":
        print("Result:", float(num_1) * float(num_2))
    elif operation == "/":
        if float(num_2) != 0:
            print("Result:", float(num_1) / float(num_2))
        else:
            print("Error: Division by zero.")
    else:
        print("Invalid operation.")
except ValueError:
    print("Value Error!")


# Task 8

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = input("Select a month (not the number): ").lower().strip()

print(days[months.index(month)])