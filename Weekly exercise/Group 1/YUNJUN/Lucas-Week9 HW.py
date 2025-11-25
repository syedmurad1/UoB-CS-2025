num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



score = int(input("Enter student's score (0-100): "))
if 70 <= score <= 100:
    print("1st")
elif 60 <= score <= 69:
    print("2.1")
elif 50 <= score <= 59:
    print("2.2")
elif 40 <= score <= 49:
    print("3rd")
elif 0 <= score <= 39:
    print("F")
else:
    print("Invalid score")



year = int(input("Enter a year: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if is_leap:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")




age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")




num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11")
else:
    print(f"{num} is not divisible by both 5 and 11")




units = int(input("Enter units consumed: "))
bill = 0.0
if units > 300:
    bill += (units - 300) * 1.5
    units = 300
if units > 200:
    bill += (units - 200) * 1.2
    units = 200
if units > 100:
    bill += (units - 100) * 0.75
    units = 100
bill += units * 0.5
print(f"Electricity bill: £{bill:.2f}")




num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"

print(f"Result: {result}")



month = input("Enter month name (e.g., January): ").strip().lower()
if month in ["january", "march", "may", "july", "august", "october", "december"]:
    print("31 days")
elif month in ["april", "june", "september", "november"]:
    print("30 days")
elif month == "february":
    print("28 days")
else:
    print("Invalid month name")