x = int(5) #question 1
y = int(2)

print(x + y) #question 2
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = int(6)
y = int(3)

x = y
print(x)

x += y
print(x)

x -= y
print(x)

x *= y
print(x)

x /= y
print(x)

x %= y
print(x)

x //= y
print(x)

x **= y
print(x)

x = int(x)

x &= y
print(x)

x |= y
print(x)

x ^= y
print(x)

x >>= y
print(x)

x <<= y
print(x)

if (x := y) > 1:
    print("x is greater than 1")

x = 5 #question 3

print(x == 5)

print(x != 4)

print(x > 2)

print(x < 4)

print(x <= 5)

print(x >= 8)

print(True and True) #question 4
print(True or False)
print(not(True and False))

list_1 = [1, 2, 3] #question 5
list_2 = list_1
list_3 = [1, 2, 3]

print(list_1 is list_2)
print(list_1 is list_3)

a = "mohamed"
b = "mohamed"
print(a is not b)

list = [1, 2, 3, 4]
print(2 in list)
print(3 not in list)



print(8 & 4) #question 7
print(1 | 4)
print(2 ^ 6)
print(~(2 | 6))
print(2 << 4)
print(12 >> 8)

a = 10 #question 8
a += 5
a -= 3
a *= 2
a //= 4
print(a)


x = 7 #question 9
y = 12

print(x > y)
print(x <= y)
print((x < y) and (x != y))
print((x > y) or ( y > 10))


my_list = [1, 2, 3, 4, 5] #question 10
print(3 in my_list)
print(10 not in my_list)

a = [1, 2]
b = [1, 2]
print( a is b)
print( a == b)