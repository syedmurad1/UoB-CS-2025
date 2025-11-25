
#ex 3 i made it by making a dict
football = {
            "year":2023 , 
            "quantity": 3 , 
            "price": 450.00
}

print(f"I have bought {football['quantity']} footballs for {football['price']:.2f} £, in the year {football['year']}")

sentence = "I have bought 3 footballs for 450.00 £, in the year2023"

character = sentence[0]

print(f"the first character is {character}")



sentence2 = "I have bought 3 footballs "

length = len(sentence2)


import datetime
today = datetime.datetime.now()
print(today)



import random
randomize = random.randint(1,100)
print(randomize)

num1 = int(input("please  enter num1"))
num2 = int(input("please enter num2 "))
randomize2 = random.randint(num1,num2)
print(randomize2)

print(num1 + num2)