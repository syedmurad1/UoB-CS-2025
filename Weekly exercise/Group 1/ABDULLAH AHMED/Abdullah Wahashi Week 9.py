n = int(input("Write a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
elif n == 0:
    print("Zero")


student_grade = int(input("Write the student grade: "))
if 0 <= student_grade <= 39:
    print("F")
elif 40 <= student_grade<= 49:
    print("3rd")
elif 50 <= student_grade<= 59:
    print("2.2")
elif 60 <= student_grade<= 69:
    print("2.1")
elif 70 <= student_grade <= 100:
    print("1st") 

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

age = int(input("Write your age to check if you're eligible to vote: "))
if age >= 18:
    print("You can vote")
else:
    print("You are under 18 you cannot vote")

number = int(input("Write a number: "))
if number % 5 == 0 and number % 11 == 0:
    print("It is divisble by both")
else:
    print("It is not divisble by both")

units = int(input("Write the number of units consumed: "))
bill = 0
if units <= 100:
    bill = units*0.5
elif units <= 200:
    bill = (100 * 0.50) + (units - 100) * 0.75
elif units <= 300:
    bill = (100 * 0.50) + (100 * 0.75) + (units - 200) * 1.20
elif units > 300:
    bill = (100 * 0.50) + (100 * 0.75) + (100 * 1.20) + (units - 300) * 1.50
else:
    print("Invalid unit number")

print(f"Total electricity bill: £{bill:.2f}") 

number1 = float(input("Write the first number: "))
number2 = float(input("Write the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == "+":
    result = number1 + number2
    print(result)
elif operator == "-":
    result = number1 - number2
    print(result)
elif operator == "*":
    result = number1*number2
    print(result)
elif operator == "/":
    if number2 == 0:
        print("Cannot divide by zero")
    else:
        result = number1/number2
        print(result)
else:
    print("Invalid operator")

month = input("Enter a month: ").lower
if month in ["january", "march", "may", "july", "august", "october", "december"]:
    print("31 days")
elif month in ["april", "june", "september", "november"]:
    print("30 days")
elif month == "february":
    print("28 days")
else:
    print("Invalid month")
