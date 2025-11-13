import datetime
import random

# Use the print () function to display the $$ separator between each string.
#   Expected Output:
#   My$$Name$$Is$$King

print("My", "Name", "Is", "King@!", sep="$$")

# Write a program to take three names as input from a user in 
# the single input() function call and Expected Output:
#   Enter three Names: Ali Syed Tom
#    Name1: Ali
#    Name2: Syed
#    Name3: Tom

name = ["Ali",  "Simi", "Tom"]

print("Enter three names: ", name)

x = name[0]
print("Name 1: " + x)

y = name[1]
print("Name 2: " + y)

z = name[2]
print("Name 3: " + z)

# Display float number 5.26459884 with x amount of decimals using print()

a = round(5.26459884, 2)
print(a)

print(f"{5.26459884:.4f}")
print(f"{5.26459884:.0f}")
print("THX")

# Write a program to use f-strings method to format the following three variables as per the expected output
# year = 2023
# quantity = 3
# price = 450
# Expected Output:
# I have bought 3 footballs for 450.00 £, in the year 2023.

year = 2023
quantity = 3
price = 450

txt = f"I have bought {quantity} footballs for {price} £, in the year {year}."

print(txt)

print(txt[0])

# Get the first character from the following sentence: 
# I have bought 3 footballs for 450.00 £, in the year 2023.

txt1 = f"I have bought {quantity} footballs."

# Get the length of the following sentence: I have bought 3 footballs.

a = len(txt1)
print(a)

# Get the current date using today ().

today = datetime.datetime.today()
print(today)

# Generate a random number between 1 and 100.

r = random.randrange(1, 100)
print(r)

# Write a program to take two numbers as input from a user and 
# generate a random number between those two numbers.

num1 = float(input("Add a number - "))
num2 = float(input("Add another number - "))

rand_num = random.uniform(num1, num2)

print(rand_num)

# Write a program to take two numbers as input from
# a user and program should add those two numbers and display.

total = num1 + num2

print("The first number is -> ", num1)
print("The second number is -> ", num2)

print(total)