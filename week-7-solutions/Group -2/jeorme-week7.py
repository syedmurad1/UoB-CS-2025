print("My", "Name", "Is", "King", sep="$$")

names = input("Enter three Names: Ali Syed Tom ").split()

print(f"Name1: {names[0]}")
print(f"Name2: {names[1]}")
print(f"Name3: {names[2]}")

num = 5.26459884
print(f"{num:.2f}")

year = 2023
quantity = 3
price = 450
print(f"I have bought {quantity} footballs for {price:.2f} £, in the year {year}.")

sentence = "I have bought 3 footballs for 450.00 £, in the year 2023."
first_char = sentence[0]
print(first_char)

sentence = "I have bought 3 foptballs."
length = len(sentence)
print(length)

from datetime import datetime

current_date = datetime.today()
print(current_date)

import random

random_number = random.randint(1, 100)
print(random_number)

import random

num1 = int(input("first number："))
num2 = int(input("second number："))
if num1 > num2:
    num1, num2 = num2, num1
random_num = random.randint(num1, num2)
print(f"output：{random_num}")

num1 = float(input("first number："))
num2 = float(input("second number："))
sum_result = num1 + num2
print(f"sum：{sum_result}")

