#1 Provide a python example of following arithmetic operators: + , - , * , / , % , ** , //
print(f"10 + 5 = {10 + 5}")
print(f"10 - 5 = {10 - 5}")
print(f"10 * 5 = {10 * 5}")
print(f"10 / 5 = {10 / 5}")
print(f"10 % 3 = {10 % 3}")
print(f"10 ** 2 = {10 ** 2}")
print(f"10 // 3 = {10 // 3}")

#2 Provide a python example of following assignment operators: = , += , -= , *= , /= , %= , //= , **= , &= , |= , ^= , >>= , <<= , :=
b=7
print(f"Initial value of b is:{b}")
b+=3
print(f"After 7+=3, value of b is:{b}")
b-=2
print(f"After 10-=2, value of b is:{b}")
b*=4
print(f"After 8*=4, value of b is:{b}")
b=28
b/=2
print(f"After 28/=2, value of b is:{b}")
b%=5
print(f"After 14%=5, value of b is:{b}")
b//=2
print(f"After 4//=2, value of b is:{b}")
b**=3
print(f"After 2**=3, value of b is:{b}")
b=int(b)
b&=3
print(f"After 8&=3, value of b is:{b}")
b|=2
print(f"After 0|=2, value of b is:{b}")
b^=5
print(f"After 2^=5, value of b is:{b}")
b>>=1
print(f"After 7>>=1, value of b is:{b}")
b<<=2
print(f"After 3<<=2, value of b is:{b}")
if b:=7:
    print(f"Value of b after walrus operator is:{b}")

#3 Provide a python example of following comparison operators: == , != , > , < , >= , <=
c=10
if c==10:
    print(f"c is equal to 10")
if c!=5:
    print(f"c is not equal to 5")
if c>5:
    print(f"c is greater than 5")
if c<15:
    print(f"c is less than 15")
if c>=10:
    print(f"c is greater than or equal to 10")
if c<=20:
    print(f"c is less than or equal to 20")
    
#4 Provide a python example of following logical operators: and , or , not
d=4
if d==4 and d<10:
    print(f"d is 4 and less than 10")
if d==4 or d>10:
    print(f"d is 4 or greater than 10")
if not d>10:
    print(f"d is not greater than 10")

#5 Provide a python example of following identity operators: is , is not
a=[1,2]
b=[1,2]
print(f"a is b:{a is b}")
print(f"a is not b:{a is not b}")
    
#6 Provide a python example of following membership operators: in , not in
f=[1,2,3,4,5]
if 3 in f:
    print(f"3 is in the list f")
if 6 not in f:
    print(f"6 is not in the list f")

#7 Provide a python example of following bitwise operators: & , | , ^ , ~ , << , >>
print(5 & 3)
print(5 | 2)
print(5 ^ 3)
print(~5)
print(5 << 1)
print(5 >> 1)

#8 Assign the value 10 to a variable a. Use arithmetic and assignment operators to:
a=10
print(f"a is {a}")
a+=5
print(f"Add 5 to a is {a}")
a-=3
print(f"Subtract 3 from a is {a}")
a*=2
print(f"Multiply a by 2 is {a}")
a//=4
print(f"Divide a by 4 is {a}")

#9 Define two variables, x = 7 and y = 12. Use comparison operators to check if:
x=7
y=12
result1= x>y
result2= x<y or x==y
result3= x<y and x!=y
result4= x>y or y>10
print(f"The result of x is greater than y is:{result1}")
print(f"The result of x is less or equal to y is:{result2}")
print(f"The result of x is less than y and x is not equal to 7 is:{result3}")
print(f"The result of x is greater than y or y is greater than 10 is:{result4}")

#10 Define a list my_list = [1, 2, 3, 4, 5]. Check if:
my_list=[1,2,3,4,5]
print(f"Is 3 in my list:{3 in my_list}")
print(f"Is 10 not in my list:{10 not in my_list}")
a=[1,2]
b=[1,2]
print(f"a is b:{a is b}")
print(f"a == b:{a == b}")