1.
num=int(input('enter a number'))
if num>0:
    print("positive")
elif num==0:
    print("zero")
elif num<0:
    print("negative")
2.
num1=int(input("enter the student's score"))
if 70<=num1<=100:
    print("1st")
elif 60<=num1<=69:
    print("2.2")
elif 50<=num1<=59:
    print("2.2")
elif 40<=num1<=49:
    print("3st")
elif 0<=num1<=39:
    print("F")
3.
year=int(input("enter a year"))
if year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
4.
age=int(input("enter your age"))
if age<18:
    print("you are unable to vote")
elif age>=18:
    print("you are eligible to vote")
5.
num2=int(input("enter a number"))
if num2%5==0 and num2%11==0:
    print("The number is divided by 5 and 11")
else:
    print("the number can't be divided by 5 and 11")
6.
units= int(input("enter the number of units consumed"))
if units<=100:
    bill=units*0.50
elif 100<=units<=200:
    units=units-100
    bill=50+units*0.75
elif 200<=units<=300:
    units=units-200
    bill=50+75+units*1.2
elif units>=300:
    units=units-300
    bill=50+75+120+units*1.5
print(f"your bill is {bill}")
7.
num3=float(input("enter a number"))
num4=float(input("enter another number"))
operation=input("enter an operation from'+ - * /")
if operation=="+":
    print(f"the result is {num1+num2}")
elif operation=="-":
    print(f"the result is {num3-num4}")
elif operation=="*":
    print(f"the result is {num3*num4}")
elif operation=="/":
    if num4!=0:
       print(f"the result is {num3/num4}")
    else:
        print("the divisor can't be zero")
8.
month=input("enter a month")
if month in ["January","March","May","July","August","Octuber","December"]:
    print(f"{month} has 31 days")
elif month in ["April","June","September","November"]:
    print(f"{month} has 30 days")
elif month=="February":
    print(f"{month} has 28 days")




    