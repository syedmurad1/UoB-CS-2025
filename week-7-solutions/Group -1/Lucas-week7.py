1 #print("my", "Name" "is" "king", sep="$$")
#print("mynameisking" ,end="!-!")

2 #name1,name2,name3=input("Enter three names:").split()
#print(f"Name1:{name1}")
#print(f"Name2:{name2}")
#print(f"Name3:{name3}")

num=5.26487337
print(f"{num:.2f}")

year=2023
quantity=3
price=float(450)


print(f"I have bought {quantity} footballs for {price:.2f} £, in the year {year}.")

sentence = "I have bought 3 footballs for 450.00 £, in the year 2023."
first_char = sentence[0]
print(first_char)

short_sentence = "I have bought 3 footballs."
length = len(short_sentence)
print(length)


from datetime import date

current_date = date.today()
print(current_date)

import random

random_number = random.randint(1, 100)
print(random_number)

import random


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

random_between = random.randint(min(num1, num2), max(num1, num2))
print(f"Random number between {num1} and {num2}: {random_between}")








