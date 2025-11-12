#Week7 tasks

#1
myname = "My name is King" #name string
myname = myname.replace(" ", "$$") #replace spaces with empty string
print(myname) #print modified string

#2
names = input("Enter names: ")
name1, name2, name3 = names.split(" ") #split input string into three names
print("Name 1:", name1)
print("Name 2:", name2)
print("Name 3:", name3) 

#3
floatnum = 5.26459884
print(format(floatnum, ".2f")) #print float with 2 decimal places

#4
year = 2023
quantity = 3
price = 450
print(f"I have bought {quantity} footballs for {price}.00£, in the year {year}.") #formatted string output

#5
sen = "I have bought 3 footballs for 450.00£, in the year 2023."
print(sen[0]) #print first character

#6
sentence = "I have bought 3 footballs."
print(len(sentence)) #print length of string

#7
from datetime import date
today = date.today() #get today's date
print(today)

#8
import random
randnum = random.randint(1, 100) #generate random integer
print(randnum) #print

#9
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
randomnum = random.randint(num1, num2) #generate random integer
print(randomnum) #print

#10
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
sumnum = n1 + n2 #calculate
print("Sum:", sumnum) #print



#Week8 tasks

#1
x = 1+1
y = 3-5
z = 4*2
a = 8/4
b = 7%3
c = 2**3
d = 8//3
print(x, y, z, a, b, c, d) #print

#2
xx = 10
xx += 2
xx -= 3
xx *= 4
xx /= 5
xx %= 6
xx //= 2
xx **= 3
xx = int(xx)
xx &= 4
xx |= 5
xx ^= 6
xx >>= 1
xx <<= 2
print(xx) #print

#3
yy = 5
zz = 10
if (yy == 5):
    print("Equal")
if (zz != 6):
    print("Not equal")
if (yy > zz):
    print("Greater")
if (yy < zz):
    print("Lesser")
if (yy >= 5):
    print("Greater or Equal")
if (zz <= 10):
    print("Lesser or Equal")

#4
if (yy > 1 and zz == 10):
    print("Both rue")
if (yy > 1 or zz == 10):
    print("At least one true")
if not(yy < 1):
    print("yy is not less than 1")

#5
if (yy is 5):
    print("yy is 5")
if (yy is not zz):
    print("yy is not zz")

#6
if (yy in [0,11,54,9,5]):
    print("yy is in the list")
if (zz not in [0,11,54,9,5]):
    print("zz is not in the list")

#7
number = 15
number1 = 7
print(number&number1)
print(number|number1)
print(number^number1)
print(~number)
print(number<<2)
print(number>>2)

#8
a = 10
a += 5
a /= 3
a *= 2
a //= 4
print(a)

#9
x = 7
y = 12
if (x>y):
    print("x is greater than y")
if (x<=y):
    print("x is less than or equal to y")
if (x<y and x !=y):
    print("x is less than y and not equal to y")
if (x>y or x>10):
    print("x is greater than y or greater than 10")

#10
my_list = [1,2,3,4,5]
if (3 in my_list):
    print("3 is in the list")
if (10 not in my_list):
    print("10 is not in the list")
a = [1,2]
b = [1,2]
if (a is b):
    print("a is b")
if (a == b):
    print("a is equal to b")