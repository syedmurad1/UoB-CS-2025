

#1
print("My", "Name", "Is", "King", sep="$$") # se necesitan comas entre palabras para usar un separador
print("My" "Name" "Is" "King", "", sep="!-!") #dos formas de hacer lo mismo
print("My" "Name" "Is" "King", end="!-!") 

#2
name1,name2,name3=input("Enter 3 names").split() #ejercicio con input 3 names y print por se parado
print("name1:",name1) # se necesita una coma
print("name2:",name2)
print("name3:",name3)

#3
x=3.142
print(f"{x:.3f}")    # Muestra 3.142 (3 decimales)
x=5.26459884
print(f"{x:.2f}",f"{x:.4f}",f"{x:.0f}",end="$" )

#4
year=2023
quantity=3
price=450
print(f" i have bought {quantity} footballs for {price*1000:,} in the year {year}")

#5
sentence="i have bought 3 footballs for 450.00, in the year 2023" #me pide el primer caracter"
print(sentence[0])

#6
sentence="I have bought 3 footballs"  #me pide el lenght 
print(len(sentence))

#7
from datetime import date #hay librerias que ya existen predeterminadas
date=date.today()
print(date)

#8
import random
print(random.randint(1,100))

#9
number1=int(input("Enter a number"))     #se debe poner int porque si no es un str y da error
number2=int(input("Enter a bigger number"))
import random
print(random.randint(number1,number2))

#10
number1=int(input("Enter a number"))     #se debe poner int porque si no es un str y da error
number2=int(input("Enter another number"))
print(number1+number2) #para que funcione sum se necesita una lista 

