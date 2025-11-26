import datetime
import random

print("My", "Name", "Is", "King", sep = "$$")

str = input("Give three names:")  

arr = str.split(" ")

print(arr[0])
print(arr[1])
print(arr[2])

f = 5.26459884 
print(f"{f:.2f}")

year = 2023
quantity = 3
price = 450.00

print(f"I have bought {quantity} footballs for {price} £, in the year {year}. ")

str1 = "I have bought 3 footballs for 450.00 £, in the year 2023"
print(f"The first character for str1 is {str1[0]}")

str2 = "I have bought 3 footballs."

print(f"The length of the second string is {str.__len__()}")

print(datetime.datetime.now())

lowerLimit = 0
upperLimit = 100

print(f"The generated random number between 1 and 100 is {random.randint(lowerLimit, upperLimit)}")

lowerLimit = int(input("Input the lower limit: "))
upperLimit = int(input("Input the higher limit: "))

print(f"The generated random number between inputted numbers {lowerLimit} and {upperLimit} is {random.randint(lowerLimit, upperLimit)}")

numberA = int(input("Last thing, input a number: "))
numberB = int(input("Input another number: "))

print(f"The total sum of the numbers is {numberA + numberB}")