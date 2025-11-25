numbers=[3,7,2,9,4,1,8]
numbers.append(5)
numbers.remove(9)
numbers.sort()
numbers.reverse()
numbers.insert(2,6)
print(numbers.index(4))

my_tuple=(15,"Python",3.14,True,42,False)
print(my_tuple.index("Python"))
print(my_tuple.count(True))
print(my_tuple[1:5])

student_scores={
    "Alice": 88,
    "Bob": 75,
    "Charlie": 92,
    "David": 67,
    "Ella": 95,
    "William": 80,
    "Grace": 73,
    "Hannah": 85,
    "Ian": 90,
    "Jack": 78,
    "Kate": 83,
    "Leo": 91,
    "Mia": 87,
    "Nina": 76,
    "Oscar": 89
}
student_scores["Frank"]=60
print(student_scores)