# 1. Check if a number is positive, negative, or zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# 2. Classify student grade
grade = int(input("Enter the student's grade (0-100): "))
if 70 <= grade <= 100:
    print("1st")
elif 60 <= grade <= 69:
    print("2.1")
elif 50 <= grade <= 59:
    print("2.2")
elif 40 <= grade <= 49:
    print("3rd")
else:
    print("F")



# 3. Check if a year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


# 4. Check eligibility to vote
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# 5. Check if a number is divisible by both 5 and 11
number = int(input("Enter a number: "))
if number % 5 == 0 and number % 11 == 0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is NOT divisible by both 5 and 11.")


# 6. Calculate electricity bill
units = int(input("Enter electricity units used: "))
bill = 0
if units <= 100:
    bill = units * 0.50
elif units <= 200:
    bill = 100 * 0.50 + (units - 100) * 0.75
elif units <= 300:
    bill = 100 * 0.50 + 100 * 0.75 + (units - 200) * 1.20
else:
    bill = 100 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 300) * 1.50

print(f"Your electricity bill is £{bill:.2f}")


# 7. Simple calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
else:
    if b == 0:
        print("Error: Division by zero")
    else:
        print("Result =", a / b)


# 8. Days in a month
month = input("Enter month name: ").lower()

if month in ["january", "march", "may", "july", "august", "october", "december"]:
    print("31 days")
elif month in ["april", "june", "september", "november"]:
    print("30 days")
else:
    print("28 days")
