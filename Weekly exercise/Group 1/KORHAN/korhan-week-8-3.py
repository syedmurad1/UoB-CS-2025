# I didn't provided all the examples for the operators because I know how to use them well.

# Task 1
a = 5 + 3

# Task 2
a += 5

# Task 3
if a == 13:
    print("The number a is equal to 13")

# Task 4
b = int(input("Input a number please: ")) 

if not(b == 34):
    print("The number you inputted is not 34")

# Task 5
if b is b:
    print("Suprisingly b is equal to b")     

# Task 6
a_list = [1, 2, 3, 4, 5]

if 3 in a_list:
    print("The number 3 is in the list")        

# Task 7
print(f"The bitwise not of the number 5 is {~5}")  

# Task 8
c = 10
c += 5
c -= 3
c *= 2
c //= 4
print(f"The final result of the number c is {c}")

# Task 9
x = 7
y = 12

if x > y:
    print("x is greater than y")

if x <= y:
    print("x is less than or equal to y")

if x < y and x != y:
    print("x is less than y and x is not equal to y")

if x > y or y > 10:
    print("x is greater than y or y is greater than 10")          
    
# Task 10
my_list = [1, 2, 3, 4, 5]

if 3 in a_list:
    print("The number 3 is in the list")  

if 10 not in a_list:
    print("The number 10 isn't in the list")  

n = [1, 2] 
r = [1, 2]  

if n is r:
    print("n is r")

if n == r:
    print("n is equal to r")    

print("The difference between the two operators is while (==) checks for if they are equal to each other in value" \
", (is) checks if they refer to the same object")    