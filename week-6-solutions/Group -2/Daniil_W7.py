list1 = [3,7,2,9,4,1,8]
list1.append(5)
list1.remove(9)
list1.sort()
list1.reverse()
list1.insert(2,6)
print(list1.index(4))

my_tuple = (15, "Python", 3.14, True, 42, False)
print(my_tuple.index("Python"))
print(my_tuple.count(True))
for i in range(1,5):
    print(my_tuple[i])

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}
students["Frank"] = 60
print(students)
