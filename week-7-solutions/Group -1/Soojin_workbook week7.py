# 1. Use the print () function to display the $$ separator between each string.
print("My", "Name", "Is", "King", sep="$$")

# 2. Write a program to take three names as input from a user in the single input() function call and
name1,name2,name3=input("Enter three Names: ").split()
print("Name1:", name1)
print("Name2:", name2)
print("Name3:", name3)

# 3. Display float number (5.26459884) with 2 decimal places using print ().
num=5.26459884
print("%.2f" %num)

# 4. Write a program to use f-strings method to format the following three variables as per the expected output.
year=2023
quantity=3
price=450
sentence=f"I have bought {quantity} footballs for {price:.2f}£, in the year {year}."
print(sentence)

# 5. Get the first character from the following sentence: I have bought 3 footballs for 450.00 £, in the year 2023.
print(sentence[0])

# 6. Get the length of the following sentence: I have bought 3 footballs.
print(len("I have bought 3 footballs."))

# 7. Get the current date using today ().
from datetime import datetime
print(datetime.today())

# 8. Generate a random number between 1 and 100.
import random
print(random.randint(1, 100))

# 9. Write a program to take two numbers as input from a user and generate a random number between those two numbers.
num1,num2=map(int, input("Input two numbers: ").split())
num1,num2=sorted((num1, num2))
print(random.randint(num1, num2))

# 10. Write a program to take two numbers as input from a user and program should add those two numbers and display.
num3,num4=map(int,input("Input two numbers: ").split())
print(num3+num4)