list = [3, 7, 2, 9, 4, 1, 8]
print("The current list", list)

list.append(5)
print("List appended by 5", list)

list.remove(9)
print("The number 9 is removed", list)

list.sort()
print("The list is sorted", list)

list.reverse()
print("the list is reversed", list)

list.insert(2, 6)
print("Number 6 is inserted at the index of 2", list)

print("Index of number 4 is", list.index(4))

print("---------------------------------------------------")

my_tuple = (15, "Python", 3.14, True, 42, False)

print("The string \"Python\" is locate at index", my_tuple.index("Python"))
print("The value 'true' apperas", my_tuple.count(True), "times")
print("Elements from index 1 to index 4 are", my_tuple[1:5])

print("---------------------------------------------------")

dict = {
    "Lily": 100,
    "George": 60,
    "John": 75,
    "Amelia": 65,
    "Olivia": 70,
    "Harry": 60,
    "Ivy": 45,
    "Jack": 100,
    "Mia": 90,
    "Paul": 30,
    "Ringo": 60,
    "Oscar": 85,
    "Noah": 75,
    "Arthur": 100,
    "Sophia": 95,
}

dict["Frank"] = 60
print("The list of students and their marks with Frank added is", dict)

#5 Mutuble variables can be changed after they are assigned. However, immituable variables can't
#be changed once assinged and act like "constant" variables

#6 Local variables can be accessed only by the function where they are declared, but
#global variables can be accessed everywhere at any time. Local variables lifetime is bounded
#by the scope of the function or where they defined, but global variables lifetime is
#same as the program