numbers = [3, 7, 2, 9, 4, 1, 8] #question 2
numbers.append(5)
numbers.remove(9)
numbers.sort()
numbers.reverse()
numbers.insert(2, 6)
print(numbers.index(4))

my_tuple = (15, "Python", 3.14, True, 42, False) #question 3
print(my_tuple.index("Python"))
my_tuple.count(True)
print(my_tuple[1:5])

test_marks = {        #question 4
    "Hassan": 75,
    "Karim": 60,
    "Mohamed": 80,
    "Omar": 85,
    "Ali": 90,
    "Sarah": 78,
    "Lina": 88,
    "Youssef": 72,
    "Nora": 95,
    "Ahmed": 67,
    "Maya": 82,
    "John": 59,
    "Layla": 93,
    "Ziad": 70,
    "Hoda": 100
    }
test_marks["Frank"]= 60
print(test_marks)

age = 18     # question 5
print(id(age))
age = age + 1
print(id(age)) 
# because intger variables are immutable, when i change the value of age the computer created another location for age with a new unique id
scores = [1, 2, 3]
print(id(scores))
scores.append(4)
print(id(scores))
# because list variables are mutable, when i append the list the computer will not create another ocation for scores, rather edit the current value and the id remains the same



student_name = "hassan" #global variable.  #question 6

def school():
  print("enrolled student name is " + student_name)

school()

def my_name_is():
     print("my name is " + student_name)
my_name_is()    
# I was able to pass the same global variable to 2 functions because it is global(recognised evrywhere)

def country():
  country_name = "Egypt"
  print(country_name)

country()

def call_local_variable():
  print(country_name)

call_local_variable()
# The local variable: country_name was not accesible since it is local(not recognised outside its function)

