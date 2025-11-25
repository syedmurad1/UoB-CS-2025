# Arithmetic Operators
# x = "Ol" + "eks"

# y = 5 - 3

# z = 4 * 4

# a = 20 / 10

# b = 60 % 7

# c = 10**2

# d = 13 // 3

# print("Hello my name is", x)
# print(y)
# print(z)
# print(a)
# print("Remainder is", b)
# print("10 sqrd is", c)
# print("13 divded by 3 rounded down is", d)

# # Assignment Operators
# e = 6
# e += 6
# print(e)

# e -= 3
# print(e)

# e *= 9
# print(e)

# e /= 3
# print(e)

# e %= 5
# print(e)

# e //= 1.1
# print(e)

# e **= 5
# print(e)

# e = 56

# e &= 6
# print(e)

# e |= 12
# print(e)

# e ^= 7
# print(e)

# e >>= 50
# print(e)

# e <<= 15
# print(e)

# print(e:= 5)

# # Comparison Operators
# x = 5
# y = 12

# print(x == y)
# print(y != x)
# print(x < y)
# print(y > x)
# print(x <= y)
# print(y >= x)

# # Logical Operators
# x = 1
# y = -1
# print(x < 10 and y > 10)
# print(x < 10 or y > 10)
# print(not(x > 10 and y > 0))

# # Identity Operators
# print(x is y)
# print(x is not y)

# # Membership Operators
# list1 = ["Oleks", "Evan", "Nandaiyoo"]
# x = "Evan"
# y = "Paris"

# print(x in list1)
# print(y not in list1)

# # Bitwise Operators
# print(5 & 3)
# print(5 | 4)
# print(7^8)
# print(~3)
# print(5 >> 2)
# print(3 << 1)

# Assign the value 10 to a variable a.
#   Use arithmetic and assignment operators to:
#   Add 5 to a.
#   Subtract 3 from a.
#   Multiply a by 2.
#   Divide a by 4 (use floor division).
#   Print the result of a.

a = 10

a = a + 5
a = a - 3
a = a * 2
a = a // 4
print(a)

# Define two variables, x = 7 and y = 12.
        # Use comparison operators to check if:
        # x is greater than y
        # x is less than or equal to y
        # Combine these comparisons using logical operators to:
        # Check if x is less than y and x is not equal to y
        # Check if x is greater than y or y is greater than 10
        # Print the results of each check.

x = 7
y = 12

if x > y:
    print("Yey!")
elif x <= y:
    print("Noh!")

print(x < y and x != y)
print(x > y or y > 10)


# Define a list my_list = [1, 2, 3, 4, 5].
    # Check if:
    # The number 3 is in my_list.
    # The number 10 is not in my_list.
    # Define two variables, a = [1, 2] and b = [1, 2].
    # Check if:
    # a is b
    # a == b

my_list = [1, 2, 3, 4, 5]
x = 3
y = 10
print(x in my_list)
print(y not in my_list)

a = [1, 2]
b = [1, 2]

print(a is b)
print(a == b)