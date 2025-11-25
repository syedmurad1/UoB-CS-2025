# TASK 1

print("My", "Name", "Is", "King", sep="$$")


# TASK 2

names = str(input("Enter three names (use spaces only) "))
names_list = names.split(" ")

print(f"Name_1: {names_list[0]}\n",
      f"Name_2: {names_list[1]}\n",
      f"Name_3: {names_list[2]}")


# TASK 3

number = 5.26459884

print(round(number, 2))


# TASK 4 

year = 2023
quantity = 3
price = 450

print(f"I've bought {quantity} footballs for {float(price)} £, in the year {year}")


# TASK 5

sentence = "I've bought 3 footballs for 450.00 £, in the year 2023"

for i in sentence:
    print(i)
    break

# TASK 6

sentence = "I have bought 3 footballs"

print(len(sentence))


# TASK 7

from datetime import datetime

current_date = datetime.now().date()
print(current_date)


# TASK 8

import random

print(random.randint(1, 100))


# TASK 9

import random

numbers = []

numbers.append(int(input("Enter the first number: ")))
numbers.append(int(input("Enter the second number: ")))

numbers.sort()

print(f"The random number from the range from {numbers[0]} to {numbers[1]} is: {random.randint(numbers[0], numbers[1])}")


# TASK 10

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))


print(f"{number_1} + {number_2} = {number_1 + number_2}")