import datetime
import random
print("My", "Name", "Is", "King", sep="$$")
names = input("Enter three Names: ").split()
name1, name2, name3 = names
print("Name1:", name1)
print("Name2:", name2)
print("Name3:", name3)
number = 5.26459884
print(format(number, ".2f"), format(number, ".4f"), int(number), end="$")
year = 2023
quantity = 3
price = float(450)
sentence = f"I have bought {quantity} footballs for {format(price, ".2f")}£, in the year {year}"
print(f"\n{sentence}")
first_char = sentence[0]
print(first_char)
sentence2 = f"I have bought {quantity} footballs"
print(len(sentence2))
today = datetime.datetime.now()
print(today)
random_number = random.randint(1,100)
print(random_number)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(random.randint(num1, num2))
total = num1 + num2
print(total)



