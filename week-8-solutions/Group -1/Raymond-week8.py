a=3
b=4
print(a+b)
print(a-b)
print(a*b)
print(f"{a/b:.2f}")
print(a%b)
print(a**b)
print(a//b)

c=6
print(c)
c+=3
print(c)
c-=3
print(c)
c*=2
print(c)
c/=2
print(c)
c%=6
print(c)
c//=2
print(c)
c**=3
print(c)

c=int(c)
c^=3
print(c)
c>>=1
print(c)
c<<=2
print(c)

x=4
y=8
print(x==y)
print(a!=b)
print(y>x)
print(x<y)
print(y>=x)
print(x<=y)

d=int(input())
if d==5 and d<10:
 print(f"d is 5 and d is smaller than 10")
 if d==5 or d>10:
   print(f"d is 5 or d is greater than 10")
if not d<6:
  print(f"d is not smaller than 6")

e=[1,2,3]
f=[1,2,3]
print("e is f:", e is f)
print("e is not f:", e is not f)

balls=["basketball","football","volleyball" ]
print("'basketball' is in balls:", "basketball" in balls)
print("'baseball' is in balls", "baseball" not in balls)

a=3
b=9
print("a & b =", a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>1)

a=10
a-=3
a*=2
a/=4
print(a)

p=7
q=12
print("p is greater than q:", p>q)
print("p is less than or equal to q", p<=q)
print(f"p is less than q and p is not equal to q {(p<q) and (p!=q)}")
print(f"p is greater than q or q is greater than 10 {(p>q) or (q>10)}")

my_list=[1,2,3,4,5]
print("3 is in my_list", 3 in my_list)
print("10 is not in my list", 10 not in my_list)

A=[1,2]
B=[1,2]
print("A is B", A is B)
print("A is B", A==B)