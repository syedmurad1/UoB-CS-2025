print ("My", "name", "is", "king", sep="$$")
Name1, Name2, Name3=input("Enter 3 names seperated by space: ").split()
print (Name1)
print (Name2)
print (Name3)
Num1 =float(input("Please type in your number with decimal: "))
print (f"{Num1: .3}")
year=input("Please type in the year: ")
quantity=input("Please type in the quantity: ")
price=input("Please type in tha price: ")
x=(f"I have bought {quantity} footballs for {price}, in {year}.")
first_character=x[0] 
print(x)
lenght=len(x)
from datetime import date, datetime
today= date.today()
import random
rannum1= random.randint(1,100)
usernum1=int(input("Please type in your first number: "))
usernum2=int(input("Please type in your second number: "))
rannum2=random.randint(usernum1,usernum2)
print(rannum2)
sumnum1=usernum1+rannum1
sumnum2=usernum2+rannum2
print(sumnum1)
print(sumnum2)