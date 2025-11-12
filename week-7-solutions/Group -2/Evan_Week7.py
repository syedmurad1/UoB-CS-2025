import datetime, random

#1 Use the print() function to display the $$ separator between each string
print("My", "Name", "Is", "King", sep='$$')

print("My", "Name", "Is", "King", sep='')

print("My", "Name", "Is", "King", sep='', end='@!\n')

#2 Write a program to take three names as input from a user in the single input() function call
'''name1, name2, name3 = input("Enter three names: ").split()

print(f"Name1: {name1}")
print(f"Name2: {name2}")
print(f"Name3: {name3}")'''

#3 Display float number (5.26459884) with 2 decimal places using print()
num = 5.26459884

print("%.2f" %(num))

#4 Write a program to use f-string method to format the following three variables as per the expected output
year = 2023
quantity = 3
price = 450

print(f"I have bought {quantity} footballs for{price: .2f} £, in the year {year}.")

#5 Get the first character from the following sentence:
sentence_1 = "I have I have bought 3 footballs for 450.00 £, in the year 2023."
print(sentence_1[0])

#6 Get the length of the following sentence:
sentence_2 = "I have bought 3 footballs."
print(len(sentence_2))

#7 Get the current date using today()
today_date = datetime.datetime.today()
print(today_date)

#8 Generate a random number between 1 and 100
rand_num = random.randint(1, 100)
print(rand_num)

#9 Write a program to take two numbers as input from a user and generate a random number between those two numbers
a = int(input("Enter the first natural number: "))
b = int(input("Enter the second natural number: "))

if a > b:
    rand_ab = random.randint(b, a)
    print(f"The random number generated between {b} and {a}: {rand_ab}")
else:
    rand_ab = random.randint(a, b)
    print(f"The random number generated between {a} and {b}: {rand_ab}")

#10 Write a program to take two numbers as input from a user and program should add those two numbers and display
c = int(input("Enter the first integer: "))
d = int(input("Enter the second integer: "))

sum = c+d

print(f"The sum of the two integers: {sum}")