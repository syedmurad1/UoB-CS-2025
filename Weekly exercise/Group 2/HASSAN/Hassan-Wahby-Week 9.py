#q1
number_check = int(input("please enter a number"))
if number_check > 0:
    print("number is positive")
elif number_check == 0:
       print("number is equal to 0")
else:
      print("number is negative")

#q2
grade = int(input("please enter your grade"))
if  70 <= grade <= 100:
    print("1st")
elif 60 <= grade <= 69:
    print("2.1")
elif 50 <= grade <= 59:
    print("2.2")
elif 40 <= grade <= 49:
    print("3rd")
elif 0 <= grade <= 39:
    print("F")
else:
    print("grade entered is not within 0-100")

#q3
current_year = int(input("please enter the amount of days in the current calendar year"))
if current_year == 365:
    print("the current year is not a leap year")
elif current_year == 366:
    print("the current year is a leap year")
else:
    print("the amount of days entered is not equivalent to any year")

#q4
age = int(input("please enter your age"))
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

#q5
number = int(input("enter a number: "))
if number % 11 == 0:
    if number % 5 == 0:
        print(number , "is divisible by 11 and 5")
else:
    print(number ,"is not divisible by 11 and 5")

#q6
electricity_bill = int(input("please enter the amount of units consumed: "))

first_unit = electricity_bill * 0.50
second_unit = ((electricity_bill - 100 ) * 0.75) + (100 * 0.5)
third_unit = (electricity_bill - 200 ) * 1.2 + (100 * 0.5) + (100 * 0.75)
final_unit = ((electricity_bill - 300 ) * 1.5 ) + (100 * 0.5) + (100 * 0.75) + (100  * 1.2)
if electricity_bill <= 100:
    print("your electricity bill is: ", first_unit)
elif 100 < electricity_bill <= 200:
     print("your electricity bill is: ", second_unit)
elif 200 < electricity_bill <= 300:
     print("your electricity bill is: ", third_unit)
elif electricity_bill > 300:
     print("your electricity bill is: ", final_unit)
else:
     print("the number of units consumed is incorrect, please try again")
    
#q7
n1, n2 = map(int, input("please input 2 numbers").split())
operator = input("please input operator")

if operator == "+":
   print(n1 + n2)
elif operator == "-":
   print(n1 - n2)
elif operator == "/":
   print(n1 / n2)
elif operator == "*":
   print(n1 * n2)
else:
   print("operator not recognised")

january = "31"
february = "28"
march = "31"
april = "30"
may = "31"
june = "30"
july = "31"
august = "31"
september = "30"
october = "31"
november = "30"
december = "31" 

#q8
month = input("Enter a month: ").lower()

if month in ["january", "march", "may", "july", "august", "october", "december"]:
    print("31 days")
elif month in ["april", "june", "september", "november"]:
    print("30 days")
elif month == "february":
    print("28 days")
else:
    print("Invalid month")


