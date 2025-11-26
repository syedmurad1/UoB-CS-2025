#program to check if the num is postive or negative or zero
n =int(input("please enter num"))
if n > 0:
  print("postive")
elif n < 0: 
     print("negative")
else:
 print("zero")


grade = int(input("please enter your grade: "))

if grade >= 70:
    print("1st")
elif grade >= 60:
    print("2.1")
elif grade >= 50:
    print("2.2") 
elif grade >= 40:
    print("3rd")
elif grade >= 0:
    print("Fail")
else:
    print("invalid grade")  


age = int(input("How old are you "))
if age >= 18:
    print("you can vote")
else:
    print("you can vote")    

num = int(input("type in your number "))
if num % 5 ==  0 and num % 11 == 0:
    print("it is divisable by 5 and 11")
else:
    print("it is not divisiable by 5 and 11")    

units= int(input("input the amount of units used"))

if units <= 100:
    bill = units * 0.50
elif units <= 200:
    bill = (100 * 0.50) + ((units - 100) * 0.75)
elif units <= 300:
    bill = (100 * 0.50) + (100 * 0.75) + ((units - 200) * 1.20)
else:
    bill = (100 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 300) * 1.50)    

print(bill)

num1 = int(input("please enter your first number"))

num2 = int(input("please enter your second number"))

operator = int(input("chosse your operator by typing these numbers 1 = +, 2 = - ,3 = *, 4 = /"))

if operator == 1 :
    print(num1 + num2)
elif operator == 2:
    print(num1 - num2)
elif operator == 3:
    print(num1 * num2)
elif operator == 4:
    print(num1 / num2)            
else:
    print("invalid operator")



month = int(input("Enter the month number (1-12): "))

if month == 2:
    print("28 days")
    
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
    
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 days")
    
else:
    print("Invalid month number")