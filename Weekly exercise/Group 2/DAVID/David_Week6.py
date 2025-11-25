#The following a list of integers: numbers = [3, 7, 2, 9, 4, 1, 8]

numbers = [3, 7, 2, 9, 4, 1, 8]
# print(numbers)

#Append the number 5 to the list.
numbers.append(5)
# print(numbers)

#Remove the number 9 from the list.
numbers.remove(9)
# print(numbers)

#Sort the list in ascending order.
# smallest = numbers[0]
# for i in range(numbers):
#     if i < smallest:
#         smallest = i
    
#     else:
#         print(smallest)

numbers.sort()
# print(numbers)

#Reverse the list after sorting it.
i = len(numbers) - 1

# while i >= 0:
#     print(numbers[i])
#     i -= 1

numbers.sort(reverse=True)
# print(numbers)

#Insert the number 6 at the index 2.
numbers.insert(2, 6)
print(numbers)

#Print the index of the number 4 in the list
print(numbers.index(4))

# The following code is immutable
# The following tuple of mixed data types: my_tuple = (15, "Python", 3.14, True, 42, False)
my_tuple = (15, "Python", 3.14, True, 42, False)

# Print the index of the string "Python".
x = my_tuple.index("Python")
print(my_tuple)
print(x)

# Count how many times the value True appears in the tuple.
print(my_tuple.count(True))

# Prints the elements from index 1 to index 4.
y = my_tuple[1:5]
print(y)

# Create a python dictionary representing the marks of students (at least 15 students) in a test.
pydic = {
            "Abubu" : 10,
         "Isabelle" : 20,
         "Jonas" : 7,
         "Targaryen" : 49, 
         "Gandalf" : 52, 
         "Leo" : 69,
         "Geralt" : 69, 
         "Hassan" : 80,
         "XORHAN" : 69,
         "Rehan" : 40,
         "Tibet" : 31,
         "Henry" : 1,
         "Donald" : 100,
         "Freddy" : 50,
         "Eminem" : 15
         }

print(pydic)

# Add a new student "Frank" with a mark of 60.
pydic["Frank"] = 60

# Print all student names and their corresponding marks.
print("Marks:\n")

for name, mark in pydic.items():
    print(f"{name} : {mark}")

#The Abubu Function :DDD
# print("Easter Egg")

