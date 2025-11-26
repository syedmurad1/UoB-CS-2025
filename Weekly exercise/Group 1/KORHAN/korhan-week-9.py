number = int(input("Please input a number: "))

if number > 0:
    print("The number inputted is positive")
elif number < 0:
    print("The number inputted is negative")
else:
    print("The number inputted is 0")

grade = int(input("Input your grade: "))

if grade >= 70:
    print("A")
elif grade >= 60:    
    print("B") 
elif grade >= 50: 
    print("C") 
elif grade >= 40:  
    print("D") 
else:
    print("F")    

year = int(input("Input a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("The inputted year is a leap year")
else:
    print("The inputted year isn't a leap year")

age = int(input("Input your age: ")) 

if age >= 18:
    print("You're eligible to vote")
else:
     print("You're not eligible to vote")

anotherNumber = int(input("Input another number: ")) 

if anotherNumber % 5 == 0 and anotherNumber % 11 == 0:
    print("The number inputted is both divisible by 5 and 11")
else:
   print("The number you inputted is either not divisible by 5 or 11")

energyConsumed = int(input("Input your energy usage in units: ")) 

energyPrice = 0

priceArray = [0.50, 0.75, 1.20, 1.50]
priceIndex = 0

while energyConsumed != 0:
    dummy = 100 if energyConsumed >= 100 else energyConsumed
    
    energyPrice += dummy * priceArray[priceIndex]
    energyConsumed -= dummy
    
    if priceIndex != 3:
        priceIndex += 1

print(f"The price of your bill is {energyPrice}")

# calculator
num1 = int(input("Input a number to the calculator: "))
sign = input("Input a sign to the calcualtor: ")
num2 = int(input("Input anoter number to the calculator: "))

if sign == "+":
    print(f"{num1} {sign} {num2} = {num1 + num2}")
elif sign == "-":
    print(f"{num1} {sign} {num2} = {num1 - num2}")
elif sign == "/":
    print(f"{num1} {sign} {num2} = {num1 / num2}")
elif sign == "*":
    print(f"{num1} {sign} {num2} = {num1 * num2}")
else:
    print("Your sign is invalid")

months = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

month = input("Input the name of the month: ")

month = month.lower()

day = months.get(month)

if month in months:
    print(f"{month.capitalize()} has {day} days in it")
else:
    print("The month you inputted is not valid")    