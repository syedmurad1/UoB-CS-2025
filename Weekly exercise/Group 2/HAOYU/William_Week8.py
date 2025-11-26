#Question1 Provide a python example of following arithmetic operators.
print('"+" means addition, the result of "1 + 2" =',1+2)
print('"-" means subtraction, the result of "6 - 2" =',6-2)
print('"*" means multiplication, the result of "3 * 4" =',3*4)
print('"/" means division, the result of "10 / 5" =',10/5)
print('"%" means taking the remainder, the result of "20 % 3" =',20%3)
print('"**" means exponentiation, the result of "6 ** 2" =',6**2)
print('"//" means floor division, the result of "30 // 4" =',30//4)

#Question2 Provide a python example of following assignment operators.
num=3#Assignment
num+=5#num=num+5
num-=5#num=num-5
num*=5#num=num*5
num/=5#num=num/5
num%=5#num=num%5
num//=5#num=num//5
num**=5#num=num**5
num=8
num&=5#num=num&5
num|=5#num=num｜5
num^=5#num=num^5
num>>=5#num=num>>5
num<<=5#num=num<<5

#Question3 Provide a python example of following comparison operators
x, y = 3,4
print(x == y)#False
print(x != y)#True
print(x > y)#False
print(x < y)#True
print(x >= 3)#True
print(y <= 4)#True

#Question4 Provide a python example of following logical operators
a, b = True, False
print(a and b)#False
print(a or b)#True
print(not a)#False

#Question5 Provide a python example of following identity operators
a = [3, 4]
b = [3, 4]
c = a
print(a is b)#False
print(a is c)#True
print(a is not b)#True

#Question6 Provide a python example of following membership operators
num_list = [1,2,3,4,5]
print(5 in num_list)#True
print(0 not in num_list)#True

#Question7 Provide a python example of following bitwise operators
a = 6#110 in binary
b = 3#011 in binary
print("a & b =", a & b)#AND → 110 & 011 = 010 → 2
print("a | b =", a | b)#OR  → 110 | 011 = 111 → 7
print("a ^ b =", a ^ b)#XOR → 110 ^ 011 = 101 → 5
print("~a =", ~a)#NOT → -(a+1) → -7
print("a << 1 =", a << 1)#Left shift  → 110 → 1100 → 12
print("a >> 1 =", a >> 1)#Right shift → 110 → 11   → 3

#Question8
a=10
a+=5
a-=3
a*=2
a//=4
print(a)#a=6

#Question9
x,y=7,12
print("x > y ->",x>y)#False
print("x <= y ->",x<=y)#True
print("x < y and x != y ->",x<y and x!=y)#True
print("x > y or y > 10 ->",x>y or y>10)#True

#Question10
my_list = [1,2,3,4,5]
print(3 in my_list)#True
print(10 not in my_list)#True
a = [1,2]
b = [1,2]
print("a is b ->",a is b)#False
print("a == b ->",a == b)#True