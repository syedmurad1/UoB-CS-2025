#1.
num1=int(input("input number: "))
if num1>0:
    print("positive")
elif num1<0:
    print("negative")
else:
    print("zero")

#2.
grade=int(input("input grade: "))
if 70<=grade<=100:
    print("1st")
elif 60<=grade<=69:
    print("2.1")
elif 50<=grade<=59:
    print("2.2")
elif 40<=grade<=49:
    print("3rd")
elif 0<=grade<=39:
    print("F")
else:
    print("invalid grade")

#3.
year=int(input("input year: "))
if year%400==0:
    print("leap year")
elif year%100==0:
    print("not a leap year")
elif year%4==0:
    print("leap year")
else:
    print("not a leap year")

#4.
age=int(input("input age: "))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")

#5.
num2= int(input("input number: "))
if num2%5==0 and num2%11==0:
    print("divisible by both 5 and 11")
else:
    print("not divisible by both")

#6.
units=int(input("input units consumed: "))
bill = 0
if units<=100:
    bill=units*0.50
elif units<=200:
    bill=100*0.50+(units-100)*0.75
elif units<=300:
    bill=100*0.50+100*0.75+(units-200)*1.20
else:
    bill =100*0.50+100*0.75+100*1.20+(units-300)*1.50
print("total bill:", bill)

#7.
num3 = int(input("input first number: "))
num4 = int(input("input second number: "))
operator = input("input operator (+, -, *, /): ")

if operator=="+":
    print(num3+num4)
elif operator=="-":
    print(num3-num4)
elif operator=="*":
    print(num3*num4)
elif operator=="/":
    print(num3/num4)
else:
    print("invalid operator")

#8.
month=int(input("input month: "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print(31)
elif month==4 or month==6 or month==9 or month==11:
    print(30)
elif month==2:
    print(28)
else:
    print("invalid month")