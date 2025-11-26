#Antonella Ferrer
#2806513
#Activity 

n = int(input("Write a number: "))  #Check if number its positive, negavite, zero
if n > 0:
    print("The number its Positive")
elif n < 0:
    print("The number its Negative")
elif n == 0: 
    print("The number its Zero")


student_grade = int(input("Write the student grade: ")) #Check if the student pasess or not the work
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

year = int(input("Enter a year: ")) # Check if the year its a leap year

if year % 4 == 0:  #Leap year
    if year % 100 == 0: 
        if year % 400 == 0:
            print("The chosen year its a leap year")
        else:   #Not a leap year
            print("The chosen year its not a leap year")
    else:
        print("The chosen year its a leap year")
else:
    print("The chosen year its not a leap year")

age = int(input("Write your age to check if you're eligible to vote: ")) #Check if its over 18
if age >= 18:
    print("You can vote")
else:
    print("You are under 18 you cannot vote")

number = int(input("Write a number: ")) #If a number its diviisible by 5 and 11
if number % 5 == 0 and number % 11 == 0: 
    print("The chosen number its divisible by 5 and 11")
else:
    print("The chosen number its not divisible by 5 and 11")

units = int(input("Write the number of units consumed: ")) # Electicity bill based on unit numbers  
bill = 0
if units <= 100: #for the first 100 units (0.50)
    bill = units*0.5
elif units <= 200: #for the next 100 units (0.75)
    bill = (100 * 0.50) + (units - 100) * 0.75
elif units <= 300: #for the next 100 units (0.125)
    bill = (100 * 0.50) + (100 * 0.75) + (units - 200) * 1.20
elif units > 300: #for any above 300 units (1.50)
    bill = (100 * 0.50) + (100 * 0.75) + (100 * 1.20) + (units - 300) * 1.50
else:
    print("Invalid unit number")

print(f"Total electricity bill: £{bill:.2f}") 

number1 = float(input("Write the first number: ")) #Calculate two numbers with random operators
number2 = float(input("Write the second number: "))
operator = input("Enter an operator (+, -, *, /): ") #4 posibilities
if operator == "+": #Adding
    result = number1 + number2
    print(result)
elif operator == "-": #Substracting
    result = number1 - number2
    print(result)
elif operator == "*": # Multiplying
    result = number1*number2
    print(result)
elif operator == "/": #Dividing
    if number2 == 0:
        print("Cannot divide by zero")
    else:
        result = number1/number2
        print(result)
else:
    print("Invalid operator")

month = input("Enter a month: ").lower()   #Tell the user if the month they choose has 31/30 or 28 days 
if month in ["january", "march", "may", "july", "august", "october", "december"]:
    print("The month has 31 days")
elif month in ["april", "june", "september", "november"]:
    print("The month has 30 days")
elif month == "february":
    print("The month has 28 days")
else:
    print("Invalid month")
