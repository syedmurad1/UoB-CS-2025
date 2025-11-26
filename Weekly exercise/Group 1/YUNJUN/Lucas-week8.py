#1

a = 7
b = 3


print(f"{a} + {b} = {a + b}")

print(f"{a} - {b} = {a - b}")

print(f"{a} * {b} = {a * b}") 

print(f"{a} / {b} = {a / b}")

print(f"{a} % {b} = {a % b}")  

print(f"{a} ** {b} = {a ** b}")

print(f"{a} // {b} = {a // b}") 


#2 the use of "="
a=b
print(a)

#3 the use of"=="
if b==3:
    print("b is equal to 3")

#4 the use of "and"
c=5
d=6
result=(c+d==11)and(d>c)
print(result)

#5 the use of "is"
e=8
f=e
print(f is e)

#6 the use of "in"
list=[1,2,3,4]
print(4 in list)

#7 the use of"&"
x=5
y=9
print(x&y)

a = 10

# 8
a += 5   
a -= 3    
a *= 2    
a //= 4  

print(a)

#9
x = 7
y = 12


print("x is greater than y:", x > y)               
print("x is less than or equal to y:", x <= y)     


print("x is less than y and x is not equal to y:", (x < y) and (x != y))  
print("x is greater than y or y is greater than 10:", (x > y) or (y > 10)) 

#10
my_list = [1, 2, 3, 4, 5]


print("Is 3 in my_list?:", 3 in my_list)          
print("Is 10 not in my_list?:", 10 not in my_list)

a = [1, 2]
b = [1, 2]


print("Is a the same object as b?:", a is b)      
print("Do a and b have the same value?:", a == b)
