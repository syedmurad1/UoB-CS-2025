N=int(input("Enter a number:"))
if N>0:
   print(f"{N} is positive.")
elif N<0:
   print(f"{N} is nagetive.")
elif N==0:
   print(f"{N}"is 0)

grade=int(input("Enter a number:"))
if 70<=grade<=100:
   print("this student is 1st")
elif 60<=grade<=69:
   print("this student is 2.1")
if  50<=grade<=59:
   print("this student is 2.2")
elif 40<=grade<=49:
   print("this student is 3rd")
if 0<=grade<=39:
   print("this student is F")
else:
   print("it is invalid number")

year=int(input("Enter a year:"))
if (year % 4==0 and year % 100 !=0) or(year % 400 ==0):
   print (f"{year} is a leap year")
else:
   print(f"{year} is not a leap year")

age=int(input("Enter a age:")) 
if (age is 18 ) or (age > 18):
   print("this person is eligible to vote")
else:
   print("thsi person is not eligible to vote")

num=int(input("Enter a number:"))
if (num % 5==0 and num % 11==0):
   print("this number is divisible by both 5 and 11")
else:
   print("this number is not divisible by both 5 and 11")

units = float(input("Enter the number of units consumed: "))
if units <= 100:
   bill = units * 0.5
elif units <=200:
   bill = 100 * 0.5 + (units - 100) * 0.75
elif units <=300:
   bill = 100 * 0.5 + 100 * 0.75+ (units -200) * 1.2
else:
   bill = 100 * 0.5 + 100 * 0.72 + 100 * 1.2 + (units - 300) * 1.5
print(f"Electricity Bill: £{bill:.2f}")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."
print(f"Result:{result}")

month = input(" Enter a month").strip()
if month in ["january","March","May","July","August","October","December"]:
   days = 31
elif month in ["April","june","September","November"]:
   days = 30
elif month in ("February"):
   days = 28
else:
   days = "Invalid month"
print(f"The number of days in{month.title()} is {days}")

   


   

