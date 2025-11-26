# Ba Alawi-Week8.py
n1 = 3+4    # 7
n2 = 9-3   # 6
n3 = 3*5   # 15
n4 = 5/2   # 2.5
n5 = 11%3   # 2
n6 = 14 // 4  # 3  
n7 = 3**4   # 81
print(n1,n2,n3,n4,n5,n6,n7)

x = 18 
x += 2 #20 
x -= 10 #10
x *= 2 #20
x /= 5 #4
x %= 3 #1
print(x)

y = 16
y //= 7 #2
y **= 8 #2^8 = 256
print(y)

z = 5 # 0101 (binary)
z &= 3 # AND 0011 (binary)
z  #  0001 -> 1
print(z) # 1

z1 = 9 #1001
z1 |= 4 # OR 0100
print(z1) # 1101 -> 1+4+8=13

z2 = 12 # 1100
z2 ^= 9 # XOR 1001
print(z2) # 0101 -. 4+1 = 5

z3 = 13 # 0000-1101
z3 >>= 1 # moves right one step 0000-0110 2+4 = 6
z3 <<=2 # moves left two steps 0001-1000 8+16 = 24

print(z3 := 27) # 27

A = 19
B = 29
print(A==B) #False
print(A!=B) #True
print(A<=B) #True
print(A>=B) #False
print(A>B) #False
print(A<B) #True

C = 7
print(C>5 and C<9) #True
print(C>5 or C<2) #True
print(not(C>5 and C<9)) #False

D = 19
E = 25
print(D is E) #False
print(D is not E) #True

F = ["Ali", "Khalid"]
print("Khalid" in F) #True
print("Moha" not in F) #True

print(15 & 19) # 15 - 0000-1111 & 19 - 0001-0011 -> 0000-0011 = 3
print(15 | 19) # 15 - 0000-1111 OR 19 - 0001-0011 -> 0001-1111 = 16+8+4+2+1 = 31
print(15 ^ 19) # 15 - 0000-1111 XOR 19 - 0001-0011 -> 0001-1100 = 16+8+4 = 28
print(15 << 1) # 15 - 0000-1111 left 1 step -> 0001-1110 = 16+8+4+2 = 30
print(15 >> 2) # 15 - 0000-1111 right 2 steps -> 0000-0011 = 2+1 = 3

a = 10
a += 5
a -= 3
a *= 2
a //= 4
print(a) # 6

b=7
c=12
print(b<c) # Ture
print(b>c) # False
print(b<c and b!=c) # Ture
print(b<c or c<10) # Ture


my_list = [1, 2, 3, 4, 5]
print(3 in my_list) # Ture
print(10 in my_list) # False


m = [1, 2]
n = [1, 2]

print(m is n) # False
print(m == n) # Ture