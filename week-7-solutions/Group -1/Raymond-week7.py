print("My","Name","is","King",sep="$$")

names=input("enter three names:").split()
print("Name1:",names[0])
print("Name2:",names[1])
print("Nmae3:",names[2])

number=5.26459884
print(f"{number:.2f}")

year=2023
quantity=3
price=450
print(f"I have bought {quantity} footballs for {price:.2f}$ , in the year {year}")

list1="I have bought 3 footballs for 450.00$ , in the year 2023"
print(list1[0])

list2="I have bought 3 footballs"
print(len(list2))

from datetime import date
print(date.today())

import random
print(random.randint(1,100))

num1= float(input("enter a number"))
num2=float(input("enter a number"))
randomnumber=random.uniform(num1,num2)
print(randomnumber)