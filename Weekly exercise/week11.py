# Calculating the sum of numbers from 1 to 10

t = 0
for i in range(1, 11):
    t += i
print("Total:", t)










# Create password validation with while loop.

password = ""
while password != "python123":
    password = input("Enter your password: ")
print("Access granted!")



















# Calculate sum of all numbers from 1 to a given number.

s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
# print("\n")
print("Sum is: ", s)







# Write a Python program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 100, then skip it and move to the following number
# If the number is greater than 500, then stop the loop

# numbers = [12, 75, 100, 150, 180, 145, 525, 50]

numbers = [12, 75, 100, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 100:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)




# Reverse an integer number
# number - 598762


num = 598762
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("revere Number ", reverse_number)


# Write a Python code to print the following number pattern using a while and for loop.

# Using a while loop
print("Using a while loop:")
rows = 5
while rows > 0:
    print("*" * rows)
    rows -= 1

# Using a for loop
print("\nusing a for loop:")
for rows in range(5, 0, -1):
    print("*" * rows)


# Write a Python program to print the multiplication table of a given number. The user should input the number, and the program should print the table from 1 to 15.

# Ask the user to input a number
number = int(input("Enter a number to print its multiplication table: "))

# Using a for loop
print("\nmultiplication Table:")
for i in range(1, 16):
    print(f"{number} x {i} = {number * i}")


