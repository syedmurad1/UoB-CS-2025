print("My", "Name", "Is", "King", sep=("$$")) #question 1

name1, name2, name3 = input("Enter three names ").split() #question 2
print(f"Name1: {name1}", f"Name2: {name2}", f"Name3: {name3}", sep=("\n"))

number = 5.26459884 #question 3
print(f"{number:.2f}")

year = 2023  #question 4 and 5
quantity = 3
price = 450
sentence = f"I have bought {quantity} footballs for {price:.2f}£, in the year {year}"
print(sentence[0])

sentence = "I have bought 3 footballs" #question 6
print(len(sentence))

import datetime      #question 7
today = datetime.date.today()
print(today)

import random        #question 8
print(random.randint(1, 100))

number1, number2 = map(int, input("Please enter 2 numbers: ").split())   #question 9
import random
print(random.randint(number1, number2))

number1, number2 = map(int, input("please enter 2 numbers: ").split())
print(number1 + number2)
