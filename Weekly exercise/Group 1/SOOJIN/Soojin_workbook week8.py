# 1. Provide a python example of following arithmetic operators:
num1,num2=10,20
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1**num2)
print(num1//num2)

print("=======================================================")

# 2. Provide a python example of following assignment operators:
num1,num2=10,20
print(num1)
num1+=num2
print(num1)
num1-=num2
print(num1)
num1*=num2
print(num1)
num1/=num2
print(num1)
num1%=num2
print(num1)
num1//=num2
print(num1)
num1**=num2
print(num1)

print("=======================================================")

num1,num2=10,20
num1&=num2
print(num1)
num1|=num2
print(num1)
num1^=num2
print(num1)
num1>>=num2
print(num1)
num1<<=num2
print(num1)
print(num1:=num2)

print("=======================================================")

# 3. Provide a python example of following comparison operators:
num1,num2=10,20
print(num1==num2)
print(num1!=num2)
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)

print("=======================================================")

# 4. Provide a python example of following logical operators:
a,b=True,False
print(a and b)
print(a or b)
print(not a)

print("=======================================================")

# 5.Provide a python example of following identity operators:
num1,num2=10,20
print(num1 is num2)
print(num1 is not num2)

print("=======================================================")

# 6. Provide a python example of following membership operators:
numbers=(10,20,30,40,50)
print(10 in numbers)
print(100 not in numbers)

print("=======================================================")

# 7. Provide a python example of following bitwise operators:
num1,num2=10,20
print(num1&num2)
print(num1|num2)
print(num1^num2)
print(~num1)
print(num1<<10)
print(num1>>10)

print("=======================================================")

# 8. Assign the value 10 to a variable a.
# Use arithmetic and assignment operators to:
a=10
# Add 5 to a.
print(a:=a+5)
# Subtract 3 from a.
print(a:=a-3)
# Multiply a by 2.
print(a:=a*2)
# Divide a by 4 (use floor division).
print(a:=a//4)
# Print the result of a.
print(a)

print("=======================================================")

# 9. Define two variables, x = 7 and y = 12.
# Use comparison operators to check if:
x,y=7,12
# x is greater than y
print(x>y)
# x is less than or equal to y
print(x<=y)
# Combine these comparisons using logical operators to:
# Check if x is less than y and x is not equal to y
print(x<y and x!=y)
# Check if x is greater than y or y is greater than 10
print(x>y or y>10)
# Print the results of each check.
print(x,y)

print("=======================================================")

# 10. Define a list my_list = [1, 2, 3, 4, 5].
# Check if:
my_list=[1,2,3,4,5]
# The number 3 is in my_list.
print(3 in my_list)
# The number 10 is not in my_list.
print(10 not in my_list)

print("=======================================================")

# 11. Define two variables, a = [1, 2] and b = [1, 2].
# Check if:
a=[1,2]
b=[1,2]
# a is b
print(a is b)
# a == b
print(a==b)