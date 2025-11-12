#1 Use the print () function to display the $$ separator between each string.
print(f"My","Name","Is","King",sep='$$')

#2Write a program to take three names as input from a user in the single input() function call
name=input()
name_list=name.split()
print(f"Name1:{name_list[0]}",end="\n")
print(f"Name2:{name_list[1]}",end="\n")
print(f"Name3:{name_list[2]}",end="\n")

#3 Display float number (5.26459884) with 2 decimal places using print ().
float_num=5.2645984
print(f"{float_num:.2f}")

#4 Write a program to use f-strings method to format the following three variables as per
year=2023
quantity=3
price=450
print(f"I have bought {quantity} footballs for {price}£, in the year {year}.")

#5 Get the first character from the following sentence
sentence = "I have bought 3 footballs for 450.00 £, in the year 2023."
first_char = sentence[0]
print(f"The first character is: {first_char}")

#6 Get the length of the following sentence
sentence1="I have bought 3 footballs."
words1=sentence1.split()
print(f"the length of the sentence is:{len(words1)}")

#7 Get the current date using today ().
from datetime import date
current_date = date.today()
print(f"Today's date is: {current_date}")

#8 Generate a random number between 1 and 100.
import random
random_num=random.randint(1,100)
print(f"The random number is:{random_num}")

#9 Write a program to take two numbers as input from a user and generate a random number between those two numbers.
num1=input("Pleacs enter first number:")
num2=input("Please enter second number:")
if int(num1)>int(num2):
    random_num2=random.randint(int(num2),int(num1))
else:
    random_num2=random.randint(int(num1),int(num2))
print(f"The random number between {num1} and {num2} is:{random_num2}")

#10 Write a program to take two numbers as input from a user and program should add those two numbers and display.
num3=float(input("Please enter a number:"))
num4=float(input("Please enter another number:"))
sum=num3+num4
print(f"The sum of {num3} and {num4} is:{sum}")