list = [3,7,2,9,4,1,8]
print(list)

list.append(5)
print(list)

list.remove(9)
print(list)

list.sort(reverse = False)
print(list)

list.insert(2, 6)
print(list)

print(list[4])



my_tuple = (15, "Python", 3.14, True, 42, False)

print(my_tuple[1])

print(my_tuple.count(True))

print(my_tuple[0:4])



student_marks = {
    "A": 85,"B": 78,"C": 92,"D": 66,"E": 74,"G": 88,"H": 59,"I": 91,"J": 83,"K": 70,"L": 95,"M": 82,"N": 77,"O": 89,"P": 68
}

student_marks["Frank"] = 60


for student, mark in student_marks.items():
    print(f"{student}: {mark}")