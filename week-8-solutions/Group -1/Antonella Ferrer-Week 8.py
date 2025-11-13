#1 

print(5+5) #addition
print(10-5) #substraction
print(10*5) #multiplication
print(10/2) #divition
print(10%100) #Módulo = el sobrante de una división 
print(5**2) #exponent 
print(100//3) # floor divition, it removes decimals 

#2

x=10
print(x) #asigna el valor de x a un numero 
x = 10
x += 5 # x = x + 5  el signo es += toma el valor de x y lo opera con suma
print(x)   # 15
x = 10
x -= 5  # x = x - 5 toma el valor de x y lo opera con restas
print(x)   # 5
x = 10
x *= 5  # x = x * 5  toma el valor de x y lo opera con multiplicacion
print(x)   # 50
x = 10 
x /= 5   # x = x / 5  toma el valor de x y lo opera con division 
print(x)   # 4.0
x = 10
x %= 3   # x = x % 3 → resto = 1 porque 10/3= 3 (sin decimales) 3*3=9 10-9=1
print(x)   # 1
x = 10
x //= 3  # x = x // 3 → parte entera lo toma sin los decimales
print(x)   # 3
x = 10
x **= 5  # x = x ** 3  
print(x)   # 8

#Bit a bit= rabajan directamente con los bits (0 y 1) usan el metodo binario 
print(10 & 5)   # 0 AND lo questa haciendo es basicamente ver si tienen algo en comun cuando son binarios 
print(10 | 5)   # 15 OR combina los dos numeros 
print(10 ^ 5)   # 15  XOR combina las partes diferentes ? 
print(10 ^ 10) 
print(10 << 1)   # 20  multiplica por 2 se desplaza 2 a la izquierda 
print(10 >> 1)   # 5 divide por dos se desplaza 2 a la derecha

#3
a = 10
b = 5
print(a == b)  # Equal to False, because 10 is not equal to 5
print(a != b) # Not equal to True, because 10 is different from 5
print(a > b)  # Greater than True, because 10 is greater than 5
print(a < b)  # Less than False, because 10 is not less than 5
print(a >= b)  # Greater than or equal toTrue, because 10 is greater than 5
print(a <= b)  # Less than or equal to,False, because 10 is not less than or equal to 5 

#4
x = True
y = False
print(x and y) # AND: True if both are True
print(x or y) # OR: True if at least one is True
print(not x) # NOT: Inverts the Boolean value
print(not y)  

#5
a = 10
b = 10
c = 15
print(a is b)  # True (same number)
print(a is c)  # False
print(a is not b)  # False (same number)
print(a is not c)  # True

#6
print(10 in [1, 2, 3])      # False
print("10" not in [1,2,3]) #True 

#7
a = 10   # 1010
b = 5    # 0101
print(a & b)   # 0 AND
print(a | b)   # 15 OR
print(a ^ b)   # 15 XOR
print(~a)# -11  complemento (lo opuesto en numero binario)
print(a << 1)   # 20 x2 
print(a << 2)   # 40 x4
print(a >> 1)   # 5  /2
print(a >> 2)   # 2  /4

#8
a=10
a+=5
a-=3
a*=2
a//=4
print(a)

#9
x=7
y=12
print(x>y)
print(x<=y)
print(x<y and x!=y)  #Cuando tengo que hacer dos simultaneos se escribe and/ or etc sin coma ni nada
print(x>y or y>10)

#10
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(10 not in my_list)

a = [1, 2]
b = [1, 2]
print(a is b) # Falso porque a pesar de que tienen los mismos numeros no son las misma variable
print(a == b)
