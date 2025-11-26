#1 
while True:
    try: 
        n = int(input("Enter a integer: "))
        break
    except:
        print("Please enter a integer next time.")

if n > 0:
    print("Positive")
elif n == 0:
    print("Zero")
else:
    print("Negative")

#2
grade = int(input("Enter your grade (0-100): "))
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

#3
year = int(input("Enter the current year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("It is leap year.")
else:
    print("It is not leap year.")

#4
age = int(input("Enter your age: "))
if 18 <= age:
    print("You can vote.")
else:
    print("You can't vote.")

#5
num = int(input("Enter a integer: "))
if num % 5 == 0 and num % 11 == 0:
    print("The given number is divisible by both 5 and 11.")
else:
    print("It is not divisible by both 5 and 11.")

#6
units = int(input("Enter the number of units consumed: "))
if 0 <= units <= 100:
    print("£0.50 per unit")
elif 101 <= units <= 200:
    print("£0.75 per unit")
elif 201 <= units <= 300:
    print("£1.20 per unit")
elif 300 < units:
    print("£1.50 per unit")
else:
    print("Invalid input!")

#7
a, b = map(int, input("Enter two number seperated by space: ").split())
operator = input("Choose one between the following operators. (+, -, *, /): ").strip()

if operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)
elif operator == "*":
    print(a*b)
elif operator == "/":
    print(a/b)
else:
    print("Invalid operator!")

#8
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = input("Enter a month: ").lower().strip()

print(days_in_months[months.index(month)])