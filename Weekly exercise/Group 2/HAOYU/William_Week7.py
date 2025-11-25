#Question1 Use the print () function to display the $$ separator between each string.
print("My","Name","Is","King",sep="$$")

#Question2 Write a program to take three names as input from a user in the single input() function call.
names=input("Enter Three Names: ")
names=names.split(" ")
print(f"Name1: {names[0]}")
print(f"Name2: {names[1]}")
print(f"Name3: {names[2]}")

#Question3 Display float number (5.26459884) with 2 decimal places using print ().
num=5.26459884
print("%.2f"%(num))

#Question4 Write a program to use f-strings method to format the following three variables as per the expected output.
year=2023
quantity=3
price=450
print(f"I have bought {quantity} footballs for {price:.2f} £, in the year {year}")

#Question5 Get the first character from the following sentence: I have bought 3 footballs for 450.00 £, in the year 2023.
sentence1 = "I have bought 3 footballs for 450.00 £, in the year 2023."
first_char = sentence1[0]
print(f'The first character is "{first_char}".')

#Question6 Get the length of the following sentence: I have bought 3 footballs.
sentence2="I have bought 3 footballs"
print(f"The sentence has {len(sentence2)} characters.")

#Question7 Get the current date using today ().
from datetime import date
today=date.today()
print(f"The date of today is {today}.")

#Question8 Generate a random number between 1 and 100.
import random
random_num=random.randint(1,100)
print(f"The random number between 1 and 100: {random_num}")

#Question9 Write a program to take two numbers as input from a user and generate a random number between those two numbers.
import random
numbers1=input("Enter two numbers: ")
numbers1=list(map(int,numbers1.split()))
new_num=random.randint(numbers1[0],numbers1[1])
print(f"The random number between those two numbers: {new_num}")

#Question10 Write a program to take two numbers as input from a user and program should add those two numbers and display.
numbers2=input("Enter two numbers: ")
numbers2=list(map(int,numbers2.split()))
sum=numbers2[0]+numbers2[1]
print(f"The sum of those two numbers: {sum}")