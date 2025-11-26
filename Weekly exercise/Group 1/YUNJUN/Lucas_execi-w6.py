numbers=[3,7,2,9,4,1,8]
numbers.append(5)

numbers.remove(9)

numbers.sort()

numbers.reverse()

numbers.insert(2,6)

print(numbers.index(4))


my_tuple = (15, "Python", 3.14, True, 42, False)

print(my_tuple.index("Python"))  

print(my_tuple.count(True))   

print(my_tuple[1:5])    


student_marks = {
    "Alice": 88,   
    "Bob": 76,     
    "Jay": 92, 
    "Diana": 81,
    "Ethan": 69,
    "Fiona": 78,
    "Tony": 95,
    "Herry": 83,
    "Coke": 71,
    "Jerry": 89,
    "Kevin": 74,
    "Lily": 90,
    "Mia": 79,
    "Mike": 85,    
    "Sam": 77   
}

student_marks["Frank"] = 60

print("Student Marks:")
for name, mark in student_marks.items():
 print(f"{name}: {mark}")