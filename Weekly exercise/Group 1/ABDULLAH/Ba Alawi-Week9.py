# Ba Alawi Week 9 EX
# task 1
while True:
    try:
        n1=int(input("enter a number: "))
        break
    except ValueError:
        print("invalid input try again:")

if n1==0:
        print("The 1st number you entered is Zero")
elif n1>0:
        print("The 1st number you entered is Positive")
elif n1<0:
        print("The 1st number you entered is Negative")

# task 2
while True:
    try:
        Student_grade=int(input("enter your score: "))
        break
    except ValueError:
        print("invalid input try again:")

if Student_grade >=70:
     print("You got 1st, Well done!")
elif Student_grade <70 and Student_grade >= 60:
     print("You got 2.1, Good job!")
elif Student_grade <60 and Student_grade >= 50:
     print("You got 2.2, You can do better!")
elif Student_grade <50 and Student_grade >= 40:
     print("You got 3rd, Try harder next time!")
else:
     print("You got F, Try harder next time!")

# task 3
while True:
    try:
        Year=int(input("enter any year: "))
        break
    except ValueError:
        print("invalid input try again:")

if Year%4 == 0:
     print("It is a leap year")
else:
     print("It is not a leap year")

# Task 4
while True:
    try:
        age=int(input("enter your age: "))
        break
    except ValueError:
        print("invalid input try again:")

if age>=18:
     print("you are eligible to vote")
else:
     print("you are not eligible to vote")

# task 5
while True:
    try:
        n2=int(input("enter a number: "))
        break
    except ValueError:
        print("invalid input try again:")

if n2%5 == 0 and n2 %11 == 0:
     print("the 2nd number you entered is divisible by both 5 and 11.")
else:
     print("the 2nd number you entered is not divisible by 5 nor 11.")

# task 6
while True:
    try:
        units =int(input("enter the number of units consumed: "))
        break
    except ValueError:
        print("invalid input try again:")
if units >= 0 and units <=100 :
     print(f"your bill is {units * 0.5}£")
elif units >= 101 and units <=200 :
     print(f"your bill is {units * 0.75}£")
elif units >= 201 and units <=300 :
     print(f"your bill is {units * 1.2}£")
else:
     print(f"your bill is {units * 1.5}£")

#  task 7 
while True:
     try:
          num1 = float(input("Enter the first number: "))
          break
     except ValueError:
          print("invalid input try again,")
while True:
     try:  
          num2 = float(input("Enter the second number: "))
          break
     except ValueError:
          print("invalid input try again,")


operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator!")

# task 8

Month_input = input(f"Enter a month with the full spell: ")
Month = Month_input.lower()
if Month == "january" or Month == "march" or Month == "may" or Month == "july" or Month == "august" or Month == "october" or Month == "december":
     print("this month has 31 days")
elif Month == "april" or Month == "june" or Month == "september" or Month == "november":
     print("this month has 30days")
else:
     print("this month has 28 days")
