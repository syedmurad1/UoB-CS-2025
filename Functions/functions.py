

def sayHi():
  print("Hello")

sayHi()
sayHi()



def sayHi(name,k):
  print("Hello " + name)

sayHi("iusrhoihsgpihgsphogisghpdf","tom")


# def my_function2():
#     z=2+5
#     # return z

# print(my_function2())



# def my_function2():
#     z=4+5
#     y=z
#     return z,y

# print(my_function2())


# def my_function(x):
#     return 5 * x

# print(my_function(2))



# def outer():
#     print("This is the outer function.")
#     def inner():
#         print("This is the inner function.")
#     inner()


# outer()


def my_fun(*city):
    print(f"I Love {city}")

my_fun('Bristol', 'London', 'York')

# my_fun('Bristol', 'London', 'York')


# def my_fun(*city):
#     print(f"I Love {city[2]}" )

# my_fun('Bristol', 'London', 'York')






def my_fun(*city):
    print("I Love" )
    for i in city:
        print(f"{i}")

my_fun('Bristol', 'London', 'York')




def my_function(**name):
    print("His last name is " + name["lname"])

my_function(lname = "Murad", fname = "Syed" , age = 24)




def my_function(uname, **details):
  print("Username:", uname)
  print("Details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("tom55", age = 999, city = "Bristol", hobby = "coding")