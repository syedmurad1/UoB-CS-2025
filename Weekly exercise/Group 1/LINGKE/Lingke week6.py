numbers = [3,7,9,4,1,8]

numbers.append(5)

numbers.remove(9)
numbers.sort()
numbers.reverse()
numbers.insert(2,6)
print(numbers.index(4))
print (numbers)

# Ex 2
my_tuple = (15, "Python", 3.14, True, 42, False,True,True)

print(my_tuple.index("Python"))

print(my_tuple.count(True))

print(my_tuple[0:4])

# Exc 3
Marks_S = {
    "Name": ["Ali", "Moha", "Bilal", "Rakan"],
    "Score": [20, 48, 58, 30]
}
Marks_S["Name"].append("frank")
Marks_S["Score"].append(40)
print(Marks_S)